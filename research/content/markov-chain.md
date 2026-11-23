## Motivating example
A device moves among operating states as it is monitored each minute. To predict the next minute, an engineer might need only its present state, provided that state records everything relevant to the transition rule. If the same rule applies at every minute, a row of transition probabilities tells how it may move next, and repeated application gives probabilities several minutes ahead. This is the appeal of a Markov chain: a long, dependent history can sometimes be summarised by a sufficiently informative current state.{{cite:levin_peres2017}} (§1.1, pp. 2–3, Markov Chains)

## Intuition
The Markov property is about *conditional* prediction. Once the present state is known, earlier states do not change the conditional distribution of the next one. It does not say that consecutive states are independent: the present state can exert a strong influence. It also depends on how the state is defined. A queue length may be adequate for a memoryless arrival-and-service model, while a machine whose failure risk grows with elapsed time in service may need that elapsed time included in its state.{{cite:levin_peres2017}} (§1.1, pp. 2–3, Markov property)

A time-homogeneous chain reuses one transition rule. Writing its possible moves as arrows makes structural questions visible: can all states be reached, can the chain get trapped, and can it oscillate on a fixed schedule? These are separate from the Markov property itself. A chain can have the one-step memory rule while being reducible, periodic, or without a stationary probability on an infinite state space.{{cite:levin_peres2017}} (§§1.1, 1.3, 1.5)

## Definition
On a countable state space $S$, a sequence $X_0,X_1,\ldots$ is a **discrete-time Markov chain** if, whenever the conditioning event has positive probability,
$$
\Pr(X_{t+1}=j\mid X_t=i,X_{t-1},\ldots,X_0)
=\Pr(X_{t+1}=j\mid X_t=i).
$$
That displayed equality is the countable case. When the state space is finite and the chain is time-homogeneous, the right-hand side is a matrix entry $P_{ij}$ and every row is a probability distribution: $P_{ij}\ge0$ and $\sum_jP_{ij}=1$.{{cite:levin_peres2017}} (§1.1, pp. 2–3, finite transition matrix)

On a measurable space the one-step law is a kernel, not an equality of atom probabilities. For each measurable set $A$, the map $x\mapsto P_t(x,A)$ is measurable and $\Pr(X_{t+1}\in A\mid X_0,\ldots,X_t)=P_t(X_t,A)$ almost surely. The matrix is that kernel when $S$ is finite. Using one kernel at every time is time-homogeneity; powers of a single kernel require it. The initial distribution and the kernel together specify the finite-dimensional laws. The chain can start from a fixed state or from a random initial distribution; neither choice changes the transition rule.

## Properties — From one step to many
If $\mu_0$ is written as a row vector, the state distribution after one step is $\mu_1=\mu_0P$ and after $n$ steps is $\mu_n=\mu_0P^n$. The entry $(P^n)_{ij}$ is the chance of being in $j$ after $n$ steps when starting from $i$. In particular, to find a two-step probability one sums over the intermediate state, not merely the most likely route. This is the Chapman–Kolmogorov rule:
$$
(P^{m+n})_{ij}=\sum_{k\in S}(P^m)_{ik}(P^n)_{kj}.
$$
The sum displayed above is Chapman–Kolmogorov on a countable state space.{{cite:levin_peres2017}} (§1.1, pp. 2–4, finite transitions) On a measurable space the matching identity is an integral against the $n$-step kernel, and that kernel is a power of one transition kernel only when the chain is time-homogeneous.

A stationary distribution $\pi$ satisfies $\pi P=\pi$; starting in it leaves the one-time distribution unchanged. Whether it exists, is unique, or attracts distributions from arbitrary starts requires additional conditions. For a finite irreducible aperiodic chain it is unique and $P^n$ approaches rows equal to $\pi$. A deterministic two-state alternation is Markov and irreducible, and has a stationary vector, but its one-time distribution never settles when started from one state.{{cite:levin_peres2017}} (§1.5, Stationary Distributions; §4.3, convergence theorem)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For a particular path $i_0,i_1,\ldots,i_n$, the chain rule of probability and the Markov property give
$$
\Pr(X_0=i_0,\ldots,X_n=i_n)=\mu_0(i_0)\prod_{r=0}^{n-1}P_{i_ri_{r+1}}.
$$
Summing these path probabilities over possible intermediate states yields each entry of $P^n$. To obtain the Chapman–Kolmogorov identity, condition on $X_m=k$ when starting from $i$. The Markov property makes the probability of reaching $j$ in the following $n$ steps equal to $(P^n)_{kj}$. Therefore
$(P^{m+n})_{ij}=\sum_k\Pr(X_m=k\mid X_0=i)(P^n)_{kj}=\sum_k(P^m)_{ik}(P^n)_{kj}$.
The distribution formula $\mu_n=\mu_0P^n$ follows by averaging the $i$th rows over $\mu_0(i)$.{{cite:levin_peres2017}} (§1.1, Markov Chains)

