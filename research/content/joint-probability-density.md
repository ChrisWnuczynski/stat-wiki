## Lead context
It assigns probability by volume under a surface. A single coordinate still has its own density, obtained by integrating out the others, but that marginal surface does not remember how the coordinates move together.{{cite:durrett2019}}

## Motivating example
Two independent uniform draws on the unit interval fill the unit square evenly, so their joint density is the constant \(1\). A point drawn uniformly from the triangle beneath the diagonal does not: the coordinates are tied together, and the constant density on that triangle is not a product of its marginals. The integral of either surface over a region is the probability of the region. The calculations below use the triangle, where the dependence can be read off the limits.{{cite:durrett2019}}

## Intuition
A joint density is a height, not a probability. The probability of a single point is zero. The probability of a region is the volume underneath the surface. Integrating away one coordinate collapses that volume onto a line and produces the marginal density. Multiplying the marginal densities rebuilds the joint surface only when the coordinates are independent. Otherwise the surface has ridges and empty corners that no pair of separate curves can reproduce.{{cite:durrett2019}}

## Definition
Random variables \(X\) and \(Y\) have a **joint probability density** \(f\) when \(f\) is nonnegative and, for every Borel region \(B\) in the plane,
\[
\mathbb P\bigl((X,Y)\in B\bigr)=\iint_B f(x,y)\,\mathrm dx\,\mathrm dy.
\]
Taking \(B\) to be the whole plane forces the double integral of \(f\) to equal \(1\). The same formula with \(B=A\times\mathbb R\) shows that
\[
f_X(x)=\int_{-\infty}^{\infty} f(x,y)\,\mathrm dy
\]
is a marginal density of \(X\), and likewise for \(Y\). For a nonnegative or integrable function \(g\),
\[
\mathbb E\bigl(g(X,Y)\bigr)=\iint g(x,y)\,f(x,y)\,\mathrm dx\,\mathrm dy,
\]
when the integral exists. A density is determined only up to values on a set of area zero: changing \(f\) at one point does not change any probability.{{cite:durrett2019}}

The definition extends to a vector \((X_1,\ldots,X_n)\) by replacing the double integral with an integral over a region in \(\mathbb R^n\). A random sample from a density \(f_1\) is the case in which the joint density is the product \(\prod_{i=1}^n f_1(x_i)\).{{cite:durrett2019}}

## Interpretation
The height \(f(x,y)\) is not \(\mathbb P(X=x,Y=y)\). It is the concentration of probability per unit area. A tall, narrow peak can contribute the same probability as a low, wide plateau. Units matter: if \(X\) is measured in centimetres and \(Y\) in seconds, \(f\) has units of one over centimetre-seconds, because probability is dimensionless. Changing either unit rescales the density so that areas still integrate to probabilities.{{cite:durrett2019}}

Independence has a density form. If \(f(x,y)=f_X(x)f_Y(y)\) for almost every \((x,y)\), then every rectangle probability factors and \(X\) and \(Y\) are independent. Conversely, when \(X\) and \(Y\) are independent and have marginal densities, the product of those densities is a joint density. The existing exponential example is this case: \(2e^{-x-2y}=e^{-x}\cdot 2e^{-2y}\) on the positive quadrant.{{cite:durrett2019}}

## Properties
The integral of a joint density over the whole plane is \(1\), and integrating out one variable produces a marginal density. If the joint density is a product of the marginals almost everywhere, the coordinates are independent, and then \(\mathbb E(XY)=(\mathbb E X)(\mathbb E Y)\) whenever the expectations exist. For any pair with finite variances, whether or not they are independent,
\[
\operatorname{Cov}(X+Y,X-Y)=\operatorname{Var}(X)-\operatorname{Var}(Y).
\]
Independence is what makes the cross-covariance terms in that expansion vanish in the exponential example already on this page.{{cite:durrett2019}}

