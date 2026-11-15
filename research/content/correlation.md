## Lead context
Correlation puts two measurements' linear association on a common scale, so their original units do not determine the reported strength. Its sign says which direction the variables tend to move together, while its magnitude describes how closely the pattern follows a straight line. A scatterplot and the study design are needed to interpret that number responsibly.{{cite:nist_correlation2013}}

## Motivating example
Suppose a clinic records age and a laboratory measurement on each patient. Their covariance has units of years times laboratory units, and its size changes if years are replaced by months. Their Pearson correlation is unchanged by that positive unit conversion. It can help compare linear associations measured in different units, but the paired observations and their shape still matter.{{cite:nist_correlation2013}}

## Intuition
Subtract each variable's mean and divide by its standard deviation. Correlation is the expected product of these standardised deviations. Products tend to be positive when both measurements are above or both below their respective means and negative when they move in opposite directions. Squared deviations and the Cauchy–Schwarz inequality keep the average product between $-1$ and $1$.{{cite:anderson2003_mva}}

## Definition
For random variables $X$ and $Y$ with finite positive standard deviations $\sigma_X$ and $\sigma_Y$, means $\mu_X,\mu_Y$, and covariance $\sigma_{XY}$, Pearson's population correlation is

$$
\rho=\frac{\sigma_{XY}}{\sigma_X\sigma_Y}
=\mathbb E\!\left[\frac{X-\mu_X}{\sigma_X}\frac{Y-\mu_Y}{\sigma_Y}\right].
$$

The retained definition above writes $X_j,X_k$ for coordinates of a random vector and $\rho_{jk}$ for their pairwise correlation; this two-variable formula is the same rule without coordinate subscripts. If either standard deviation is zero, the denominator vanishes and Pearson correlation is undefined. The covariance's units cancel against those of the standard deviations.{{cite:nist_correlation2013,anderson2003_mva}}

For observed pairs $(x_i,y_i)$, $i=1,\ldots,n$, with nonzero variation in each column, the sample correlation is

$$
r=\frac{\sum_i(x_i-\overline x)(y_i-\overline y)}
{\sqrt{\sum_i(x_i-\overline x)^2\sum_i(y_i-\overline y)^2}},
$$

where $\overline x,\overline y$ are the two sample means. It estimates $\rho$ under a suitable sampling model. The corrected sample-covariance divisors cancel between numerator and denominator; this formula does not require choosing $n$ or $n-1$ in the final ratio.{{cite:nist_correlation2013}}

## Properties
The bound $|\rho|\le1$ follows from Cauchy–Schwarz. For positive variances, $\rho=1$ holds exactly when $Y=a+bX$ almost surely for some $b>0$; $\rho=-1$ has the same form with $b<0$. Thus a perfect population correlation characterises a straight-line relation up to probability-zero exceptions, matching the equality claim in the retained interpretation.{{cite:anderson2003_mva,nist_correlation2013}}

Changing units by $X'=a+bX$ and $Y'=c+dY$ leaves the magnitude of correlation unchanged for nonzero $b,d$ and multiplies its sign by the sign of $bd$. The diagonal of a correlation matrix is one, and the whole matrix is positive semi-definite; a proposed array of pairwise numbers can fail to be a valid correlation matrix even if every entry lies between $-1$ and $1$. The retained matrix identity $P=D^{-1}\Sigma D^{-1}$ makes the unit conversion precise.{{cite:anderson2003_mva}}

Correlation also controls the best *linear* prediction of $Y$ from $X$ in mean squared error. Its slope is $b=\rho\sigma_Y/\sigma_X$, its intercept is $\mu_Y-b\mu_X$, and its remaining mean squared prediction error is $\sigma_Y^2(1-\rho^2)$. With an intercept in this one-predictor population calculation, $\rho^2$ is the fraction of $Y$ variance captured by the linear predictor. This does not assert that the actual conditional mean is linear unless the model supplies that condition.{{cite:anderson2003_mva}}

Independence implies zero correlation when the variances exist, but the converse fails: a symmetric $X$ and $Y=X^2$ can be dependent with zero covariance. For a *jointly normal* pair, zero correlation does imply independence. Those conclusions require different assumptions, so a zero observed sample correlation cannot by itself prove independence in a population.{{cite:anderson2003_mva}}

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Set $U=(X-\mu_X)/\sigma_X$ and $V=(Y-\mu_Y)/\sigma_Y$. Both have mean zero and variance one. Cauchy–Schwarz gives $|\mathbb E(UV)|\le\sqrt{\mathbb E(U^2)\mathbb E(V^2)}=1$. Equality means $V$ is a constant multiple of $U$ almost surely; unit variances force that multiple to be $+1$ or $-1$. Rearranging gives the asserted affine relation and slope sign. For $X'=a+bX$, $Y'=c+dY$, covariance becomes $bd\sigma_{XY}$ and standard deviations become $|b|\sigma_X,|d|\sigma_Y$, proving the unit rule.{{cite:anderson2003_mva}}

For a random vector with covariance matrix $\Sigma$ and positive diagonal standard deviations collected in $D$, direct entrywise division gives $P=D^{-1}\Sigma D^{-1}$ and $\Sigma=DPD$. The diagonal entries equal one. For any fixed vector $z$, $z^\top Pz=(D^{-1}z)^\top\Sigma(D^{-1}z)\ge0$, since a covariance matrix is positive semi-definite. This also explains why pairwise bounds alone are insufficient: the full quadratic-form condition must hold.{{cite:anderson2003_mva}}

