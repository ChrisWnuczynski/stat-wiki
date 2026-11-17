## Lead context
A uniformly minimum-variance unbiased estimator is an unbiased estimator whose variance is as small as the unbiased class allows, at every parameter value.

## Motivating example
Take \(n=4\), \(k=1\) and \(T=3\). Then
\[
U(3)=\binom{3}{1}\Bigl(\frac14\Bigr)\Bigl(\frac34\Bigr)^{2}=\frac{27}{64}=0.421875.
\]
The plug-in maximum-likelihood value is \(e^{-3/4}(3/4)=0.3543\) to four decimals. The two numbers answer different questions: \(0.421875\) is the unbiased conditional probability, and \(0.3543\) is \(g\) evaluated at \(T/n\).

## Intuition — Stay unbiased, then discard noise
Unbiasedness fixes the expectation. Among rules with that fixed expectation, the variance is the remaining squared-error risk. A sufficient statistic carries every part of the sample that moves with the parameter, so an unbiased function of that statistic is the place to look. A further average, the conditional expectation of any unbiased estimator given the sufficient statistic, stays unbiased and does not raise the variance. Completeness then says there is only one such function.{{cite:rao1945}} (pp. 237–238){{cite:blackwell1947}} (pp. 105–107)

## Definition — Smallest variance at every parameter
Let \(g(\theta)\) be a scalar target. An estimator \(U\) is unbiased for \(g(\theta)\) when \(\mathbb{E}_\theta U=g(\theta)\) for every \(\theta\), and it has finite variance. It is uniformly minimum-variance unbiased when, for every other unbiased \(V\) and every \(\theta\),
\[
\operatorname{Var}_\theta(U)\le\operatorname{Var}_\theta(V).
\]
The inequality has to hold on the whole parameter space. An estimator that wins at one \(\theta\) and loses at another is not uniformly minimum-variance unbiased.{{cite:siegrist2022_sufficient_complete}} (§7.6, Properties of Sufficient Statistics and Complete Statistics)

## Properties — The Poisson conditional probability is unbiased
Let \(X_1,\ldots,X_n\) be independent Poisson(\(\theta\)) random variables, \(T=\sum_{j=1}^n X_j\), and fix an integer \(k\ge 0\). Given \(T=t\), the count \(X_1\) is binomial with \(t\) trials and success probability \(1/n\), so
\[
U(t)=\binom{t}{k}\Bigl(\frac1n\Bigr)^k\Bigl(1-\frac1n\Bigr)^{t-k}
\]
for \(t\ge k\), and \(U(t)=0\) for \(t<k\).

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The binomial formula does not depend on \(\theta\). The law of total probability therefore gives
\[
\mathbb{E}_\theta U(T)=\mathbb{E}_\theta\bigl[\mathbb{P}(X_1=k\mid T)\bigr]=\mathbb{P}(X_1=k)=e^{-\theta}\theta^k/k!.
\]
So \(U(T)\) is unbiased for \(g(\theta)=\mathbb{P}(X_1=k)\). The plug-in \(e^{-\overline X}\overline X^k/k!\) is a different function of \(T\). For \(k=0\) the map \(x\mapsto e^{-x}\) is strictly convex, and \(\overline X\) is unbiased for \(\theta\) and not degenerate, so Jensen's inequality yields \(\mathbb{E} e^{-\overline X}>e^{-\theta}\). The plug-in is biased high.
:::
:::

Uniqueness needs completeness of \(T\): if two unbiased functions of a complete sufficient statistic differ, their difference has mean zero and must be zero almost surely. Completeness is the extra hypothesis that step needs.

## Worked example — One zero in four Poisson draws

**Your turn.** Keep \(n=4\) and estimate \(\mathbb{P}(X_1=0)\) when \(T=2\). Give \(U(2)\) and the plug-in \(e^{-T/n}\), to four decimals for the plug-in.

::: {.callout-tip collapse="true" title="Answer"}
\(U(2)=(3/4)^2=9/16=0.5625\). The plug-in is \(e^{-1/2}=0.6065\) to four decimals. It is larger, which is the direction Jensen's inequality requires on average, though one sample does not by itself prove the bias.
:::

## Connections — Bounds, sufficiency and completeness
An estimator that meets the [Cramér–Rao lower bound](cramer-rao-lower-bound.qmd) at every \(\theta\) is uniformly minimum-variance unbiased, because nothing unbiased can undercut that bound. The converse fails: the normal [sample variance](sample-variance-and-standard-deviation.qmd) with divisor \(n-1\) is the unbiased estimator built from the complete sufficient residual sum, and it does not attain the one-parameter information bound for \(\sigma^2\). The variance drop from conditioning is the [Rao–Blackwell theorem](rao-blackwell-theorem.qmd). Completeness is the extra property, beyond a [sufficient statistic](sufficient-statistic.qmd), that makes the unbiased function unique.{{cite:siegrist2022_sufficient_complete}} (§7.6, Properties of Sufficient Statistics and Complete Statistics)

## Check yourself
### A single success shared by two observations
For \(n=2\), \(k=0\) and \(T=1\), compute \(U(1)\).

::: {.callout-tip collapse="true" title="Answer"}
\(U(1)=(1/2)^1=1/2\). Given one success in total, it falls on the second observation with probability \(1/2\), so the conditional probability that the first observation is zero is \(1/2\).
:::

### Where the plug-in is not unbiased
Why is \(e^{-\overline X}\) not uniformly minimum-variance unbiased for \(e^{-\theta}\) in an independent Poisson sample?

::: {.callout-tip collapse="true" title="Answer"}
It is not unbiased. Strict convexity of \(e^{-x}\) and Jensen's inequality give \(\mathbb{E} e^{-\overline X}>e^{-\theta}\) whenever \(\overline X\) is non-degenerate. The unbiased class does not contain this plug-in, so the minimum-variance competition among unbiased estimators does not include it.
:::
