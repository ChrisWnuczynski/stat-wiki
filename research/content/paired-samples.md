## Motivating example
A laboratory compares two instruments on the same set of specimens. Differences among specimens may be much larger than the systematic difference between instruments. Matching the two readings for each specimen preserves the comparison of interest and prevents specimen-to-specimen variation from obscuring it. The pairing is determined by the design, rather than by sorting two unrelated samples into a convenient order.{{cite:openintro2019}} (§7.2.1, paired observations)

## Definition — The independent units are the pairs
Write the measurements on pair $i$ as $(X_i,Y_i)$ and define a consistently ordered difference $D_i=X_i-Y_i$. A paired analysis treats the vectors for different pairs as independent while allowing dependence between the two measurements within a pair. Its mean target is $\delta=E(D)=E(X)-E(Y)$. Equal marginal means alone do not imply that the paired measurements are independent.{{cite:dodge2008}} (p. 409, Paired Student’s T-Test)

For a paired $t$ test assume that the differences themselves form an independent normal sample with positive variance. With $n$ complete pairs, use $T=(\bar D-\delta_0)/(S_D/\sqrt n)$ and a $t_{n-1}$ reference under $H_0:\delta=\delta_0$. Normal marginal distributions for $X$ and $Y$ are not a replacement for checking the distribution of $D$; a sufficient condition is joint normality within each pair.{{cite:openintro2019}} (§7.2.2, inference for paired data){{cite:dodge2008}} (p. 409, mathematical aspects)

## Properties — Covariance determines the gain from matching
The identity
$$\operatorname{Var}(D)=\sigma_X^2+\sigma_Y^2-2\operatorname{Cov}(X,Y)$$
follows by expanding $E[(X-EX-Y+EY)^2]$. For independent pairs, $\operatorname{Var}(\bar D)=\operatorname{Var}(D)/n$. Positive within-pair covariance reduces the variance relative to the sum of the marginal variances. Negative covariance can increase it. Thus pairing is not an algebraic promise of a smaller standard error; its benefit depends on matching units that share relevant variation.{{cite:nist_two_sample_t2002}} (§1.3.5.3, paired and unpaired data)

A common subject-level model makes this concrete: $X_i=a_i+\tau+e_{i1}$ and $Y_i=a_i+e_{i2}$. Subtracting removes $a_i$, giving $D_i=\tau+e_{i1}-e_{i2}$. Large variation in $a_i$ need not inflate the paired standard error. This cancellation is an explicit model calculation, not a justification for ignoring order, carryover or time effects in a crossover experiment.

## Worked example — Five matched changes
Consider five hypothetical differences $4,1,3,2,5$. Their mean is $3.000$ and their corrected variance is $2.500$, so the estimated standard error is $\sqrt{2.5/5}=0.707107$. Against a zero mean the statistic is $4.242641$ on four degrees of freedom. The two-sided $p$-value is $0.013236$ and the 95% interval is $(1.036757,4.963243)$. The calculation is a one-sample Student procedure applied to differences.{{cite:openintro2019}} (§7.2.2)

If each first measurement were increased by a common $100$ units and each second measurement were increased by the same amount, every difference would be unchanged. The paired statistic and interval would therefore be identical. That invariance isolates the comparison from a common location shift; it does not protect against a differential calibration error affecting just one instrument.

**Your turn.** Reverse the subtraction order. How do the mean, standard error, statistic, two-sided $p$-value and confidence interval change?

::: {.callout-tip collapse="true" title="Answer"}
The mean becomes $-3.000$, the standard error stays $0.707107$, and the statistic becomes $-4.242641$. Symmetry preserves the two-sided probability $0.013236$. The interval is $(-4.963243,-1.036757)$, obtained by reversing and negating the endpoints.
:::

## Assumptions and limits — Keep the pair identities through analysis
A complete-pair analysis discards a pair when one measurement is absent. Its target can change if missingness is associated with the unobserved difference. Taking the two available marginal means separately is a different estimator and generally destroys the exact cancellation. Retaining the pair identifier is therefore essential for understanding both the estimator and the missing-data pattern.{{cite:openintro2019}} (§7.2, paired data)

The paired design does not remove all bias. In a before-and-after comparison, time trends can affect both the intervention and the outcome. In a two-instrument comparison, systematic measurement differences can depend on specimen size, so one common average difference may conceal proportional bias. Plotting differences against a relevant level or covariate can reveal such structure; a small $p$-value for the mean difference does not establish agreement at every measurement level.{{cite:nist_two_sample_t2002}} (§1.3.5.3, one-to-one correspondence and paired differences)

## Interpretation — Count the differences, and keep their order

Two measurements on each pair produce one difference. With $n$ independent pairs the Student statistic treats those $n$ differences as the sample and estimates one mean, so the reference law has $n-1$ degrees of freedom. Counting all $2n$ raw measurements as an unpaired sample uses the wrong independent pieces and, when the paired measurements move together, the wrong variance. Positive within-pair covariance shrinks $\operatorname{Var}(X-Y)$ below the sum of the marginal variances. Negative covariance enlarges it. Pairing is therefore a property of the design, not a free reduction available whenever two samples happen to have the same length.

Reversing which measurement is subtracted reverses the mean difference, the statistic and both endpoints of a confidence interval. A two-sided tail probability is unchanged, because the central Student law is symmetric and the absolute statistic is the same. A one-sided test changes its conclusion under that reversal, because the tail that was upper becomes lower. The sign convention has to be fixed when the alternative is one-sided, and it has to be reported with the estimate either way. A common additive shift of both instruments cancels in every difference. A calibration error that affects only one instrument remains inside the difference and is not removed by matching.{{cite:openintro2019}} (§7.2.2, inference for paired data){{cite:nist_two_sample_t2002}} (§1.3.5.3, one-to-one correspondence and paired differences){{cite:dodge2008}} (p. 409, mathematical aspects)

## Connections

[One-sample t-test](one-sample-t-test.qmd) applied to the differences is the paired test. [One-sample t-pivot](one-sample-t-pivot.qmd) supplies the ratio, and [Student t distribution](student-t-distribution.qmd) is its null law. A before-and-after comparison on the same subjects is paired by the subject. Time trends that move with the intervention stay inside the difference. Two separate groups, even of equal size, do not become pairs by being written in two columns of the same length.{{cite:openintro2019}} (§7.2.1, paired observations)
