## Lead context
That allowance is a ceiling, fixed before the data are used to make the decision. The size of the test is the largest rejection probability the chosen rule attains on the null. The ceiling and the size are equal only when the test is exactly calibrated.

## Motivating example
A laboratory standard is supposed to have mean 5. A sample of 195 measurements has mean 9.261460 and standard deviation 0.022789. The measurements sit far from 5, but "far" needs a rule stated in advance. With a two-sided level of 0.05, the critical value of the $t_{194}$ law is 1.9723. The standardised distance from 5 is about 2611, vastly larger than 1.9723, so the rule rejects. The same level also builds the interval $9.261460\pm1.9723\times0.022789/\sqrt{195}$, which is $(9.258241,\ 9.264679)$ and does not contain 5. Because 1.9723 is the $0.975$ quantile of the continuous $t_{194}$ law, the null probability of this rejection region equals the chosen level 0.05, and for this rule the size equals the ceiling. The level describes repeated use of the rule when the mean is 5. It assigns no probability to the hypothesis that the mean equals 5.{{cite:nist_mean_limits2002}} (§1.3.5.2, significance level and critical region){{cite:dodge2008}} (pp. 250–251, step 2, the significance level)

## Intuition
A test divides the possible values of a statistic into a rejection region and its complement. The significance level $\alpha$ is fixed after the hypotheses are named and before the critical value is calculated. It is the largest type I error rate the analyst is willing to allow. NIST's normal-mean page uses that order: choose $\alpha$, then the critical point $t_{1-\alpha/2,\,N-1}$, then reject if the statistic falls beyond it.{{cite:nist_mean_limits2002}} (§1.3.5.2, “Definition: Hypothesis Test”){{cite:dodge2008}} (pp. 250–251, steps of a test)

The size is the probability of the region that this choice produces. When the null contains more than one distribution, the size is the supremum of the rejection probability over that null.{{cite:rudloff_karatzas2010}} (p. 1226, (2.1)) A continuous quantile is built so that the supremum equals the chosen $\alpha$. The $t$ rule above is of that kind: choosing $\alpha=0.05$ produces a region that contains 5% of samples drawn from its null. A discrete statistic does not offer every probability between 0 and 1. Its distribution places mass on isolated values, and a non-randomised region must take each value entirely or leave it out. The attainable sizes therefore jump across $\alpha$. For $X\sim\mathrm{Bin}(15,0.6)$, the upper tail $\{13,14,15\}$ has null probability $0.027114$, which is $2.7114\%$. The next larger tail already exceeds $0.05$. A nominal level of $0.05$ is still the ceiling under which the smaller tail was selected. It is the size only for an exactly calibrated test. The level is likewise distinct from the probability that a rejected null was true.

## Definition
When a simple null makes the type I error a single probability, that probability is sometimes itself called the significance level, and a nominal level is then the bound placed on it. The names used here keep the bound and the attained probability apart. Write $R$ for the rejection region and $P_\theta$ for the distribution of the sample at parameter $\theta$, with null set $\Theta_0$. The size of the test is
$$
\sup_{\theta\in\Theta_0}P_\theta(R).
$$
The significance level $\alpha$ is a number chosen in advance. The test has level $\alpha$ when its size is at most $\alpha$, and the test is exactly calibrated when the size equals $\alpha$. Rudloff and Karatzas separate the two roles. The significance level is the largest type I error that is to be allowed, and the size is the supremum of the type I error over the null, which the test is required to keep at or below that level.{{cite:rudloff_karatzas2010}} (p. 1224, significance level as the bound; p. 1226, (2.1)) Siegrist identifies the maximum of the power function on the null both with the significance level of the test and with the size of the critical region, and describes the usual construction in which the region is chosen so that the maximum equals a prescribed small value.{{cite:siegrist2022_testing}} (§9.1, Tests of an Unknown Parameter) That equality is exact calibration.