The following calculation is the infinite-state case. For the simple symmetric walk on all integers, a stationary probability would satisfy $\pi_j=(\pi_{j-1}+\pi_{j+1})/2$ at every integer $j$. Thus successive differences $\pi_{j+1}-\pi_j$ are constant. Nonnegativity for arbitrarily large positive and negative $j$ forces that constant to be zero, leaving $\pi_j$ the same at every integer. A positive constant cannot sum to one, and the zero constant is not a probability, so no stationary probability exists.
:::
:::

## Statistical use — Specifying and checking a state model
To use a chain for forecasting or simulation, define states so the next-step rule is plausible given the current state. Estimate or specify each row of $P$, then compare observed transitions with its predicted probabilities. A transition matrix describes possible moves, while an initial distribution describes where the process began; confusing the two can make early forecasts wrong even if the long-run model is sound. For Markov chain Monte Carlo, the states may be parameter values rather than physical modes, and the transition rule is designed so that a desired target law is stationary. A random-walk Metropolis update is one such current-state rule; the resulting draws are generally dependent, and discarding early draws does not by itself make them independent. The Markov property alone does not certify that a run has explored its target.{{cite:levin_peres2017}} (§§1.1, 1.5, 3.1)

## Worked example
Consider a schematic traffic signal with states red ($R$), green ($G$), and yellow ($Y$). Each minute it either stays in its present colour or advances through $R\to G\to Y\to R$, according to
$$
P=\begin{pmatrix}
1/5&4/5&0\\
0&3/10&7/10\\
3/5&0&2/5
\end{pmatrix}.
$$
Starting at red, the chance of the particular path $R\to G\to Y$ is $(4/5)(7/10)=14/25=0.56$. There is no other two-step route from red to yellow, so this is also $\Pr(X_2=Y\mid X_0=R)$. Multiplying the matrix gives the full two-step distribution from red,
$$
\mu_2=(1,0,0)P^2=(1/25,\ 2/5,\ 14/25)=(0.04,\ 0.40,\ 0.56).
$$
The entries sum to one.{{cite:levin_peres2017}} (§1.1, path and matrix calculations)

**Your turn.** Find the probability of the entire path $R\to G\to Y\to R$ in three steps, and give $\Pr(X_3=R\mid X_2=Y,X_1=G,X_0=R)$.

::: {.callout-tip collapse="true" title="Answer"}
The path probability is $(4/5)(7/10)(3/5)=42/125=0.336$. Conditional on the signal being yellow at time two, the Markov rule uses only the yellow row, so the conditional probability of red next is $3/5=0.6$. The path probability includes the earlier moves; the one-step conditional probability does not.
:::

## Common misconceptions
“Memoryless given the current state” does not mean independent states: red makes green much more likely here than yellow does. A Markov chain need not be time-homogeneous; a transition rule can depend on the time index while still ignoring earlier states once the present is known. The existence of a transition matrix does not guarantee convergence to a stationary distribution, as deterministic alternation shows. And a process can appear non-Markov merely because the recorded state omits a relevant variable, such as time since the last change. These are different questions about dependence, timing, long-run behaviour, and state design.{{cite:levin_peres2017}} (§§1.1, 1.3, 1.5)

## Assumptions and limits — When a small state is inadequate
Suppose a real signal always changes after exactly three minutes in one colour. Recording only its colour leaves the chance of a change dependent on how long that colour has already lasted, so the colour sequence is not a time-homogeneous Markov chain with one row per colour. Recording both colour and elapsed duration can restore a Markov state description. In another example, a random walk on all integers is Markov but the symmetric walk has no stationary probability: its steps depend only on the current position while its distribution spreads without settling, as the proof above shows. A finite transition table and the Markov property must therefore be matched to the mechanism and the question being asked.{{cite:levin_peres2017}} (§1.1, finite chains)

## Connections
[Transition matrices](transition-matrix.qmd) store the one-step rule; [irreducible Markov chains](irreducible-markov-chain.qmd) can reach every state from every other. [Aperiodic Markov chains](aperiodic-markov-chain.qmd) avoid a fixed return-time rhythm, and [stationary distributions](stationary-distribution.qmd) are unchanged by one transition. [Markov chain Monte Carlo](../notes/bayes-04-mcmc.qmd) uses a deliberately constructed chain to explore a target law, making its structural conditions consequential for inference.{{cite:levin_peres2017}} (§§1.1, 1.3, 1.5, 3.1)

## History
Andrei Markov's early study of dependent quantities showed that the classical independence assumption was not needed for every useful probability calculation. Those dependent sequences later became a language for random processes evolving by a present-state rule. The modern transition-matrix presentation makes the rule computational: powers of one matrix produce probabilities at later times.{{cite:dodge2008}} (pp. 330–331, “Markov, Andrei Andreevich”){{cite:levin_peres2017}} (§1.1, Markov Chains)
