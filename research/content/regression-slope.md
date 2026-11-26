## Lead context
The regression slope is the change in the fitted mean response when the explanatory variable increases by one unit.

## Motivating example
The points $(1,1)$, $(2,2)$ and $(4,6)$ have $\overline x=7/3$ and $\overline Y=3$. Fitting a [least-squares line](least-squares-line.qmd) gives vertical slope $12/7\approx 1.714$ for $Y$ on $x$, whereas regressing $x$ on $Y$ gives slope $4/7\approx 0.571$ rather than the reciprocal $7/12\approx 0.583$.{{cite:shalizi2025_truth_regression}} (Ch. 1, §1.1, pp. 15–17; Ch. 10, §§10.3–10.4, pp. 180, 183)

## Intuition — The least-squares line trades off the two directions
In the conditional mean line $\E(Y\mid x)=\beta_0+\beta_1 x$, the parameter $\beta_1$ is the expected difference in $Y$ per unit increase in $x$. Least squares estimates $(\beta_0,\beta_1)$ by minimising the sum of squared *vertical* deviations in $Y$, whereas regressing $x$ on $Y$ minimises squared *horizontal* deviations in $x$; because the two criteria penalise errors along perpendicular axes, their slopes are not reciprocals unless every point lies on a single non-horizontal, non-vertical line.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Why "Least Squares"?){{cite:shalizi2025_truth_regression}} (Ch. 10, §§10.3–10.4, pp. 180, 183)

## Definition — The ratio of centred products
For pairs $(x_i,Y_i)$ with $i=1,\ldots,n$, write $S_{xx}=\sum_i(x_i-\overline x)^2$ and $S_{xY}=\sum_i(x_i-\overline x)(Y_i-\overline Y)$. Whenever $S_{xx}>0$, the least-squares slope and intercept are
$$
\widehat\beta_1=\frac{S_{xY}}{S_{xx}},\qquad\widehat\beta_0=\overline Y-\widehat\beta_1\overline x.
$$
If every $x_i$ is equal, $S_{xx}=0$ and the sample contains no variation in $x$ from which to define a slope. The estimator remains a linear least-squares slope when $x$ is replaced by a known transform such as $\log x$, because $(\beta_0,\beta_1)$ still enter linearly.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Definition of a Linear Least Squares Model and Examples of Linear Functions){{cite:james_islr2013}} (Ch. 3, §3.1.1, pp. 61–63, eq. 3.4)

## Properties — One normal equation
Substituting the mean-matching intercept $\beta_0=\overline Y-\beta_1\overline x$ reduces the two-parameter objective to a single normal equation $S_{xY}-\widehat\beta_1 S_{xx}=0$ in the slope alone. Because $\sum_i(x_i-\overline x)=0$, $\widehat\beta_1=\sum_i(x_i-\overline x)Y_i/S_{xx}$ is linear in the responses and unchanged by adding a constant to every $Y_i$. Under $\E(Y_i\mid x_i)=\beta_0+\beta_1 x_i$ at fixed $x_i$ with $S_{xx}>0$, [least-squares estimators are unbiased](least-squares-estimators-are-unbiased.qmd) ($\E(\widehat\beta_1)=\beta_1$), and uncorrelated equal-variance errors give $\operatorname{Var}(\widehat\beta_1)=\sigma^2/S_{xx}$.{{cite:james_islr2013}} (Ch. 3, §3.1.2, pp. 65–66, eq. 3.8){{cite:shalizi2025_truth_regression}} (Ch. 4, §4.1, pp. 51–52)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The residual sum of squares is $\sum_i(Y_i-\beta_0-\beta_1 x_i)^2$. For a fixed slope, the minimising intercept is $\beta_0=\overline Y-\beta_1\overline x$, so the residuals are the centred values $(Y_i-\overline Y)-\beta_1(x_i-\overline x)$. Differentiating the sum of their squares with respect to $\beta_1$ and setting the derivative to zero gives $-2S_{xY}+2\beta_1 S_{xx}=0$, hence $\widehat\beta_1=S_{xY}/S_{xx}$ when $S_{xx}>0$.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Why "Least Squares"?){{cite:james_islr2013}} (Ch. 3, §3.1.1, p. 62, eq. 3.4)
:::
:::

