## Motivating example
A histogram of waiting times changes visibly when its bin edges move.{{cite:parzen1962}} (pp. 1065–1076) A kernel density estimate places a small smooth bump at each observation and averages the bumps, so it describes the shape of a continuous distribution without fixing bins. The width of those bumps is the important judgment: too narrow reproduces chance clumps in the sample, while too wide can hide a second peak that matters to the application.

## Intuition
The empirical distribution gives each observed value mass $1/n$. A density estimate spreads each mass through a kernel $K$ and then averages. In one dimension, $\widehat f_h(x)=(nh)^{-1}\sum_i K\{(x-x_i)/h\}$ for bandwidth $h>0$.{{cite:parzen1962}} (pp. 1065–1076){{cite:silverman1986}} (§2.11, Discussion and bibliography) The factor $1/h$ compensates for stretching or squeezing the kernel: a wider bump is lower so its total area remains one. The shape of $K$ affects fine details, but the bandwidth usually controls the visible smoothness more strongly.

## Definition
For independent observations $x_1,\ldots,x_n$ from a continuous population, choose a nonnegative kernel integrating to one. In one dimension, each term $h^{-1}K((x-x_i)/h)$ is itself a density centred at $x_i$ when $K$ is centred at zero. Averaging makes $\widehat f_h$ a nonnegative density with total area one. For vector observations, replacing the scalar $h^2$ by a positive-definite bandwidth matrix $H$ can stretch the bumps differently in different directions. A density kernel is distinct from a positive-definite feature kernel in a support vector machine.

## Properties — Why smoothing has a cost
At an interior point where the true density $f$ is twice differentiable, a symmetric centred kernel cancels the first-order Taylor term. Its pointwise bias is approximately $(h^2/2)f''(x)\mu_2(K)$, where $\mu_2(K)=\int u^2K(u)\,du$. The leading variance is approximately $f(x)R(K)/(nh)$, with $R(K)=\int K(u)^2\,du$. Thus widening the bandwidth generally raises squared bias while lowering variance. The familiar smooth-density integrated error balance is of order $h^4+1/(nh)$, giving a bandwidth of order $n^{-1/5}$ under its regularity assumptions. These are interior asymptotic statements; a boundary or sharp discontinuity changes the bias behavior.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For a density kernel, $\int\widehat f_h(x)\,dx=(1/n)\sum_i\int h^{-1}K\{(x-x_i)/h\}\,dx$. Substitute $u=(x-x_i)/h$, so $dx=h\,du$. Each integral becomes $\int K(u)\,du=1$, hence the estimate integrates to one. Nonnegativity follows term by term. In $p$ dimensions, $u=H^{-1/2}(x-x_i)$ has Jacobian $dx=|H|^{1/2}du$, which cancels the factor $|H|^{-1/2}$ in each matrix-kernel term.

For the interior approximation, write $E\{\widehat f_h(x)\}=\int K(u)f(x-hu)\,du$. Taylor expansion gives $f(x)-hf'(x)\int uK(u)du+(h^2/2)f''(x)\int u^2K(u)du+o(h^2)$. Symmetry makes the first-order integral zero. Independence gives $\operatorname{Var}\{\widehat f_h(x)\}=\operatorname{Var}[h^{-1}K\{(x-X)/h\}]/n$. Its leading second moment is $f(x)R(K)/(nh)$, while the squared expectation contributes lower order as $h\to0$ and $nh\to\infty$. Balancing integrated squared bias $O(h^4)$ with integrated variance $O(1/(nh))$ yields $h\asymp n^{-1/5}$.

The training-likelihood pitfall follows directly from the same formula. At each observed $x_i$, the summand centred on $x_i$ is $K(0)/(nh)$. If $K(0)>0$, then $\widehat f_h(x_i)\geq K(0)/(nh)$, which diverges as $h\downarrow0$. Consequently the sum of training log-density values has no finite maximizing positive bandwidth. Removing $x_i$ from the estimate evaluated at $x_i$ removes this automatic self-contribution.
:::
:::

