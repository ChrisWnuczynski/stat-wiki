## Lead context
A polynomial kernel computes the inner product of all monomials up to a chosen degree without writing those monomials down.

## Motivating example
A linear classifier cannot separate the corners of a square when opposite corners share a label. Products of the coordinates can. Expanding two inputs into the constant, the two linear terms, the two squares and the cross term produces a six-dimensional vector, and a linear rule in that vector is a quadratic rule in the original inputs. The kernel evaluates the inner product of two such vectors from the original coordinates alone.{{cite:hastie_esl2009}} (§12.3.1, eq. 12.23, p. 424)

## Intuition — Features in the inner product only
A support-vector classifier needs the feature vectors only through their inner products. If a map $h$ sends the inputs to a higher-dimensional space, every inner product $h(\mathbf{x})^\top h(\mathbf{x}')$ can be replaced by a kernel $K(\mathbf{x},\mathbf{x}')$, provided $K$ is symmetric and positive semi-definite. The polynomial choice
$$
K(\mathbf{x},\mathbf{x}')=(1+\mathbf{x}^\top\mathbf{x}')^d
$$
is the inner product of a map that contains the monomials up to degree $d$. The constant inside the parentheses includes the lower-degree terms. The pure power $(\mathbf{x}^\top\mathbf{x}')^d$ omits them.{{cite:hastie_esl2009}} (§12.3.1, eq. 12.21–12.22, pp. 423–424)

## Definition — Degree two in two inputs
For $\mathbf{x}=(x_1,x_2)$,
$$
(1+x_1 x_1'+x_2 x_2')^2
=1+2x_1 x_1'+2x_2 x_2'+x_1^2{x_1'}^2+x_2^2{x_2'}^2+2x_1 x_2 x_1' x_2'.
$$
This equals $h(\mathbf{x})^\top h(\mathbf{x}')$ for
$$
h(\mathbf{x})=\bigl(1,\sqrt{2}\,x_1,\sqrt{2}\,x_2,x_1^2,x_2^2,\sqrt{2}\,x_1 x_2\bigr).
$$
The map has length $\binom{2+2}{2}=6$. In $p$ inputs the monomials up to degree $d$ have dimension $\binom{p+d}{d}$. The fitted function is then a linear combination of kernel values against the training points, $f(\mathbf{x})=\sum_i \alpha_i y_i K(\mathbf{x},\mathbf{x}_i)+\beta_0$, and the vectors $h(\mathbf{x}_i)$ are never stored.{{cite:hastie_esl2009}} (§12.3.1, eq. 12.23–12.24, p. 424)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Expand $(1+\mathbf{x}^\top\mathbf{x}')^2$ by writing $\mathbf{x}^\top\mathbf{x}'=x_1 x_1'+x_2 x_2'$ and squaring the sum of three terms. The cross term $2x_1 x_1'\cdot x_2 x_2'$ is the product of the coordinates of $\sqrt{2}\,x_1 x_2$ and $\sqrt{2}\,x_1' x_2'$. The terms $2x_j x_j'$ match $\sqrt{2}\,x_j$ with $\sqrt{2}\,x_j'$. The squares and the constant match the remaining coordinates. Collecting them gives $h(\mathbf{x})^\top h(\mathbf{x}')$.{{cite:hastie_esl2009}} (§12.3.1, eq. 12.23)
:::
:::

## Worked example
Let $\mathbf{x}=(1,2)$ and $\mathbf{x}'=(3,0)$. The original inner product is $3$, so
$$
K(\mathbf{x},\mathbf{x}')=(1+3)^2=16.
$$
The feature vectors are
$$
h(\mathbf{x})=(1,\sqrt{2},2\sqrt{2},1,4,2\sqrt{2}),\qquad h(\mathbf{x}')=(1,3\sqrt{2},0,9,0,0).
$$
Their inner product is $1+3\cdot 2+9=16$. The factors $\sqrt{2}\cdot 3\sqrt{2}=6$ come from the first input, and $1\cdot 9=9$ comes from the square of that input. The second input of $\mathbf{x}'$ is $0$, so every term that uses it drops out.

**Your turn.** Compute $K\bigl((1,0),(0,1)\bigr)$ for this degree-two kernel, and the value of $(\mathbf{x}^\top\mathbf{x}')^2$ on the same pair.

::: {.callout-tip collapse="true" title="Answer"}
The inner product is $0$, so $K=(1+0)^2=1$, while $(0)^2=0$. The two kernels disagree. The constant $1$ inside $K$ is the feature that survives when the inputs are orthogonal.
:::

## Connections — Other kernels and the linear case
The [kernel trick](kernel-trick.qmd) is the replacement of $h(\mathbf{x})^\top h(\mathbf{x}')$ by $K$. A [radial basis function kernel](radial-basis-function-kernel.qmd) is another positive semi-definite choice, and it is not a polynomial. [Which functions are kernels](which-functions-are-kernels.qmd) is the positive semi-definite requirement on every Gram matrix. Degree $d=1$ gives $K=1+\mathbf{x}^\top\mathbf{x}'$, a linear rule plus an intercept feature. The [kernel support vector machine](kernel-support-vector-machine.qmd) is where these inner products are optimised.
