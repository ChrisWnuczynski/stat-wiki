## Motivating example
A classification tree can fit increasingly small groups until most training leaves are pure. That reduces training loss but can make predictions unstable. Cost-complexity pruning compares subtrees by charging for terminal nodes as well as their empirical prediction loss. Validation then chooses how much simplification is useful.{{cite:loh2014_trees}} (§2.1, p. 331)

## Definition — Put risk and leaf count on a common scale
For a subtree $T$, define
$$
R_\alpha(T)=R(T)+\alpha|\widetilde T|,\qquad\alpha\ge0,
$$
where $|\widetilde T|$ is its number of terminal nodes and $R(T)$ is a specified empirical risk. In classification, a leaf contribution can be its sample fraction times its misclassification rate, so the sum is the overall training misclassification fraction. The loss, observation weights and use of a sum or average determine the units of $\alpha$.{{cite:quan_etal2023_hybrid_trees}} (§2.1, eq. 4)

A larger penalty favours fewer leaves. For a fixed collection of candidate subtrees, this monotonicity follows directly. If $T_1,T_2$ minimise the criterion at $\alpha_1<\alpha_2$, their two optimality inequalities imply
$$
(\alpha_2-\alpha_1)\{ |\widetilde T_2|-|\widetilde T_1|\}\le0.
$$
Thus the number of leaves cannot increase as the penalty increases. This argument compares sizes; the stronger nested-path property additionally uses the structure of pruning a fixed tree.{{cite:quan_etal2023_hybrid_trees}} (§2.1, cost-complexity criterion)

## Properties — The effective price of a branch
Consider replacing a branch rooted at node $t$ by one terminal node. If the branch has $m>1$ leaves, its criterion equals that of the single node at
$$
\alpha=\frac{R(t)-R(T_t)}{m-1}.
$$
This identity comes from equating $R(t)+\alpha$ with $R(T_t)+\alpha m$. Weakest-link pruning successively removes branches with the smallest such effective penalty, producing a nested sequence from the fully grown tree. []{#property-nested-pruning-path} Each step replaces at least one branch by a leaf, so the resulting partitions become progressively coarser.{{cite:loh2014_trees}} (§2.1, p. 331)

For a fixed finite binary tree, global minimisation at a specified penalty also has a direct recursive solution. Let $C_\alpha(t)$ be the minimum penalised risk available below node $t$. At a terminal node, $C_\alpha(t)=R(t)+\alpha$. At an internal node with children $t_L,t_R$,
$$
C_\alpha(t)=\min\{R(t)+\alpha,\ C_\alpha(t_L)+C_\alpha(t_R)\}.
$$
Every pruned subtree either collapses $t$ to one leaf or preserves its split and chooses a subtree under each child. Additivity of leaf risk makes these the exhaustive alternatives. Induction from terminal nodes proves the recursion finds a global optimum over all prunings of that fixed tree. This argument gives an optimum for one penalty; the weakest-link construction arranges the comparisons into a path across penalties.{{cite:quan_etal2023_hybrid_trees}} (§2.1, eq. 4)

## Worked example — Two trees and a crossover
A two-leaf tree has weighted leaf risks $0.3$ and $0.2$, hence total risk $0.5$. A five-leaf tree has total risk $0.3$. At $\alpha=0.15$ their penalised risks are $0.8$ and $1.05$, selecting the smaller tree. At $\alpha=0.05$ they are $0.6$ and $0.55$, selecting the larger. Their crossover is $\alpha=(0.5-0.3)/(5-2)=1/15=0.066667$. Both are optimal among these two candidates exactly at that value.{{cite:quan_etal2023_hybrid_trees}} (§2.1, eq. 4)

**Your turn.** A branch has four leaves and risk $0.12$; collapsing it gives risk $0.24$. At what penalty are the two choices tied?

::: {.callout-tip collapse="true" title="Answer"}
The risk increase is $0.12$ for three fewer leaves, giving effective penalty $0.12/3=0.04$. Above this value the collapsed node has the lower criterion among these choices.
:::

## Statistical use — Choose the penalty within validation
The training objective constructs candidates. Cross-validation estimates their predictive performance and can choose a subtree with minimum estimated error or a simpler one within a chosen uncertainty allowance. A final test set should be excluded from all such choices. Reusing test error to choose among penalties makes it part of model selection rather than an independent final assessment.{{cite:loh2014_trees}} (§2.1, p. 331){{cite:cawley_talbot2010}} (§2, pp. 2081–2084)

The familiar one-standard-error preference for a smaller tree is a selection convention, not a confidence statement that two trees have equal population risks. The standard error describes uncertainty in an estimated validation error; it does not remove the effects of trying many candidate procedures.{{cite:cawley_talbot2010}} (§2, model-selection criterion overfitting)

