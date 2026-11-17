## Lead context
A Gram matrix stores the inner product of every pair of feature vectors, so a kernel method can work without writing the feature map down.

## Motivating example
Take \(\phi(x)=x\) on the points \((1,0)\), \((0,1)\) and \((1,1)\). The Gram matrix is
\[
K_S=\begin{pmatrix}1&0&1\\0&1&1\\1&1&2\end{pmatrix}.
\]
Its eigenvalues are \(0\), \(1\) and \(3\), all nonnegative, which matches the quadratic-form test. For \(c=(1,-1,1/2)^\top\),
\[
c^\top K_S c=\bigl\|1\cdot(1,0)-1\cdot(0,1)+\tfrac12(1,1)\bigr\|^2=\bigl\|(1.5,-0.5)\bigr\|^2=2.5.
\]

## Intuition — Pairwise products instead of features
Once a map \(\phi\) sends each input to a feature vector, every later formula that needs those features often needs them only through products \(\phi(x_i)^\top\phi(x_j)\). Collecting those products in a matrix means the map itself can stay off the page. The \((i,j)\) entry is large when the two mapped points point the same way, and it is zero when they are orthogonal.{{cite:hastie_esl2009}} (Ch. 12, §12.3, p. 424, Eq. 12.21)

The same matrix appears in a penalised expansion. If the columns of \(H\) are the feature coordinates of the training inputs, then \(HH^\top\) has entries \(K(x_i,x_{i'})\). Predictions depend on that \(N\times N\) matrix, not on a separate inner-product matrix in the big feature space.{{cite:hastie_esl2009}} (Ch. 12, §12.3.7, p. 437, Eq. 12.48)

## Definition — The matrix of kernel values
For inputs \(x_1,\ldots,x_N\) and a kernel \(K(x,x')=\langle\phi(x),\phi(x')\rangle\), the Gram matrix \(K_S\) is the \(N\times N\) matrix with
\[
(K_S)_{ij}=K(x_i,x_j).
\]
A kernel that really is an inner product has to be symmetric, and every finite matrix of this form has to be positive semidefinite.{{cite:hastie_esl2009}} (Ch. 12, §12.3, p. 424)

## Properties — Why every Gram matrix is positive semidefinite
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Symmetry is \(K(x_i,x_j)=\phi(x_i)^\top\phi(x_j)=\phi(x_j)^\top\phi(x_i)\). For any real coefficients \(c_1,\ldots,c_N\),
\[
\sum_{i=1}^N\sum_{j=1}^N c_i c_j K(x_i,x_j)
=\Bigl\|\sum_{i=1}^N c_i\phi(x_i)\Bigr\|^2\ge 0.
\]
The left-hand side is \(c^\top K_S c\), so \(K_S\) is positive semidefinite. The argument uses only the inner-product representation, so it applies to every finite set of inputs.{{cite:hastie_esl2009}} (Ch. 12, §12.3, p. 424, Eq. 12.21)
:::
:::

## Worked example — Three planar points

**Your turn.** On the real line, with \(K(x,x')=xx'\), form the Gram matrix of the inputs \(1\) and \(-1\). Give its eigenvalues, and evaluate \(c^\top K_S c\) at \(c=(1,1)^\top\).

::: {.callout-tip collapse="true" title="Answer"}
The products are \(1\cdot 1=1\), \(1\cdot(-1)=-1\) and \((-1)\cdot(-1)=1\), so
\[
K_S=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
The eigenvalues are \(0\) and \(2\). At \(c=(1,1)^\top\) the quadratic form is \(0\): the two mapped points are scalar multiples, and the coefficients cancel them.
:::

## Connections — Kernels and margin methods
A [kernel](kernel.qmd) is the function whose values fill the Gram matrix. [Positive definite matrices](positive-definite-matrix.qmd) are the stricter case in which \(c^\top K_S c>0\) for every \(c\neq 0\); semidefiniteness allows a zero eigenvalue when the mapped points are linearly dependent. The [soft-margin primal](soft-margin-primal.qmd) and the [hard-margin dual](hard-margin-dual.qmd) replace each feature inner product by a kernel entry, which is why the dual is written entirely in terms of \(K_S\).{{cite:hastie_esl2009}} (Ch. 12, §12.3, pp. 424 and 437)

