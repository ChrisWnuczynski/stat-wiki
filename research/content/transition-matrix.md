## Motivating example
A service system can be idle, busy, or recovering at the end of each hour. To forecast its state two hours ahead, a one-hour table is useful only if we know how to combine possible intermediate states. A transition matrix records those one-step choices; multiplying it by itself sums every route through the intervening hour. That is why the matrix is more than a compact way to list probabilities.{{cite:levin_peres2017}} (§1.1, transition matrices and paths)

## Intuition
Choose an order for the states. In a **row-stochastic** transition matrix, row $i$ is a probability distribution over the next state *given* current state $i$. Its entries cannot be negative, and each row sums to one. A zero entry rules out one particular direct move, but may still allow a move after several steps through another state. The matrix describes the rule of movement; a separate initial distribution describes where the process starts.{{cite:levin_peres2017}} (§1.1, transition matrix)

Matrix multiplication has the right shape for prediction. In $(P^2)_{ij}=\sum_kP_{ik}P_{kj}$, each term is the probability of moving from $i$ to an intermediate state $k$ and then to $j$. Summing over $k$ adds all mutually exclusive routes. Repeating this operation produces the $n$-step probabilities in $P^n$ when the same rule applies at every step. The weather example in the Definition shows how the two directions can have different probabilities even with only two states.{{cite:levin_peres2017}} (§1.1, matrix powers and paths)

## Definition
For a time-homogeneous discrete-time Markov chain on finite or countable state space $S$, write
$$
P_{ij}=\Pr(X_{t+1}=j\mid X_t=i),\qquad i,j\in S.
$$
The value does not depend on $t$. Under the row convention used here, $P_{ij}\ge0$ and $\sum_jP_{ij}=1$ for every current state $i$. If the distribution of $X_0$ is a row vector $\mu_0$, then $\mu_n=\mu_0P^n$, and $(P^n)_{ij}=\Pr(X_n=j\mid X_0=i)$. In particular $P^0=I$ represents zero transitions.{{cite:levin_peres2017}} (§1.1, definition and powers)

Some authors instead store current states in columns and use column probability vectors, writing $\mu_{t+1}=P\mu_t$. Such a matrix is the transpose of the row-convention matrix for the same chain. The probabilities are identical when all formulas use one convention consistently. A quick check before multiplying is whether the current-state probabilities live in rows or columns.{{cite:levin_peres2017}} (§1.1, row-vector convention)

## Properties — Composition and equilibrium
For nonnegative integers $m,n$, conditioning on the state after $m$ steps gives
$$
(P^{m+n})_{ij}=\sum_k(P^m)_{ik}(P^n)_{kj}.
$$
These are the Chapman–Kolmogorov equations in matrix form. Products of row-stochastic matrices remain row-stochastic, so every row of $P^n$ is again a probability distribution. The two-step weather calculation in the Definition and the worked example below are instances of the same route-summing identity.{{cite:levin_peres2017}} (§1.1, composition of transitions)

A row probability vector $\pi$ is **stationary** when $\pi P=\pi$: drawing the present state from $\pi$ leaves its distribution unchanged after one step. A chain started elsewhere may remain far from that equilibrium. Matrix powers may fail to approach a single limiting row, as a deterministic alternation shows. Whether convergence holds depends on structural features such as communicating classes and period, in addition to the entries summing to one.{{cite:levin_peres2017}} (§§1.5, 1.7, 4.3)

## Statistical use — From a model to forecasts
When transition probabilities are estimated from repeated observations, each fitted row can be read as the predicted next-state mix for that current state. Multiplying an initial distribution $\mu_0$ by $P^n$ produces a population forecast after $n$ steps; selecting a row of $P^n$ produces the forecast conditional on one known starting state. The two are different questions. A practitioner should also check whether the proposed states contain the information needed for a stable one-step rule: a process with unrecorded duration dependence may not be Markov in the recorded state alone.{{cite:levin_peres2017}} (§1.1, Markov property and transition rule)

In Markov chain Monte Carlo, the transition matrix or kernel is chosen so a desired distribution is stationary rather than estimated as a description of observed movements. The equation $\pi P=\pi$ checks invariance, while reachability and mixing determine whether a run from its chosen start actually explores that target. For a finite matrix, directed edges from positive entries expose unreachable classes; matrix powers reveal indirect routes.{{cite:levin_peres2017}} (§§1.3, 1.5, 4.3)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The Markov property gives $\Pr(X_{t+1}=j\mid X_t=i)=P_{ij}$. For two steps, condition on the intermediate state:
$$
\Pr(X_2=j\mid X_0=i)
=\sum_k\Pr(X_1=k\mid X_0=i)\Pr(X_2=j\mid X_1=k)
=\sum_kP_{ik}P_{kj}=(P^2)_{ij}.
$$
Applying the same conditioning after $m$ steps proves $(P^{m+n})_{ij}=\sum_k(P^m)_{ik}(P^n)_{kj}$ and hence the claimed power formula by induction. If $P$ and $Q$ are row-stochastic, $(PQ)_{ij}\ge0$ and $\sum_j(PQ)_{ij}=\sum_kP_{ik}\sum_jQ_{kj}=\sum_kP_{ik}=1$. Thus the matrix products used in forecasts remain valid transition matrices.

