## Intuition — Two draws from the same node
At a tree node, the class proportions $\hat p_g$ say how mixed the training cases are. The Gini index is the probability that two independent draws from those proportions fall in different classes. A pure node scores zero. An even split scores the most. Misclassification rate only notices whether the majority has changed, so a split can improve the mix and leave the misclassification rate still. The Gini index moves as soon as the proportions move.{{cite:hastie_esl2009}} (Ch. 9, §9.2.3, pp. 309–310)

The name is also used for an income coefficient. Dodge defines that coefficient from the area between the Lorenz curve and the diagonal, with $0$ for equal incomes and $1$ for complete inequality, and then multiplies by $100$ to obtain a percentage. That coefficient is not the node impurity below.{{cite:dodge2008}} (p. 231)

## Definition — Three expressions, one number
For class proportions $\hat p_1,\ldots,\hat p_G$ at a node,
$$
I_G=\sum_{g\neq g'}\hat p_g\hat p_{g'}=\sum_{g=1}^G\hat p_g(1-\hat p_g)=1-\sum_{g=1}^G\hat p_g^2.
$$
Hastie, Tibshirani and Friedman read the first sum as the error rate of the rule that classifies a random case from the node to class $g$ with probability $\hat p_g$. The same quantity is the sum, over classes, of the Bernoulli variances $\hat p_g(1-\hat p_g)$. For two classes and proportion $p$ of class $1$, it reduces to $2p(1-p)$.{{cite:hastie_esl2009}} (Ch. 9, §9.2.3, pp. 309–310)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Because the proportions sum to one,
$$
\sum_g\hat p_g(1-\hat p_g)=\sum_g\hat p_g-\sum_g\hat p_g^2=1-\sum_g\hat p_g^2.
$$
The cross sum expands as $(\sum_g\hat p_g)^2-\sum_g\hat p_g^2=1-\sum_g\hat p_g^2$. The two-class reduction is $p(1-p)+(1-p)p=2p(1-p)$.{{cite:hastie_esl2009}} (Ch. 9, §9.2.3, p. 309)
:::
:::

## Worked example — Ten cases, three classes
A node holds $6$, $2$ and $2$ cases of three classes, so the proportions are $0.6$, $0.2$ and $0.2$. Then
$$
I_G=0.6\cdot 0.4+0.2\cdot 0.8+0.2\cdot 0.8=0.56,
$$
and $1-(0.6^2+0.2^2+0.2^2)=1-0.44=0.56$. The misclassification rate is $1-0.6=0.4$. The natural-log cross-entropy is $-(0.6\log 0.6+2\cdot 0.2\log 0.2)=0.9503$ to four decimal places. The Gini index sits between the misclassification rate and the entropy on this node.{{cite:hastie_esl2009}} (Ch. 9, §9.2.3, pp. 309–310)

**Your turn.** A two-class node has $8$ cases of class $1$ and $2$ of class $2$. Find the Gini index and the misclassification rate.

::: {.callout-tip collapse="true" title="Answer"}
The class-$1$ proportion is $0.8$, so the Gini index is $2\cdot 0.8\cdot 0.2=0.32$. The misclassification rate is $0.2$.
:::

## Check yourself
### A pure node
All $10$ cases in a node belong to one class. What is the Gini index?

::: {.callout-tip collapse="true" title="Answer"}
One proportion is $1$ and the others are $0$, so $1-\sum\hat p_g^2=0$. Two draws from the node always match.
:::

### The even two-class node
For two classes with $p=1/2$, what is $2p(1-p)$?

::: {.callout-tip collapse="true" title="Answer"}
$2\cdot\tfrac12\cdot\tfrac12=\tfrac12$. This is the largest two-class value: the quadratic $2p(1-p)$ opens downwards and its vertex is at $p=1/2$.
:::

## Connections — What a split is asked to reduce
A [decision tree](decision-tree.qmd) chooses the split that most reduces a node impurity, and the Gini index is one such impurity. [Cross-entropy](cross-entropy.qmd) is the other smooth choice in the same list; misclassification rate is the piecewise-linear one. A [random forest](random-forest.qmd) often accumulates the Gini decrease of each predictor across trees, which is a different summary from a permutation of an out-of-bag sample.{{cite:hastie_esl2009}} (Ch. 9, §9.2.3, pp. 309–310; Ch. 15, §15.3.2, p. 593)
