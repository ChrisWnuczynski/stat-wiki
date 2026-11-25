## Motivating example
A Markov chain simulation often starts with a desired equilibrium distribution and needs transition probabilities that preserve it. Solving every stationarity equation at once can be inconvenient. Detailed balance instead matches the probability flow along each pair of opposite transitions. Those local equalities provide a direct sufficient condition for the desired distribution to be stationary.{{cite:hastings1970}} (§2.2, pp. 99–100)

## Statement
Let $P$ be a row-stochastic transition matrix on a finite or countable state space, and let $\pi$ be a probability vector. If $\pi_iP_{ij}=\pi_jP_{ji}$ for every pair of states, then $\pi P=\pi$. The assumption that $\pi$ sums to one distinguishes a stationary probability distribution from a merely invariant measure. In an infinite state space, an unnormalisable set of balance weights does not give a stationary probability vector.{{cite:grinstead_snell1997}} (§11.5, p. 463, time reversal and reversible chains)

## Proof
For a fixed destination state $j$, sum the detailed-balance equalities over all origins $i$:
$$ (\pi P)_j=\sum_i\pi_iP_{ij}=\sum_i\pi_jP_{ji}=\pi_j\sum_iP_{ji}=\pi_j.$$
The last sum is over row $j$ of $P$, and equals one. Nonnegative terms justify the same summation in a countable state space. This proof neither uses nor establishes irreducibility or aperiodicity. It only establishes preservation of $\pi$ after a transition.{{cite:hastings1970}} (§2.2, reversibility and the stationary distribution)

## Key results — Reversibility imposes more than equilibrium
At stationarity, $\Pr(X_t=i,X_{t+1}=j)=\pi_iP_{ij}$. Detailed balance makes that pair probability unchanged when time is reversed. More generally, multiplying the pairwise equalities along a finite path shows that the stationary path and its reversal have equal probabilities. A stationary chain can nevertheless have net circulation, in which case it is not reversible. Stationarity and reversibility are therefore different structural properties.{{cite:grinstead_snell1997}} (§11.5, p. 463, reverse chains)

## Worked example
### A two-state chain
Take
$$P=\begin{pmatrix}3/4&1/4\\1/2&1/2\end{pmatrix},\qquad \pi=(2/3,1/3).$$
The two cross-flows are $(2/3)(1/4)=1/6$ and $(1/3)(1/2)=1/6$. Diagonal flow conditions hold automatically, so detailed balance proves stationarity. Direct multiplication gives $\pi P=(2/3,1/3)$ as a check. Starting from state one instead gives next-step law $(3/4,1/4)$, showing that having a stationary distribution does not mean that every initial distribution already equals it.{{cite:hastings1970}} (§2.2)

A deterministic cycle on three states has a uniform stationary distribution but positive flow only in the cycle's forward direction. Its reverse cross-flow is zero. This gives a finite counterexample to the converse: global inflow equals global outflow even though opposite edge flows do not match.{{cite:grinstead_snell1997}} (§11.5, p. 463, reversibility and reverse transition matrices)

**Your turn.** Replace $P$ by the two-state identity matrix. Does it satisfy detailed balance with $\pi=(2/3,1/3)$, and does a chain starting in state one approach that distribution?

::: {.callout-tip collapse="true" title="Answer"}
Detailed balance holds because both cross-flows are zero. A chain starting in state one stays there forever, so it does not approach the specified mixture.
:::

## Common misconceptions — Invariance is only one simulation requirement
A reducible chain may preserve many stationary distributions and never move between their components. A periodic chain can preserve a distribution while its law oscillates from a fixed starting point. For practical simulation, the transition construction must therefore be followed by an analysis of reachability, periodicity and mixing. The balance proof checks an invariant target, not the adequacy of a particular finite simulation run.{{cite:hastings1970}} (§§2.1–2.2)


## Statistical use — Construct a sampling transition through balanced flows
For a proposed simulation transition, checking the two directed stationary flows on each edge can be simpler than multiplying a large transition matrix. Metropolis–Hastings uses an acceptance rule designed to make those flows agree, accounting for an asymmetric proposal in both directions. The construction still needs a valid transition kernel and a proper target probability distribution. Invariance identifies a candidate equilibrium; useful sampling additionally depends on the chain reaching and exploring its relevant support.{{cite:hastings1970}} (§2.2, pp. 99–100)

