#! /usr/bin/env python
# -*- python -*-

"""\
Translate a TMVA boosted decision tree classifier to C++

TODO:
 - Multi-class BDT support
 - Make the dummy main functions read arg vectors from argv
"""

from __future__ import print_function
from math import sqrt
from array import array
import textwrap


def printNodes(node, depth=0):
    nodetype = node.GetNodeType()
    if nodetype == 1:
        nodestr = "SIG<type={}>".format(nodetype)
    elif nodetype == -1:
        nodestr = "BKG<type={}>".format(nodetype)
    else:
        nodestr = "DECISION<type={}, cutidx={}, cutval={}, cutdir={}>".format(
              nodetype, node.GetSelector(), node.GetCutValue(), node.GetCutType())
    print(depth*"  " + nodestr)
    if node.GetNodeType() == 0:
        printNodes(node.GetLeft(), depth+1)
        printNodes(node.GetRight(), depth+1)


def mkcxxiftree(node, depth=0, regression=False):
    nodetype = node.GetNodeType()
    indent = depth * "  "

    cout = ""
    if nodetype != 0: # leaf node
        cout += "{}return {};".format(indent, node.GetResponse() if regression else nodetype)
    else: # decision node
        cmp = ">=" if node.GetCutType() else "<"
        if node.GetNFisherCoeff() == 0: # cut on raw feature
            cout += indent + "if (args[{}] {} {}) {{\n".format(node.GetSelector(), cmp, node.GetCutValue())
        else: # cut on a Fisher discriminant (= linear combination of features)
            if regression:
                print("Fisher cut used for regression!?") #< throw a more controlled / less repetitive warning?
            cutvalstr = str( node.GetFisherCoeff(node.GetNFisherCoeff()-1) )
            for ivar in range(node.GetNFisherCoeff()-1):
                cutvalstr += " + {}*args[{}]".format(node.GetFisherCoeff(ivar), ivar);
                cout += indent + "double fisher = {};\n".format(cutvalstr)
                cout += indent + "if (fisher {} {}) {{\n".format(cmp, node.GetCutValue())
        cout += mkcxxiftree(node.GetRight(), depth+1, regression)
        cout += "\n{}}} else {{\n".format(indent)
        cout += mkcxxiftree(node.GetLeft(), depth+1, regression)
        cout += "\n{}}}".format(indent)

        return cout


def mkpyiftree(node, depth=0, regression=False):
    nodetype = node.GetNodeType()
    indent = depth * "  "

    cout = ""
    if nodetype != 0: # leaf node
        cout += "{}return {}\n".format(indent, node.GetResponse() if regression else nodetype)
    else: # decision node
        cmp = ">=" if node.GetCutType() else "<"
        if node.GetNFisherCoeff() == 0: # cut on raw feature
            cout += indent + "if args[{}] {} {}:\n".format(node.GetSelector(), cmp, node.GetCutValue())
        else: # cut on a Fisher discriminant (= linear combination of features)
            if regression:
                print("Fisher cut used for regression!?") #< throw a more controlled / less repetitive warning?
            cutvalstr = str( node.GetFisherCoeff(node.GetNFisherCoeff()-1) )
            for ivar in range(node.GetNFisherCoeff()-1):
                cutvalstr += " + {}*args[{}]".format(node.GetFisherCoeff(ivar), ivar);
                cout += indent + "fisher = {}\n".format(cutvalstr)
                cout += indent + "if fisher {} {}:\n".format(cmp, node.GetCutValue())
        cout += mkpyiftree(node.GetRight(), depth+1, regression)
        cout += indent + "else:\n"
        cout += mkpyiftree(node.GetLeft(), depth+1, regression)
    return cout


def dt_to_cpp(tree, dtname="decision", regression=False, inline=True):
    rtntype = "double" if regression else "int"
    inline = "inline " if inline else ""
    cout = "template <typename C=std::vector<double>>\n"
    cout += "{}{} {}(const C& args) {{\n".format(inline, rtntype, dtname)
    cout += mkcxxiftree(tree.GetRoot(), 1, regression)
    cout += "\n}"
    return cout


def dt_to_py(tree, dtname="decision", regression=False):
    cout = "def {}(args):\n".format( dtname)
    cout += mkpyiftree(tree.GetRoot(), 1, regression)
    return cout