A uniform distribution on a region of area \(a\) has joint density \(1/a\) on that region and \(0\) outside it. The marginal densities are not themselves uniform unless the region is a product set. For an invertible linear map \(\mathbf Z=A\mathbf X\) with joint density \(f_{\mathbf X}\), the change-of-variables formula already stated on this page gives \(f_{\mathbf Z}(\mathbf z)=f_{\mathbf X}(A^{-1}\mathbf z)/|\det A|\).

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The definition with \(B=\mathbb R^2\) gives \(\iint f=1\). For a Borel set \(A\subset\mathbb R\),
\[
\mathbb P(X\in A)=\iint_{A\times\mathbb R} f(x,y)\,\mathrm dx\,\mathrm dy=\int_A\Bigl(\int f(x,y)\,\mathrm dy\Bigr)\mathrm dx,
\]
where the inner integral is finite for almost every \(x\) because \(f\) is nonnegative and integrable. Thus \(f_X(x)=\int f(x,y)\,\mathrm dy\) is a marginal density. The formula for \(\mathbb E g(X,Y)\) is the definition applied to the distribution of \((X,Y)\), first for indicators of regions, then for nonnegative simple functions, then for nonnegative measurable \(g\) by monotone convergence.{{cite:durrett2019}}

Suppose \(f(x,y)=f_X(x)f_Y(y)\) almost everywhere. For Borel sets \(C\) and \(D\),
\[
\mathbb P(X\in C,Y\in D)=\int_C f_X(x)\,\mathrm dx\int_D f_Y(y)\,\mathrm dy=\mathbb P(X\in C)\mathbb P(Y\in D).
\]
That is independence. Conversely, if \(X\) and \(Y\) are independent and have marginal densities, the product \(f_X(x)f_Y(y)\) assigns to every rectangle the probability \(\mathbb P(X\in C)\mathbb P(Y\in D)\).{{cite:durrett2019}} The Borel sets on which this product agrees with the joint law form a \(\lambda\)-system: the plane is included, and the collection is closed under proper differences and increasing limits. Finite rectangles form a \(\pi\)-system. Let \(\mathcal L\) be the smallest \(\lambda\)-system containing that \(\pi\)-system \(\mathcal P\). For \(A\in\mathcal P\), the sets \(B\in\mathcal L\) with \(A\cap B\in\mathcal L\) form a \(\lambda\)-system containing \(\mathcal P\), hence containing \(\mathcal L\). For \(A\in\mathcal L\), the same collection again contains \(\mathcal P\) and therefore \(\mathcal L\). So \(\mathcal L\) is itself a \(\pi\)-system. A \(\lambda\)-system that is a \(\pi\)-system is a \(\sigma\)-field, because complements come from differences with the whole plane and countable unions follow by disjointification. Thus \(\mathcal L\) is the Borel \(\sigma\)-field, and the product is a joint density.

Expanding the covariance gives
\[
\operatorname{Cov}(X+Y,X-Y)=\operatorname{Var}(X)-\operatorname{Cov}(X,Y)+\operatorname{Cov}(Y,X)-\operatorname{Var}(Y).
\]
The cross terms cancel, which is the identity used by the exponential example. Under independence, \(\operatorname{Cov}(X,Y)=0\) as well, because \(\mathbb E(XY)-(\mathbb E X)(\mathbb E Y)=0\) follows from writing the product expectation as an iterated integral of \(xy f_X(x)f_Y(y)\).{{cite:durrett2019}}

For the linear map, the transformation rule already stated on this page has Jacobian matrix \(A^{-1}\) and determinant \(1/\det A\). Its absolute value is \(1/|\det A|\), which is the displayed factor.
:::
:::

## Statistical use
A joint density is the sampling model when several continuous measurements are recorded together. Independence is the special case in which the joint density factors and the likelihood is a product. A regression model usually specifies the conditional density of the response given the covariates, then multiplies by a marginal density of the covariates if that marginal is part of the model. Leaving the marginal unspecified is a different joint model: the conditional probabilities are still defined where the marginal density is positive, but probabilities for the covariates are not supplied by the regression alone.{{cite:durrett2019}}

## Worked example
Let \((X,Y)\) be uniform on the triangle \(0<y<x<1\). The triangle has area \(1/2\), so the joint density is \(2\) there and \(0\) elsewhere. The marginals are
\[
f_X(x)=\int_0^x 2\,\mathrm dy=2x, \qquad 0<x<1,
\]
\[
f_Y(y)=\int_y^1 2\,\mathrm dx=2(1-y), \qquad 0<y<1.
\]
Then
\[
\mathbb E X=\int_0^1 x\cdot 2x\,\mathrm dx=\frac23,
\qquad
\mathbb E Y=\int_0^1 2y(1-y)\,\mathrm dy=\frac13,
\]
\[
\mathbb E(XY)=\int_0^1\int_0^x 2xy\,\mathrm dy\,\mathrm dx=\int_0^1 x^3\,\mathrm dx=\frac14.
\]
The covariance is \(1/4-(2/3)(1/3)=1/36\). The product of the marginals is \(4x(1-y)\), which is not equal to the constant \(2\) on the triangle, so \(X\) and \(Y\) are not independent.{{cite:durrett2019}}

