## Motivating example
A response curve can bend in one part of an input range while remaining almost straight elsewhere. A global high-degree polynomial makes every coefficient influence the whole range, whereas a spline joins lower-degree pieces with stated smoothness at a set of knots. This lets a model adapt locally while keeping continuity conditions explicit. A regression spline chooses a finite basis; a smoothing spline chooses a function by trading data fit against roughness.{{cite:rasmussen_williams2006}} (§6.3, spline models, pp. 137–140)

## Definition — Degree and continuity are separate specifications
A cubic spline on an interval is a function that is a polynomial of degree at most three between successive knots and has continuous first and second derivatives at those knots. The function itself is continuous too. The third derivative may jump. A natural cubic spline adds zero second derivative at its boundary knots, producing linear tails when extended outside them. These conditions distinguish a spline from an arbitrary collection of unrelated polynomial pieces.{{cite:reinsch1967}} (§3, equations 5–6, p. 178)

For $M$ distinct interior knots $\xi_1<\cdots<\xi_M$, a truncated power representation is
$$g(x)=\beta_0+\beta_1x+\beta_2x^2+\beta_3x^3+\sum_{m=1}^M\gamma_m(x-\xi_m)_+^3.$$
The notation $(u)_+=\max(u,0)$ makes the basis contribution zero to the left of its knot. There are $M+4$ basis functions before extra boundary restrictions. With two separate fixed boundary knots, imposing the natural conditions removes two independent dimensions, leaving $M+2$. This count treats $M$ as the number of strictly interior knots.{{cite:rasmussen_williams2006}} (§6.3, piecewise-polynomial representation and null space)

## Properties — What the cubic basis guarantees
The value and first two derivatives of $(x-\xi)_+^3$ are zero at $\xi$, whether approached from the left or right. Its third derivative is zero on the left and six on the right. Thus adding $\gamma(x-\xi)_+^3$ changes the third derivative by $6\gamma$ while preserving the three joining conditions. This directly proves the required smoothness of the truncated power representation.

For Gaussian observations, a cubic smoothing spline minimises an objective of the form
$$\sum_i\{y_i-g(x_i)\}^2+\lambda\int\{g''(x)\}^2dx,$$
with $\lambda>0$ and a suitable function space. The curvature penalty is zero for affine functions because their second derivatives vanish. Larger penalties suppress curvature relative to the data-fit term. The minimiser has a natural cubic spline representation, with observed distinct input values supplying the knots.{{cite:rasmussen_williams2006}} (§6.3.1, equation 6.26){{cite:reinsch1967}} (§§2–3, pp. 177–178)

## Worked example — A join that preserves two derivatives
Let $g(x)=x+2(x)_+^3$. To the left of zero, $g(x)=x$; to the right, $g(x)=x+2x^3$. At the join the value is zero, the first derivative is one and the second derivative is zero from both sides. The third derivative jumps from 0 to 12. Values at $-1$, 0 and 1 are $-1$, 0 and 3, respectively.

On the interval $[-1,1]$, the integrated squared curvature is
$$\int_{-1}^1\{g''(x)\}^2dx=\int_0^1(12x)^2dx=48.$$
The straight line $g_0(x)=x$ has penalty zero. A data-fit criterion can prefer the curved function, but it must improve squared error sufficiently to offset the added penalty $48\lambda$. The penalty compares fitted functions through their curvature, rather than through an arbitrary count of nonzero polynomial coefficients.

**Your turn.** Replace the coefficient 2 by 1. What happens to the third-derivative jump and the integrated squared curvature on the same interval?

::: {.callout-tip collapse="true" title="Answer"}
The jump becomes 6. The second derivative on the positive side is 6x, giving integrated squared curvature 36/3=12.
:::

## Statistical use — Basis size and smoothing strength do different jobs
A reduced-basis regression spline specifies a finite set of possible shapes. A penalty then controls how strongly the fit favours smoother shapes within that space. Changing the basis dimension can enlarge the available space, while changing $\lambda$ changes the preference inside it. A small basis cannot interpolate an arbitrary response vector merely because its penalty is made small.{{cite:rasmussen_williams2006}} (§6.3, spline representation and regularisation)

