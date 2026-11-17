## Motivating example

Suppose a clinician measures sodium concentration and heart function for each patient. A scatterplot shows the paired observations, but one number may help compare the direction and strength of their straight-line pattern with another pair of measurements. Sodium and heart function use different units; dividing their sample covariance by both sample standard deviations removes those units. The result is the sample correlation coefficient. It describes a feature of the observed pairs, while the corresponding population correlation remains an unknown parameter.{{cite:dodge2008}} (pp. 115–117, definition and sample coefficient)

## Intuition

Center each column at its own mean. A pair contributes positively to correlation when both measurements are above their means or both are below, and negatively when they fall on opposite sides. Divide by the lengths of the two centered columns to compare patterns rather than measurement scales. A nearly straight increasing cloud gives a value near $1$; a decreasing one gives a value near $-1$. A diffuse cloud need not have a value near zero if a few distant pairs dominate its cross-products, so the number should be read beside the plotted data.{{cite:hannay2019_statsdata}} (Ch. 11 §11.4.1, correlation and slope)

## Definition

Write $S_{xx}=\sum_i(x_i-\bar x)^2$, $S_{yy}=\sum_i(y_i-\bar y)^2$, and $S_{xy}=\sum_i(x_i-\bar x)(y_i-\bar y)$ for $n$ paired observations. Then $r=S_{xy}/\sqrt{S_{xx}S_{yy}}$ when both squared-deviation sums are positive. This is the Pearson sample correlation, often written $R$ in inference problems. The same value comes from dividing the sample covariance $S_{xy}/(n-1)$ by the two sample standard deviations: all factors of $n-1$ cancel. The coefficient is undefined if either recorded variable is constant, because there is no observed scale against which to standardize it.{{cite:dodge2008}} (p. 117, sample coefficient)

The population coefficient $\rho=\operatorname{Cov}(X,Y)/(\sigma_X\sigma_Y)$ refers to a distribution with finite positive variances. A sample $r$ estimates $\rho$ when the paired observations represent that population under an appropriate sampling design. A numerical value calculated from a convenience sample is still a valid description of those recorded pairs; treating it as an estimate for a wider population needs additional assumptions about how the pairs were obtained. {{cite:dodge2008}} (p. 117, population and sample coefficients)

## Interpretation

The sign records the direction of a linear trend and the magnitude records how closely the centered points align with a line. The number has no units. Replacing metres by centimetres or adding a constant to every measurement leaves its magnitude unchanged; reversing one measurement scale reverses its sign. These properties make comparisons across units possible, but they do not turn a descriptive association into a causal effect. The sodium–ejection-fraction plot above makes the related problem of overplotting visible: many exact recorded pairs can occupy the same pixel, whereas jitter used only for display helps reveal their multiplicity without changing the numbers used for $r$.{{cite:hannay2019_statsdata}} (Ch. 11 §11.4.1)

The scatterplot matrix below puts several pairwise patterns on the same page. Each correlation describes one of those pairs; it does not describe the entire joint distribution. Curvature, clusters and outlying points can all matter even when a linear summary seems simple{{cite:dodge2008}} (pp. 115–117, definition and sample coefficient).

## Properties

The centered values form two vectors. Their normalized inner product is $r$, so Cauchy–Schwarz gives $-1\le r\le1$. Equality in magnitude means the nonconstant recorded pairs lie exactly on an increasing or decreasing straight line. Multiplying $x$ by $b\ne0$ and $y$ by $d\ne0$ changes $r$ to $\operatorname{sign}(bd)r$, while shifts do nothing. Thus a negative unit conversion changes direction without changing the strength of the line pattern.{{cite:dodge2008}} (pp. 115–116, bounds and interpretation)

For a least-squares line with an intercept, the fitted slope is $\widehat\beta_1=S_{xy}/S_{xx}$ and the coefficient of determination is $R^2=r^2$. In this particular model, $r^2$ is the fraction of the observed $y$ sum of squares explained by the fitted line. It is not a general fraction of outcomes *caused* by $x$, and the sign of the slope is the sign of $r$. These relations explain why testing the simple-regression slope and testing zero correlation can use the same statistic under their respective normal models. {{cite:hannay2019_statsdata}} (Ch. 11 §11.4.1–11.4.2, correlation and fit){{cite:dodge2008}} (pp. 117–118, simple-regression relation)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $u_i=x_i-\bar x$ and $v_i=y_i-\bar y$. Cauchy–Schwarz gives $|\sum u_iv_i|\le\sqrt{\sum u_i^2\sum v_i^2}$, so $|r|\le1$. Equality holds precisely when $v_i=cu_i$ for all $i$ and some nonzero $c$; then $y_i=\bar y+c(x_i-\bar x)$, an exact line. If $x_i'=a+bx_i$ and $y_i'=c+dy_i$, the centered vectors become $bu$ and $dv$. Their cross-product is multiplied by $bd$ and their lengths by $|b|$ and $|d|$, proving the rescaling rule{{cite:dodge2008}} (pp. 115–117, definition and sample coefficient).

For the regression relation, $\widehat y_i=\bar y+\widehat\beta_1(x_i-\bar x)$ and $\widehat\beta_1=S_{xy}/S_{xx}$. The explained sum of squares is $\widehat\beta_1^2S_{xx}=S_{xy}^2/S_{xx}$; dividing by $S_{yy}$ yields $R^2=S_{xy}^2/(S_{xx}S_{yy})=r^2$. The residual sum of squares is therefore $S_{yy}(1-r^2)$. With $s^2=S_{yy}(1-r^2)/(n-2)$ and standard error $s/\sqrt{S_{xx}}$, the slope statistic reduces to $\widehat\beta_1/(s/\sqrt{S_{xx}})=r\sqrt{n-2}/\sqrt{1-r^2}$. {{cite:hannay2019_statsdata}} (Ch. 11 §11.4, correlation and $R^2$)

