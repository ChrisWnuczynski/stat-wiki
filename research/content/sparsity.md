## Lead context
Sparsity means only a few coefficients are nonzero, and an absolute penalty can set the others to zero exactly.

## Motivating example
A regression with more predictors than observations cannot estimate every coefficient from least squares. If only three of twenty coefficients are truly nonzero, an estimator that is allowed to return exact zeros can name those three. A penalty that only shrinks, and never hits zero, still returns all twenty.

## Intuition — The corner of an absolute constraint
For one coefficient and one observation, the criterion $(y-\beta)^2+\lambda|\beta|$ charges a fixed price $\lambda$ for each unit that $\beta$ moves away from zero. If $|y|$ is smaller than $\lambda/2$, paying that price is not worth a nonzero fit, and the minimiser is $\beta=0$. If $|y|$ is larger, the minimiser moves $y$ toward zero by $\lambda/2$ and stops. The same absolute penalty in two coefficients constrains $|\beta_1|+|\beta_2|$. That set is a diamond. A smooth elliptical contour of the residual sum of squares can meet a diamond at a corner, and a corner sets one coefficient to zero. {{cite:friedman_glmnet2010}} (§2, penalty and coordinate updates) A circular constraint $|\beta_1|^2+|\beta_2|^2\le s$ has no corner, so the meeting point need not make either coefficient zero.

## Definition — Soft threshold for one coefficient
For $\lambda>0$ the minimiser of $(y-\beta)^2+\lambda|\beta|$ is
$$
\hat\beta=
\begin{cases}
y-\lambda/2 & \text{if }y>\lambda/2,\\
0 & \text{if }|y|\le\lambda/2,\\
y+\lambda/2 & \text{if }y<-\lambda/2.
\end{cases}
$$ {{cite:friedman_glmnet2010}} (§2, coordinate descent and soft threshold)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For $\beta>0$ the derivative is $-2(y-\beta)+\lambda$. It vanishes at $\beta=y-\lambda/2$, and that point is positive only when $y>\lambda/2$. For $\beta<0$ the derivative is $-2(y-\beta)-\lambda$, with root $\beta=y+\lambda/2<0$ only when $y<-\lambda/2$. At $\beta=0$ the subgradient of $\lambda|\beta|$ is $[-\lambda,\lambda]$, so zero is a minimiser when $|2y|\le\lambda$, that is $|y|\le\lambda/2$. {{cite:friedman_glmnet2010}} (§2, coordinate-descent thresholding)
:::
:::

## Worked example
Take $\lambda=2$, so the threshold is $1$. Then $y=3$ gives $\hat\beta=3-1=2$, $y=0.4$ gives $\hat\beta=0$, and $y=-4$ gives $\hat\beta=-4+1=-3$. The middle observation is not shrunk to a small nonzero value. It is set to zero.

**Your turn.** With $\lambda=2$ and $y=-0.5$, what is $\hat\beta$? With $y=1$, what is $\hat\beta$?

::: {.callout-tip collapse="true" title="Answer"}
$|-0.5|<1$, so $\hat\beta=0$. And $y=1$ sits on the threshold $|y|=\lambda/2$, so $\hat\beta=0$ as well.
:::

## Connections — Ridge shrinks and does not select
[Ridge regression](ridge-regression.qmd) adds $\lambda\|\beta\|^2$. On the collinear design with rows $(1,1)$ and $(1,1)$, response $(1,3)$, and $\lambda=1$, the ridge coefficients are $(0.8,0.8)$. Neither is zero. The [lasso](lasso.qmd) uses the absolute penalty whose one-dimensional solution is the soft threshold above. A sample covariance from $n=4$ points in $p=6$ dimensions has rank at most $3$, which is why an unpenalised coefficient vector is not uniquely available and a sparse fit is one way to proceed.

## Check yourself

### Rank when $p>n$ {#self-check-ex-sl-18-1}

Four observations lie in six dimensions. What is the maximum rank of the sample covariance, and how many eigenvalues must be zero?


::: {.callout-tip collapse="true" title="Answer"}
The rank is at most $\min(4-1,6)=3$, so at least $6-3=3$ eigenvalues are zero. At most three principal components have positive variance.
:::

### Ridge on a singular design {#self-check-ex-sl-18-2}

For $X$ with both rows equal to $(1,1)$, $y=(1,3)^{\mathsf T}$, and $\lambda=1$, what is the ridge estimate?


::: {.callout-tip collapse="true" title="Answer"}
$X^{\mathsf T}X$ has eigenvalues $4$ and $0$. The ridge estimate is $(0.8,0.8)^{\mathsf T}$. Both coefficients stay nonzero.
:::
