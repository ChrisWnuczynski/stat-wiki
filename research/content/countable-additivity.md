## Motivating example
Point masses $(1/2)^k$ on the positive integers sum to $1$. The events $A_n=\{1,\ldots,n\}$ increase to the whole space, and $P(A_3)=7/8$ while $P(A_4)=15/16$.

## Intuition — The axiom that lets probabilities pass inside a limit
Finite additivity says the probability of two disjoint events is the sum of their probabilities. Many of the events one actually cares about are limits: the event that a wait is finite, or that infinitely many of a sequence of events occur. Those are countable unions. Countable additivity is the axiom that the probability of a countable disjoint union equals the sum of the probabilities. From it, the empty event has probability zero, and the probability of an increasing sequence of events passes to the limit.{{cite:durrett2019}} (Thm. 1.1.1, pp. 1–2)

## Definition — Disjoint countable unions
A probability $P$ on a sigma-algebra satisfies $P(\Omega)=1$ and, for pairwise disjoint events $A_n$,
$$
P\Bigl(\bigcup_{n=1}^{\infty} A_n\Bigr)=\sum_{n=1}^{\infty} P(A_n).
$$
Countable additivity forces $P(\emptyset)=0$, so that value does not have to be taken as a further assumption. If $A_n\uparrow A$, then $P(A_n)\uparrow P(A)$.{{cite:durrett2019}} (Thm. 1.1.1, pp. 1–2)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The sets $\emptyset,\emptyset,\ldots$ are pairwise disjoint and their union is $\emptyset$. Countable additivity gives $P(\emptyset)=\sum_{n=1}^{\infty} P(\emptyset)$. The only number $p\in[0,1]$ equal to the sum of infinitely many copies of itself is $p=0$.

For continuity from below, set $B_1=A_1$ and $B_n=A_n\setminus A_{n-1}$ for $n\ge 2$. The $B_n$ are disjoint, their union is $A$, and the union of the first $n$ is $A_n$. Therefore
$$
P(A)=\sum_{m=1}^{\infty} P(B_m)=\lim_{n\to\infty}\sum_{m=1}^{n} P(B_m)=\lim_{n\to\infty} P(A_n).
$$
{{cite:durrett2019}} (Thm. 1.1.1 (iii), p. 2)
:::
:::

## Worked example — A geometric series of atoms
Put mass $(1/2)^k$ on the positive integer $k$. The masses sum to $1$, so this is a probability on the countable sample space, built by summing the point masses. Let $A_n=\{1,\ldots,n\}$. Then $A_n\uparrow\{1,2,\ldots\}$ and
$$
P(A_n)=\sum_{k=1}^{n}\Bigl(\frac12\Bigr)^k=1-2^{-n}.
$$
In particular $P(A_3)=7/8=0.875$ and $P(A_4)=15/16=0.9375$. The limit is $1$, which is $P$ of the whole sample space.{{cite:durrett2019}} (Ex. 1.1.2, pp. 2–3; Thm. 1.1.1 (iii), p. 2)

**Your turn.** Find $P(A_5)$ and $P(A_5\setminus A_3)$.

::: {.callout-tip collapse="true" title="Answer"}
$P(A_5)=1-2^{-5}=31/32=0.96875$. The difference $A_5\setminus A_3=\{4,5\}$ has probability $(1/2)^4+(1/2)^5=3/32=0.09375$, which is also $P(A_5)-P(A_3)=0.96875-0.875$.
:::

## Connections — Where the countable union is doing the work
An [event](event.qmd) has to lie in the [sigma-algebra](sigma-algebra.qmd) before this axiom applies to it. A [stochastic process](stochastic-process.qmd) needs those countable operations for events about a whole path, such as "the walk ever reaches $a$". The [central limit theorem](central-limit-theorem.qmd) is a later limit of probabilities; continuity from below is the special case in which the events themselves increase to a limit.{{cite:durrett2019}} (Thm. 1.1.1, pp. 1–2)

