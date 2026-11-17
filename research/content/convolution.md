## Lead context
Convolution is the way the distributions of two independent random variables combine into the distribution of their sum.

## Motivating example
The total of two dice is not uniform on $\{2,\ldots,12\}$. A total of $7$ can happen in more orders than a total of $2$. Each face of the first die is added to an independent face of the second, and the probability of a total is the sum of the probabilities of the pairs that produce it. That sum is a convolution.{{cite:pishro_nik2014}} (§5.2, sums of continuous random variables)

## Intuition — Slide one distribution across the other
Fix the sum $z$ and ask which values the first variable can take. If $X=x$, the second must equal $z-x$. For independent variables the joint probability of that pair is the product of the marginals, and $x$ is then added out. For densities the sum becomes an integral. The integrand is the first density at $x$ times the second density at $z-x$, which is the first density multiplied by a reversed and shifted copy of the second.{{cite:pishro_nik2014}} (§5.2, convolution)

## Definition — Mass functions and densities
If $X$ and $Y$ are independent and integer-valued,
$$
\Pr(X+Y=z)=\sum_k \Pr(X=k)\Pr(Y=z-k).
$$
If they are independent with densities $f_X$ and $f_Y$,
$$
f_{X+Y}(z)=\int_{-\infty}^{\infty} f_X(x)\,f_Y(z-x)\,dx.
$$
The integral is the convolution $(f_X*f_Y)(z)$. Without independence the product of marginals is replaced by the joint density along the line $x+y=z$.{{cite:pishro_nik2014}} (§5.2, convolution formula)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For integer-valued independent $X$ and $Y$, partition on the value of $X$:
$$
\Pr(X+Y=z)=\sum_k \Pr(X=k,\,Y=z-k).
$$
Independence factors each term into $\Pr(X=k)\Pr(Y=z-k)$.{{cite:pishro_nik2014}} (§5.1, independent random variables; §5.2, convolution)
:::
:::

## Worked example
Two fair dice are independent, each uniform on $\{1,\ldots,6\}$. A total of $7$ arises from the six pairs $(1,6),\ldots,(6,1)$, each with probability $1/36$, so
$$
\Pr(X+Y=7)=6/36=1/6.
$$
A total of $2$ arises only from $(1,1)$, so the probability is $1/36$. The same convolution with continuous uniforms on $[0,1]$ gives a triangular density: $f_{X+Y}(1.5)=0.5$, because the overlap of the two unit intervals at sum $1.5$ has length $0.5$.

**Your turn.** For the same two dice, find $\Pr(X+Y=5)$.

::: {.callout-tip collapse="true" title="Answer"}
The pairs are $(1,4)$, $(2,3)$, $(3,2)$ and $(4,1)$. Each has probability $1/36$, so the total probability is $4/36=1/9$.
:::

## Connections — Named families and the central limit
The convolution of two independent Poisson mass functions with means $\lambda$ and $\mu$ is Poisson with mean $\lambda+\mu$, which is why the sum stays in the family. Independent normal densities convolve to a normal density whose mean and variance add.{{cite:pishro_nik2014}} (§5.2, sum of independent normals) Repeated convolution of a fixed density is the distribution of a longer sum, and under a finite variance that shape approaches the normal curve of the [central limit theorem](central-limit-theorem.qmd). [Independent random variables](independent-random-variables.qmd) are the hypothesis that lets the joint probability factor inside the sum.

