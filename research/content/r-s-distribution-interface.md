## Motivating example
A beta posterior supports distinct questions: how high its density is at a probability, how much mass lies below that probability, which probability is its median, and how to generate numerical draws. R's distribution-function naming convention separates these operations. Choosing the correct prefix is part of expressing the intended calculation.{{cite:r_stats_distributions2026}} (§Details, distribution-function naming convention)

## Definition — Prefixes identify operations rather than distributions
For a named family such as the beta, the `d` function evaluates a density or probability mass, `p` evaluates a cumulative probability, `q` evaluates a quantile and `r` generates pseudorandom observations. In R the functions are `dbeta`, `pbeta`, `qbeta` and `rbeta`. Their argument positions differ: `rbeta` takes a requested number of draws first, whereas `qbeta` takes a probability.{{cite:r_stats_beta2026}} (§Usage and §Value)

The underlying beta distribution on $(0,1)$ has density proportional to $\theta^{a-1}(1-\theta)^{b-1}$ for positive shapes $a,b$. Its mean is $a/(a+b)$. A density value at a single point is not a point probability: for a continuous law the probability of any one point is zero, while interval probabilities are integrals of the density. These are mathematical distinctions independent of R's naming convention.{{cite:siegrist2022_beta}} (§5.17, probability density and moments)

## Interpretation — Keep arguments and tails explicit
For $\theta\mid D\sim\operatorname{Beta}(3,9)$, `pbeta(0.5,3,9)` asks for $P(\theta\le0.5\mid D)$, while `qbeta(0.5,3,9)` asks for a median. Exchanging these operations changes both the input's role and the answer's meaning. In a continuous strictly increasing part of the distribution, applying the CDF to a $q$-quantile returns $q$; for a discrete distribution the quantile is a leftmost value attaining the requested cumulative probability, so exact inverse equalities need qualification.{{cite:r_stats_beta2026}} (§Arguments and §Value){{cite:siegrist2022_quantiles}} (§3.06, quantile functions)

R's `lower.tail=FALSE` option requests a strict upper tail rather than the default lower tail. For discrete variables, $P(X>k)$ differs from $P(X\ge k)$ by the probability mass at $k$. Logarithmic tail options can also reduce avoidable underflow in extreme calculations; they change the output scale, not the event being requested.{{cite:r_stats_beta2026}} (§Arguments, `lower.tail` and `log.p`)

## Worked example — Deterministic beta summaries
At $\theta=0.25$ the $\operatorname{Beta}(3,9)$ density is $3.097243$, which exceeds one without violating any probability axiom. Its cumulative probability below $0.5$ is $0.967285$, and its median is $0.235786$. Its equal-tailed 95% interval has endpoints $0.060218$ and $0.517756$. The posterior mean $0.250$ need not equal its median because this posterior is asymmetric. The beta density and its integrals determine these quantities before any simulation is run.{{cite:siegrist2022_beta}} (§5.17, density and moments)

The corresponding R expressions are `dbeta(0.25,3,9)`, `pbeta(0.5,3,9)`, `qbeta(0.5,3,9)` and `qbeta(c(0.025,0.975),3,9)`. R recycles numerical arguments according to the documented vectorisation rules, so a vector of probabilities can produce several quantiles in one call. Explicitly naming shape parameters is useful when several numerical arguments occur together.{{cite:r_stats_beta2026}} (§Usage and §Value, lengths and recycling)

**Your turn.** What is the posterior probability above $0.5$, and which R expression directly requests it?

::: {.callout-tip collapse="true" title="Answer"}
The upper probability is $1-0.96728515625=0.032715$ to six decimal places. The direct request is `pbeta(0.5,3,9,lower.tail=FALSE)`.
:::

## Statistical use — Simulation estimates an already specified quantity
Independent beta draws allow averages and indicator proportions to approximate the same posterior summaries. For example, the proportion exceeding $0.5$ estimates the upper probability above; it is a random numerical estimate, rather than a replacement definition of that probability. A beta–binomial update determines which beta shapes should be supplied in the first place. Using highly accurate numerical functions with incorrect shapes gives an accurate answer to the wrong model.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”)

Pseudorandom draws also depend on the generator state. Record a reproducible configuration when simulation is needed, and assess Monte Carlo precision for the desired summary. Deterministic CDF and quantile evaluation is generally more direct when the named distribution is available; simulation becomes useful when the quantity is more complicated or the posterior is represented by draws.{{cite:r_base_random2026}} (§Description and §Examples)
