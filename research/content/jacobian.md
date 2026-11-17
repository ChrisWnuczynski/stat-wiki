## Motivating example
Stretching a square into a larger region cannot create probability. If a random point is uniform on the square, its density must fall as its possible area expands. The Jacobian records the local area or volume change of a smooth transformation, supplying the correction that keeps the transformed density normalized. It is the bridge between a geometric change of coordinates and a probabilistic change of density.{{cite:cambridge_stats1b2016}} (lecture 1, §1.13, pp. 21–22)

## Intuition
In one dimension, doubling every value doubles the length of a small interval, so density on the new scale is halved. In several dimensions, partial derivatives form a matrix describing how small coordinate directions move. Its determinant gives the signed volume scale: a negative sign records reversed orientation, while probability needs only the magnitude. The *inverse* transformation is used when evaluating the new density because a new point must be traced back to its old location. The transformed support matters as much as the multiplier.{{cite:cambridge_stats1b2016}} (lecture 1, §1.13, two-dimensional rule)

## Definition
For a differentiable map $g:\mathbb R^n\to\mathbb R^n$, its **Jacobian matrix** at $x$ is $Dg(x)=[\partial g_i/\partial x_j]_{i,j}$ and its **Jacobian determinant** is $J_g(x)=\det Dg(x)$. Authors sometimes say “the Jacobian” for either object, so the matrix or determinant should be identified from context. Where $g$ is one-to-one with a differentiable inverse and nonzero determinant, the density of $Z=g(X)$ is
$$
f_Z(z)=f_X\bigl(g^{-1}(z)\bigr)\bigl|\det Dg^{-1}(z)\bigr|
$$
on the image of the original support, and zero elsewhere. Equivalently, the multiplier is $1/|\det Dg(x)|$ at $x=g^{-1}(z)$. This is a density rule for equal-dimensional smooth coordinate changes, with almost-everywhere qualifications at harmless exceptional points.{{cite:cambridge_stats1b2016}} (lecture 1, §1.13, pp. 21–22)

## Properties — Direction, scale, and support
The determinant of the forward map measures how old volume expands; the determinant of its inverse measures how much old volume corresponds to a unit of new volume. For $Z=AX+b$ with an invertible matrix $A$, the inverse Jacobian is the constant $|\det A|^{-1}$. The absolute value prevents a reversed orientation from making a negative density. One must still restrict the formula to $A$'s image of the support: a constant multiplier on all of $\mathbb R^n$ would generally fail to integrate to one.{{cite:cambridge_stats1b2016}} (lecture 1, §1.13)

A vanishing determinant needs care. If $A$ is singular, $AX$ lies in a lower-dimensional set and has no density with respect to full-dimensional volume there. A non-injective map needs all inverse branches, not one selected branch. These are different difficulties: one collapses dimension, while the other folds several old points onto one new point.{{cite:cambridge_stats1b2016}} (lecture 1, §1.13, one-to-one condition)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For the linear map in the worked example, $S=X+Y$ and $D=X-Y$, so
$$
\begin{pmatrix}S\\D\end{pmatrix}
=\begin{pmatrix}1&1\\1&-1\end{pmatrix}
\begin{pmatrix}X\\Y\end{pmatrix},\qquad
\begin{pmatrix}X\\Y\end{pmatrix}
=\begin{pmatrix}1/2&1/2\\1/2&-1/2\end{pmatrix}
\begin{pmatrix}S\\D\end{pmatrix}.
$$
The forward determinant is $-2$ and the inverse determinant is $-1/2$, so the inverse absolute factor is $1/2$. The unit square maps to a diamond of area $2$. Thus a uniform original density $1$ becomes density $1/2$ on that diamond and integrates to $(1/2)2=1$. For $0<s<1$, the allowed interval of $d$ is $(-s,s)$, of length $2s$, so $f_S(s)=(1/2)(2s)=s$. For $1<s<2$ the interval is $(s-2,2-s)$, of length $2(2-s)$, giving $f_S(s)=2-s$. Integrating $s$ from zero to one gives $\Pr(S<1)=1/2$.

To see why injectivity is needed, let $X\sim\operatorname{Uniform}(-1,1)$ and $Y=X^2$. For $0<y<1$, the two inverse branches are $x=\sqrt y$ and $x=-\sqrt y$. Each contributes $(1/2)(1/(2\sqrt y))=1/(4\sqrt y)$ to the new density, so $f_Y(y)=1/(2\sqrt y)$. Keeping one branch would integrate to only $1/2$. The smooth bijection rule is the definition above; these calculations establish the linear and two-branch cases.{{cite:cambridge_stats1b2016}} (lecture 1, §1.13, inverse-map rule)
:::
:::

