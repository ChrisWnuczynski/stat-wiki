## Motivating example
A manufacturer tests whether a process mean equals a target, then wants to know which nearby targets are still compatible with the measurements. Repeating the same test for every possible mean produces an interval automatically. The interval communicates direction and precision as well as the binary decision for one chosen null. This connection depends on using the same sampling assumptions, significance level and tail convention in both calculations.{{cite:nist_handbook2002}} (§1.3.5.2, confidence limits and the one-sample test)

## Definition — Invert the acceptance sets
For each parameter value $\theta_0$, let $A(\theta_0)$ be the set of samples for which a level-$\alpha$ test does not reject it. Define
$$C(x)=\{\theta_0:x\in A(\theta_0)\}.$$
For a fixed true $\theta$, the event $\theta\in C(X)$ is exactly the event $X\in A(\theta)$. Thus
$$\Pr_\theta\{\theta\in C(X)\}=1-\Pr_\theta\{\text{reject }\theta\}\ge1-\alpha.$$
This is the whole coverage argument. It works for confidence sets that are intervals, disconnected sets or multivariate regions. If the tests have exact size $\alpha$, coverage is exactly $1-\alpha$; conservative tests give at least that coverage.{{cite:openintro2019}} (§5.2, confidence level; §5.3, significance level)

The construction also explains what a confidence set contains: parameter values whose own tests accept the observed sample. It does not assign probabilities to those parameter values. In repeated sampling the procedure varies and the true parameter stays fixed.{{cite:nist_handbook2002}} (§1.3.5.2, confidence coefficient)

## Properties — A direct calculation with a pivot
For independent normal data with unknown nonzero variance, put $\mathrm{SE}=s/\sqrt n$. The two-sided Student test rejects when $|\bar x-\mu_0|/\mathrm{SE}>c$, where $c$ is the $1-\alpha/2$ quantile of $t_{n-1}$. Its nonrejection condition is
$$-c\mathrm{SE}\le\bar x-\mu_0\le c\mathrm{SE},$$
which rearranges to $\bar x-c\mathrm{SE}\le\mu_0\le\bar x+c\mathrm{SE}$. Including the endpoints corresponds to rejecting only beyond the cutoff. Equality events have probability zero under the continuous normal model, but a consistent endpoint convention still makes the numerical statements exact.{{cite:nist_handbook2002}} (§1.3.5.2, test statistic and critical region)

For an upper alternative $\mu>\mu_0$, the nonrejection condition rearranges to $\mu_0\ge\bar x-t_{n-1;1-\alpha}\mathrm{SE}$. Its inverse is a lower confidence bound extending to positive infinity. A two-sided $95\%$ interval generally does not invert a one-sided $5\%$ test, because their critical values allocate tail probability differently.{{cite:openintro2019}} (§7.1, “One-sample means with the t-distribution”)

## Worked example — One dataset, several null values
Suppose $n=16$, $\bar x=12$ and $s=4$. Then $\mathrm{SE}=1$ and the $95\%$ Student interval, using $t_{15;0.975}\approx2.13145$, is approximately $[9.86855,14.13145]$. The null $\mu_0=10$ yields $t=2$ and two-sided $p\approx0.06395$, so it is not rejected. The null $\mu_0=9$ yields $t=3$ and $p\approx0.00897$, so it is rejected. The interval and the corresponding tests agree by construction.

For a one-sided upper test against $\mu>10$, the same $t=2$ has $p\approx0.03197$. The $95\%$ lower confidence bound is $12-t_{15;0.95}\approx10.24695$, which lies above $10$. Rejecting that one-sided null while the two-sided interval contains $10$ is consistent: these are different tail allocations.{{cite:nist_handbook2002}} (§1.3.5.2, one- and two-sided alternatives)

**Your turn.** A two-sided $95\%$ interval obtained by inverting a test is $[2.1,4.7]$. State the decisions for null values $2$, $3$ and $5$. Does this interval alone give a posterior probability that the parameter exceeds $3$?

::: {.callout-tip collapse="true" title="Answer"}
The matching two-sided tests reject $2$ and $5$ and do not reject $3$. The confidence interval gives no posterior probability for the event that the parameter exceeds $3$. Such a probability needs a probability model for the unknown parameter, as in Bayesian inference.
:::

