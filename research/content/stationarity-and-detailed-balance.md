## Motivating example
A Markov-chain sampler is useful only if its desired target distribution is preserved as the chain moves. One can check this by summing all probability entering each state, but in many samplers it is easier to match the flow along each edge in both directions. That stronger calculation is detailed balance. It proves stationarity, while also identifying a reversible chain whose stationary paths look the same when time is reversed.{{cite:levin_peres2017}} (§1.6, pp. 13–14)

## Intuition
Stationarity is a state-by-state accounting rule: total incoming probability equals the mass already at the state. Detailed balance makes a separate equality for each pair of states, matching the flow from $x$ to $y$ with its reverse. Pairwise equality guarantees the total equality when the flows are summed. The converse need not hold: a steady current can circulate around a cycle, keeping every state's mass fixed while no individual edge is balanced.{{cite:levin_peres2017}} (§1.6, pp. 13–14, biased-cycle example)

## Definition
For a finite state space, let $P(x,y)=\Pr(X_{n+1}=y\mid X_n=x)$ and let $\pi$ be a probability distribution. It is stationary when $\pi(y)=\sum_x\pi(x)P(x,y)$ for every $y$. It satisfies detailed balance when $\pi(x)P(x,y)=\pi(y)P(y,x)$ for every pair. The first is also called global balance; the second says the kernel is reversible with respect to $\pi$. For continuous states, replace sums and point masses by the corresponding integral or measure identity, with care about densities and support.{{cite:levin_peres2017}} (§§1.5.1 and 1.6, pp. 10–14)

## Interpretation
If the chain starts with distribution $\pi$ and $\pi P=\pi$, every later state has the same marginal law. This says nothing by itself about convergence from another start; periodic chains can remain stationary when started correctly yet oscillate from a fixed state. Under detailed balance, the probability of a stationary path $x_0,\ldots,x_n$ equals that of the reversed path $x_n,\ldots,x_0$. A chain can be stationary without having that path symmetry.{{cite:levin_peres2017}} (§1.6, pp. 13–14; §1.3, periodicity)

## Properties
Detailed balance is sufficient for stationarity and for reversibility, but not necessary for stationarity. In the four-state lazy random walk, the weights $(1,2,2,1)/6$ match each neighbouring flow and give the stationary law. Its self-loops also remove the even–odd oscillation of the non-lazy path walk. For a state pair with zero target probability, the balance equation must still be checked on the full support; dividing by $\pi(x)$ is only valid when $\pi(x)>0$.{{cite:levin_peres2017}} (§1.6, pp. 13–14; §1.3, pp. 7–8)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Fix $y$ and sum detailed balance over $x$: $\sum_x\pi(x)P(x,y)=\sum_x\pi(y)P(y,x)=\pi(y)\sum_xP(y,x)=\pi(y)$. Thus $\pi P=\pi$. For a path, multiply each pairwise equality $\pi(x_{i-1})P(x_{i-1},x_i)=\pi(x_i)P(x_i,x_{i-1})$ after cancelling the intermediate $\pi$ factors, or write the forward path probability and replace each transition with its reversed expression. This yields equality with the reversed stationary path probability wherever the relevant probabilities are positive; paths with zero probability satisfy the equality directly.{{cite:levin_peres2017}} (§1.6, pp. 13–14, detailed-balance proof and path identity)
:::
:::

## Statistical use
To validate a proposed stationary law for a finite chain, first check that it is nonnegative and sums to one. Then either verify $\pi P=\pi$ or check the simpler pairwise equations on the allowed transitions. In Metropolis–Hastings, acceptance probabilities are chosen so that accepted moves and their reversals match under the target law. This proves invariance of the kernel; irreducibility and aperiodicity are additional questions before treating distant draws as converged or independent.{{cite:levin_peres2017}} (§§1.5–1.6, pp. 10–14; §3.2)

For a three-state one-way cycle, uniform mass is stationary but no positive pairwise reverse flow exists, so detailed balance is unusable even though global balance works. For the deterministic two-state flip, the uniform law satisfies detailed balance, yet a chain started at one state oscillates forever; balance alone does not prove convergence. On an infinite or continuous state space, a proposed invariant measure may fail to have total mass one, and formal pairwise equations do not make it a stationary *probability* law without normalisation.{{cite:levin_peres2017}} (§1.6, pp. 13–14; §1.3, periodicity)

## Worked example
Consider three states on a directed cycle. From each state, the chain stays put with probability $0.2$ and moves clockwise with probability $0.8$. Each row and column of $P$ sums to one, so $\pi=(1/3,1/3,1/3)$ is stationary. But the flow from state 1 to state 2 is $(1/3)(0.8)=4/15\approx0.2667$, while the reverse flow is zero. Detailed balance fails. This concrete current around the cycle shows why stationarity cannot be inferred to imply reversibility.{{cite:levin_peres2017}} (§1.6, pp. 13–14, biased-cycle example)

**Your turn.** A two-state chain has $P(1,2)=0.3$ and $P(2,1)=0.2$. Find a stationary distribution by detailed balance and check both directed flows.

::: {.callout-tip collapse="true" title="Answer"}
Detailed balance gives $0.3\pi_1=0.2\pi_2$, hence $\pi_2=1.5\pi_1$. Normalising yields $\pi=(0.4,0.6)$. The flows are $0.4(0.3)=0.12$ and $0.6(0.2)=0.12$. Since a two-state chain has only this nontrivial edge pair, the equality proves stationarity.
:::

## Common misconceptions
Stationarity does not mean the chain remains in one state; the distribution stays fixed while paths can move. Detailed balance is stronger than global balance, as the directed cycle shows. A stationary law does not guarantee stepwise convergence from every starting state. Finally, matching one pair of states is not enough for a large chain: all edges with possible flow must be checked, together with normalisation.{{cite:levin_peres2017}} (§§1.5–1.6, pp. 10–14; §1.3, periodicity)

## Connections
The [stationary distribution](stationary-distribution.qmd) page develops invariance and convergence separately. The [birth–death question](../questions/ex-sp-birth-death-pi.qmd) uses local edge balance to find a law on three states; the [periodic-chain question](../questions/ex-prob-markov-periodic.qmd) tests why stationarity does not imply convergence. These exercise different limits of the balance shortcut.{{cite:levin_peres2017}} (§§1.5–1.6, pp. 10–14)

## History
Markov's early work on dependent sequences created the setting in which invariant distributions became central; That work dates to the beginning of the twentieth century. Modern Monte Carlo methods use detailed balance as a constructive way to make a chosen target law stationary, with Hastings's transition design a well-known example.{{cite:dodge2008}} (pp. 330–331, “Markov, Andrei Andreevich”){{cite:levin_peres2017}} (§1.6, pp. 13–14; §3.2)
