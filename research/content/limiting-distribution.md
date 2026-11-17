## Lead context
Stationarity describes a distribution that does not change under the transition rule; convergence asks whether other starting distributions approach it.

## Motivating example
A weather model predicts tomorrow from today's weather. The initial forecast may depend heavily on today's state, while a long-range forecast may become almost independent of it. The relevant calculation is the distribution after many transitions, not whether one realised weather sequence becomes constant.{{cite:grinstead_snell1997}} (§11.4, fundamental limit theorem)

## Statement
[]{#property-countable-convergence}

For a finite irreducible aperiodic transition matrix $P$, a unique stationary probability vector $\pi$ exists, and $P^n(i,j)\to\pi_j$ for every pair of states. The finiteness condition makes positive recurrence automatic. For a countable irreducible aperiodic chain, the corresponding convergence theorem requires a stationary probability distribution.{{cite:durrett2019}} (§5.6, Thm. 5.6.6, pp. 313–314)

## Intuition — Forgetting the starting state
The matrix equation $\pi P=\pi$ is an equilibrium condition. It says nothing on its own about the approach to equilibrium. The deterministic two-state cycle has stationary law $(1/2,1/2)$, while a point start alternates forever. Aperiodicity excludes this obstruction.{{cite:durrett2019}} (§5.6, Ex. 5.6.2, p. 311)

On a finite state space, irreducibility and aperiodicity imply that some power $P^m$ has all entries positive. This provides a uniform amount of mixing in a fixed number of steps, even when individual entries of $P$ are zero. It is the regularity condition in the finite-chain fundamental limit theorem.{{cite:grinstead_snell1997}} (§11.4, regular transition matrices)

## Proof
Here is a finite-state contraction argument. Let $Q=P^m$ have strictly positive entries, let $c_j=\min_i Q_{ij}$, and set $\varepsilon=\sum_jc_j>0$. If $\varepsilon<1$, every row decomposes as
$$
Q_{ij}=c_j+(1-\varepsilon)R_{ij},
$$
where $R$ is stochastic. For two probability row vectors $\mu,\nu$, the common part cancels and
$$
\|\mu Q-\nu Q\|_1\le(1-\varepsilon)\|\mu-\nu\|_1.
$$
A stochastic matrix cannot increase this norm, by the triangle inequality and row sums. Iteration makes the distributions approach one another geometrically along multiples of $m$; the remaining steps also cannot increase their distance. Existence of a stationary law follows by taking a convergent subsequence of the averaged distributions $n^{-1}\sum_{k<n}\mu P^k$ in the compact probability simplex: multiplying an average by $P$ changes it by $(\mu P^n-\mu)/n$, which tends to zero. The contraction proves uniqueness and convergence to that law. If $\varepsilon=1$, all rows of $Q$ are already identical and the same conclusion follows directly.{{cite:grinstead_snell1997}} (§11.4, finite-chain convergence proof){{cite:durrett2019}} (§5.6, Ex. 5.6.3–5.6.4)

## Generalizations — Time proportions and infinite spaces
[]{#property-ergodic-proportions}

State probabilities and time proportions are different limits. For a finite irreducible chain, the fraction of visits to each state converges to its stationary probability even when the chain is periodic. Thus periodicity can prevent convergence of a point-start distribution without preventing a long-run visit average.{{cite:durrett2019}} (§5.6, Thm. 5.6.1, pp. 310–311)

An infinite state space needs an additional recurrence check. A reflected nearest-neighbour walk with upward probability $p$ and downward probability $q=1-p$, where $0<p<1$, has weights proportional to $(p/q)^j$. They can be normalised only when $p<q$. At equality, repeated returns coexist with the absence of a stationary probability distribution.{{cite:durrett2019}} (§5.5, stationary measures and positive recurrence)

## Worked example
Take
$$
P=\begin{pmatrix}0.8&0.2\\0.4&0.6\end{pmatrix},\qquad\pi=(2/3,1/3).
$$
If $a_n$ is the probability of a dry day after $n$ transitions, then $a_{n+1}=0.4+0.4a_n$. Subtracting $2/3$ gives
$$
a_n-\frac23=0.4^n\left(a_0-\frac23\right).
$$
Starting wet means $a_0=0$, so $a_2=0.56$ and $a_5=2062/3125=0.65984$. The total variation distance after five steps is $|a_5-2/3|=64/9375\approx0.006827$.

**Your turn.** If the chain starts dry instead, find the dry probability after five transitions.

::: {.callout-tip collapse="true" title="Answer"}
Use $a_0=1$, giving $a_5=2/3+(1/3)(0.4)^5=0.67008$. Both starts approach the same limit from opposite sides.
:::
