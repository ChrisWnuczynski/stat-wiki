## Motivating example
A test can control its false-positive probability and still rarely detect a practically meaningful difference. Its level describes rejection when a null model holds. Its power describes rejection at a specified alternative. A power function keeps the rejection rule fixed and asks how its rejection probability varies across the parameter space.{{cite:siegrist2022_testing}} (§9.01, “Power” and tests of an unknown parameter)

## Definition — A probability indexed by the data-generating parameter
For a non-randomised test with rejection region $C$ and model $P_\theta$, define $\pi(\theta)=P_\theta(X\in C)$. On the null parameter set $\Theta_0$, this is a type-I error probability, and the test's size is $\sup_{\theta\in\Theta_0}\pi(\theta)$. On the alternative set, $1-\pi(\theta)$ is the type-II error probability at that parameter value. There is generally a whole function of false-negative probabilities, rather than one number independent of the alternative.{{cite:siegrist2022_testing}} (§9.01, power-function properties)

A randomised test replaces the indicator of $C$ by a rejection probability $\varphi(X)\in[0,1]$, giving $\pi(\theta)=E_\theta\varphi(X)$. This definition includes deterministic rules as the special case $\varphi=\mathbf1_C$. Randomisation can sometimes attain a specified size exactly in a discrete problem; an ordinary discrete threshold may instead have size strictly below its nominal upper bound.

## Properties — Fix the rule before comparing alternatives
For an upper-tail normal-mean test with known scale, reject if $Z=\sqrt n(\bar X-\mu_0)/\sigma>z_{1-\alpha}$. At a true mean $\mu$, $Z$ has distribution $N(\delta,1)$, where $\delta=\sqrt n(\mu-\mu_0)/\sigma$. Thus
$$\pi(\mu)=1-\Phi(z_{1-\alpha}-\delta).$$
This follows by subtracting the alternative mean from the same random statistic. The critical value stays at its null-calibrated value while the distribution shifts.{{cite:openintro2019}} (§7.4.2, computing power)

The formula shows which scale controls detectability. Multiplying both the departure $\mu-\mu_0$ and $\sigma$ by the same positive constant leaves power unchanged; increasing only the departure increases power. Holding a standardised departure fixed while increasing $n$ moves the alternative mean of $Z$ in proportion to $\sqrt n$. Those comparisons all presuppose that the sample still follows the stated independent normal model.

## Worked example — Continuous and discrete rejection regions
Let $n=25$, $\sigma=2$, an upper-tail level of $0.05$ and an alternative mean one unit above $\mu_0$. The noncentrality is $2.500$ and the normal critical value is $1.644854$. Power is $1-\Phi(1.644854-2.5)=0.803765$. The type-II error probability at that alternative is $0.196235$. A smaller scientifically relevant departure would need its own power calculation.{{cite:openintro2019}} (§7.4, power and sample size)

For a discrete contrast, suppose $X\sim\operatorname{Binomial}(10,p)$ and reject $p=0.5$ in favour of a larger value when $X\ge9$. Then $\pi(p)=10p^9(1-p)+p^{10}$. At the null, $\pi(0.5)=0.010742$; at $p=0.8$, it is $0.375810$. The rule is conservative relative to a nominal 0.05 cap and has less than one-half power even at a sizeable departure. These probabilities are exact binomial tails, not simulation estimates.{{cite:dodge2008}} (p. 44, Binomial Distribution)

**Your turn.** For that binomial rule, calculate power when $p=1$ and when $p=0$.

::: {.callout-tip collapse="true" title="Answer"}
At $p=1$, ten successes occur with probability one and the rule always rejects, so power is $1$. At $p=0$, there are no successes and the rejection probability is $0$.
:::

## Statistical use — Design for a specified effect, then assess precision
A design calculation specifies the effect worth detecting, the sampling variability, the test rule and the acceptable error probabilities. These choices precede data collection. A power curve can show how sensitive the design is to a range of plausible effects rather than concealing uncertainty behind one chosen alternative.{{cite:openintro2019}} (§§7.4.1–7.4.3)

Substituting the observed effect into a post hoc power calculation does not add independent evidence to the observed test result. An interval for the effect is more informative about which practically important departures remain compatible with the data. When simulation estimates power, its own Monte Carlo uncertainty should also be reported: independent rejection indicators with probability $\pi$ have estimated standard error approximately $\sqrt{\hat\pi(1-\hat\pi)/R}$ for $R$ replicates. This is an uncertainty about the numerical estimate of a rejection probability, distinct from sampling uncertainty in the study's effect estimate.{{cite:siegrist2022_testing}} (§9.01, rejection probabilities and error types)
