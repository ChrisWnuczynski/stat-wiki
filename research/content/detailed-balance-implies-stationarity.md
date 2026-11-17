## Motivating example — Construct local flows instead of solving a global system
A Markov chain simulation often starts with a desired equilibrium distribution and needs transition probabilities that preserve it. Solving every stationarity equation at once can be inconvenient. Detailed balance instead matches the probability flow along each pair of opposite transitions. Those local equalities provide a direct sufficient condition for the desired distribution to be stationary.{{cite:hastings1970}} (§2.2, pp. 99–100)

## Statement
Let $P$ be a row-stochastic transition matrix on a finite or countable state space, and let $\pi$ be a probability vector. If $\pi_iP_{ij}=\pi_jP_{ji}$ for every pair of states, then $\pi P=\pi$. The assumption that $\pi$ sums to one distinguishes a stationary probability distribution from a merely invariant measure. In an infinite state space, an unnormalisable set of balance weights does not give a stationary probability vector.{{cite:grinstead_snell1997}} (§11.5, p. 463, time reversal and reversible chains)

## Proof
For a fixed destination state $j$, sum the detailed-balance equalities over all origins $i$:
$$ (\pi P)_j=\sum_i\pi_iP_{ij}=\sum_i\pi_jP_{ji}=\pi_j\sum_iP_{ji}=\pi_j.$$
The last sum is over row $j$ of $P$, and equals one. Nonnegative terms justify the same summation in a countable state space. This proof neither uses nor establishes irreducibility or aperiodicity. It only establishes preservation of $\pi$ after a transition.{{cite:hastings1970}} (§2.2, reversibility and the stationary distribution)

## Key results — Reversibility imposes more than equilibrium
At stationarity, $\Pr(X_t=i,X_{t+1}=j)=\pi_iP_{ij}$. Detailed balance makes that pair probability unchanged when time is reversed. More generally, multiplying the pairwise equalities along a finite path shows that the stationary path and its reversal have equal probabilities. A stationary chain can nevertheless have net circulation, in which case it is not reversible. Stationarity and reversibility are therefore different structural properties.{{cite:grinstead_snell1997}} (§11.5, p. 463, reverse chains)

## Worked example — A two-state chain
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
