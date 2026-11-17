## Motivating example
Suppose a proposed similarity gives self-similarities $K(a,a)=K(b,b)=1$ but cross-similarity $K(a,b)=K(b,a)=2$. All four entries are positive, yet the matrix $\left(\begin{smallmatrix}1&2\\2&1\end{smallmatrix}\right)$ has quadratic form $-2$ at $(1,-1)^T$. It cannot be a Gram matrix of feature vectors. Positivity of individual similarities is much weaker than positive semidefiniteness.{{cite:scholkopf_smola2003_intro}} (§7, defs. 1–3, p. 57)

## Definition
For a real-valued function on $\mathcal X\times\mathcal X$, kernel validity means symmetry together with
$$\sum_{i,j=1}^m c_ic_jK(x_i,x_j)\ge0$$
for every finite list of inputs and every real coefficient vector. Repeated inputs are permitted. Some literature calls this a positive-definite kernel even though the associated matrices may be singular. Strict matrix positive definiteness is a stronger condition.{{cite:rasmussen_williams2006}} (§4.1, p. 80)

A feature map immediately proves validity: if $K(x,z)=\langle\phi(x),\phi(z)\rangle$, the quadratic form is $\|\sum_i c_i\phi(x_i)\|^2$. Conversely, finite-Gram positivity constructs such a representation. Take formal finite linear combinations of symbols $e_x$ and define their bilinear form by $\langle e_x,e_z\rangle=K(x,z)$. Positivity and the quadratic inequality imply Cauchy–Schwarz, so a zero-norm element has zero inner product with every element. Quotient out these zero-norm elements and complete the resulting inner-product space. Mapping $x$ to the class of $e_x$ gives the desired Hilbert-space feature map.{{cite:scholkopf_smola2003_intro}} (§7, pp. 57–60, feature-space construction)

## Properties — Necessary checks and constructive proofs
Every valid kernel has $K(x,x)\ge0$ and
$$|K(x,z)|^2\le K(x,x)K(z,z).$$
The latter follows by requiring every quadratic form of the two-input Gram matrix to be nonnegative; equivalently its determinant is nonnegative. Consequently, a zero diagonal entry forces its entire corresponding row of similarities to vanish. These checks can disprove a proposal quickly, but passing them for pairs alone does not establish positivity for larger sets.{{cite:scholkopf_smola2003_intro}} (§7, prop. 2, p. 58)

Closure operations provide more useful proofs than checking many randomly chosen matrices. Nonnegative weighted sums concatenate scaled feature maps. Products use tensor-product features: if $K_1=\sum_r f_r(x)f_r(z)$ and $K_2=\sum_s g_s(x)g_s(z)$, their product is the sum over $(r,s)$ of $f_rg_s$ products. The same argument extends to Hilbert features. Integer powers follow by repeated products. Negative multiples and arbitrary nonlinear transforms have no comparable general guarantee.{{cite:rasmussen_williams2006}} (§4.2.4, p. 95)

## Worked example — A polynomial and a failed similarity
For scalar inputs, $K(x,z)=(1+xz)^2$ has feature map
$$\phi(x)=(1,\sqrt2x,x^2).$$
Multiplication gives $\phi(x)^T\phi(z)=1+2xz+x^2z^2$. On inputs $-1,0,1$, its Gram matrix is
$$G=\begin{pmatrix}4&1&0\\1&1&1\\0&1&4\end{pmatrix}.$$
Its eigenvalues are $(5-\sqrt{17})/2$, $4$, and $(5+\sqrt{17})/2$, approximately $0.4384,4,4.5616$. The feature identity proves validity on every real input, while the eigenvalues check this particular matrix.{{cite:rasmussen_williams2006}} (§4.2.2, pp. 89–90, polynomial feature maps)

By contrast, $H(x,z)=1-(x-z)^2$ fails on $0,2$, giving matrix $\left(\begin{smallmatrix}1&-3\\-3&1\end{smallmatrix}\right)$. Its quadratic form at $(1,1)^T$ is $-4$. Symmetry and positive diagonal entries do not rescue it.

**Your turn.** Prove that $K(x,z)=f(x)f(z)$ is valid for any real function $f$. Can its Gram matrix on two distinct inputs be singular?

::: {.callout-tip collapse="true" title="Answer"}
The quadratic form is $(\sum_i c_if(x_i))^2\ge0$, and symmetry is immediate. The Gram matrix is $vv^T$, with $v_i=f(x_i)$, so its rank is at most one. A two-input matrix is therefore singular even when the inputs differ.
:::

## Assumptions and limits — A valid function versus one matrix
A successful eigenvalue check on one training set certifies only that matrix. A proof by a feature map or a closure theorem certifies the function throughout its domain. Small negative eigenvalues in numerical work may arise from rounding, but a substantial negative eigenvalue is mathematical evidence against positive semidefiniteness on those inputs. Distinguish these numerical and analytic questions.

Mercer expansions concern an integral operator and require additional assumptions on a domain, measure and regularity. The finite-Gram definition itself needs no Euclidean coordinates, integration measure or compact domain. It therefore applies to strings and other structured objects once their proposed similarities satisfy the same positivity condition.{{cite:rasmussen_williams2006}} (§4.3, pp. 96–97)