It holds for a two-sided $t$ test of a normal mean, because the critical point $t_{1-\alpha/2,\,n-1}$ is the quantile that puts probability $\alpha$ on $\{|T|\ge t_{1-\alpha/2,\,n-1}\}$ under the null.{{cite:nist_mean_limits2002}} (§1.3.5.2, critical region at level $\alpha$) It fails for a discrete region whose atoms cannot be summed to $\alpha$. The size is then the probability of the region that will be used, and $\alpha$ remains the ceiling that region was required to respect. A randomised decision on the boundary atom can close the gap. A rejection probability strictly between 0 and 1 on that atom can enforce the significance level with no slack, so that the type I error equals $\alpha$.{{cite:rudloff_karatzas2010}} (p. 1225, randomisation without slackness)

## Interpretation — Level, critical value, and p-value
The critical value is a cutoff computed from $\alpha$. The $p$-value is computed from the data: it is the smallest level at which this observed statistic would fall in the rejection region. Rejecting when the $p$-value is at most $\alpha$ is the same decision as rejecting when the statistic falls in the level-$\alpha$ region, provided the region was the one used to define the $p$-value. Reporting only "significant at 0.05" throws away how far inside the region the statistic landed. Reporting only the $p$-value, and then choosing a level after seeing it, abandons the procedure whose ceiling was fixed before the data were examined. For an exactly calibrated test that precommitted ceiling is also the false-rejection rate. For a discrete test the same ceiling can sit strictly above the size.{{cite:nist_mean_limits2002}} (§1.3.5.2, confidence interval as the set of means not rejected){{cite:siegrist2022_testing}} (§9.1, P-value){{cite:dodge2008}} (p. 251, decision after the region is fixed)

## Properties — Where the level goes in a normal-mean test
For independent $N(\mu,\sigma^2)$ observations with known $\sigma$, the level-$\alpha$ two-sided region for $Z=(\overline X-\mu_0)/(\sigma/\sqrt n)$ is $|Z|\ge z_{1-\alpha/2}$. Because the null distribution of $Z$ is continuous, this quantile construction makes the size equal $\alpha$. The matching region for the sample mean is $|\overline X-\mu_0|\ge z_{1-\alpha/2}\,\sigma/\sqrt n$. With unknown $\sigma$ the normal quantile is replaced by a $t_{n-1}$ quantile and $\sigma$ by $s$. A one-sided level $\alpha$ uses one tail, $t_{1-\alpha,\,n-1}$, which is smaller than the two-sided critical value at the same $\alpha$. NIST's illustration with 194 degrees of freedom has two-sided critical value 1.9723 at $\alpha=0.05$ and one-sided critical value 1.6527.{{cite:nist_mean_limits2002}} (§1.3.5.2, two-sided and one-sided critical values)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Under $H_0:\mu=\mu_0$ with known $\sigma$, $Z\sim N(0,1)$. The quantile $z_{1-\alpha/2}$ satisfies $\Pr(|Z|\ge z_{1-\alpha/2})=\alpha$, so the test that rejects for $|Z|\ge z_{1-\alpha/2}$ has size $\alpha$, and therefore level $\alpha$. Multiplying the inequality by $\sigma/\sqrt n$ gives the region for $\overline X$. Replacing $\sigma$ by $S$ and $z_{1-\alpha/2}$ by $t_{n-1,1-\alpha/2}$ preserves the equality of size and level when the observations are independent and normal, because then $(\overline X-\mu_0)/(S/\sqrt n)\sim t_{n-1}$.

If the statistic is discrete and the null is simple, the size of a region $R$ is $\Pr_{H_0}(T\in R)$. If the null is composite, the size is the supremum of that probability over the null. A region whose size is at most $\alpha$ has level $\alpha$. The size can lie strictly below $\alpha$, because the probability changes only when a whole atom is added to the region, and the next atom may already exceed the ceiling. Rejecting with a probability between 0 and 1 on that atom can raise the type I error exactly to $\alpha$. A non-randomised threshold cannot spend part of an atom.{{cite:rudloff_karatzas2010}} (p. 1225, randomisation without slackness; p. 1226, (2.1)){{cite:nist_mean_limits2002}} (§1.3.5.2, critical region)
:::
:::

