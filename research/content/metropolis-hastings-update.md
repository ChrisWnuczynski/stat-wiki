## Motivating example
Suppose a posterior density is easy to evaluate up to a constant but hard to sample from directly. One can propose a new parameter value using a simple distribution and then decide whether to move there. The acceptance decision corrects both for the posterior's relative support and for any directional bias in the proposal. Repeating the update creates a chain with the posterior as its stationary distribution, provided the proposal can reach the relevant support. The retained draws are dependent, so a plausible looking histogram alone cannot establish that the chain has explored the whole posterior.{{cite:hastings1970}} (§§1–2.2, pp. 97–101){{cite:levin_peres2017}} (§3.2, pp. 38–40)

## Intuition
The proposal $q(y\mid x)$ describes where the algorithm *tries* to go from $x$. It is not, by itself, the transition rule after rejection. If proposals from $x$ to $y$ are common but reverse proposals are rare, accepting every proposed move can overrepresent $y$. The Hastings ratio compares target-weighted forward and reverse proposal flow. The minimum with one clips the correction to a probability; a rejected proposal leaves the chain at $x$. This is why repeated states in a trace are genuine observations from the simulated chain.{{cite:hastings1970}} (§2.2, pp. 99–100){{cite:levin_peres2017}} (§3.2, pp. 38–40)

## Definition
For $x\ne y$ with $\pi(x)q(y\mid x)>0$, the update uses

$$
r(x,y)=\frac{\pi(y)q(x\mid y)}{\pi(x)q(y\mid x)},\qquad a(x,y)=\min\{1,r(x,y)\}.
$$

If $q(y\mid x)>0$ but $\pi(y)q(x\mid y)=0$, the proposed move is rejected. With symmetric proposals the $q$ terms cancel, yielding the original Metropolis acceptance rule. With an independent proposal $q(y\mid x)=g(y)$, they generally do *not* cancel: the correction is $g(x)/g(y)$. Computing in log form uses $\log r=\log\pi(y)-\log\pi(x)+\log q(x\mid y)-\log q(y\mid x)$ and avoids multiplying tiny densities.{{cite:hastings1970}} (§2.2, pp. 99–101){{cite:levin_peres2017}} (§3.2, pp. 38–40)

## Properties
The accepted off-diagonal transition is $P(x,y)=q(y\mid x)a(x,y)$. The rest of the row's probability remains at $x$, including proposals to $x$ and rejections of other proposals. This self-transition is essential to the target distribution. If the target is known only as $\pi(x)=f(x)/Z$, the unknown $Z$ cancels in $r(x,y)$; it is enough to evaluate the unnormalised posterior or energy weight at the two states.{{cite:hastings1970}} (§§1 and 2.2, pp. 98–100)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For distinct $x,y$, write $F=\pi(x)q(y\mid x)$ and $R=\pi(y)q(x\mid y)$. The Metropolis–Hastings choice gives $\pi(x)P(x,y)=F\min\{1,R/F\}=\min\{F,R\}$. Reversing $x,y$ gives $\pi(y)P(y,x)=R\min\{1,F/R\}=\min\{R,F\}$; the same equality holds by continuity when one flow is zero. The diagonal needs no paired comparison. Summing detailed balance over origins yields $\sum_x\pi(x)P(x,y)=\pi(y)\sum_xP(y,x)=\pi(y)$, so $\pi$ is stationary. Replacing $\pi$ by $f/Z$ multiplies numerator and denominator of $r$ by the same $1/Z$ and leaves the transition unchanged.{{cite:hastings1970}} (§2.2, pp. 99–100){{cite:levin_peres2017}} (§1.6, p. 13; §3.2, pp. 38–40)
:::
:::

Stationarity is a property of the transition kernel, not a certificate that a finite run has reached the target. Irreducibility, recurrence and adequate exploration have to be considered separately. A small local proposal may accept almost every move yet traverse the posterior slowly; a huge one may propose remote low-density values that are mostly rejected. The figure illustrates both extremes for a normal target.{{cite:hastings1970}} (§§2.2–2.3, pp. 100–101){{cite:levin_peres2017}} (§3.2, pp. 38–40)

