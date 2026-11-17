## Motivating example
A test can control its false-positive probability and still rarely detect a practically meaningful difference. Its level describes rejection when a null model holds. Its power describes rejection at a specified alternative. A power function keeps the rejection rule fixed and asks how its rejection probability varies across the parameter space.

## Definition — A probability indexed by the data-generating parameter
For a non-randomised test with rejection region $C$ and model $P_\theta$, define $\pi(\theta)=P_\theta(X\in C)$. On the null parameter set $\Theta_0$, this is a type-I error probability, and the test's size is $\sup_{\theta\in\Theta_0}\pi(\theta)$. On the alternative set, $1-\pi(\theta)$ is the type-II error probability at that parameter value. There is generally a whole function of false-negative probabilities, rather than one number independent of the alternative.

A randomised test replaces the indicator of $C$ by a rejection probability $\varphi(X)\in[0,1]$, giving $\pi(\theta)=E_\theta\varphi(X)$. This definition includes deterministic rules as the special case $\varphi=\mathbf1_C$. Randomisation can sometimes attain a specified size exactly in a discrete problem; an ordinary discrete threshold may instead have size strictly below its nominal upper bound.

## Properties — Fix the rule before comparing alternatives
For an upper-tail normal-mean test with known scale, reject if $Z=\sqrt n(\bar X-\mu_0)/\sigma>z_{1-\alpha}$. At a true mean $\mu$, $Z$ has distribution $N(\delta,1)$, where $\delta=\sqrt n(\mu-\mu_0)/\sigma$. Thus
$$\pi(\mu)=1-\Phi(z_{1-\alpha}-\delta).$$
This follows by subtracting the alternative mean from the same random statistic. The critical value stays at its null-calibrated value while the distribution shifts.{{cite:openintro2019}} (Ch. 7, §7.4.2, pp. 279–280)

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

A post hoc calculation that inserts the observed effect into the power formula retraces the observed test statistic. An interval for the effect lists the departures that remain compatible with the data. When simulation estimates power, independent rejection indicators with probability $\pi$ have Monte Carlo standard error about $\sqrt{\hat\pi(1-\hat\pi)/R}$ for $R$ replicates. That standard error describes the numerical estimate of a rejection probability. The study's sampling uncertainty about the effect is a different quantity, attached to the estimator computed from the observations.

## Intuition — Shift a fixed critical value
The upper-tail normal test rejects when the null-standardised mean exceeds $z_{1-\alpha}$. Under an alternative the same statistic is normal with mean $\delta=\sqrt n(\mu-\mu_0)/\sigma$ and variance one, so the rejection probability is the probability that this shifted normal exceeds the original critical value. Increasing $n$ increases $\delta$ in proportion to $\sqrt n$ when the raw departure and $\sigma$ stay fixed. In the worked design, $n=25$, $\sigma=2$ and a one-unit departure give $\delta=2.5$ and power $0.803765$. At $n=100$ the same departure and scale give $\delta=\sqrt{100}\times1/2=5$. With the same critical value $1.644854$, the power is $1-\Phi(1.644854-5)=0.999603$, and the type-II probability is $0.000397$. The test rule is unchanged. The alternative distribution has moved farther past the cutoff.{{cite:openintro2019}} (Ch. 7, §7.4.2, pp. 279–280)

The binomial example shows a discrete version of the same idea. The rejection region $\{9,10\}$ is fixed. At $p=0.5$ its probability is $0.010742$; at $p=0.8$ it is $0.375810$; at $p=0.9$ it is $0.736099$; at $p=1$ it is $1$. The power function is the map $p\mapsto P_p(X\ge9)$, and each of these numbers is one point on that map.

## Common misconceptions
The null rejection probability $0.010742$ is a property of the rule and the null model. It is available before any particular sample is observed. A $p$-value is computed from an observed statistic. The two numbers can be close numerically and still answer different questions: one is $\pi(0.5)$ for this threshold, and the other is a tail probability for a statistic that has already been seen.

Power at a single alternative is one point on $\pi$. The worked normal test has type-II probability $0.196235$ at a one-unit shift with $n=25$. At a half-unit shift, $\delta=1.25$ and the power is $1-\Phi(1.644854-1.25)=0.346475$. A design sentence names the departure it was computed for. A curve of $\pi(\mu)$, or a short table of departures, shows how fast the rejection probability changes.{{cite:openintro2019}} (§§7.4.1–7.4.3)

## Connections
For a test with rejection region $C$, $\pi(\theta)=P_\theta(X\in C)$ is the definition, and $1-\pi(\theta)$ is the type-II probability at alternatives. Size is the supremum of $\pi$ on the null set. A level-$\alpha$ test satisfies that supremum being at most $\alpha$; the binomial threshold has size $0.010742$, which is below a nominal $0.05$ cap, because a discrete tail cannot hit every probability. Randomisation can fill the gap between attainable sizes when a problem demands an exact level. The normal formula has a continuous distribution and attains the level $0.05$ exactly at $\delta=0$.{{cite:dodge2008}} (p. 44, Binomial Distribution)
