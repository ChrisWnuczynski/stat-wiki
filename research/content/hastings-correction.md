## Lead context
The Hastings correction down-weights a proposed move that the jumping rule was already eager to make, and it up-weights a move the jumping rule rarely offers.

## Motivating example
A random-walk proposal centred on the current value is equally happy to go from $a$ to $b$ and from $b$ to $a$. The chance of accepting the move can then depend on the target density alone. An asymmetric proposal does not have that balance. If it is much easier to jump from the current point to the candidate than to jump back, an uncorrected rule would visit the candidate too often. The Hastings factor puts the return probability back into the acceptance chance.{{cite:gelman_bda2013}} (§11.2, pp. 278–280)

## Intuition — A ratio of ratios
Let $p$ be the target density and let $J(\omega^\ast\mid\omega)$ be the density of proposing $\omega^\ast$ from $\omega$. The Metropolis rule, which assumes $J(\omega^\ast\mid\omega)=J(\omega\mid\omega^\ast)$, accepts a move with probability $\min(r,1)$ for $r=p(\omega^\ast)/p(\omega)$. Hastings replaces that ratio by
$$
r=\frac{p(\omega^\ast)/J(\omega^\ast\mid\omega)}{p(\omega)/J(\omega\mid\omega^\ast)}=\frac{p(\omega^\ast)\,J(\omega\mid\omega^\ast)}{p(\omega)\,J(\omega^\ast\mid\omega)}.
$$
The move is accepted with probability $\min(r,1)$. When the proposal is symmetric the two jumping densities cancel and the Metropolis ratio remains. When they do not, a proposal that is too keen in one direction is accepted less often, exactly enough that the chain's stationary distribution is still $p$.{{cite:gelman_bda2013}} (§11.2, eq. 11.2, p. 280)

## Definition — The correction factor
The Hastings correction in the ratio above is $J(\omega\mid\omega^\ast)/J(\omega^\ast\mid\omega)$. It equals $1$ for every symmetric proposal, including a random walk with a symmetric increment. It is undefined only if the proposal actually used had probability zero, which cannot occur for a jump the chain just proposed.{{cite:gelman_bda2013}} (§11.2, p. 280)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Suppose $J(\omega^\ast\mid\omega)=J(\omega\mid\omega^\ast)$ for the two points in the ratio. Then the factors of $J$ cancel, and equation (11.2) reduces to $p(\omega^\ast)/p(\omega)$, which is the Metropolis ratio (11.1). In particular the correction factor equals $1$.{{cite:gelman_bda2013}} (§11.2, eq. 11.1 and eq. 11.2)
:::
:::

The argument that this $r$ makes $p$ stationary is the same detailed-balance comparison as in the symmetric case, with the jumping densities left in the product. That comparison is not reproduced here.

## Worked example
Suppose the target values are $p(1)=0.2$ and $p(3)=0.5$, and the proposal densities are $J(3\mid 1)=0.4$ and $J(1\mid 3)=0.1$. A move from $1$ to $3$ has
$$
r=\frac{0.5\times 0.1}{0.2\times 0.4}=0.625.
$$
The target density is higher at $3$, by a factor $2.5$, but the proposal is four times more likely to go from $1$ to $3$ than to return. The product of $2.5$ and $1/4$ is $0.625$, so the move is accepted with probability $0.625$ and rejected with probability $0.375$. Despite the higher target density, the move is not automatic.

**Your turn.** Keep the same target values and make the proposal symmetric, with $J(3\mid 1)=J(1\mid 3)=0.2$. What is $r$ for the move from $1$ to $3$, and what is the acceptance probability?

::: {.callout-tip collapse="true" title="Answer"}
The correction factor is $1$, so $r=0.5/0.2=2.5$. The acceptance probability is $\min(2.5,1)=1$. Every proposal from $1$ to $3$ is accepted. The symmetric rule no longer needs to refuse some of those moves.
:::

## Connections — Symmetric walks and Gibbs updates
The [Metropolis algorithm](metropolis-algorithm.qmd) is the special case with correction $1$. The [Metropolis–Hastings algorithm](metropolis-hastings-algorithm.qmd) is the general step, and [Metropolis–Hastings invariance](metropolis-hastings-invariance.qmd) is the statement that the target remains stationary. A Gibbs update is a Metropolis–Hastings step whose conditional proposal makes $r=1$ for every legal jump, so the draw is always accepted.{{cite:gelman_bda2013}} (§11.4, Gibbs as Metropolis–Hastings)

## Check yourself

### A keen reverse jump
Using $p(1)=0.2$, $p(3)=0.5$, $J(1\mid 3)=0.4$ and $J(3\mid 1)=0.1$, find $r$ for a move from $1$ to $3$.

::: {.callout-tip collapse="true" title="Answer"}
$$
r=\frac{0.5\times 0.4}{0.2\times 0.1}=10.
$$
The acceptance probability is $1$. The proposal rarely offers the move, and the target density is higher at the destination, so the correction makes the ratio larger than $1$.
:::

### Where the correction is idle
A proposal adds an increment drawn from $N(0,1)$, independent of the sign. What is the Hastings correction?

::: {.callout-tip collapse="true" title="Answer"}
The increment density is symmetric, so $J(\omega+d\mid\omega)=J(\omega\mid\omega+d)$. The correction equals $1$ and the acceptance ratio reduces to the ratio of target densities.
:::