## Statistical use — From a model to another scale
Jacobian factors appear whenever a density is expressed in new coordinates: forming a ratio of random variables, changing a variance to a precision, or turning a parameter probability into log odds. If a prior is declared “flat,” its density is flat only relative to its stated coordinates; transforming it introduces the corresponding Jacobian. In a kernel density estimator, the determinant of a bandwidth matrix keeps each rescaled kernel normalized. These applications all use the same conservation of probability, even though the algebra looks different.{{cite:dodge2008}} (p. 540, “Transformation”, applied motives)

For $Y=X^2$ with $X$ uniform on $(-1,1)$, the two inverse branches each carry probability into $y$, so a one-branch calculation integrates to only $1/2$. For the map $(X,Y)\mapsto(X,X)$, the determinant is zero and all mass lies on a line; no ordinary two-dimensional joint density exists. Even for an invertible linear map, writing the corrected constant density outside the transformed square would assign mass where no point can occur. The hypotheses of injectivity, appropriate dimension, and transformed support have distinct roles.{{cite:cambridge_stats1b2016}} (lecture 1, §1.13, hypotheses)

## Worked example
Let $X$ and $Y$ be independent $\operatorname{Uniform}(0,1)$ variables. Define $S=X+Y$ and $D=X-Y$. The inverse is $X=(S+D)/2$, $Y=(S-D)/2$, and its absolute Jacobian determinant is $1/2$. The joint density of $(S,D)$ is therefore $1/2$ on the diamond where $0<(s+d)/2<1$ and $0<(s-d)/2<1$, and zero outside. The diamond has area $2$, so the density integrates to one. At a sum $s$ between zero and one, the allowable difference runs from $-s$ to $s$, giving $f_S(s)=s$. Above one it runs from $s-2$ to $2-s$, giving $f_S(s)=2-s$. Thus $\Pr(S<1)=\int_0^1s\,ds=1/2$. The inverse determinant sets the *height*, and the transformed support sets the *shape*.{{cite:cambridge_stats1b2016}} (lecture 1, §1.13, analogous two-dimensional calculation)

**Your turn.** Keep $X,Y$ independent $\operatorname{Uniform}(0,1)$, but set $U=2X$ and $V=3Y$. Find the inverse Jacobian factor, the support and joint density of $(U,V)$, and $\Pr(U<1,V<1)$.

::: {.callout-tip collapse="true" title="Answer"}
The inverse map is $(x,y)=(u/2,v/3)$ and has absolute determinant $(1/2)(1/3)=1/6$. The support is $0<u<2$, $0<v<3$, a rectangle of area $6$. The joint density is $1/6$ there and zero elsewhere, so it integrates to $(1/6)6=1$. The event $U<1,V<1$ occupies a unit square inside the rectangle, so its probability is $(1/6)\times1=1/6$.
:::

## Common misconceptions
The Jacobian matrix is not the scalar factor that multiplies a density; that factor is the *absolute determinant* of the inverse matrix. Using the forward determinant instead would double, rather than halve, the density in the worked example. A negative determinant does not mean negative probability; its sign records orientation. Finally, a correct local factor without the transformed support is not a complete density, and a many-to-one map cannot be handled by choosing just one inverse branch.{{cite:cambridge_stats1b2016}} (lecture 1, §1.13)

## Connections
The [transformation rule](transformation-rule.qmd) states the full density formula. A [flat prior](flat-prior.qmd) illustrates its parameterization dependence; the [lognormal distribution](lognormal-distribution.qmd) gets a $1/x$ factor by exponentiating a normal variable. Rescaling a [kernel](kernel.qmd) uses a determinant so its integral remains one. The exponential sum-and-proportion example above shows a nonlinear map where the support and Jacobian together yield a Gamma–Uniform factorization.{{cite:cambridge_stats1b2016}} (lecture 1, §1.13)

## History
Functional determinants appeared before Jacobi: MacTutor identifies an 1815 paper of Cauchy, then Jacobi's 1841 memoir devoted to their properties. The determinant now carries Jacobi's name. In probability and statistics its geometric volume factor became the practical correction for expressing the same distribution in different coordinates, including the transformations used to simplify models and stabilize variance.{{cite:oconnor_robertson2000_jacobi}} (biography, functional-determinant paragraphs){{cite:dodge2008}} (p. 540, “Transformation”)
