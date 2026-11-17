## Motivating example
An insurance payment may be $0$, $100$ or $500$, depending on the event that occurs. Multiplying each payment by the probability of its event gives an average payment without requiring a density, a smooth distribution or a geometrical sample space. Simple random variables turn this finite weighted-average idea into the building block for a general expectation.{{cite:durrett2019}} (§1.4, pp. 18–19, simple-function integral)

## Definition — Values and their measurable pieces
A real simple random variable has finitely many values and can be represented as $S=\sum_{j=1}^k a_j1_{A_j}$ on disjoint measurable events, adding a zero-valued complement if needed. Its expectation is $\sum_j a_jP(A_j)$. The events need not have equal probabilities. A finite-valued observation is simple even if the underlying experiment has infinitely many outcomes.{{cite:siegrist2022_expectation_integral}} (section “Definitions”, finite support)

The representation is not unique. Splitting one event into two disjoint pieces with the same attached value leaves the expectation alone because their probabilities add. More generally, two representations admit the common refinement consisting of all intersections of their pieces. On each intersection both formulas have the same value; summing over the refined partition proves the definition independent of representation. The same refinement proves linearity for two simple variables, without assuming that they are independent.{{cite:durrett2019}} (§1.4, p. 19, simple-function linearity and order)

## Properties — Approximate values from below
For a nonnegative measurable $X$, one explicit approximation is
$$S_m=2^{-m}\left\lfloor 2^m\min(X,m)\right\rfloor,\qquad m=1,2,\ldots.$$
It is simple because truncation makes its range finite. Increasing $m$ raises the truncation threshold and refines the grid, so $S_m\le S_{m+1}\le X$. At every finite value of $X$, eventually truncation disappears and the rounding error is less than $2^{-m}$; hence $S_m\uparrow X$. On points where $X=+\infty$, the sequence tends to infinity as well.

Define the nonnegative integral as the supremum of expectations of simple variables between zero and $X$. Monotone convergence then identifies this supremum with the limit of expectations along any increasing simple approximation. Choosing a particular discretisation supplies a computational route, while the supremum definition expresses why the resulting expectation is intrinsic.{{cite:durrett2019}} (§1.4, pp. 21–22, nonnegative integral; §1.5, monotone convergence)

A signed variable needs more care. Put $X^+=\max(X,0)$ and $X^-=\max(-X,0)$. A finite expectation requires $E|X|<\infty$, equivalently both nonnegative parts have finite expectation. If precisely one part is infinite, an extended expectation can be defined with the corresponding sign. If both are infinite, cancellation is undefined; symmetry of the distribution does not make the expectation zero.{{cite:siegrist2022_expectation_integral}} (section “Definitions”, positive and negative parts)

## Worked example — A payout and a continuous limit
Suppose mutually exclusive loss events have probabilities $0.7,0.2,0.1$ and payouts $0,100,500$. The expected payout is $0(0.7)+100(0.2)+500(0.1)=70$. Paying an administrative amount of $10$ in every outcome raises expectation to $80$. This follows directly by adding the same constant on each piece of the partition.

For a continuous example let $U$ be uniform on $[0,1]$ and define $T_m=2^{-m}\lfloor2^mU\rfloor$. The endpoint $U=1$ has probability zero and makes no contribution. Each of $2^m$ grid values $k/2^m$, $k=0,\ldots,2^m-1$, has probability $2^{-m}$. Therefore
$$ET_m=2^{-2m}\sum_{k=0}^{2^m-1}k=\frac12-2^{-m-1}.$$
The values for $m=1,2,3$ are $0.25,0.375,0.4375$, increasing towards $EU=1/2$. This computes the continuous expectation from finite sums alone.{{cite:durrett2019}} (§1.6, pp. 28–29, expectation as integration)

**Your turn.** A simple variable is $S=2\,1_A+5\,1_B$ with disjoint events of probabilities $0.3$ and $0.2$ and value zero elsewhere. Compute $ES$ and $E(S+4)$.

::: {.callout-tip collapse="true" title="Answer"}
The expectation is $2(0.3)+5(0.2)=1.6$. The complement has probability $0.5$; adding four everywhere raises expectation by $4$, giving $5.6$.
:::

## Connections — The distribution is enough for scalar expectation
If $F_X$ is the probability distribution induced by $X$, then integrating a measurable function of $X$ on the outcome space equals integrating that function against $F_X$. For indicators this is the definition $P(X\in B)=F_X(B)$; finite linear combinations give the simple-function case; increasing limits give nonnegative functions; and positive-negative decomposition gives integrable signed functions. Thus the familiar mass-function sum and density integral are special cases of the same construction.{{cite:siegrist2022_expectation_integral}} (sections “Definitions” and “Change of Variables”)

Once the induced distribution of a single variable is known, a further description of the underlying outcome space is unnecessary for the expectation of a function of that variable.
