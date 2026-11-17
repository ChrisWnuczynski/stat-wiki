## Motivating example
A scientist estimates an unknown location from a few noisy measurements but has no defensible prior centre. Giving every possible value of that location the same *density* leads to a posterior shaped like the likelihood. The calculation can be useful, yet the constant density over the entire real line is not itself a probability distribution. Whether its posterior exists, and what “equal” means, therefore matter before an interval or prediction is reported.{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 51–52)

## Intuition
A prior is flat relative to a chosen measure and coordinate. Uniform density on a finite interval is a proper distribution: equal-length intervals have equal prior probability. A positive constant density on all of $\mathbb R$ has infinite integral, so it is an improper kernel used in Bayes' formula only when the likelihood supplies a finite normalising integral. Broad proper priors can approximate some resulting posteriors locally, but as their range expands they do not approach a uniform *probability* on the entire line. The widening-slab calculation in the definition makes that distinction explicit.{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 51–52)

## Definition
For a scalar parameter $\theta$ in a stated coordinate, a flat prior has density $\pi(\theta)=c$ on its support, where $c$ is a normalising constant if the support has finite length and an arbitrary positive multiplier if it does not. A posterior based on an improper flat kernel exists only when $0<\int L(\theta;y)\,d\theta<\infty$. In that case $\pi(\theta\mid y)=L(\theta;y)/\int L(u;y)\,du$. The resulting mode coincides with a likelihood maximiser when one exists, but a posterior mean or interval is generally different from that mode.{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–53)

## Interpretation
Consider a binomial success probability $p\in(0,1)$. A uniform $\operatorname{Beta}(1,1)$ prior is proper and flat in $p$. Under $\eta=\log\{p/(1-p)\}$, the *same* prior has density proportional to $e^\eta/(1+e^\eta)^2$, not a constant. A prior flat in $\eta$ instead has kernel $1/[p(1-p)]$ in $p$. These represent different prior assumptions even though each can be called “flat” in its own coordinate. Jeffreys' rule addresses this coordinate dependence through Fisher information, and for the binomial parameter yields $\operatorname{Beta}(1/2,1/2)$ rather than the uniform $\operatorname{Beta}(1,1)$.{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–53, equations 2.19–2.20)

## Properties
With $Y_i\mid\mu\overset{\mathrm{iid}}\sim N(\mu,\sigma^2)$ and known $\sigma^2$, a flat kernel on $\mu\in\mathbb R$ gives $\mu\mid y\sim N(\bar y,\sigma^2/n)$ for $n\geq1$. The likelihood is integrable in $\mu$ because its quadratic exponent rises away from $\bar y$. This is one case in which the formal improper prior gives a proper posterior. It does not provide a prior predictive distribution: integrating the sampling law against an infinite prior measure does not produce probabilities summing to one.{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 51–52)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Complete the square: $\sum_i(y_i-\mu)^2=\sum_i(y_i-\bar y)^2+n(\mu-\bar y)^2$. Multiplying the normal likelihood by a constant kernel leaves, as a function of $\mu$, $\exp\{-n(\mu-\bar y)^2/(2\sigma^2)\}$. Its integral is $\sqrt{2\pi\sigma^2/n}$ times a factor independent of $\mu$, so normalisation gives $N(\bar y,\sigma^2/n)$. For the coordinate claim, $p=e^\eta/(1+e^\eta)$ has derivative $dp/d\eta=p(1-p)$. A constant density in $p$ therefore becomes proportional to $p(1-p)$ in $\eta$; a constant density in $\eta$ becomes proportional to $1/[p(1-p)]$ in $p$.{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–53)
:::
:::

## Statistical use — A constant weight on the parameter
State the parameter coordinate, support and base measure when describing a flat prior. Check posterior propriety by integrating the likelihood times the prior kernel. Then ask whether posterior summaries change materially under plausible proper alternatives, such as a broad normal prior for a location or a modest Beta prior for a probability. When likelihood information is weak, the prior's support and tails can dominate the answer even if its density appears visually low and nearly constant over a small range.{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–54)

With no observations, the constant kernel on $\mathbb R$ remains nonintegrable, so it has no posterior. Under a binomial model, a prior flat on log-odds is proportional to $1/[p(1-p)]$ in $p$; if every trial is a success or every trial is a failure, the posterior integral diverges at one endpoint. A proper uniform prior on $[-5,5]$ cannot represent a true normal mean of $8$, since its posterior is forced to remain inside $[-5,5]$. These are failures of normalisation or support, not algebraic defects in Bayes' rule.{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 53–54)

## Worked example
Four independent readings $y=(9,11,10,12)$ follow a normal model with known standard deviation $\sigma=2$. Their mean is $10.5$. Under $\pi(\mu)\propto1$ on $\mathbb R$, the posterior is $N(10.5,2^2/4)=N(10.5,1)$, with posterior standard deviation $1$. A central normal 95% credible interval is $10.5\pm1.96=(8.54,12.46)$. The posterior is proper because the likelihood has finite integral in $\mu$; the calculation does not imply that a uniform probability distribution on all real means existed before the readings.{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 51–52)

**Your turn.** Four independent normal readings are $(6,9,12,9)$ with known $\sigma=3$. Use a flat kernel for the unknown mean. Find the posterior standard deviation and a central 95% credible interval.

::: {.callout-tip collapse="true" title="Answer"}
The sample mean is $9$ and the posterior variance is $3^2/4=2.25$, so the standard deviation is $1.5$. The interval is $9\pm1.96(1.5)=(6.06,11.94)$. Its interpretation is conditional on the normal likelihood and the formal flat-kernel calculation.
:::

## Common misconceptions
“Flat” is not an absolute synonym for ignorance: changing coordinates changes which values receive equal density. A flat kernel on an unbounded domain is not a broad probability distribution; it has no normalising constant. A posterior mode equal to the maximum-likelihood estimate does not make every posterior summary equal to its frequentist analogue. And an apparently weak proper uniform prior with a hard upper bound still assigns exactly zero posterior probability beyond that bound, regardless of the data.{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–54)

## Assumptions and limits — Flatness depends on the coordinate
“Flat” is not an absolute synonym for ignorance: changing coordinates changes which values receive equal density. {{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–54)

## Connections
An [improper prior](improper-prior.qmd) requires a posterior propriety check, while a [normal–normal update](normal-normal-conjugacy.qmd) shows how a proper broad normal prior approaches the location calculation. The [improper-normal question](../questions/ex-improper-normal.qmd) adds an unknown variance, where propriety needs more care; the [geometric-observation question](../questions/ex-applied-geometric.qmd) uses a proper uniform prior on a bounded probability; the [model-odds question](../questions/q-11.qmd) uses its normalising constant to compute a Bayes factor.{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–54)

## History
Gelman and colleagues describe the uniform $\operatorname{Beta}(1,1)$ prior for a binomial probability as the Bayes–Laplace choice, and contrast it with Jeffreys' information-based $\operatorname{Beta}(1/2,1/2)$ prior. Jeffreys published *Theory of Probability* in 1939; his invariance principle sought a prior rule that transforms consistently between parameter coordinates. The two choices remain useful examples of why “noninformative” requires a specified model and scale.{{cite:gelman_bda2013}} (Ch. 2, §2.8, pp. 52–53){{cite:dodge2008}} (p. 274, “Jeffreys, Harold”)
