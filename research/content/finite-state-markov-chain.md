## Motivating example

A machine is working or failed at the end of each day. Its chance of tomorrow's condition depends on today's condition, while the records from earlier days need not enter the next-step rule separately. A finite-state Markov chain represents those transitions in a small table. Repeated multiplication of that table answers short-term questions, and under additional conditions a stationary distribution describes the share of time spent in each condition.{{cite:levin_peres2017}} (§§1.1, 1.5, pp. 2–10)

## Intuition

The state is a summary sufficient for predicting the *next* state under the model. A row of the transition matrix lists all possible destinations from one current state; because those destinations exhaust the possibilities, its entries sum to one. Multiplying a current distribution row vector by $P$ averages over the uncertain current state. Multiplying again averages over the next one, so $P^n$ collects probabilities across all $n$-step paths. This is why matrix multiplication, rather than a list of every path, becomes the main computational tool.{{cite:levin_peres2017}} (§1.1, pp. 2–4, matrix orientation and Chapman–Kolmogorov)

## Definition

For finite state set $E$, the Markov condition is an equality of conditional next-state laws given a positive-probability history. In a *time-homogeneous* chain the entries $P_{ij}$ do not vary with time, making one stochastic matrix sufficient for all steps. Without homogeneity, the Markov property can still hold, but a sequence of matrices $P_0,P_1,\ldots$ replaces the single power $P^n$. The finite state space may describe weather, machine states or a deliberately discretized population; finiteness alone implies neither independence across time nor convergence to equilibrium.{{cite:levin_peres2017}} (§1.1, pp. 2–4)

## Properties

The $n$-step probability of reaching $j$ from $i$ is $(P^n)_{ij}$. Its composition law, $P^{m+n}=P^mP^n$, sums over the intermediate state after $m$ steps. A row distribution $\mu$ becomes $\mu P^n$ after $n$ steps. A stationary row distribution $\pi$ solves $\pi P=\pi$, so starting with $\pi$ keeps the same distribution at every later time. These are distributional statements; one simulated path can keep changing even when its law is stationary.{{cite:levin_peres2017}} (§§1.1, 1.5, pp. 2–4, 9–10)

$(P^n)_{ij}$ is the probability of occupying $j$ at the single time $n$, which is not the probability of having visited $j$ at least once by then, and not the probability that the first visit falls at that time. On the working-or-failed machine below, start from working, take $j$ to be failed, and take $n=2$. The one-time occupancy is $0.16$. The probability of ever visiting failed by time $2$ is $0.19$, split into a first hit at step $1$, which is $0.10$, and a first hit exactly at step $2$, which is $0.09$.{{cite:levin_peres2017}} (§1.1, pp. 2–4, $n$-step probabilities)

An irreducible finite chain has a unique stationary distribution, but its rows need not converge to it. The long-run time average still converges to $\pi$ when the chain is periodic: the share of steps spent in each state settles. A deterministic two-state alternation is irreducible and periodic. Its time averages settle at $(1/2,1/2)$ from either start. Started in one state, the one-time law oscillates; started at $\pi=(1/2,1/2)$, that same one-time law is already constant. Aperiodicity is what makes every row of $P^n$ converge to $\pi$, equivalently the one-time law from every starting state. It is not a requirement on an initial distribution that is already $\pi$. With aperiodicity, the rows of $P^n$ approach the unique stationary distribution; the six-stone example shows this numerically, whereas the figure of an infinite-state random walk marks the boundary of the finite-state result. {{cite:levin_peres2017}} (§§1.3, 1.5, pp. 7–8; Thm. C.1, pp. 390–391, time averages)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Conditional on $X_m=k$, the Markov rule gives $\Pr(X_{m+n}=j\mid X_0=i,X_m=k)=(P^n)_{kj}$. Summing over $k$ proves $(P^{m+n})_{ij}=\sum_k(P^m)_{ik}(P^n)_{kj}$ and hence the matrix identity and $\mu P^n$ rule. Row sums of $P$ equal one by summing its conditional probabilities over every destination.{{cite:levin_peres2017}} (§1.1, pp. 2–4)

To see existence of a stationary distribution on a finite state set, take any initial row $\mu$ and Cesàro averages $\nu_N=N^{-1}\sum_{k=0}^{N-1}\mu P^k$. Compactness of the probability simplex gives a convergent subsequence; $\nu_NP-\nu_N=(\mu P^N-\mu)/N\to0$, so any limit $\pi$ is stationary. In an irreducible chain it is positive everywhere: if $\pi_j=0$, stationarity forces $\pi_i=0$ at every predecessor of $j$, and paths from all states then contradict total mass one. To prove uniqueness, let $\rho$ be another stationary distribution and put $c=\min_i\rho_i/\pi_i$. Then $\rho-c\pi$ is nonnegative and stationary but vanishes at some state. The same predecessor argument forces it to vanish everywhere; normalization gives $c=1$ and $\rho=\pi$. {{cite:levin_peres2017}} (§1.5, pp. 9–12, stationary existence and uniqueness)

