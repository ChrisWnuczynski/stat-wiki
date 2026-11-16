## Lead context
A discrete-time Markov chain chooses its next state from a distribution that depends on the state it occupies now.

## Intuition — The present state is the whole memory
The chain may still be dependent from one time to the next. What the definition removes is any extra dependence on the route that led to the present state. Two paths that arrive in the same state then leave with the same probabilities. The transition matrix records those probabilities: row $i$ is the distribution of the next state when the chain is in $i$, so the entries are non-negative and the row sums to one.{{cite:norris1997}} (§1.1, pp. 2–3)

## Definition — A stochastic matrix and an initial law
Let $I$ be a countable set of states and let $P=(p_{ij})$ be a matrix on $I$ whose every row is a probability distribution. A process $(X_n)_{n\ge 0}$ is a Markov chain with initial distribution $\lambda$ and transition matrix $P$ when $X_0$ has law $\lambda$ and, given $X_n=i$, the next state $X_{n+1}$ has distribution $(p_{ij}:j\in I)$ and does not depend on $X_0,\ldots,X_{n-1}$.{{cite:norris1997}} (§1.1, p. 2)

The same rule implies a joint formula. For any finite string of states,
$$
\Pr(X_0=i_0,\ldots,X_N=i_N)=\lambda_{i_0}p_{i_0 i_1}\cdots p_{i_{N-1}i_N}.
$$
A conditional probability of the next state, given the whole past, is then the single factor $p_{i_n i_{n+1}}$.{{cite:norris1997}} (§1.1, pp. 2–3, joint formula)

## Properties — Two steps add the routes through the middle
Write $p_{ij}^{(2)}$ for the probability of going from $i$ to $j$ in two steps. Conditioning on the intermediate state gives
$$
p_{ij}^{(2)}=\sum_{k\in I}p_{ik}p_{kj},
$$
which is the $(i,j)$ entry of $P^2$.{{cite:norris1997}} (§1.1, pp. 2–3)

A probability row vector $\pi$ is invariant when $\pi P=\pi$. If the chain starts with law $\pi$, it still has law $\pi$ after one step, and therefore at every later time.{{cite:norris1997}} (§1.7, invariant distributions)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Fix states $i$ and $j$. The law of total probability splits the two-step event on the state $k$ occupied at the middle time. The Markov property replaces the conditional probability of the second step by $p_{kj}$, and the first step contributes $p_{ik}$. Summing over $k$ is matrix multiplication, so the two-step matrix is $P^2$.{{cite:norris1997}} (§1.1, pp. 2–3)

Now suppose $\pi P=\pi$ and $X_0$ has law $\pi$. The law of $X_1$ is the row $\pi P$, which equals $\pi$. The same one-step update applies at every later time, so $X_n$ has law $\pi$ for every $n$.{{cite:norris1997}} (§1.7, invariant distributions)
:::
:::

## Worked example
Take the two-state chain with
$$
P=\begin{pmatrix}0.8&0.2\\0.5&0.5\end{pmatrix}.
$$
Starting in state $1$, the chance of being in state $2$ two steps later is $0.8\times 0.2+0.2\times 0.5=0.26$. The off-diagonal rates are $\alpha=0.2$ and $\beta=0.5$, so an invariant distribution is
$$
\pi=\Bigl(\frac{\beta}{\alpha+\beta},\frac{\alpha}{\alpha+\beta}\Bigr)=\Bigl(\frac{5}{7},\frac{2}{7}\Bigr).
$$
The first coordinate of $\pi P$ is $(5/7)(0.8)+(2/7)(0.5)=5/7$, which checks the fixed-point equation.{{cite:norris1997}} (§1.1, p. 2; §1.7, the two-state chain)

**Your turn.** Change the off-diagonal probabilities to $\alpha=0.4$ and $\beta=0.1$. Find the invariant probability of state $1$, and the two-step probability of staying in state $1$.

::: {.callout-tip collapse="true" title="Answer"}
The invariant probability of state $1$ is $0.1/(0.4+0.1)=0.2$. The two-step stay probability is $0.6\times 0.6+0.4\times 0.1=0.40$.{{cite:norris1997}} (§1.1, p. 2)
:::

## Connections
The one-step rule is the discrete-time case of the [Markov property](markov-property.qmd). The matrix $P$ is a [transition matrix](transition-matrix.qmd). An invariant row $\pi$ is the chain's [stationary distribution](stationary-distribution.qmd) when it is used as the starting law. The same matrix arithmetic, with a target distribution in place of $\pi$, is what a Monte Carlo chain is built to preserve.{{cite:norris1997}} (§1.7, invariant distributions)

## Check yourself — Two quick matrix checks
**1.** Both rows of a two-state matrix equal $(1/2,1/2)$. What is the two-step probability of moving from state $1$ to state $2$?

::: {.callout-tip collapse="true" title="Answer"}
Every one-step probability into state $2$ is $1/2$, so the two-step probability is $(1/2)(1/2)+(1/2)(1/2)=1/2$. The square of this matrix equals the matrix itself.{{cite:norris1997}} (§1.1, pp. 2–3)
:::

**2.** Successive states of a Markov chain are not automatically independent. For the worked matrix above, why is state $2$ more likely after state $2$ than after state $1$?

::: {.callout-tip collapse="true" title="Answer"}
The second row puts probability $0.5$ on staying in state $2$, while the first row puts only $0.2$ there. Different rows mean the next state still carries information about the current state.{{cite:norris1997}} (§1.1, p. 2)
:::
