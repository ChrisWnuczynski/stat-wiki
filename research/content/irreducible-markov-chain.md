## Motivating example
Imagine a service system with three operating modes: idle, busy, and recovery. A transition from idle straight to recovery may be impossible, yet a busy period can intervene. The relevant question for long-run behaviour is whether *some finite route* connects each pair of modes, not whether every direct transition has positive probability. If all modes can communicate, the model cannot permanently split into separate operating regimes. This is what irreducibility detects.{{cite:levin_peres2017}} (§1.3, Irreducibility)

## Intuition
Draw an arrow from state $i$ to state $j$ whenever the one-step transition probability $P_{ij}$ is positive. For a finite chain, irreducibility means that this directed graph is strongly connected: for every ordered pair, a directed path leads from the first state to the second. The path may contain many steps and may revisit states. Multiplying transition probabilities along a particular positive-probability path gives a positive probability of following it; conversely, a positive entry of $P^n$ must contain at least one path whose product is positive. This is why graph reachability and probabilistic accessibility give the same test.{{cite:levin_peres2017}} (§1.3, Irreducibility)

The word *irreducible* refers to the whole specified state space. If a model includes a state that is mathematically possible but cannot be reached from the states actually used, irreducibility still fails on that stated space. One can sometimes restrict attention to a closed communicating class, but that changes which chain is under discussion.{{cite:levin_peres2017}} (§1.7, Classifying the States of a Markov Chain)

## Definition
Write $P^n_{ij}=\Pr(X_n=j\mid X_0=i)$ for a time-homogeneous discrete-time chain. State $j$ is *accessible* from $i$ if $P^n_{ij}>0$ for at least one integer $n\geq0$. States $i$ and $j$ *communicate* if each is accessible from the other. A chain is **irreducible** if every pair of states communicates. The $n=0$ case makes each state accessible from itself, since $P^0=I$.{{cite:levin_peres2017}} (§§1.3, 1.7)

Communication partitions the states into equivalence classes. The entire chain is irreducible precisely when there is one such class. In a finite chain with several classes, at least one class is closed, meaning there is no route out of it. Different closed classes can carry different stationary laws, so there is no single equilibrium determined by the transition rule alone.{{cite:levin_peres2017}} (§1.7, Classifying the States of a Markov Chain)

## Properties — What irreducibility buys
On a **finite** state space, an irreducible chain has one stationary probability vector $\pi$, every component of which is positive. The equation $\pi P=\pi$ says that starting with this distribution leaves it unchanged after one transition. The same stationary weight can be interpreted as the reciprocal of a state's mean return time: states visited frequently have shorter expected waits between visits. These claims depend on finiteness; a countably infinite irreducible chain need not have a normalisable stationary probability.{{cite:levin_peres2017}} (§1.5.3, stationary-law construction; §1.7)

Irreducibility alone does not say that the distribution at time $n$ approaches $\pi$. For that one-time limit, the finite chain must also be *aperiodic*, so return times are not trapped on a repeating schedule. Under both conditions, $P^n_{ij}\to\pi_j$ for every starting state $i$ and destination $j$. Thus the stationary equation, uniqueness of its probability solution, and convergence toward that solution are three separate claims with different hypotheses.{{cite:levin_peres2017}} (§4.3, convergence theorem)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For finite $n$, matrix multiplication writes
$$
(P^n)_{ij}=\sum_{i_1,\ldots,i_{n-1}}P_{i i_1}P_{i_1 i_2}\cdots P_{i_{n-1}j}.
$$
All summands are nonnegative. Therefore $(P^n)_{ij}>0$ exactly when at least one length-$n$ directed path from $i$ to $j$ has all its edge probabilities positive. This proves the graph criterion for irreducibility.

Accessibility is reflexive because $P^0=I$. It is transitive because if $(P^m)_{ij}>0$ and $(P^n)_{jk}>0$, then the $j$ summand in $(P^{m+n})_{ik}=\sum_\ell(P^m)_{i\ell}(P^n)_{\ell k}$ is positive. Mutual accessibility is consequently reflexive, symmetric by definition, and transitive. It is an equivalence relation, so its classes partition the state space.{{cite:levin_peres2017}} (§§1.3, 1.7)
:::
:::

## Statistical use — Checking a sampler's reach
In Markov chain Monte Carlo, a transition rule may preserve the intended target distribution while failing to explore all regions of positive target mass. A sampler that only changes one coordinate at a time, for example, must be able to reach every allowed configuration through a sequence of allowed changes. A zero-probability barrier can isolate separate communicating classes. Checking irreducibility identifies this structural failure before interpreting a long run as a sample from the entire target. Aperiodicity and appropriate recurrence conditions remain separate requirements for convergence in the state spaces to which they apply.{{cite:levin_peres2017}} (§§1.3, 4.3)

