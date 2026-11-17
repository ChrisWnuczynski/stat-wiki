## Motivating example
A regression coefficient estimated from one sample is a number. Its sampling distribution describes the estimates that would arise if the responses were observed again at the same predictor values. For a Gaussian error model, this distribution and the distribution of the residual sum of squares are available exactly, providing the basis for coefficient intervals and tests.{{cite:openintro2019}} (§8.4, inference for linear regression)

## Statement
Let $Y=X\beta+\varepsilon$, with fixed $n\times p$ matrix $X$ of rank $p<n$ and $\varepsilon\sim N_n(0,\sigma^2I)$, $\sigma^2>0$. Then
$$\hat\beta=(X^\top X)^{-1}X^\top Y\sim N_p\{\beta,\sigma^2(X^\top X)^{-1}\}.$$
With $H=X(X^\top X)^{-1}X^\top$ and $\mathrm{SSE}=\|(I-H)Y\|^2$, one also has $\mathrm{SSE}/\sigma^2\sim\chi^2_{n-p}$, independently of $\hat\beta$. The least-squares formula and residual degrees of freedom match the matrix regression model; the Gaussian transformation argument supplies the exact laws.{{cite:dodge2008}} (p. 365, Multiple Linear Regression)

## Proof
Set $A=(X^\top X)^{-1}X^\top$. Since $AX=I_p$, $\hat\beta-\beta=A\varepsilon$. A linear image of a normal vector is normal, and its covariance is $\sigma^2AA^\top=\sigma^2(X^\top X)^{-1}$. The residual vector is $(I-H)\varepsilon$. Its cross-covariance with the coefficient error is $\sigma^2A(I-H)=0$. Joint normality therefore makes the vectors independent, and applying a measurable function to the residual vector preserves independence from $\hat\beta$.

The symmetric idempotent matrix $I-H$ has rank $n-p$. An orthonormal basis for its image and null space transforms $\varepsilon/\sigma$ into independent standard normal coordinates. Exactly $n-p$ contribute to $\varepsilon^\top(I-H)\varepsilon/\sigma^2$, so this sum of squared coordinates is chi-squared with $n-p$ degrees of freedom. The proof is the same normal projection mechanism that separates a sample mean from its residual variance.

## Key results — Studentise a specified linear contrast
For any nonzero fixed vector $c$, the coefficient contrast has mean $c^\top\beta$ and variance $\sigma^2c^\top(X^\top X)^{-1}c$. Let $s^2=\mathrm{SSE}/(n-p)$. Independence and the normal-over-chi-square construction give
$$\frac{c^\top\hat\beta-c^\top\beta}{s\sqrt{c^\top(X^\top X)^{-1}c}}\sim t_{n-p}.$$
This includes an individual coefficient and any preselected linear combination. Simultaneous coverage for many chosen contrasts requires an additional multiple-comparison construction; individual Student intervals do not automatically have their nominal joint coverage.{{cite:openintro2019}} (§8.4, coefficient inference){{cite:dodge2008}} (p. 526, Student ratio construction)

## Worked example
### A centred five-point regression
Take an intercept and predictors $x=(-2,-1,0,1,2)$. Then $X^\top X=\operatorname{diag}(5,10)$ and $(X^\top X)^{-1}=\operatorname{diag}(0.2,0.1)$. At error variance $\sigma^2=4$, the intercept and slope variances are $0.800$ and $0.400$, with zero covariance. Normality makes these two coefficient estimators independent in this centred design.

For hypothetical observed responses $y=(0,1,1,3,5)$, the fitted coefficients are $\hat\beta_0=2.000$ and $\hat\beta_1=1.200$. Residuals are $(0.4,0.2,-1, -0.2,0.6)$, giving $\mathrm{SSE}=1.600$ and $s^2=0.533333$. The slope standard error is $0.230940$, and its statistic against a zero slope is $5.196152$ on three degrees of freedom. The residual degrees of freedom are five minus two, rather than five minus one.{{cite:nist_ls_straight2002}} (§4.4.3.1, fitted coefficients and residual standard deviation)

**Your turn.** If $\sigma$ doubles while this design stays fixed, what happens to the covariance matrix of the coefficient estimator?