For independent pairs from a bivariate normal distribution with $\rho=0$, $X$ and $Y$ are independent and, conditional on the observed nonconstant $x$ values, the $y$ values are independent normals with a constant mean and variance. Orthogonal projection of the normal error vector onto the centered $x$ direction yields a standard normal slope numerator. Projection onto the $n-2$-dimensional residual space yields an independent chi-squared sum divided by the error variance. Their ratio has a $t_{n-2}$ law. This is the exact reference distribution for the statistic above when the stated model and $n>2$ hold. {{cite:dodge2008}} (p. 117, test statistic and reference law)
:::
:::

## Statistical use — Summarizing a straight-line association

Plot each pair first, check that both variables vary, and decide which population the sample can represent. Report $r$ together with the sample size and enough context to identify the measurements. A test of $H_0:\rho=0$ uses $t=r\sqrt{n-2}/\sqrt{1-r^2}$ and an exact $t_{n-2}$ reference for independent bivariate-normal pairs under the null. It tests zero *linear* population correlation, not absence of every possible relationship. Confidence intervals and hypothesis tests also describe sampling uncertainty that the point value $r$ alone cannot show.{{cite:dodge2008}} (p. 117, hypothesis test)

The preserved 20-pair test below illustrates that a moderately positive observed coefficient can miss a fixed significance threshold. Its population value was set by simulation, so the failure to reject is visibly a sampling outcome rather than evidence that the true correlation is zero. In observational work, a positive or negative $r$ also cannot identify whether a third variable, reverse direction, selection or chance produced the association. {{cite:hannay2019_statsdata}} (Ch. 11 §11.4.1, association and causation)

## Worked example

For the four pairs $(1,1),(2,2),(3,4),(4,3)$, both column means are $2.5$. The centered $x$ values are $(-1.5,-0.5,0.5,1.5)$ and the centered $y$ values are $(-1.5,-0.5,1.5,0.5)$. Their squared-deviation sums are $S_{xx}=S_{yy}=5$, while $S_{xy}=4$. Consequently $r=4/\sqrt{5\cdot5}=0.8$. A fitted line with an intercept explains $r^2=0.64$ of the observed $y$ sum of squares. The swapped last two $y$ values keep the association positive but prevent a perfect straight line.{{cite:hannay2019_statsdata}} (Ch. 11 §11.4.2, $R^2$)

**Your turn.** Convert every response to $y'=10-2y$, leaving the four $x$ values as they are. Find the new $r$ and the new regression $R^2$ without recomputing all four cross-products.

::: {.callout-tip collapse="true" title="Answer"}
The shift by $10$ has no effect, while multiplying just the response by $-2$ reverses the correlation's sign. The new coefficient is $-0.8$; its square remains $R^2=0.64$. The fitted line now slopes down, but its proportion of fitted sample variation is unchanged.
:::

## Common misconceptions

A coefficient of zero means no *linear* pattern in the sample, not necessarily independence. For $x=(-2,-1,0,1,2)$ and $y=x^2$, the centered cross-product sum is zero although every $y$ value is determined by $x$. A large coefficient is not a causal effect: variables can share a cause or the observed set can be selected. Nor is $r$ a regression slope; it is unitless, while the slope changes if either variable is remeasured in new units. Finally, a small $p$-value for zero correlation does not make a nearly straight line inevitable; sample size also influences the test.{{cite:hannay2019_statsdata}} (Ch. 11 §11.4.1, slope and cautions)

## Assumptions and limits — When the summary fails

If all four $x$ measurements equal $3$, then $S_{xx}=0$ and $r$ is undefined, no matter how the responses vary. Even when defined, a single extreme pair can change the sign or magnitude sharply; the four-pair worked example's $r=0.8$ becomes negative if $(10,-10)$ is added. A curved U-shaped relation can have $r=0$, and separate subgroups can have within-group patterns unlike the pooled coefficient. Inspect support, groups and influential points before giving the summary a substantive reading.{{cite:dodge2008}} (p. 118, domains and limitations)

The formula for $r$ itself does not require normality. The exact small-sample $t$ law above does require its distributional model and independent pairs. Correlated repeated observations, heavy-tailed data or a sample chosen by an outcome can make a nominal $t$-based $p$-value misleading even when the arithmetic of $r$ is correct. A rank correlation or a different model may then answer a more suitable question. {{cite:dodge2008}} (pp. 117–118, reference distribution and domains)

## Connections

[Correlation](correlation.qmd) names the population-level association and its general properties. [Covariance](covariance.qmd) supplies the unscaled numerator; [scatterplot](scatterplot.qmd) shows structure the single ratio can hide. [Simple linear regression](simple-linear-regression.qmd) converts the same cross-products into a slope, while [partial correlation](partial-correlation.qmd) describes association after adjustment for other variables. The [mean vector and covariance matrix](mean-vector-and-covariance-matrix.qmd) collect multivariate summaries; their standardized covariance entries form a correlation matrix, whose entries cannot be chosen independently.{{cite:hannay2019_statsdata}} (Ch. 11 §11.4.1)

## History

Galton's work on heredity and regression in the late nineteenth century motivated the language of correlation. He used “co-relation” and “correlation” in 1888, and Pearson and Edgeworth developed the quantitative theory and the term “correlation coefficient.” The modern sample formula belongs to that subsequent mathematical development; its everyday use is now tied to scatterplots, regression and inference.{{cite:dodge2008}} (pp. 115–116, History)
