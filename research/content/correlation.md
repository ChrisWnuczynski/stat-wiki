## Lead context
Correlation puts two measurements' linear association on a common scale, so their units do not determine the reported strength. Its sign says which direction the variables tend to move together, while its magnitude describes how closely the pattern follows a straight line. A scatterplot and the study design help interpret that number.{{cite:nist_correlation2013}} (Description) {{cite:dicker2025_cdc}} (Ch. 8, “Planning the Analysis”)

## Motivating example
Suppose a clinic records age and a laboratory measurement on each patient. Their covariance has units of years times laboratory units, and its size changes if years are replaced by months. Their Pearson correlation is unchanged by that positive unit conversion. It can help compare linear associations measured in different units, while a scatterplot shows whether a straight-line summary fits the pairs.{{cite:wang2025_foundations}} (Ch. 3, §4.4.2) {{cite:nist_correlation2013}} (Description)

## Intuition
Subtract each variable's mean and divide by its standard deviation. Correlation is the expected product of these standardised deviations. Products tend to be positive when both measurements are above or both below their respective means and negative when they move in opposite directions. Cauchy–Schwarz keeps the average product between $-1$ and $1$.{{cite:wang2025_foundations}} (Ch. 7, Example 24)

## Definition
For random variables $X$ and $Y$ with finite positive standard deviations $\sigma_X$ and $\sigma_Y$, means $\mu_X,\mu_Y$, and covariance $\sigma_{XY}$, Pearson's population correlation is

$$
\rho=\frac{\sigma_{XY}}{\sigma_X\sigma_Y}
=\mathbb E\!\left[\frac{X-\mu_X}{\sigma_X}\frac{Y-\mu_Y}{\sigma_Y}\right].
$$

For coordinates $X_j,X_k$ of a random vector, the same coefficient is written $\rho_{jk}$. If either standard deviation is zero, the denominator vanishes and Pearson correlation is undefined. The covariance's units cancel against those of the standard deviations.{{cite:wang2025_foundations}} (Ch. 3, §4.4.2) {{cite:strimmer2025_mva}} (Ch. 1, §1.1, “Correlation matrix”)

For observed pairs $(x_i,y_i)$, $i=1,\ldots,n$, with nonzero variation in each column, the sample correlation is

$$
r=\frac{\sum_i(x_i-\overline x)(y_i-\overline y)}
{\sqrt{\sum_i(x_i-\overline x)^2\sum_i(y_i-\overline y)^2}},
$$

where $\overline x,\overline y$ are the two sample means. It estimates $\rho$ under a suitable sampling model. The sample-covariance divisors cancel between numerator and denominator, leaving centred sums in the final ratio.{{cite:nist_correlation2013}} (Description)

## Properties
The bound $|\rho|\le1$ follows from Cauchy–Schwarz. For positive variances, $\rho=1$ holds exactly when $Y=a+bX$ almost surely for some $b>0$; $\rho=-1$ has the same form with $b<0$. Thus a perfect population correlation characterises a straight-line relation up to probability-zero exceptions.{{cite:wang2025_foundations}} (Ch. 7, Example 24)

Changing units by $X'=a+bX$ and $Y'=c+dY$ leaves the magnitude of correlation unchanged for nonzero $b,d$ and multiplies its sign by the sign of $bd$. The diagonal of a correlation matrix is one, and the whole matrix is positive semi-definite; a proposed array of pairwise numbers can fail to be a valid correlation matrix even if every entry lies between $-1$ and $1$. The identity $P=D^{-1}\Sigma D^{-1}$ relates the correlation matrix to the covariance matrix.{{cite:strimmer2025_mva}} (Ch. 1, §1.1, “Correlation matrix”)

