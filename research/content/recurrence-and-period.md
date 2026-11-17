## Lead context
Return probability, expected return time and the arithmetic of possible return times describe different aspects of a Markov chain.

## Motivating example
A machine alternates between two operating modes at every step. It certainly revisits either mode, but a mode can be revisited only after an even number of steps. Another machine can remain in its present mode or move permanently to failure. A self-loop permits a return after one step, yet does not ensure that return occurs. These two examples separate recurrence from aperiodicity.{{cite:durrett2019}} (§§5.3 and 5.6, pp. 281–282 and 311–312)

## Definition — Certainty, waiting time and return-time arithmetic
Starting at state $i$, define $T_i^+=\inf\{n\ge1:X_n=i\}$. The state is recurrent if $\mathbb P_i(T_i^+<\infty)=1$, and transient otherwise. A recurrent state is positive recurrent when its expected return time is finite; otherwise it is null recurrent.{{cite:durrett2019}} (§5.3, p. 281; §5.5, p. 306)

The period is the greatest common divisor of all possible positive return lengths. It need not be the shortest return length. If returns of lengths $3$ and $4$ are possible, their greatest common divisor is $1$, even if a one-step return is impossible. Communicating recurrent states have the same period.{{cite:durrett2019}} (§5.6, Ex. 5.6.3 and Lem. 5.6.4, p. 312)

## Properties — Occupation does not require convergence of every transition probability
For an irreducible positive recurrent chain, stationary mass and mean return time satisfy $\pi_i=1/\mathbb E_iT_i^+$. A large stationary mass corresponds to short average gaps between visits. This identity holds for periodic chains as well as aperiodic ones.{{cite:grinstead_snell1997}} (§11.5, Thm. 11.15, p. 455)

Periodicity can prevent $P^n$ from converging while time-averaged occupation still settles. Deterministic alternation has stationary law $(1/2,1/2)$, but $P^{2n}=I$ and $P^{2n+1}=P$. Each mode nevertheless occupies half the steps in the long run.{{cite:durrett2019}} (§5.6, Thm. 5.6.1 and Ex. 5.6.2, pp. 310–311)

## Worked example — A self-loop and a genuine return
Consider
$$
P=\begin{pmatrix}1/2&1/2\\1/4&3/4\end{pmatrix}.
$$
The stationary equations give $\pi=(1/3,2/3)$. Let $m$ be the mean number of steps to reach state $0$ starting from state $1$. First-step conditioning yields $m=1+(3/4)m$, hence $m=4$. Starting from $0$, the mean first return is $1+(1/2)m=3$, agreeing with $1/\pi_0=3$. First-step equations and the stationary identity provide two distinct ways to check the answer.{{cite:grinstead_snell1997}} (§11.5, eqs. 11.2–11.4 and Thm. 11.15, pp. 455–456)

Both self-loop probabilities are positive, so both periods are $1$. The two-step matrix is
$$
P^2=\begin{pmatrix}0.375&0.625\\0.3125&0.6875\end{pmatrix}.
$$
The one-step probability $P_{00}=1/2$ is neither the eventual return probability, which is $1$, nor the stationary mass, which is $1/3$.

**Your turn.** Change the chain to deterministic alternation. Find the first return time to state $0$, its period and its stationary mass.

::: {.callout-tip collapse="true" title="Answer"}
The first return occurs at time $2$ with certainty. The possible return lengths are the positive even integers, so the period is $2$. The stationary mass at state $0$ is $1/2$.
:::

## Check yourself

### A return without a self-loop {#self-check-depth-return-vs-selfloop}
[A return without staying put](../questions/depth-return-vs-selfloop.qmd): must recurrence imply a positive probability of staying put?

::: {.callout-tip collapse="true" title="Answer"}
No. Deterministic alternation returns after two steps with probability one and has zero probability of staying put for one step.
:::

### Following a stationary law {#self-check-ex-sp-weather-two-step}
[Two steps and the stationary law](../questions/ex-sp-weather-two-step.qmd): compute the indicated two-step transition probability and stationary distribution.

::: {.callout-tip collapse="true" title="Answer"}
The two possible intermediate states give $(P^2)_{12}=0.9(0.1)+0.1(0.6)=0.15$. Stationarity requires $0.1\pi_1=0.4\pi_2$ and $\pi_1+\pi_2=1$, giving $(0.8,0.2)$.
:::
