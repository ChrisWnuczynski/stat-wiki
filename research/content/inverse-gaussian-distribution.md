## Lead context
The inverse Gaussian distribution is a law on the positive line whose mean and shape can be chosen separately, and whose variance grows like the cube of the mean.

## Motivating example
A positive measurement has mean 2. If it were gamma with variance equal to the square of the mean, the variance would be 4. An inverse Gaussian law with the same mean and shape $\lambda=4$ has variance $\mu^3/\lambda=8/4=2$, half as large. Doubling the mean to 4, with $\lambda$ held at 4, replaces the variance by $64/4=16$, which is eight times 2. The cubic growth is the modelling reason to reach for this family: the spread opens faster than a gamma spread as the mean increases, and the shape parameter is what holds that rate fixed.

## Intuition
The density piles up on $(0,\infty)$ and has a single peak. The parameter $\mu$ is the mean, not a log-scale and not a rate. The parameter $\lambda$ pulls the distribution toward that mean: larger $\lambda$ means smaller variance $\mu^3/\lambda$. At $x=\mu$ the exponential factor equals 1, so the height of the density at the mean is $\sqrt{\lambda/(2\pi\mu^3)}$. For $\mu=2$ and $\lambda=4$ that height is $\sqrt{4/(2\pi\cdot 8)}=\sqrt{1/(4\pi)}=0.2821$. The distribution is not symmetric about the mean. Probability above 3, one unit above the mean, is 0.1756, while the probability below 1, one unit below the mean, is 0.2324. The two tails do not match. A symmetric law around 2 would have matched those two tails.

## Definition
The density on $x>0$, for $\mu>0$ and $\lambda>0$, is
$$
f(x)=\sqrt{\frac{\lambda}{2\pi x^3}}\exp\Bigl(-\frac{\lambda(x-\mu)^2}{2\mu^2 x}\Bigr).
$$
The mean is $\mu$ and the variance is $\mu^3/\lambda$. A useful reparameterisation makes the algebra of scaling obvious. Let $Y$ have the standardised density with a single parameter $\nu>0$,
$$
f_Y(y)=\frac{1}{\sqrt{2\pi y^3}}\exp\Bigl(-\frac{(y-\nu)^2}{2\nu^2 y}\Bigr),
$$
and set $X=\lambda Y$ with $\nu=\mu/\lambda$. Then $X$ has the two-parameter density above, $\E X=\mu$ and $\Var(X)=\mu^3/\lambda$. Feeding $\mu$ in as $\nu$ and leaving the scale at 1 produces the law with $\lambda=1$, whose variance is $\mu^3$, not $\mu^3/\lambda$.

## Properties
The moment generating function $\E e^{tX}=\exp\bigl\{(\lambda/\mu)\bigl[1-\sqrt{1-2\mu^2 t/\lambda}\bigr]\bigr\}$, for $t$ near 0, is the source of the mean and variance. Its logarithm, the cumulant generating function, begins $\mu t+(\mu^3/(2\lambda))t^2$. The first cumulant is the mean $\mu$ and the second is the variance $\mu^3/\lambda$. At fixed $\lambda$, replacing $\mu$ by $2\mu$ multiplies the variance by 8. At fixed $\mu$, replacing $\lambda$ by $2\lambda$ halves the variance and does not move the mean. Those two levers are the reason the family is used when a positive response needs a mean model and a separate dispersion.

For $\mu=2$ and $\lambda=4$ the variance is 2, the density at the mean is 0.2821, the distribution function at the mean is 0.6277, and the survival probability at 3 is 0.1756. The median is therefore below the mean: more than half the probability sits at or below 2, which is the right-skew pattern the cubic variance is accompanying.

## Related distributions
A gamma law with the same mean has variance proportional to the square of the mean, not the cube. Holding a gamma shape fixed and doubling the mean multiplies the gamma variance by 4. The inverse Gaussian calculation above multiplies the variance by 8. The two families can share a log link in a regression and still describe different amounts of noise at a large mean. A normal law is not a limit one should casually substitute: the inverse Gaussian support is positive, and a normal approximation centred at $\mu=2$ with variance 2 still places mass on negative numbers.

## Statistical inference
In a regression the mean is written as a function of predictors, often through a log link so that every finite linear predictor gives a positive mean. The canonical link is not the log link. It is an inverse quadratic function of the mean, and that link stays on the positive reals only when the linear predictor stays in the region where the square root is real. A log link is a choice of mean function. It does not change the variance function $\mu^3/\lambda$. Estimating $\lambda$, or a dispersion multiple in front of $\mu^3$, is a separate step from estimating the regression coefficients. A fit that reports only the coefficients has not said how fast the variance grows.