::: {.callout-tip collapse="true" title="Answer"}
Its covariance is multiplied by four, because it is proportional to $\sigma^2$. Each coefficient's sampling standard deviation doubles.
:::

## Statistical use — Match a contrast to the design and response scale
The fitted covariance matrix describes how the chosen design translates response noise into coefficient uncertainty. A contrast vector should be specified in the same coefficient order as the design columns. If the response is rescaled by a factor $a$, the coefficient estimates and their standard errors scale by $a$ in magnitude, while a test of a correspondingly rescaled contrast has the same Student statistic. Correlated coefficient estimates must be combined using the full covariance matrix when assessing a sum or difference.{{cite:nist_ls_straight2002}} (§4.4.3.1, least-squares model and parameter uncertainty)

## Common misconceptions — A sampling law does not randomise the parameter
The displayed normal law varies $Y$ while $\beta$, $\sigma$ and $X$ are fixed. A Bayesian posterior varies parameter values conditional on observed data and a prior; a similar-looking normal expression does not make those two conditionings interchangeable. If predictors are random, the fixed-design result can still be used conditionally when the stated error model holds given the observed predictors.{{cite:openintro2019}} (§8.4, repeated-sampling interpretation)

Non-normal zero-mean errors with covariance $\sigma^2 I$ preserve the coefficient mean and the covariance $\sigma^2(X^\top X)^{-1}$. The exact chi-squared law of $\mathrm{SSE}/\sigma^2$ and its independence from $\hat\beta$ are the further Gaussian conclusions. Unequal variances $\operatorname{Var}(\varepsilon)=\Omega$ replace the coefficient covariance by $A\Omega A^\top$. Least squares remains computable in all of these cases. The Student reference derived from the normal projection is tied to the Gaussian equal-variance model.

## Intuition — The design fixes the covariance before any response is seen
For the centred predictors $x=(-2,-1,0,1,2)$, $X^\top X=\operatorname{diag}(5,10)$ and the coefficient covariance at $\sigma^2=4$ is $\operatorname{diag}(0.800,0.400)$. The intercept and slope are independent because the cross term is zero and the errors are Gaussian. The sum of the two coefficients then has variance $0.800+0.400=1.200$ and standard deviation $\sqrt{1.200}=1.095445$. A contrast $c=(1,-1)$ has variance $0.800+0.400=1.200$ as well, since the covariance term is zero; a nonzero covariance would have contributed $-2c_0c_1\operatorname{Cov}(\hat\beta_0,\hat\beta_1)$. These variances are properties of $X$ and $\sigma^2$. They can be computed before $Y$ is observed. The realised estimates $\hat\beta_0=2.000$ and $\hat\beta_1=1.200$ for $y=(0,1,1,3,5)$ are one draw from that distribution, and the residual calculation $s^2=0.533333$ estimates $\sigma^2$ from the three directions orthogonal to the two-column design.{{cite:nist_ls_straight2002}} (§4.4.3.1, fitted coefficients and residual standard deviation)

The Student pivot divides a centred contrast by $s$ times the design factor. For the slope, the design factor is $\sqrt{0.1}=0.316228$ when $\sigma=1$, and with $s=\sqrt{0.533333}=0.730297$ the standard error is $0.230940$, matching the worked statistic $1.200/0.230940=5.196152$ on $3$ degrees of freedom. Doubling $\sigma$ multiplies every coefficient variance by four and every coefficient standard deviation by two, which is the content of the covariance formula's proportionality to $\sigma^2$.

## Related concepts
The simple-regression formulas are the case $p=2$. Centring the predictor diagonalises $X^\top X$ and makes the intercept the fitted mean at the predictor average, with variance $\sigma^2/n$. The multivariate normal calculation that turns a linear image $A\varepsilon$ into a normal vector with covariance $\sigma^2 AA^\top$ is the same calculation that gives $\hat\beta$ its law. The residual chi-squared law is the count of unit eigenvalues of $I-H$, here $5-2=3$. Hotelling's statistic and the single-coefficient $t$ statistic are later uses of this normal-plus-independent-scatter structure, one for a vector of means and one for a one-dimensional contrast.{{cite:dodge2008}} (p. 526, Student ratio construction)
