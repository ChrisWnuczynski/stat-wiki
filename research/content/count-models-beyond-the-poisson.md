## Lead context
A mixture of Poisson rates adds the variance of the random rate to the variance of the count, so the count variance is the mean plus a nonnegative extra term and cannot fall below the Poisson mean.

## Motivating example — A mixture of visit rates is wider than one Poisson
A clinic records how many asthma visits each patient makes in a year. A Poisson model with mean $4$ says the variance is also $4$, because a Poisson count has mean, variance and every cumulant equal to $\mu$.{{cite:mccullagh_nelder1989}} (§6.2.1, p. 195) Patients differ in unrecorded severity, so the visit counts mix several Poisson rates. The mixture is wider than any single Poisson with the same average: the variance of the random rate is added to the mean.{{cite:mccullagh_nelder1989}} (§6.2.3, p. 198) A model that can be drawn from, and that allows this extra spread, is the usual next step. A count that is instead tighter than a Poisson needs a different family again.

## Intuition — The mean fixes a Poisson, and then it does not
For a Poisson random variable the probability function $e^{-\mu}\mu^{x}/x!$ has no second free parameter with which to stretch the variance while holding the mean still.{{cite:mccullagh_nelder1989}} (§6.2.1, pp. 194–195) If the rate itself is random, the law of total variance adds the variance of that rate to the average Poisson variance. The sum is larger than the mean whenever the rate is not constant. Counts that are tighter than the mean cannot come from that mixture: every Poisson component already has variance equal to its own mean, and mixing adds a nonnegative term.{{cite:mccullagh_nelder1989}} (§6.2.3, p. 198) Greenwood and Yule treated the ordinary Poisson series as the standard for a constant chance, and as a lower limit on the variation once that chance is allowed to differ between people.{{cite:greenwood_yule1920}} (§I, p. 257)

## Definition — Extra variance from a random rate, and two other accounts
Let $Y\mid\lambda\sim\mathrm{Poisson}(\lambda)$ and let $\lambda$ be a positive random variable with mean $\mu$ and variance $\tau$. Then
$$
\mathrm{E}(Y)=\mu,\qquad \operatorname{Var}(Y)=\mu+\tau.
$$
One useful choice, not the only one, takes $\tau=\mu^{2}/\nu$ for a concentration $\nu>0$, so the variance is $\mu+\mu^{2}/\nu$. A gamma mixture with constant index produces that quadratic variance.{{cite:mccullagh_nelder1989}} (§6.2.3, p. 199; p. 352){{cite:ver_hoef_boveng2007}} (p. 2767, eq. 2) A quasi-Poisson description instead multiplies the mean by a constant $\phi$ and does not, by itself, name a distribution one can simulate.{{cite:mccullagh_nelder1989}} (§9.1, pp. 323–324){{cite:ver_hoef_boveng2007}} (p. 2767) The [Conway–Maxwell–Poisson distribution](conway-maxwell-poisson-distribution.qmd) is a third route. Its probability function is proportional to $\lambda^{y}/(y!)^{\nu}$. At $\nu=1$ it is Poisson. For $\nu>1$ the factorials in the denominator fall faster and the counts concentrate; for $0\le\nu<1$ they spread out. In that scaling $\lambda$ is not the mean.

## Properties — Why mixing widens the count
The variance addition does not need a gamma mixing distribution. Any non-degenerate distribution on the Poisson rate raises the variance above the mean.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Condition on $\lambda$. Then $\mathrm{E}(Y\mid\lambda)=\lambda$ and $\operatorname{Var}(Y\mid\lambda)=\lambda$, because a Poisson random variable has variance equal to its mean.{{cite:mccullagh_nelder1989}} (§6.2.1, p. 195) The law of total expectation gives $\mathrm{E}(Y)=\mathrm{E}(\lambda)=\mu$. The law of total variance gives
$$
\operatorname{Var}(Y)=\mathrm{E}\bigl(\operatorname{Var}(Y\mid\lambda)\bigr)+\operatorname{Var}\bigl(\mathrm{E}(Y\mid\lambda)\bigr)=\mathrm{E}(\lambda)+\operatorname{Var}(\lambda)=\mu+\tau.
$$
If $\tau>0$, then $\operatorname{Var}(Y)>\mu$. If $\lambda$ is almost surely constant, $\tau=0$ and the Poisson variance returns. A gamma law for $\lambda$ is one choice that makes $\tau=\mu^{2}/\nu$; the inequality itself uses only that a variance is nonnegative.{{cite:mccullagh_nelder1989}} (§6.2.3, p. 198)
:::
:::

