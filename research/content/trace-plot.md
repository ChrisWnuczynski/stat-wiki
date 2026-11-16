## Lead context
A trace plot draws each sampled sequence against iteration so that a chain stuck in one region can be seen beside a chain that never entered it.{{cite:gelman_rubin1992}} (§1.2, pp. 457–458)

## Motivating example
Two short sequences are supposed to be draws from the same target. The first alternates $0,1,0,1$. The second alternates $5,6,5,6$. Each sequence, read alone, looks stable: it moves by $1$ and returns. Drawn on one plot against iteration, the two paths occupy different horizontal bands and never meet. A histogram that pooled them would show two spikes and would not reveal that no single sequence visited both spikes. The trace is the picture of that separation; the between-sequence variance is the matching number.{{cite:gelman_rubin1992}} (§2.2, pp. 460–461)

## Intuition — One path cannot see the gap it never crosses
A Markov chain Monte Carlo sequence is a path $x^{(1)},x^{(2)},\ldots$ from a transition that is intended to leave the target distribution invariant. Plotting the scalar $x^{(t)}$ against $t$ shows whether this path is travelling or sitting still. A path that drifts, that stays constant because proposals are rejected, or that lives in a different band from a second path started elsewhere, has not yet represented the whole target. A calm path is not a proof that the transition is correct, and it is not a proof that every important region has been entered. Gelman and Rubin’s point is that a single finite sequence can remain under the influence of its start for many iterations, and that the summaries of a lower-dimensional function can look unimodal even when the chain has missed a mode.{{cite:gelman_rubin1992}} (§1.2, pp. 457–458)

Several sequences, started from a distribution more spread out than the target, make the missing region visible as a difference among the sequences. Discarding an initial stretch reduces the pull of a bad start. It does not create the visits that none of the sequences made.{{cite:gelman_rubin1992}} (§2.2, pp. 460–461)

## Definition
For a scalar function of the sampler’s state, the trace plot is the graph of that function against iteration index, usually with one line for each independent sequence. After a warm-up prefix has been dropped, Gelman and Rubin compare the sequences through two quantities. If $m\ge 2$ sequences each retain $n$ draws, $B/n$ is the sample variance of the $m$ sequence means and $W$ is the average of the $m$ within-sequence sample variances. The variance estimate that mixes them is
$$
\hat\sigma^{2}=\frac{n-1}{n}W+\frac{1}{n}B.
$$
If the sequences are still in different regions, $B$ is large relative to $W$ and $\hat\sigma^{2}$ is much larger than the within-sequence variance. If only one sequence is run, $B$ cannot be calculated.{{cite:gelman_rubin1992}} (§2.2, eq. 3, pp. 460–461)

## Properties — Between-sequence variance is invisible on one trace
The comparison of $\hat\sigma^{2}$ with $W$ is a numerical reading of what several traces show at once.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Each within-sequence variance uses only the draws in that sequence, so a sequence that never leaves a small interval contributes a small term to $W$ even when another sequence lives far away. The sample variance of the sequence means, $B/n$, is zero only when all the sequence means agree. Substituting into equation (3),
$$
\hat\sigma^{2}-W=\frac{1}{n}(B-W).
$$
Thus $\hat\sigma^{2}>W$ exactly when $B>W$. A single sequence supplies no second mean, so this difference is undefined and a trace that looks locally stable cannot be checked against a between-sequence gap. Under stationarity the mixture $\hat\sigma^{2}$ is unbiased for the target variance, while for finite $n$ it remains larger than the within-sequence variance precisely to the extent that the sequence means still differ.{{cite:gelman_rubin1992}} (§2.2, eq. 3, pp. 460–461)
:::
:::

The published potential scale reduction multiplies a square-root variance ratio by a degrees-of-freedom factor that tends to $1$ as $n$ grows. The factor does not tend to $1$ when separate sequences remain near separate modes: further draws inside the wrong mode do not by themselves close the gap between the means.{{cite:gelman_rubin1992}} (§2.2 and §2.4, pp. 461)

## Statistical use — Read the traces, then the variance ratio
Draw every sequence on the same axes after the same warm-up rule. Look for a band that one sequence never enters, for a flat stretch of rejections, and for a slow drift that has not settled by the last iteration. Then compute $W$ and $B$ for each scalar of interest. A ratio $\hat\sigma^{2}/W$ near $1$ is evidence that the retained draws from these sequences occupy a common scale. It is not evidence that the transition kernel leaves the intended posterior invariant, and it is not evidence about a mode that none of the starting points reached. Posterior means and interval endpoints are averages of the retained draws. They inherit whatever region the traces actually visited.{{cite:gelman_rubin1992}} (§1.2 and §2.2, pp. 457–461)

## Worked example
Take $m=2$ sequences of length $n=4$, after warm-up. Sequence $1$ is $0,1,0,1$, with mean $0.5$. The squared deviations from $0.5$ sum to $1$, so the within-sequence variance is $1/3$. Sequence $2$ is $5,6,5,6$, with mean $5.5$ and the same within-sequence variance $1/3$. Hence $W=1/3$. The two means differ from their average $3$ by $2.5$ each, so
$$
\frac{B}{n}=\frac{(2.5)^{2}+(2.5)^{2}}{2-1}=12.5,\qquad B=50.
$$
Equation (3) gives
$$
\hat\sigma^{2}=\frac{3}{4}\cdot\frac{1}{3}+\frac{1}{4}\cdot 50=0.25+12.5=12.75.
$$
The ratio $\hat\sigma^{2}/W=12.75/(1/3)=38.25$, and $\sqrt{38.25}\approx 6.185$. The traces sit about $5$ units apart while each wiggles by $1$, and the variance ratio reports that separation. Replace both sequences by $1,2,1,2$. Then both means equal $1.5$, so $B=0$, $W=1/3$ and $\hat\sigma^{2}=(3/4)(1/3)=0.25$. The ratio $\hat\sigma^{2}/W=3/4$ is below $1$: with no between-sequence gap, equation (3) shrinks $W$ by $(n-1)/n$. A trace of either sequence would show the same small oscillation, and the second sequence would lie on top of the first.{{cite:gelman_rubin1992}} (§2.2, eq. 3, pp. 460–461)

