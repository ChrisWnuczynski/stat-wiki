## Lead context
A Poisson count has variance equal to its mean, and many counted outcomes are wider or tighter than that.{{cite:dodge2008}} (p. 426)

## Motivating example
A clinic records how many asthma visits each patient makes in a year. A Poisson model with mean $4$ says the variance is also $4$, so a year with a dozen visits is a tail event of a tightly specified law. Patients differ in unrecorded severity, so the visit counts mix several Poisson rates. The mixture is wider than any single Poisson with the same average. A model that can be drawn from, and that allows this extra spread, is the usual next step; a count that is instead tighter than a Poisson needs a different family again.{{cite:dodge2008}} (pp. 425–426)

## Intuition — The mean fixes a Poisson, and then it does not
For a Poisson random variable with mean $\theta$, both the expectation and the variance equal $\theta$. The probability function $e^{-\theta}\theta^{x}/x!$ has no second free parameter with which to stretch the variance while holding the mean still. If the rate itself is random, the law of total variance adds the variance of that rate to the average Poisson variance. The sum is larger than the mean whenever the rate is not constant. Counts that are tighter than the mean cannot come from that mixture: every Poisson component already has variance equal to its own mean, and mixing adds a nonnegative term.{{cite:dodge2008}} (p. 426)

## Definition
Let $Y\mid\lambda\sim\mathrm{Poisson}(\lambda)$ and let $\lambda$ be a positive random variable with mean $\mu$ and variance $\tau$. Then
$$
\mathrm{E}(Y)=\mu,\qquad \operatorname{Var}(Y)=\mu+\tau.
$$
The negative-binomial specification on this page takes $\tau=\mu^{2}/\nu$ for a concentration $\nu>0$, so the variance is $\mu+\mu^{2}/\nu$. A quasi-Poisson description instead multiplies the mean by a constant $\phi$ and does not, by itself, name a distribution one can simulate. The Conway–Maxwell–Poisson probability function is proportional to $\lambda^{y}/(y!)^{\nu}$. At $\nu=1$ it is Poisson. For $\nu>1$ the factorials in the denominator fall faster and the counts concentrate; for $0\le\nu<1$ they spread out. In that scaling $\lambda$ is not the mean.{{cite:dodge2008}} (pp. 425–426)

## Properties — A two-point mixture is already overdispersed
The variance addition does not need a gamma mixing distribution. Any non-degenerate distribution on the Poisson rate raises the variance above the mean.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Condition on $\lambda$. Then $\mathrm{E}(Y\mid\lambda)=\lambda$ and $\operatorname{Var}(Y\mid\lambda)=\lambda$, because a Poisson random variable has variance equal to its mean. The law of total expectation gives $\mathrm{E}(Y)=\mathrm{E}(\lambda)=\mu$. The law of total variance gives
$$
\operatorname{Var}(Y)=\mathrm{E}\bigl(\operatorname{Var}(Y\mid\lambda)\bigr)+\operatorname{Var}\bigl(\mathrm{E}(Y\mid\lambda)\bigr)=\mathrm{E}(\lambda)+\operatorname{Var}(\lambda)=\mu+\tau.
$$
If $\tau>0$, then $\operatorname{Var}(Y)>\mu$. If $\lambda$ is almost surely constant, $\tau=0$ and the Poisson variance returns. A gamma law for $\lambda$ is one choice that makes $\tau=\mu^{2}/\nu$; the inequality itself uses only that a variance is nonnegative.{{cite:dodge2008}} (p. 426)
:::
:::

The same identity shows why a negative-binomial variance cannot describe underdispersion. The term $\mu^{2}/\nu$ is positive for finite $\nu$, so $\mu+\mu^{2}/\nu>\mu$. Sending $\nu\to\infty$ removes the extra term and recovers the Poisson boundary. It does not cross that boundary.

## Statistical use — Match the parameter to the mean before comparing fits
A regression coefficient is easiest to compare across count models when it multiplies the log of the mean. A Poisson log-linear model and a negative-binomial model with the same linear predictor both speak about $\mu$. A Conway–Maxwell–Poisson model written in the rate $\lambda$ does not: $\lambda$ is not $\mu$, and neither the mean nor the variance has a closed form in $\lambda$ and $\nu$. A mean parameterisation solves for the rate that delivers a prescribed mean, and then a coefficient can be compared with the Poisson coefficient. Until that translation is made, a smaller AIC on the $\lambda$ scale is not evidence about the mean.{{cite:dodge2008}} (p. 426)