## Statistical use — Designing a posterior transition
Start by writing an unnormalised target on its actual support and a proposal whose forward and reverse probabilities can be evaluated. For a random-walk proposal, verify symmetry before dropping proposal terms; for an independent or otherwise asymmetric proposal, keep them. Store the old value on rejection and inspect whether proposals cross the regions that carry appreciable target mass. Estimate posterior summaries from the retained dependent draws, with uncertainty calculations that account for serial correlation. Hastings already emphasised that correlated output makes Monte Carlo error assessment more delicate than for independent draws.{{cite:hastings1970}} (§§1–2.2, pp. 98–100; §4, pp. 104–105)

## Worked example
Consider a target on two states with $\pi=(0.7,0.3)$. An asymmetric proposal tries to move from $0$ to $1$ with probability $q(1\mid0)=0.8$, but from $1$ to $0$ with probability $q(0\mid1)=0.2$. At state $0$, a proposal of $1$ has ratio

$$
r(0,1)=\frac{0.3(0.2)}{0.7(0.8)}=\frac{3}{28}\approx0.107143.
$$

It is accepted with that probability. The reverse proposal has ratio $28/3>1$, so it is accepted with probability one. The resulting transition matrix has off-diagonal entries $P(0,1)=0.8(3/28)=3/35\approx0.085714$ and $P(1,0)=0.2$. Its diagonal entries are therefore $32/35$ and $0.8$. The flows match: $0.7(3/35)=0.06=0.3(0.2)$. Frequent proposals towards state $1$ are offset by frequent rejections; the target remains $(0.7,0.3)$ rather than drifting toward the proposal's preference.{{cite:hastings1970}} (§2.2, pp. 99–100)

**Your turn.** Let $\pi=(0.25,0.75)$, $q(1\mid0)=0.4$ and $q(0\mid1)=0.6$. Find the acceptance probabilities in both directions and the resulting off-diagonal transition probabilities.

::: {.callout-tip collapse="true" title="Answer"}
$r(0,1)=0.75(0.6)/[0.25(0.4)]=4.5$, so $a(0,1)=1$. In reverse $r(1,0)=1/4.5=2/9$, so $a(1,0)=2/9$. Therefore $P(0,1)=0.4$ and $P(1,0)=0.6(2/9)=2/15\approx0.133333$. The target flows agree: $0.25(0.4)=0.1=0.75(2/15)$. Dropping the proposal ratio would give a different and incorrect stationary law.
:::

## Common misconceptions
High acceptance does not imply efficient sampling: tiny proposals can accept almost always while remaining highly correlated. Rejection is not permission to try again without recording a state; repeating proposals until one succeeds changes the transition rule. An asymmetric or independent proposal does not lose its correction simply because it is easy to sample. Finally, having the right stationary distribution does not make successive draws independent or prove that a chain started far away has already reached it.{{cite:hastings1970}} (§§1–2.3, pp. 98–101)

## Assumptions and limits — When the update misses the target
If the proposal cannot reach a second mode from the current region, no amount of rejection correction makes the chain visit that mode; the transition is reducible even if formal balance holds where it moves. If a programmer redraws after every rejection in the two-state worked example, the output jumps on each retained step instead of holding at $0$ with probability $32/35$; the intended stationary law is lost. If an independent proposal assigns zero probability to a region where $\pi$ is positive, that region cannot be explored from outside. These are support and transition-design failures, distinct from merely running a sound chain for too few steps.{{cite:hastings1970}} (§§2.1–2.2, pp. 98–100; §4, pp. 104–105)

## Connections
The [stationary distribution](stationary-distribution.qmd) is the desired fixed point of this transition. [Detailed balance](detailed-balance.qmd) proves invariance, while [irreducibility](irreducible-markov-chain.qmd) and [aperiodicity](aperiodic-markov-chain.qmd) concern eventual access and convergence. The [random-walk and independent proposal](random-walk-and-independent-proposals.qmd) choices produce different Hastings factors. [Effective sample size](effective-sample-size.qmd) describes the loss of precision caused by serial dependence in the retained chain.{{cite:hastings1970}} (§§1–2.2, pp. 98–100){{cite:levin_peres2017}} (§§1.5–1.6, pp. 9–14; §3.2, pp. 38–40)

## History
The 1953 Metropolis collaboration developed a symmetric-proposal simulation scheme for molecular configurations. Hastings's 1970 paper generalised the construction to arbitrary proposal transitions, explicitly included the proposal ratio, and discussed correlated-sample error and rejection rates. The distinction still matters: “Metropolis” often names the symmetric special case, whereas “Metropolis–Hastings” includes asymmetric proposals.{{cite:hastings1970}} (§§1–2.3, pp. 97–101, historical introduction and construction)
