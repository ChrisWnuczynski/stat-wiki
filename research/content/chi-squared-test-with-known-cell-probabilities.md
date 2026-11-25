## Motivating example
A genetic ratio specifies probabilities before the chickens are counted. The statistical question is whether deviations of the three counts from their predicted values exceed ordinary multinomial sampling variation. The observations are counts of individual chickens, with each individual assigned to exactly one category. The model differs from comparing measured sample variances.{{cite:openintro2019}} (§6.3, “Testing for goodness of fit using chi-square”)

## Intuition
The expected counts are fixed under the null, but observed counts must sum to the sample size. If one category gains observations, at least one other loses them. This constraint explains why $k$ categories contribute only $k-1$ asymptotically independent directions of departure. A cell with expectation zero is outside the displayed Pearson formula: observing any count there already contradicts that null model.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, “Definition”)

## Properties — A projection argument
Let $p=(p_1,\ldots,p_k)^\top$ have positive entries summing to one, let $D=\operatorname{diag}(p)$ and write
$$Z_n=D^{-1/2}(O-np)/\sqrt n.$$
The multinomial central limit theorem gives limiting covariance
$$D^{-1/2}(D-pp^\top)D^{-1/2}=I-uu^\top,\qquad u_i=\sqrt{p_i}.$$
Since $u^\top u=1$, this matrix projects onto the $k-1$ dimensional subspace perpendicular to $u$. In an orthonormal basis of that subspace the limiting coordinates are independent standard normals. Consequently $T=Z_n^\top Z_n$ converges to $\chi^2_{k-1}$. This argument states what “large sample” means: $k$ and all positive $p_i$ remain fixed while $n$ increases. The right tail supplies the goodness-of-fit $p$-value.{{cite:openintro2019}} (§6.3.2–6.3.4, chi-square statistic, distribution and p-value)

## Worked example — Three equally likely outcomes
A device produces counts $(18,12,30)$ in sixty independent trials, against probabilities $(1/3,1/3,1/3)$. Each expectation is twenty, so
$$T=(18-20)^2/20+(12-20)^2/20+(30-20)^2/20=8.4.$$
With two degrees of freedom the approximate upper-tail probability is $0.0150$. At level 5% the counts challenge equal probabilities. They do not identify the physical mechanism responsible for the imbalance. The reference calculation tests all departures from the specified probability vector.{{cite:openintro2019}} (§6.3.4–6.3.5, p-values and evaluating fit)

**Your turn.** For sixty trials and equal probabilities, replace the counts by $(20,15,25)$. Compute $T$ and its approximate $p$-value.

::: {.callout-tip collapse="true" title="Answer"}
The statistic is $0+25/20+25/20=2.5$ on two degrees of freedom. Its upper-tail probability is $e^{-2.5/2}=0.2865$, so it does not reject at level 5%.
:::

## Assumptions and limits
The individual trials must be independent and the categories exhaustive and mutually exclusive. Small expected counts make a continuous chi-squared tail a poor approximation to a discrete count distribution. Pooling categories should follow a scientifically meaningful rule established without searching for a favorable result. Alternatively, simulate multinomial samples under the fully specified null and compare their Pearson statistics with the observed one. Different bin boundaries can alter the test's sensitivity.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, purpose and binning discussion)

## Connections
The frizzled-chicken genetic counts give statistic $0.72043$ and upper-tail probability $0.69753$. The small value means those counts are unsurprising under the model; a goodness-of-fit test cannot certify that a genetic model is uniquely correct. Fitting parameters from the same counts changes the limiting degrees of freedom and requires a separate calibration, which is the subject of the [chi-squared test with estimated parameters](chi-squared-test-with-estimated-parameters.qmd).{{cite:nist_chi_square_gof2002}} (§1.3.5.15, “Critical Region”)