**Your turn.** One sequence of length $4$ is $2,2,2,2$ and the other is $2,4,2,4$. Find the two means, $W$, and $B/n$.

::: {.callout-tip collapse="true" title="Answer"}
The means are $2$ and $3$. The first within-sequence variance is $0$. The second has squared deviations $1,1,1,1$ from its mean $3$, summing to $4$, so its variance is $4/3$. Thus $W=(0+4/3)/2=2/3$. The variance of the two means is $(2-2.5)^{2}+(3-2.5)^{2}=0.5$, and that quantity is $B/n$. The traces share the value $2$ but one of them also reaches $4$, so a single glance at the constant sequence would miss half of the visited range.{{cite:gelman_rubin1992}} (§2.2, pp. 460–461)
:::

## Common misconceptions
A tidy trace is not a convergence proof. It is one finite path. Several tidy traces that agree are stronger, and they still do not prove that the transition leaves the target invariant. The histogram of the pooled draws is not a trace: the histogram discards the order and the sequence labels, which are exactly what show a stuck chain. Thinning, keeping every $k$th draw, makes a trace look less dependent and throws away draws; it does not make $B$ small if the sequences began in different modes. Discarding a warm-up prefix is a practical reduction of the influence of the start, not a theorem that the retained draws are from the target.{{cite:gelman_rubin1992}} (§1.2 and §2.4, pp. 457–458, 461)

## Assumptions and limits — Separated modes and a single sequence
Equation (3) needs $m\ge 2$. One trace, however long, leaves $B$ undefined. Lengthening a chain that is trapped in one mode reduces Monte Carlo error inside that mode and does not estimate the mass of a mode it never entered. Gelman and Rubin note that the scale-reduction summary will not fall to $1$ while sequences remain near the modes where they started, and that the sampler itself may have to be changed, by reparameterisation or by a move that can jump modes, before further iterations help.{{cite:gelman_rubin1992}} (§2.4, p. 461)

The variance split is for a scalar function of the state. A trace of one coordinate can look mixed while another coordinate is stuck. Each scalar that will be reported needs its own trace and its own $W$ and $B$. The normal approximation they attach to the combined variance is a summary device for the Monte Carlo estimates. It describes the sampling distribution of those estimates under their regularity conditions.{{cite:gelman_rubin1992}} (§1.1 and §2.2, pp. 457–461)

## Connections
The [autocorrelation function](autocorrelation-function.qmd) summarises dependence along one sequence; the trace shows the path that produced those correlations. [Effective sample size](effective-sample-size.qmd) converts that dependence into an equivalent number of independent draws, and it still describes only the region the sequences visited. [Warm-up](burn-in.qmd) is the discarded prefix in the multiple-sequence protocol. The [Gibbs sampler](gibbs-sampling.qmd) and [Metropolis–Hastings](metropolis-hastings-algorithm.qmd) are two transitions whose output is commonly drawn this way; a valid trace does not distinguish which transition was used.{{cite:gelman_rubin1992}} (§1 and §2.2, pp. 457–461)

## Check yourself
### A separated pair {#self-check-trace-ratio}

Sequences $0,1,0,1$ and $5,6,5,6$ give $W=1/3$ and $\hat\sigma^{2}=12.75$. Why does a histogram of the eight numbers fail to show what the trace shows?

::: {.callout-tip collapse="true" title="Answer"}
The histogram records that the values $0$, $1$, $5$ and $6$ occurred. It does not record that one sequence produced only $0$ and $1$ while the other produced only $5$ and $6$. The trace, and the gap between the means that enters $B$, keep the sequence labels.{{cite:gelman_rubin1992}} (§2.2, pp. 460–461)
:::

### When $B$ is zero {#self-check-trace-agree}

Both sequences are $1,2,1,2$, so $B=0$ and $W=1/3$. What is $\hat\sigma^{2}$, and why is a second trace still worth drawing?

::: {.callout-tip collapse="true" title="Answer"}
Equation (3) gives $\hat\sigma^{2}=(3/4)(1/3)=0.25$. The second trace is what makes $B$ a number rather than an undefined symbol. Agreement of the two paths is the observation that $B=0$; one path alone cannot show agreement with a path that was never run.{{cite:gelman_rubin1992}} (§2.2, eq. 3, pp. 460–461)
:::

### One chain, two modes {#self-check-trace-one}

A target has two well-separated modes. A single sequence of length $10{,}000$ stays in the mode where it started, and its trace looks stable. What does equation (3) refuse to provide?

::: {.callout-tip collapse="true" title="Answer"}
It refuses $B$. With one sequence there is no variance among sequence means, so the comparison of between-sequence and within-sequence variation cannot be formed. Stability inside the visited mode does not estimate the unvisited mode.{{cite:gelman_rubin1992}} (§2.2, p. 461)
:::

## History
Gelman and Rubin’s 1992 paper in *Statistical Science* recommended several independent sequences, started from a distribution more dispersed than the target, and a variance estimate that combines the within-sequence variance $W$ with the between-sequence term $B$. They contrasted that numerical comparison with earlier monitoring that looked at graphs or at $B$ alone. The trace plot is the display on which the disagreement those formulae measure is visible iteration by iteration.{{cite:gelman_rubin1992}} (§1–2, pp. 457–461)
