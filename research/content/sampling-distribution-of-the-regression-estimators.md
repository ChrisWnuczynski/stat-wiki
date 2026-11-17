## Motivating example
Two studies can use the same number of observations and have the same residual variation yet estimate a slope with different precision. A design whose predictors cluster near one value gives little information about a change per predictor unit. The sampling distribution shows this directly through $S_{xx}$, rather than attributing all uncertainty to sample size.{{cite:nist_ls_straight2002}} (§4.4.3.1, least-squares coefficients)

## Statement
Suppose $Y_i=\beta_0+\beta_1x_i+\varepsilon_i$ with fixed predictors, $S_{xx}=\sum_i(x_i-\bar x)^2>0$, independent $N(0,\sigma^2)$ errors and $n>2$. Then
$$\operatorname{Var}(\hat\beta_1)=\frac{\sigma^2}{S_{xx}},\quad\operatorname{Var}(\hat\beta_0)=\sigma^2\left(\frac1n+\frac{\bar x^2}{S_{xx}}\right),\quad\operatorname{Cov}(\hat\beta_0,\hat\beta_1)=-\frac{\sigma^2\bar x}{S_{xx}}.$$
Both estimators are jointly normal about their true values. The corrected residual variance $S^2=\mathrm{SSE}/(n-2)$ is independent of the coefficient pair, and $(n-2)S^2/\sigma^2$ is chi-squared with $n-2$ degrees of freedom.{{cite:dodge2008}} (pp. 491–492, normal straight-line model and least squares){{cite:siegrist_multinormal2022}} (“The General Multivariate Normal Distribution”, “Transformations”; normal linear transformations and independence)

## Proof
The slope error is $\hat\beta_1-\beta_1=\sum_i(x_i-\bar x)\varepsilon_i/S_{xx}$. Summing its squared weights gives variance $\sigma^2/S_{xx}$. Its covariance with $\bar\varepsilon$ is zero because the centred predictor weights sum to zero. Normality converts this zero covariance into independence of $\hat\beta_1$ and $\bar Y$. Since $\hat\beta_0-\beta_0=\bar\varepsilon-\bar x(\hat\beta_1-\beta_1)$, the intercept variance and intercept–slope covariance follow by expansion.{{cite:siegrist_multinormal2022}} (“The General Multivariate Normal Distribution”, “Transformations”; affine normal transformations and zero covariance)

Project the normal error vector onto the span of the all-ones vector and the centred predictor vector. These are two orthogonal directions. Its remaining $n-2$ orthonormal coordinates are independent standard normals after division by $\sigma$, and their squared sum is $\mathrm{SSE}/\sigma^2$. The projected coefficient coordinates are independent of that residual vector. This establishes both its chi-square law and the coefficient–residual independence; unbiasedness $E(S^2)=\sigma^2$ follows from the mean of the chi-square law.{{cite:siegrist2022_normals}} (§6.08, orthogonal normal sample decomposition)

## Intuition — Intercept uncertainty depends on the origin
The mean response at the centre, $\beta_0+\beta_1\bar x$, is estimated by $\bar Y$ and has variance $\sigma^2/n$. An intercept at $x=0$ is different when zero lies far from the predictor centre: its uncertainty includes the uncertain slope multiplied by the distance $\bar x$. Recentering the predictor changes the intercept and coefficient covariance while preserving fitted responses at the same scientific predictor values.{{cite:nist_ls_straight2002}} (§4.4.3.1, dependence of intercept and slope)

This is why “the slope and intercept are independent” requires a centred design in the normal model. The slope and response mean are independent for any fixed predictor centre; the uncentred intercept is $\bar Y-\bar x\hat\beta_1$ and shares slope variation. For non-normal errors the same weight calculation gives zero covariance between slope and response mean, but zero covariance alone does not establish independence.

## Worked example
### Move the origin without changing the fit
For $x=1,2,3,4,5$, $\bar x=3$ and $S_{xx}=10$. At $\sigma=2$, the slope variance is $0.400$, the intercept variance is $4.400$, and their covariance is $-1.200$. Their sampling correlation is $-0.904534$. With centred predictor $u=x-3$, the intercept becomes the mean response at $x=3$: its variance is $0.800$ and its covariance with the slope is zero.

