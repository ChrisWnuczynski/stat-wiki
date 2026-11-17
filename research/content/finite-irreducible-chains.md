## Motivating example
A finite queueing controller may switch among operating modes forever. If every mode can eventually reach every other, there is one stationary occupancy law. Whether its distribution at an exact future time approaches that law also depends on possible return times.{{cite:grinstead_snell1997}} (§11.3, Thms. 11.10–11.11, p. 438)

## Intuition — Occupancy and the clock are different limits
Stationarity is the algebraic identity $\pi P=\pi$. It says that a chain started with law $\pi$ has that same law at every later step. Irreducibility on a finite state space gives existence, uniqueness and positivity of $\pi$. A deterministic cycle still has these properties, even though its location at a particular time depends on the starting phase.{{cite:grinstead_snell1997}} (§11.3, Thm. 11.10, p. 438)

[]{#property-return-time-identity}

For long-run frequencies, visits are grouped by successive returns to a state. The reciprocal mean return time equals the stationary mass of that state. The occupancy fraction converges even when one-time probabilities oscillate.{{cite:durrett2019}} (§5.5, Thm. 5.5.11, p. 306; §5.6, Thm. 5.6.1, pp. 310–311)

## Key results — Positivity, uniqueness and the role of aperiodicity

[]{#property-aperiodic-convergence}
For a finite irreducible transition matrix, every component of the stationary law is positive. If the common period is one, then $(P^n)_{ij}\to\pi_j$. A positive self-transition supplies a return of length one and forces this period for the whole irreducible class.{{cite:durrett2019}} (§5.6, Lem. 5.6.4 and Thm. 5.6.6, pp. 312–314)

## Proof
To establish existence on the finite state space, start with any probability row $\nu$ and form $v_n=n^{-1}\sum_{k=0}^{n-1}\nu P^k$. The finite-dimensional probability simplex is compact, so some subsequence has limit $\pi$. Since $v_nP-v_n=(\nu P^n-\nu)/n$ tends to zero componentwise, $\pi P=\pi$. At least one coordinate $\pi_i$ is positive. For any state $j$, irreducibility gives an $m$ with $(P^m)_{ij}>0$, and $\pi_j=(\pi P^m)_j\ge\pi_i(P^m)_{ij}>0$.

For uniqueness, let $q$ be another stationary probability row and choose $c=\min_i(q_i/\pi_i)$. The row $r=q-c\pi$ is nonnegative and stationary, with some zero coordinate $r_j$. If $r_i>0$ anywhere, a positive-probability route from $i$ to $j$ would imply $r_j=(rP^m)_j>0$, a contradiction. Thus $r=0$, and summing the coordinates gives $c=1$, so $q=\pi$. This proves existence, positivity and uniqueness without assuming aperiodicity. The convergence statement adds the aperiodicity hypothesis.{{cite:grinstead_snell1997}} (§§11.3–11.4, pp. 438, 447–450)

## Statistical use — A two-state transition calculation

### Worked example
For
$$P=\begin{pmatrix}1/2&1/2\\1&0\end{pmatrix},$$
balance gives $\pi_1=\pi_0/2$ and hence $\pi=(2/3,1/3)$. The self-loop at state zero makes the chain aperiodic. If it starts at zero, let $u_n=\Pr(X_n=0)$. Then $u_{n+1}=1-u_n/2$, so
$$u_n=\frac23+\frac13(-1/2)^n.$$
At step six this is $0.671875$; the second coordinate is $0.328125$. The mean return time to zero is $1/\pi_0=3/2$ steps. In contrast, deterministic alternation has stationary law $(1/2,1/2)$ and a return probability alternating between zero and one.{{cite:durrett2019}} (§5.6, Ex. 5.6.2 and Ex. 5.6.1, pp. 311, 315)

**Your turn.** What is the stationary law for deterministic motion around three states, and does it imply convergence from one fixed state?

::: {.callout-tip collapse="true" title="Answer"}
The law is uniform, $(1/3,1/3,1/3)$. Starting from one state, the position cycles with period three, so the one-time probabilities have no limit.
:::