For the worked three-state matrix, $\pi=(1/3,1/3,1/3)$ satisfies $\pi P=\pi$ because each of its columns, as well as each row, sums to one. In general a row-stochastic matrix need not have column sums one, so uniform stationarity is special to this example. The deterministic two-state swap has stationary $\pi=(1/2,1/2)$, yet from a fixed state $P^{2n}=I$ and $P^{2n+1}=P$. Its distributions oscillate rather than converge; this proves the equilibrium-versus-limit distinction without appealing to a general convergence theorem.
:::
:::

## Worked example
Consider a hypothetical machine with modes $A,B,C$. From each mode it stays put with probability $1/2$ or advances to the next mode in the directed cycle $A\to B\to C\to A$ with probability $1/2$. In that state order its transition matrix is
$$
P=\begin{pmatrix}
1/2&1/2&0\\
0&1/2&1/2\\
1/2&0&1/2
\end{pmatrix}.
$$
Every row sums to one. Starting from $A$, reaching $C$ in exactly two steps requires $A\to B\to C$, with probability $(1/2)(1/2)=1/4$; the direct one-step probability is zero. Multiplication supplies the full matrix
$$
P^2=\begin{pmatrix}
1/4&1/2&1/4\\
1/4&1/4&1/2\\
1/2&1/4&1/4
\end{pmatrix}.
$$
Thus the two-step distribution from $A$ is its first row, $(1/4,1/2,1/4)$. One more multiplication gives the first row of $P^3$ as the three-step distribution $(1/4,3/8,3/8)$. Notice that the initial distribution has not vanished in only a few steps. The uniform row $\pi=(1/3,1/3,1/3)$ is stationary because each column of this particular $P$ also sums to one; a start drawn from $\pi$ would remain uniform at every step.{{cite:levin_peres2017}} (§1.1, matrix powers; §1.5, stationarity)

**Your turn.** Start in mode $C$. Find the probability of reaching $B$ in exactly two steps, name the route that contributes, and give the entire two-step distribution. Explain why the chance of $C\to B$ in one step is different.

::: {.callout-tip collapse="true" title="Answer"}
The route is $C\to A\to B$, so the probability is $(1/2)(1/2)=1/4$. The third row of $P^2$ is $(1/2,1/4,1/4)$ in the order $A,B,C$. The direct entry $P_{CB}$ is zero: the advance rule goes from $C$ to $A$, and the intermediate state creates the two-step route. A zero in $P$ can therefore become positive in $P^2$.
:::

## Common misconceptions
Rows summing to one does not mean columns do too; the weather matrix in the Definition has unequal column totals, whereas the worked cycle happens to be doubly stochastic. A one-step zero does not make a later-step move impossible; $P_{AC}=0$ but $(P^2)_{AC}=1/4$ in the worked example. A stationary vector is not automatically the long-run distribution from every start; the two-state swap in the proof is a counterexample. Finally, $P^n$ is appropriate only when the same one-step rule is used each time. These mistakes concern orientation, routes, convergence, and time dependence.{{cite:levin_peres2017}} (§§1.1, 1.5, 1.7)

## Assumptions and limits — When matrix powers mislead
Suppose a system alternates between a first-step swap matrix $S=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ and a second-step identity matrix $I$. Its two-step rule is $SI=S$, not $S^2=I$. Treating this time-varying process as if it reused one matrix predicts the wrong outcome. Even with a fixed matrix, a reducible chain can be trapped in one closed class, and a periodic chain can keep oscillating. The matrix specifies a mechanism; forecasts using its powers are only as credible as the state definition, homogeneity assumption, and supplied probabilities.{{cite:levin_peres2017}} (§§1.1, 1.3, 1.7)

## Connections
[Markov chains](markov-chain.qmd) supply the conditional-independence setting in which a transition matrix is meaningful. [Irreducibility](irreducible-markov-chain.qmd) asks whether its powers connect states, and [stationary distributions](stationary-distribution.qmd) solve its equilibrium equation. The answered bank problems [Two steps of a three-state chain](../questions/ex-prob-markov-two-steps.qmd), [A doubly stochastic matrix](../questions/ex-sp-doubly-stochastic.qmd), and [One closed class](../questions/ex-sp-closed-classes.qmd) respectively practise route sums, uniform stationarity, and how a closed class changes long-run behaviour.{{cite:levin_peres2017}} (§§1.1, 1.5, 1.7)

## History
Markov's early work made dependent sequences a subject of systematic probability calculation. A transition matrix packages a later, finite-state presentation of the conditional rule: its entries give one-step movements and its products organize longer paths. Dodge's account traces the historical role of Markov's dependent quantities, while the modern matrix and equilibrium statements are developed in the Markov-chain text.{{cite:dodge2008}} (pp. 330–331, “Markov, Andrei Andreevich”){{cite:levin_peres2017}} (§1.1, Markov Chains)
