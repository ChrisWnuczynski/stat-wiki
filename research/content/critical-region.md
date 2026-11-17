## Motivating example
A laboratory will investigate a mean only if its sample is sufficiently far from a reference value. The word *sufficiently* needs a rule chosen before the data are examined: which observed test-statistic values count against the null, and how frequently would that rule trigger under the null? The critical region is this rejection rule written as a set. It links a scientific alternative to a controlled false-rejection probability.{{cite:nist_process_mean2002}} (§7.2.2, “Comparison with critical values”)

## Intuition
Imagine the null distribution drawn over a horizontal axis of possible statistic values. A right-sided alternative places the critical region in the upper tail; a left-sided alternative places it in the lower tail. A two-sided question often puts pieces in both tails. The cutoffs must come from the null distribution and the selected significance level, not from the observed statistic. Once those choices are fixed, the observation either belongs to the region or it does not. This is a decision rule, not a statement that the null itself has been proved true or false.{{cite:nist_process_mean2002}} (§7.2.2, one- and two-sided critical-value rules)

## Definition
For sample data $X$ and a specified test statistic $T(X)$, write $C$ for the set of statistic values that lead to rejection. Equivalently the rejection event in the sample space is $\{x:T(x)\in C\}$. Under a simple null $P_0$, its size is $P_0\{T(X)\in C\}$. Under a composite null the size is the supremum of this probability over all parameter values allowed by $H_0$. A level-$\alpha$ rule has size at most $\alpha$; equality need not be attainable, especially for a discrete statistic.{{cite:dodge2008}} (pp. 452–454, “Rejection Region”){{cite:nist_process_mean2002}} (§7.2.2, “Critical values”)

For a continuous null distribution with CDF $F_0$, an upper-tail region can be $C=[F_0^{-1}(1-\alpha),\infty)$ when the quantile is unique. A symmetric two-tail rule commonly uses the $\alpha/2$ and $1-\alpha/2$ quantiles. These are common constructions, not the definition of a critical region: a discrete test may use selected count values, and a likelihood-ratio test can have a different shape.{{cite:nist_process_mean2002}} (§7.2.2, one- and two-sided critical-value rules){{cite:dodge2008}} (pp. 453–454, one- and two-sided regions)

## Interpretation
The caffeine figure shows an upper-tail Student region. The cutoff $2.43$ is chosen from the $t_{39}$ null law at level $0.01$; the observed $2.575$ falls beyond it. The $p$-value $0.007$ is the null tail area beyond the *observed* statistic and thus differs from the prechosen region's $0.01$ area. The same picture also shows why a one-sided $0.01$ test can reject while a two-sided $0.01$ test does not: the latter uses a smaller area in each tail and hence more distant cutoffs.{{cite:nist_process_mean2002}} (§7.2.2, tail allocation and critical values)

## Properties
The region determines both error rates. At a null parameter $\theta_0$, $P_{\theta_0}(T\in C)$ is the type I error probability. At an alternative $\theta_1$, the same probability is power; its complement is the type II error probability there. Shrinking a region lowers or preserves both the false-rejection probability and power. This tradeoff explains why the significance level is specified before comparing candidate regions.{{cite:dodge2008}} (p. 452, “Rejection Region”){{cite:nist_process_mean2002}} (§7.2.2.2, roles of $\alpha$ and $\beta$)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
If $C_1\subseteq C_2$, then the indicator $\mathbf1\{T\in C_1\}\leq\mathbf1\{T\in C_2\}$ for every possible sample. Taking expectations under any $P_\theta$ gives $P_\theta(T\in C_1)\leq P_\theta(T\in C_2)$. At a null parameter these probabilities are false-rejection rates; at an alternative they are powers. For a continuous null law, the probability integral over an upper tail beginning at its $(1-\alpha)$ quantile is $\alpha$. In a discrete law the tail jumps by positive masses, so a deterministic cutoff can skip over the target $\alpha$ and attain only a smaller value.{{cite:nist_process_mean2002}} (§7.2.2, critical-value rules; §7.2.2.2, errors)
:::
:::

