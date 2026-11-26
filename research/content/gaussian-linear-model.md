## Lead context
A Gaussian linear model gives each response its own mean, linear in known predictors, and says the errors around those means are independent and normal with one common variance.

## Motivating example
Five responses, $0, 0, 1, 3$ and $2$, are recorded at $x=0,1,2,3,4$. Fitting a straight line with an intercept estimates two coefficients and leaves $5-2=3$ residual degrees of freedom. The least-squares slope is $0.7$ and its estimated standard error is $\sqrt{19/300}\approx 0.25166$, so the $t$ ratio on $3$ degrees of freedom is $0.7/\sqrt{19/300}\approx 2.78152$. That estimate exceeds twice its standard error and clears the normal-approximation cutoff $1.96$, yet the two-sided $5\%$ critical value of $t_3$ is $t_{3,0.975}\approx 3.18245$, so the exact $5\%$ test does not reject a zero slope: three residual degrees of freedom still make the reference law heavy-tailed. The Gaussian model is what supplies that exact $t_3$ reference law; without normal errors, the same arithmetic produces a fitted line and does not produce a $t_3$ probability.{{cite:hastie_esl2009}} (§3.2, pp. 46–47, Gaussian errors and the $t$ reference){{cite:shalizi2025_truth_regression}} (Ch. 7, §§7.2–7.3, pp. 122–125)

## Intuition
The linear predictor $X\beta$ represents the systematic part of the response explained by the design columns, and $\varepsilon=Y-X\beta$ is the unobservable error. Calling the model Gaussian specifies independent $N(0,\sigma^2)$ coordinates for $\varepsilon$. [Least squares](least-squares.qmd) itself needs no error distribution: whenever $X$ has full column rank, minimizing $\|Y-Xb\|^2$ returns $\hat\beta=(X^\top X)^{-1}X^\top Y$. Independent Gaussian errors turn $\hat\beta$ into a multivariate normal vector and the residual sum of squares into an independent $\sigma^2\chi^2_{n-p}$ variable, which together justify exact finite-sample Student-$t$ intervals and tests.{{cite:hastie_esl2009}} (§3.2, pp. 45–47, least squares before the Gaussian assumption, then the sampling law){{cite:shalizi2025_truth_regression}} (Ch. 20, §20.3, pp. 347–348)

## Definition
Stack the $n$ responses in $Y$ and the predictors, including a column of ones when an intercept is fitted, as the columns of the $n\times p$ design matrix $X$. The model is
$$
Y=X\beta+\varepsilon,\qquad \varepsilon\sim N(0,\sigma^2 I),
$$
equivalently $Y\mid X\sim N(X\beta,\sigma^2 I)$ with fixed $X$ (treating predictor uncertainty as outside the conditional model). Uncorrelated errors with constant variance $\sigma^2$ already yield $\operatorname{Var}(\hat\beta)=\sigma^2(X^\top X)^{-1}$; Gaussian errors add joint normality of $\hat\beta$ and the independent $\chi^2_{n-p}$ law of $\operatorname{SSE}/\sigma^2$.{{cite:hastie_esl2009}} (§3.2, pp. 46–47, equations (3.8)–(3.11))

In this fixed-design regression setting, **Gaussian linear model** and **[normal linear model](normal-linear-model.qmd)** are synonymous: the [normal linear model](normal-linear-model.qmd) owns the general fixed-design matrix formulation and orthogonal-projection distribution results, while the Gaussian linear model develops their small-sample Student-$t$ inference application.{{cite:shalizi2025_truth_regression}} (Ch. 3, §3.2, p. 44; Ch. 20, §20.3, pp. 347–349)

## Interpretation — What is random
Before the responses are observed, $Y$ is random while $\beta$ and $\sigma^2$ are fixed unknown parameters; once $y$ is observed, $\hat\beta$ is a realised numerical vector. A $t$ confidence level or $p$-value describes the repeated-sampling law of $\hat\beta$ across hypothetical draws of $Y$ at the same $X$ and $(\beta,\sigma^2)$, not a posterior probability for $\beta$ given the single observed sample. Placing a prior distribution on $(\beta,\sigma^2)$ defines a Bayesian regression analysis on top of the same Gaussian likelihood.{{cite:hastie_esl2009}} (§3.2, p. 47, sampling distribution of the least-squares estimator){{cite:shalizi2025_truth_regression}} (Ch. 7, §§7.3–7.4, pp. 124–126)

