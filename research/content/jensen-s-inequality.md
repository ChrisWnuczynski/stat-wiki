## Motivating example

Suppose a treatment effect varies across patients, and the quantity of interest is the square of that effect. Squaring the average effect and averaging the squared effects are different operations: large individual effects receive much more weight in the second calculation. Jensen's inequality tells which way the comparison goes whenever the transformation is convex. It lets a statistician bound an expected nonlinear outcome using only an expected input, even when the full distribution is difficult to calculate.{{cite:wang2025_foundations}} (Ch. 7, §8.7)

## Intuition

A convex curve lies below its chords, so the height at a weighted average of inputs cannot exceed the same weighted average of their heights. An expectation is a weighted average with probability as the weight. For a concave curve, such as the logarithm on positive inputs, the direction reverses. The inequality is about the shape of the function over the *values that the random variable can take*, not about whether its graph bends somewhere else.{{cite:jensen1906}} (pp. 176–181, convexity and weighted means){{cite:wang2025_foundations}} (Ch. 7, §8.7.1–8.7.2)

## Definition — Convexity and expectation

Let $X$ take values in a convex interval $I$, and let $\varphi$ be convex on $I$. If $X$ and $\varphi(X)$ are integrable, then $\varphi(\mathbb E X)\leq\mathbb E\varphi(X)$. If $\varphi$ is concave, the inequality reverses. For a strictly convex function and a nonconstant $X$, strict inequality holds when the relevant expectations are finite. An affine function gives equality for every distribution, while a merely convex function can give equality when all observed values lie on one straight segment of its graph.{{cite:jensen1906}} (pp. 176–181, definitions and weighted inequality){{cite:wang2025_foundations}} (Ch. 7, §8.7.1–8.7.2)

## Properties — A supporting-line proof

The proof needs one fact about a convex function: at an interior point of its domain, a line can support its graph from below. Put that line at the mean of $X$. Its slope term disappears on taking expectation, leaving exactly the desired comparison. In one dimension, if the mean lies at an endpoint of the support interval, then $X$ must equal that endpoint almost surely, so equality follows directly.{{cite:wang2025_foundations}} (Ch. 7, §8.7.2){{cite:jensen1906}} (pp. 179–181, convexity and weighted means)

::: {.callout-note collapse="true" title="Proof"}
Write $\mu=\mathbb E X$. For $\mu$ in the interior of $I$, convexity supplies a subgradient $a$ with $\varphi(x)\geq\varphi(\mu)+a(x-\mu)$ for every $x\in I$. Substitute $X$ and take expectations: $\mathbb E\varphi(X)\geq\varphi(\mu)+a(\mathbb E X-\mu)=\varphi(\mu)$. If $\mu$ is an endpoint of the support interval, $X=\mu$ almost surely and equality holds. Applying this to $-\varphi$ proves the concave case. For strict convexity, the supporting-line inequality is strict away from $\mu$, so a nonconstant $X$ gives strict expectation inequality.{{cite:wang2025_foundations}} (Ch. 7, §8.7.2)
:::

## Interpretation — The gap measures variation in familiar cases

For $\varphi(x)=x^2$, Jensen gives $(\mathbb E X)^2\leq\mathbb E X^2$ and the gap is exactly $\operatorname{Var}(X)$. For $\varphi(x)=e^x$, it gives $e^{\mathbb E X}\leq\mathbb E e^X$, provided the right side exists. For the concave logarithm on positive values, $\mathbb E\log X\leq\log\mathbb E X$. These are different applications of one convexity principle. The gap's numerical size depends on the curvature and distribution; Jensen alone does not say that it is small.{{cite:jensen1906}} (pp. 177–178, power, exponential and logarithm examples){{cite:wang2025_foundations}} (Ch. 7, §8.7.2)

## Statistical use

In a classification calculation, a concave function of a conditional error rate can be moved outside an expectation to obtain an upper bound; the nearest-neighbour risk formula in the definition section is an example. In likelihood work, concavity of the logarithm bounds an average log score by the log of an average score, though the two quantities answer different questions. In estimation, the square-function case identifies how much a nonlinear plug-in calculation misses because of variation. Jensen therefore gives a direction for approximation error before a more detailed distributional calculation is available.{{cite:wang2025_foundations}} (Ch. 7, §8.7.2, logarithm and variance examples)

## Worked example