## Worked example
The points $(1,1)$, $(2,2)$ and $(4,6)$ have means $\overline x=7/3$ and $\overline Y=3$. Then $S_{xx}=14/3$ and $S_{xY}=8$, so
$$
\widehat\beta_1=\frac{8}{14/3}=\frac{12}{7}\approx 1.714,\qquad\widehat\beta_0=3-\frac{12}{7}\cdot\frac{7}{3}=-1.
$$
The fitted line is $\widehat Y=-1+(12/7)x$. The sum of squared $Y$-deviations is $S_{YY}=14$, so the slope of $x$ on $Y$ is $S_{xY}/S_{YY}=8/14=4/7\approx 0.571$. The reciprocal of $12/7$ is $7/12\approx 0.583$, which is not $4/7$.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Why "Least Squares"?)

**Your turn.** For the same points, predict $\widehat Y$ at $x=3$, and say why a fit with every $x_i$ equal to $3$ would not have a slope.

::: {.callout-tip collapse="true" title="Answer"}
The prediction is $-1+(12/7)\cdot 3=29/7\approx 4.143$. If every $x_i$ equals $3$, then $S_{xx}=0$ and the ratio that defines the slope is undefined.
:::

## Common misconceptions
Inverting a deterministic line $y=\beta_0+\beta_1 x$ gives slope $1/\beta_1$, which creates the misconception that the least-squares slope $\widehat\gamma_1=S_{xY}/S_{YY}$ of $x$ on $Y$ equals $1/\widehat\beta_1$. When $S_{xx}>0$ and $S_{YY}>0$, multiplying the two centred-product ratios gives
$$
\widehat\beta_1\widehat\gamma_1=\frac{S_{xY}}{S_{xx}}\cdot\frac{S_{xY}}{S_{YY}}=\frac{S_{xY}^2}{S_{xx}S_{YY}}=r^2\le 1
$$
by the Cauchy–Schwarz inequality, where $r$ is the sample correlation. For $S_{xY}\neq 0$, $\widehat\gamma_1=r^2/\widehat\beta_1$ equals $1/\widehat\beta_1$ if and only if $r^2=1$—that is, when all points lie strictly on one non-horizontal, non-vertical line. On $(1,1)$, $(2,2)$ and $(4,6)$, $r^2=8^2/((14/3)\cdot 14)=48/49<1$, so $\widehat\gamma_1=(48/49)(7/12)=4/7\approx 0.571$ is strictly smaller in magnitude than $7/12\approx 0.583$.{{cite:shalizi2025_truth_regression}} (Ch. 10, §§10.3–10.4, pp. 180, 183)

A regression slope is neither dimensionless nor inherently causal. Because $\widehat\beta_1=r\sqrt{S_{YY}/S_{xx}}$ carries units of $Y$ per unit of $x$, rescaling $x$ from metres to centimetres divides $\widehat\beta_1$ by $100$ without altering $r$. Moreover, $\widehat\beta_1$ estimates an average difference between observations one unit apart in $x$, not the outcome of physically intervening to change $x$.{{cite:shalizi2025_truth_regression}} (Ch. 3, §3.1, p. 44; Ch. 10, §10.4, p. 183)

## Connections
The slope $\widehat\beta_1$ is the single covariate coefficient in [simple linear regression](simple-linear-regression.qmd) and in the [linear predictor](linear-predictor.qmd) of a straight-line mean. Interchanging response and predictor fits a distinct conditional expectation and exhibits the [regression effect](regression-effect.qmd), pulling predictions toward the mean of whichever variable is treated as the response whenever $|r|<1$. By contrast, a straight-line specification that multiplies two unknown parameters in the slope, such as $\beta_0+\beta_0\beta_1 x$, is nonlinear in the parameters and outside linear least squares.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Nonlinear Model Example){{cite:james_islr2013}} (Ch. 3, §3.1.1, pp. 61–63)
