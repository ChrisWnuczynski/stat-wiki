## Lead context
The regression slope is the change in the fitted mean response when the explanatory variable increases by one unit.

## Intuition — The least-squares line trades off the two directions
In the straight line $\mathbb{E}(Y\mid x)=\beta_0+\beta_1 x$, the slope $\beta_1$ is that change in the mean. The least-squares fit chooses the intercept and slope that minimise the sum of squared vertical deviations. The slope of $x$ on $Y$ minimises the horizontal deviations instead, so the two numbers are not reciprocals of each other unless the points already lie on a line.{{cite:nist_least_squares}} (§4.1.4.1, minimising squared deviations)

## Definition — The ratio of centred products
For points $(x_i,Y_i)$, write $S_{xx}=\sum_i(x_i-\overline x)^2$ and $S_{xY}=\sum_i(x_i-\overline x)(Y_i-\overline Y)$. If $S_{xx}>0$, the least-squares slope and intercept are
$$
\widehat\beta_1=\frac{S_{xY}}{S_{xx}},\qquad\widehat\beta_0=\overline Y-\widehat\beta_1\overline x.
$$
If every $x_i$ is equal, then $S_{xx}=0$ and the points contain no information about a change in $x$. The fit is linear in the parameters even when the line is redrawn against a transformed $x$, such as $\log x$.{{cite:nist_least_squares}} (§4.1.4.1, linear in the parameters)

## Properties — One normal equation
Differentiating the residual sum of squares with respect to the slope, and using an intercept that matches the two means, leaves $S_{xY}-\widehat\beta_1 S_{xx}=0$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The residual sum of squares is $\sum_i(Y_i-\beta_0-\beta_1 x_i)^2$. For a fixed slope, the minimising intercept is $\beta_0=\overline Y-\beta_1\overline x$, so the residuals are the centred values $(Y_i-\overline Y)-\beta_1(x_i-\overline x)$. Differentiating the sum of their squares with respect to $\beta_1$ and setting the derivative to zero gives $-2S_{xY}+2\beta_1 S_{xx}=0$, hence $\widehat\beta_1=S_{xY}/S_{xx}$ when $S_{xx}>0$.{{cite:nist_least_squares}} (§4.1.4.1, the minimisation that produces the parameter estimates)
:::
:::

## Worked example
The points $(1,1)$, $(2,2)$ and $(4,6)$ have means $\overline x=7/3$ and $\overline Y=3$. Then $S_{xx}=14/3$ and $S_{xY}=8$, so
$$
\widehat\beta_1=\frac{8}{14/3}=\frac{12}{7}\approx 1.714,\qquad\widehat\beta_0=3-\frac{12}{7}\cdot\frac{7}{3}=-1.
$$
The fitted line is $\widehat Y=-1+(12/7)x$. The sum of squared $Y$-deviations is $S_{YY}=14$, so the slope of $x$ on $Y$ is $S_{xY}/S_{YY}=8/14=4/7\approx 0.571$. The reciprocal of $12/7$ is $7/12\approx 0.583$, which is not $4/7$.{{cite:nist_least_squares}} (§4.1.4.1, least squares)

**Your turn.** For the same points, predict $\widehat Y$ at $x=3$, and say why a fit with every $x_i$ equal to $3$ would not have a slope.

::: {.callout-tip collapse="true" title="Answer"}
The prediction is $-1+(12/7)\cdot 3=29/7\approx 4.143$. If every $x_i$ equals $3$, then $S_{xx}=0$ and the ratio that defines the slope is undefined.{{cite:nist_least_squares}} (§4.1.4.1)
:::

## Connections
The slope is one coefficient in the [linear predictor](linear-predictor.qmd) of a straight-line mean. Swapping the axes fits a different conditional mean, which is the [regression effect](regression-effect.qmd): each regression is pulled toward the mean of its own response. A model that is linear in $x$ but multiplies two unknown parameters in the slope, such as $\beta_0+\beta_0\beta_1 x$, is not a linear least-squares problem.{{cite:nist_least_squares}} (§4.1.4.1, a product of parameters is nonlinear)

## Check yourself — A perfect line and a zero denominator
**1.** The points $(0,1)$, $(1,3)$ and $(2,5)$ lie on $Y=1+2x$. What least-squares slope does the formula return?

::: {.callout-tip collapse="true" title="Answer"}
The means are $\overline x=1$ and $\overline Y=3$. Then $S_{xx}=2$ and $S_{xY}=4$, so the slope is $4/2=2$ and the intercept is $3-2\cdot 1=1$. The residuals are zero.{{cite:nist_least_squares}} (§4.1.4.1)
:::

**2.** Why can one unusual $Y$ value move $\widehat\beta_1$ by a large amount?

::: {.callout-tip collapse="true" title="Answer"}
The criterion squares vertical deviations, so a point far from the line in the $Y$ direction contributes a large squared term and pulls the slope. The fit has no separate protection against that point.{{cite:nist_least_squares}} (§4.1.4.1, sensitivity to unusual points)
:::
