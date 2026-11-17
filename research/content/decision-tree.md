## Motivating example

A clinic wants to classify patients using age and a blood measurement. A tree can first ask whether the measurement exceeds a threshold, then ask about age only within the group where age helps. The result is a set of regions with a local prediction in each. The simple rules are useful to explain, but the threshold choices depend on the training sample; a tree needs an explicit rule for growing and limiting those regions.

## Intuition — Why a sequence of splits partitions predictors

A decision tree repeatedly divides predictor space. For numerical predictors, one split asks whether a single coordinate is below a cutoff, so a path from root to leaf defines an axis-aligned rectangle, possibly unbounded. Each classification leaf predicts its most frequent training class, while a regression leaf commonly predicts its training mean. A class may occupy several disconnected leaves; the displayed rule list, not a single smooth equation, describes the fitted classifier.

The same partition has two readings. Geometrically it draws boundaries; operationally it asks a sequence of questions of each new case. Both readings matter: the first reveals limits such as difficulty approximating a diagonal boundary, while the second makes individual predictions traceable.

## Definition

At a node containing training indices $R$, a candidate split divides them into $R_L$ and $R_R$ by a condition such as $x_j<c$. For classification, write $\hat p_{Rg}$ for the proportion of class $g$ in $R$. An impurity measure $I(\hat p_R)$ scores the mixture, and the weighted improvement is

$$
\Delta I=I(\hat p_R)-\frac{|R_L|}{|R|}I(\hat p_{R_L})-\frac{|R_R|}{|R|}I(\hat p_{R_R}).
$$

A greedy tree chooses a split with the largest current improvement among its candidates, then repeats within the children. This choice examines the immediate children, not all trees that might grow beneath them. Identical predictor vectors with conflicting labels cannot be separated by deterministic splits on those predictors.{{cite:hastie_esl2009}} (§9.2, pp. 305–310)

## Properties — Choosing a split

For two classes, the Gini impurity is $G(p)=2p(1-p)$, where $p$ is the class-one proportion. It equals zero in a pure node and reaches $1/2$ at a fifty-fifty mixture. Cross-entropy, $-p\log p-(1-p)\log(1-p)$ with $0\log0=0$, is another smooth criterion. The misclassification impurity $\min(p,1-p)$ directly counts the minority proportion, yet can be insensitive to a useful intermediate separation. If both children still have the parent's majority class, their weighted misclassification impurities equal the parent's, even when their class proportions have moved apart. Gini or entropy detects that movement.{{cite:hastie_esl2009}} (§9.2, pp. 305–310)

For a numerical predictor, only gaps between consecutive distinct observed values can produce different training partitions. A midpoint is a conventional representative of each gap; the training impurity does not identify one unique threshold inside it. A new observation in the gap can therefore be classified differently by another equally scoring cutoff. For an unordered categorical predictor, candidate subsets of levels replace numerical thresholds. One must account for the number and arrangement of candidate splits when comparing variables with very different numbers of possible cuts.

## Interpretation

The fraction of each class in a leaf is a local empirical estimate of its class probability. It is constant across that entire leaf even if the true probability varies within it. A majority-class label minimizes the empirical zero–one loss within the leaf, but leaf proportions can be poorly calibrated if the leaf is small or the tree was selected on the same cases.

For concave impurity functions such as Gini and entropy, the parent proportions equal the size-weighted average of the child proportions, so the weighted impurity cannot increase after a split. This is a statement about training impurity, not future prediction error. A single noisy case can create a pure leaf, lower training impurity and worsen prediction on new cases. Rescaling one numerical variable by a strictly increasing affine transformation preserves the partitions because it preserves the ordering of its values. Rotating several predictors changes the available axis-aligned cuts.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
If $w=|R_L|/|R|$, counting class $g$ on both sides yields $\hat p_{Rg}=w\hat p_{R_Lg}+(1-w)\hat p_{R_Rg}$. Concavity gives $I(\hat p_R)\geq wI(\hat p_{R_L})+(1-w)I(\hat p_{R_R})$, hence $\Delta I\geq0$. In particular $G(p)=2p(1-p)$ has second derivative $-4$, and binary entropy has second derivative $-1/[p(1-p)]$ for $0<p<1$. If the same class is the majority in parent and children, and $p,p_L,p_R$ are its proportions, the weighted misclassification rate equals $w(1-p_L)+(1-w)(1-p_R)=1-p$; thus its improvement is zero. Within a leaf with $n_g$ cases in class $g$, predicting $g$ makes $n-n_g$ training mistakes, minimized by a largest $n_g$. Finally, inequalities $x_j<c$ and $x_j\ge c$ intersect along a root-to-leaf path to form coordinate intervals; their Cartesian product is an axis-aligned rectangular leaf region.
:::
:::

