## Motivating example
A filling machine has a target mean of $1.10$ litres. Ten measured cartons average less than that target, but their volumes vary from carton to carton. Statistical inference asks whether the discrepancy is large relative to the sampling uncertainty of the estimated mean. It also separates a target for the process mean from a minimum acceptable volume for individual cartons. Those two performance requirements are different.{{cite:nist_process_mean2002}} (§7.2.2, comparison with an assumed process mean)

The following values are an illustrative dataset, rather than evidence about a particular producer or a legal rule. The statistical calculations depend on a sampling model and a stated target. A scientific or regulatory interpretation would additionally need the actual specification and the way cartons were selected.{{cite:openintro2019}} (§7.1, “One-sample means with the t-distribution”)

## Definition — Distinguish the mean, scatter and uncertainty
Let $X_1,\ldots,X_{10}$ be independent normal fill volumes with mean $\mu$ and unknown variance $\sigma^2$. The sample mean estimates the process mean, the sample standard deviation estimates individual-volume scatter, and $s/\sqrt{10}$ estimates the standard deviation of the sample mean. Normality provides an exact t sampling distribution for $(\overline X-\mu)/(S/\sqrt{10})$. The separate roles of $s$ and $s/\sqrt{10}$ must be maintained.{{cite:dodge2008}} (pp. 528–529)

Testing $\mu=1.10$ against a two-sided alternative asks whether the process mean is off target in either direction. Testing for a downward shift uses a one-sided alternative specified before inspecting the observations. Changing the alternative after seeing a negative statistic changes the inferential procedure.{{cite:nist_process_mean2002}} (§7.2.2, null hypotheses and critical values)

## Worked example — Recompute the ten volumes
The ten measurements are $1.035,1.019,1.068,1.084,1.077,0.998,1.041,1.037,1.051,1.102$. Their sum is $10.512$ litres, giving $\overline x=1.0512$. The sample standard deviation is $0.0316923$ litres and the estimated standard error of the mean is $0.0100220$ litres. Thus
$$t=\frac{1.0512-1.10}{0.01002198}=-4.869299,$$
with nine degrees of freedom. The two-sided p-value is $0.0008844$. Under the stated model, that is the probability at the hypothesized mean of observing a t statistic at least this far from zero in either direction. It is not the probability that the target-mean hypothesis is true.{{cite:nist_process_mean2002}} (§7.2.2, t statistic and two-sided comparison)

A central 95% confidence interval is $\overline x\pm t_{0.975,9}s/\sqrt{10}$, giving $(1.028529,1.073871)$ litres. It excludes $1.10$. The interval's nominal coverage concerns repetition of the sampling procedure under its assumptions, not a statement that 95% of individual cartons fall inside these endpoints.{{cite:openintro2019}} (§7.1, “One sample t-confidence intervals”)

For descriptive summaries, the median is $1.0460$, the minimum is $0.998$, the maximum is $1.102$ and the range is $0.104$. Using the medians of the lower and upper five sorted observations gives quartiles $1.035$ and $1.077$. Quantile algorithms can use other interpolation conventions; the convention should accompany a small-sample five-number summary.

**Your turn.** Test a target mean of $1.05$ litres using the same standard error. Find the t statistic and say whether the two-sided 5% test rejects.

::: {.callout-tip collapse="true" title="Answer"}
The statistic is $(1.0512-1.05)/0.01002198=0.119737$. Its absolute value is below the two-sided 5% critical value $2.262157$, so the test does not reject.
:::

## Interpretation — Mean performance and individual compliance
The confidence interval estimates the process mean. Predicting the volume of one additional carton involves both uncertainty about the mean and fresh carton-to-carton variation. Under the same normal model, a prediction interval uses $s\sqrt{1+1/10}$ in place of $s/\sqrt{10}$ and is wider. An interval for a mean cannot be relabeled as an individual-volume guarantee.{{cite:openintro2019}} (§7.1, interpretation of a mean confidence interval)

Likewise, the single observed volume below one litre establishes that one of these ten measurements falls below that illustrative threshold. It does not estimate a tiny long-run underfill probability precisely. Tail-rate inference may depend strongly on the sampling distribution's shape, measurement accuracy and process stability.

## Assumptions and limits — Check what was sampled
The exact t calculation assumes independent normal observations from one stable process. Serial drift, batches with different settings or selection of only convenient cartons can invalidate its interpretation. With ten observations, a histogram or normal quantile plot offers limited information about tail shape. Process knowledge and the sampling plan therefore matter alongside a formal calculation.{{cite:openintro2019}} (§7.1, conditions for one-sample mean inference)

The target $1.10$ was specified before calculating the statistic. If many targets, subgroups or monitoring times are searched and only the most extreme discrepancy is reported, the single-test p-value no longer describes the full selection procedure. The numerical calculation remains reproducible, while the question it answers must be stated with the selection rule.
