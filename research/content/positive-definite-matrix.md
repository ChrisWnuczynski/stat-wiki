## Lead context
This condition guarantees that a quadratic expression has strictly positive curvature in every direction. In statistics it distinguishes a nonsingular covariance matrix from one with a zero-variance linear combination, and it permits inverses and Cholesky factorisation in multivariate calculations.{{cite:anderson2003_mva,golub_vanloan2013}}

## Motivating example
Two measurements can each vary while their difference never does: if the second always equals the first, their covariance matrix is singular. A calculation requiring its inverse cannot proceed as if the two measurements supplied independent directions of variation. Checking positive definiteness detects this problem before fitting a multivariate normal model or solving a weighted least-squares system.{{cite:anderson2003_mva,golub_vanloan2013}}

## Intuition
For a real symmetric matrix $A$, the expression $\mathbf a^\top A\mathbf a$ assigns a number to each direction $\mathbf a$. Positive definiteness says that every nonzero direction receives a positive number. Positive *semi*-definiteness permits some directions to receive zero. A covariance matrix gives this expression the concrete meaning of the variance of a linear combination. A zero value then identifies a combination with no random spread.{{cite:anderson2003_mva}}

## Definition
Let $A$ be a real symmetric $d\times d$ matrix and $\mathbf a$ a real column vector of length $d$. The matrix is **positive definite** when $\mathbf a^\top A\mathbf a>0$ for every $\mathbf a\ne\mathbf0$; it is **positive semi-definite** when the same quadratic form is nonnegative for every $\mathbf a$. The superscript $\top$ means transpose. Symmetry is part of both definitions here, so an unsymmetric matrix is not classified by testing its quadratic form alone.{{cite:golub_vanloan2013}}

For a random vector $\mathbf X$ with finite second moments, its covariance matrix $\Sigma=\operatorname{Cov}(\mathbf X)$ is symmetric and positive semi-definite. It is positive definite exactly when every nonzero linear combination $\mathbf a^\top\mathbf X$ has positive variance. This is stronger than requiring each coordinate to have positive variance: two individually variable coordinates can be perfectly dependent.{{cite:anderson2003_mva}}

