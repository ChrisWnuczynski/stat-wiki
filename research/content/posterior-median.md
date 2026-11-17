## Motivating example

A public-health study estimates the chance of an adverse event. Its posterior distribution is skewed because few events were observed, so the mean, median and most likely value do not coincide. If the reported single number will be judged by absolute error in the unknown chance, the median of the posterior is the appropriate choice.{{cite:gelman_bda2013}} (Ch. 2, §§2.1, 2.3, pp. 29–34) The full posterior still matters for the range of plausible chances and for decisions with different costs.

## Intuition — Why absolute loss selects the median

A median divides posterior probability so that at least half lies on either side. Moving a proposed estimate slightly to the right reduces error for parameter values above it and increases error for those below it. At a median, those opposing effects balance under absolute-error loss. This is a decision statement about an unknown parameter conditional on observed data; it is not the median of the raw observations unless a particular model happens to make them equal.

Posterior shape determines how far this summary lies from others. In a symmetric unimodal posterior, mean, median and mode agree. For a right-skewed posterior the long upper tail usually pulls the mean above the median, while the mode can lie below it. None of these points alone shows how uncertain the parameter remains. A credible interval or a plot of the posterior should accompany a point summary when uncertainty matters.

## Definition

Given data $x$ and a scalar posterior distribution for $\theta$, a posterior median $m$ satisfies $\Pr(\theta\leq m\mid x)\geq1/2$ and $\Pr(\theta\geq m\mid x)\geq1/2$. For a continuous strictly increasing posterior CDF, it is the unique solution of $F(m\mid x)=1/2$. A discrete posterior can have an interval of medians; any value in that interval minimizes posterior expected absolute error.{{cite:gelman_bda2013}} (Ch. 2, §§2.1, 2.3, pp. 29–34) Reporting a conventional midpoint is possible, but the data do not single it out as a unique decision.

This definition presumes a proper posterior. An unnormalized kernel that cannot be integrated has no posterior probabilities and hence no posterior median. A point summary of a multivariate parameter also needs a specified target, such as one component or a scientifically meaningful function of the whole vector.

## Properties

Under loss $L(a,\theta)=|a-\theta|$, a posterior median minimizes $\mathbb E[L(a,\theta)\mid x]$ when the posterior has a finite first absolute moment. In regular cases, the mean instead minimizes squared error, and a mode is connected to a different, local loss criterion. A strictly increasing transformation $g$ carries a posterior median $m$ to a median $g(m)$ of $g(\theta)$. This equivariance helps when reporting a rate on a log-odds or odds scale; a posterior mean does not generally transform in the same way.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For a continuous posterior with density $p$, set $R(a)=\int|a-\theta|p(\theta\mid x)\,d\theta$. Differentiating from the right and left gives slopes determined by $\Pr(\theta<a\mid x)-\Pr(\theta>a\mid x)$, with the posterior atom at $a$ accounting for any gap between them. Convexity of absolute value makes $a$ a minimizer exactly when zero lies between the one-sided slopes, equivalent to at least half the mass on each side. For a strictly increasing $g$, the events $\{g(\theta)\leq g(m)\}$ and $\{\theta\leq m\}$ coincide, as do their reversed inequalities, proving median equivariance. For squared loss, expand $\mathbb E[(\theta-a)^2\mid x]=\operatorname{Var}(\theta\mid x)+(a-\mathbb E[\theta\mid x])^2$ when the second moment exists.
:::
:::

## Interpretation

With a Beta$(3,9)$ posterior for a probability, the median is about $0.2358$, the mean is $3/12=0.25$, and the density mode is $(3-1)/(3+9-2)=0.20$. The three numbers answer different questions. The median balances absolute deviations in the *probability* scale; transforming it to odds gives a median on the odds scale. Recomputing an arithmetic mean after transforming would generally produce a different answer from transforming $0.25$.

The median is also the central dividing point for an equal-tailed credible interval. It is not, in general, the arithmetic midpoint of that interval: unequal tails in the coordinate scale can give asymmetric distances to its endpoints. Nor is the posterior median automatically an optimal forecast of a future observation. Prediction uses the posterior predictive distribution, which includes sampling variability beyond uncertainty about $\theta$.

## Statistical use

For an analytic posterior, solve its CDF equation or use its quantile function. For posterior draws, sort scalar draws and take the sample median. With an even number of draws, software usually averages the two central values, although any point between them minimizes the sample absolute-deviation criterion. Monte Carlo error remains: a median from a short or poorly mixed Markov chain may be unstable. Repeated chains or a suitable simulation error estimate help judge that stability.

When a posterior is highly skewed, show the median together with quantiles and a description of the scale. A median of a rate per person-year, for example, should retain that unit. If the practical costs of overestimation and underestimation differ, use the appropriate posterior quantile instead of assuming the median still minimizes the actual cost.

If the posterior is improper, its “half the mass” criterion is undefined. In the discrete example, there is no unique median, so a report that insists on one exact value hides a genuine range of equally good actions. If a decision costs four times as much when an event rate is underestimated as when it is overestimated, the posterior median targets the wrong loss; a higher quantile is appropriate. A badly mixing chain can also make an empirical median look precise when its Monte Carlo uncertainty is substantial.
## Worked example

Suppose the posterior probability of an event is Beta$(3,9)$. Numerically solving $F(m)=0.5$ gives $m\approx0.2358$. The mean is $0.25$ and the mode is $0.20$, so reporting only “about a quarter” conceals the skewness. The equal-tailed 95% credible interval is approximately $(0.0602,0.5178)$; its midpoint is $0.2890$, not the posterior median. The posterior median says half the posterior probability lies below about $0.236$ and half above it, conditional on the model and data.

**Your turn.** A discrete posterior puts probability $0.2$ on $\theta=0$, probability $0.3$ on $\theta=1$, and probability $0.5$ on $\theta=4$. Find all posterior medians, the posterior mean, and the expected absolute error at actions $1$, $2$ and $4$.

::: {.callout-tip collapse="true" title="Answer"}
Any $m\in[1,4]$ is a median: at least half the mass lies at or below it and at least half at or above it. The mean is $0.2(0)+0.3(1)+0.5(4)=2.3$. At $a=1$, the absolute-error risk is $0.2(1)+0.3(0)+0.5(3)=1.7$; at $a=2$ it is $0.2(2)+0.3(1)+0.5(2)=1.7$; at $a=4$ it is $0.2(4)+0.3(3)+0.5(0)=1.7$. The flat risk between $1$ and $4$ explains the nonuniqueness.
:::

## Common misconceptions

A posterior median is not generally the median of the observations. It is also not generally the same as a posterior mean or mode; their loss functions and sensitivity to tails differ. The median need not be the midpoint of an equal-tailed interval. Finally, it is a posterior probability summary of a parameter, not a repeated-sampling guarantee about the data-generating process.

## Connections

The [posterior mean](posterior-mean.qmd) is the squared-error Bayes action, while the [maximum a posteriori estimate](maximum-a-posteriori-estimate.qmd) uses a density peak. [Credible-region constructions](credible-region-constructions.qmd) summarize more of the posterior than one point. [Posterior summaries from draws](posterior-summaries-from-draws.qmd) shows how quantiles are estimated from simulation. The ordinary [median](median.qmd) applies the same centrality idea to a sampling distribution or a data set.

## History

The median's use as an ordered-data summary predates posterior decision theory. Euler and Mayer independently described procedures for dividing ordered observations into two halves in 1748.{{cite:dodge2008}} (p. 346, “Median”) The posterior median applies a related dividing criterion to probability assigned to parameter values after observing data.