## Statistical use — Reading a reported level
A reported level belongs to a named test and a named null. "Significant at 0.05" without the statistic, the direction, and the sample size is not a description of a region. The same data can reject at 0.05 on a one-sided test and not on a two-sided test, because the one-sided critical value is closer to zero. An interval of confidence $1-\alpha$ contains the parameter values that the two-sided level-$\alpha$ test would not reject. That duality fixes the relationship between the two procedures. It does not turn $\alpha$ into a posterior probability.{{cite:nist_mean_limits2002}} (§1.3.5.2, interval and the hypothesis test)

## Worked example
Blood pressure in a reference population has standard deviation 7. For a sample of 101 independent normal readings, the level-0.05 two-sided region for $T=(\overline X-127)/(7/\sqrt{101})$, using $z_{0.975}=1.960$, is $|T|\ge1.960$. The standard error is $7/\sqrt{101}=0.6965$, and $1.960\times0.6965=1.365$. The sample mean rejects $H_0:\mu=127$ when $\overline X\le125.635$ or $\overline X\ge128.365$. Under the normal model the null probability of that region is 0.05, so the size equals the chosen level.{{cite:nist_mean_limits2002}} (§1.3.5.2, level and critical region)

A discrete comparison shows why the ceiling and the size can differ even when every modelling assumption holds. Let $X\sim\mathrm{Bin}(15,0.6)$, and let the test of $p=0.6$ against $p>0.6$ reject for $X\in\{13,14,15\}$. Then
$$
\Pr(X\ge13)=\sum_{k=13}^{15}\binom{15}{k}(0.6)^k(0.4)^{15-k}=0.027114,
$$
so the size is $2.7114\%$. The next larger upper tail has probability $\Pr(X\ge12)=0.090502$, and the difference is the atom $\Pr(X=12)=0.063388$. A non-randomised upper tail must include that atom entirely or not at all, so none of these tails has null probability $0.05$. The largest upper tail whose size does not exceed the nominal level $0.05$ is $\{13,14,15\}$, and the size it attains is $2.7114\%$. The value $0.05$ is the ceiling used to select the region, chosen before the critical value is applied to the data. At $p=0.9$ the power of the same region is $0.8159$.{{cite:rudloff_karatzas2010}} (p. 1226, size bounded by the significance level){{cite:dodge2008}} (p. 251, significance level chosen before the critical value)

**Your turn.** Seven observations are used to test $H_0:\sigma^2=1.1$ against $\sigma^2<1.1$ at level 0.05, rejecting for small $s^2$. The critical point is $\chi^2_{6;0.05}=1.635$. Find the largest $s^2$ that still rejects.

::: {.callout-tip collapse="true" title="Answer"}
Reject when $6s^2/1.1\le1.635$, so $s^2\le1.635\times1.1/6=0.29975$, which rounds to $0.2998$. Any larger sample variance is outside this level-0.05 region. Under $\sigma^2=1.1$ the continuous chi-squared law assigns probability 0.05 to that region, so the size equals the chosen level. The level assigns no probability to the hypothesis that the variance is 1.1.
:::

## Common misconceptions
The significance level is not the probability that the null hypothesis is true after a rejection, and it is not the $p$-value. A nominal level of 0.05 equals the long-run proportion of true-null rejections only when the test is exactly calibrated. The binomial region above has size $2.7114\%$. A $p$-value of 0.04 and a level of 0.05 are different objects: one is computed from the sample, the other was chosen as a cutoff. A result that is not significant at 0.05 is not evidence that the null is true; the test was built to limit false rejections, not to limit missed effects. And 0.05 is a convention NIST and many textbooks record as common, not a law of nature. A different scientific cost can justify 0.01 or 0.10, provided the choice is made with the region, not after the $p$-value is known.{{cite:nist_mean_limits2002}} (§1.3.5.2, choice of $\alpha$){{cite:dodge2008}} (pp. 250–251, level as a step of the procedure)

