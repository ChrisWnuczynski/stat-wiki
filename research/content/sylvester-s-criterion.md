## Lead context
Strict positive definiteness can be checked by a sequence of nested determinants without calculating every eigenvalue.

## Motivating example
A proposed covariance matrix must give positive variance to every nonzero linear combination if it is to be nonsingular. Inspecting its diagonal alone checks only individual variables. Sylvester's criterion tests all directions indirectly, using determinants of successively larger leading blocks.{{cite:treil2026_linear_algebra}} (§7.4.1, Thm. 7.4.2)

## Definition — Leading principal minors
For a real symmetric matrix $A\in\mathbb R^{p\times p}$, let $A_k$ be its upper-left $k\times k$ submatrix. Its leading principal minors are $\Delta_k=\det A_k$. Sylvester's criterion states
$$
A\succ0\quad\Longleftrightarrow\quad\Delta_k>0\quad\text{for all }k=1,\ldots,p.
$$
Symmetry is essential: the quadratic form of a nonsymmetric matrix depends only on its symmetric part, while the determinants of that matrix also depend on its antisymmetric part.{{cite:treil2026_linear_algebra}} (§7.1.2 and §7.4.1)

A principal submatrix uses the same index set for its rows and columns. A leading principal submatrix uses the first $k$ indices in a fixed order. Positive semidefiniteness has a different determinant criterion: all principal minors must be nonnegative. Merely replacing strict inequalities by weak ones in the leading-minor test fails. The eigenvalue and quadratic-form characterisations make the distinction explicit.{{cite:boyd_vandenberghe2004}} (§A.5.2, p. 647)

## Properties — Elimination and positive pivots
The criterion has a useful inductive proof. Partition a leading block as
$$
A_k=\begin{pmatrix}A_{k-1}&v\\v^\top&a\end{pmatrix}.
$$
If $A_{k-1}\succ0$, its Schur complement is $s=a-v^\top A_{k-1}^{-1}v$, and
$$
\det A_k=\det A_{k-1}\,s.
$$
Completing the square gives
$$
\begin{pmatrix}x\\t\end{pmatrix}^{\!\top}A_k
\begin{pmatrix}x\\t\end{pmatrix}
=(x+tA_{k-1}^{-1}v)^\top A_{k-1}(x+tA_{k-1}^{-1}v)+st^2.
$$
Positive successive minors make $s>0$, proving positivity by induction from $A_1$. Conversely, restricting a positive quadratic form to its first $k$ coordinates makes every $A_k$ positive definite, so its eigenvalues and determinant are positive.{{cite:boyd_vandenberghe2004}} (§A.5.5, pp. 650–651){{cite:treil2026_linear_algebra}} (§7.4.1, proof of Thm. 7.4.2)

The semidefinite criterion follows by adding a small diagonal. If all principal minors of $A$ are nonnegative, every leading principal determinant of $A+\varepsilon I$ is a polynomial in $\varepsilon$ whose coefficients are sums of principal minors of the corresponding block, with leading coefficient one. Thus it is positive for $\varepsilon>0$, and the strict criterion gives $A+\varepsilon I\succ0$. Letting $\varepsilon$ decrease to zero gives $x^\top Ax\ge0$ for every $x$. Conversely, each principal submatrix of a semidefinite matrix is semidefinite, so its eigenvalues and determinant are nonnegative.{{cite:boyd_vandenberghe2004}} (§A.5.2, p. 647, quadratic forms and eigenvalues)

## Worked example
Consider
$$
A=\begin{pmatrix}2&1&0\\1&2&1\\0&1&2\end{pmatrix}.
$$
The leading determinants are $\Delta_1=2$, $\Delta_2=3$ and $\Delta_3=4$. All are positive. The successive elimination pivots are $2$, $3/2$ and $4/3$, each a ratio $\Delta_k/\Delta_{k-1}$ with $\Delta_0=1$. The eigenvalues $2-\sqrt2$, $2$ and $2+\sqrt2$ provide an independent check.

Now take $B=\operatorname{diag}(0,-1)$. Its leading minors are both zero, but $(0,1)B(0,1)^\top=-1$. This is a counterexample to a leading-minor test for semidefiniteness. Its nonleading principal minor $-1$ detects the problem.

**Your turn.** Does $C=\operatorname{diag}(-1,-1)$ pass a test based only on a positive full determinant? Is it positive definite?

::: {.callout-tip collapse="true" title="Answer"}
Its determinant is $1$, but its first leading minor is $-1$. The quadratic form is $-x_1^2-x_2^2$, so every nonzero vector has a negative value. A positive determinant alone does not establish positive definiteness.
:::

## Interpretation — What a covariance check establishes
If $A$ is a covariance matrix, $c^\top Ac$ is the variance of $c^\top X$. A zero variance for a nonzero direction is compatible with positive semidefiniteness but makes the covariance singular. Strict positive definiteness excludes those exact linear dependencies. In numerical work, nearly zero pivots also signal sensitivity to rounding; exact sign criteria and floating-point decisions require different tolerances.{{cite:boyd_vandenberghe2004}} (§A.5.2, definiteness and matrix inequalities)

