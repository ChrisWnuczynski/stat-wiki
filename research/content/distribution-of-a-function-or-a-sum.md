## Motivating example

A squared measurement, a component lifetime, and a sum of independent delays require different probability calculations. A transformation changes which input outcomes map to an output value; a sum combines two inputs through their joint law. Finding the support first prevents a density formula from assigning probability to impossible results.{{cite:deisenroth_faisal_ong2020}} (§6.7.1, pp.215–216)

## Definition — Push probabilities through the function

For a measurable function $g$, the distribution of $Y=g(X)$ is specified by
$$F_Y(y)=P\{g(X)\le y\}.$$
Differentiate this CDF wherever it is absolutely continuous. For a differentiable one-to-one branch with nonzero derivative, substitution gives $f_Y(y)=f_X(g^{-1}(y))|d g^{-1}(y)/dy|$. With several inverse branches, their contributions must be added. A transformation that is constant on a set of positive probability can create an atom, which a density alone cannot describe.{{cite:deisenroth_faisal_ong2020}} (§§6.7.1–6.7.2, pp.215–218)

## Worked example — A square has two inverse branches

Let $X$ be uniform on $[-1,1]$ and let $Y=X^2$. For $0<y<1$,
$$P(Y\le y)=P(-\sqrt y\le X\le\sqrt y)=\sqrt y,
\qquad f_Y(y)=\frac1{2\sqrt y}.$$
The CDF is zero below zero and one above one. Thus $P(Y\le1/4)=1/2$ and $E(Y)=1/3$. Using only $+\sqrt y$ would account for half the input interval. The density diverges near zero but its integral is one.{{cite:deisenroth_faisal_ong2020}} (§6.7.1, pp.215–216)

**Your turn.** If $X\sim\operatorname{Exp}(1/2)$ and $Y=1+2X$, find the density and mean of $Y$.

::: {.callout-tip collapse="true" title="Answer"}
The inverse is $x=(y-1)/2$ and its derivative is $1/2$. Thus $f_Y(y)=\tfrac14 e^{-(y-1)/4}$ for $y\ge1$, and zero elsewhere. Its mean is $1+2(2)=5$.
:::

## Properties — Sums and convolution

For independent continuous variables $X$ and $Z$, extend their densities by zero outside their supports. Then
$$f_{X+Z}(s)=\int_{-\infty}^{\infty}f_X(x)f_Z(s-x)\,dx.$$
To derive it, write the CDF as $\int f_X(x)F_Z(s-x)\,dx$ and differentiate under the usual integrability conditions. Independence supplies the product density. If the inputs are dependent, use their joint density instead; their marginal distributions do not in general determine the sum.{{cite:grinstead_snell1997}} (§7.2, p.291, Thm.7.1)

For independent uniform $[0,1]$ variables, the integrand is one precisely where $0\le x\le1$ and $0\le s-x\le1$. The length of that overlap is
$$f_S(s)=\begin{cases}s&0<s<1,\\2-s&1\le s<2,\\0&\text{otherwise}.\end{cases}$$
Integrating gives $P(S\le0.5)=0.125$ and $P(S\le1.5)=0.875$, so $P(0.5<S<1.5)=0.75$. The mean is one and variance is $1/6$.{{cite:grinstead_snell1997}} (§7.2, pp.291–292, Ex.7.3)

## Connections — Combining waiting times

For two independent exponentials of common rate $\lambda$, convolution yields $f_S(s)=\lambda^2s e^{-\lambda s}$ for $s>0$. A sum asks how long successive tasks take. A minimum asks when the first component fails and is more easily found from survival probabilities: for independent $T_i\sim\operatorname{Exp}(\lambda_i)$,
$$P(\min_iT_i>t)=\prod_i e^{-\lambda_i t}=e^{-t\sum_i\lambda_i}.$$
Five independent lifetimes of mean $1000$ therefore have a minimum with mean $1000/5=200$, while their sum has mean $5000$.{{cite:grinstead_snell1997}} (§7.2, pp.292–293, Ex.7.4; p.303, Ex.10)


## Check yourself

### [An affine exponential transformation](../questions/ex-prob-affine-exponential.qmd) {#self-check-ex-prob-affine-exponential}

::: {.callout-tip collapse="true" title="Answer"}
For $X\sim\operatorname{Exp}(1/2)$ and $Y=1+2X$, substitute $x=(y-1)/2$ and multiply by $1/2$. The result is $e^{-(y-1)/4}/4$ on $[1,\infty)$.
:::

### [Two independent exponentials](../questions/ex-prob-independent-exponentials.qmd) {#self-check-ex-prob-independent-exponentials}

::: {.callout-tip collapse="true" title="Answer"}
The density $2e^{-x-2y}$ on the positive quadrant factors into exponential densities with rates one and two. Independence gives $E(XY)=1/2$. Also $\operatorname{Cov}(X+Y,X-Y)=\operatorname{Var}(X)-\operatorname{Var}(Y)=1-1/4=3/4$.
:::
