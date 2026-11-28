## Motivating example
Suppose a Markov chain Monte Carlo sampler begins at an extreme parameter value. Its first draws may still reflect that choice rather than the distribution we want to study. Discarding an initial stretch can reduce this starting-state effect, but the length must be judged in light of how the chain moves. A chain trapped in one part of a distribution will not be rescued merely by throwing away its early draws.{{cite:geyer1992}} (§3.7, p. 480){{cite:gelman_rubin1992}} (§§1.2–1.3, pp. 458–459)

## Intuition
An MCMC chain is built so that the target distribution is stationary: if the current state already has that distribution, one further transition preserves it. A chosen starting value generally has a different distribution. Early transitions still carry information about that start; as a suitable chain mixes, their distribution moves toward the target. **Burn-in**, also called **warm-up**, removes some of these early states from the averages and quantiles used for inference. It does not alter the transition rule or make later states independent.{{cite:geyer1992}} (§3.7, p. 480)

The distinction matters because two errors have different causes. Starting-state bias is about *where* the chain was initialized. Monte Carlo error is about how much information the retained, often correlated, draws contain. Increasing the warm-up may address the first but leaves strong serial dependence in the second. Geyer's separate discussions of spacing and burn-in make that separation explicit.{{cite:geyer1992}} (§§3.6–3.7, p. 480)

## Definition
**Direct posterior simulation** differs: drawing fresh independent pairs from a known factorisation produces a new target draw each time, so there is no initial segment to discard. Ordinary MCMC output may remain dependent after burn-in. For a chain $X_0,X_1,\ldots,X_T$ targeting a stationary distribution $\pi$, choose a nonnegative integer $B<T$ and retain $X_{B+1},\ldots,X_T$ for a Monte Carlo summary. The initial segment $X_0,\ldots,X_B$ is discarded as burn-in under this indexing convention. For an integrable function $h$, the retained average is
$$
\widehat{\mu}_{B,T}=\frac{1}{T-B}\sum_{t=B+1}^{T}h(X_t),
\qquad \mu=\E_{\pi}\{h(X)\}.
$$
The number $B$ is a computational choice, not a property of the target distribution. Other software may count the initial state differently, so the relevant record is which draws were retained. Burn-in should be accompanied by an assessment of whether the sampler explored the target well enough for the desired summary.{{cite:geyer1992}} (§3.7, p. 480){{cite:gelman_rubin1992}} (§1.3, pp. 458–459)

## Properties — What discarding changes
If the chain starts exactly from $\pi$, every state already has the target marginal distribution. No burn-in is needed to remove starting-state bias, though consecutive states may remain correlated. At the other extreme, if the chain cannot reach an important region at all, no finite discard length fixes the missing region. Between these cases, a longer warm-up can make the retained marginal distribution closer to $\pi$, but it leaves fewer observations for estimating summaries.{{cite:geyer1992}} (§3.7, p. 480){{cite:gelman_rubin1992}} (§§1.2–1.3, pp. 458–459)

The needed length depends on the transition kernel, the starting state, and the quantity being estimated. A trace of one coordinate can look settled while another coordinate or a separated mode has barely moved. Comparing chains begun in dispersed, valid parts of the parameter space helps expose such failures. Agreement is useful evidence, but a finite diagnostic cannot certify exact equilibrium.{{cite:gelman_rubin1992}} (§§1.2–1.3, pp. 458–459)

## Statistical use — Warm-up and adaptation
In a fixed-kernel sampler, burn-in primarily concerns the distribution of states relative to the start. In adaptive implementations, warm-up also trains the sampler. For example, Stan estimates a step size and a mass matrix during its warm-up stages; the latter uses the variation of warm-up draws to improve subsequent movement. This tuning gives a second reason to separate those iterations from the later sample used for inference. Merely dropping draws after a poorly tuned run would not reproduce that adaptation.

After warm-up, assess movement and compare independent chains for the summaries of interest. Estimate Monte Carlo error with methods that account for dependence rather than dividing a standard deviation by the square root of the raw draw count. The [autocorrelation function](autocorrelation-function.qmd) and [effective sample size](effective-sample-size.qmd) address this retained-sample precision, which burn-in alone cannot supply.{{cite:geyer1992}} (§§3.6–3.7, p. 480)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For the two-state chain in the worked example, let $p_t=\Pr(X_t=B)$. A move to $B$ comes from $A$ with probability $0.1$ or from $B$ with probability $0.8$, so
$$
p_{t+1}=0.1(1-p_t)+0.8p_t=0.1+0.7p_t.
$$
The fixed point solves $p=0.1+0.7p$, giving $p=1/3$. Subtracting it yields $p_{t+1}-1/3=0.7(p_t-1/3)$ and hence $p_t-1/3=0.7^t(p_0-1/3)$. Starting at $A$ gives $p_0=0$ and $p_t=(1-0.7^t)/3$; starting at $B$ gives $p_0=1$ and $p_t=1/3+(2/3)0.7^t$. On two states, total variation from $\pi$ is the absolute difference in the probability assigned to $B$. These formulas quantify starting-state decay for this particular kernel. They do not prove a universal burn-in rule.
:::
:::