## Statistical use — Selecting a bandwidth
A density curve is useful for inspecting skewness, tails and possible multiple modes, and for supplying a smooth estimate at unobserved values. The estimate should be compared under several plausible bandwidths before reading a small peak as a separate population. The empirical training log-likelihood is an unsafe selector: with $K(0)>0$, every observation contributes at least $K(0)/(nh)$ to its own estimated density, which grows without bound as $h$ approaches zero. Leave-one-out log-likelihood removes that self-contribution; other cross-validation or plug-in methods target density error directly.

In R, `density(x, bw =..., kernel =...)` computes a univariate estimate. Its default `bw = "nrd0"` remains the default for historical compatibility, and that default is not a general recommendation; `bw = "SJ"` is one alternative. The argument `adjust` multiplies the chosen bandwidth. This implementation detail matters because a plot can change substantially when the bandwidth changes even if the data do not.

With nonnegative lifetimes, a Gaussian bump centred near zero puts some density below zero, where lifetimes cannot occur; a boundary correction or different estimator may be needed. With a discrete outcome such as a count of failures, a continuous KDE is not a probability mass function. In high dimensions, local neighborhoods become sparse and a full bandwidth matrix has many entries to choose; the same sample may no longer resolve local structure. If the observations are strongly dependent, the independent-sample variance approximation in the proof is unreliable.

## Worked example
Take observations $0,0,2$ and a standard Gaussian kernel $\varphi(u)=(2\pi)^{-1/2}e^{-u^2/2}$. With $h=1$, the density at zero is $\widehat f_1(0)=\{\varphi(0)+\varphi(0)+\varphi(2)\}/3$. Using $\varphi(0)\approx0.39894228$ and $\varphi(2)\approx0.05399097$, this is $(0.39894228+0.39894228+0.05399097)/3\approx0.28395851$. The repeated zero gives two bumps at the same point; it does not create a probability mass at zero, because the estimated curve is still a continuous density.

If $h=2$, the two zero-centred bumps each contribute $\varphi(0)/2$ and the bump centred at two contributes $\varphi(1)/2$. The estimate at zero is $\{2\varphi(0)+\varphi(1)\}/6\approx(0.797884+0.241971)/6\approx0.173309$. Smoothing more has lowered this local peak and spread its area across a wider range. The calculation with observations $-1,0,2$ evaluates the curve at a different point; neither density height is itself a probability.

**Your turn.** With observations $0,2$ and a standard Gaussian kernel, calculate the density estimate at $x=1$ for $h=1$ and for $h=2$. Use $\varphi(1)\approx0.241971$ and $\varphi(0.5)\approx0.352065$.

::: {.callout-tip collapse="true" title="Answer"}
For $h=1$, both standardized distances have magnitude one, so $\widehat f_1(1)=\{\varphi(1)+\varphi(1)\}/2=0.241971$. For $h=2$, both have magnitude $0.5$ and the factor $1/h$ applies: $\widehat f_2(1)=\{\varphi(0.5)+\varphi(0.5)\}/4\approx0.176033$. The second curve is lower at the midpoint even though each bump reaches farther.
:::

## Common misconceptions
A density value can exceed one without violating probability rules; probabilities are areas under the curve. A high local peak does not establish a distinct generating subgroup, because sampling noise and bandwidth can make or erase peaks. The kernel's width is not the histogram bin width: both smooth, but the KDE has no fixed bin edges. Finally, a feature kernel in machine learning computes similarities or inner products and need not be a probability density kernel; the shared word does not make the constructions interchangeable.

## Assumptions and limits — A density value may exceed one
A density value can exceed one without violating probability rules; probabilities are areas under the curve.

## Connections
The [bandwidth](choosing-the-bandwidth.qmd) governs the bias–variance balance, while the [Gaussian kernel](gaussian-kernel.qmd) is one choice of bump shape. A [histogram](histogram.qmd) also estimates a density, but its bins introduce edges the KDE avoids. [Cross-validation](cross-validation.qmd) can assess smoothing on held-out observations. The [kernel density laboratory](../labs/kernel-density.qmd) makes the bandwidth effect visible on the same data.