## Generating random samples
Draw $Y$ from the standardised one-parameter law with $\nu=\mu/\lambda$, then set $X=\lambda Y$. The mean of $Y$ is $\nu$, so the mean of $X$ is $\lambda\nu=\mu$. The variance of $Y$ is $\nu^3$, so the variance of $X$ is $\lambda^2\nu^3=\mu^3/\lambda$. For $\mu=2$ and $\lambda=4$ one draws the standardised law at $\nu=0.5$ and multiplies by 4. Drawing the standardised law at $\nu=2$ and not scaling it produces mean 2 and variance $2^3=8$, which is the $\lambda=1$ member, not the intended distribution.

## Worked example
Take $\mu=2$ and $\lambda=4$. The mean is 2 and the variance is $2^3/4=2$. The standard deviation is $\sqrt{2}=1.4142$. One unit above the mean, at 3, the survival probability is 0.1756. The density at 2 equals 0.2821, and the distribution function at 2 equals 0.6277, so the median is less than 2. Doubling the mean at the same $\lambda$ produces variance $4^3/4=16$.

**Your turn.** For $\mu=4$ and $\lambda=16$, find the mean, the variance, and the density at the mean.

::: {.callout-tip collapse="true" title="Answer"}
The mean is 4 and the variance is $4^3/16=64/16=4$. The density at the mean is $\sqrt{16/(2\pi\cdot 64)}=\sqrt{16/(128\pi)}=\sqrt{1/(8\pi)}=0.1995$. A larger $\lambda$ has pulled the distribution toward the mean: the variance equals the mean, whereas $\mu=4$ and $\lambda=4$ had variance 16.
:::

A second check of the scaling: if a generator is given shape $\nu=4/16=0.25$ and scale 16, the draws have mean 4 and variance 4. If it is given shape 4 and scale 1, the draws have mean 4 and variance 64.

::: {.callout-tip collapse="true" title="Answer"}
Shape 4 and scale 1 is the standardised law with $\nu=4$, mean 4 and variance $4^3=64$. The two-parameter law with $\mu=4$ and $\lambda=16$ is the standardised law at $\nu=4/16=0.25$, multiplied by 16. Its variance is $16^2\times(0.25)^3=256\times0.015625=4$. The two calls share a mean and do not share a variance.
:::

## Common misconceptions
The mean parameter is not the shape parameter of the standardised density. In the map above the standardised shape is $\mu/\lambda$, and the scale is $\lambda$. Swapping them, or ignoring the scale, produces a different member of the family. The variance does not grow like $\mu^2$. That is the gamma pattern. And a density that is highest near the mean does not make the mean, the median and the mode the same number. For $\mu=2$ and $\lambda=4$ the distribution function at the mean is already 0.6277, so the median is smaller than the mean.

## Assumptions and limits — When a positive cubic-variance law is the wrong noise
The support is $x>0$. A zero or a negative observation is not a draw from this density. Independent observations are part of the usual regression sampling model; a shared shock across observations is dependence, and the variance formula $\mu^3/\lambda$ is then the marginal variance of one observation, not the variance of a mean of dependent observations. If the variance grows like the square of the mean rather than the cube, a gamma model matches the mean–variance plot and this one does not. Doubling a fitted mean and watching the residual spread multiply by about 4 points to the square. Multiplication by about 8 points to the cube. A single outlier can imitate either pattern. The variance function is a claim about the whole curve, not about one point.

## Connections
The [gamma distribution](gamma-distribution.qmd) is the other standard positive family, with variance proportional to the square of the mean at fixed shape. A [log link](log-link.qmd) keeps fitted inverse-Gaussian means positive. The [Gaussian linear model](gaussian-linear-model.qmd) is the constant-variance special case people sometimes force onto positive data by transforming first. The inverse Gaussian model leaves the response on the measurement scale and puts the curvature into the variance and the link.

## History
The two-parameter density used here is the form with mean $\mu$ and shape $\lambda$ whose variance is $\mu^3/\lambda$. The cumulant calculation that yields that variance is the one recorded with the distribution's mean and variance. The numerical values above follow from the density and from the mean and variance formulae. Differentiating the cumulant generating function twice at zero recovers $\mu$ and $\mu^3/\lambda$, which is the check on the cubic variance.
