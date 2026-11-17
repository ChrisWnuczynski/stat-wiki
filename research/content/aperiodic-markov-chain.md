## Motivating example

A simulation that alternates between two states visits each equally often, yet a snapshot taken at an even time always shows its starting state. Waiting longer does not make that snapshot representative. The obstacle is the chain's rhythm: returns are possible only at even times. Aperiodicity describes the absence of such a rigid common cycle and supplies the missing condition in the usual finite-state convergence theorem.

## Intuition

For a state $i$, list all positive numbers of steps in which a return to $i$ has positive probability. Their greatest common divisor is the period $d(i)$.{{cite:siegrist2022_markov_period}} (§5, period is a class property) A period of two means that every possible return occurs at an even time; a period of three means returns lie on multiples of three. When the gcd is one, the possible return times need not include every small number. Their timing eventually ceases to force the chain to stay in fixed phases. This is what *aperiodic* means.

A self-loop makes a one-step return possible and immediately gives period one.{{cite:siegrist2022_markov_period}} (§5, period is a class property; a self-loop is sufficient but not necessary) It is only a sufficient test. A chain can have no self-loops and still have two return routes whose lengths, such as three and five, have gcd one. Conversely, random transitions do not by themselves remove periodicity: a random walk that switches between two parts of a bipartite graph on every step still alternates between those parts.

## Definition

For a discrete-time transition matrix $P$, write $p_{ij}^{(n)}=(P^n)_{ij}$. A state $i$ with at least one possible return has period

$$
d(i)=\gcd\{n\geq1:p_{ii}^{(n)}>0\}.
$$

It is aperiodic when $d(i)=1$. Communicating states have the same period, so an irreducible chain has one well-defined period. In a reducible chain, different closed classes can have different periods; calling the whole chain aperiodic without naming the relevant class can hide this distinction. A state with no return path is transient and its period needs separate conventions, so the convergence discussion below concerns irreducible chains.

## Properties

### Why communication preserves the period
Suppose $i$ and $j$ communicate. Let a path from $i$ to $j$ have length $a$ and a path back have length $b$, both with positive probability. Going out and back makes $a+b$ a return length for $i$. If $n$ is any return length for $j$, going from $i$ to $j$, making that return, and coming back gives a return to $i$ of length $a+n+b$. Hence $d(i)$ divides both $a+b$ and $a+n+b$, so it divides $n$. It therefore divides every return length for $j$ and hence $d(j)$. Interchanging $i$ and $j$ gives the reverse divisibility, proving $d(i)=d(j)$. The same rhythm belongs to the entire communicating class.

### Aperiodicity and convergence
Every finite irreducible chain has a unique stationary distribution $\pi$, which satisfies $\pi P=\pi$. Aperiodicity answers a different question: whether the distribution at time $n$, starting from a particular state, approaches $\pi$. If the chain is also aperiodic, then $p_{ij}^{(n)}\to\pi_j$ for every start $i$ and destination $j$. In a periodic chain, $\pi$ can remain stationary while the rows of $P^n$ oscillate. The long-run fraction of visits to a state may still approach its stationary mass; that is an average over times, rather than a limit at one time.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Here is a finite-state proof of the convergence claim. Fix a state $s$. Its possible return lengths have gcd one, and a finite subset already has gcd one. Choose one length $a$ from that subset. The other lengths generate every residue class modulo $a$ by nonnegative addition: in the finite group of residues, their additive semigroup is the subgroup they generate, which is the whole group because the gcd is one. Choose one nonnegative combination for each residue. Every sufficiently large integer is that combination plus a nonnegative multiple of $a$, so it is a possible return length. Concatenating return paths shows $p_{ss}^{(n)}>0$ for all sufficiently large $n$. Irreducibility gives a positive-probability path from any $i$ to $s$ and another from $s$ to any $j$; insert a sufficiently long return at $s$. Therefore, for some common integer $m$, every entry of $P^m$ is positive.

