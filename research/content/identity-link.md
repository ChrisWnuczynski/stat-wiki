## Lead context
The identity link leaves the mean on the same scale as the linear predictor, so a coefficient is a change in the mean itself.

## Motivating example
A laboratory records a yield at three settings of a dose, $x=0,1,1$, and obtains $y=1,2,5$. If the mean yield is a straight line in the dose, the slope is how many units of yield the mean gains per unit of dose. No further transformation sits between the line and the mean.

## Intuition — The mean is the line
A link function $g$ connects the mean $\mu$ to a linear predictor $\eta=x^{\mathsf T}\beta$ by $g(\mu)=\eta$. The identity choice is $g(\mu)=\mu$, so $\mu=\eta$. {{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374) In the simple line $\mu=\beta_0+\beta_1 x$, the intercept is the mean at $x=0$ and the slope is the change in the mean for a one-unit change in $x$.

In R’s `gaussian` family the default link is `identity`, and the same link is one of the links the binomial and Gamma families also accept.{{cite:rstats_family2026}} (“gaussian” usage and “link” argument) Choosing it for a binary or positive response does not change the fact that a linear predictor can fall outside $(0,1)$ or below $0$. The identity link is the ordinary match for an unrestricted mean. {{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

## Definition — Normal equations from an identity link
Let $Y_1,\ldots,Y_n$ be independent normal responses with means $\mu_i=x_i^{\mathsf T}\beta$ and common variance $\sigma^2>0$. The log-likelihood, up to a constant free of $\beta$, is
$$
\ell(\beta)=-\frac{1}{2\sigma^2}\sum_{i=1}^n(y_i-x_i^{\mathsf T}\beta)^2.
$$
Differentiating and setting the score to zero gives the normal equations $X^{\mathsf T}(y-X\beta)=0$. The identity link is what puts $\mu_i$ itself, rather than a function of $\mu_i$, into that residual. {{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $r_i=y_i-x_i^{\mathsf T}\beta$. Then $\partial r_i/\partial\beta=-x_i$, so
$$
\frac{\partial\ell}{\partial\beta}=\frac{1}{\sigma^2}\sum_{i=1}^n r_i x_i=\frac{1}{\sigma^2}X^{\mathsf T}(y-X\beta).
$$
The factor $1/\sigma^2$ is positive. The score vanishes if and only if $X^{\mathsf T}(y-X\beta)=0$.
:::
:::

## Worked example
For the three rows $(x,y)=(0,1),(1,2),(1,5)$, with an intercept,
$$
X=\begin{pmatrix}1&0\\1&1\\1&1\end{pmatrix},\qquad y=\begin{pmatrix}1\\2\\5\end{pmatrix}.
$$
Then $X^{\mathsf T}X=\begin{pmatrix}3&2\\2&2\end{pmatrix}$ and $X^{\mathsf T}y=\begin{pmatrix}8\\7\end{pmatrix}$. The determinant is $2$, and
$$
\hat\beta=\begin{pmatrix}1\\2.5\end{pmatrix}.
$$
The fitted means are $1$, $3.5$, and $3.5$. The residuals are $0$, $-1.5$, and $1.5$, and the residual sum of squares is $4.5$. The slope $2.5$ is the change in the fitted mean when $x$ increases by one.

**Your turn.** Fit the same identity-link line to $(x,y)=(0,2),(0,4),(1,6)$. Report $\hat\beta$ and the residual sum of squares.

::: {.callout-tip collapse="true" title="Answer"}
$X^{\mathsf T}X=\begin{pmatrix}3&1\\1&1\end{pmatrix}$ and $X^{\mathsf T}y=\begin{pmatrix}12\\6\end{pmatrix}$, so $\hat\beta=(3,3)^{\mathsf T}$. The fitted values are $3,3,6$ and the residual sum of squares is $1+1+0=2$.
:::

## Connections — Other links keep the mean in range
The [log link](log-link.qmd) and the [logit link](logit-link.qmd) are used when the mean must stay positive or inside $(0,1)$. Their coefficients are multipliers or log odds ratios, not changes in the mean. The [linear predictor](linear-predictor.qmd) is $\eta$ in every case; only the identity link sets $\mu=\eta$. Fitting still uses [iteratively reweighted least squares](newton-raphson-method.qmd) when the variance depends on the mean, and it collapses to one linear solve when the variance is constant and the link is the identity. {{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

