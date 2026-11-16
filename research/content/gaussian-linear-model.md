## Lead context
A Gaussian linear model gives each response its own mean, linear in known predictors, and says the errors around those means are independent and normal with one common variance.

## Motivating example
Four responses, 0, 1, 1 and 2, are recorded at $x=0,1,2,3$. A straight line with an intercept has two coefficients and only two degrees of freedom left for error. The least-squares slope is $0.6$ and its estimated standard error is $\sqrt{1/50}=0.1414$, so the $t$ ratio on 2 degrees of freedom is $3\sqrt{2}=4.243$. The two-sided 5% critical value of $t_2$ is 4.3027. The slope looks large beside its standard error, and it still does not clear a pre-chosen 5% test, because two residual degrees of freedom make the reference law heavy-tailed. The Gaussian model is what names that reference law. Without normal errors the same arithmetic produces a fitted line and does not produce a $t_2$ probability.{{cite:hastie_esl2009}} (§3.2, pp. 46–47, Gaussian errors and the $t$ reference)

## Intuition
The line $X\beta$ is the part of the response the predictors are allowed to explain. Whatever is left is an error. "Gaussian" fixes the distribution of that error: independent coordinates, mean zero, variance $\sigma^2$. Least squares itself does not need that distribution. It only needs a sum of squares to minimise, and it returns $\hat\beta=(X^\top X)^{-1}X^\top Y$ whenever $X$ has full column rank. The normal assumption is what turns $\hat\beta$ into a normal random vector and the residual sum of squares into a chi-squared multiple of $\sigma^2$, independent of $\hat\beta$. Intervals and $t$ tests are statements about those two laws. A fit without them is still a fitted line.{{cite:hastie_esl2009}} (§3.2, pp. 45–47, least squares before the Gaussian assumption, then the sampling law)

## Definition
Stack the responses as $Y$ and the predictors, including a column of ones if there is an intercept, as the rows of $X$. The model is
$$
Y=X\beta+\varepsilon,\qquad \varepsilon\sim N(0,\sigma^2 I).
$$
Equivalently, the coordinates of $\varepsilon$ are independent $N(0,\sigma^2)$, so conditionally on $X$ the response is $N(X\beta,\sigma^2 I)$. The matrix $X$ is treated as fixed. That does not say the predictors were never measured. It says their uncertainty is not part of this model. Hastie, Tibshirani and Friedman write the same equation with an intercept and $p$ further predictors, and they separate two layers: uncorrelated constant-variance errors already give $\mathrm{Var}(\hat\beta)=\sigma^2(X^\top X)^{-1}$, and Gaussian errors add normality of $\hat\beta$ and the chi-squared law of the residual sum of squares.{{cite:hastie_esl2009}} (§3.2, pp. 46–47, equations (3.8)–(3.11))

## Interpretation — What is random
Before the responses are observed, $Y$ is random and $\beta$ and $\sigma^2$ are unknown numbers. After the responses are observed, the realised vector $y$ is fixed and $\hat\beta$ is a computed vector. The $t$ probability is a statement about the random $\hat\beta$ across repeated samples from the same $X$ and the same $\beta$, not a posterior probability for the fixed $\beta$ that produced this one sample. A Bayesian analysis of the same sampling model puts a distribution on $\beta$ and $\sigma^2$ as well. That is a further layer. The Gaussian linear model, as a sampling model, is the distribution of $Y$ given the parameters.{{cite:hastie_esl2009}} (§3.2, p. 47, sampling distribution of the least-squares estimator)

