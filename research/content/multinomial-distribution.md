## Lead context
A multinomial count splits a fixed number of independent trials across several categories.{{cite:dodge2008}} (p. 363)

## Motivating example
Let $n=3$ and $(p_1,p_2,p_3)=(1/2,\ 1/3,\ 1/6)$. The count vector $(1,1,1)$ has probability
$$
\frac{3!}{1!\,1!\,1!}\cdot\frac12\cdot\frac13\cdot\frac16=\frac{6}{36}=\frac16.
$$
The mean of the first coordinate is $3\cdot(1/2)=3/2$. Its variance is $3\cdot(1/2)\cdot(1/2)=3/4$. The covariance of the first and second coordinates is $-3\cdot(1/2)\cdot(1/3)=-1/2$. The three counts cannot all be large together: their sum is $3$.

## Intuition — The categories compete for a fixed total
Each trial lands in one category. After $n$ trials the category counts sum to $n$, so a large count in one category is a small count in the others. The marginal count in a single category is binomial, because that category can be collapsed to “in” or “out”. The covariance between two different category counts is negative: the trials they both want are the same trials. Each coordinate has expectation $n p_i$ and variance $n p_i(1-p_i)$, the binomial margin, and the joint probability is the number of sequences with those counts times the probability of any one such sequence.{{cite:dodge2008}} (p. 363)

## Definition
For $n$ independent trials and category probabilities $p_1,\ldots,p_s$ summing to $1$, the joint probability of counts $x_1,\ldots,x_s$ that are nonnegative integers summing to $n$ is
$$
P(X_1=x_1,\ldots,X_s=x_s)=\frac{n!}{x_1!\cdots x_s!}\,p_1^{x_1}\cdots p_s^{x_s}.
$$
The factorial ratio counts the sequences with those category totals. The product of powers is the probability of any one such sequence.{{cite:dodge2008}} (p. 363) One statement of the range of each $p_i$ is the open interval $(0,1)$. A category probability of $0$ or $1$ is a degenerate but coherent case of the same formula: that category is then impossible or certain, and the corresponding count is $0$ or $n$.

## Worked example

The same formula with $n=10$ and $(p_1,p_2,p_3)=(0.2,0.3,0.5)$ gives $P(2,3,5)=0.08505$. The three-trial probability $1/6$ is the exact small case.

**Your turn.** With the same $n=3$ and the same probabilities, find $P(3,0,0)$ and the mean of the third coordinate.

::: {.callout-tip collapse="true" title="Answer"}
There is one sequence of three outcomes in the first category, and its probability is $(1/2)^{3}=1/8$. The multinomial coefficient is $1$, so $P(3,0,0)=1/8$. The third mean is $3\cdot(1/6)=1/2$.
:::

**Check yourself.** Why is $\operatorname{Cov}(X_1,X_2)$ negative when both probabilities are positive and $n\ge 1$?

::: {.callout-tip collapse="true" title="Answer"}
On a single trial the two category indicators cannot both equal $1$, so their product has expectation $0$ while the product of the expectations is $p_1 p_2>0$. The covariance on one trial is $-p_1 p_2$. Independent trials add those covariances, giving $-n p_1 p_2$.
:::

**Check yourself.** Suppose the probabilities are required to satisfy $0<p_i<1$. If $p_3=0$ and $(p_1,p_2)=(1/2,1/2)$, what is $P(1,1,1)$ for $n=3$?

::: {.callout-tip collapse="true" title="Answer"}
The count $1$ in the third category is impossible, so the probability is $0$. The formula returns the same answer because it contains the factor $p_3^{1}=0$. The strict inequality excludes this boundary; the probability function itself does not.
:::

## Connections
Each coordinate is a [binomial distribution](binomial-distribution.qmd) count, and the dependence among coordinates is the content of the joint law. The [Poisson distribution](poisson-distribution.qmd) is the different regime in which category counts are independent and the total is not fixed. A [multinomial logistic regression](multinomial-logistic-regression.qmd) puts the probability vector $p$ under a regression and keeps this likelihood for the counts.{{cite:dodge2008}} (p. 363)
