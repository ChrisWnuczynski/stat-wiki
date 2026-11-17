## Motivating example — A favourable game can still end in bankruptcy
A gambler starts with a finite fortune, wins one unit with probability $p$, and loses one unit with probability $q=1-p$ independently at each play. Play stops upon reaching zero or a target fortune $d$. Even when $p>1/2$, an early sequence of losses can cause ruin before the long-run upward drift has much opportunity to act. The relevant probability is a boundary-hitting probability for the whole path, rather than the chance of winning the next play.{{cite:grinstead_snell1997}} (§12.2, Gambler's Ruin)

## Definition — Two absorbing boundaries
Write $S_0=x\in\{0,\ldots,d\}$ and $\tau=\inf\{n\ge0:S_n\in\{0,d\}\}$. For $0<p<1$, let $h_x=\Pr_x(S_\tau=d)$. Conditioning on the first step yields $h_x=p h_{x+1}+q h_{x-1}$, with $h_0=0$ and $h_d=1$. The boundaries must be specified along with the step probabilities: reaching a finite target before ruin is a different event from avoiding ruin indefinitely on an unbounded state space. If $x$ is already a boundary, the stopping time is zero.{{cite:grinstead_snell1997}} (§12.2, thm. 12.2)

## Properties — Solve for first differences
Set $\Delta_x=h_x-h_{x-1}$. The recurrence rearranges to $p\Delta_{x+1}=q\Delta_x$. When $p=q$, the increments are equal and their sum from zero to $d$ is one, giving $h_x=x/d$. When $p\ne q$, summing a geometric progression gives
$$h_x=\frac{1-(q/p)^x}{1-(q/p)^d}.$$
This derivation uses the boundary values to determine the normalisation, rather than guessing which of success and ruin the formula represents. The ruin probability is $1-h_x$. In particular, a walk biased upward increases success above $x/d$, but cannot make success certain at an interior starting point.{{cite:durrett2019}} (§4.8.1, applications to random walks)

To see uniqueness, subtract any two solutions of the recurrence with the same boundary values. A positive maximum of their difference at an interior point must also occur at both neighbours, because the value is a strict positive weighted average of them. Repeating this reaches a boundary, where the difference is zero, a contradiction. The same argument excludes a negative minimum. Thus the computed harmonic function is the only solution of the boundary problem.

## Statistical use — Duration is a different risk measure
Let $m_x=\mathbb E_x\tau$. First-step conditioning gives $m_x=1+p m_{x+1}+q m_{x-1}$ and $m_0=m_d=0$. For a fair walk, direct substitution gives $m_x=x(d-x)$. For a biased walk,
$$m_x=\frac{d h_x-x}{p-q}.$$
Substitution into the recurrence verifies the expression, using the harmonic equation for $h$. This is also consistent with the drift identity $\mathbb E_xS_\tau=x+(p-q)\mathbb E_x\tau=d h_x$. A negative numerator for downward drift is divided by a negative drift, producing a positive duration.{{cite:grinstead_snell1997}} (§12.2, expected duration of the game)

Finite expectation can be justified without applying an optional-stopping theorem before checking its hypotheses. From any interior state, a run of $d$ upward steps reaches the upper boundary within the next $d$ plays. That run has probability $p^d>0$. Consequently $\Pr(\tau>kd)\le(1-p^d)^k$ by successive conditioning on surviving each block. This geometric bound gives almost-sure absorption and finite expected duration. With bounded stopped increments, the usual martingale stopping argument is then valid as well.{{cite:durrett2019}} (§4.8, optional stopping and §4.8.1)

## Worked example — Five units as a target
Take $d=5$, $x=2$ and $p=3/5$. Then $q/p=2/3$ and
$$h_2=\frac{1-(2/3)^2}{1-(2/3)^5}=\frac{135}{211}\approx0.639810.$$
The ruin probability is $76/211\approx0.360190$. The expected duration is $(5h_2-2)/(1/5)=1265/211\approx5.995261$ plays. For comparison, the fair game has success probability $2/5$ and expected duration $2(5-2)=6$. The duration happens to be close here, despite a large change in the direction of absorption. Comparing just the mean duration would conceal the improvement in the probability of reaching the target.

**Your turn.** With the same boundaries and upward probability, what is the success probability from $x=1$?

::: {.callout-tip collapse="true" title="Answer"}
It is $[1-2/3]/[1-(2/3)^5]=81/211\approx0.383886$. Starting one unit above ruin leaves substantial short-run risk even in a favourable game.
:::

## Assumptions and limits — Removing the upper boundary
For $p>q$, sending $d$ to infinity gives an ultimate ruin probability $(q/p)^x$. For $p\le q$, ultimate ruin has probability one. This limit concerns the unbounded walk and should not be confused with the finite-target probability $h_x$. In the fair unbounded game, ruin is certain but the mean time to ruin is infinite. A probability-one termination statement therefore does not imply a finite expected duration; the finite upper boundary was essential to the geometric-block bound.{{cite:grinstead_snell1997}} (§12.2, gambler's ruin with an unlimited opponent)

The calculation assumes independent unit-sized steps with a fixed win probability. Variable stakes, dependence between plays, transaction costs and changing odds alter the recurrence or the state space. They cannot be accounted for by substituting an average win probability unless a separate model establishes that reduction. The endpoints $p=0$ and $p=1$ are deterministic walks and are handled directly, rather than by dividing by a zero probability.
