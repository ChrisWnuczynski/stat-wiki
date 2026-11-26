## Motivating example
A random measurement may enter a nonlinear cost, such as its square, an excess over a threshold or the indicator of an alarm. Finding the whole distribution of that transformed quantity can be unnecessary if the goal is only its mean. The expectation-of-a-function rule computes the average directly using the distribution of the underlying measurement. It weights the transformed values by the probabilities or density of the values that produced them.{{cite:grinstead_snell1997}} (§6.1, pp. 229–230, expectation of a function)

## Statement
For a random variable $X$ and measurable real function $g$, if $g(X)\ge0$, its expectation is the possibly infinite integral $\int g\,dP_X$. If $\E|g(X)|<\infty$, the expectation is a finite real number. In particular,
$$\E\{g(X)\}=\sum_xg(x)p_X(x)\quad\text{or}\quad \E\{g(X)\}=\int g(x)f_X(x)\,dx,$$
for a discrete law or a law with density. If both positive and negative parts have infinite expectation, their formal subtraction does not define an expectation. Absolute convergence is the safe condition for the signed discrete sum.{{cite:grinstead_snell1997}} (§6.1, pp. 229–230, expectation of a function; §6.3, expectation of a function)

## Proof
For a finite-valued $X$, group together values of $x$ sharing the same transformed value $z=g(x)$. Then
$$\sum_z z\Pr\{g(X)=z\}=\sum_z z\sum_{x:g(x)=z}p_X(x)=\sum_xg(x)p_X(x).$$
For a nonnegative simple function $g=\sum_ja_j\mathbf1_{A_j}$, linearity gives $\E\{g(X)\}=\sum_ja_jP_X(A_j)=\int g\,dP_X$. Approximating a nonnegative measurable function from below by simple functions and applying monotone convergence gives the general nonnegative identity. Splitting an absolutely integrable signed function into positive and negative parts gives the finite signed case. This is an integration identity for the induced law $P_X$, so it does not require an invertible transformation.{{cite:grinstead_snell1997}} (§§6.1, 6.3, direct expectation rule)

## Key results — Nonlinearity changes the average
Taking $g(x)=ax+b$ gives $\E(aX+b)=aE(X)+b$. Taking $g(x)=x^2$ gives the second moment and, when finite, $\operatorname{Var}(X)=\E(X^2)-\{\E(X)\}^2$. Consequently $\E(X^2)$ generally differs from $\{\E(X)\}^2$. Taking an indicator gives $\E\mathbf1_A(X)=\Pr(X\in A)$, which turns probability calculations into expectations.{{cite:dodge2008}} (p. 190, expected value and its properties)

## Worked example
### A squared loss and an excess charge
Let $X$ take $-1,0,2$ with probabilities $1/4,1/2,1/4$. Then $\E(X)=1/4$, while $\E(X^2)=5/4$ and $\operatorname{Var}(X)=19/16$. Substituting the mean into the square would give only $1/16$. If the charge is $g(x)=\max(x-1,0)$, its expectation is $1/4$: only the outcome $2$ incurs a charge. No transformed distribution table is needed, although constructing it would give the same answer.{{cite:grinstead_snell1997}} (§6.1, pp. 229–230, expectation of a function)

For a continuous illustration, if $U$ is uniform on $[0,1]$, then $\E(U^2)=\int_0^1u^2\,du=1/3$, while $\{\E(U)\}^2=1/4$. The difference $1/12$ is its variance.{{cite:grinstead_snell1997}} (§6.3, p. 272, uniform variance)

**Your turn.** For the discrete $X$ above, calculate $\E|X|$.

::: {.callout-tip collapse="true" title="Answer"}
It is $1(1/4)+0(1/2)+2(1/4)=3/4$.
:::

## Statistical use — Choose the quantity to be averaged
Expected losses compare decisions on the scale that matters for the decision, and posterior expectations average functions of a parameter against its posterior law. In either setting the function and probability law must both be specified. A Monte Carlo average of transformed draws approximates this integral, while transforming the Monte Carlo mean generally targets a different quantity.{{cite:dodge2008}} (p. 190, weighted-mean definition)

## Intuition
The expectation-of-a-function rule changes the number that is averaged and leaves the probability weights where they were. A value $x$ that had probability $p_X(x)$, or density $f_X(x)$, still contributes with that weight. The function $g$ only replaces $x$ by the cost, payoff, or indicator attached to $x$. If several inputs share one output, the proof groups those inputs first and adds their probabilities, then multiplies by the shared output. Invertibility of $g$ is not part of the argument.

Collapsing $X$ to its mean and only then applying $g$ is a different operation. That collapse throws away variation that a curved $g$ may charge. In the three-point example, the mean is $1/4$ and the square of the mean is $1/16$, while the mean of the square is $5/4$. The gap $19/16$ is the variance. The same identity, $\E(X^2)-\{\E(X)\}^2=\operatorname{Var}(X)$, holds for every random variable with a finite second moment.

