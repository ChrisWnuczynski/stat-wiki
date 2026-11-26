## Lead context
A geometric distribution counts how many independent trials are needed until the first success, when each trial has the same success probability.

## Motivating example
A machine accepts a part with probability $0.2$ on every independent attempt. The number of attempts until the first acceptance has mean $1/0.2=5$. The chance that the first three attempts all fail is $(0.8)^3=0.512$, so more than half of such waits run past three attempts even though the mean wait is five. The count of failures before the first success has mean $4$, one less than the trial count. Both counts are called geometric, and they are not the same random variable.{{cite:dodge2008}} (pp. 226–227)

## Intuition
The probabilities of the trial counts $1,2,3,\ldots$ are $p$, $p(1-p)$, $p(1-p)^2$, and so on. Each term is the previous term multiplied by the failure probability $1-p$. That is a geometric progression, which is why the family has this name. Stopping at the first success is the negative-binomial law with the number of required successes equal to one.{{cite:dodge2008}} (p. 226)

The lack of memory is the same progression read from the middle. If the first $s$ trials have failed, the number of further trials still needed has the same law as a fresh count. The machine does not become due.

## Definition
On this page $X$ is the trial of the first success, with
$$
\mathrm{P}(X=x)=p(1-p)^{x-1},\qquad x=1,2,3,\ldots,
$$
mean $1/p$, and variance $(1-p)/p^2$. Another convention lets the variable count the failures before the first success, with mass $p(1-p)^k$ on $k=0,1,2,\ldots$, mean $(1-p)/p$, and variance $(1-p)/p^2$. The variances agree. The means differ by $1$, because the trial count is the failure count plus one.{{cite:dodge2008}} (pp. 226–227)

The survival function on this page is $\mathrm{P}(X>m)=(1-p)^m$ for integers $m\ge 0$. That is the chance of $m$ failures in a row.

## Properties
The tail sum gives the mean, and the same tail gives the memoryless property.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For a positive integer-valued variable, $\mathrm{E} X=\sum_{m=0}^{\infty}\mathrm{P}(X>m)$. Here $\mathrm{P}(X>m)=(1-p)^m$, and the geometric series sums to $1/p$.

The second moment follows from the failure-count formula. If $K=X-1$, the failure-count formulas give $\mathrm{E} K=(1-p)/p$ and $\mathrm{Var}(K)=(1-p)/p^2$. Adding the constant $1$ does not change the variance, and $\mathrm{E} X=\mathrm{E} K+1=1/p$.{{cite:dodge2008}} (pp. 226–227)

For integers $s,t\ge 0$,
$$
\mathrm{P}(X>s+t\mid X>s)=\frac{(1-p)^{s+t}}{(1-p)^s}=(1-p)^t=\mathrm{P}(X>t),
$$
provided $p<1$. The conditional remaining wait has the same law as $X$.
:::
:::

## Related distributions
A single Bernoulli trial is the success indicator on one attempt. The geometric law stacks independent copies of that trial until the first success. A negative binomial count of trials until $r$ successes is the sum of $r$ independent copies of this geometric law, all with the same $p$. A Poisson number of events in a fixed interval is a different story: it counts events in time, rather than trials until one success.

## Statistical inference
**One success probability, independent trials.** The likelihood for an observed trial count $x$ is $p(1-p)^{x-1}$. For one observation the maximiser is $1/x$ when $x\ge 1$. For independent copies $X_1,\ldots,X_n$ the likelihood depends on the data through $\sum X_i$, and the maximiser is $n/\sum X_i$, the reciprocal of the sample mean. That estimator is the success probability that matches the observed mean wait to $1/p$. For finite $n\ge 1$ and $0<p<1$, $\overline X$ is nondegenerate and $x\mapsto 1/x$ is strictly convex on $x>0$, so Jensen's inequality gives $\E[1/\overline X]>1/\E[\overline X]=p$: the estimator is upward biased. At $p=1$, every observation and the estimator are identically $1$, so the estimator is unbiased.

A sample that includes a coded zero, from software that counts failures, is one smaller than the trial count used here. Feeding those zeros to the trial-count likelihood treats an immediate success as an impossible observation.

## Generating random samples
Draw independent Bernoulli trials with success probability $p$ and record the attempt number of the first success. The same draw minus one is the failure count. A generator that returns values in $\{0,1,2,\ldots\}$ is using the failure convention. Adding one converts it to the trial convention on this page. Using the returned zero as a trial count makes $\mathrm{P}(X=1)$ look like a point mass at an illegal value.

