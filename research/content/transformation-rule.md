## Motivating example

A measurement can be recorded in metres, then converted to centimetres without changing which objects were measured. The numerical density must change because a one-centimetre interval occupies a different length from a one-metre interval. The transformation rule accounts for that change of scale while keeping the probability of corresponding sets equal. For several measurements transformed together, a determinant replaces the one-dimensional derivative.{{cite:wang2025_foundations}} (Ch. 5, §§6.1, 6.2.4, 6.4.1)

## Statement

The stated formula applies on a region where the map is one-to-one, smooth, and has a smooth inverse with nonzero Jacobian determinant. Its last factor is evaluated at the *new* coordinate; equivalently, divide by the absolute determinant of the forward map at its preimage. The density is zero outside the transformed support. The support condition is as important as the algebraic factor: a formula that integrates over impossible values is not the density of the transformed variable.{{cite:wang2025_foundations}} (Ch. 5, §6.4.1, Jacobian theorem and “Support matters”)

## Intuition

In one dimension, a short interval of width $dx$ around $x$ maps to width approximately $|g'(x)|dx$ around $y=g(x)$. The probability in it is approximately $f_X(x)dx$, so the new density is $f_X(x)/|g'(x)|$. A two-dimensional map can stretch one axis and squeeze another; its determinant measures the net change of area, including any shear. Taking the absolute value discards orientation but keeps area positive. This is why the factor is a determinant rather than a sum of partial derivatives.{{cite:wang2025_foundations}} (Ch. 5, §§6.2.4, 6.4.1)

## Key results

For a scalar monotone differentiable map, $f_Y(y)=f_X(g^{-1}(y))|(g^{-1})'(y)|$ on its image. An affine map $Y=aX+b$ with $a\ne0$ therefore has $f_Y(y)=f_X((y-b)/a)/|a|$. For an invertible matrix $A$, the density of $AX$ is $f_X(A^{-1}y)/|\det A|$. These are the same volume-preservation argument in one and several dimensions. The factor $|a|$ or $|\det A|$ is necessary to make the transformed density integrate to one.{{cite:wang2025_foundations}} (Ch. 5, §§6.2.4–6.2.5, 6.4.1)

If the map is not globally one-to-one but has finitely many smooth inverse branches, add the contributions from all preimages: $f_Y(y)=\sum_{x:g(x)=y}f_X(x)/|g'(x)|$ at regular values. For $Y=X^2$, positive and negative $x$ can lead to the same $y$. Taking only the positive root loses probability. The squared-standard-normal example uses the CDF method, which automatically counts both roots.{{cite:wang2025_foundations}} (Ch. 5, §§6.2.3, 6.2.6, squared-normal example)

## Proof

For a smooth bijection $g$ between the relevant supports, every measurable target set $B$ satisfies $\Pr(g(X)\in B)=\int_{g^{-1}(B)}f_X(x)\,dx$. The multivariable substitution theorem for integrals changes this to $\int_B f_X(g^{-1}(y))|\det Dg^{-1}(y)|\,dy$. Since this holds for all such $B$, the integrand is the density of $g(X)$ almost everywhere. In one dimension, the same argument follows by differentiating $F_X(g^{-1}(y))$ for an increasing map; for a decreasing map, $F_Y(y)=1-F_X(g^{-1}(y))$ at continuity points, producing the absolute derivative. Partitioning a finite-to-one map into disjoint one-to-one branches and adding their probabilities gives the sum-over-preimages formula.{{cite:wang2025_foundations}} (Ch. 5, §§6.2.3–6.2.4, 6.4.1)

## Generalizations — When the formula changes

The theorem concerns densities of equally dimensional random vectors under locally invertible maps. If $X$ has both signs and $Y=X^2$, the inverse is not unique; use both branches or first find $F_Y$. If $Y=(X_1,X_2)\mapsto X_1+X_2$, a two-dimensional input has become one-dimensional; a two-by-two inverse Jacobian does not exist, and convolution or integration over a remaining coordinate is needed. If $Y=0$ for every $X$, the output is a point mass, so it has no ordinary Lebesgue density despite an input density. These cases require a different calculation rather than a determinant mechanically inserted into the stated formula.{{cite:wang2025_foundations}} (Ch. 5, §§6.2.3, 6.4.1, 6.5.1)

## Statistical use

Changing from a positive scale parameter to its logarithm, standardizing a normal vector, and deriving the distribution of a ratio all depend on tracking support and volume. For simulation, the same calculation runs in reverse: transform simple uniform variables and verify that the resulting density is the desired one. The Box–Muller map takes independent uniforms to independent standard normals; another map splits two exponential waiting times into their total and one proportion.{{cite:wang2025_foundations}} (Ch. 5, §§6.2.4, 6.3.5, 6.4.3)

## Worked example

Let $X_1$ and $X_2$ be independent uniform variables on $(0,2)$ and $(0,3)$, and define $Y_1=X_1+X_2$ and $Y_2=X_2$. The inverse is $x_1=y_1-y_2$, $x_2=y_2$. Its Jacobian matrix is $\begin{pmatrix}1&-1\\0&1\end{pmatrix}$, with determinant $1$. The original joint density is $1/(2\cdot3)=1/6$, so $f_Y(y_1,y_2)=1/6$ on the slanted region $0<y_2<3$, $0<y_1-y_2<2$, and zero elsewhere. The unchanged numerical density reflects area-preserving shear, not unchanged support.{{cite:wang2025_foundations}} (Ch. 5, §6.4.1, Jacobian theorem)

For example, $Y_1<1$ corresponds to the triangle $x_1>0$, $x_2>0$, $x_1+x_2<1$ of area $1/2$ inside the original rectangle. Thus $\Pr(Y_1<1)=(1/6)(1/2)=1/12\approx0.08333$. Integrating the transformed density over its triangular section gives the same result. This equality of probabilities is the decisive check on the transformation.{{cite:wang2025_foundations}} (Ch. 5, §§6.2.3, 6.4.1)

**Your turn.** If $X$ is uniform on $(1,3)$ and $Y=4X+5$, find the support and density of $Y$, then calculate $\Pr(Y<13)$.

::: {.callout-tip collapse="true" title="Answer"}
The support is $(9,17)$. The inverse is $x=(y-5)/4$, with derivative $1/4$; multiplying by $f_X=1/2$ gives $f_Y(y)=1/8$ on $(9,17)$ and zero elsewhere. The part below $13$ has length $13-9=4$, so $\Pr(Y<13)=4/8=1/2$. The density is smaller because the support is four times as wide.{{cite:wang2025_foundations}} (Ch. 5, §§6.2.4–6.2.5)
:::

## Common misconceptions

The Jacobian is not evaluated at an arbitrary input point: the forward determinant belongs at $x=g^{-1}(y)$, or the inverse determinant at $y$. A negative determinant does not produce a negative density, because probability uses absolute volume. A correct determinant without the transformed support is still an incomplete density. And a nonlinear map is not automatically a bijection; squaring across zero requires two inverse branches. These are distinct errors of location, orientation, support, and invertibility.{{cite:wang2025_foundations}} (Ch. 5, §§6.2.4, 6.4.1)

## Related concepts

The [Jacobian](jacobian.qmd) describes local volume change. The [CDF](cumulative-distribution-function.qmd) method handles transformations for which inverse branches are awkward. [Convolution](convolution.qmd) integrates over the coordinate that remains when several variables are collapsed to a sum. The [Box–Muller method](box-muller-method.qmd) shows the rule used constructively to simulate a distribution.{{cite:wang2025_foundations}} (Ch. 5, §§6.2.3, 6.4.1, 6.5.1)
