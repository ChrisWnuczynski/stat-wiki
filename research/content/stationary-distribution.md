## Motivating example
A weather model predicts tomorrow from today's weather. Even when today's forecast is known, a planner may want the fraction of days expected to be rainy over a long period. A stationary distribution answers the balance question: if the proportions of sunny and rainy days already have those values, applying the transition rule leaves them unchanged. For the weather chain in the definition, sunny days send probability mass to rain at rate $0.2\pi_S$ and rainy days return it at rate $0.3\pi_R$; equality leads to the answer $(0.6,0.4)$. This balance describes a distribution over days, not an assertion that each day has the same weather.{{cite:levin_peres2017}} (§1.5.1, eqs. 1.14–1.15)

## Intuition
Imagine a unit of probability spread among the states. Each row of $P$ tells how the mass currently at one state is redistributed. At stationarity every state receives as much total probability mass as it gives up, although individual paths keep moving. That is why a stationary distribution is sometimes called an *invariant* distribution. The equation concerns the entire distribution: a state need not stay put, and successive states need not be independent.{{cite:levin_peres2017}} (§1.5.1, eqs. 1.14–1.15)

This fixed-point idea also explains why a stationary law and a limiting law must be distinguished. An irreducible chain on a finite set has one stationary law. If it is periodic, a chain started at one state can keep cycling instead of converging to that law at each time. Aperiodicity supplies the extra condition for convergence from every starting state.{{cite:levin_peres2017}} (§1.3, p. 8; §1.5.1; §4.3, pp. 52–53)

## Definition
For a finite or countable state space $S$, write $P(i,j)=\Pr(X_{n+1}=j\mid X_n=i)$ and let $\pi$ be a probability row vector. The stationary equation is $\pi=\pi P$, meaning $\pi_j=\sum_{i\in S}\pi_iP(i,j)$ at every destination $j$. The entries of $\pi$ must be nonnegative and sum to one; a nonzero eigenvector of $P$ alone is not yet a probability distribution. The row-vector convention matters because row distributions evolve by multiplication on the right: $\mu_n=\mu_0P^n$.{{cite:levin_peres2017}} (§1.5.1, eqs. 1.14–1.15)

If $X_0\sim\pi$, then $X_n\sim\pi$ at every time. This describes stationary *one-time marginals*. In a time-homogeneous Markov chain it also makes the joint law invariant under shifts of time, but it does not remove dependence between adjacent states. A chain that stays where it is with high probability can have a stationary marginal while retaining strong serial dependence.{{cite:levin_peres2017}} (§1.5.1, eq. 1.14)

## Properties
On a finite irreducible chain a stationary distribution exists, is unique and has positive mass at every state. Its state weights have a recurrence interpretation: $\pi_i=1/\mathbb E_iT_i^+$, where $T_i^+$ is the first positive return time to $i$. A state visited, on average, once every four steps therefore has stationary weight one quarter. For a finite chain with several closed communicating classes, stationary distributions are mixtures of the stationary laws within those classes; transient states receive zero stationary weight.{{cite:levin_peres2017}} (§1.5, pp. 12–13 and p. 13; §1.7, pp. 16–17)

Finding a stationary law does not always require solving the full linear system. If $P$ is doubly stochastic on a finite state space, each of its columns as well as its rows sums to one, so the uniform distribution is stationary. For a simple random walk on a finite undirected graph, state $i$ instead has weight proportional to its degree: $\pi_i=\deg(i)/(2|E|)$. A hub receives more visits because more edges lead into it. Neither shortcut says how quickly the chain approaches stationarity.{{cite:levin_peres2017}} (§1.5.1, pp. 9–10; §1.6, p. 14)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Suppose $\pi P=\pi$. Then induction gives $\pi P^n=\pi P^{n-1}P=\pi P=\pi$ for every positive integer $n$. Conversely, if $X_0$ has law $\pi$, its one-step law is $\pi P$, so equality at the first step requires the stationary equation. For a finite doubly stochastic matrix with $m$ states, put $u_i=1/m$. Then $(uP)_j=m^{-1}\sum_iP(i,j)=1/m=u_j$, proving uniform stationarity. For an undirected graph, put $\pi_i=\deg(i)/(2|E|)$; then $\pi_iP(i,j)=1/(2|E|)$ on an edge and zero off it, which is symmetric in $i,j$. Summing these detailed-balance equalities over $i$ gives $(\pi P)_j=\pi_j$. This also proves directly that detailed balance is sufficient for stationarity. On nonnegative integers with deterministic transition $n\mapsto n+1$, stationarity would require $\pi_0=0$ and then $\pi_n=\pi_{n-1}=0$ for every $n>0$, contradicting total mass one.{{cite:levin_peres2017}} (§1.5.1, pp. 9–10; §1.6, p. 13 and p. 14)
:::
:::

