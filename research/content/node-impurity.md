## Motivating example
A classification tree separates 20 observations into groups to predict whether each belongs to class A or B. If one candidate split leaves both groups mixed while another nearly separates the classes, their training error might not fully reveal the difference. Node impurity scores the class mixture at each step, giving the tree a local guide for choosing a split.{{cite:stanford_cs229_trees2018}} (§§2–3, pp. 2–5)

## Intuition
A pure node contains one class and needs no further division to classify its training cases. A mixed node contains competing labels. The simplest score is the fraction that a majority-class prediction would get wrong, but that score changes only when a split changes the majority composition enough. Gini impurity and entropy respond more smoothly as class proportions move, so a useful early split can be rewarded even before either child's predicted label changes. The aim is a *local* reduction in weighted impurity. This alone cannot establish that the resulting full tree will predict best on new observations.{{cite:stanford_cs229_trees2018}} (§3, pp. 4–5)

## Definition
At a classification node $m$, let $\hat p_{mg}$ be the fraction of training cases in class $g$, with $\sum_g\hat p_{mg}=1$. Common impurity functions are Gini $I_G(m)=1-\sum_g\hat p_{mg}^2$, entropy $I_C(m)=-\sum_g\hat p_{mg}\log\hat p_{mg}$ with $0\log0=0$, and majority-class misclassification $I_M(m)=1-\max_g\hat p_{mg}$. A zero score means the node is pure in the observed training data. Their numerical scales differ, so compare candidate splits using the *same* chosen criterion.{{cite:stanford_cs229_trees2018}} (§3, pp. 4–5)

For a split sending fractions $w$ and $1-w$ of the node's observations left and right, its reduction is $\Delta I=I(m)-wI(m_L)-(1-w)I(m_R)$. The weights reflect the child sizes, preventing a tiny pure child from being treated as valuable as a large one. At a node, a greedy tree chooses the available variable and cut point with the greatest reduction and repeats the process in the children. That decision does not compare all complete trees that could be grown from the node.{{cite:stanford_cs229_trees2018}} (§§2–3, pp. 2–5)

## Interpretation — Three scales for the same mixture
For binary classes with class-A proportion $p$, Gini is $2p(1-p)$, entropy is $-p\log p-(1-p)\log(1-p)$, and misclassification impurity is $\min(p,1-p)$. Each is zero at $p=0$ or $1$ and largest at a balanced node. In the two-class case their maxima are respectively $0.5$, $\log2\approx0.6931$ with natural logs, and $0.5$. Changing entropy's logarithm base multiplies all entropy values and reductions by the same positive constant, so it leaves the ordering of candidate splits unchanged when everything else is fixed.{{cite:stanford_cs229_trees2018}} (§3, pp. 4–5)

The word *Gini* needs care. Tree Gini impurity is a function of **class probabilities** and measures mixing. Dodge's "Gini index" entry describes a different measure of **income inequality** based on a Lorenz curve. A class node's value $0.5$ is not an income-inequality coefficient, even though the names share Gini's surname.{{cite:dodge2008}} (p. 231, Gini Index){{cite:stanford_cs229_trees2018}} (§3, p. 5, tree Gini)

## Properties — Why a split cannot raise weighted concave impurity
The parent class-proportion vector is the size-weighted average of its children's vectors. Gini and entropy are concave functions of that vector; Jensen's inequality therefore makes the parent impurity at least the weighted average of the children. Misclassification impurity is also concave but has flat linear regions: if both children keep the same majority class, its weighted value may not fall at all. A split can be useful as preparation for later splits even when its immediate misclassification gain is zero.{{cite:stanford_cs229_trees2018}} (§3, pp. 4–5, impurity and flat misclassification)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $p_g=w p_{Lg}+(1-w)p_{Rg}$. For Gini, $I_G(p)=1-\sum_gp_g^2$; each negative square is concave. For entropy, $-p_g\log p_g$ has second derivative $-1/p_g<0$ on the interior and extends continuously to zero. Hence Jensen's inequality gives $I(p)\ge wI(p_L)+(1-w)I(p_R)$ for either criterion. Misclassification impurity is $1-\max_gp_g$, the negative of a convex maximum plus one, so the same inequality holds, although equality can persist across a nontrivial split.

For two classes, $1-[p^2+(1-p)^2]=2p(1-p)$. Its derivative is $2-4p$ and entropy's is $\log\{(1-p)/p\}$, so each peaks at $p=1/2$; misclassification $\min(p,1-p)$ peaks there too. With $G$ classes, $\sum_gp_g^2\ge1/G$ by Cauchy–Schwarz and entropy is at most $\log G$ by concavity, both equalities at equal proportions. For a fixed majority class in both children, the weighted misclassification score is $1-[wp_L+(1-w)p_R]=1-p$, exactly the parent's score.{{cite:stanford_cs229_trees2018}} (§3, pp. 4–5, impurity curves)
:::
:::

