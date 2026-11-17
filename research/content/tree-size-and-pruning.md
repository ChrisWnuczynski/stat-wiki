## Motivating example
A regression tree can isolate individual training responses in tiny leaves and drive its training sum of squares towards zero. Such a tree also learns accidental variation in the sample. Choosing its size asks how much of the fitted detail is likely to predict new responses. Growing a generous tree and then comparing subtrees allows a useful branch to survive even when its first split is only a gateway to a later improvement.{{cite:loh2011_trees}} (pp. 14–15, “Classification Trees”)

## Definition — Risk plus a charge for leaves
For leaves $m$ containing $n_m$ of the $n$ training observations, a sample-weighted impurity criterion is
$$R(T)=\sum_{m\in\mathcal L(T)}\frac{n_m}{n}I(m),\qquad R_\alpha(T)=R(T)+\alpha|\mathcal L(T)|.$$
For squared-error regression, $R(T)$ may instead be a sum or average of squared errors; the units of $\alpha$ must match that risk. The penalty prices model size, not depth directly. A long narrow tree and a balanced tree can have the same number of leaves.{{cite:loh2014_trees}} (§2.1, p. 331, CART pruning)

A split replaces a leaf by two children. Its reduction in weighted impurity is the parent's weighted impurity minus the children's weighted impurities. Summing those reductions throughout the tree telescopes: every intermediate-node term cancels, leaving root impurity minus total leaf impurity. This identity requires consistent sample weights. An unweighted sum of average leaf impurities measures something else.

## Properties — Comparing a branch with its collapse
Let $T_t$ be a branch rooted at node $t$ with $L_t>1$ leaves. Suppose its unpenalised risk is $R(T_t)$ and replacing it by one leaf gives $R(t)$. The two penalised risks agree when
$$\alpha_t=\frac{R(t)-R(T_t)}{L_t-1}.$$
For larger $\alpha$ the collapsed leaf is preferable; for smaller $\alpha$ the branch is preferable. This is the branch's average risk improvement per extra leaf. Weakest-link pruning repeatedly removes branches with the smallest such ratio and generates a nested sequence of candidates.{{cite:loh2014_trees}} (§2.1, p. 331)

The criterion compares complete subtrees of the grown tree. It does not promise to search every possible tree structure in the input space. An early greedy split can exclude a structure that would predict better. Pruning controls size conditional on the grown structure, while split selection and size selection remain different choices.{{cite:loh2011_trees}} (pp. 14–15, recursive splitting and pruning)

## Worked example — A lower envelope of three candidates
Suppose three candidate regression trees have leaf counts $1,3,5$ and total training squared errors $20,8,4$. Their penalised scores are $20+\alpha$, $8+3\alpha$, and $4+5\alpha$. The five-leaf and three-leaf scores cross at $\alpha=2$; the three-leaf and one-leaf scores cross at $\alpha=6$. Thus the best among these candidates has five leaves for $0\le\alpha<2$, three for $2<\alpha<6$, and one for $\alpha>6$, with ties at the boundaries.

The one- versus five-leaf scores also cross at $\alpha=4$, but neither is best there: the three-leaf score is $20$, whereas each other score is $24$. Pairwise intersections alone do not identify the pruning choice; the lower envelope of all candidate scores does.

**Your turn.** A four-leaf branch has squared error $6$. Collapsing it to one leaf gives squared error $15$. Find its critical penalty. Which option wins at penalties $2$ and $4$?

::: {.callout-tip collapse="true" title="Answer"}
The threshold is $(15-6)/(4-1)=3$. At penalty $2$, the branch scores $6+8=14$ and the collapsed leaf scores $15+2=17$, so the branch wins. At penalty $4$, the scores are $22$ and $19$, so collapse wins.
:::

## Statistical use — Select size without reusing the assessment data
Cross-validation compares prediction errors of candidate sizes on observations excluded from their fitting folds. Its selected minimum is itself chosen using those errors, so the minimum is not an independent assessment of the final selected model. A separate test set, or an outer validation loop, assesses the whole selection procedure. A smaller candidate within one standard error of the minimum is a common simplicity rule; it trades a little estimated accuracy for a smaller tree.{{cite:loh2011_trees}} (pp. 14–15, cross-validation pruning)

In `rpart`, `cp` scales a risk improvement relative to root risk and also restricts tree growth. To compare very small leaves on the iris petal plane, specify their size controls as well as `cp`. With `minsplit=2`, `minbucket=1`, and no cross-validation during this comparison, `cp=0.1` and `cp=0.001` give three and seven leaves respectively. Under default minimum-node controls both fits have three leaves. Decreasing `cp` permits more detail; it does not force another split.{{cite:rpart_longintro2023}} (§4.1, complexity parameter; §6.1, program options)

## Assumptions and limits
No penalty is universal across differently scaled losses or different samples. Classification misclassification risk, Gini impurity and entropy may rank pruning candidates differently. Also, identical input rows with conflicting class labels cannot be separated by deterministic splits on those inputs, so even a maximally grown tree need not achieve zero training error. Report the loss, size controls, validation design and selected tree size together.

## Connections — A pruned tree and a forest
A random forest averages trees built from perturbed training samples and random feature choices. Its component trees can be grown deeply without applying the single-tree pruning choice to each tree. Averaging and pruning address different aspects of prediction: pruning limits the complexity of an individual tree, while randomisation and averaging can reduce the sensitivity of the ensemble to the particular training sample. The number of trees is also distinct from the number of leaves in each tree.{{cite:breiman2001_rf}} (§§3–4, tree construction and out-of-bag assessment)

A complexity penalty chooses among trees by charging for extra leaves. Averaging many deep trees is a different operation and does not apply that charge inside each tree.