## Assumptions and limits — Matching procedures matters
A Wald interval and a score test for a proportion need not agree because they use different standard errors. Inverting the score inequality gives a score interval, while inverting equal-tail exact binomial tests gives a corresponding exact interval. The word “matching” carries mathematical content: choosing two familiar procedures with nominal levels $0.05$ and $0.95$ is insufficient.

Failure to reject a null value does not establish that the value is true. A wide interval can contain both negligible and practically important effects. Conversely, a narrow interval can exclude zero while containing only small effects. State the effect scale and a scientifically meaningful tolerance so that precision and practical importance can be assessed separately.{{cite:openintro2019}} (§5.3, practical versus statistical significance)

An interval that just includes the null value and an interval that lies far from it can share one decision at a fixed level while describing very different sets of compatible parameters.

## Connections
Inverting a test builds the confidence set from the acceptance region. For a two-sided level-$\alpha$ test of each candidate value $\mu_0$, the set of $\mu_0$ that are accepted is the $1-\alpha$ interval. In the normal example with $n=16$, $\bar x=12$ and $s=4$, the standard error is $1$ and $t_{15;0.975}\approx 2.13145$, so the interval is about $[9.86855,14.13145]$. The null $\mu_0=10$ gives $t=2$ and a two-sided $p$ about $0.06395$, and $10$ lies inside the interval. The null $\mu_0=9$ gives $t=3$ and a two-sided $p$ about $0.00897$, and $9$ lies outside it. The interval and the family of two-sided tests are reporting one construction.{{cite:nist_handbook2002}} (§1.3.5.2, one- and two-sided alternatives)

A one-sided test is a different family. Against $\mu>10$ the same $t=2$ has a one-sided $p$ about $0.03197$, and the $95\%$ lower confidence bound is about $10.24695$, which lies above $10$. The two-sided interval still contains $10$. The two procedures allocate the error rate differently, so agreement between them is not part of the duality. A Wald interval and a score test for a proportion can disagree for the same reason: they estimate the standard error at different places. The score interval is the inversion of the score test. An equal-tail exact binomial interval is the inversion of the corresponding exact binomial tests. Naming two procedures that both use $0.05$ and $0.95$ does not make them inverses of each other.{{cite:nist_handbook2002}} (§1.3.5.2, one- and two-sided alternatives){{cite:openintro2019}} (§5.3, practical versus statistical significance)

## Common misconceptions
An interval that contains a null value and an interval that lies far from it can share the decision "do not reject" or the decision "reject" at one fixed level. The interval records the whole set of values the test accepts. A wide interval can contain both a negligible effect and a large one. A narrow interval can exclude zero while containing only effects too small to matter on the scale of the measurement. The $t$ example separates those readings: $10$ is kept by the two-sided $95\%$ interval, and $9$ is excluded, and the distance from $12$ to each of those values is visible in the endpoints $[9.86855,14.13145]$.{{cite:openintro2019}} (§5.3, practical versus statistical significance)

The same interval does not supply a posterior probability that the parameter exceeds $3$, or any other point. A posterior probability needs a probability model for the unknown parameter. The worked inversion says which null values the two-sided test rejects. For an interval $[2.1,4.7]$ obtained that way, the matching tests reject $2$ and $5$ and accept $3$. That is a statement about the test. It leaves the posterior probability of $\{\mu>3\}$ for a Bayesian calculation with a stated prior.{{cite:nist_handbook2002}} (§1.3.5.2, one- and two-sided alternatives)

## History
The duality is a bookkeeping identity once the test and the interval are built from the same acceptance rule. Fix a level and a family of null values. Collect every null value whose acceptance region contains the observed sample. The resulting set has the coverage probability of the test, because the sample falls in the acceptance region of the true value with that probability, and the set then contains the true value. Changing the tail split, the variance estimator, or the null family produces a different set. The normal calculation above is the Student case of this bookkeeping: one sample, one standard error, and a $t$ threshold, read either as a $p$-value at a named null or as the set of nulls that clear the threshold.{{cite:nist_handbook2002}} (§1.3.5.2, one- and two-sided alternatives){{cite:openintro2019}} (§5.3, practical versus statistical significance)