For linear prediction, expand $\mathbb E[(Y-a-bX)^2]$ around the two means. At fixed $b$ it is smallest at $a=\mu_Y-b\mu_X$. The remaining quadratic is $\sigma_Y^2-2b\sigma_{XY}+b^2\sigma_X^2$, whose derivative vanishes at $b=\sigma_{XY}/\sigma_X^2=\rho\sigma_Y/\sigma_X$. Substitution leaves $\sigma_Y^2(1-\rho^2)$. Independence gives $\mathbb E(XY)=\mathbb E X\mathbb E Y$, hence zero covariance. For $X$ standard normal, $\operatorname{Cov}(X,X^2)=\mathbb E X^3-\mathbb E X\mathbb E X^2=0$ by symmetry, while the nonconstant $X^2$ is completely determined by $X$ and thus dependent on it. Finally, when a pair is jointly normal and $\rho=0$, its joint normal density factors into the product of its marginal normal densities; conversely independence gives zero correlation as already shown.{{cite:anderson2003_mva}}
:::
:::

## Statistical use
Plot the paired observations before quoting a sample correlation. A curved pattern, separated groups, or one influential point can make a single linear summary misleading. In a simple linear regression with an intercept, the squared sample correlation equals the fitted $R^2$, but that numerical identity does not turn an observational association into a causal effect. Tests or intervals for a population correlation need a sampling model; they are not encoded in the value of $r$ alone.{{cite:nist_correlation2013,anderson2003_mva,dicker2025_cdc}}

## Worked example
Take three observed pairs $(1,1)$, $(2,3)$, and $(3,2)$. Both sample means are $2$. The centred $x$ values are $-1,0,1$ and the centred $y$ values are $-1,1,0$. Their cross-product sum is $1$ and each squared-deviation sum is $2$, so $r=1/\sqrt{2\cdot2}=1/2$. The corrected sample covariance is $1/(3-1)=1/2$, and each sample variance is $2/(3-1)=1$, giving the same result after standardisation. The retained population example also yields $1/2$, but a sample calculation and a population parameter are different objects.{{cite:nist_correlation2013}}

**Your turn.** Replace the second coordinate by $y'=5-2y$ for each of the three pairs. What is the new sample correlation? What happens if instead every $x$ value is multiplied by $12$?

::: {.callout-tip collapse="true" title="Answer"}
The factor on $y$ is negative, so the correlation becomes $-1/2$; adding $5$ does not affect it. Multiplying all $x$ values by positive $12$ leaves it at $1/2$.
:::

## Common misconceptions
Correlation near zero does not mean “no relationship”: the $X$ and $X^2$ construction is a precise counterexample. A large correlation does not establish causality, because confounding, reverse direction, selection, or chance may explain an observational pattern. Correlation also is not a slope in the variables' original units; multiplying the correlation by $\sigma_Y/\sigma_X$ gives the slope of the best linear predictor of $Y$ from $X$.{{cite:anderson2003_mva,nist_correlation2013,dicker2025_cdc}}

## Assumptions and limits
The population coefficient needs positive finite variances; the sample coefficient needs variation in both observed columns. Neither requires a normal distribution merely to be *defined*. Normality enters the special independence result and some familiar inference formulas. A single outlier can strongly change Pearson's sample coefficient, and a nonlinear or subgroup structure may be poorly represented by one straight-line summary. Interpretation also requires that pairs correspond to the same sampling units.{{cite:nist_correlation2013,anderson2003_mva}}

## Connections
[Covariance](covariance.qmd) is the numerator of Pearson correlation, while the [mean vector and covariance matrix](mean-vector-and-covariance-matrix.qmd) collect all pairwise numerators for a random vector. The [sample correlation coefficient](sample-correlation-coefficient.qmd) estimates the population coefficient from data. [Partial correlation](partial-correlation.qmd) measures linear association after adjusting linearly for other coordinates, and [simple linear regression](simple-linear-regression.qmd) supplies the best-linear-predictor relationship proved above. None of these adjustments alone supplies a causal design.{{cite:anderson2003_mva}}

## Check yourself
In [reading a correlation](../questions/ex-da-correlation-reading.qmd), identify the signs without attaching a causal story. Then use [uncorrelated but dependent](../questions/ex-sl-01-3.qmd) to test the zero-correlation limit, and [the effect of correlation](../questions/ex-sl-03-3.qmd) to connect a correlation matrix to principal-component variance.

## History
Francis Galton's 1886 study of hereditary stature compared measurements across related people to investigate regression toward an average. Karl Pearson's 1896 paper on regression, heredity, and panmixia belongs to the subsequent effort to describe such association quantitatively. The available publisher record verifies its date and subject, but it does not justify claiming that this one paper invented the modern sample-correlation formula.{{cite:galton1886,pearson1896}}

Modern treatments distinguish a population correlation from its sample estimate and from a causal interpretation. The NIST reference manual computes the sample coefficient from centred cross-products and describes its linear meaning; multivariate analyses put pairwise coefficients in a correlation matrix, as in the Anderson reference used above. These uses extend the early paired-measurement problem without changing the need to inspect the underlying data.{{cite:nist_correlation2013,anderson2003_mva}}