## Worked example
Consider the hypothetical three-mode chain with states $1,2,3$ and row-stochastic transition matrix
$$
P=\begin{pmatrix}
0&1&0\\
1/2&0&1/2\\
1/2&1/2&0
\end{pmatrix}.
$$
State $1$ cannot jump directly to $3$, but it can follow $1\to2\to3$ with probability $1(1/2)=1/2$. State $3$ can reach $1$ in one step with probability $1/2$. The edges $1\to2$, $2\to3$, and $3\to1$ form a directed cycle through all three states, so every state can reach every other: the chain is irreducible. Indeed,
$$
P^2=\begin{pmatrix}1/2&0&1/2\\1/4&3/4&0\\1/4&1/2&1/4\end{pmatrix}.
$$
The zero in position $(1,2)$ of $P^2$ does not matter; irreducibility asks for *some* step count for each pair.{{cite:levin_peres2017}} (§1.3, Irreducibility)

For an equilibrium calculation, solve $\pi P=\pi$ together with $\pi_1+\pi_2+\pi_3=1$. The result is $\pi=(1/3,4/9,2/9)$; multiplication checks that the inflow to state $3$ is $(1/2)(4/9)=2/9$. The chain can return to state $1$ in two steps through $2$ or in three steps through $2,3$. Since $\gcd(2,3)=1$, its period is one, and the finite-chain convergence theorem applies. Starting from any of its three modes, the distribution eventually approaches this same $\pi$.{{cite:levin_peres2017}} (§1.3, periods; §4.3, convergence theorem)

**Your turn.** In the same matrix, find the probability of moving from state $2$ to state $2$ in exactly two steps. Name the intermediate states that contribute, and explain whether this number alone proves irreducibility.

::: {.callout-tip collapse="true" title="Answer"}
The two possible two-step returns are $2\to1\to2$, with probability $(1/2)(1)=1/2$, and $2\to3\to2$, with probability $(1/2)(1/2)=1/4$. Thus $(P^2)_{22}=3/4$. A return to one state proves only that one state can reach itself in two steps; irreducibility needs a route for every ordered pair of states.
:::

## Common misconceptions
Irreducible does not mean every entry of $P$ is positive: the worked chain has several zero one-step entries. It also does not mean that a particular power $P^n$ has all positive entries: the worked $P^2$ still contains zeros. Irreducible does not imply aperiodic; a deterministic alternation between two states has full mutual reachability but repeats with period two. Finally, a stationary vector is not the same as a limiting distribution: the alternating chain has the former, while its distributions oscillate forever.{{cite:levin_peres2017}} (§1.3, periodicity; §4.3, convergence theorem)

## Assumptions and limits — When the conclusion changes
An absorbing state gives an immediate counterexample to irreducibility if any other state is present: once entered, the chain cannot reach the other states. A chain with two absorbing states has many stationary distributions, one for each mixture of the two point masses. For an infinite-state counterexample to the finite equilibrium claim, the simple symmetric random walk on all integers is irreducible but has no stationary *probability*: its stationary equations have a constant solution, which cannot be summed to one over infinitely many integers. The integer walk and the finite three-mode model therefore require different long-run statements.{{cite:levin_peres2017}} (§1.7, Classifying the States of a Markov Chain; §1.5.3)

## Connections
[Communicating classes](communicating-classes.qmd) are the pieces into which a reducible chain separates. [Aperiodic Markov chains](aperiodic-markov-chain.qmd) add the timing condition needed for convergence on a finite state space. [Stationary distributions](stationary-distribution.qmd) solve the equilibrium equation, while [transition matrices](transition-matrix.qmd) encode the routes that determine irreducibility. In an MCMC application, [detailed balance](detailed-balance.qmd) can establish stationarity, but reachability must still be checked for the chosen transition rule.{{cite:levin_peres2017}} (§§1.3, 1.5, 4.3)

## History
Andrei Markov introduced dependent sequences into probability at the beginning of the twentieth century. The later language of communicating classes and irreducibility makes explicit which transitions allow one dependent process to explore its whole state space. Dodge's biographical account connects Markov's work on chains with the development of the modern study of random processes.{{cite:dodge2008}} (pp. 330–331, “Markov, Andrei Andreevich”)