Changing instead the design to $x=1,1,3,5,5$ gives $S_{xx}=16$ and slope standard deviation $0.500$, compared with $0.632456$ for the first design. This comparison holds the error standard deviation and sample size fixed. It is a conditional variance comparison; a more spread-out design can introduce different practical costs or model limitations.{{cite:openintro2019}} (§8.4, inference for regression coefficients)

**Your turn.** Keep the first design and double $\sigma$ from two to four. What are the slope standard deviation and the intercept–slope correlation?

::: {.callout-tip collapse="true" title="Answer"}
The slope standard deviation doubles to $1.264911$. All coefficient variances and covariances multiply by four, so the correlation remains $-0.904534$.
:::

## Statistical use — Prediction requires the covariance term
For a mean response at $x_*$, the fitted value is $\hat\beta_0+x_*\hat\beta_1$. Expanding its variance with all three covariance entries gives $\sigma^2\{1/n+(x_*-\bar x)^2/S_{xx}\}$. The intercept–slope covariance is required for this reduction to be invariant under a shift of the predictor origin. The variance is smallest at $x_*=\bar x$, where it equals $\sigma^2/n$, and it grows with the squared distance from the predictor mean.{{cite:nist_ls_straight2002}} (§4.4.3.1, coefficient dependence and derived predictions)

## Key results — Read the three entries on one design
For $x=1,2,3,4,5$, $\bar x=3$, $S_{xx}=10$ and $\sigma=2$, the slope variance is $4/10=0.400$, the uncentred intercept variance is $4(1/5+9/10)=4.400$, and the covariance is $-4\times3/10=-1.200$. The correlation is $-1.200/\sqrt{0.400\times4.400}=-0.904534$. At the centre $x=3$ the fitted-mean variance is $4/5=0.800$. At $x=5$ it is $4\{1/5+(5-3)^2/10\}=4(0.2+0.4)=2.400$. The ratio $2.400/0.800=3$ is the inflation from moving two predictor units away from the centre, in units of the slope information $S_{xx}=10$.

The more spread design $x=1,1,3,5,5$ has $S_{xx}=16$ and slope variance $4/16=0.250$, so the slope standard deviation is $0.500$ against $0.632456$ on the first design. Doubling every centred predictor deviation multiplies $S_{xx}$ by four and divides the slope variance by four, with $n$ and $\sigma$ held fixed. Doubling $\sigma$ from $2$ to $4$ multiplies every variance and covariance by four, doubles the slope standard deviation from $0.632456$ to $1.264911$, and leaves the correlation at $-0.904534$.{{cite:openintro2019}} (§8.4, inference for regression coefficients)

## Common misconceptions
Independence of the slope and the intercept holds in the Gaussian model when the covariance entry is zero, which is the centred design. On $x=1,2,3,4,5$ the covariance is $-1.200$, so the uncentred intercept and the slope are dependent. The slope and the sample mean $\bar Y$ have covariance zero for any fixed centre, because the centred predictor weights sum to zero. Zero covariance becomes independence under joint normality; with non-normal errors the same weights still give zero covariance and leave higher-order dependence possible.

The residual variance $S^2$ is independent of $(\hat\beta_0,\hat\beta_1)$ under the Gaussian model, and $(n-2)S^2/\sigma^2$ is chi-squared on $n-2$ degrees of freedom. Replacing $S$ by $\sigma$ in the slope standard error changes the reference distribution from $t_{n-2}$ to standard normal. The design factor $1/\sqrt{S_{xx}}$ is common to both standard errors. For the five-point design the known-sigma slope standard deviation at $\sigma=2$ is $\sqrt{0.400}=0.632456$, and the $t$ standard error replaces $2$ by the residual estimate $S$ while keeping $\sqrt{S_{xx}}=\sqrt{10}$ in the denominator. A prediction for the mean at $x=5$ has variance $2.400$ when $\sigma=2$, three times the variance $0.800$ at the centre $x=3$. That factor is $1+(5-3)^2/(S_{xx}/n)=1+4/(10/5)=1+4/2=3$, the same inflation written in the equivalent form $1+n(x_*-\bar x)^2/S_{xx}$.{{cite:siegrist2022_normals}} (§6.08, orthogonal normal sample decomposition){{cite:dodge2008}} (pp. 491–492, normal straight-line model and least squares)