def main():
    import argparse
    ap = argparse.ArgumentParser(__doc__)
    ap.add_argument("FILE", help="XML file containing the BDT weights")
    ap.add_argument("VARNAMES", nargs="?", default=None, help="comma-separated names of input variables")
    ap.add_argument("-n", "--name", dest="NAME", default="decision", help="name to use for the output function and source file [default=%(default)s]")
    ap.add_argument("-r", "--regression", dest="REGRESSION", action="store_true", default=False, help="return values for regression, rather than labels for classification")
    ap.add_argument("-v", "--verbose", dest="VERBOSE", action="store_true", default=False, help="print the resulting source code")
    ap.add_argument("-l", "--lang", dest="LANG", default="c++", help="what langauge to write the output as: c++ or py [default=%(default)s]")
    ap.add_argument("--no-inline", dest="INLINE", action="store_false", default=True, help="don't make the DT functions inline for C++")
    ap.add_argument("--main", dest="MAIN", action="store_true", default=False, help="add a main function for trivial testing")
    args = ap.parse_args()

    try:
        from ROOT import TFile, TTree, TMVA
    except ImportError:
        print("{} requires the ROOT Python module to be installed", ap.prog)

    ## Manually parse the XML file to obtain the variable names
    varnames = []
    if not args.VARNAMES:
        import xml.etree.ElementTree as ET
        xtree = ET.parse(args.FILE)
        xvars = xtree.getroot().find("Variables")
        for xvar in xvars.findall("Variable"):
            varnames.append( xvar.get("Label") )
    else:
        varnames = args.VARNAMES.split(",")
    print(varnames)


    ## Load the BDT into TMVA, using the discovered variables
    TMVA.Tools.Instance()
    reader = TMVA.Reader("!Color:!Silent")
    bdtvars = { name : array('f', [0]) for name in varnames }
    for varname in varnames:
        reader.AddVariable(varname, bdtvars[varname])
    reader.BookMVA("MyBDT", args.FILE)
    bdt = reader.FindMVA("MyBDT")

    ## DEBUG PRINTOUTS FOR TREE 1
    # print(bdt, type(bdt), "", sep="\n")
    # t0 = bdt.GetForest()[0]
    # print(t0, type(t0), sep="\n")
    # print()
    # printNodes(t0.GetRoot())
    # print()
    # print(dt_to_cpp(t0))


    ## Generate the set of individual decision trees
    boostweights = bdt.GetBoostWeights()
    couts, treefns = [], []
    for it, tree in enumerate(bdt.GetForest()):
        treefn = "{}_{:03d}".format(args.NAME, it)
        treefns.append(treefn)
        if args.LANG == "c++":
            tree = dt_to_cpp(tree, treefn, args.REGRESSION, args.INLINE)
        if args.LANG == "py":
            tree = dt_to_py(tree, treefn, args.REGRESSION)
        couts.append(tree)


    ## Set the language-specific parts, and add top-level functions that sum over tree output-node values
    inline = "inline " if (args.LANG == "c++" and args.INLINE) else ""
    sumstr = " + ".join("{}*{}(args)".format(w, tf) for (w,tf) in zip(boostweights, treefns))

    if args.LANG == "c++":
        ext =".cc"
        cout = "#include <vector>\n"
        if args.MAIN:
            cout += "#include <iostream>\n"
        cout += "\n"

        btree = """\
        template <typename C=std::vector<double>>
        {inline}double {bdtname}(const C& args) {{
          return ({sumstr}) / {norm};
        }}""".format(inline=inline, bdtname=args.NAME, scale=1.0, sumstr=sumstr, norm=sum(boostweights))

    elif args.LANG == "py":
        ext =".py"
        cout = "#! /usr/bin/env python\n"
        if args.MAIN:
            cout += "from __future__ import print_function\n"
        cout += "\n"
        btree = """\
        def {bdtname}(args):
          return ({sumstr}) / {norm}
        """.format(bdtname=args.NAME, scale=1.0, sumstr=sumstr, norm=sum(boostweights))

    couts.append(textwrap.dedent(btree))
    cout += "\n\n".join(couts)


    ## Add a main function for testing (in C++'s case, needed to test compiled-object size)
    if args.MAIN:
        if args.LANG == "c++":
            mainfn = textwrap.dedent("""\
            int main() {{
              std::vector<double> args(1.0, {nargs});
              double x = {bdtname}(args);
              std::cout << x << std::endl;
              return bool(x);
            }}
            """.format(nargs=len(varnames), bdtname=args.NAME))

        elif args.LANG == "py":
            mainfn = textwrap.dedent("""\
            if __name__ == "__main__":
                args = {args}
                x = {bdtname}(args)
                print(x)
            """.format(args=list(range(len(varnames))), bdtname=args.NAME))

        cout += "\n\n" + mainfn


    ## Output to terminal and file
    if args.VERBOSE:
        print(cout)
    with open(args.NAME + ext, "w") as f:
        f.write(cout)


if __name__ == "__main__":
    main()
