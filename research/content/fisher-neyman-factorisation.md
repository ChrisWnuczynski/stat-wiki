## Lead context
Fisher–Neyman factorisation is a test for sufficiency: the parameter may enter the joint density only through the statistic being tested.

## Motivating example
Independent Bernoulli($\theta$) variables have joint mass

$$
p(x\mid\theta)=\theta^{s}(1-\theta)^{n-s},\qquad s=\sum_{i=1}^n x_i,
$$


on sequences of zeros and ones. Here $h(x)=1$ and $g_\theta(s)=\theta^{s}(1-\theta)^{n-s}$, so the success count is sufficient. For $n=4$ and $s=2$, six sequences share that count, and each has conditional probability $1/6$. The value $1/6$ does not depend on $\theta$.{{cite:dasgupta2011_exponential_family}} (§18.4.1, pp. 512–514)

## Statement
**A product with one parameter-free factor.** Suppose a dominated family has joint density or mass function $p(x\mid\theta)$. A statistic $T$ is sufficient for $\theta$ when

$$
p(x\mid\theta)=g_\theta\{T(x)\}\,h(x)
$$


for a nonnegative $g_\theta$ and a nonnegative $h$ that does not depend on $\theta$. In the discrete case this factorisation is enough to show that the conditional distribution of the sample given $T$ is free of $\theta$. The argument above gives the discrete case. A general dominated family needs a conditional kernel for the converse.{{cite:dasgupta2011_exponential_family}} (§18.4.1, pp. 512–514)

## Intuition — Everything about $\theta$ has to pass through $T$
Once $T(x)=t$ is known, any leftover factor that still depends on $\theta$ would change the conditional probabilities of the sample points that share that value of $T$. If no such factor remains, those conditional probabilities can be computed from $h$ alone. The statistic can still be a function of the whole sample. What is reduced is the part of the likelihood that moves with $\theta$.

## Proof
For a discrete sample with $T(x)=t$ and $p(u\mid\theta)>0$ on the relevant points,

$$
\mathbb{P}_\theta(X=x\mid T=t)
=\frac{g_\theta(t)\,h(x)}{\sum_{u:T(u)=t}g_\theta(t)\,h(u)}
=\frac{h(x)}{\sum_{u:T(u)=t}h(u)}.
$$


The factor $g_\theta(t)$ cancels because it is the same for every sample point with $T=t$. The conditional probability does not depend on $\theta$, which is sufficiency in the discrete case.{{cite:dasgupta2011_exponential_family}} (§18.4.1, pp. 512–514)

## Worked example

**Your turn.** Three independent Bernoulli trials produce two successes. What is the conditional probability of one particular sequence with those two successes, given the success count?

::: {.callout-tip collapse="true" title="Answer"}
Three sequences have success count $2$, namely $(1,1,0)$, $(1,0,1)$ and $(0,1,1)$. The conditional probability of each is $1/3$. The parameter cancels for the same reason as in the four-trial case.
:::

### A second conditional probability
Five independent Bernoulli trials produce one success. Give the conditional probability of a particular sequence with that one success.

::: {.callout-tip collapse="true" title="Answer"}
There are five such sequences, one for each position of the success. The conditional probability is $1/5$.
:::

### Where the factor $h$ is not constant
Independent Poisson($\theta$) observations have joint mass proportional to $\theta^{t}e^{-n\theta}/\prod_i x_i!$, with $t=\sum x_i$. Which factor is free of $\theta$?

::: {.callout-tip collapse="true" title="Answer"}
The factor $h(x)=1/\prod_i x_i!$ does not depend on $\theta$. All of the parameter dependence sits in $g_\theta(t)=\theta^{t}e^{-n\theta}$, so the sum is sufficient. The factorial term changes the conditional probabilities of the compositions of $t$, but it does not put $\theta$ back into them.
:::

## Related concepts — Sufficiency, ancillarity and the exponential family
Factorisation is the practical test for a [sufficient statistic](sufficient-statistic.qmd). An [ancillary statistic](ancillary-statistic.qmd) is the complementary idea: its distribution, rather than a factor of the likelihood, is free of $\theta$. A one-parameter [exponential family](exponential-family.qmd) is already in factorised form, with the natural sufficient statistic in the exponent. The Bayesian use of the same cancellation is that the posterior depends on the sample only through $T$, because $h(x)$ does not depend on $\theta$.

## History
Factorisation is the criterion that isolates a statistic sufficient for the parameter.{{cite:dasgupta2011_exponential_family}} (§18.4.1, pp. 512–514)
