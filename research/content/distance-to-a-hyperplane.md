## Lead context
Normalising a linear score separates the geometry of a boundary from the arbitrary scale of its coefficients.

## Motivating example
A classifier labels a measurement vector by the sign of a linear score. Multiplying every coefficient by ten leaves every label unchanged, yet makes every score ten times larger. To assess how close a measurement is to changing sides, the quantity needed is distance measured in input coordinates. The shortest displacement runs perpendicular to the boundary.{{cite:treil2026_linear_algebra}} (§5.3, Thm. 5.3.2)

## Definition — Projection onto an affine boundary
For a nonzero normal vector $w\in\mathbb R^p$ and a scalar $b$, write
$$
H=\{z:w^\top z+b=0\},\qquad s(x)=w^\top x+b.
$$
The normal direction is $w/\|w\|$. The signed distance and the ordinary distance are respectively
$$
d_s(x,H)=\frac{s(x)}{\|w\|},\qquad d(x,H)=\frac{|s(x)|}{\|w\|}.
$$
The sign records the orientation chosen by $w$; ordinary distance is nonnegative. The closest point is
$$
x_\perp=x-\frac{s(x)}{w^\top w}w.
$$
It satisfies the boundary equation, and $x-x_\perp$ is normal to every direction within the hyperplane.{{cite:treil2026_linear_algebra}} (§5.3, Def. 5.3.1 and Props. 5.3.3) Hyperplanes are affine sets, so translating the coordinate system reduces the projection problem to projection onto a subspace.{{cite:boyd_vandenberghe2004}} (§2.2.1, pp. 27–28)

## Properties — Why the perpendicular displacement is shortest
For any $z\in H$, the vectors $x-x_\perp$ and $x_\perp-z$ are perpendicular. Pythagoras gives
$$
\|x-z\|^2=\|x-x_\perp\|^2+\|x_\perp-z\|^2.
$$
The second term is nonnegative and is zero exactly when $z=x_\perp$. This proves both minimality and uniqueness of the projection.{{cite:treil2026_linear_algebra}} (§5.3, Thm. 5.3.2)

The planes $w^\top x+b=c_1$ and $w^\top x+b=c_2$ are $|c_2-c_1|/\|w\|$ apart. In the usual support-vector normalisation, the two supporting planes have scores $-1$ and $1$, giving total margin $2/\|w\|$. Maximising this distance is equivalent to minimising the squared norm subject to the class constraints.{{cite:cortes_vapnik1995}} (§2.1, pp. 277–279)

Scaling $(w,b)$ by a positive factor leaves both distances unchanged. A negative factor reverses the signed distance and preserves ordinary distance. Changing the units of individual coordinates has a different effect: Euclidean distance depends on the chosen metric, so feature scaling is part of the geometry rather than a harmless rescaling of the boundary equation.{{cite:treil2026_linear_algebra}} (§5.1.1, norm and inner product)

## Worked example
Let $w=(3,4)^\top$, $b=-5$ and $x=(2,3)^\top$. Then $s(x)=13$ and $\|w\|=5$. The signed and ordinary distances are both $13/5=2.6$. The projection is
$$
x_\perp=(2,3)^\top-\frac{13}{25}(3,4)^\top=(11/25,23/25)^\top.
$$
Substitution gives $3(11/25)+4(23/25)-5=0$. The displacement has length $2.6$, while moving horizontally to the line would generally require a larger displacement.

**Your turn.** For the same line, find the signed distance of the origin and the distance between the score planes $s(x)=-1$ and $s(x)=1$.

::: {.callout-tip collapse="true" title="Answer"}
At the origin the score is $-5$, so the signed distance is $-1$ and ordinary distance is $1$. The two score planes are $2/5=0.4$ apart.
:::
