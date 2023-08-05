![](petrified-forest.jpg)

> "They took all the trees, and put em in a tree museum...
>  And they charged the people a dollar and a half to see them"
>    — Joni Mitchell, "Big Yellow Taxi"

Boosted decision trees are widely used in HEP, particularly in data analyses for
making complex, multivariate nested cuts to separate signal events from background ones.

While powerful, the complexity of their training makes BDT (and therefore
analysis) preservation troublesome: BDTs get stored in different formats, which
may not be forwards-compatible with future versions of their framework
libraries. So now we start talking about dragging around Docker containers just
to make sure the right _version_ of the right framework is used. Plus those
libraries have to be included in any user code, adding unwelcome dependencies
and complexity, and perhaps even being incompatible with the target language
(e.g. applying a BDT from a Python framework in a C++ application).

This is ridiculous, because BDTs are actually absurdly simple objects. The
framework complexity is needed for training, but not for execution. This package
provideds a set of utilities for converting sklearn and TMVA boosted decision
trees, for either classification or regression, from their custom formats to
vanilla C++ and Python code that has _no_ dependencies, can be safely used
forever without risk of format or framework breaking-changes, and by virtue of
being static code can execute more quickly and with less memory overhead than
the original form.