## Properties — The four-point fit
For $x=(0,1,2,3)$ and $y=(0,1,1,2)$,
$$
X^\top X=\begin{pmatrix}4&6\\6&14\end{pmatrix},\qquad \det(X^\top X)=20.
$$
The inverse is $\begin{pmatrix}0.7&-0.3\\-0.3&0.2\end{pmatrix}$. Then $\hat\beta=(0.1,\ 0.6)^\top$. The fitted values are $0.1$, $0.7$, $1.3$ and $1.9$, and the residuals are $-0.1$, $0.3$, $-0.3$ and $0.1$. The residual sum of squares is $0.2$. Dividing by $4-2=2$ gives $s^2=0.1$. The slope variance factor is the $(2,2)$ entry $0.2$, so the estimated slope standard error is $\sqrt{0.1\times0.2}=\sqrt{1/50}=0.1414$.{{cite:hastie_esl2009}} (§3.2, p. 46, $\mathrm{Var}(\hat\beta)=\sigma^2(X^\top X)^{-1}$)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
If $Y\sim N(X\beta,\sigma^2 I)$ and $X$ has full column rank, then $\hat\beta=(X^\top X)^{-1}X^\top Y$ is an affine image of a normal vector, hence normal. Its mean is $(X^\top X)^{-1}X^\top X\beta=\beta$. Its covariance is
$$
\sigma^2(X^\top X)^{-1}X^\top X(X^\top X)^{-1}=\sigma^2(X^\top X)^{-1}.
$$
The residual maker $I-H$, with $H=X(X^\top X)^{-1}X^\top$, is symmetric and idempotent of rank $n-p$, where $p$ is the number of columns of $X$. For Gaussian errors the residual sum of squares divided by $\sigma^2$ is chi-squared on $n-p$ degrees of freedom and independent of $\hat\beta$. The ratio of a coordinate of $\hat\beta-\beta$ to its estimated standard error is therefore Student's $t$ on $n-p$ degrees of freedom. In the four-point example $n-p=2$, and $0.6/\sqrt{1/50}=3\sqrt{2}=4.243$, which is just short of the $0.975$ quantile $4.3027$ of $t_2$.{{cite:hastie_esl2009}} (§3.2, p. 47, normality, chi-squared residuals, and independence)
:::
:::

## Statistical use — When the normal law is doing the work
Use the Gaussian model when the scientific target is a coefficient, an interval, or a test, and the errors can be treated as independent and homoscedastic as well as normal. The point $\hat\beta$ can be reported from least squares either way. The interval $\hat\beta_j\pm t_{n-p,1-\alpha/2}\,s\sqrt{[(X^\top X)^{-1}]_{jj}}$ uses the $t$ law and therefore uses normality. A residual plot that curves, or a spread that grows with the fitted mean, is evidence that this interval's reference law is the wrong one. Transforming $Y$, adding a term, or leaving the Gaussian model for a different family are different responses to that plot. They should not be described as the same fit.{{cite:hastie_esl2009}} (§3.2, pp. 46–47, assumptions used for tests and intervals)

## Worked example
The four-point calculation gives $\hat\beta_0=0.1$, $\hat\beta_1=0.6$, $s^2=0.1$ and a slope standard error $0.1414$. The 95% critical value is $t_{2,0.975}=4.3027$. The margin for the slope is $4.3027\times\sqrt{1/50}=0.6085$, and the interval is $0.6\pm0.6085=(-0.0085,\ 1.2085)$. It contains 0. A rule of thumb that rejects when the estimate exceeds twice its standard error would have rejected, because $2\times0.1414=0.2828$ and $0.6>0.2828$. That rule is a normal approximation. With two residual degrees of freedom the normal approximation is the wrong reference, and the Gaussian model says so through $t_2$.{{cite:hastie_esl2009}} (§3.2, p. 47, $t$ intervals from the Gaussian sampling law)

**Your turn.** Replace the responses by $y=(0,1,3,2)$ at the same $x$. The least-squares slope is $0.8$ and the residual sum of squares is $1.8$. Find $s^2$ and the estimated slope standard error, using the same $(X^\top X)^{-1}$ entry $0.2$.

::: {.callout-tip collapse="true" title="Answer"}
The residual degrees of freedom are still 2, so $s^2=1.8/2=0.9$. The slope standard error is $\sqrt{0.9\times0.2}=\sqrt{0.18}=0.4243$. The residual variance is $0.9/0.1=9$ times the original, and the slope standard error is $\sqrt{9}=3$ times $\sqrt{1/50}$, which equals $0.4243$. The design matrix did not change, so the variance factor $0.2$ did not change.{{cite:hastie_esl2009}} (§3.2, p. 46, the variance factor depends on $X$ and $\sigma^2$, not on $y$)
:::