## Statistical use — Equilibrium and Monte Carlo sampling
In a stochastic-process model, $\pi$ describes the long-run share of visits to each state when the chain can move throughout a finite state space. In Markov chain Monte Carlo the direction of the problem is reversed: choose transitions so that a desired target distribution is stationary, then run the chain long enough for its current law to be close to that target. Establishing $\pi P=\pi$ confirms the target but does not by itself determine an adequate run length. The starting state, periodicity and rate of mixing still matter.{{cite:levin_peres2017}} (§1.5.1; §3.1, sampling with Markov chains; §4.3, pp. 52–53)

Take the deterministic chain $0\to1\to0$. Its stationary distribution is $(1/2,1/2)$, but from state $0$ the probability of state $0$ alternates between one and zero; no stepwise limiting distribution exists. Take instead $P=I$ on two states. Every distribution is stationary, so the equation does not identify a unique answer and the starting law persists. On the nonnegative integers, a deterministic transition $n\mapsto n+1$ has no stationary probability law, as the proof shows. These cases fail for different reasons: periodicity, reducibility and movement without return on an infinite space.{{cite:levin_peres2017}} (§1.3, periodicity; §1.7, stationary laws on closed classes)

## Worked example
Suppose a machine can be in states $0$, $1$ or $2$, with transition matrix

$$
P=\begin{pmatrix}0.5&0.5&0\\0.25&0.25&0.5\\0&0.5&0.5\end{pmatrix}.
$$

Only neighbouring states communicate. Balance across the $0$–$1$ edge gives $0.5\pi_0=0.25\pi_1$, so $\pi_1=2\pi_0$. Balance across the $1$–$2$ edge gives $0.5\pi_1=0.5\pi_2$, so $\pi_2=\pi_1$. Normalising $\pi_0+\pi_1+\pi_2=1$ yields $\pi=(1/5,2/5,2/5)=(0.2,0.4,0.4)$. Multiplication verifies every coordinate: $(\pi P)_0=0.2(0.5)+0.4(0.25)=0.2$, $(\pi P)_1=0.2(0.5)+0.4(0.25)+0.4(0.5)=0.4$, and $(\pi P)_2=0.4(0.5)+0.4(0.5)=0.4$.

Starting in state $0$ instead gives next-step law $(0.5,0.5,0)$ and two-step law $(0.375,0.375,0.25)$. The stationary weights are therefore not claims about the first few steps from this start. Self-loops make the irreducible finite chain aperiodic, so its stepwise laws eventually approach $(0.2,0.4,0.4)$.{{cite:levin_peres2017}} (§1.5.1, stationary equations; §4.3, pp. 52–53)

**Your turn.** A two-state chain has $P=\begin{pmatrix}0.6&0.4\\0.2&0.8\end{pmatrix}$. Find its stationary distribution, then check it by multiplying by $P$.

::: {.callout-tip collapse="true" title="Answer"}
Across the two states, $0.4\pi_0=0.2\pi_1$, so $\pi_1=2\pi_0$ and $\pi=(1/3,2/3)$. Indeed, $(1/3,2/3)P=(0.6/3+0.4/3,\,0.4/3+1.6/3)=(1/3,2/3)$. The second coordinate is larger because the chain moves from state $0$ to state $1$ twice as readily as it moves back.
:::

## Common misconceptions
“Stationary” does not mean the chain stops moving; it means its probability distribution does not change after a step. A stationary distribution is not automatically the limit from a chosen starting state: a deterministic cycle has a uniform stationary distribution but keeps rotating. It need not be uniform either; on a graph with unequal degrees, high-degree vertices have larger weights. Nor does stationarity require detailed balance: a directed cycle can maintain equal mass at all states while probability flows around it in one direction.{{cite:levin_peres2017}} (§1.3, p. 8; §1.5.1, pp. 9–10; §1.6, p. 14)

## Assumptions and limits — When the distribution does not settle
A finite irreducible chain has one stationary distribution. If the chain is periodic, that distribution still solves the balance equation, but the one-step law can keep alternating and never converge to it. An infinite state space can fail to have any stationary distribution.

## Connections
The [transition matrix](transition-matrix.qmd) advances a distribution, while the [limiting distribution](limiting-distribution.qmd) describes convergence from a start. [Detailed balance](detailed-balance.qmd) is a convenient sufficient test for a candidate stationary law. [Irreducibility](irreducible-markov-chain.qmd) supplies uniqueness in finite chains, and [aperiodicity](aperiodic-markov-chain.qmd) supports stepwise convergence. For [Metropolis–Hastings](metropolis-hastings-update.qmd), constructing the target as a stationary distribution is the basis of the sampling algorithm.{{cite:levin_peres2017}} (§§1.5–1.6; §3.2; §4.3)

## History
Markov introduced the dependent sequences that bear his name in work published in 1906; the stationary equation later became a central way to describe their long-run behaviour. That work was presented to the Kazan mathematical society and became part of the theory of random processes. Modern treatments separate the fixed-point question from convergence and use the same invariant-distribution idea to design Monte Carlo samplers.{{cite:levin_peres2017}} (Ch. 1 Notes, p. 19; §1.5.1; §3.1){{cite:dodge2008}} (pp. 330–331, “Markov, Andrei Andreevich”)
