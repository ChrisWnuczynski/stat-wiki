## Motivating example — A varying call rate spreads the hourly count

A help desk may receive an average of three calls per hour yet have quiet hours and sudden busy ones. A Poisson model with mean three fixes the variance at three. If the underlying call rate changes from hour to hour, the count can vary more widely even when its overall mean remains three. The negative binomial distribution gives one precise account of that extra variation: it is the count law obtained when a Poisson rate itself follows a gamma distribution.{{cite:zeileis_kleiber_jackman2008}} (§2, pp. 4–5, count distributions and gamma mixture)

## Intuition — Gamma mixing creates extra count variation

Think of the conditional Poisson rate as a hidden feature of each hour. Conditional on a low rate, zero calls are common; conditional on a high rate, large counts are more common. Combining these hours creates both more zeros and a heavier upper tail than a single-rate Poisson law with the same average. The dispersion parameter $\nu$ controls how much the hidden rates vary: a small $\nu$ allows substantial variation, while a large $\nu$ concentrates the rate around $\mu$. The mass function and the cumulative distribution function describe that shape; neither summary says why the variation arose.{{cite:zeileis_kleiber_jackman2008}} (§2, pp. 4–5, mean–variance relation and mixture)

## Definition

In the mean–dispersion parameterisation, $X\sim\operatorname{NegBin}(\mu,\nu)$ has mean $\mu>0$, dispersion $\nu>0$, and mass function
$$
p(x)=\frac{\Gamma(x+\nu)}{\Gamma(\nu)\,x!}\left(\frac{\nu}{\mu+\nu}\right)^{\nu}\left(\frac{\mu}{\mu+\nu}\right)^{x}
$$
on $x=0,1,\ldots$. Another convention uses a success probability $p=\nu/(\mu+\nu)$ and a size $\nu$; for integer size it counts failures before the $\nu$th success. Then $\mu=\nu(1-p)/p$. The gamma function extends the combinatorial coefficient to any positive real $\nu$, so the distribution is useful even when there is no literal sequence of $\nu$ successes. Always check which of the two parameters a software function calls “size” and whether its geometric special case begins at zero or one.{{cite:zeileis_kleiber_jackman2008}} (§2, pp. 4–5, probability functions and parameterisations){{cite:dodge2008}} (pp. 369–370, “Negative Binomial Distribution,” mathematical aspects)

## Properties

The variance is $\mu+\mu^2/\nu$, exceeding $\mu$ for finite positive $\mu$ and $\nu$. The excess $\mu^2/\nu$ grows quadratically with the mean at fixed dispersion. Thus comparing groups only by a common additive variance is not equivalent to fitting this count law. In the gamma–Poisson construction, the mixing rate $\Lambda$ has mean $\mu$ and variance $\mu^2/\nu$; total variance adds the ordinary conditional Poisson variability $\mu$ to rate variability $\mu^2/\nu$. These two variance components describe variation within a fixed rate and variation between rates.{{cite:zeileis_kleiber_jackman2008}} (§2, pp. 4–5, gamma–Poisson mixture and variance)

The zero probability is $(\nu/(\mu+\nu))^\nu$. With mean three and $\nu=1$, this equals $1/4$, while a Poisson law of mean three gives $e^{-3}\approx0.0498$. At the other end, the chance of at least seven counts is $(3/4)^7\approx0.1335$ for this geometric case, compared with approximately $0.0335$ for the Poisson law. These comparisons make “overdispersion” concrete: the same mean can coexist with markedly different chances of a quiet or very busy hour. They do not imply that every dataset with excess zeros follows a negative binomial law. {{cite:zeileis_kleiber_jackman2008}} (§2, pp. 4–5, Poisson and negative-binomial count probabilities)

## Related distributions

Setting $\nu=1$ gives the geometric distribution on $0,1,2,\ldots$, whose success probability is $1/(1+\mu)$. Holding $\mu$ fixed while $\nu$ grows makes the gamma mixing rate concentrate and the negative binomial law approach a Poisson law. In the integer-size waiting-time account, the count is also a sum of independent geometric failure counts, one for each awaited success. The mixing and waiting-time stories lead to the same mass function but suggest different scientific mechanisms.{{cite:zeileis_kleiber_jackman2008}} (§2, pp. 4–5, geometric special case and Poisson limit){{cite:dodge2008}} (pp. 369–370, “Negative Binomial Distribution,” geometric sum)

## Statistical inference

