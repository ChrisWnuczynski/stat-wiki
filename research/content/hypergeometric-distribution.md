## Motivating example

An inspector draws four items from a lot of twenty containing five defective items. The question is how many defects the sample contains when tested items are not put back. Each draw changes the composition available for the next one; the sample has a fixed size but its indicators are dependent.{{cite:dodge2008}} (p. 247)

## Definition

Uniform sampling means that every subset of size $n$ is equally likely. Among those subsets, $\binom r x\binom{N-r}{n-x}$ contain exactly $x$ marked items. Dividing by $\binom N n$ gives the hypergeometric mass function and its support. Both the marked and the unmarked counts must fit inside the sample and the population. This combinatorial argument also explains why a zero sample size or a census gives a deterministic count.{{cite:siegrist_hypergeometric2022}} (§ “Basic Theory, The Probability Density Function”)

The indicator on any one draw has success probability $r/N$. That marginal probability does not change with the draw number: the dependence appears in conditional probabilities after earlier results are revealed. Confusing those two statements can lead to an incorrect independence assumption.{{cite:dodge2008}} (pp. 247–248)

## Properties

For distinct draw positions, $\mathbb{P}(I_i=I_j=1)=r(r-1)/[N(N-1)]$, and subtraction of $(r/N)^2$ gives
$$
\operatorname{Cov}(I_i,I_j)=-\frac{p(1-p)}{N-1}.
$$
This covariance is nonpositive, and strictly negative only when $0<p<1$, where $p=r/N$. For $N>1$, the finite-population variance is no larger than the variance of a binomial variable with the same $n$ and $p$. It is strictly smaller when $n\ge2$ and $0<p<1$; equality holds when $n=0$, $n=1$, or $p\in\{0,1\}$. At $n=1$ both laws are Bernoulli, so for $N=20$ and $r=5$ both variances are $3/16$. Summing all $n$ variances and $n(n-1)$ ordered cross-covariances proves the correction factor $(N-n)/(N-1)$. The formula assumes $N>1$; for a one-item population every possible sample count is deterministic.{{cite:siegrist_hypergeometric2022}} (§ “Basic Theory, Moments”)

## Related distributions

As $N$ grows, with $n$ fixed and $r/N\to p$, the probability of any fixed pattern of marked and unmarked draws tends to the probability under independent Bernoulli trials. Summing over patterns gives the binomial limit. Whether that is an adequate approximation for a particular sample depends on the sampling fraction and the probability being approximated.{{cite:siegrist_hypergeometric2022}} (§ “Convergence of the Hypergeometric Distribution to the Binomial”)

## Worked example

For the inspection lot, $N=20$, $r=5$ and $n=4$. The probabilities of no defects and exactly two defects are
$$
\mathbb{P}(X=0)=\frac{\binom{15}4}{\binom{20}4}=\frac{1365}{4845}\approx0.28173,
\qquad
\mathbb{P}(X=2)=\frac{\binom52\binom{15}2}{\binom{20}4}
=\frac{1050}{4845}\approx0.21672.
$$
The mean is one defect and the variance is $4(1/4)(3/4)(16/19)=12/19\approx0.63158$. Sampling with replacement would leave the mean at one but give variance $3/4$. For two particular draws, the covariance is $-3/304$, and the twelve ordered covariance contributions reduce the variance by $9/76$. The enumeration and covariance approaches agree.{{cite:dodge2008}} (pp. 247–248)

**Your turn.** If all twenty items are inspected, what are the mean and variance of the defect count?

::: {.callout-tip collapse="true" title="Answer"}
Exactly five defects are found. The mean is five and the variance is zero; the finite-population correction vanishes when $n=N$.
:::

A lot of 10 items contains 4 defectives, and a sample of 2 is drawn without replacement. What is the probability that both items are defective?

::: {.callout-tip collapse="true" title="Answer"}
$\mathbb{P}(X=2)=\binom{4}{2}/\binom{10}{2}=6/45=2/15$.
:::

## Statistical inference

When the population composition is unknown, a sampling law is still defined for each candidate integer value of $r$. Likelihood comparison or tail inversion can then estimate or test that count. The candidate values are integers compatible with the sample: observing two defects rules out a lot containing fewer than two defects.{{cite:dodge2008}} (p. 248)

## Connections — Finite populations and conditioning

The marked fraction is fixed by the sampling model. Conditioning on earlier draws changes the composition of the remaining lot, while the unconditional success probability on any one draw stays the same.{{cite:dodge2008}} (pp. 247–248)