## Assumptions and limits — When the advertised level is not the error rate
The $t$ critical value has size $\alpha$ when the observations are independent and normal and the null mean is the one in the statistic. Dependence, or a badly skewed population in a small sample, moves the true rejection probability away from $\alpha$. The binomial region above is a different limit, visible with no modelling surprise. The statistic is discrete, the atom at 12 carries probability $0.063388$, and the tail from 12 has probability $0.090502$, so the region $\{13,14,15\}$ cannot be given probability $0.05$. Its size is $2.7114\%$. Quoting $0.05$ as that size would overstate how often a true null is rejected. A second limit is optional stopping. If the tester peeks and adds observations until the $p$-value drops below 0.05, the probability of eventually rejecting a true null is larger than 0.05. The level attaches to a region that was fixed, including the sample size.{{cite:nist_mean_limits2002}} (§1.3.5.2, the level is a property of the method){{cite:dodge2008}} (p. 251, region fixed before the decision)

## Connections
The [critical region](critical-region.qmd) is the set on which the test rejects. The null probability of that set, or the supremum of the null probability when the null is composite, is the size, and the significance level is the ceiling placed on the size.{{cite:rudloff_karatzas2010}} (p. 1226, (2.1)) [Type I and type II errors](type-i-and-type-ii-errors.qmd) name a false rejection and a missed rejection. The [p-value](p-value.qmd) is the smallest level at which the observed sample rejects. A [confidence interval](confidence-interval.qmd) of level $1-\alpha$ inverts the tests of level $\alpha$. The [Neyman–Pearson approach](neyman-pearson-approach.qmd) fixes a ceiling on the type I error and then looks for a region with small type II error.{{cite:dodge2008}} (pp. 250–251, type I and type II errors in the 1933 paper)

## Check yourself

### A critical region for a known variance {#self-check-ex-inf-blood-pressure-region}

For the blood-pressure statistic $T=(\overline X-127)/(7/\sqrt{101})$ and $z_{0.975}=1.960$, state the level-0.05 region for $T$ and for $\overline X$.

[Exercise](../questions/ex-inf-blood-pressure-region.qmd)

::: {.callout-tip collapse="true" title="Answer"}
Reject when $|T|\ge1.960$. Since $7/\sqrt{101}=0.6965$ and $1.960\times0.6965=1.365$, reject when $\overline X\le125.635$ or $\overline X\ge128.365$. The probability of that region is 0.05 when $\mu=127$ and the normal model holds.
:::

### Power of a serve test {#self-check-ex-inf-serve-power}

Serves follow $\mathrm{Bin}(15,p)$. The test of $p=0.6$ against $p>0.6$ rejects for $X\in\{13,14,15\}$. What is the size, and what is the power at $p=0.9$?

[Exercise](../questions/ex-inf-serve-power.qmd)

::: {.callout-tip collapse="true" title="Answer"}
The size is $\Pr(X\ge13)$ at $p=0.6$, which equals $0.027114$, or $2.7114\%$. The power at $p=0.9$ is $\Pr(X\ge13)=0.8159$. The nominal level $0.05$ is the ceiling under which this region was selected.
:::

## History
Talk of the significance or insignificance of a batch of observations goes back to the eighteenth century, including Arbuthnot (1710), Daniel Bernoulli (1734) and Laplace (1773), and such calculations became more common in the nineteenth century. Neyman and Pearson's 1928 *Biometrika* paper set a null against an alternative, and their 1933 paper distinguished a type I error from a type II error. In that procedure the significance level is the allowed probability of the type I error, fixed when the rejection region is chosen.{{cite:dodge2008}} (pp. 250–251, History and mathematical steps)