For an irreducible aperiodic finite chain, a sufficiently large common power $P^r$ has all entries positive: irreducibility supplies connecting paths, and aperiodic return paths supply all sufficiently large added lengths. Choose $\delta>0$ with $P^r(i,j)\geq\delta\pi_j$ for every pair. Writing $P^r=\delta\Pi+(1-\delta)Q$, where every row of $\Pi$ equals $\pi$ and $Q$ is stochastic, shows that repeated $r$-step updates contract the distance between any distribution and $\pi$ by at least a factor $1-\delta$. Thus $\mu P^n\to\pi$ for every start. If $\rho$ were another stationary distribution, the same contraction applied to $\rho$ and $\pi$ would force $\rho=\pi$. {{cite:levin_peres2017}} (§1.3, positive-power proposition; §4.3, convergence proof)
:::
:::

## Statistical use — Simulation and long-run behavior

To simulate a path, sample the next state from the row indexed by the present state and repeat. One path illustrates possible behavior, while $\mu P^n$ gives an exact distribution under the chosen matrix. The stationary distribution can be computed by solving $\pi P=\pi$ with entries summing to one, then compared with long-run proportions in a simulation if the chain is irreducible. Apparent agreement over a short run cannot establish that transition probabilities are correctly specified or remain constant over time.{{cite:levin_peres2017}} (§§1.1, 1.5, pp. 2–4, 9–12)

If a repair policy changes on weekends, the chance of leaving the failed state depends on the day, so a constant $P$ misses the time variation even if the process is Markov after calendar time is included. If wear accumulates but the state records only working or failed, tomorrow's failure risk may depend on how long the machine has run; enlarging the state to include age can restore a Markov description. A reducible chain with two absorbing states has many stationary mixtures, and a deterministic alternation oscillates rather than converging. These give concrete reasons to check both model state and convergence assumptions.{{cite:levin_peres2017}} (§§1.1, 1.3, 1.5, pp. 2–10)
## Worked example

Suppose states are working and failed, in that order, with $P=\begin{pmatrix}0.9&0.1\\0.3&0.7\end{pmatrix}$. Starting working, the probability of working two days later is $0.9^2+0.1(0.3)=0.84$: either the machine works on both steps or fails and is repaired. At stationarity the flow from working to failed balances the reverse flow, so $0.1\pi_W=0.3\pi_F$ and $\pi_W+\pi_F=1$. Thus $\pi=(0.75,0.25)$. A high two-day working probability and a lower long-run working fraction answer different questions: the latter accounts for repeated failures and repairs indefinitely.{{cite:levin_peres2017}} (§§1.1, 1.5, pp. 2–4, 9–10)

**Your turn.** With the same matrix, start in the failed state. What is the probability of working two days later, and what distribution results after one day?

::: {.callout-tip collapse="true" title="Answer"}
After one day the distribution is the failed-state row $(0.3,0.7)$. The two-step working probability is $0.3(0.9)+0.7(0.3)=0.48$. Its complement gives a failed probability of $0.52$. These are conditional predictions from a failed start, whereas the stationary $(0.75,0.25)$ is unchanged after every step.
:::

## Common misconceptions

The Markov property concerns conditioning on the current state; it does not say consecutive states are independent. A stationary distribution is an invariant *law*, not a fixed state in which one path stays. Irreducibility alone guarantees one stationary law in the finite case but does not make $P^n$ converge, as a two-cycle shows. Finally, finite-state conclusions should not be carried over to the unrestricted random walk on the integers shown in the figure below; that chain has an infinite state set.{{cite:levin_peres2017}} (§§1.1, 1.3, 1.5, 4.3, pp. 2–10, 52–53)

## Connections

The [Markov property](markov-property.qmd) specifies the conditional independence rule. A [transition matrix](transition-matrix.qmd) implements it for a finite homogeneous chain. [Irreducibility](irreducible-markov-chain.qmd), [aperiodicity](aperiodic-markov-chain.qmd), and the [stationary distribution](stationary-distribution.qmd) explain whether a limiting law exists; [Markov chain Monte Carlo](../notes/bayes-04-mcmc.qmd) uses long chain runs to approximate expectations under a designed stationary law.{{cite:levin_peres2017}} (§§1.1, 1.3, 1.5, 4.3)

## History

Andrei Markov's work on dependent quantities gave his name to chains of this kind; Dodge's biographical entry notes that his investigations helped develop the modern theory of dependent random processes. Later expositions made transition matrices, stationary laws and convergence conditions the standard finite-state toolkit. The distinction between a stationary law and convergence to it remains essential in modern accounts of Markov chains.{{cite:dodge2008}} (pp. 330–331, Markov entry){{cite:levin_peres2017}} (Chs. 1, 4)
