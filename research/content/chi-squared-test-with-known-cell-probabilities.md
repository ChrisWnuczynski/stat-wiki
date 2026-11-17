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
The frizzled-chicken calculation below has statistic $0.72043$ and upper-tail probability $0.69753$. Its small value means those counts are unsurprising under the model; a goodness-of-fit test cannot certify that a genetic model is uniquely correct. Fitting parameters from the same counts changes the limiting degrees of freedom and requires a separate calibration.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, “Critical Region”)
