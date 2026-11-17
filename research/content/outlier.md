## Motivating example

Suppose nine delivery times, in minutes, are $2,3,3,4,5,6,7,8,20$. The last delivery is visibly separated from the others. The median is $5$, while the mean is $58/9\approx6.44$; without the last delivery the mean is $38/8=4.75$. The difference matters if the mean is used to forecast total delivery time, but it does not tell us whether the $20$ was a typo, a genuine delay, or a sign that deliveries have a long right tail. The data record and the scientific question must decide what happens next.{{cite:nist_handbook2002}} (§1.3.5.17, “Detection of Outliers,” Introduction and Labeling, Accommodation, Identification)

## Definition

An observation is *outlying* relative to a comparison set or a proposed distribution when it is unusually separated from the bulk expected under that comparison. There is no model-free numerical threshold that decides every case. For example, a large insurance claim may be surprising under a normal model and ordinary under a heavy-tailed claim model. A boxplot fence is a descriptive *label* for further investigation, not a conclusion that the observation could not have arisen from the population.{{cite:dodge2008}} (p. 404, definition and “Domains and Limitations”){{cite:nist_handbook2002}} (§1.3.5.17, Introduction and Normality Assumption)

For ordered observations with lower and upper quartiles $Q_1$ and $Q_3$, write $IQR=Q_3-Q_1$. The customary inner fences are $Q_1-1.5IQR$ and $Q_3+1.5IQR$. An observation beyond either fence is plotted separately as a possible outlier. Quartile conventions vary for small samples, so a software package can put a value just inside or outside a fence without disagreeing about the underlying data. The further outer fences at $3IQR$ mark more extreme departures in one version of the display. {{cite:nist_handbook2002}} (§1.3.3.7, “Box Plot,” Box plots with fences)

## Interpretation

Labeling, identifying and accommodating outliers are different tasks. A fence or a plot labels unusual values. A formal test identifies departures under a specified distributional model and error rate. Accommodation asks whether the analysis should use a robust estimator, a different error distribution, or a model with several populations. If the source record confirms a transcription error, correction is appropriate; if the value is genuine, deleting it solely because it crosses a fence changes the analysis after seeing the result.{{cite:nist_handbook2002}} (§1.3.5.17, Introduction; Labeling, Accommodation, Identification)

The *response* need not be extreme for an observation to matter to a regression fit. A point with a predictor far from the others has high leverage; its influence also depends on its residual and on the fitted model. Conversely, an extreme response at a typical predictor value need not move the fitted slope much. A useful investigation therefore checks the raw record, plots the variable in context, and compares fitted conclusions with and without the observation while reporting both analyses when the value is genuine. {{cite:nist_handbook2002}} (§1.3.5.17, Introduction and graphical techniques)

## Properties

Fences move with a change of origin and scale. If every observation becomes $a+bx$ with $b>0$, both quartiles become $a+bQ_j$, the interquartile range becomes $bIQR$, and each fence becomes the same transformed fence. Thus changing minutes to seconds cannot by itself change which observations are flagged. A strictly increasing nonlinear transformation does not generally preserve this flag: taking logarithms compresses a long right tail and changes the spacing relative to the quartiles.{{cite:nist_handbook2002}} (§1.3.3.7, “Box Plot,” Box plots with fences)

A standardized score $z_i=(x_i-\bar x)/s$, with the sample standard deviation $s$, may be a poor small-sample screening rule because the observation being assessed also affects $\bar x$ and $s$. In a sample of size $n>1$, its magnitude is bounded by $(n-1)/\sqrt n$. Even an arbitrarily distant single point among four identical values therefore has a largest possible score of $4/\sqrt5\approx1.79$ when $n=5$. A rule requiring $|z|>2$ cannot flag that point, no matter how far away it is. Median-based scores and graphical checks avoid this particular self-masking mechanism, although neither automatically identifies errors. {{cite:nist_handbook2002}} (§1.3.5.17, Z-Scores and Modified Z-Scores; Masking and Swamping)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Put $r_j=x_j-\bar x$. Since $\sum_jr_j=0$, the other $n-1$ residuals sum to $-r_i$. Cauchy–Schwarz gives $\sum_{j\ne i}r_j^2\ge r_i^2/(n-1)$. Hence
$$
s^2=\frac{\sum_jr_j^2}{n-1}\ge\frac{n r_i^2}{(n-1)^2},
\qquad \left|\frac{r_i}{s}\right|\le\frac{n-1}{\sqrt n}.
$$
Equality holds when all other observations are equal, so the bound is sharp. Under $y_j=a+bx_j$ with $b>0$, quartiles and their differences transform as $Q_j(y)=a+bQ_j(x)$ and $IQR(y)=bIQR(x)$; substitution in either fence proves the claimed invariance.{{cite:nist_handbook2002}} (§1.3.5.17, Z-Scores and Modified Z-Scores; §1.3.3.7, Box plots with fences)
:::
:::

## Statistical use — Investigating a flagged observation