Correlation also controls the best *linear* prediction of $Y$ from $X$ in mean squared error. Its slope is $b=\rho\sigma_Y/\sigma_X$, its intercept is $\mu_Y-b\mu_X$, and its remaining mean squared prediction error is $\sigma_Y^2(1-\rho^2)$. With an intercept in this one-predictor population calculation, $\rho^2$ is the fraction of $Y$ variance captured by the linear predictor. The conditional mean equals this line in the jointly normal case.{{cite:hannay2019_statsdata}} (Ch. 11, §11.4) {{cite:wang2025_foundations}} (Ch. 6 Extra, Example 27)

Independence implies zero correlation when the variances exist, while a symmetric $X$ and $Y=X^2$ give a dependent pair with zero covariance. For a *jointly normal* pair, zero correlation does imply independence. These statements distinguish linear association from general dependence.{{cite:wang2025_foundations}} (Ch. 6 Extra, Example 27)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Set $U=(X-\mu_X)/\sigma_X$ and $V=(Y-\mu_Y)/\sigma_Y$. Both have mean zero and variance one. Cauchy–Schwarz gives $|\mathbb E(UV)|\le\sqrt{\mathbb E(U^2)\mathbb E(V^2)}=1$. Equality means $V$ is a constant multiple of $U$ almost surely; unit variances force that multiple to be $+1$ or $-1$. Rearranging gives the asserted affine relation and slope sign. For $X'=a+bX$, $Y'=c+dY$, covariance becomes $bd\sigma_{XY}$ and standard deviations become $|b|\sigma_X,|d|\sigma_Y$, proving the unit rule.{{cite:wang2025_foundations}} (Ch. 7, Example 24)

For a random vector with covariance matrix $\Sigma$ and positive diagonal standard deviations collected in $D$, direct entrywise division gives $P=D^{-1}\Sigma D^{-1}$ and $\Sigma=DPD$. The diagonal entries equal one. For any fixed vector $z$, $z^\top Pz=(D^{-1}z)^\top\Sigma(D^{-1}z)\ge0$, since a covariance matrix is positive semi-definite. This also explains why pairwise bounds alone are insufficient: the full quadratic-form condition must hold.{{cite:strimmer2025_mva}} (Ch. 1, §1.1, “Properties of the covariance matrix” and “Correlation matrix”)

For linear prediction, expand $\mathbb E[(Y-a-bX)^2]$ around the two means. At fixed $b$ it is smallest at $a=\mu_Y-b\mu_X$. The remaining quadratic is $\sigma_Y^2-2b\sigma_{XY}+b^2\sigma_X^2$, whose derivative vanishes at $b=\sigma_{XY}/\sigma_X^2=\rho\sigma_Y/\sigma_X$. Substitution leaves $\sigma_Y^2(1-\rho^2)$.{{cite:hannay2019_statsdata}} (Ch. 11, §11.4)

Independence gives $\mathbb E(XY)=\mathbb E X\mathbb E Y$, hence zero covariance. For $X$ standard normal, $\operatorname{Cov}(X,X^2)=\mathbb E X^3-\mathbb E X\mathbb E X^2=0$ by symmetry, while the nonconstant $X^2$ is determined by $X$ and thus dependent on it. When a pair is jointly normal and $\rho=0$, its joint density factors into the product of its marginal densities.{{cite:wang2025_foundations}} (Ch. 6 Extra, Example 27)
:::
:::

## Statistical use
Plot the paired observations before quoting a sample correlation. A curved pattern, separated groups, or one influential point can make a single linear summary misleading. In a simple linear regression with an intercept, the squared sample correlation equals the fitted $R^2$. Tests or intervals for a population correlation need a sampling model. An observed association also calls for checking chance, selection, and confounding before giving it a causal interpretation.{{cite:hannay2019_statsdata}} (Ch. 11, §11.4) {{cite:dicker2025_cdc}} (Ch. 8, “Epidemiologic Interpretation Checklist 1”)