## Common misconceptions
Least squares is not the same object as the Gaussian linear model. The former is a fitting rule. The latter is a distribution for $Y$. A high $R^2$ is not evidence that the errors are normal. Normality is about the shape of the residuals around the mean, not about how much of the variance the mean explains. And an intercept column of ones does not make the predictors random. It is a fixed column. Dropping it changes which contrasts $\beta$ contains. It does not turn $X$ into a sample from a distribution.

## Assumptions and limits — Dependence, unequal variance, and a rank drop
If the errors are uncorrelated with variance $\sigma^2$ but not normal, $\hat\beta$ still has mean $\beta$ and covariance $\sigma^2(X^\top X)^{-1}$, and it does not have an exact $t$ law in small samples. If the variances differ across rows, that covariance formula is already wrong: the correct covariance is $(X^\top X)^{-1}X^\top\Sigma X(X^\top X)^{-1}$ with a diagonal $\Sigma$ that is not $\sigma^2 I$. If two columns of $X$ are identical, $X^\top X$ is singular and there is no unique $\hat\beta$. In the four-point design the columns $(1,1,1,1)$ and $(0,1,2,3)$ are not multiples, and the determinant is 20, so the fit exists. Adding a second copy of $x$ would make the determinant 0. The Gaussian assumption cannot repair a rank deficiency. There is then no single coefficient whose $t$ ratio one could compute.{{cite:hastie_esl2009}} (§3.2, pp. 46–47, full rank, constant variance, then Gaussian sampling)

## Connections
[Ordinary least squares](ordinary-least-squares.qmd) is the fitting rule. The [sampling distribution of the least-squares estimator](sampling-distribution-of-the-ols-estimator.qmd) is the normal law this model adds. A [residual](error-and-residual.qmd) is $y-X\hat\beta$, not the unobservable $\varepsilon$. [Student's t distribution](student-t-distribution.qmd) is the reference for a coordinate when $\sigma$ is estimated. A [generalised linear model](generalised-linear-model.qmd) keeps a linear predictor and drops the Gaussian assumption on $Y$ itself.{{cite:hastie_esl2009}} (§3.2, pp. 45–47)

## Check yourself

### Normal equations {#self-check-ex-inf-normal-equations}

In the four-point example, why does a slope of 0.6 with standard error 0.1414 fail to reject at the 5% level?

[Question-bank page](../questions/ex-inf-normal-equations.qmd)

::: {.callout-tip collapse="true" title="Answer"}
The ratio is $0.6/0.1414=4.243$. The $0.975$ quantile of $t_2$ is 4.3027. Because $4.243<4.3027$, the level-0.05 two-sided test does not reject a zero slope. The comparison uses two residual degrees of freedom. A normal critical value near 1.96 would have rejected, and that is not the Gaussian model's reference law here.{{cite:hastie_esl2009}} (§3.2, p. 47, $t$ reference)
:::

### Normal–inverse-$\chi^2$ regression {#self-check-ex-reg-nichisq}

The sampling model says $\hat\beta$ is normal. What extra ingredient makes a posterior for $\beta$ normal–inverse-chi-squared rather than a sampling distribution?

[Question-bank page](../questions/ex-reg-nichisq.qmd)

::: {.callout-tip collapse="true" title="Answer"}
A prior distribution on $(\beta,\sigma^2)$. The Gaussian linear model by itself is the distribution of $Y$ given those parameters. Putting a normal–inverse-chi-squared prior on them, and conditioning on $Y$, produces a posterior in the same family. The least-squares fit is the posterior mode or mean only for particular priors. It is not automatically a posterior summary.{{cite:hastie_esl2009}} (§3.2, p. 47, the sampling distribution is the distribution of the estimator, not a posterior)
:::

## History
Least squares is older than the Gaussian sampling model built on top of it. Hastie, Tibshirani and Friedman separate the two steps explicitly: the minimiser of the residual sum of squares is defined without a distribution, and the normal, chi-squared and $t$ statements begin only once the errors are assumed independent and Gaussian with constant variance. The four-point numbers above are that second step, small enough that the difference between a normal critical value and a $t_2$ critical value is visible.{{cite:hastie_esl2009}} (§3.2, pp. 45–47)