The same identity shows why a negative-binomial variance cannot describe underdispersion. The term $\mu^{2}/\nu$ is positive for finite $\nu$, so $\mu+\mu^{2}/\nu>\mu$. Sending $\nu\to\infty$ removes the extra term and recovers the Poisson boundary. It does not cross that boundary. The second moment of the negative binomial series is necessarily greater than its mean, while the second moment of the positive binomial falls short of its mean.{{cite:greenwood_yule1920}} (p. 279){{cite:mccullagh_nelder1989}} (§6.2.3, p. 199)

Changing the variance function also changes the estimating weights. For a log link the derivative of the inverse link is the mean, so the iteratively weighted least-squares weights are inversely proportional to the variance function. A variance proportional to $\mu$ weights large counts differently from a variance $\mu+\kappa\mu^{2}$ that levels off.{{cite:ver_hoef_boveng2007}} (p. 2768)

## Statistical use — Match the parameter to the mean before comparing fits
A regression coefficient is easiest to compare across count models when it multiplies the log of the mean. A Poisson log-linear model and a negative-binomial model with the same linear predictor both speak about $\mu$.{{cite:mccullagh_nelder1989}} (§6.1, eq. 6.2, p. 194) A Conway–Maxwell–Poisson model written in the rate $\lambda$ does not: $\lambda$ is not $\mu$, and neither the mean nor the variance has a closed form in $\lambda$ and $\nu$. A mean parameterisation solves for the rate that delivers a prescribed mean, and then a coefficient can be compared with the Poisson coefficient. Until that translation is made, a smaller AIC on the $\lambda$ scale is not evidence about the mean. The [Conway–Maxwell–Poisson distribution](conway-maxwell-poisson-distribution.qmd) records that reparameterisation.

Quasi-Poisson estimation keeps a score that is the Poisson score divided by a common $\phi$. The point estimates of the mean coefficients do not move when $\phi$ moves. The standard errors do: the covariance is the Poisson information multiplied by $\phi$.{{cite:mccullagh_nelder1989}} (§9.2.3, eqs. 9.5–9.6, p. 327) That is a correction for spread, not a generative model.{{cite:ver_hoef_boveng2007}} (p. 2767)

## Worked example — A two-point mixture with mean four and variance eight
Suppose the rate equals $2$ or $6$ with equal probability $1/2$. The mean rate is $(2+6)/2=4$. The variance of the rate is
$$
\frac{(2-4)^{2}+(6-4)^{2}}{2}=4.
$$
A Poisson count at a random rate of this kind has mean $4$ and variance $4+4=8$. A Poisson random variable with the same mean would have variance $4$, and $P(Y=0)=e^{-4}\approx 0.0183$. The mixture probability of a zero is the average of two Poisson probabilities,
$$
\frac{e^{-2}+e^{-6}}{2}\approx 0.0689,
$$
about $3.76$ times the single-Poisson value, because the low rate contributes many zeros. The negative-binomial formula with $\mu=4$ and $\nu=2$ gives variance $4+16/2=12$ only for a different mixing distribution; the two-point mixture is the smaller illustration, and its variance $8$ is already twice the Poisson benchmark.{{cite:mccullagh_nelder1989}} (§6.2.3, p. 199)

**Your turn.** Use the same two rates but put probability $3/4$ on rate $2$ and probability $1/4$ on rate $6$. Find the mean and the variance of the resulting count.

::: {.callout-tip collapse="true" title="Answer"}
The mean rate is $(3/4)\cdot 2+(1/4)\cdot 6=3$. The variance of the rate is $(3/4)(2-3)^{2}+(1/4)(6-3)^{2}=3/4+9/4=3$. The count therefore has mean $3$ and variance $3+3=6$. The Poisson benchmark with the same mean would have variance $3$, so the mixture is still twice as wide.
:::

## Common misconceptions — Excess variance does not identify a negative binomial
Equal mean and variance is a property of the Poisson law, not a property of every count.{{cite:mccullagh_nelder1989}} (§6.2.1, p. 195) A sample variance larger than the sample mean does not by itself identify a negative binomial: any mixture with $\tau>0$ has the same qualitative excess, and a quasi-Poisson factor $\phi>1$ describes the excess without naming a full distribution.{{cite:mccullagh_nelder1989}} (§6.2.3, p. 198; §9.1, pp. 323–324) A negative-binomial fit cannot be rescued into underdispersion by taking $\nu$ small. Small $\nu$ makes $\mu^{2}/\nu$ large and the variance larger, not smaller. Finally, a Conway–Maxwell–Poisson coefficient on $\lambda$ is not a log-mean coefficient. Comparing it with a Poisson slope as if both multiplied $\mu$ misstates the regression.