An indicator makes the rule look like a probability statement because it is one. If $g=\mathbf 1_A$, then $g(X)$ equals one on the event $\{X\in A\}$ and zero elsewhere, so its expectation equals that event's probability. Tail probabilities, distribution functions, and event probabilities are expectations of this kind. A variance is an expectation of a square. A posterior expected loss is an expectation against a posterior law. The grammar is the same once the probability law and the function have both been named.

### Key results — Convex costs penalise spread
Suppose $g$ is convex and both $\E(X)$ and $\E|g(X)|$ are finite. Jensen's inequality says that $\E\{g(X)\}$ is at least $g\{\E(X)\}$.{{cite:jensen1906}} (pp. 176–181){{cite:wang2025_foundations}} (Ch. 7, §8.7) The square is the standard illustration: $\{\E(X)\}^2\le \E(X^2)$, and the difference is the variance. A linear function $g(x)=ax+b$ is both convex and concave, so the inequality becomes the equality $\E(aX+b)=aE(X)+b$ already obtained from the sum.

The inequality is strict for a strictly convex $g$ when $X$ is not concentrated at a single value. Squaring the three-point law gives a strict gap: $5/4$ against $1/16$. The uniform law on $[0,1]$ gives the same lesson on a continuous scale, with $\E(U^2)=1/3$ and $\{\E(U)\}^2=1/4$. Jensen's inequality explains the direction of that gap. It does not by itself compute the size; the integral or the sum still has to be evaluated.

A standard exponential waiting time, with density $e^{-t}$ for $t>0$, shows the same split of targets. Integrating $t e^{-t}$ and $t^2 e^{-t}$ against that density, which is the continuous form of the rule, gives mean $1$ and second moment $2$. The variance is $1$. Squaring the mean waiting time returns $1$ and misses the second unit of the second moment. The calculation is ordinary integration against the density of the waiting time; no new density for the square is required.

The absolute deviation from the mean is another function of the same three-point law. With mean $1/4$, the absolute deviations at $-1$, $0$, and $2$ are $5/4$, $1/4$, and $7/4$. Weighting by $1/4$, $1/2$, and $1/4$ gives
$$\frac{5}{16}+\frac{1}{8}+\frac{7}{16}=\frac{7}{8}.$$
This is $\E|X-\E(X)|$, a different functional from $\E|X|=3/4$. The two agree only for special laws. Reporting one of them does not determine the other.

## Common misconceptions
A finite mean of $X$ does not guarantee a finite mean of $g(X)$. In the St Petersburg game a fair coin is tossed until the first head, and a head on toss $n$ pays $2^n$ with probability $2^{-n}$. Each term in the expectation equals $1$, so the sum diverges.{{cite:grinstead_snell1997}} (Ch. 6, §6.1) A long finite play still has an average of the observed payoffs. That average is not estimating a finite population expectation, because none exists.

Signed variables need a further caution. If the positive part of $g(X)$ and the negative part both have infinite expectation, their formal difference is not a real number. Absolute integrability, $\E|g(X)|<\infty$, is the condition that makes the signed sum or integral unambiguous. Nonnegative $g$ may have an infinite expectation, and that infinite value is well defined as an extended number. The two situations should be kept separate when a model is declared.

A Monte Carlo average of the transformed draws estimates $\E\{g(X)\}$, up to ordinary sampling error. Averaging the draws first and then applying $g$ estimates a different target whenever $g$ is nonlinear. The second procedure can be a useful approximation to $g\{\E(X)\}$, and it remains the wrong estimator of $\E\{g(X)\}$ even if the sample is huge. The distinction is the same one Jensen's inequality quantifies for a convex cost.

## Related concepts
Moments, probabilities, and expected losses are one construction with different choices of $g$. The distribution of $g(X)$ is a further object: it is needed for a quantile of the transformed variable, or for a probability such as $\mathbb{P}\{g(X)>c\}$ when $g$ is not an indicator. The expectation rule skips that distribution when only the mean is required. Building the distribution and then averaging it must return the same mean when the mean exists, which is what the grouping argument proves for a finite-valued $X$.

The same split appears in estimation. A plug-in $g(\widehat\theta)$ estimates $g(\theta)$. The expectation $\E\{g(\widehat\theta)\}$ is generally different, and the difference is a bias created by the curvature of $g$. The delta method later approximates that transformed sampling law. It does not replace the exact identity $\E\{g(X)\}=\int g\,dP_X$ when the integral can be evaluated directly.{{cite:grinstead_snell1997}} (§6.1, pp. 229–230, expectation of a function)
