#! /usr/bin/env python3

"""\
Translate a SKL decision tree classifier to C++
"""

import textwrap

def dt_to_cpp(estimator, dtname="decision", regression=False):
    """\
    Turn the given estimator into a standalone C++ source string, using the given function name.

    TODO: enable passing in a set of node values for regression/score use.
    """

    ## Parallel arrays containing tree structure
    n_nodes = estimator.tree_.node_count
    children_left = estimator.tree_.children_left
    children_right = estimator.tree_.children_right
    feature = estimator.tree_.feature
    threshold = estimator.tree_.threshold
    values = estimator.tree_.value

    rtntype = "double" if regression else "int"

    cout = f"""\
    template <typename C=std::vector<double>>
    {rtntype} {dtname}(const C& args) {{"""
    if regression:
        valstr = ", ".join([("%.8g" % v) for v in values[:,0,0]]) #< TODO: robust? + flatten non-leaf values
        cout += f"""
      static const double values[{n_nodes}] = {{ {valstr} }};"""
    cout += """
      int inode = 0;
      while (1) {
        switch (inode) {"""

    for inode in range(n_nodes):
        ival = feature[inode]
        thres = threshold[inode]
        ileft = children_left[inode]
        iright = children_right[inode]
        cout += f"\n        case {inode}:"
        if children_left[inode] == children_right[inode]:
            if regression:
                cout += f"\n          return values[{inode}];"
            else:
                cout += f"\n          return {inode};"
        else:
            cout += f"\n          inode = (args[{ival}] <= {thres}) ? {ileft} : {iright}; break;"

    cout += """
        }
      }
      return -1;
    }
    """
    return textwrap.dedent(cout)


def main():

    import argparse
    ap = argparse.ArgumentParser(__doc__)
    ap.add_argument("FILE", nargs="?", help="pickle or joblib file containing the decision tree model")
    ap.add_argument("-n", "--name", dest="NAME", default="decision", help="name to use for the output function and source file [default=%(default)s]")
    ap.add_argument("-v", "--verbose", dest="VERBOSE", action="store_true", default=False, help="print the resulting source code")
    args = ap.parse_args()

    try:
        from sklearn.tree import DecisionTreeClassifier
    except ImportError:
        print("{} requires the ROOT Python module to be installed", ap.prog)

    estimator = None
    if args.FILE is None:
        ## Demo with SKL Iris dataset
        print("No model given: training a demo BDT on the SKL Iris test data")
        from sklearn.model_selection import train_test_split
        from sklearn.datasets import load_iris
        iris = load_iris()
        X = iris.data
        y = iris.target
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
        estimator = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
        estimator.fit(X_train, y_train)
        print(type(estimator))
        cout = dt_to_cpp(estimator, args.NAME)

    elif args.FILE.endswith(".pkl"):
        import pickle
        with open(args.FILE, "rb") as f:
            estimator = pickle.load(f)
        print(type(estimator))
        cout = dt_to_cpp(estimator, args.NAME)

    elif args.FILE.endswith(".xml") or args.FILE.endswith(".job"): #< NOT XML!!
        import joblib
        gbclassifier = joblib.load(args.FILE)
        print(type(gbclassifier))
        print(type(gbclassifier.estimators_))
        print("NEstimators", len(gbclassifier.estimators_))
        print("NFeatures", gbclassifier.n_features_)
        print("NClasses", gbclassifier.n_classes_)
        print("Classes", gbclassifier.classes_)
        # estimators = gbclassifier.estimators_[0,0]
        couts = []
        for icls in range(1): #self.n_classes):
            treefns = []
            for iest in range(gbclassifier.n_estimators):
                estimator = gbclassifier.estimators_[iest, icls]
                # print(icls, iest, type(estimator))
                tree = estimator.tree_
                treefn = "{}_{:03d}_{:03d}".format(args.NAME, iest, icls)
                tree_cc = dt_to_cpp(estimator, treefn, True)
                treefns.append(treefn)
                couts.append(tree_cc)

            # Sum over tree output-node values, based on
            #   def predict_stages ->
            #   cdef void _predict_regression_tree_inplace_fast_dense
            # from sklearn ensemble/_gradient_boosting.pyx:
            #   out[i * K + k] += scale * value[node - root_node]
            # ~ out[k] += scale * tree.value
            sumstr = " + ".join("{}(args)".format(tf) for tf in treefns)
        btree_cc = """\
    template <typename C=std::vector<double>>
    double {bdtname}(const C& args) {{
      return {scale}*({sumstr});
    }}""".format(bdtname=args.NAME, scale=gbclassifier.learning_rate, sumstr=sumstr)
        couts.append(textwrap.dedent(btree_cc))
        cout = "\n\n".join(couts)

    cout = "#include <vector>\n\n" + cout
    if args.VERBOSE:
        print(cout)
    with open(args.NAME + ".cc", "w") as f:
        f.write(cout)


if __name__ == "__main__":
    main()
