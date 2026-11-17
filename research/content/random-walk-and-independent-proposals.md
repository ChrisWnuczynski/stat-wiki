## Motivating example
Suppose a posterior distribution has two separated regions of appreciable probability. A proposal that takes small steps from the current state may spend a long time in one region. Drawing candidates from a fixed distribution could jump across the gap, but those candidates may be poorly matched to the posterior. Both designs can target the same distribution if their acceptance probabilities account for how candidates are proposed.{{cite:hastings1970}} (§§2.1–2.3, pp. 99–101)

## Intuition
A **random-walk proposal** adds a random displacement to the current state. It explores nearby values and is often easy to tune locally. An **independent proposal** draws the candidate from a fixed density $g$, regardless of the current state. The word *independent* describes the candidate-generating rule, not the resulting accepted chain: rejection can repeat the current state, and successive retained states are generally dependent.{{cite:hastings1970}} (§§1, 2.1, pp. 97–100)

The acceptance step corrects the proposal's directional bias. If a move from $x$ to $y$ is proposed more readily than its reverse, the algorithm must account for that difference to preserve the target distribution. In a symmetric random walk the proposal factors cancel. In an independence sampler the factors are $g(x)$ and $g(y)$, which ordinarily differ and must remain in the ratio.{{cite:hastings1970}} (§2.2, pp. 99–100)

## Definition
Let $\pi$ denote a target mass or density and $q(y\mid x)$ the proposal probability or density of candidate $y$ given current state $x$. When both directions are admissible, the Metropolis–Hastings acceptance probability is
$$
a(x,y)=\min\left\{1,\frac{\pi(y)q(x\mid y)}{\pi(x)q(y\mid x)}\right\}.
$$
If the proposal is accepted, the next state is $y$; otherwise it is $x$ again. An unknown normalising constant in $\pi$ cancels from the ratio. Rejected states remain part of the chain and its averages.{{cite:metropolis1953}} (§II, p. 1088){{cite:hastings1970}} (§§2.1–2.2, pp. 99–100)

For $Y=x+Z$ with a symmetric increment law, $q(y\mid x)=q(x\mid y)$ and $a(x,y)=\min\{1,\pi(y)/\pi(x)\}$. This is the familiar Metropolis ratio. For a fixed candidate law $q(y\mid x)=g(y)$, the ratio becomes $\pi(y)g(x)/\{\pi(x)g(y)\}$. Equivalently, with weight $w(z)=\pi(z)/g(z)$, accept with probability $\min\{1,w(y)/w(x)\}$. Independence of $Y$ from $x$ does **not** make the proposal correction disappear.{{cite:hastings1970}} (§§2.1–2.2, pp. 99–100)

## Properties — Why both preserve the target
The defining balance is pairwise: stationary probability flowing from $x$ to $y$ equals the reverse flow. The acceptance rule makes each flow the smaller of the two proposed directional flows. This explains at once why a symmetric proposal has a simpler ratio and why a lopsided independent proposal needs the $g(x)/g(y)$ factor. Balance establishes that $\pi$ is stationary; access to all target regions and suitable recurrence are still needed for convergence from an arbitrary starting state.{{cite:hastings1970}} (§§2.1–2.2, pp. 99–100)

A proposal also needs support where the target has support. If $g(y)=0$ on a positive-target region $y$, an independence sampler starting elsewhere never proposes that region. A local random walk can be irreducible yet take a very long time to cross a low-probability valley. These are different obstacles: one is impossible access, the other is slow exploration.{{cite:hastings1970}} (§§2.1–2.3, pp. 99–101)

## Statistical use — Choosing a proposal
Small random-walk steps tend to have high acceptance but may carry little new information per transition. Very large steps can repeatedly land in low-target-density locations and be rejected. The trace figure for a Normal target illustrates both extremes and a moderate proposal scale. Hastings's own Normal example likewise found poor estimates with an extremely small step size. An acceptance rate is therefore useful only together with how far the chain moves and how quickly its output decorrelates.{{cite:hastings1970}} (§2.3, Example 2, p. 101)

An independent proposal can make long-distance moves and can be attractive when $g$ approximates $\pi$ over all important regions. If $g=\pi$, every proposal is accepted and draws can be independent. If $g$ has light tails or misses a mode, proposed moves from a badly represented region may be rarely accepted, and the chain can remain stuck. The choice between local and global proposals is consequently a choice about the geometry of the target and the cost of evaluating candidates, not a contest of acceptance percentages alone.{{cite:hastings1970}} (§§1, 2.3, pp. 97–101)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For distinct states with positive proposed flows, write $A=\pi(x)q(y\mid x)$ and $B=\pi(y)q(x\mid y)$. The acceptance rule gives
$$
\pi(x)q(y\mid x)a(x,y)=A\min(1,B/A)=\min(A,B).
$$
Reversing $x,y$ gives $B\min(1,A/B)=\min(A,B)$ as well. If one proposed flow is zero, the corresponding accepted flow is zero in both directions. Thus detailed balance holds for every pair, and summing or integrating over previous states proves stationarity of $\pi$. This proof does not establish irreducibility or rapid mixing. For a symmetric random walk, $q(x\mid y)=q(y\mid x)$ cancels; for an independence proposal, substituting $q(y\mid x)=g(y)$ and $q(x\mid y)=g(x)$ gives the two specialised ratios above.{{cite:hastings1970}} (§2.2, pp. 99–100)
:::
:::