## Properties
A real symmetric matrix is positive definite exactly when all its eigenvalues are positive, or when all its *leading principal minors* are positive. A leading principal minor is the determinant of the upper-left $k\times k$ block for $k=1,\ldots,d$; the latter test is [Sylvester's criterion](sylvester-s-criterion.qmd). Positive semi-definiteness instead corresponds to nonnegative eigenvalues or nonnegative determinants of *every* principal submatrix, not merely the leading blocks. These tests give exact algebraic ways to distinguish strict from weak positivity.{{cite:sylvester1852,golub_vanloan2013}}

Positive definiteness implies invertibility, and the inverse is again symmetric positive definite. It also gives a unique lower-triangular [Cholesky factor](cholesky-decomposition.qmd) $L$ with positive diagonal and $A=LL^\top$. A semi-definite covariance may lack an inverse and a strictly positive Cholesky diagonal, even though it remains a valid covariance matrix.{{cite:golub_vanloan2013,anderson2003_mva}}

If $A$ is positive semi-definite and $\tau>0$, then $A+\tau I$ is positive definite, where $I$ is the identity matrix and $\tau$ is the chosen diagonal adjustment. This is the algebra behind adding a positive diagonal term to a singular Gram or covariance matrix before a computation that requires an inverse. The added term changes the matrix and must be reported as part of the model or numerical method.{{cite:golub_vanloan2013}}

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The spectral theorem writes a real symmetric $A$ as $Q\operatorname{diag}(\lambda_1,\ldots,\lambda_d)Q^\top$, where $Q$ is orthogonal and the $\lambda_j$ are its eigenvalues. Set $\mathbf b=Q^\top\mathbf a$; then $\mathbf a^\top A\mathbf a=\sum_j\lambda_j b_j^2$. Taking $\mathbf b$ along each coordinate proves the eigenvalue criteria in both directions. Positive eigenvalues also give $A^{-1}=Q\operatorname{diag}(1/\lambda_j)Q^\top$ positive definite. For semi-definite $A$, $\mathbf a^\top(A+\tau I)\mathbf a=\mathbf a^\top A\mathbf a+\tau\|\mathbf a\|^2>0$ when $\mathbf a\ne0$.{{cite:golub_vanloan2013}}

Each leading block of a positive-definite matrix is positive definite by extending a vector with zeros, so its determinant, the product of its positive eigenvalues, is positive. Conversely, proceed by induction on block size. Let $B$ be the upper-left $(d-1)\times(d-1)$ block, $\mathbf b$ the final off-diagonal column, and $c$ the last diagonal entry, so $A=\begin{pmatrix}B&\mathbf b\\\mathbf b^\top&c\end{pmatrix}$. If $B$ is positive definite and $A$ has positive determinant, its Schur complement $s=c-\mathbf b^\top B^{-1}\mathbf b=\det(A)/\det(B)$ is positive. For a vector with first block $\mathbf u$ and last entry $t$, completing the square gives $\begin{pmatrix}\mathbf u\\t\end{pmatrix}^\top A\begin{pmatrix}\mathbf u\\t\end{pmatrix}=(\mathbf u+B^{-1}\mathbf b t)^\top B(\mathbf u+B^{-1}\mathbf b t)+s t^2>0$ for every nonzero pair. This proves the strict Sylvester test.{{cite:sylvester1852,golub_vanloan2013}}

For semi-definite $A$, every principal submatrix is semi-definite by the same zero-extension argument, so all its eigenvalues and determinant are nonnegative. Conversely, if every principal minor is nonnegative, every leading minor of $A+\tau I$ is strictly positive for $\tau>0$: expanding the determinant in $\tau$ gives sums of principal minors plus the positive highest-power term. Sylvester's strict test makes $A+\tau I$ positive definite. Letting $\tau\downarrow0$ gives $\mathbf a^\top A\mathbf a\ge0$ for every vector.{{cite:golub_vanloan2013}}

For a covariance matrix, $\mathbf a^\top\Sigma\mathbf a=\mathbb E\{[\mathbf a^\top(\mathbf X-\boldsymbol\mu)]^2\}=\operatorname{Var}(\mathbf a^\top\mathbf X)\ge0$, where $\boldsymbol\mu=\mathbb E\mathbf X$. Equality occurs exactly when that centred linear combination is zero almost surely. The positive Cholesky factorisation follows recursively from the same positive Schur complements used in Sylvester's induction, choosing positive square roots on the diagonal; these choices also make the factor unique.{{cite:anderson2003_mva,golub_vanloan2013}}

For the Gram-matrix relationship below, put its generating column vectors into a matrix $V$. Then $K=V^\top V$ and $\mathbf a^\top K\mathbf a=\|V\mathbf a\|^2\ge0$. This is strictly positive for every nonzero $\mathbf a$ exactly when the columns of $V$ are linearly independent.{{cite:golub_vanloan2013}}
:::
:::

## Statistical use
Before inverting a covariance estimate for a Mahalanobis distance or a Gaussian density, inspect its symmetry, rank, and eigenvalues or attempt a Cholesky factorisation. A failure can indicate redundant variables, too few observations for the dimension, or an invalid proposed correlation pattern. A positive-definite *population* covariance is an assumption of a nonsingular multivariate-normal density; a sample covariance can be singular even when the population covariance is positive definite, especially when dimension is large relative to sample size.{{cite:anderson2003_mva,golub_vanloan2013}}

## Worked example
Consider $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$. Its leading principal minors are $2$ and $\det A=3$, both positive; its eigenvalues are $1$ and $3$. Directly, for $\mathbf a=(u,v)^\top$, $\mathbf a^\top A\mathbf a=2u^2+2uv+2v^2=(u+v)^2+u^2+v^2>0$ unless $u=v=0$. This can be a covariance matrix: two variables each have variance $2$ and covariance $1$, hence correlation $1/2$.{{cite:anderson2003_mva,golub_vanloan2013}}

**Your turn.** Can $B=\begin{pmatrix}1&2\\2&1\end{pmatrix}$ be a covariance matrix? Check a determinant and one direction.

::: {.callout-tip collapse="true" title="Answer"}
No. Its determinant is $1-4=-3<0$, and for $\mathbf a=(1,-1)^\top$ the quadratic form is $\mathbf a^\top B\mathbf a=-2$. A variance cannot be negative. The diagonal entries being positive and the matrix being symmetric were insufficient.
:::

## Common misconceptions
Symmetry does not imply positive definiteness; the challenge matrix is symmetric and indefinite. Nonnegative diagonal entries do not certify a covariance matrix. For the semi-definite case, checking only leading principal minors is insufficient: $\operatorname{diag}(0,-1)$ has leading minors $0$ and $0$ but has a negative quadratic form in its second coordinate. A singular covariance matrix can still describe a legitimate, degenerate random vector; it simply cannot be inserted into formulas that require an ordinary inverse or a full-dimensional normal density.{{cite:anderson2003_mva,golub_vanloan2013}}

## Assumptions and limits
The eigenvalue and minor tests here apply to *real symmetric* matrices. Covariance matrices require finite second moments for their entries to be defined. Numerical eigenvalues close to zero can be sensitive to rounding, so a floating-point Cholesky or eigenvalue check should be interpreted with the scale and tolerance recorded. Adding $\tau I$ repairs strict positivity algebraically but changes estimated variances and often the implied statistical model.{{cite:golub_vanloan2013,anderson2003_mva}}

## Connections
A [covariance matrix](mean-vector-and-covariance-matrix.qmd) is always positive semi-definite, with strict positivity when no nonzero linear combination has zero variance. [Sylvester's criterion](sylvester-s-criterion.qmd) checks strict positivity through leading determinants. [Cholesky decomposition](cholesky-decomposition.qmd) factors a positive-definite matrix for sampling and solving linear systems. A [Gram matrix](gram-matrix.qmd) is semi-definite because its quadratic form is a squared vector norm; it is definite when its generating vectors are linearly independent.{{cite:anderson2003_mva,golub_vanloan2013}}

## Check yourself
[Why a covariance is positive semi-definite](../questions/ex-sl-01-1.qmd) applies the quadratic form to an impossible proposed correlation matrix. [A Gram matrix](../questions/ex-sl-17-5.qmd) uses principal minors to test a kernel matrix. [Whitening and its limits](../questions/ex-sl-02-7.qmd) asks when the inverse needed for whitening exists.

## History
In an 1852 paper on homogeneous quadratic polynomials, James Joseph Sylvester studied their reduction by real orthogonal substitutions to sums of positive and negative squares. The paper discusses the real roots of the associated determinant equation and the invariant counts of positive and negative terms. These are the quadratic-form and eigenvalue ideas behind distinguishing definite, semi-definite, and indefinite matrices.{{cite:sylvester1852}}

The determinant test bearing Sylvester's name connects those quadratic forms to leading principal minors. In modern multivariate statistics the same tests decide whether a proposed covariance can support an ordinary normal density. Modern numerical linear algebra also exploits strict positive definiteness to obtain a stable Cholesky factorisation for solving systems. The original paper is cited for its quadratic-form analysis, and the modern matrix reference for the computational consequences.{{cite:sylvester1852,anderson2003_mva,golub_vanloan2013}}