For a fixed Gaussian basis matrix $B$ and penalty matrix $\Omega$, fitted values often have the form $S_\lambda y$ with $S_\lambda=B(B^TB+\lambda\Omega)^{-1}B^T$. The effective degrees of freedom are the trace of that smoothing matrix. They need not equal an integer or the polynomial degree. The null space of a second-derivative penalty consists of constants and straight-line slopes, explaining the two unpenalised directions when both are included.{{cite:rasmussen_williams2006}} (§6.3, null-space discussion and spline smoother)

## Common misconceptions — Smooth joins do not guarantee useful extrapolation
Continuity constraints control what happens at the knots; boundary conditions control the tails. A cubic regression spline without natural boundary restrictions can extrapolate cubically, while a natural spline has linear tails. Neither behaviour establishes that the response relationship continues that way outside the observed range. Knot placement, the penalty, the loss and the intended prediction range all belong to the model specification.{{cite:reinsch1967}} (§3, boundary and continuity conditions)

## Interpretation — Knots and boundary conditions set two different dimensions
A cubic truncated-power basis with three strictly interior knots has dimension $3+4=7$ before boundary restrictions: one column each for the constant, the line, the square and the cube, plus one truncated cube at each interior knot. Natural boundary conditions at two distinct boundary knots remove two free dimensions and leave $3+2=5$. The count changes if a boundary knot is mistakenly included in $M$. The integrated squared second derivative of an affine function $g(x)=4-3x$ is zero on every bounded interval, because $g''$ is identically zero. That function sits in the null space of the roughness penalty whether the basis has five columns or seven. Penalising it does not change it. A cubic term does not sit in that null space.{{cite:rasmussen_williams2006}} (§6.3, piecewise-polynomial representation and null space){{cite:reinsch1967}} (§3, equations 5–6, p. 178)

For $g(x)=x+2(x)_+^3$ the third derivative jumps by $12$ at zero, and the integrated squared curvature on $[-1,1]$ is $48$. Replacing the coefficient $2$ by $1$ multiplies the second derivative on the positive side by $1/2$, multiplies the integrated square by $1/4$, and produces $12$. The jump in the third derivative falls from $12$ to $6$. Curvature penalties therefore scale with the square of the jump coefficient. A fit that reports a small penalty can still have a large third-derivative jump if the jump is confined to a short interval; the integral, not the jump alone, is the quantity in the smoothing objective.{{cite:rasmussen_williams2006}} (§6.3.1, equation 6.26)

### Statistical use — Effective degrees of freedom sit between the null space and the basis size
With a fixed basis matrix $B$ and penalty $\Omega$, the smoother $S_\lambda=B(B^TB+\lambda\Omega)^{-1}B^T$ has trace equal to the effective degrees of freedom. At $\lambda=0$, and with $B$ of full column rank, the trace equals the number of columns. As $\lambda$ grows, the trace falls toward the dimension of the null space of $\Omega$. For a second-derivative penalty that null space is the affine functions, dimension two, provided the basis can represent them. A cubic regression spline with a tiny basis cannot reach an effective dimension larger than its column count, however small $\lambda$ becomes. Choosing $\lambda$ by prediction error, and then quoting that minimum as an unbiased assessment of the selected fit, uses the same observations twice.{{cite:rasmussen_williams2006}} (§6.3, null-space discussion and spline smoother)

## Connections
A [regression tree](regression-tree.qmd) also partitions the input, and its pieces are constants with no smoothness at the cuts. A spline trades that jump for continuous derivatives and a penalty on curvature. Both procedures can [underfit](underfitting.qmd) when the allowed pieces cannot follow the conditional mean, and both can fit training noise when the basis or the leaves are left unrestricted. The effective degrees of freedom are one way to report where a penalised spline sits between those extremes.{{cite:rasmussen_williams2006}} (§6.3, spline representation and regularisation)
