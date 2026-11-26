## Lead context
Duration counts the steps until either absorbing boundary is reached, rather than the probability of reaching a particular boundary.

## Motivating example
A gambler stops when their fortune reaches zero or a target. The chance of success is only part of the question: a game with acceptable success probability may still take many plays. A first-step equation determines the mean duration by charging one step now and adding the expected remaining time.{{cite:durrett2012_essentials}} (§1.9, Exs. 1.49–1.50, pp. 52–53)

## Definition — Stop at either boundary
Let $X_n$ move up one with probability $p\in(0,1)$ and down one with probability $q=1-p$. On the finite interval $\{0,\ldots,d\}$, with integer $d\ge2$, define
$$
T=\inf\{n\ge0:X_n\in\{0,d\}\},\qquad e_x=\E(T\mid X_0=x).
$$
A start at an absorbing boundary gives $e_0=e_d=0$. At an interior state,
$$
e_x=1+pe_{x+1}+qe_{x-1}.
$$
The initial one counts the first transition, including a transition that ends the game.{{cite:durrett2012_essentials}} (§1.9, first-step equations, Ex. 1.49)

The finite mean follows without assuming the formula. From any interior state, $d$ consecutive upward steps cause absorption with probability at least $p^d>0$. Applying that bound in blocks of $d$ steps gives $P(T>md)\le(1-p^d)^m$. Summing this geometric tail bounds $\E(T)$. The same reasoning guarantees eventual absorption.{{cite:grinstead_snell1997}} (§11.2, absorbing chains and expected absorption time)

## Properties — A quadratic for a fair walk
For $p=q=1/2$, the recurrence becomes
$$
e_{x+1}-2e_x+e_{x-1}=-2.
$$
The quadratic $x(d-x)$ has second difference $-2$ and vanishes at both endpoints, hence solves the equations. Uniqueness follows from the maximum principle: a difference between two solutions is a weighted average of its neighbours with zero boundary values; an interior positive maximum would propagate to a boundary, a contradiction. Apply the same reasoning to its negative. Therefore
$$
e_x=x(d-x).
$$
The duration grows quadratically when starting position and interval width are enlarged by the same integer factor.{{cite:durrett2012_essentials}} (§1.9, Ex. 1.49, pp. 52–53)

## Interpretation — Success probability enters the biased formula
Let $h_x=P_x(X_T=d)$. The same first-step reasoning, now without charging a step, gives $h_x=ph_{x+1}+qh_{x-1}$, $h_0=0,h_d=1$. For $p\ne q$, putting $r=q/p$ gives
$$
h_x=\frac{1-r^x}{1-r^d},\qquad
 e_x=\frac{x-dh_x}{q-p}.
$$
The geometric expression solves the boundary equations for $h$. To verify duration, note that the weighted average of the coordinate $x$ is $x+p-q$, while the weighted average of $h$ is $h$. Substitution therefore gives $1+pe_{x+1}+qe_{x-1}=e_x$; both boundaries vanish, and uniqueness completes the argument.{{cite:grinstead_snell1997}} (§12.2, pp. 487–489){{cite:durrett2012_essentials}} (§1.9, Ex. 1.50, p. 53)

An equivalent identity is $(p-q)e_x=dh_x-x$: expected accumulated drift equals expected final displacement. A very small $p-q$ makes the closed form numerically subtract nearly equal quantities. The fair-walk expression or a direct solution of the first-step linear system avoids that subtraction at equality.{{cite:durrett2012_essentials}} (§1.9, Exs. 1.49–1.50)

## Worked example
Take boundaries $0$ and $6$ and start at $2$. A fair walk has mean duration $2(6-2)=8$. For $p=3/5$, $q=2/5$, the success probability is
$$
h_2=\frac{1-(2/3)^2}{1-(2/3)^6}=\frac{81}{133}\approx0.609023.
$$
The expected duration becomes
$$
e_2=\frac{2-6(81/133)}{-1/5}=\frac{1100}{133}\approx8.270677.
$$
A drift toward the farther boundary has slightly increased the mean duration here. Greater upward success probability does not by itself imply a shorter game.{{cite:durrett2012_essentials}} (§1.9, Ex. 1.50, p. 53)

**Your turn.** For the fair walk, double both the initial fortune and target. What happens to the expected duration?

::: {.callout-tip collapse="true" title="Answer"}
The new start is $4$ and target is $12$, giving $4(12-4)=32$ steps. Duration increases by a factor of four, rather than two.
:::

## Check yourself
### Fair success and duration {#self-check-ex-sp-fair-ruin}
[A fair walk on eight steps](../questions/ex-sp-fair-ruin.qmd): calculate both quantities from its start at five.

::: {.callout-tip collapse="true" title="Answer"}
The upper-boundary probability is $5/8$. The expected duration until either boundary is $5(8-5)=15$ steps. One is a probability, the other a mean number of transitions.
:::

### Checking the quadratic {#self-check-ex-sp-duration-identity}
[Checking the duration formula](../questions/ex-sp-duration-identity.qmd): verify the recurrence directly.

::: {.callout-tip collapse="true" title="Answer"}
Both endpoints of $e_x=x(d-x)$ are zero. Expanding the two neighbouring values gives $(e_{x+1}+e_{x-1})/2=x(d-x)-1$. Adding one therefore returns $e_x$, exactly the fair-walk first-step equation.
:::