Let the state space have $N$ states and $\varepsilon=\min_{ij}(P^m)_{ij}>0$. Every row of $P^m$ contains the same mass $N\varepsilon$ spread uniformly, with its remaining mass in another probability row. Thus multiplying two probability rows by $P^m$ contracts their total-variation distance by at most $1-N\varepsilon<1$ (the case $N\varepsilon=1$ converges in one block). A stationary distribution exists by taking a convergent subsequence of the finite-dimensional averages $n^{-1}\sum_{k=0}^{n-1}\mu P^k$; their one-step difference tends to zero. The contraction makes this distribution unique and sends $\mu P^{km}$ to it. Applying the remaining $r<m$ steps preserves the limit because $\pi P^r=\pi$. Consequently $\mu P^n\to\pi$ for every initial row $\mu$, and in particular $p_{ij}^{(n)}\to\pi_j$.
:::
:::

## Worked example

Consider three states with transition matrix

$$
P=\begin{pmatrix}0&1&0\\0&0&1\\1/2&1/2&0\end{pmatrix}.
$$

There is no self-loop. Starting at state $0$, one route returns in three steps, $0\to1\to2\to0$, with probability $1/2$. Another returns in five steps, $0\to1\to2\to1\to2\to0$, with probability $1/4$. Since $\gcd(3,5)=1$, state $0$ is aperiodic. All states communicate, so the entire chain has period one. Solving $\pi P=\pi$ gives $\pi_0=\pi_2/2$ and $\pi_1=\pi_2$; normalization yields $\pi=(1/5,2/5,2/5)$. Thus the probability of being in state $0$ at a distant time approaches $1/5$ from any starting state, even though an immediate return is impossible.

**Your turn.** A chain on states $0,1$ has $P=\begin{pmatrix}1/4&3/4\\1/2&1/2\end{pmatrix}$. Find its period and stationary distribution. Starting from $0$, find $p_{00}^{(2)}$ and explain what happens to $p_{00}^{(n)}$ as $n$ grows.

::: {.callout-tip collapse="true" title="Answer"}
Both states communicate, and both have self-loops, so the period is one. Balance gives $(3/4)\pi_0=(1/2)\pi_1$, hence $\pi=(2/5,3/5)$. The two-step return probability is $(1/4)^2+(3/4)(1/2)=7/16$. The chain is finite, irreducible and aperiodic, so $p_{00}^{(n)}\to2/5$; the fact that $7/16$ differs from $2/5$ shows that convergence is a limit, not an equality after two steps.
:::

## Common misconceptions

An aperiodic chain need not have a self-loop: the three-state worked example has none. Stationarity is not the same as convergence from an arbitrary start: deterministic alternation preserves $(1/2,1/2)$ when started there, yet a fixed-state start keeps oscillating. A period-one calculation does not by itself guarantee a unique limiting distribution either; a chain with two separate absorbing states has aperiodic classes but remembers which class it entered. Finally, time averages can settle when single-time probabilities do not, as in alternation. These are different claims about return routes, initial laws, class structure and averaging.

## Assumptions and limits — When convergence fails

For deterministic alternation $P=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, the stationary law is $(1/2,1/2)$, but $p_{00}^{(n)}$ equals one for even $n$ and zero for odd $n$. Its period is two, so aperiodicity fails. For two absorbing states $P=I_2$, each state has period one but there are two closed classes and infinitely many stationary distributions; irreducibility fails. On an infinite state space, period one and irreducibility alone do not ensure a stationary *probability* distribution: a reflected symmetric random walk on nonnegative integers has a self-loop at zero but is null recurrent. Positive recurrence is needed for the countable-state convergence theorem.

## Connections

Irreducibility makes the period common to all states. The [stationary distribution](stationary-distribution.qmd) solves an invariant equation, while aperiodicity lets that law become the one-time limit in the finite irreducible case. In [Markov-chain Monte Carlo](../notes/bayes-04-mcmc.qmd), a self-loop from a rejected proposal often breaks a deterministic cycle, but the whole chain still needs access to its target's support. For a periodic irreducible chain of period $d$, considering every $d$th step separates the process into cyclic classes.

## History

Andrei Markov's studies of dependent sequences helped establish the theory of stochastic processes now bearing his name. His work on chains is part of that development. The period-one condition belongs to the later mathematical description of long-run behaviour: it distinguishes a stationary probability from the distribution observed after many transitions.{{cite:dodge2008}} (p. 331, Markov entry)