Begin with the measurement process: inspect units, decimal places, duplicate records, and whether the observation belongs to the intended population. Then compare plots and summaries that expose the observation's position. A boxplot uses quartiles; a histogram or normal quantile plot can reveal whether the whole tail, rather than one point, disagrees with a normal model. For a regression, inspect predictors and influence as well as response residuals. Only after this diagnosis should a model or estimator be changed.{{cite:nist_handbook2002}} (§1.3.5.17, Introduction, Normality Assumption and graphical techniques)

When inference is required, a formal outlier test has its own sampling assumptions. NIST's discussion of common single- and multiple-outlier tests is explicitly limited to approximately normal univariate data; applying such a test to a skewed population can label an ordinary tail value. Repeating a single-outlier test until nothing is rejected does not generally preserve its stated error rate or detect a masked cluster of unusual values. A sensitivity analysis that reports how the estimate changes when a questionable observation is included is often more informative than a silent deletion. {{cite:nist_handbook2002}} (§1.3.5.17, Normality Assumption; Single Versus Multiple Outliers; Masking and Swamping)

The $1.5IQR$ rule does not imply a fixed false-alarm probability across distributions or sample sizes. In a strongly right-skewed distribution, many genuine upper-tail observations may cross its upper fence. If a dataset mixes adults and children, applying one fence to all heights can flag legitimate adults because the comparison population is wrong. If two very large values inflate a mean and standard deviation, a simple $z$-score rule can mask both; asking a single-outlier test to find all outliers is likewise unsuitable. These failures call for context, stratification, robust summaries, or a more suitable distributional model, not automatic deletion.{{cite:nist_handbook2002}} (§1.3.5.17, Normality Assumption; Single Versus Multiple Outliers; Masking and Swamping)
## Worked example

Return to the nine delivery times $2,3,3,4,5,6,7,8,20$. Using hinges that include the median in each half gives $Q_1=3$, $Q_3=7$, and $IQR=4$. The inner fences are $3-1.5(4)=-3$ and $7+1.5(4)=13$. Only $20$ is beyond them. The full-sample mean is $6.44$ to two decimal places; omitting $20$ gives $4.75$, a change of about $1.69$ minutes. These are descriptions of the observed data, not estimates of how likely a typing error is. The retained median of $5$ conveys a different, less tail-sensitive question about a typical delivery.{{cite:nist_handbook2002}} (§1.3.3.7, Box plots with fences; §1.3.5.17, Introduction)

For a separate warning about standardized scores, take $0,0,0,0,10$. Its mean is $2$, its sample standard deviation is $\sqrt{20}\approx4.472$, and the score of $10$ is $8/\sqrt{20}\approx1.789$. Replacing $10$ by $1000$ leaves that score unchanged. The point is obviously separated, but the conventional score cannot exceed the proved bound at this sample size. {{cite:nist_handbook2002}} (§1.3.5.17, Z-Scores and Modified Z-Scores)

**Your turn.** For the ordered sample $1,2,2,3,4,5,6,7,18$, use hinges including the median to calculate the inner fences. Which observation is flagged, and what does the flag establish?

::: {.callout-tip collapse="true" title="Answer"}
The median is $4$, the hinges are $Q_1=2$ and $Q_3=6$, and $IQR=4$. The fences are $2-1.5(4)=-4$ and $6+1.5(4)=12$. Only $18$ is beyond a fence. It deserves investigation; the calculation alone does not show that it is erroneous or justify omitting it.
:::

## Common misconceptions

A point beyond a whisker is not automatically bad data: the fence is a descriptive rule and can flag genuine tail values. A large raw value is not necessarily an outlier without a comparison group or model: the same number can be ordinary in one population and surprising in another. An observation that is not extreme in the response can still strongly influence a regression through its predictor position. Finally, an ordinary-looking standardized score does not certify that a point is unremarkable in a small sample, because the point enlarges its own denominator.{{cite:dodge2008}} (p. 404, definition and “Domains and Limitations”){{cite:nist_handbook2002}} (§1.3.5.17, Introduction; Z-Scores and Modified Z-Scores)

## Connections

The [five-number summary and boxplot](five-number-summary-and-boxplot.qmd) make the quartile fence visible, while the [interquartile range](interquartile-range.qmd) supplies its scale. The [median](median.qmd) is less responsive than the mean to the magnitude of one extreme observation. A [normal quantile plot](normal-quantile-plot.qmd) tests whether a proposed normal shape is plausible across the whole tail, and a [regression slope](regression-slope.qmd) can be influenced by a point whose predictor value is remote.{{cite:nist_handbook2002}} (§1.3.3.7, Box plots with fences; §1.3.5.17, graphical techniques)

## History

Concern about apparently discordant measurements predates modern boxplots. Proposals for rejecting observations appear in nineteenth-century least-squares work, including Legendre's 1805 discussion and Peirce's 1852 criterion, and that rejection was contested. The later development of robust methods offered a way to estimate a pattern without allowing a few extreme observations to dominate it. The modern boxplot fence is best read in that historical spirit: it starts an investigation rather than finishing one.{{cite:dodge2008}} (p. 404, “History” and “Domains and Limitations”){{cite:nist_handbook2002}} (§1.3.3.7, Box plots with fences)