## Properties — The five-point fit
For $x=(0,1,2,3,4)$ and $y=(0,0,1,3,2)$,
$$
X^\top X=\begin{pmatrix}5&10\\10&30\end{pmatrix},\qquad \det(X^\top X)=50,
$$
with inverse $\begin{pmatrix}0.6&-0.2\\-0.2&0.1\end{pmatrix}$. Multiplying $(X^\top X)^{-1}X^\top y$ gives $\hat\beta=(-0.2,\ 0.7)^\top$. The fitted values are $-0.2$, $0.5$, $1.2$, $1.9$ and $2.6$, the residuals are $0.2$, $-0.5$, $-0.2$, $1.1$ and $-0.6$, and the residual sum of squares is $\operatorname{SSE}=1.9$. Dividing by $5-2=3$ residual degrees of freedom gives $s^2=19/30\approx 0.6333$. Multiplying by the $(2,2)$ entry $0.1$ of $(X^\top X)^{-1}$ gives the estimated slope standard error $\sqrt{(19/30)\times 0.1}=\sqrt{19/300}\approx 0.25166$.{{cite:hastie_esl2009}} (§3.2, p. 46, $\mathrm{Var}(\hat\beta)=\sigma^2(X^\top X)^{-1}$){{cite:sas2012_glm}} (Ch. 4, p. 87, “Estimating the Precision”)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
If $Y\sim N(X\beta,\sigma^2 I)$ and $X$ has full column rank $p$, then $\hat\beta=(X^\top X)^{-1}X^\top Y$ is a linear image of a Gaussian vector, hence multivariate normal with mean $(X^\top X)^{-1}X^\top X\beta=\beta$ and covariance
$$
\sigma^2(X^\top X)^{-1}X^\top X(X^\top X)^{-1}=\sigma^2(X^\top X)^{-1}.
$$
The residual projector $I-H$, with $H=X(X^\top X)^{-1}X^\top$, is symmetric and idempotent of rank $n-p$. Under Gaussian errors, $\operatorname{SSE}/\sigma^2=Y^\top(I-H)Y/\sigma^2$ follows $\chi^2_{n-p}$ independently of $\hat\beta$, so each standardized coordinate $(\hat\beta_j-\beta_j)/(s\sqrt{[(X^\top X)^{-1}]_{jj}})$ follows Student's $t_{n-p}$. In the five-point example, $n-p=3$ and $0.7/\sqrt{19/300}\approx 2.78152$, just short of the $0.975$ quantile $3.18245$ of $t_3$.{{cite:hastie_esl2009}} (§3.2, p. 47, normality, chi-squared residuals, and independence){{cite:shalizi2025_truth_regression}} (Ch. 7, §7.2, pp. 122–123; Ch. 20, §20.3, pp. 347–348)
:::
:::

## Statistical use — When the normal law is doing the work
Invoke the Gaussian model when the inferential target is an exact small-sample interval or test and independent, homoscedastic normal errors are credible. While $\hat\beta$ is defined by least squares alone, the interval $\hat\beta_j\pm t_{n-p,1-\alpha/2}\,s\sqrt{[(X^\top X)^{-1}]_{jj}}$ relies on the $t_{n-p}$ pivot and hence on Gaussian errors. Curvature in a residual plot or spread that changes with the fitted mean invalidates that reference law; adding covariates, transforming $Y$, or adopting a non-Gaussian model addresses different departures and solves different estimation problems.{{cite:hastie_esl2009}} (§3.2, pp. 46–47, assumptions used for tests and intervals){{cite:sas2012_glm}} (Ch. 4, pp. 78, 87, “Regression with the REG and GLM Procedures” and “Estimating the Precision”)

## Worked example
The five-point fit gives $\hat\beta_0=-0.2$, $\hat\beta_1=0.7$, $s^2=19/30\approx 0.6333$, and slope standard error $\sqrt{19/300}\approx 0.25166$. With $t_{3,0.975}\approx 3.18245$, the $95\%$ margin of error is $3.18245\times\sqrt{19/300}\approx 0.8009$, giving the $95\%$ confidence interval $0.7\pm 0.8009=(-0.1009,\ 1.5009)$, which contains $0$. Here $t\approx 2.78152$ exceeds $1.96$ and the estimate $0.7$ exceeds twice its standard error ($2\times 0.25166\approx 0.5033$), so the normal-approximation rule of thumb would reject $H_0:\beta_1=0$. On three residual degrees of freedom, however, $t_3$ has substantially heavier tails than $N(0,1)$, and the exact Gaussian test retains $0$.{{cite:hastie_esl2009}} (§3.2, p. 47, $t$ intervals from the Gaussian sampling law){{cite:shalizi2025_truth_regression}} (Ch. 7, §§7.2–7.4, pp. 122–126)

**Your turn.** Replace the responses by $y=(2,1,2,4,3)$ at the same $x=(0,1,2,3,4)$. The least-squares slope is $0.5$ and the residual sum of squares is $2.7$. Find $s^2$ and the estimated slope standard error, using the same $(X^\top X)^{-1}$ entry $0.1$.

::: {.callout-tip collapse="true" title="Answer"}
The residual degrees of freedom are still $3$, so $s^2=2.7/3=0.9$. The slope standard error is $\sqrt{0.9\times 0.1}=\sqrt{0.09}=0.3$. Because the design matrix $X$ did not change, the $(2,2)$ entry $0.1$ of $(X^\top X)^{-1}$ is unchanged.
:::

## Common misconceptions
Least squares is a fitting criterion, whereas the Gaussian linear model is a probability distribution for $Y\mid X$. A large $R^2$ does not imply Gaussian errors, because $R^2$ compares explained and total sample variation rather than assessing error shape. Nor does including a column of ones treat the predictors as random draws: it is a fixed design column that defines the intercept contrast in $\beta$.{{cite:shalizi2025_truth_regression}} (Ch. 10, §10.3, pp. 180–182; Ch. 20, §§20.1–20.3, pp. 342–348)