## Worked example
Let $p=0.2$. Then $\mathrm{P}(X=1)=0.2$, $\mathrm{P}(X=2)=0.8\cdot 0.2=0.16$, and $\mathrm{P}(X=3)=0.8^2\cdot 0.2=0.128$. These three masses sum to $0.488$. The chance of a wait longer than three trials is $0.512$. The mean is $5$ and the variance is $0.8/0.2^2=20$, so the standard deviation is $\sqrt{20}\approx 4.472$. A wait of ten trials is about $1.118$ standard deviations above the mean, and it is not rare: $\mathrm{P}(X>10)=0.8^{10}\approx 0.1074$.{{cite:dodge2008}} (pp. 226–227)

The failure count has mean $4$ and the same variance $20$. Reporting a mean of $4$ for the trial of the first success would be the other convention.

**Your turn.** Still with $p=0.2$, the first two trials have failed. Find the conditional probability that the wait exceeds five trials, and the conditional mean of the remaining number of trials.

::: {.callout-tip collapse="true" title="Answer"}
Memorylessness gives $\mathrm{P}(X>5\mid X>2)=\mathrm{P}(X>3)=0.8^3=0.512$. The remaining number of trials has the original geometric law, so its conditional mean is $5$, not $5-2$.
:::

**Check yourself.** For $p=1/4$, the survival $\mathrm{P}(X>3)=(3/4)^3$ equals $27/64$. What is the mean trial count, and what is the mean failure count?

::: {.callout-tip collapse="true" title="Answer"}
The trial-count mean is $1/(1/4)=4$. The failure-count mean is $(3/4)/(1/4)=3$. The survival probability $27/64\approx 0.4219$ belongs to the trial count, because $X>3$ means the first three trials failed.
:::

Why does a geometric model with $p=0.2$ fitted to times between buses, measured in minutes, often fail?

::: {.callout-tip collapse="true" title="Answer"}
The geometric law is supported on the positive integers and is memoryless. A waiting time in continuous minutes is not a trial count, and a bus that runs on a timetable is not memoryless: having already waited ten minutes changes the chance of a further long wait.
:::

## Common misconceptions
The two conventions are not a matter of notation inside one formula. Mean $1/p$ and mean $(1-p)/p$ describe different variables. A common software convention counts failures. The trial convention counts trials. Subtracting or adding one converts a sample from one convention to the other. Forgetting to convert shifts every mean by $1$ and leaves the variance unchanged, which is why a variance check will not catch the mistake.

Memorylessness does not say that a long wait makes the next trial more likely to succeed. After any number of failures the conditional success probability on the next trial is still $p$.

The geometric law is not the law of a fixed number of trials. A binomial count fixes the number of trials and counts the successes. A geometric count fixes the number of successes at one and lets the number of trials vary.

## Assumptions and limits — When the trials are not interchangeable
The success probability has to be the same on every trial, and the trials have to be independent. A machine that wears out has a success probability that falls with the attempt number. The tail is then no longer a pure geometric series, the mean need not be $1/p$, and the remaining wait after two failures is not a fresh copy of $X$.

If the first trial is already known to have failed, the conditional law of $X$ given $X>1$ is $1$ plus a fresh geometric count, not the unconditional law. Conditioning on survival is exactly the memoryless shift. Conditioning on a success having occurred is the opposite event and does not leave the original law in place.

At $p=1$ the variable is identically $1$. The variance formula $(1-p)/p^2$ is $0$, and the failure-count mean is $0$. The memoryless ratio was stated for $p<1$ because conditioning on $X>s$ for $s\ge 1$ is conditioning on an empty event when $p=1$.

## Connections
A [Bernoulli trial](bernoulli-distribution.qmd) is one attempt. The [negative binomial distribution](negative-binomial-distribution.qmd) waits for more than one success. The lack of memory is shared, in continuous time, with the [exponential distribution](exponential-distribution.qmd): remaining time does not depend on time already spent. A [Poisson process](homogeneous-poisson-process.qmd) has exponential interarrival times, not geometric trial counts, unless time has been chopped into fixed slots.

## History
One geometric law counts the failures before the first success in independent Bernoulli trials. The masses form a geometric progression with ratio equal to the failure probability, the mean is $(1-p)/p$, and the variance is $(1-p)/p^2$, from the series $1+2q+3q^2+\cdots=1/(1-q)^2$. That law is the negative binomial stopped at the first success.{{cite:dodge2008}} (pp. 226–227) The trial-count convention is that failure count plus one, with mean $1/p$.
