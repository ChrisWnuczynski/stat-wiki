## Motivating example

Three measurements may all move together even when the first and third share no association after the middle measurement is known. A Gaussian graphical model asks which associations survive that conditioning. An absent edge concerns the other measured variables; it does not mean that the two measurements have zero marginal correlation.{{cite:bien_tibshirani2011_covariance}} (§1, pp. 807–808)

## Intuition — Marginal association and conditional association

The covariance matrix describes pairs before conditioning. Its inverse describes the quadratic terms in the joint normal log density. A mixed product involving two coordinates disappears when the corresponding precision entry is zero. This is why estimating a sparse inverse covariance matrix estimates a conditional dependence graph.{{cite:friedman_glasso2008}} (§1, p. 432)

An edge also depends on the conditioning set: introducing another measured variable can change a partial correlation. A concentration graph should therefore be read with its vertex set attached. Covariance graphs answer the separate question of which variables are marginally independent.{{cite:bien_tibshirani2011_covariance}} (§1, p. 808)

## Properties — Conditional regression from the quadratic form

For positive definite $K$, collect the terms containing $x_j$ in the log density. Completing the square gives
$$
X_j\mid X_{-j}=x_{-j}\sim N\left(\mu_j-\frac{1}{k_{jj}}\sum_{k\ne j}k_{jk}(x_k-\mu_k),\frac{1}{k_{jj}}\right).
$$
Thus the coefficient of $x_k$ in the conditional regression of $X_j$ is $-k_{jk}/k_{jj}$. The two regressions $j$ on the others and $k$ on the others need not have equal coefficients, but their zero patterns agree. These conditional regressions motivate neighbourhood estimation; a symmetric positive definite precision estimate additionally requires the regressions to be mutually compatible.{{cite:friedman_glasso2008}} (§§1–2, pp. 432–434)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Put $z=x-\mu$. The terms involving $z_j$ are $-k_{jj}z_j^2/2-z_j\sum_{k\ne j}k_{jk}z_k$. Completing the square produces a normal density with variance $1/k_{jj}$ and the stated mean. A positive definite matrix has $k_{jj}>0$, so that density is well defined. Repeating the calculation for a pair gives conditional precision $K_{AA}$ and partial correlation $-k_{jk}/\sqrt{k_{jj}k_{kk}}$.
:::
:::

## Worked example

Let a centred normal vector have covariance
$$
\Sigma=\begin{pmatrix}1&1/2&1/4\\1/2&1&1/2\\1/4&1/2&1\end{pmatrix},\qquad
K=\begin{pmatrix}4/3&-2/3&0\\-2/3&5/3&-2/3\\0&-2/3&4/3\end{pmatrix}.
$$
Multiplication gives $K\Sigma=I$. All three marginal correlations are positive, but $k_{13}=0$, so the graph is the path $1-2-3$. The partial correlations on its edges equal $1/\sqrt5\approx0.4472$. The conditional mean of the middle variable is $2(x_1+x_3)/5$, and its conditional variance is $3/5$. For $x_1=1$ and $x_3=2$, that mean is $1.2$. These are consequences of the conditional quadratic form. The graph describes conditional associations.{{cite:friedman_glasso2008}} (§1, p. 432)

**Your turn.** What are the conditional mean and variance of $X_1$ when $X_2=2$ and $X_3=10$?

::: {.callout-tip collapse="true" title="Answer"}
They are $X_2/2=1$ and $3/4$. The value of $X_3$ has no further effect after $X_2$ is fixed.
:::

## Check yourself

### [Precision to graph](../questions/ex-sl-19-2.qmd) {#self-check-ex-sl-19-2}

For $K=\left(\begin{smallmatrix}2&-1&0\\-1&3&-1\\0&-1&2\end{smallmatrix}\right)$, identify the graph and the partial correlation on each edge.

::: {.callout-tip collapse="true" title="Answer"}
The graph is $1-2-3$ and both edge partial correlations equal $1/\sqrt6$. Its inverse is $\frac18\left(\begin{smallmatrix}5&2&1\\2&4&2\\1&2&5\end{smallmatrix}\right)$, whose $(1,3)$ entry is nonzero.
:::

### [A three-variable chain](../questions/ex-sl-19-3.qmd) {#self-check-ex-sl-19-3}

What is the covariance between the endpoints when the two transition coefficients are $0.8$ and each coordinate has variance one?

::: {.callout-tip collapse="true" title="Answer"}
It is $0.8^2=0.64$. Conditioning on the middle coordinate removes that endpoint association; the precision entry $k_{13}$ is zero.
:::
