## Lead context
A multinomial count splits a fixed number of independent trials across several categories.{{cite:dodge2008}} (p. 363)

## Motivating example
Let $n=3$ and $(p_1,p_2,p_3)=(1/2,\ 1/3,\ 1/6)$. The count vector $(1,1,1)$ has probability
$$
\frac{3!}{1!\,1!\,1!}\cdot\frac12\cdot\frac13\cdot\frac16=\frac{6}{36}=\frac16.
$$
The mean of the first coordinate is $3\cdot(1/2)=3/2$. Its variance is $3\cdot(1/2)\cdot(1/2)=3/4$. The covariance of the first and second coordinates is $-3\cdot(1/2)\cdot(1/3)=-1/2$. The three counts cannot all be large together: their sum is $3$.

## Intuition — The categories compete for a fixed total
Each trial lands in one category. After $n$ trials the category counts sum to $n$, so a large count in one category is a small count in the others. The marginal count in a single category is binomial, because that category can be collapsed to “in” or “out”. The covariance between two different category counts is negative: the trials they both want are the same trials. Each coordinate has expectation $n p_i$ and variance $n p_i(1-p_i)$, the binomial margin, and the joint probability is the number of sequences with those counts times the probability of any one such sequence.{{cite:dodge2008}} (p. 363){{cite:durrett2019}} (§3.10, p. 201, die-count covariance)

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

## Common misconceptions
Independent trials do not produce independent counts. The fixed total ties the coordinates together: $\operatorname{Cov}(X_i,X_j)=-np_ip_j$ is negative whenever both probabilities are positive, so a large count in one category must be offset by smaller counts in the others. The binomial margins describe the coordinates one at a time; they do not describe the joint law, and treating the counts as independent misstates the probability of configurations in which several counts are simultaneously far from their means. The expectation $np_i$ is also not a typical value that an experiment can realise: with $n=3$ and $p_3=1/6$ the third coordinate has mean $1/2$, although every realised count is a whole number.

## Assumptions and limits
The multinomial law assumes that the number of trials $n$ is fixed in advance, that the trials are independent, and that every trial shares the same probability vector $p$. Each assumption has a distinct failure mode. A random total changes the joint law: under a Poisson total with multinomial allocation, the counts are independent Poissons rather than multinomial counts. A probability vector that varies between trials, as in a mixture of populations, inflates the count variances beyond $np_i(1-p_i)$. Dependence between trials, such as clustering within groups, distorts the counts in the same direction. The boundary cases $p_i=0$ and $p_i=1$ remain coherent but degenerate: the corresponding count is then $0$ or $n$ with probability one, and the remaining categories follow a multinomial law on fewer categories.

## Connections
Each coordinate is a [binomial distribution](binomial-distribution.qmd) count, and the dependence among coordinates is the content of the joint law. The [Poisson distribution](poisson-distribution.qmd) supplies the complementary regime, and the two laws are joined by an exact split. If the total $N$ is Poisson with mean $\lambda$ and, given $N=n$, the counts are multinomial with the same fixed probability vector $p$ for every $n$, then the counts are independent and $X_i$ is Poisson with mean $\lambda p_i$; conditioning independent Poisson counts on their sum returns the multinomial law with probabilities proportional to their means.{{cite:durrett2019}} (§3.7, p. 179){{cite:siegrist2022_poisson_splitting}} (Thinning and Superposition) Both hypotheses carry weight. A random total alone does not split: if the total is $1$ with probability $1/4$ and $0$ otherwise, and a single trial is labelled by a fair coin, each of two counts equals $1$ with probability $1/8$, yet the two counts cannot both equal $1$, so they are not independent. The missing hypothesis is the Poisson total, not the labelling. A [multinomial logistic regression](multinomial-logistic-regression.qmd) puts the probability vector $p$ under a regression and keeps this likelihood for the counts.{{cite:dodge2008}} (p. 363)