## Worked example
Consider a hypothetical sampler with states $A$ and $B$ and row-stochastic transition matrix
$$
P=\begin{pmatrix}0.9&0.1\\0.2&0.8\end{pmatrix}.
$$
The stationary distribution is $\pi=(2/3,1/3)$, as multiplication by $P$ confirms. If the run starts at $A$, the proof gives $\Pr(X_t=B)=(1-0.7^t)/3$. After $t=5$ transitions this is $0.27731$, still below the stationary probability $1/3$. The total-variation distance is $0.0560233$. After $t=10$, the probability is $0.3239174917$ and the distance has fallen to $0.0094158416$. Thus discarding at least ten initial transitions would put the distribution of the next state within about one percentage point of stationarity *for this start and this model*. It would not turn the retained sequence into independent draws or establish that a different sampler has mixed.{{cite:geyer1992}} (§3.7, p. 480, motivation for assessing initial iterations)

**Your turn.** For the same matrix, start at $B$ instead. Find $\Pr(X_5=B)$ and its total-variation distance from the stationary distribution. Why is the distance larger than it was after five steps from $A$?

::: {.callout-tip collapse="true" title="Answer"}
Starting at $B$ gives $p_0=1$. The recursion in the proof yields $p_5=1/3+(2/3)(0.7)^5=0.44538$, and the total-variation distance is $(2/3)(0.7)^5=0.1120467$. Starting at $A$ put only $1/3$ of probability mass away from the stationary $B$ probability, whereas starting at $B$ put $2/3$ away. Both deviations shrink by the same factor $0.7$ per step, so the second remains twice as large at every positive time.
:::

## Common misconceptions
Warm-up is not a guarantee of convergence: a fixed number of discarded draws says nothing by itself about a chain's access to all important regions. It is not thinning: removing an initial block addresses the start, while retaining every $k$th later state changes spacing. It does not make retained observations independent, even when their marginal distribution is close to the target. Nor does an attractive trace plot of one scalar certify that a high-dimensional joint distribution has been explored. These are distinct questions about bias, sampling frequency, dependence, and incomplete exploration.{{cite:geyer1992}} (§§3.6–3.7, p. 480){{cite:gelman_rubin1992}} (§1.2, pp. 458–459)

## Assumptions and limits — When discarding fails
Suppose a sampler targeting two separated modes proposes only tiny local moves and remains in the first mode for the whole run. Discarding its first half still leaves draws from that one region; its estimate of the other mode's probability will be near zero. Several dispersed chains may reveal the mismatch if some begin in the second mode, but even agreement between finite runs cannot rule out an unseen region. A reducible chain is a sharper failure: if its transition rule never crosses between two positive-mass classes, no amount of burn-in can recover the intended target from a start in one class. The transition mechanism must be repaired.{{cite:gelman_rubin1992}} (§§1.2–1.3, pp. 458–459)

## Connections
[Stationary distributions](stationary-distribution.qmd) describe the target preserved by a transition kernel. [Irreducibility](irreducible-markov-chain.qmd) and [aperiodicity](aperiodic-markov-chain.qmd) help determine whether a finite chain approaches it from different starts. [Trace plots](trace-plot.qmd), multiple chains, and [autocorrelation](autocorrelation-function.qmd) reveal different aspects of a run; none can replace a correct transition rule. The worked answers for [Gibbs, Metropolis–Hastings, and Monte Carlo error](../questions/q-25.qmd) and [conditional versus marginal sampling](../questions/q-43.qmd) apply this distinction when deciding whether warm-up is needed and how retained draws should be summarised.{{cite:gelman_rubin1992}} (§1.3, pp. 458–459)

## History
The broad Monte Carlo method predates MCMC's modern diagnostic language: Monte Carlo calculation became associated in the mid-twentieth century with numerical work by von Neumann, Ulam, and Metropolis. Geyer's 1992 discussion explicitly named the “burn-in” or “warm-up” problem and treated its length as a question about reaching equilibrium. In the same year, Gelman and Rubin argued that multiple sequences from dispersed starts provide information a single apparently settled sequence may miss. Modern adaptive samplers also use warm-up to tune their transitions.{{cite:dodge2008}} (pp. 359–360, “Monte Carlo Method”){{cite:geyer1992}} (§3.7, p. 480){{cite:gelman_rubin1992}} (§1.3, pp. 458–459)