If an independent proposal assigns zero mass to a target mode, the chain cannot discover that mode from another starting state; detailed balance on accessible states does not rescue the missing support. If a random walk crosses a low-density valley only through many unlikely intermediate states, it may be formally able to reach both modes yet practically remain in one during a finite run. An enormous proposal spread can create another failure: most candidates fall in negligible-target regions and the chain repeats its state. The remedies involve the proposal and convergence assessment, not merely discarding a longer warm-up segment.{{cite:hastings1970}} (§§2.1–2.3, pp. 99–101)

## Worked example
Take a hypothetical target on states $0,1,2$ with probabilities $\pi=(1/2,1/3,1/6)$. A local proposal moves between neighbouring states with probability $1/2$ in each direction; at either endpoint it uses the remaining $1/2$ to propose staying put. Thus $q(1\mid0)=q(0\mid1)=1/2$, and similarly for states $1$ and $2$. This proposal is symmetric. For a proposed move $0\to1$, its acceptance probability is $\min\{1,(1/3)/(1/2)\}=2/3$. The accepted stationary flow is $\pi(0)q(1\mid0)a(0,1)=(1/2)(1/2)(2/3)=1/6$, equal to the reverse flow $(1/3)(1/2)(1)=1/6$.{{cite:hastings1970}} (§2.2, symmetric Metropolis case, p. 100)

Now propose independently with $g=(1/6,1/2,1/3)$. For the *same* move, the acceptance probability is
$$
a(0,1)=\min\left\{1,\frac{(1/3)(1/6)}{(1/2)(1/2)}\right\}=\frac29.
$$
The forward stationary flow is $(1/2)(1/2)(2/9)=1/18$, matching the reverse flow $(1/3)(1/6)(1)=1/18$. Using only the target ratio $2/3$ here would leave the two flows unequal and change the stationary law. The example makes the Hastings correction visible even though both proposal mechanisms target the same $\pi$.{{cite:hastings1970}} (§2.2, pp. 99–100)

**Your turn.** From state $1$, consider a proposed move to state $2$. Find the acceptance probability under the symmetric local proposal and under $g=(1/6,1/2,1/3)$. Explain why they differ.

::: {.callout-tip collapse="true" title="Answer"}
The local proposal is symmetric, so $a_{\mathrm{RW}}(1,2)=\min\{1,(1/6)/(1/3)\}=1/2$. For the independent proposal, reverse and forward candidate probabilities are $g(1)=1/2$ and $g(2)=1/3$, giving $a_{\mathrm{ind}}(1,2)=\min\{1,(1/6)(1/2)/[(1/3)(1/3)]\}=3/4$. The target density decreases by the same factor in both cases; the independent proposal's directional imbalance changes the required correction.
:::

## Common misconceptions
An independent *proposal* is not an independent *sample*: rejection and state-dependent acceptance couple successive states. Proposal symmetry means $q(y\mid x)=q(x\mid y)$ for the two directions of a move, not that the target is symmetric. A high acceptance rate does not certify efficient exploration; a tiny random-walk step can be accepted almost always while barely moving. Finally, the target normalising constant cancels, but an asymmetric proposal ratio does not. These are separate statements about dependence, proposal geometry, efficiency, and algebra.{{cite:hastings1970}} (§§1, 2.1–2.3, pp. 97–101)

## Connections
[Metropolis–Hastings invariance](metropolis-hastings-invariance.qmd) gives the balance principle behind both designs. [Burn-in](burn-in.qmd) addresses initial-state influence, while [trace plots](trace-plot.qmd) and [autocorrelation](autocorrelation-function.qmd) help assess exploration and retained-sample precision. [Metropolis–Hastings cancellations](../questions/c-14.qmd) tests when target and proposal factors cancel; [An independent Gamma proposal](../questions/ex-applied-gamma-mh.qmd) derives the non-cancelling correction on a continuous target rather than the three-state example here.{{cite:hastings1970}} (§§2.1–2.3, pp. 99–101)

## History
Metropolis and coauthors' 1953 molecular simulation proposed local symmetric displacements and accepted energetically unfavourable moves with a probability tied to their energy difference. Their procedure retained repeated states after rejection. Hastings's 1970 generalisation made the direction-dependent proposal ratio explicit, enabling a much broader range of candidate mechanisms while preserving the desired equilibrium. Those Markov-chain methods grew out of that earlier numerical-simulation setting.{{cite:metropolis1953}} (§II, pp. 1087–1088){{cite:hastings1970}} (§§1–2.2, pp. 97–100){{cite:dodge2008}} (pp. 359–360, “Monte Carlo Method”)