For regression, one may let $\mu_i$ depend on predictors and keep the variance $\mu_i+\mu_i^2/\nu$ tied to its mean. The extra parameter must be estimated or fixed; a Poisson model has no corresponding free size parameter. A negative binomial fit can correct understated uncertainty when overdispersion follows this variance pattern. It is still necessary to inspect where the mismatch occurs. A hurdle process, a distinct structural-zero class, or unmodelled exposure differences can produce counts a single negative binomial regression describes poorly, even if its overall variance is large enough.{{cite:zeileis_kleiber_jackman2008}} (§2, pp. 4–5, overdispersion; §3, pp. 6–8, hurdle and zero-inflated models)

One comparison asks why the extra $\mu^2/\nu$ term matters. Another begins with the success-probability parameterisation and derives a link for a regression with fixed size. Together they test two distinct steps: recognizing the count variance and translating its parameterisation into an inferential model.

## Worked example — Mean three and $\nu=1$ against a Poisson benchmark

Suppose daily service requests are modelled with $\mu=3$ and $\nu=1$. Their variance is $3+3^2/1=12$. One quarter of days have no request under this model, whereas a same-mean Poisson model predicts about five percent. The negative binomial probability of seven or more requests is $0.1335$, about four times the Poisson probability $0.0335$. The comparison explains why fitting only an average count could underestimate both idle days and busy-day staffing needs. It does not establish a particular physical reason for the varying rate.{{cite:zeileis_kleiber_jackman2008}} (§2, pp. 4–5, model probabilities and overdispersion)

**Your turn.** A count has $\mu=2$ and $\nu=2$. Find its variance and its probabilities of zero and one count in the mean–dispersion parameterisation.

::: {.callout-tip collapse="true" title="Answer"}
The variance is $2+2^2/2=4$. Here $p=\nu/(\mu+\nu)=1/2$, so $P(X=0)=p^2=1/4$ and $P(X=1)=2p^2(1-p)=1/4$. Both probabilities are equal, but the distribution still has a long positive tail.
:::

## Common misconceptions — “Negative” does not mean a negative count

“Negative” does not mean the count can be negative: the support begins at zero. Size $\nu$ is not the mean $\mu$; changing it at fixed mean changes the variance and tails. A negative binomial law with real-valued $\nu$ need not represent a literal count of failures before a noninteger number of successes. Finally, extra variance alone does not identify gamma rate mixing, because dependence, structural zeros and omitted predictors can also spread a count distribution.{{cite:zeileis_kleiber_jackman2008}} (§2, pp. 4–5, parameterisations and model selection; §3, pp. 6–8, alternative count models)

## Assumptions and limits — Mixing does not license impossible counts

The gamma–Poisson story assumes nonnegative counts and a gamma distribution of conditional rates. If calls are capped at four by a scheduling rule, the negative binomial assigns positive probability to impossible counts above four. If each arrival provokes another, dependence between arrivals may produce bursts that do not follow a gamma mixture. If one group has exactly zero exposure, treating its zeros as observations from the same positive-mean distribution confuses exposure with dispersion. A count model should follow the observation mechanism, and residual patterns or held-out frequencies can reveal these failures.{{cite:zeileis_kleiber_jackman2008}} (§2, pp. 4–5, count-model assumptions; §3, pp. 6–8, excess-zero alternatives)

## Connections — The mixture pieces and the regression setting

[Poisson distribution](poisson-distribution.qmd) supplies the conditional count law in the mixture and the limiting law as $\nu$ grows. [Gamma distribution](gamma-distribution.qmd) supplies the fluctuating rate. [Geometric distribution](geometric-distribution.qmd) is the $\nu=1$ case on the failures-before-success convention. [Overdispersion](overdispersion.qmd) describes the variance diagnostic, while [Poisson regression](poisson-regression.qmd) and [count models beyond the Poisson](count-models-beyond-the-poisson.qmd) put the distribution into an inferential setting.{{cite:zeileis_kleiber_jackman2008}} (§2, pp. 4–5, distributional relationships and regression)

## History — From a series to Greenwood and Yule, then to a mixture

The name comes from the negative-binomial series used in the waiting-time mass function.{{cite:dodge2008}} (pp. 369–370, “Negative Binomial Distribution,” history and mathematical aspects) Greenwood and Yule studied repeated accidents by giving each person a Poisson count at a liability of their own and letting that liability vary across people. They fitted the compound series from the mean and the second moment.{{cite:greenwood_yule1920}} (§I, pp. 255–257; §IV, pp. 273–276) The same construction, written as a gamma mixture with constant index, has variance $\mu+\mu^2/v$.{{cite:mccullagh_nelder1989}} (§6.2.3, p. 199) Count regression uses that gamma–Poisson reading because the mean and the extra variance are the quantities the regression has to carry.{{cite:zeileis_kleiber_jackman2008}} (§2, pp. 4–5, gamma–Poisson interpretation)
