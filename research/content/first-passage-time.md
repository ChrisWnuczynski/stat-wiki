## Lead context
A first-passage time is the moment a path first enters a chosen set, so a question about ruin or a barrier is a question about that time rather than about the position on one fixed date.

## Motivating example
A gambler who starts with a stake of 3 and stops on reaching 10 or 0 can be ahead for a long stretch and still finish ruined. The chance of hitting 10, and the number of plays until one of the two barriers is reached, depends on the whole sequence of steps.{{cite:durrett2019}} (Thm. 4.8.9, pp. 260–261)

## Intuition — The clock stops at the barrier
Fix a set $A$ of states. The first-passage time $T_A$ is the first index $n$ at which the process lies in $A$, or infinity if that never happens. Unlike the position $S_n$ at a time chosen in advance, $T_A$ looks along the path until the entry occurs. Two paths with the same value at time 20 can have different passage times if one of them touched the barrier earlier.{{cite:durrett2019}} (Thm. 4.8.9, definition of $T_z$)

On a line with steps of size one and absorbing barriers at $0$ and $d$, conditioning on the first step turns the hitting probability into a linear equation. From an interior point the walk moves one step up or one step down, and the chance of eventual success is then the hitting probability at the new point. The same one-step split gives the expected number of steps until absorption, with one step already used.{{cite:durrett2019}} (Thm. 4.8.9, pp. 260–261)

## Definition — Hitting probabilities on a finite interval
Let $S_n$ be a walk on the integers with $\Pr(S_{n+1}=S_n+1)=p$ and $\Pr(S_{n+1}=S_n-1)=q=1-p$, and $0<p<1$. Write $T_z=\inf\{n\ge 0:S_n=z\}$ and, for a start at $x\in\{0,1,\ldots,d\}$,
$$
h_x=\Pr_x(T_d<T_0).
$$
Then $h_0=0$, $h_d=1$, and $h_x=p\,h_{x+1}+q\,h_{x-1}$ for $1\le x\le d-1$. The solution is $h_x=x/d$ when $p=q$, and
$$
h_x=\frac{1-(q/p)^x}{1-(q/p)^d}
$$
when $p\neq q$.{{cite:durrett2019}} (Thm. 4.8.9, (4.8.2), pp. 260–261) The expected absorption time $e_x=\E_x(T_0\wedge T_d)$ satisfies $e_0=e_d=0$ and $e_x=1+p\,e_{x+1}+q\,e_{x-1}$ on the interior. When $p=q=1/2$, $e_x=x(d-x)$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The boundary values are immediate. From an interior $x$ the first step goes to $x+1$ with probability $p$ and to $x-1$ with probability $q$, which is the displayed recurrence. Rearrangement gives $p(h_{x+1}-h_x)=q(h_x-h_{x-1})$. If $p=q$, the first differences are equal, so $h_x$ is linear, and $h_0=0$, $h_d=1$ force $h_x=x/d$. If $p\neq q$, the differences form a geometric sequence with ratio $q/p$. Summing from $1$ to $x$ and imposing $h_d=1$ produces the displayed ratio of geometric sums.{{cite:durrett2019}} (Thm. 4.8.9, (4.8.2))

For the fair duration, substitute $e_x=x(d-x)$. Both ends are zero. The interior right-hand side is
$$
1+\tfrac12(x+1)(d-x-1)+\tfrac12(x-1)(d-x+1)=x(d-x),
$$
so the quadratic satisfies the recurrence.
:::
:::

## Worked example
Take a fair walk absorbed at $0$ and at $5$, starting at $2$. The hitting probability is $h_2=2/5$ and the expected number of steps is $e_2=2(5-2)=6$. The probability $2/5$ of reaching the upper barrier is not the same fact as the expected wait of $6$: ruin, which here has probability $3/5$, can still take several steps.

Now take $p=3/5$, so $q/p=2/3$, with the same barriers and the same start. The biased formula gives
$$
h_2=\frac{1-(2/3)^2}{1-(2/3)^5}=\frac{135}{211}\approx 0.640,
$$
which sits above the fair value $2/5=0.4$, as it must when $p>q$.

**Your turn.** A fair walk is absorbed at $0$ and at $6$ and starts at $4$. Find the probability of hitting $6$ before $0$, and the expected number of steps until absorption.

::: {.callout-tip collapse="true" title="Answer"}
$h_4=4/6=2/3$ and $e_4=4(6-4)=8$.
:::

## Connections — Barriers and fixed times
The position at a large fixed time is governed by a [law of large numbers](law-of-large-numbers.qmd) and a [central limit theorem](central-limit-theorem.qmd). A passage time uses the path up to a random index, so those two limit theorems do not by themselves give $h_x$. The same cut between neighbouring states reappears as local balance for the [M/M/1 queue](m-m-1-queue.qmd), where the state is a count rather than a fortune. On a finite irreducible chain every state is visited again; the passage time here can be infinite only when a barrier is absorbing or the state space is unbounded.{{cite:durrett2019}} (Thm. 4.8.9, pp. 260–261)

## Check yourself

### A fair walk between 0 and 8 {#self-check-ex-sp-fair-ruin}

A fair walk is absorbed at $0$ and at $8$, and starts at $5$. Find the probability of reaching $8$ before $0$, and the expected absorption time.


::: {.callout-tip collapse="true" title="Answer"}
$h_5=5/8$ and $e_5=5(8-5)=15$.
:::

### A biased walk on four steps {#self-check-ex-sp-biased-goal}

Take $p=2/3$, barriers at $0$ and $4$, and a start at $1$. Compute the probability of hitting $4$ before $0$, and compare it with the fair-walk value.


::: {.callout-tip collapse="true" title="Answer"}
$q/p=1/2$, so $h_1=(1-1/2)/(1-(1/2)^4)=(1/2)/(15/16)=8/15$. The fair value is $1/4$. Because $8/15>1/4$, the upward drift lifts the hitting probability above the fair line.
:::
