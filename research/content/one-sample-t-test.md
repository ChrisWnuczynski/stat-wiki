## Motivating example
A production target specifies a mean of 12 units. A sample mean of 12.6 could be strong evidence of a change or routine sampling variation, depending on the sample size and the variation among units. The one-sample $t$ test compares that difference with an estimated standard error and calibrates it under the null model.{{cite:nist_process_mean2002}} (§7.2.2)

## Definition — Choose the alternative before the tail
For independent $N(\mu,\sigma^2)$ observations with $n\ge2$ and positive variance, test $H_0:\mu=\mu_0$ using $T=(\bar X-\mu_0)/(S/\sqrt n)$, with the corrected sample variance in $S^2$. Under $H_0$, $T\sim t_{n-1}$. A two-sided test rejects when $|T|>t_{n-1;1-\alpha/2}$, while an upper-tailed test rejects when $T>t_{n-1;1-\alpha}$. A lower-tailed test uses the corresponding lower quantile.{{cite:nist_process_mean2002}} (§7.2.2, comparison with critical values)

The upper-tailed procedure also controls size for a composite null $\mu\le\mu_0$: at a fixed positive scale, shifting the population mean down shifts the numerator down, so the largest rejection probability on that null occurs at its boundary. The equality null is the boundary distribution used to calculate the reference tail. This distinction makes the reported null and the chosen rejection region agree.

## Properties — A test, an interval and a power curve
For observed statistic $t$, the two-sided $p$-value is $2P(t_{n-1}\ge|t|)$ and the upper-tailed $p$-value is $P(t_{n-1}\ge t)$. These probabilities describe observations at least as extreme as the observed statistic under the chosen null model. They are not probabilities that the mean equals the null value.{{cite:openintro2019}} (§7.1.5, one-sample t tests)

The two-sided level-$\alpha$ test and the $1-\alpha$ Student interval make identical decisions about a specified mean. Algebraically, $|\bar x-\mu_0|>cS/\sqrt n$ if and only if $\mu_0$ lies outside $\bar x\pm cS/\sqrt n$. A confidence interval adds the scale and range of values compatible with that procedure; the binary decision alone cannot distinguish a small precisely estimated departure from a large imprecise one.{{cite:nist_mean_limits2002}} (§1.3.5.2)

At a fixed alternative mean, the statistic has a noncentral $t$ law with parameter $\delta=\sqrt n(\mu-\mu_0)/\sigma$. Power is the probability that this alternative variable falls in the same rejection region. Increasing the sample size changes both the noncentrality and the degrees of freedom; substituting a central null tail for the alternative probability computes a type-I error rate rather than power.

## Worked example — An upper-tailed production check
For $n=16$, $\bar x=12.6$, $S=1.2$ and $\mu_0=12$, the estimated standard error is $0.300$ and $t=2.000$. The upper-tailed $p$-value on 15 degrees of freedom is $0.031973$, below a preselected level of $0.05$. The upper-tail critical value is $1.753050$; the decision is therefore the same by either calculation. The two-sided $p$-value is $0.063945$, reflecting a different question and rejection region.{{cite:nist_process_mean2002}} (§7.2.2, one-sided and two-sided alternatives)

The point estimate of the excess is $0.600$ unit. A one-sided 95% lower bound is $12.074085$. This bound provides an effect-scale statement: at this confidence level the procedure excludes means at or below that bound. It does not establish that any economically meaningful excess has been exceeded. That would require specifying such a margin and testing against it.

**Your turn.** Change only the null mean to $12.3$, retaining the upper-tailed alternative. Calculate the statistic and its $p$-value.

::: {.callout-tip collapse="true" title="Answer"}
The statistic is $(12.6-12.3)/0.3=1.000$. Its upper-tail probability on 15 degrees of freedom is $0.166585$, so the level-0.05 procedure does not reject.
:::

## Assumptions and limits — Exact calibration is conditional on independence
The sample standard deviation is not a substitute for checking how observations were generated. Serial dependence, repeated observations on a subject, informative missingness or a selected stopping time can change the distribution of the statistic. Paired observations can often be handled by applying a one-sample test to independent pair differences, whereas a clustered design needs a standard error appropriate to the cluster structure.{{cite:openintro2019}} (§§7.1.2, 7.2.2)

The normal model supplies the exact Student distribution even at small sample sizes. Approximate use with a non-normal distribution depends on sample size, skewness and outliers, and should be assessed separately. Failure to reject is compatible both with a small departure and with low power. A practical equivalence conclusion needs an equivalence margin and a procedure designed to test it.{{cite:dodge2008}} (pp. 526, 528, Student Distribution and Student Test)
