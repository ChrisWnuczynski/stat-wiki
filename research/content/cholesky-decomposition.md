## Motivating example
A multivariate normal simulation needs correlated coordinates, while a Gaussian likelihood needs a log determinant and a quadratic form. One triangular factor performs all three tasks. It avoids explicitly forming an inverse and gives a direct check that a proposed covariance matrix is positive definite.{{cite:rasmussen_williams2006}} (§A.4, pp. 202–203)

## Definition — A triangular covariance factor
A real symmetric positive-definite matrix $A$ has a unique factorisation $A=LL^\top$ with $L$ lower triangular and strictly positive diagonal. The positivity convention removes sign ambiguities. Some implementations use the upper factor $R=L^\top$ and write $A=R^\top R$; the multiplication order is part of the convention.{{cite:boyd_vandenberghe2004}} (§C.3.2, pp. 669–670)

## Properties — Existence by a Schur complement
Partition $A=\begin{pmatrix}a&r^\top\\r&B\end{pmatrix}$, where $a>0$. For every nonzero vector $z$, positive definiteness applied to $(-r^\top z/a,z)^\top$ gives
$$
z^\top(B-rr^\top/a)z>0.
$$
The Schur complement $B-rr^\top/a$ is therefore positive definite. Factor it by induction as $MM^\top$ and set
$$
L=\begin{pmatrix}\sqrt a&0\\r/\sqrt a&M\end{pmatrix}.
$$
Direct multiplication yields $A$. The first diagonal entry and first column are forced by positivity and $LL^\top=A$; induction forces the remainder, proving uniqueness. The resulting recursive algorithm uses
$$
L_{jj}=\sqrt{A_{jj}-\sum_{k<j}L_{jk}^2},\qquad
L_{ij}=\frac{A_{ij}-\sum_{k<j}L_{ik}L_{jk}}{L_{jj}}\quad(i>j).
$$
Positive definiteness guarantees positive quantities inside these square roots in exact arithmetic.{{cite:boyd_vandenberghe2004}} (§C.3.2, Cholesky factorisation)

To solve $Ax=b$, first solve $Lv=b$, then $L^\top x=v$. Also $b^\top A^{-1}b=\|L^{-1}b\|^2$ and $\log\det A=2\sum_j\log L_{jj}$. The same factor can be reused for many right-hand sides. Dense factorisation costs a leading $n^3/3$ arithmetic operations, while each pair of triangular solves has quadratic cost.{{cite:boyd_vandenberghe2004}} (§C.3.2, Algorithm C.2, pp. 669–670){{cite:rasmussen_williams2006}} (§A.4, eq. A.18, pp. 202–203)

## Worked example — Simulation and a quadratic form
For
$$
A=\begin{pmatrix}4&2\\2&3\end{pmatrix},\qquad
L=\begin{pmatrix}2&0\\1&\sqrt2\end{pmatrix},
$$
the determinant is eight and the log determinant is $2.079442$. With $b=(1,2)^\top$, triangular solves give $x=A^{-1}b=(-1/8,3/4)^\top$, hence $b^\top A^{-1}b=11/8=1.375$.

If $Z_1,Z_2$ are independent standard normals, then $(2Z_1,Z_1+\sqrt2Z_2)^\top$ has covariance $A$. Its covariance is $LL^\top$, not $L^2$. A spectral factor $\Gamma\Lambda^{1/2}$ can produce the same covariance without being triangular; covariance factors need not be unique when the triangular positivity conditions are omitted.{{cite:rasmussen_williams2006}} (§A.2, p. 201)

**Your turn.** Find the positive-diagonal lower factor of $\begin{pmatrix}9&3\\3&2\end{pmatrix}$ and its determinant.

::: {.callout-tip collapse="true" title="Answer"}
The factor is $\begin{pmatrix}3&0\\1&1\end{pmatrix}$. The determinant is $(3\cdot1)^2=9$.
:::

## Assumptions and limits — Singular and nearly singular matrices
A positive-semidefinite matrix can describe a valid degenerate covariance, but it need not have a Cholesky factor with strictly positive diagonal. At a zero pivot the ordinary recursion needs modification, such as a rank-revealing factorisation. Adding a positive diagonal term changes the covariance model; in Gaussian simulation it corresponds to extra independent noise. Its size should reflect the modelling or numerical purpose.{{cite:rasmussen_williams2006}} (§A.2, p. 201; §A.4, p. 202)