Let $X=1$ with probability $1/4$ and $X=3$ with probability $3/4$. Then $\mathbb E X=(1/4)1+(3/4)3=2.5$, while $\mathbb E X^2=(1/4)1^2+(3/4)3^2=7$. Squaring the mean gives $2.5^2=6.25$, so Jensen's gap is $7-6.25=0.75$, the variance. For the concave logarithm, $\mathbb E\log X=(3/4)\log3\approx0.82396$, below $\log(2.5)\approx0.91629$. The two directions differ because the square bends upward and the logarithm bends downward.{{cite:wang2025_foundations}} (Ch. 7, §8.7.2)

**Your turn.** Let $X$ be equally likely to be $1$ or $4$. Calculate both sides of Jensen's inequality for $x^2$ and for $\log x$. State which gaps are strict and why.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $2.5$. For the square, $\mathbb E X^2=(1+16)/2=8.5$ and $(\mathbb E X)^2=6.25$, leaving a gap of $2.25$. For the logarithm, $\mathbb E\log X=(\log1+\log4)/2\approx0.69315$, below $\log(2.5)\approx0.91629$. Both comparisons are strict because $X$ is nonconstant and the square is strictly convex while the logarithm is strictly concave on the positive support.{{cite:wang2025_foundations}} (Ch. 7, §8.7.2)
:::

## Common misconceptions

The inequality does not say $\varphi(X)\geq\varphi(\mathbb E X)$ for *each* outcome; it compares expectations. Its direction is not always upward: a concave function reverses it. It is not automatically strict when $X$ varies, since an affine $\varphi$ gives equality. A function's convexity outside the support cannot rescue an application where it is concave over the values actually taken. Finally, a nonlinear plug-in at $\mathbb E X$ is not generally an unbiased substitute for $\mathbb E\varphi(X)$.{{cite:jensen1906}} (pp. 176–181){{cite:wang2025_foundations}} (Ch. 7, §8.7)

## Assumptions and limits — Where a comparison fails

If $X$ takes both positive and negative values, $\mathbb E\log X$ is not defined as a real expectation, so a logarithm comparison cannot be made. If $\varphi(x)=x^3$ and $X$ crosses zero, the function changes curvature; for $X=-2$ or $1$ with equal probability the simple convex Jensen direction need not hold. A Cauchy-distributed $X$ lacks $\mathbb E X$, so the displayed expectation form has no value to compare. Even with finite moments, a bound can be loose: a very rare enormous value can make $\mathbb E e^X$ far exceed $e^{\mathbb E X}$.{{cite:wang2025_foundations}} (Ch. 7, §§8.7.1–8.7.2, domain and integrability conditions)

## Connections

[Variance](variance.qmd) is the Jensen gap for the square function. [Conditional expectation](conditional-expectation.qmd) permits a conditional version, $\varphi(\mathbb E[X\mid Y])\leq\mathbb E[\varphi(X)\mid Y]$ under the corresponding assumptions. [Markov's inequality](markov-s-inequality.qmd) bounds tail probabilities using a nonnegative variable, whereas Jensen compares a transformed mean with the mean transformation.{{cite:wang2025_foundations}} (Ch. 7, §§8.2, 8.7)

### Guided practice

**1. Equality.** Can a nonconstant random variable give equality in Jensen's inequality? Give a function for which it does.

::: {.callout-tip collapse="true" title="Answer"}
Yes. Any affine function, for example $\varphi(x)=2x+1$, satisfies $\mathbb E\varphi(X)=2\mathbb E X+1=\varphi(\mathbb E X)$ for every integrable $X$. Strictness needs strict curvature on the values that occur.{{cite:wang2025_foundations}} (Ch. 7, §8.7.1–8.7.2)
:::

**2. Domain.** Why can the logarithm form of Jensen not be applied to a variable that sometimes equals zero?

::: {.callout-tip collapse="true" title="Answer"}
The real logarithm is undefined at zero and $\mathbb E\log X$ may be $-\infty$ even for a positive variable approaching zero. The finite-expectation statement requires the function to be defined over the support and the transformed expectation to exist.{{cite:wang2025_foundations}} (Ch. 7, §8.7.2)
:::

## History

Jensen's paper, published in *Acta Mathematica* in 1906, begins with Cauchy's arithmetic–geometric mean argument and then develops a general inequality for convex functions of weighted averages. It extends the finite-sum statement toward integral comparisons, making the expectation form a natural probabilistic reading of the same convexity principle.{{cite:jensen1906}} (pp. 175–181, 186–187)