The exponential example already on this page can be checked the same way. On \(x>0\), \(y>0\), \(2e^{-x-2y}=e^{-x}\cdot 2e^{-2y}\). These factors are exponential densities with means \(1\) and \(1/2\) and variances \(1\) and \(1/4\). Independence gives \(\mathbb E(XY)=1\cdot 1/2=1/2\), and the covariance identity gives \(\operatorname{Cov}(X+Y,X-Y)=1-1/4=3/4\).{{cite:durrett2019}}

**Your turn.** For the same triangular density, find \(\mathbb P(X>1/2)\) and \(f_Y(1/2)\).

::: {.callout-tip collapse="true" title="Answer"}
\(\mathbb P(X>1/2)=\int_{1/2}^1 2x\,\mathrm dx=1-(1/2)^2=3/4\). The marginal formula gives \(f_Y(1/2)=2(1-1/2)=1\).
:::

## Common misconceptions
A joint density at a point is not the probability of that point. Marginal densities do not determine the joint density: many joints share the same marginals, including the independent product and distributions that put no probability on some rectangles. A constant density on a triangle is uniform on that triangle, but its marginals are not uniform. Factoring the joint density on the support is what independence requires; factoring it only at a few points is not enough. Finally, linearity of expectation does not need a joint density or independence, whereas the product formula for \(\mathbb E(XY)\) does need independence or an equivalent covariance of zero.{{cite:durrett2019}}

## Assumptions and limits
The integral definition uses Borel regions and a nonnegative integrable function. A joint distribution concentrated on a curve, such as \(Y=X\), has no density with respect to area: every region that is a neighbourhood of the diagonal has positive probability while the curve itself has area zero. The marginal formula assumes the integral over the other variable exists, which it does for almost every value when \(f\) is a density. The product criterion is an almost-everywhere statement. The linear transformation formula needs \(A\) invertible. The exponential variances use the rate parameterisation in which the density \(\lambda e^{-\lambda y}\) has variance \(1/\lambda^2\).{{cite:durrett2019}}

## Connections
A [joint probability mass function](joint-probability-mass-function.qmd) is the discrete analogue: probabilities of points replace volumes under a surface. [Independent random variables](independent-random-variables.qmd) are those whose joint density factors into the marginals. A [conditional distribution](conditional-distribution.qmd) divides the joint density by a marginal density where that marginal is positive. The [transformation rule](transformation-rule.qmd) pushes a joint density forward under a smooth change of variables, using the [Jacobian](jacobian.qmd). [Covariance](covariance.qmd) is an integral against the joint density when the second moments exist.{{cite:durrett2019}}

## Check yourself
[A probability as an integral](../questions/ex-prob-region-probability.qmd) asks for the region over which a joint density is integrated. [A product density](../questions/ex-prob-independent-exponentials.qmd) is the exponential calculation checked above. [A point in a triangle](../questions/ex-prob-triangle-conditional.qmd) asks for a conditional density from a joint density.

## History
The integral definition used here is the one in the opened account of a pair with a joint density: the probability of a planar region is the integral of \(f\) over that region. The same pages use that integral to recover a conditional mean by dividing by the marginal integral, which is why a joint density determines conditional calculations where the marginal is positive. Independence is defined there by factorisation of rectangle probabilities. When a joint density exists, that factorisation is equivalent to the joint density being the product of the marginal densities, up to a set of area zero.{{cite:durrett2019}}

The triangle and the unit square show the distinction in numbers. A product of two uniform densities is constant on a rectangle. A constant on a triangle is still a joint density, because the triangle has finite area, but the limits of integration tie the coordinates together and the marginals are triangular rather than flat. The exponential product on this page is the rectangle case: each factor is a density in its own variable, and the covariance calculation separates. No claim is made here about the earliest appearance of the words joint density.{{cite:durrett2019}}
