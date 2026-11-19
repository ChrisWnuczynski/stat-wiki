## Lead context
First-step conditioning turns a path question into a boundary-value problem for a transition matrix.

## Motivating example
A gambler can leave with a target fortune or lose the available stake. The immediate chance of an upward move is not the same as the chance of eventually reaching the target. The eventual probability accounts for every intervening path, including paths that revisit a state many times. Conditioning on the next state produces equations that account for these repeated visits automatically.{{cite:pishro_nik2014}} (§11.2.5)

## Definition — Harmonic values between two boundaries
Let $A$ and $B$ be disjoint target sets and $T_C=\inf\{n\geq0:X_n\in C\}$. For a time-homogeneous Markov chain,
$$
h_i=P_i(T_A<T_B)
$$
satisfies $h_i=1$ on $A$, $h_i=0$ on $B$, and $h_i=\sum_jP_{ij}h_j$ elsewhere. The equation averages the eventual success probabilities after one transition. The convention $n\geq0$ means a chain starting inside a target has already hit it.{{cite:pishro_nik2014}} (§11.2.5, absorption probabilities)

The boundary conditions matter as much as the averaging equation. In a finite chain that reaches $A\cup B$ almost surely from every other state, they give a unique solution. If some closed class avoids both targets, the averaging equations on that class can have multiple solutions; the hitting event itself assigns probability zero to success there.{{cite:grinstead_snell1997}} (§11.2, absorbing and transient states)

## Properties — First-step equations and uniqueness
For the finite absorbing case, collect the nonboundary states into a transient matrix $Q$, and let $r_i=\sum_{j\in A}P_{ij}$. Then
$$
(I-Q)h=r.
$$
The series $h=r+Qr+Q^2r+\cdots$ separates success on the first, second, and later transitions. Because the transient survival probabilities tend to zero, the system has the unique bounded solution $(I-Q)^{-1}r$. The matrix inverse is a way to sum paths, rather than an alternative probability definition.{{cite:grinstead_snell1997}} (§11.2, fundamental matrix and absorption probabilities)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Condition on $X_1=j$. The Markov property makes the remaining probability of success equal to $h_j$, and summing over the possible next states gives the averaging equation. If two bounded solutions agree on the boundaries, their difference $d$ satisfies $d=Qd$, hence $d=Q^nd$. Each coordinate is bounded in absolute value by $\max_j|d_j|$ times the probability of still being transient after $n$ steps. This tends to zero under eventual absorption, so $d=0$.
:::
:::

Expected absorption times use a different equation: $e_i=1+\sum_jP_{ij}e_j$ away from the boundaries, with $e_i=0$ on them. The extra one counts the transition just taken. Probabilities and durations answer different questions even though their coefficient matrix is the same.{{cite:pishro_nik2014}} (§11.2.5, mean hitting times)

## Worked example
For a fair nearest-neighbour walk on $\{0,1,2,3,4\}$ absorbed at zero and four, let success mean hitting four first. The equations are
$$
h_1=h_2/2,\quad h_2=(h_1+h_3)/2,\quad
h_3=(h_2+1)/2.
$$
Solving gives $(h_1,h_2,h_3)=(1/4,1/2,3/4)$. The expected durations solve the same averaging equations with one added to each right-hand side and give $(e_1,e_2,e_3)=(3,4,3)$. Starting halfway between the boundaries maximises the expected duration in this example.{{cite:grinstead_snell1997}} (§12.2, gambler's ruin)

With upward probability $p\ne1/2$ and downward probability $q=1-p$, the recurrence has the solution
$$
h_i=\frac{1-(q/p)^i}{1-(q/p)^4},\qquad0<p<1.
$$
The two boundary values fix the coefficients of the constant and geometric solutions. At $p=0.6$, the three interior probabilities are $27/65$, $9/13$, and $57/65$. In particular, starting from one gives approximately $0.4154$, larger than the fair value $0.25$.{{cite:grinstead_snell1997}} (§12.2)

**Your turn.** In the fair example, start at state two and ask for hitting zero before four. What changes?

::: {.callout-tip collapse="true" title="Answer"}
The two boundary roles interchange, so the success probability becomes $1-h_2=1/2$. The absorption time remains four steps in expectation because the stopping set has not changed.
:::