Quasi-Poisson estimation keeps the Poisson score equations and then rescales standard errors by $\sqrt{\phi}$. The point estimates of the mean coefficients do not move when $\phi$ moves. The standard errors do. That is a correction for spread, not a generative model.

## Worked example
Suppose the rate equals $2$ or $6$ with equal probability $1/2$. The mean rate is $(2+6)/2=4$. The variance of the rate is
$$
\frac{(2-4)^{2}+(6-4)^{2}}{2}=4.
$$
A Poisson count at a random rate of this kind has mean $4$ and variance $4+4=8$. A Poisson random variable with the same mean would have variance $4$, and $P(Y=0)=e^{-4}\approx 0.0183$. The mixture probability of a zero is the average of two Poisson probabilities,
$$
\frac{e^{-2}+e^{-6}}{2}\approx 0.0689,
$$
about $3.76$ times the single-Poisson value, because the low rate contributes many zeros. The negative-binomial formula with $\mu=4$ and $\nu=2$ gives the same variance $4+16/2=12$ only for a different mixing distribution; the two-point mixture is the smaller illustration, and its variance $8$ is already twice the Poisson benchmark.{{cite:dodge2008}} (p. 426)

**Your turn.** Use the same two rates but put probability $3/4$ on rate $2$ and probability $1/4$ on rate $6$. Find the mean and the variance of the resulting count.

::: {.callout-tip collapse="true" title="Answer"}
The mean rate is $(3/4)\cdot 2+(1/4)\cdot 6=3$. The variance of the rate is $(3/4)(2-3)^{2}+(1/4)(6-3)^{2}=3/4+9/4=3$. The count therefore has mean $3$ and variance $3+3=6$. The Poisson benchmark with the same mean would have variance $3$, so the mixture is still twice as wide.
:::

## Common misconceptions
Equal mean and variance is a property of the Poisson law, not a property of every count. A sample variance larger than the sample mean does not by itself identify a negative binomial: any mixture with $\tau>0$ has the same qualitative excess, and a quasi-Poisson factor $\phi>1$ describes the excess without naming a full distribution. A negative-binomial fit cannot be rescued into underdispersion by taking $\nu$ small. Small $\nu$ makes $\mu^{2}/\nu$ large and the variance larger, not smaller. Finally, a Conway–Maxwell–Poisson coefficient on $\lambda$ is not a log-mean coefficient. Comparing it with a Poisson slope as if both multiplied $\mu$ misstates the regression.{{cite:dodge2008}} (p. 426)

## Assumptions and limits — When the variance identity is the wrong target
The identity $\operatorname{Var}(Y)=\mu+\tau$ assumes that, given the rate, the count is Poisson, so the conditional variance equals the conditional mean. A count that cannot exceed a small integer, such as the number of bids a bankrupt firm receives, can be tighter than a Poisson with the same mean. No distribution of a Poisson rate produces that pattern, because $\tau$ cannot be negative. The Conway–Maxwell–Poisson family can, through $\nu>1$, but the probability of each count then requires the normalising series $\sum_{j\ge 0}\lambda^{j}/(j!)^{\nu}$, which is not $e^{\lambda}$ except at $\nu=1$.

A second failure is interpretive. Extra-Poisson variance estimated from a regression is variance given the covariates. A large marginal variance can be produced by a mean that changes with $x$, even when the conditional law is exactly Poisson. Mixing over an omitted covariate and mixing over a latent rate are different stories, and a variance formula does not decide which one produced the table.

## Connections
The [Poisson distribution](poisson-distribution.qmd) is the equal-mean-and-variance boundary. The [negative binomial distribution](negative-binomial-distribution.qmd) is the gamma mixture, and the [Conway–Maxwell–Poisson distribution](conway-maxwell-poisson-distribution.qmd) is the family that also allows underdispersion. A [dispersion parameter](dispersion-parameter.qmd) in a quasi-Poisson fit rescales standard errors without adding a simulable law. [Overdispersion](overdispersion.qmd) and [underdispersion](underdispersion.qmd) name the two directions in which a count sample can leave the Poisson variance.{{cite:dodge2008}} (pp. 425–426)

## History
Poisson’s 1837 derivation obtained the count law as a limit of binomial probabilities, and the modern entry records the probability function $e^{-\theta}\theta^{x}/x!$ together with the evaluation $\mathrm{E}(X)=\operatorname{Var}(X)=\theta$.{{cite:dodge2008}} (pp. 425–426) Later count regressions used that law as the baseline and added either a multiplicative dispersion, a mixture, or a second parameter in the factorial term when the baseline variance was too rigid. The mixture calculation above is the reason a random Poisson rate cannot repair a sample that is tighter than its mean.
