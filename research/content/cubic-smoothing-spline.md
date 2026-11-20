## Lead context
A cubic smoothing spline is the curve that stays close to the data without spending too much integrated squared curvature.{{cite:hastie_esl2009}} (Ch. 5, §5.4, eq. 5.9, p. 151)

## Motivating example
The three points $(0,0)$, $(1,1)$ and $(2,0)$ have least-squares line $y=1/3$. The slope is zero because the products $(x_i-1)(y_i-1/3)$ sum to zero, and the intercept is the mean response. The residual sum of squares is
$$
2\Bigl(\frac13\Bigr)^{2}+\Bigl(\frac23\Bigr)^{2}=\frac23.
$$

## Intuition — Fit the points, and charge the bends
A curve that passes through every observation can bend as sharply as it likes. A straight line cannot bend at all. Between those extremes, one curve minimises the residual sum of squares plus a penalty $\lambda$ times the integrated square of the second derivative. The residual term rewards a curve that tracks the observations. The penalty rewards a curve whose slope changes slowly. A small $\lambda$ tolerates sharp bends. A large $\lambda$ does not. The minimiser, among functions with two continuous derivatives, is a natural cubic spline with a knot at each distinct observation. The penalty has turned an infinite-dimensional search into a finite set of spline coefficients, shrunk toward the straight line.{{cite:hastie_esl2009}} (Ch. 5, §5.4, pp. 151–152)

## Definition
For observations $(x_i,y_i)$ and a fixed $\lambda\ge 0$, the cubic smoothing spline minimises
$$
\sum_{i=1}^{N}\{y_i-f(x_i)\}^{2}+\lambda\int\{f''(t)\}^{2}\,dt
$$
over functions $f$ with two continuous derivatives. At $\lambda=0$ an interpolating function attains residual sum of squares zero. As $\lambda\to\infty$ the penalty forbids any nonzero second derivative on a set of positive length, and the minimiser becomes the least-squares straight line.{{cite:hastie_esl2009}} (Ch. 5, §5.4, eq. 5.9, p. 151)

## Properties — An infinite penalty leaves the least-squares line
The limiting claim is elementary once the penalty is granted. The identification of the minimiser at finite $\lambda$ as a natural cubic spline is a separate theorem.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
If $f$ is linear, then $f''=0$ and the integral penalty is $0$. The criterion therefore reduces to the residual sum of squares. Among linear functions that sum of squares is minimised by the ordinary least-squares line, say $\ell$. For any nonlinear competitor $g$ and any $\lambda>0$, the criterion of $g$ is at least $\lambda$ times a positive penalty if $g''$ is not almost everywhere zero. Dividing the excess residual of $\ell$ by $\lambda$ shows that once $\lambda$ exceeds that excess divided by the penalty of $g$, the line beats $g$. Sending $\lambda\to\infty$ leaves only functions with $f''=0$, and among them $\ell$ is best.{{cite:hastie_esl2009}} (Ch. 5, §5.4, p. 151)
:::
:::

The finite-$\lambda$ statement, that a unique minimiser exists and is a natural cubic spline with knots at the distinct $x_i$, is the result Hastie, Tibshirani and Friedman record and assign to an exercise.

## Worked example
The quadratic $g(x)=2x-x^{2}$ interpolates the three points, so its residual sum of squares is $0$. Its second derivative is $-2$, and $\int_0^2 4\,dt=8$. The penalised criterion of this quadratic is $8\lambda$. The criterion of the line is $2/3$. They are equal at $\lambda=(2/3)/8=1/12$. For every $\lambda>1/12$ the line beats this particular interpolant. The smoothing spline at that $\lambda$ is whichever smooth function minimises the criterion, and for moderate $\lambda$ it lies between the interpolant and the line. The comparison shows how the penalty can overturn a perfect residual fit.{{cite:hastie_esl2009}} (Ch. 5, §5.4, eq. 5.9, p. 151)

**Your turn.** Use the same three points and the same line. What is the penalised criterion of the line at $\lambda=1$, and why does the value of $\lambda$ not appear in it?

::: {.callout-tip collapse="true" title="Answer"}
The second derivative of $y=1/3$ is $0$, so the penalty term is $0$ for every $\lambda$. The criterion equals the residual sum of squares, $2/3$.
:::

## Connections
A [spline](spline.qmd) is a piecewise polynomial with smooth joins at the [knots](knot.qmd). The cubic smoothing spline places a knot at every distinct $x_i$ and lets $\lambda$ choose the roughness, rather than letting the analyst choose a small knot set in advance. [Cross-validation](cross-validation.qmd), including the generalised approximation to [leave-one-out cross-validation](leave-one-out-cross-validation.qmd), is one way to choose $\lambda$. The fitted values are a linear smoother $S_\lambda y$, and the effective degrees of freedom are $\operatorname{tr}(S_\lambda)$. In the Reinsch form the eigenvalues of $S_\lambda$ are $1/(1+\lambda d_k)$, so each direction that the penalty charges shrinks as $\lambda$ grows.{{cite:hastie_esl2009}} (Ch. 5, §5.4.1, eq. 5.16 and 5.20, pp. 153–154)

## Check yourself
### Where the quadratic loses {#self-check-spline-lambda}

The interpolating quadratic above has penalty integral $8$ and residual sum of squares $0$. For which $\lambda$ is its penalised criterion larger than $2/3$?

::: {.callout-tip collapse="true" title="Answer"}
The quadratic’s criterion is $8\lambda$. This exceeds $2/3$ when $\lambda>1/12$. At $\lambda=1/12$ the two criteria are equal.
:::

### What $\lambda=0$ allows {#self-check-spline-zero}

At $\lambda=0$, why can a function that passes through every observation achieve a criterion of zero, and why is that function not unique without a further restriction?

::: {.callout-tip collapse="true" title="Answer"}
The penalty is switched off, and any interpolant has residual sum of squares zero, hence criterion zero. Many smooth functions pass through the same finite set of points. The natural-cubic-spline selection is a property of the penalised problem at $\lambda>0$, not of the unpenalised residual sum of squares.
:::
