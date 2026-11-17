## Motivating example

Imagine sampling a posterior with two well-separated peaks. A chain started in the left peak may settle into small local fluctuations after a few hundred iterations. Removing those early iterations makes its later trace look calm, yet no recorded state may have reached the right peak. A posterior mean computed from that trace then describes only one region. The difficulty is movement *between* important regions, not simply an untidy beginning. Gelman and Rubin studied precisely the risk that a finite chain can remain near its starting region; Geyer emphasized the need to assess Monte Carlo error in the retained run. {{cite:gelman_rubin1992}} (§§1.2–1.4, pp. 458–459){{cite:geyer1992}} (§§3.3–3.7, pp. 477–480)

## Intuition

Warm-up addresses initialization. A transition rule can have the correct stationary distribution while its state at a finite time still depends on where it started. Discarding a prefix may lessen that dependence, but the chosen length does not change the transition rule or open a route through a low-probability barrier. Once a chain is stationary, successive draws may remain strongly correlated; stationarity and independent information are separate questions. The proposal-scale figure illustrates that tiny accepted moves and long rejection runs can both make exploration slow even when the target is simple. {{cite:geyer1992}} (§§2–3.7, pp. 474–480){{cite:gelman_rubin1992}} (§1.2, p. 458)

## Definition — What discarding warm-up does

If $X_0,X_1,\ldots$ is a Markov chain targeting $\pi$, selecting a warm-up length $B$ means estimating posterior quantities from $X_{B+1},\ldots,X_{B+L}$ rather than the whole path. The operation removes observations. It neither changes the law of the chain at time $B+1$ nor establishes that this law equals $\pi$. The validity of the transition kernel's stationary distribution, convergence from the chosen start, and the precision of estimates from dependent draws all require their own arguments or diagnostics. {{cite:geyer1992}} (§§1–3.7, pp. 473–480)

## Properties — A slow two-state chain

An exact example makes the gap visible. Let a chain move between states $A$ and $B$ with probability $p$ at each step and otherwise stay put. For $0<p<1$, its stationary distribution assigns probability $1/2$ to each state. Starting at $A$, the probability of still being at $A$ after $t$ steps is $\{1+(1-2p)^t\}/2$. The probability of *no switch at all* is $(1-p)^t$; this is a different event, because a path can switch twice and return to $A$. Both probabilities may remain large long after an arbitrary warm-up length. {{cite:gelman_rubin1992}} (§1.2, p. 458, slow-chain motivation)

::: {.callout-note collapse="true" title="Proof"}
The transition matrix is $\begin{pmatrix}1-p&p\\p&1-p\end{pmatrix}$, so the equal-mass distribution is stationary. Write $u_t=\Pr(X_t=A\mid X_0=A)$. Conditioning on the previous state gives $u_{t+1}=(1-p)u_t+p(1-u_t)=p+(1-2p)u_t$. Thus $u_{t+1}-1/2=(1-2p)(u_t-1/2)$; with $u_0=1$, iteration gives $u_t=\{1+(1-2p)^t\}/2$. No switch requires a stay at every step, giving $(1-p)^t$. These formulas also show that convergence of the one-time law is gradual when $p$ is small.
:::

## Statistical use — Assessing the retained draws

Run chains from dispersed plausible starting regions and inspect trace plots for movement across regions that matter. Compare within-chain and between-chain behaviour, and assess effective sample size and Monte Carlo error for each estimand of interest. A discrepancy between chains can reveal a problem, but agreement is not a certificate if every chain began in the same basin or all missed a narrow mode. Extend or redesign the sampler when exploration is poor; discarding more output from the same trapped path cannot create visits that did not occur. {{cite:gelman_rubin1992}} (§§1.3–2.4, pp. 458–462){{cite:geyer1992}} (§§3–4, pp. 477–481)

Thinning concerns a different choice: it records fewer of the post-warm-up states. It may reduce storage or the cost of later processing, but weaker visible serial dependence among saved states does not mean that the original run explored more of the target. For negligible storage cost, Geyer shows that discarding intermediate states sacrifices precision for a fixed amount of chain computation. {{cite:geyer1992}} (§3.6, p. 480)

For a two-mode posterior separated by a very low-density region, local proposals may rarely cross even in a long run; deleting its first half can leave every saved draw in the initial mode. For a random-walk Metropolis chain with tiny proposal steps, the acceptance rate can approach one while movement across the target is painfully slow. A sampler with a coding error may converge smoothly to the *wrong* stationary distribution. Warm-up alone cannot diagnose any of these failures, and no finite diagnostic proves exploration of an unseen region. {{cite:gelman_rubin1992}} (§§1.2–2.4, pp. 458–462){{cite:geyer1992}} (§§3.7–4, pp. 480–481)
## Worked example

Take the two-state chain with $p=0.001$, start at $A$, and discard $1{,}000$ steps. The probability that it never switched during warm-up is $0.999^{1000}\approx0.36770$. Its probability of being at $A$ at that point is $\{1+0.998^{1000}\}/2\approx0.56753$, still above the stationary value $0.5$. This does not say that every retained run is biased in the same direction: it says that even a seemingly generous fixed warm-up leaves appreciable starting-state dependence for this slow chain. If the run records only $A$ states afterwards, its estimated probability for $A$ is $1$ although the target probability is $0.5$. {{cite:gelman_rubin1992}} (§1.2, p. 458, finite-run trap)

**Your turn.** Keep the chain and start at $A$, but set $p=0.0001$ and discard $1{,}000$ steps. Find the chance of no switch and the chance that the state at the end is $A$. Which quantity can be read directly from a path that never changes state?

::: {.callout-tip collapse="true" title="Answer"}
The no-switch probability is $0.9999^{1000}\approx0.90483$. The chance of ending at $A$ is $\{1+0.9998^{1000}\}/2\approx0.90936$. A constant observed path shows that no switch occurred along *that path*, but the chance of ending at $A$ also includes paths that switched an even number of times. The stationary probability is still $0.5$.
:::

## Common misconceptions

A settled-looking trace is not proof of stationarity: a path can fluctuate within one mode while missing another. Removing a large number of iterations does not make successive retained draws independent: their correlation comes from the transition rule. A high acceptance fraction alone does not establish good movement, since very small proposals can be accepted almost always. Conversely, poor between-chain agreement is evidence of a problem, while agreement of all chains is only a diagnostic with limits. {{cite:gelman_rubin1992}} (§§1.2–2.4, pp. 458–462){{cite:geyer1992}} (§§3.6–4, pp. 480–481)

## Connections

[Burn-in](burn-in.qmd) names the discarded prefix, while [effective sample size](effective-sample-size.qmd) concerns precision in the retained sequence. [Autocorrelation](autocorrelation-function.qmd) measures one aspect of dependence, and a [trace plot](trace-plot.qmd) can expose long sticking periods. The [Metropolis–Hastings algorithm](metropolis-hastings-algorithm.qmd) specifies a kernel targeting a distribution, but its proposal determines how quickly it moves across that distribution. {{cite:geyer1992}} (§§1–3.7, pp. 473–480)

## History

The early practical MCMC literature treated initialization and monitoring as distinct questions. Geyer's 1992 discussion explicitly called the discarded-prefix problem “burn-in” or “warm-up” and connected its choice to autocovariance and precision. Gelman and Rubin's 1992 multiple-sequence method addressed the danger of a chain confined near its starting region and examined where its diagnostic could reveal, but not repair, poor exploration. {{cite:geyer1992}} (§3.7, p. 480){{cite:gelman_rubin1992}} (§§1.2–2.4, pp. 458–462)