## Definition
Suppose each of $n$ independent trials falls in one of $k$ categories with known probabilities $p_i>0$ summing to one. Let $O_i$ be the count in category $i$ and $E_i=np_i$. Pearson's statistic is
$$
T=\sum_{i=1}^k\frac{(O_i-E_i)^2}{E_i}.
$$
Under this fully specified multinomial model, $T$ is approximately $\chi^2_{k-1}$ when $n$ is large and every $E_i$ is not small. The lost degree of freedom is the constraint $\sum_i(O_i-E_i)=0$. No parameter has been estimated from the counts. Four fixed positive probabilities therefore leave three degrees of freedom, not four and not two.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, “Definition”){{cite:openintro2019}} (§6.3.2–6.3.4, chi-square statistic, distribution and p-value)

## Statistical use
For sixty trials and probabilities $(1/3,1/3,1/3)$, the counts $(18,12,30)$ give expectations of $20$ and $T=8.4$. On two degrees of freedom the upper-tail probability is about $0.0150$, so the equal-probability model is rejected at $5\%$. The counts $(20,15,25)$ give $T=2.5$ and an upper-tail probability of about $0.2865$, which does not reject. The same reference answers both calculations. A genetic ratio such as $(1/4,1/2,1/4)$ is the same kind of fully specified vector: the expectations are $n$ times those probabilities, and the degrees of freedom are still one less than the number of categories. If a category is assigned probability zero, it cannot be placed in the denominator. A positive count in that category already falsifies the model, and a category that cannot occur and did not occur should be dropped before $T$ is formed.{{cite:openintro2019}} (§6.3.4–6.3.5, p-values and evaluating fit)

## Common misconceptions
The chi-squared approximation is a limit as $n$ grows with $k$ and the probabilities fixed. It is not an exact distribution for a small table, and it is not the normal-sample law of $(n-1)S^2/\sigma^2$. Small expected counts make the continuous tail a rough guide to a discrete distribution. Pooling rare categories changes the hypothesis: the probabilities of the pooled cells must be added, and the degrees of freedom must be recomputed from the new list. Choosing the bins after hunting for a large statistic changes the reference distribution as well. A small $T$ means the counts are close to the specified expectations. The frizzled-chicken value $0.72043$, with tail probability $0.69753$, is unsurprising under its model. It does not prove that no other probability vector could have produced similar counts.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, purpose and binning discussion){{cite:nist_chi_square_gof2002}} (§1.3.5.15, “Critical Region”)

## History
Pearson's goodness-of-fit comparison is the ancestor of this statistic: observed counts against expectations from a stated probability model. Later work separated that fully specified comparison from the comparison in which parameters are estimated from the same table. The degrees of freedom $k-1$ belong to the known-probability case. Estimating $r$ regular parameters from the counts changes the limit to $k-1-r$ under the conditions of that extension. Quoting $k-1$ after a fitted parameter, or quoting $k-1-r$ when nothing was fitted, uses the wrong reference even when the arithmetic of $T$ is unchanged.{{cite:openintro2019}} (§6.3, “Testing for goodness of fit using chi-square”)

## Interpretation
With known probabilities the only constraint on the counts is that they sum to the sample size. Sixty trials and probabilities $(1/3,1/3,1/3)$ give expectations of $20$. The counts $(18,12,30)$ produce statistic $8.4$ and an upper-tail probability of about $0.0150$ on two degrees of freedom, so the equal-probability model is rejected at $5\%$. The counts $(20,15,25)$ produce statistic $2.5$ and an upper-tail probability of about $0.2865$, which does not reject. The genetic counts that motivate the comparison are the same kind of fully specified vector. Their expectations are the sample size times the stated probabilities, and the degrees of freedom are still one less than the number of categories.

A category with probability zero cannot be placed in the denominator. A positive count there already contradicts the model. A category that cannot occur and did not occur should be dropped before the statistic is formed. The chi-squared tail is a large-sample approximation with the number of categories and the probabilities held fixed. It is a rough guide when some expected counts are small, and it is a different theorem from the exact chi-squared law of a normal sample variance.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, “Definition”)
