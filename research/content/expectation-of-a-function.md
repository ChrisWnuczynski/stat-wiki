## Motivating example
A random measurement may enter a nonlinear cost, such as its square, an excess over a threshold or the indicator of an alarm. Finding the whole distribution of that transformed quantity can be unnecessary if the goal is only its mean. The expectation-of-a-function rule computes the average directly using the distribution of the underlying measurement. It weights the transformed values by the probabilities or density of the values that produced them.{{cite:grinstead_snell1997}} (§6.1, pp. 229–230, expectation of a function)

## Statement
For a random variable $X$ and measurable real function $g$, if $g(X)\ge0$, its expectation is the possibly infinite integral $\int g\,dP_X$. If $E|g(X)|<\infty$, the expectation is a finite real number. In particular,
$$E\{g(X)\}=\sum_xg(x)p_X(x)\quad\text{or}\quad E\{g(X)\}=\int g(x)f_X(x)\,dx,$$
for a discrete law or a law with density. If both positive and negative parts have infinite expectation, their formal subtraction does not define an expectation. Absolute convergence is the safe condition for the signed discrete sum.{{cite:grinstead_snell1997}} (§6.1, pp. 229–230, expectation of a function; §6.3, expectation of a function)

## Proof
For a finite-valued $X$, group together values of $x$ sharing the same transformed value $z=g(x)$. Then
$$\sum_z z\Pr\{g(X)=z\}=\sum_z z\sum_{x:g(x)=z}p_X(x)=\sum_xg(x)p_X(x).$$
For a nonnegative simple function $g=\sum_ja_j\mathbf1_{A_j}$, linearity gives $E\{g(X)\}=\sum_ja_jP_X(A_j)=\int g\,dP_X$. Approximating a nonnegative measurable function from below by simple functions and applying monotone convergence gives the general nonnegative identity. Splitting an absolutely integrable signed function into positive and negative parts gives the finite signed case. This is an integration identity for the induced law $P_X$, so it does not require an invertible transformation.{{cite:grinstead_snell1997}} (§§6.1, 6.3, direct expectation rule)

## Key results — Nonlinearity changes the average
Taking $g(x)=ax+b$ gives $E(aX+b)=aE(X)+b$. Taking $g(x)=x^2$ gives the second moment and, when finite, $\operatorname{Var}(X)=E(X^2)-\{E(X)\}^2$. Consequently $E(X^2)$ generally differs from $\{E(X)\}^2$. Taking an indicator gives $E\mathbf1_A(X)=\Pr(X\in A)$, which turns probability calculations into expectations.{{cite:dodge2008}} (p. 190, expected value and its properties)

## Worked example
### A squared loss and an excess charge
Let $X$ take $-1,0,2$ with probabilities $1/4,1/2,1/4$. Then $E(X)=1/4$, while $E(X^2)=5/4$ and $\operatorname{Var}(X)=19/16$. Substituting the mean into the square would give only $1/16$. If the charge is $g(x)=\max(x-1,0)$, its expectation is $1/4$: only the outcome $2$ incurs a charge. No transformed distribution table is needed, although constructing it would give the same answer.{{cite:grinstead_snell1997}} (§6.1, pp. 229–230, expectation of a function)

For a continuous illustration, if $U$ is uniform on $[0,1]$, then $E(U^2)=\int_0^1u^2\,du=1/3$, while $\{E(U)\}^2=1/4$. The difference $1/12$ is its variance.{{cite:grinstead_snell1997}} (§6.3, p. 272, uniform variance)

**Your turn.** For the discrete $X$ above, calculate $E|X|$.

::: {.callout-tip collapse="true" title="Answer"}
It is $1(1/4)+0(1/2)+2(1/4)=3/4$.
:::

## Statistical use — Choose the quantity to be averaged
Expected losses compare decisions on the scale that matters for the decision, and posterior expectations average functions of a parameter against its posterior law. In either setting the function and probability law must both be specified. A Monte Carlo average of transformed draws approximates this integral, while transforming the Monte Carlo mean generally targets a different quantity.{{cite:dodge2008}} (p. 190, weighted-mean definition)
