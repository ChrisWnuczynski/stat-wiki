## Intuition — Averaging helps only while the trees disagree
A forest grows many trees and averages them. If the trees were independent, the variance of the average would fall like $1/B$ as the number of trees $B$ grew. Bootstrap samples alone do not make the trees independent: they still tend to split on the same strong predictors. Random forests restrict each split to a fresh handful of predictors so that neighbouring trees are less alike. Averaging then has something to cancel. What remains is a floor set by the correlation between trees.{{cite:hastie_esl2009}} (Ch. 15, §15.2, pp. 587–589)

## Definition — Bootstrap sample, then a random subset of predictors
For $b=1,\ldots,B$, draw a bootstrap sample of the training set and grow a tree on it. Before each split, choose $m\le p$ of the $p$ predictors at random and pick the split from that subset only. The regression forest predicts the average of the $B$ trees. Hastie, Tibshirani and Friedman note that typical choices are $m$ near $\sqrt p$, or even $m=1$. The trees are identically distributed. They are not independent. If each tree has variance $\sigma^2$ at a fixed $x$ and each pair has correlation $\rho$, the variance of the average is
$$
\rho\sigma^2+\frac{1-\rho}{B}\sigma^2.
$$
As $B$ grows, the second term vanishes and the first remains.{{cite:hastie_esl2009}} (Ch. 15, §15.2, pp. 588–589, display 15.1)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $T_1,\ldots,T_B$ be identically distributed with variance $\sigma^2$ and $\operatorname{Cov}(T_b,T_s)=\rho\sigma^2$ for $b\neq s$. The variance of the sum is $B\sigma^2+B(B-1)\rho\sigma^2$. Divide by $B^2$:
$$
\operatorname{Var}\Bigl(\frac1B\sum_{b=1}^B T_b\Bigr)=\frac{\sigma^2}{B}\bigl(1+(B-1)\rho\bigr)=\rho\sigma^2+\frac{(1-\rho)\sigma^2}{B}.
$$
The algebra uses a common variance and a common pairwise correlation. It does not use normality.{{cite:hastie_esl2009}} (Ch. 15, §15.2, p. 588, display 15.1)
:::
:::

## Worked example — A floor of $0.8$
Take $\sigma^2=4$, $\rho=0.2$ and $B=100$. The variance of the average is
$$
0.2\cdot 4+\frac{0.8}{100}\cdot 4=0.8+0.032=0.832.
$$
One tree has variance $4$. An average of $100$ independent trees, the case $\rho=0$, would have variance $4/100=0.04$. The correlation floor $0.8$ is twenty times that independent-average variance. Adding further trees can eat the $0.032$, not the $0.8$.{{cite:hastie_esl2009}} (Ch. 15, §15.2, p. 588)

**Your turn.** Take $\sigma^2=1$, $\rho=0.5$ and $B=50$. Find the variance of the average, and the variance that independence would have given.

::: {.callout-tip collapse="true" title="Answer"}
The variance is $0.5\cdot 1+(0.5/50)\cdot 1=0.5+0.01=0.51$. Independence would give $1/50=0.02$. Most of the $0.51$ is the correlation floor.
:::

## Check yourself
### Doubling the forest
In the worked example, replace $B=100$ by $B=200$ and leave $\sigma^2=4$ and $\rho=0.2$. What is the new variance?

::: {.callout-tip collapse="true" title="Answer"}
$0.8+(0.8/200)\cdot 4=0.8+0.016=0.816$. The floor is unchanged. The second term has halved.
:::

### A single candidate predictor
If $m=1$, each split sees only one randomly chosen predictor. What happens to the formula if that choice drives $\rho$ down and $\sigma^2$ up?

::: {.callout-tip collapse="true" title="Answer"}
Both terms move. A smaller $\rho$ lowers the floor $\rho\sigma^2$, but a larger $\sigma^2$ raises it and also raises the term that still depends on $B$. The formula does not say that the smallest $m$ is the best $m$.{{cite:hastie_esl2009}} (Ch. 15, §15.2, pp. 588–589)
:::

## Connections — What the average is made of
Each member is a [decision tree](decision-tree.qmd), and the split inside it is often scored by the [Gini index](gini-index.qmd). The row resampling is [bagging](bagging.qmd), which uses the [bootstrap](bootstrap.qmd). [Out-of-bag estimation and variable importance](out-of-bag-estimation-and-variable-importance.qmd) uses the cases a tree did not see. The correlation floor is why a restriction on the predictors is part of the definition, not a cosmetic extra.{{cite:hastie_esl2009}} (Ch. 15, §15.2, pp. 587–589)
