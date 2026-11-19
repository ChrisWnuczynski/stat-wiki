## Motivating example
A posterior density may be evaluable only up to a normalising constant. With a symmetric local proposal, the Metropolis algorithm needs only the ratio of target densities at the current and proposed states. A rejected proposal contributes another observation of the current state to the chain.{{cite:prado_ferreira_west2021}} (§1.5.5.1, pp. 25–26)

## Definition — A symmetric proposal and an accept/reject step
Let $\pi(x)$ be a target density or mass function. From current state $x$ propose $y\sim q(\cdot\mid x)$ with $q(y\mid x)=q(x\mid y)$. Accept the proposal with probability
$$
\alpha(x,y)=\min\{1,\pi(y)/\pi(x)\};
$$
otherwise the next state is $x$. The ratio cancels any multiplicative normalising constant in $\pi$. The state must remain within the target's support.{{cite:prado_ferreira_west2021}} (§1.5.5.1, pp. 25–26)

An asymmetric proposal requires the Hastings correction $q(x\mid y)/q(y\mid x)$. A proposal being centred near $x$ does not guarantee symmetry: truncating or renormalising at a boundary can change its forward and reverse probabilities.{{cite:hastings1970}} (§2.1, pp. 98–99)

## Properties — Why the rejected states count
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For two distinct states, the stationary flow is
$$
\pi(x)q(y\mid x)\alpha(x,y)
=q(y\mid x)\min\{\pi(x),\pi(y)\}.
$$
Proposal symmetry makes this expression unchanged on exchanging $x$ and $y$. The self-transition probability completes each transition row to one. Detailed balance then gives stationarity after summing or integrating over the starting state. The stay probabilities are part of the kernel in this argument.{{cite:hastings1970}} (§2.1, p. 98)
:::
:::

Stationarity is a property of the transition kernel. Convergence from a specified starting state needs additional conditions, and dependence remains between successive draws even after the target is stationary. Monte Carlo uncertainty must therefore account for serial correlation.{{cite:hastings1970}} (§2.2, pp. 99–101)

## Worked example
Consider three states with unnormalised target weights $(1,2,3)$. Propose either of the other states with probability $1/2$. The Metropolis transition matrix is
$$
P=\begin{pmatrix}
0&1/2&1/2\\
1/4&1/4&1/2\\
1/6&1/3&1/2
\end{pmatrix}.
$$
Its invariant distribution is $(1/6,1/3,1/2)$. For example, the flow from state $2$ to state $1$ is $(1/3)(1/4)=1/12$, equal to the reverse flow $(1/6)(1/2)$.{{cite:hastings1970}} (§2.1, detailed-balance construction)

If the repeated states are discarded, the chain observed only at accepted moves has invariant weights proportional to target mass times the probability of leaving that state. Here those weights are proportional to $(1/6,1/4,1/4)$, giving $(1/4,3/8,3/8)$. That is a different distribution. Averages over the full Markov sequence must include rejections.

**Your turn.** From the state with target weight $3$, what is the probability of accepting a proposal to the state with weight $1$?

::: {.callout-tip collapse="true" title="Answer"}
The probability is $1/3$. Since that proposal is selected with probability $1/2$, its total transition probability is $1/6$.
:::