## Statistical use — Controlling tree size

If splitting continues until leaves are pure, a tree can memorize distinct training points. A minimum leaf size, maximum depth, or pruning rule limits this. Cost-complexity pruning scores a subtree $T$ by its sample-weighted leaf risk $R(T)$ plus $\alpha|T|$, where $|T|$ is its number of leaves and $\alpha\geq0$. Increasing $\alpha$ charges more for each extra leaf. A validation set or cross-validation can choose the penalty using predictive loss, while an untouched test set can estimate performance after that choice. The loss used to grow a tree, the loss used to prune it, and the loss used to assess it need to be named separately.

If two patients have the same recorded predictors but opposite outcomes, no further split on those predictors can separate them. If a useful boundary is $x_1+x_2>0$, a single axis-aligned split cannot represent it; several rectangles approximate the diagonal. With a rare outcome, growing until singleton leaves may produce apparent training accuracy of $100\%$ but volatile predictions. Missing predictors require an explicit routing policy, such as a surrogate split or a designated missing branch; different policies can change predictions. Trees can also favor variables offering many candidate cut points unless selection is adjusted or validated.
## Worked example

Suppose a node has eight observations ordered by a numerical measurement. Their labels are $A,A,A,B,B,B,B,B$. The root class proportions are $(3/8,5/8)$, so its Gini impurity is $2(3/8)(5/8)=30/64=0.46875$. A cut between the third and fourth values produces a pure three-case $A$ leaf and a pure five-case $B$ leaf, giving weighted child impurity zero and $\Delta G=0.46875$. The tree needs only one question for these training cases.

A cut after the second value instead produces a pure two-case left leaf and a right node containing one $A$ and five $B$ cases. Its right Gini impurity is $2(1/6)(5/6)=5/18$, and its weighted impurity is $(6/8)(5/18)=5/24\approx0.20833$. Its improvement is $0.46875-0.20833\approx0.26042$, so the cut after the third value wins. This comparison also shows why weighting matters: the six-case mixed child should matter more than a tiny pure child.

**Your turn.** Six ordered observations have labels $A,A,B,B,B,B$. Compare the Gini improvement of a cut after the second value with a cut after the first. Which is chosen?

::: {.callout-tip collapse="true" title="Answer"}
The root Gini impurity is $2(2/6)(4/6)=4/9\approx0.44444$. Cutting after the second value makes both leaves pure, so the improvement is $4/9$. Cutting after the first leaves one $A$ and four $B$ cases on the right, whose Gini impurity is $2(1/5)(4/5)=8/25$. Its weighted impurity is $(5/6)(8/25)=4/15$, so improvement is $4/9-4/15=8/45\approx0.17778$. The cut after the second value is preferred.
:::

## Common misconceptions

A readable rule does not make the fitted tree stable: changing one case can alter an early split and every branch below it. A pure training leaf does not imply certainty about a future case that enters the same region. A split that improves training impurity need not improve test accuracy. Leaf proportions are empirical frequencies, not automatically calibrated probabilities. The axis-aligned boundary also should not be read as evidence that the scientific relationship itself changes discontinuously at the printed cutoff.

## Connections

[Node impurity](node-impurity.qmd) explains the local scores, while [cost-complexity pruning](cost-complexity-pruning.qmd) addresses tree size. A [regression tree](regression-tree.qmd) replaces class proportions with numerical leaf summaries. Averaging many unstable trees in a [random forest](random-forest.qmd) can reduce prediction variance, though the ensemble no longer has one short rule list. A [surrogate split](surrogate-split.qmd) routes a case when the primary split variable is missing.

## History

Classification methods include partitions, hierarchical grouping and geometric grouping, and one use is prediction followed by an action.{{cite:dodge2008}} (pp. 82–83, “Classification”) A supervised decision tree uses labeled training cases to construct a partition for prediction. The later CART name comes from Breiman, Friedman, Olshen and Stone's 1984 *Classification and Regression Trees*.