## Intuition
Stationarity says that if the chain is started from $\pi$, the distribution after one step is still $\pi$. That is a global balance of probability: the total flow into each state equals the total flow out. Detailed balance is a stronger bookkeeping rule. It matches the flow from $i$ to $j$ with the flow from $j$ to $i$, for every pair, rather than only matching the sums. In the two-state example the off-diagonal flows are $(2/3)(1/4)=1/6$ and $(1/3)(1/2)=1/6$. They agree, so the global sums agree, and $\pi P=\pi$. The diagonal flows do not need a separate check. A transition from a state to itself appears on both sides of the detailed-balance equation as the same product $\pi_i P_{ii}$.

The identity matrix on two states satisfies detailed balance with every probability vector, because every cross-flow is zero. Stationarity holds. A chain that starts in state one stays in state one, so the existence of a stationary distribution $\pi=(2/3,1/3)$ does not mean that this chain approaches $\pi$ from every start. Detailed balance delivered invariance. Irreducibility and aperiodicity, which this chain lacks, are what deliver convergence from an arbitrary start.

## Related concepts — A return probability fixed by one flow
Suppose $\pi_A=1/4$, $\pi_B=3/4$, and $P_{AB}=1/3$. The flow from $A$ to $B$ is $(1/4)(1/3)=1/12$. Detailed balance requires $\pi_B P_{BA}=1/12$, so $P_{BA}=(1/12)/(3/4)=1/9$. The remaining diagonal probabilities are then $P_{AA}=2/3$ and $P_{BB}=8/9$, because each row sums to one. The construction uses one free transition probability and the target masses. It does not require the other off-diagonal entry to be guessed and then checked. On a larger finite state space the same idea applies edge by edge, with the row-sum constraints still to be satisfied. An assignment of flows that cannot be realised by a row-stochastic matrix is not a transition kernel, however neatly the products match on paper.

The three-state deterministic cycle is the standard demonstration that stationarity does not imply detailed balance. The uniform distribution $\pi=(1/3,1/3,1/3)$ is stationary for the cycle that sends $1\to 2\to 3\to 1$, because each state receives the entire mass of its unique predecessor and that mass equals $1/3$. The forward flow on each edge is $1/3$ and the reverse flow is $0$. Global balance holds. Detailed balance fails. Reversing time on this chain follows the cycle backwards. The forward chain and the reversed chain are different.{{cite:grinstead_snell1997}} (§11.5, p. 463, reversibility and reverse transition matrices)

### Uniqueness, convergence and mixing
A unique stationary distribution is sometimes inferred from detailed balance alone. The two-state identity matrix has detailed balance for every $\pi$ and has infinitely many stationary distributions. Uniqueness needs a communication condition, typically irreducibility on a finite state space. Convergence of the law of $X_t$ needs a further aperiodicity condition, or a statement about averages along the path rather than about the distribution at a fixed large time. The balance proof in the statement is one summation. It does not mention the period.

Simulation adds a practical version of the same distinction. A Metropolis–Hastings kernel can be shown to satisfy detailed balance with the desired posterior, and the chain can still mix slowly, or fail to reach a mode that the proposal never proposes. Invariance says that the target is an equilibrium. It does not say that a finite run has arrived there. Diagnostics of a run are checks on the trajectory. They are not a substitute for the algebraic check that the acceptance probability was derived from the target and the proposal in both directions.{{cite:hastings1970}} (§§2.1–2.2)

## Generalizations — Reversibility and continuous time
Reversibility is the path-wise form of the pairwise flow identity. If every edge balances, every finite path has the same stationary probability as its reversal. The cycle shows a stationary chain that is not reversible. Continuous-time chains use the same idea with rates in place of transition probabilities: $\pi_i q_{ij}=\pi_j q_{ji}$. The summation that turns local balance into global balance is unchanged. Birth–death processes on a line satisfy detailed balance for their stationary distribution when one exists, because the only edges run between neighbours and the global balance equations reduce to those neighbour equalities. A queue length that drifts to infinity has no stationary probability distribution for those equations to solve. The algebraic implication from detailed balance to stationarity still requires a probability vector, not merely a set of nonnegative weights.