## Statistical use — Choosing a rejection set
Specify the null and alternative, choose a statistic with a known or justified null reference law, and decide the allowed size. Place the region where the alternative predicts more extreme values, then calculate its null probability. For a normal mean with known standard deviation, $Z=(\overline X-\mu_0)/(\sigma/\sqrt n)$ is standard normal under the point null; a level-$0.05$ upper-tail test uses $Z\geq1.645$, while an equal-tail two-sided test uses $|Z|\geq1.960$. If the standard deviation is estimated from a small normal sample, use the appropriate Student law instead.{{cite:nist_process_mean2002}} (§7.2.2, known- and unknown-standard-deviation cases)

If the ten trials in the worked example share a latent success probability, their count need not be binomial even if each marginal success chance is $0.5$; the binomial tail no longer controls size. If a normal-mean test substitutes a normal cutoff for a small-sample Student statistic, its true rejection probability can exceed its advertised level. If many candidate cutoffs or directions are inspected and only the most favorable is reported, the original region no longer describes the procedure actually used. Each failure concerns the reference model or how the rule was chosen.{{cite:nist_process_mean2002}} (§7.2.2, reference-law assumptions and one- versus two-sided rules)

## Worked example
Suppose $X$ counts successes in ten independent trials and $H_0:p=0.5$ is tested against $H_1:p>0.5$. If the rule rejects for $X\geq8$, its exact null size is $P_{0.5}(X\geq8)=(45+10+1)/1024=0.0546875$, above $0.05$. Moving the cutoff to $X\geq9$ gives $(10+1)/1024=0.0107421875$, a valid but conservative level-$0.05$ rule. The gap occurs because one cannot include only a fraction of the $X=8$ outcomes with a deterministic threshold on $X$. If eight successes are observed, the first rule rejects and the second does not; the choice must precede that observation.{{cite:dodge2008}} (pp. 452–454, cutoff and significance-level interpretation)

**Your turn.** For twelve independent fair trials, use a right-tail count rule at level $0.05$. Does $X\geq10$ qualify? If ten successes occur, what is the decision?

::: {.callout-tip collapse="true" title="Answer"}
$P_{0.5}(X\geq10)=(66+12+1)/4096=79/4096\approx0.01929$, so the rule qualifies and rejects when ten successes occur. The level $0.05$ is a bound on null rejection probability, not the probability that this observed rejection is mistaken.
:::

## Common misconceptions
The region is not selected after seeing a surprising statistic; doing that would make its stated null error rate unreliable. Its probability under the null is not the probability that a rejected null is true. A two-sided region need not put equal tail probability on every skewed null distribution; equal tails are a choice that depends on the testing problem. Finally, failing to enter the region means only that this rule did not reject: it is not evidence that the null parameter is exactly correct.{{cite:nist_process_mean2002}} (§7.2.2, sidedness and decision rules)

## Assumptions and limits — The region is fixed before the data
The cutoffs are chosen so that the null probability is at most the chosen level. On a discrete null the probability can jump, so the nearest region need not have size exactly equal to that level. The calculation uses the null distribution of the statistic; a different null changes the region.{{cite:nist_process_mean2002}} (§7.2.2, sidedness and decision rules)

## Connections
The [significance level](significance-level.qmd) bounds the region's null probability, while the [power function](power-function.qmd) evaluates its probability at alternatives. A [p-value](p-value.qmd) is the smallest level at which the corresponding family of regions would reject for the observed statistic. The [blood-pressure question](../questions/ex-inf-blood-pressure-region.qmd) translates a statistic region to sample-mean cutoffs; the [serve-power question](../questions/ex-inf-serve-power.qmd) computes the size and power of a discrete region; the [two-sided-power question](../questions/ex-inf-ump-two-sided.qmd) shows how tail placement changes power.{{cite:nist_process_mean2002}} (§7.2.2, critical-value rules; §7.2.2.1, confidence-interval connection)

## History
Neyman and Pearson's approach made a test a preassigned rule whose false-rejection probability and power can be compared across hypotheses. The rejection region is the complement of the acceptance region and is tied to the significance level. Modern usage often says *fail to reject* instead of *accept*: absence from the region gives no proof of the null.{{cite:dodge2008}} (pp. 1, 452–454, “Acceptance Region” and “Rejection Region”)