## Statistical use — Grow, then check the tree
At each proposed cut, calculate the child class proportions and weight each child's impurity by its fraction of cases. The largest positive reduction is attractive for growing a classification tree. Constraints on minimum leaf size or improvement can prevent a cut supported by too few observations; cost-complexity pruning and cross-validation then assess whether a larger training tree predicts well enough to retain. Since the split is chosen from the training sample, the impurity drop is an in-sample score and may exaggerate predictive value, especially when many candidate cut points are searched.{{cite:rpart_longintro2023}} (§§1, 3.1, 4){{cite:sklearn_tree2026}} (§§1.10.7–1.10.9)

For the baseline example, a parent that is $80\%$ class 1 and $20\%$ class 2 has Gini impurity $0.32$, entropy about $0.500$, and misclassification impurity $0.20$. Equal-size children at $(0.7,0.3)$ and $(0.9,0.1)$ still predict class 1. Weighted misclassification stays $0.20$, but weighted Gini falls to $0.30$ and weighted entropy to about $0.468$. The respective reductions are $0$, $0.02$ and about $0.032$. The smoother rules detect progress that majority error cannot yet see.{{cite:stanford_cs229_trees2018}} (§3, pp. 4–5, flat majority loss and entropy)

## Worked example
Suppose a node contains 12 class-A and 8 class-B cases, giving proportions $(0.6,0.4)$ and Gini impurity $1-(0.6^2+0.4^2)=0.48$. A proposed split makes equal-size children: the left has 8 A and 2 B, and the right has 4 A and 6 B. Their Gini impurities are $1-(0.8^2+0.2^2)=0.32$ and $1-(0.4^2+0.6^2)=0.48$. Weighted child impurity is $0.5(0.32)+0.5(0.48)=0.40$, so the reduction is $0.08$. The right child changes its majority to B; the split has separated some class information, though both children remain mixed.{{cite:stanford_cs229_trees2018}} (§3, pp. 4–5, weighted child loss)

**Your turn.** With the same parent, another equal-size split makes a pure left child of 10 A and 0 B, and a right child of 2 A and 8 B. Calculate its weighted Gini impurity and reduction. Which of the two candidate splits does a Gini-greedy tree choose?

::: {.callout-tip collapse="true" title="Answer"}
The left Gini impurity is $0$. The right has proportions $(0.2,0.8)$ and impurity $2(0.2)(0.8)=0.32$. Weighted impurity is $0.5(0)+0.5(0.32)=0.16$, so the reduction from $0.48$ is $0.32$. This exceeds $0.08$, so the tree chooses the second split at this node, subject to its split and leaf-size constraints.{{cite:stanford_cs229_trees2018}} (§3, pp. 4–5, weighted child loss)
:::

## Common misconceptions
Low impurity in a small training node does not establish that future cases in its region are all one class. Gini and entropy use different numerical scales, so their values cannot be compared as if they were the same units. A split with zero immediate misclassification improvement can still lower Gini and help later divisions. A large local impurity reduction is not a guarantee of low test error for the final tree. These are separate issues of sampling uncertainty, score scale, greedy search and generalization.{{cite:stanford_cs229_trees2018}} (§§3–4, pp. 4–7, impurity and generalization)

## Assumptions and limits — When a pure leaf misleads
If a node contains just one training case, all three empirical impurities are zero, even though its prediction for a new case may be unreliable. If one class is rare but costly to miss, plain class proportions and equal-error loss can favor the majority; class weights or an explicit loss matrix change the decision problem. If a predictor offers many candidate thresholds, the best observed impurity decrease can reflect search noise. Leaf-size rules, validation, pruning and a loss function suited to the task address these different failures.{{cite:stanford_cs229_trees2018}} (§4.2, pp. 7–8, small leaves and pruning){{cite:rpart_longintro2023}} (§3.2, software loss options)

## Connections
[Decision trees](decision-tree.qmd) use impurity to choose branches. [Cross-entropy](cross-entropy.qmd) and [Gini index](gini-index.qmd) describe two criteria in more detail; [cost-complexity pruning](cost-complexity-pruning.qmd) controls final tree size. [Variable importance](variable-importance.qmd) can aggregate decreases across a tree, but it inherits the way candidate splits were searched. [Regression trees](regression-tree.qmd) instead use criteria for numeric responses, such as squared-error reduction.{{cite:stanford_cs229_trees2018}} (§§3–4, pp. 4–8, classification, regression and pruning){{cite:sklearn_tree2026}} (§1.10.9, software pruning criterion)

## History
Breiman, Friedman, Olshen and Stone's 1984 *Classification and Regression Trees* gave a systematic framework for tree construction and pruning, as recounted by the authors of the `rpart` methods guide. The guide explains why misclassification risk is too flat to guide early splits and describes Gini and information impurity as alternatives. Modern tree software continues to implement weighted child-impurity searches and separate pruning rules.{{cite:rpart_longintro2023}} (§§1, 3.1, 4){{cite:sklearn_tree2026}} (§§1.10.6–1.10.9)
