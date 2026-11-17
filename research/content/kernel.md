## Motivating example
Points arranged in an XOR pattern cannot be separated by one straight line in their original two coordinates. A kernel lets a learning algorithm compare those points as though they had first been mapped into a richer feature space. The classifier can then fit a linear boundary in that space while producing a curved boundary in the original coordinates. The choice of kernel determines which similarities the algorithm can use, so it is part of the model rather than a harmless computational shortcut.{{cite:scholkopf_smola2003_intro}} (§§1, 4, 6.1–6.2, pp. 41–54)

## Intuition — Inner products without coordinates
An ordinary dot product measures alignment of two vectors. A feature map $\phi$ changes what counts as alignment: $K(x,z)=\langle\phi(x),\phi(z)\rangle$ computes a dot product after that change. The map can contain polynomial terms, local radial features, or infinitely many coordinates, yet an algorithm may need only the value of $K$. For support-vector machines, the training dual and prediction function use pairwise feature-space dot products, so replacing them by kernel evaluations avoids constructing every feature vector explicitly. It does not avoid choosing a regularisation level or evaluating the resulting model on new data.{{cite:scholkopf_smola2003_intro}} (§§4, 6.1–6.2, pp. 48–55)

## Definition
For real-valued inputs, a valid feature kernel is symmetric and gives a positive-semidefinite Gram matrix $G_{ij}=K(x_i,x_j)$ for *every* finite list of points. The condition means $c^\top Gc\ge0$ for every coefficient vector $c$. A single large similarity, or a nonnegative value for each individual pair, does not establish validity. Conversely, the Gram condition permits a Hilbert-space feature representation even when no short formula for $\phi$ is available. The proof below gives the two directions.{{cite:scholkopf_smola2003_intro}} (§7, pp. 57–60, positive-definite kernels and feature-space construction)

## Interpretation
The quadratic kernel in the example below reveals the mechanism: the single value $(u^\top v)^2$ equals a dot product among squared and cross-product features. The Gaussian radial kernel takes a different route, assigning larger values to nearby points and values near zero to distant ones. Its width parameter changes the scale of “nearby.” Neither kernel is a probability density in the statistical-learning usage here: its integral need not be one, and a valid linear kernel can even have negative values for some distinct inputs.{{cite:scholkopf_smola2003_intro}} (§§6.2, 7–8, pp. 54–61)

## Properties
If $K(x,z)=\langle\phi(x),\phi(z)\rangle$, every finite Gram matrix is positive semidefinite. That condition makes the quadratic form in a support-vector dual well behaved. The converse construction shows that the Gram test characterizes feature kernels; a check of one training matrix alone only tests that finite collection, not all possible future inputs. The inequality $|K(x,z)|^2\le K(x,x)K(z,z)$ follows from any two-point Gram matrix and is another quick diagnostic. Mercer's eigen-expansion requires additional analytic conditions beyond finite-matrix positive semidefiniteness.{{cite:scholkopf_smola2003_intro}} (§7, pp. 57–60, positive-definite kernels and kernel Cauchy–Schwarz inequality){{cite:mercer1909}} (Introduction, p. 415; Part IV)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For the forward direction, if $K(x,z)=\langle\phi(x),\phi(z)\rangle$, then for any finite list $x_1,\ldots,x_n$ and real coefficients $c_i$,
$$
\sum_{i,j}c_ic_jK(x_i,x_j)
=\left\|\sum_i c_i\phi(x_i)\right\|^2\ge0.
$$
The Gram matrix is symmetric because the inner product is symmetric. Conversely, suppose $K$ is symmetric and every finite Gram matrix is positive semidefinite. Form finite formal sums $f=\sum_i c_i e_{x_i}$ and define $\langle f,g\rangle_K=\sum_{i,j}c_i d_jK(x_i,z_j)$ for $g=\sum_jd_je_{z_j}$. The Gram condition makes this a nonnegative semidefinite form. Quotient by its zero-norm vectors and complete the resulting inner-product space. The image $\phi(x)$ of $e_x$ in that space then satisfies $\langle\phi(x),\phi(z)\rangle=K(x,z)$. This construction establishes a feature representation without selecting coordinates for it.{{cite:scholkopf_smola2003_intro}} (§7, pp. 57–60, construction of a feature space)
:::
:::