## Worked example
Take three observed pairs $(1,1)$, $(2,3)$, and $(3,2)$. Both sample means are $2$. The centred $x$ values are $-1,0,1$ and the centred $y$ values are $-1,1,0$. Their cross-product sum is $1$ and each squared-deviation sum is $2$, so $r=1/\sqrt{2\cdot2}=1/2$. The sample covariance is $1/(3-1)=1/2$, and each sample variance is $2/(3-1)=1$, giving the same result after standardisation. The value $r=1/2$ summarizes these three pairs; $\rho$ denotes the corresponding population parameter.{{cite:nist_correlation2013}} (Description)

**Your turn.** Replace the second coordinate by $y'=5-2y$ for each of the three pairs. What is the new sample correlation? What happens if instead every $x$ value is multiplied by $12$?{{cite:wang2025_foundations}} (Ch. 3, §4.4.2)

::: {.callout-tip collapse="true" title="Answer"}
The factor on $y$ is negative, so the correlation becomes $-1/2$; adding $5$ does not affect it. Multiplying all $x$ values by positive $12$ leaves it at $1/2$.
:::

The [uncorrelated but dependent exercise](../questions/ex-sl-01-3.qmd) gives a pair with zero correlation that remains dependent.{{cite:strimmer2025_mva}} (Ch. 1, §1.1)

## Common misconceptions
Correlation near zero can accompany strong nonlinear dependence: the $X$ and $X^2$ construction is a precise example. Confounding, reverse direction, selection, or chance can explain an observed association. To express linear prediction in the variables' units, multiply the correlation by $\sigma_Y/\sigma_X$ to obtain the slope of the best linear predictor of $Y$ from $X$.{{cite:wang2025_foundations}} (Ch. 6 Extra, Example 27) {{cite:dicker2025_cdc}} (Ch. 8, “Epidemiologic Interpretation Checklist 1”) {{cite:hannay2019_statsdata}} (Ch. 11, §11.4)

## Assumptions and limits
The population coefficient needs positive finite variances; the sample coefficient needs variation in both observed columns. Both coefficients are defined for non-normal variables. Normality enters the special independence result and some familiar inference formulas. A single outlier can strongly change Pearson's sample coefficient, and a nonlinear or subgroup structure may be poorly represented by one straight-line summary. Each pair must belong to the same sampling unit.{{cite:nist_correlation2013}} (Description) {{cite:wang2025_foundations}} (Ch. 6 Extra, Example 27)

## Connections
[Covariance](covariance.qmd) is the numerator of Pearson correlation, while the [mean vector and covariance matrix](mean-vector-and-covariance-matrix.qmd) collect all pairwise numerators for a random vector. The [sample correlation coefficient](sample-correlation-coefficient.qmd) estimates the population coefficient from data. [Partial correlation](partial-correlation.qmd) measures linear association after adjusting linearly for other coordinates, and [simple linear regression](simple-linear-regression.qmd) supplies the best-linear-predictor relationship proved above. Causal interpretation also requires study design and subject-matter evidence.{{cite:strimmer2025_mva}} (Ch. 6, “Related quantity: partial correlation”) {{cite:dicker2025_cdc}} (Ch. 8, “Epidemiologic Interpretation Checklist 1”)

## History
Francis Galton's 1886 study of hereditary stature compared children's heights with their parents' heights. He used these paired measurements to investigate regression toward average stature. His paper describes 930 adult children from 205 parentages and explains why he had first studied the same pattern using seeds.{{cite:galton1886}} (pp. 246–247)

Correlation later became a standard way to report the strength and direction of a linear association in a dimensionless number. In multivariate work, the pairwise coefficients form a correlation matrix obtained by standardizing a covariance matrix. The same coefficient also enters the slope of a one-predictor regression line.{{cite:wang2025_foundations}} (Ch. 3, §4.4.2) {{cite:strimmer2025_mva}} (Ch. 1, §1.1, “Correlation matrix”) {{cite:hannay2019_statsdata}} (Ch. 11, §11.4)