## Assumptions and limits — When the variance identity is the wrong target
The identity $\operatorname{Var}(Y)=\mu+\tau$ assumes that, given the rate, the count is Poisson, so the conditional variance equals the conditional mean. A count that cannot exceed a small integer can be tighter than a Poisson with the same mean. No distribution of a Poisson rate produces that pattern, because $\tau$ cannot be negative. The Conway–Maxwell–Poisson family can, through $\nu>1$, but the probability of each count then requires the normalising series $\sum_{j\ge 0}\lambda^{j}/(j!)^{\nu}$, which is not $e^{\lambda}$ except at $\nu=1$.

A second failure is interpretive. Extra-Poisson variance estimated from a regression is variance given the covariates. A large marginal variance can be produced by a mean that changes with $x$, even when the conditional law is exactly Poisson. Mixing over an omitted covariate and mixing over a latent rate are different stories, and a variance formula does not decide which one produced the table. The mean equation is the part to check first.{{cite:mccullagh_nelder1989}} (§6.1, p. 194)

## Connections — Poisson, a gamma mixture, and a family that can be tight
The [Poisson distribution](poisson-distribution.qmd) is the equal-mean-and-variance boundary. The [negative binomial distribution](negative-binomial-distribution.qmd) is the gamma mixture, and the [Conway–Maxwell–Poisson distribution](conway-maxwell-poisson-distribution.qmd) is the family that also allows underdispersion. A [dispersion parameter](dispersion-parameter.qmd) in a quasi-Poisson fit rescales standard errors without adding a simulable law. [Overdispersion](overdispersion.qmd) and [underdispersion](underdispersion.qmd) name the two directions in which a count sample can leave the Poisson variance. A later regression for extra zeros, the zero-inflated Poisson, mixes a point mass at zero with a Poisson count and lets both the inflation probability and the Poisson mean depend on covariates.{{cite:lambert1992_zip}} (abstract, p. 1)

## Check yourself
### A mixture variance
A rate equals $1$ or $5$ with equal probability. What are the mean and the variance of a Poisson count drawn at that rate?

::: {.callout-tip collapse="true" title="Answer"}
The mean rate is $3$. The rate variance is $\bigl((1-3)^{2}+(5-3)^{2}\bigr)/2=4$. The count has mean $3$ and variance $3+4=7$.
:::

### Which family can be tight?
A sample of counts has mean $4$ and variance $2$. Which of a Poisson model, a negative-binomial model, and a Conway–Maxwell–Poisson model with $\nu>1$ can represent that pair of moments, and why do the other two fail?

::: {.callout-tip collapse="true" title="Answer"}
The Poisson model forces the variance to equal $4$. The negative binomial forces the variance to exceed $4$. Only the Conway–Maxwell–Poisson law with $\nu>1$ is built to be tighter than the Poisson with a comparable mean. Whether a particular $(\lambda,\nu)$ hits variance $2$ at mean $4$ is a numerical question about the normalising series, but the other two families are algebraically incapable of the inequality $\operatorname{Var}(Y)<\mathrm{E}(Y)$.
:::

## History — From a constant chance to a varying liability
Greenwood and Yule took the ordinary Poisson series as the standard for a constant chance of accident, and they treated it as a lower limit on the variation.{{cite:greenwood_yule1920}} (§I, p. 257) They then let each person's liability vary. The infinitely compound Poisson distribution gives each person a Poisson count with their own $\lambda$, and $\lambda$ follows a skew curve on the non-negative line. The resulting series is fitted from the mean and the second moment, and it graduated the accident counts where the simple Poisson series did not.{{cite:greenwood_yule1920}} (§IV, pp. 273–276) In the later generalised-linear-model account the same construction is a gamma mixture, with variance $\mu+\mu^{2}/v$ when the gamma index is constant, and the alternative that does not choose a mixing distribution is a single multiplier on the Poisson variance.{{cite:mccullagh_nelder1989}} (§6.2.3, p. 199; §6.1, pp. 193–194) The identity $\operatorname{Var}(Y)=\mu+\tau$ is why a random Poisson rate cannot repair a sample that is tighter than its mean. A regression that instead mixes a structural zero with a Poisson count, letting both pieces depend on covariates, is the zero-inflated Poisson model.{{cite:lambert1992_zip}} (abstract, p. 1; §2, p. 3)