## Statistical use
A kernel SVM selects a boundary after the kernel and regularisation parameter are chosen. A narrow Gaussian kernel can make distinct training points almost orthogonal, allowing near-perfect training fit while producing poor predictions between observed points. [A tempting wrong turn](../questions/ex-sl-17-7.qmd) asks how to check that failure using held-out data. [Nonlinear separation of XOR](../questions/ex-sl-17-10.qmd) demonstrates why a nonlinear feature map can turn an inseparable input pattern into a separable one. Both questions use feature kernels, unlike the smoothing bump in a kernel density estimator.{{cite:scholkopf_smola2003_intro}} (§§4, 8–9, pp. 48–62)

The function $K(u,v)=-u^\top v$ fails immediately at $u=v=1$, where its one-point Gram matrix is $[-1]$. A sigmoid formula may look like a smooth similarity yet fail the positive-semidefinite requirement for some choices of its parameters and inputs. A Gaussian kernel with an excessively narrow width and weak regularisation can fit isolated training points and generalize poorly. Kernel evaluations also still require computation and storage of a training Gram matrix; “implicit features” do not make an arbitrarily large dataset free to process.{{cite:scholkopf_smola2003_intro}} (§§7–9, pp. 57–62)

## Worked example
Use the Gaussian kernel $K(x,z)=\exp\{-\gamma(x-z)^2\}$ on two inputs $x_1=0$ and $x_2=1$, with $\gamma=\log2$. Since $K(0,0)=K(1,1)=1$ and $K(0,1)=e^{-\log2}=1/2$, the Gram matrix is $G=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}$. Its eigenvalues are $3/2$ and $1/2$, and its determinant is $3/4$; this two-point matrix is positive definite. Increasing $\gamma$ lowers the off-diagonal similarity while leaving the diagonal at one. The calculation illustrates the local geometry, although global kernel validity requires the Gram condition for every finite list.{{cite:scholkopf_smola2003_intro}} (§8, pp. 60–61, Gaussian radial kernel)

**Your turn.** For $K(x,z)=(1+xz)^2$ on the real line, find the Gram matrix for inputs $0$ and $1$, and exhibit a feature map that proves this is a valid kernel for every finite list.

::: {.callout-tip collapse="true" title="Answer"}
The values give $G=\begin{pmatrix}1&1\\1&4\end{pmatrix}$, with determinant $3>0$ and eigenvalues $(5\pm\sqrt{13})/2\approx4.302776,0.697224$. More decisively, $\phi(x)=(1,\sqrt2 x,x^2)$ satisfies $\phi(x)^\top\phi(z)=1+2xz+x^2z^2=(1+xz)^2$. Every finite Gram matrix built from this feature map is positive semidefinite by the proof above; checking only this two-point matrix would not establish that global claim.
:::

## Common misconceptions
A kernel is not simply any function called a similarity: symmetry and all finite Gram matrices matter. Positive semidefinite does not mean every entry is positive; the linear kernel has $K(-1,1)=-1$ but is valid. The kernel trick does not make a nonlinear classifier linear in the original inputs; it makes it linear in feature space. A density-estimation kernel is a normalized smoothing function, and a likelihood kernel is an unnormalized parameter-dependent factor; neither definition alone makes it a feature-space kernel.{{cite:scholkopf_smola2003_intro}} (§§6–8, pp. 53–61)

## Connections
The [kernel trick](kernel-trick.qmd) is the substitution of $K(x,z)$ for a feature dot product in an algorithm. A [Gram matrix](gram-matrix.qmd) collects these pairwise values, and a [kernel support vector machine](kernel-support-vector-machine.qmd) uses them in its margin optimization. A [Gaussian kernel](gaussian-kernel.qmd) and a [polynomial kernel](polynomial-kernel.qmd) encode different geometries. The [kernel density estimator](kernel-density-estimator.qmd) uses the same word for a different mathematical object; its bandwidth controls smoothing rather than feature-space similarity.{{cite:scholkopf_smola2003_intro}} (§§4, 6–8, pp. 48–61)

## History
The term *kernel* came from integral-operator theory, where a two-argument function defines an operator by integration. Feature-space kernels later entered pattern recognition through potential-function methods and support-vector classifiers; the 1992 margin-classifier work used implicit feature comparisons to obtain nonlinear decision boundaries. This history explains why one word now covers related mathematical machinery as well as the separate density-smoothing usage.{{cite:scholkopf_smola2003_intro}} (§§6.2, 7, pp. 54–59, historical discussion and references)