## Assumptions and limits — Dependence, unequal variance, and a rank drop
If the errors have mean zero, are uncorrelated, and share variance $\sigma^2$ without being Gaussian, $\hat\beta$ still has mean $\beta$ and covariance $\sigma^2(X^\top X)^{-1}$, yet moment assumptions alone do not guarantee an exact $t$ reference distribution in small samples. Under heteroskedastic covariance $\Sigma\neq\sigma^2 I$, even the covariance formula changes to $(X^\top X)^{-1}X^\top\Sigma X(X^\top X)^{-1}$. In the five-point design the columns $(1,1,1,1,1)$ and $(0,1,2,3,4)$ are not multiples, and the determinant is $50$, so $\hat\beta$ is unique. Appending a duplicate copy of $x$ to form design rows $(1,x_i,x_i)$ drops $X^\top X$ to rank $2$ and makes its determinant $0$, yet only the *individual slopes* $\beta_1$ and $\beta_2$ are aliased—not the intercept $\beta_0$, and not the slope sum $\beta_1+\beta_2$. On $y=(0,0,1,3,2)$, $\widehat\beta_0=-0.2$ and $\widehat{\beta_1+\beta_2}=0.7$ remain uniquely estimable on $5-2=3$ residual degrees of freedom, and under independent Gaussian errors the slope sum still has the exact $t_3$ statistic $0.7/\sqrt{19/300}\approx 2.78152$ against $t_{3,0.975}\approx 3.18245$.{{cite:hastie_esl2009}} (§3.2, pp. 46–47, full rank, constant variance, then Gaussian sampling){{cite:sas2012_glm}} (Ch. 4, pp. 87, 89–92, “Estimating the Precision”, “Models Not of Full Rank”, and “Testing Linear Hypotheses”; Ch. 15, pp. 251–252, 256–257, “Estimability” and “A Multiple Regression Model”)

## Connections
The [normal linear model](normal-linear-model.qmd) develops the general matrix projection and distribution theory for this same Gaussian error law, while [ordinary least squares](ordinary-least-squares.qmd) establishes the algebraic fit. Both the [sampling distribution of the regression estimators](sampling-distribution-of-the-regression-estimators.qmd) and the [sampling distribution of the OLS estimator](sampling-distribution-of-the-ols-estimator.qmd) connect the normal numerator and $\chi^2_{n-p}$ denominator that form [Student's t distribution](student-t-distribution.qmd). Fitted [residuals](error-and-residual.qmd) satisfy $e=y-X\hat\beta$ rather than equalling $\varepsilon$, and a [generalised linear model](generalised-linear-model.qmd) retains $X\beta$ while replacing the Gaussian response distribution and identity link.{{cite:hastie_esl2009}} (§3.2, pp. 45–47){{cite:shalizi2025_truth_regression}} (Ch. 20, §20.3, pp. 347–349)

## Check yourself

### Normal equations {#self-check-ex-inf-normal-equations}

For a four-observation simple linear regression with an intercept, why does a slope of 0.6 with standard error 0.1414 fail to reject at the 5% level?

[Exercise](../questions/ex-inf-normal-equations.qmd)

::: {.callout-tip collapse="true" title="Answer"}
The ratio is $0.6/0.1414=4.243$. The $0.975$ quantile of $t_2$ is 4.3027. Because $4.243<4.3027$, the level-0.05 two-sided test does not reject a zero slope. The comparison uses two residual degrees of freedom. A normal critical value near 1.96 would have rejected, and that is not the Gaussian model's reference law here.
:::

### Normal–inverse-$\chi^2$ regression {#self-check-ex-reg-nichisq}

The sampling model says $\hat\beta$ is normal. What extra ingredient makes a posterior for $\beta$ normal–inverse-chi-squared rather than a sampling distribution?

[Exercise](../questions/ex-reg-nichisq.qmd)

::: {.callout-tip collapse="true" title="Answer"}
A prior distribution on $(\beta,\sigma^2)$. The Gaussian linear model by itself is the distribution of $Y$ given those parameters. Putting a normal–inverse-chi-squared prior on them, and conditioning on $Y$, produces a posterior in the same family. The least-squares fit is the posterior mode or mean only for particular priors. It is not automatically a posterior summary.
:::

## History
Least squares predates the Gaussian sampling model built upon it: minimizing the residual sum of squares requires no probability law, whereas exact normal, chi-squared, and Student-$t$ conclusions arise once independent constant-variance Gaussian errors are posited. In the five-point fit on three residual degrees of freedom, that distinction separates a normal-theory $1.96$ rule of thumb from the heavier-tailed $t_3$ critical value.{{cite:hastie_esl2009}} (§3.2, pp. 45–47){{cite:shalizi2025_truth_regression}} (Ch. 3, §3.2, p. 44; Ch. 7, §7.2, pp. 122–123)
