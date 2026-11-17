## Lead context
The remaining wait for an exponential lifetime has the same law as the wait from the start, so age does not enter the forecast.{{cite:grinstead_snell1997}} (p. 68, memoryless property)

## Motivating example
A workshop replaces hard drives whose lifetimes are modelled as exponential with mean $30$ months. A drive that has already run for $15$ months invites the guess that about $15$ months remain. Under the exponential model the remaining lifetime still has mean $30$ months, the same mean as a new drive. The time already spent does not shorten the forecast.{{cite:grinstead_snell1997}} (p. 68, hard-drive residual life)

## Statement
For a positive waiting time $X$, the memoryless property is the identity $\Pr(X>s+t\mid X>s)=\Pr(X>t)$ whenever $s,t>0$ and $\Pr(X>s)>0$. The exponential laws are the continuous distributions with this property, and the geometric laws are the discrete distributions on the positive integers with the matching identity at integer times.{{cite:grinstead_snell1997}} (pp. 68, 186, 206–207)

Write $S(u)=\Pr(X>u)$. The identity is $S(s+t)=S(s)S(t)$. An exponential rate $\lambda>0$ has density $\lambda e^{-\lambda x}$ on $x>0$ and survival $S(u)=e^{-\lambda u}$, so both sides equal $e^{-\lambda t}$.{{cite:dodge2008}} (p. 194, exponential density and distribution function){{cite:grinstead_snell1997}} (pp. 206–207, exponential survival)

## Intuition
The exponential density falls at a constant proportional rate. The hazard, density divided by survival, equals $\lambda$ at every age, so the chance of failing in a short interval does not rise as the device gets older. Conditioning on survival to age $s$ cuts the left tail away and renormalises what remains; for this density the renormalised tail is a copy of the original law, shifted to start at $s$.{{cite:grinstead_snell1997}} (pp. 206–207)

A geometric clock on the positive integers has the same reading one step at a time. If each time unit brings an independent success with probability $p\in(0,1)$, and $X$ is the trial number of the first success, then $\Pr(X>k)=(1-p)^k$. Surviving $r$ failures leaves a fresh sequence of trials. The probability of needing at least $s$ further trials is $(1-p)^s$, with no dependence on $r$.{{cite:grinstead_snell1997}} (p. 186, geometric survival)

## Key results
The conditional survival calculation is an equality of two exponential functions, not an approximation. For $X\sim\operatorname{Exp}(\lambda)$,
\[
\Pr(X>s+t\mid X>s)=\frac{e^{-\lambda(s+t)}}{e^{-\lambda s}}=e^{-\lambda t}=\Pr(X>t).
\]
The conditional law of $X-s$ given $X>s$ is again $\operatorname{Exp}(\lambda)$. Its mean is $1/\lambda$, the unconditional mean, rather than $1/\lambda-s$.{{cite:dodge2008}} (p. 194, mean $1/\theta$){{cite:grinstead_snell1997}} (pp. 206–207)

On the positive integers the same cancellation uses a geometric ratio. With success probability $p$ and $q=1-p$,
\[
\Pr(X>r+s\mid X>r)=\frac{q^{r+s}}{q^r}=q^s=\Pr(X>s)
\]
for integers $r,s\ge 0$. The mean number of trials until the first success is $1/p$. Counting failures before the first success instead, the masses are $p q^k$ for $k=0,1,2,\ldots$ and the mean is $q/p$, one less than $1/p$. Both indexings are memoryless on their own lattice; they are not the same random variable.{{cite:grinstead_snell1997}} (p. 186){{cite:dodge2008}} (p. 226, geometric masses and mean $q/p$)

A Weibull lifetime with shape different from $1$ fails the identity. Shape $2$ and scale $1$ has survival $\exp(-t^2)$. Then $\Pr(T>1)=e^{-1}\approx 0.3679$, while
\[
\Pr(T>2\mid T>1)=\frac{e^{-4}}{e^{-1}}=e^{-3}\approx 0.0498,
\]
which is not $e^{-1}$. Ageing has made the next unit of time much less likely to be survived.{{cite:grinstead_snell1997}} (pp. 206–207, the exponential case of the identity)

## Proof
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $S(u)=\Pr(X>u)$. The exponential density $\lambda e^{-\lambda x}$ on $(0,\infty)$ integrates to the survival $S(u)=e^{-\lambda u}$ for $u>0$. Dividing $S(s+t)$ by $S(s)$ cancels $e^{-\lambda s}$ and leaves $e^{-\lambda t}$. That is the continuous identity.{{cite:grinstead_snell1997}} (pp. 206–207){{cite:dodge2008}} (p. 194)

For the geometric law of the trial of the first success, $S(k)=q^k$ for each integer $k\ge 0$, because the first $k$ trials are failures. The ratio $S(r+s)/S(r)$ is $q^s$.{{cite:grinstead_snell1997}} (p. 186)

Conversely, on the positive reals, assume $S$ is continuous, $S(0)=1$, $S(t)>0$, and $S(s+t)=S(s)S(t)$ for all $s,t\ge 0$. Then $S(nt)=S(t)^n$ and $S(t)=S(t/n)^n$, so $S(m/n)=S(1)^{m/n}$. Continuity extends the identity from the rationals to every $t\ge 0$, giving $S(t)=S(1)^t$. A proper waiting time has $S(t)\to 0$, so $0<S(1)<1$. Set $\lambda=-\log S(1)>0$. Then $S(t)=e^{-\lambda t}$, which is the exponential survival. The exponential laws are the only continuous memoryless waiting-time laws.{{cite:grinstead_snell1997}} (p. 68, only the exponential density)

On the positive integers the same multiplicative rule with $S(0)=1$ gives $S(n)=S(1)^n$. Set $q=S(1)$. Properness forces $0\le q<1$, and the point masses are $S(n-1)-S(n)=(1-q)q^{n-1}$ for $n\ge 1$. That is the geometric law with success probability $1-q$.{{cite:grinstead_snell1997}} (p. 186){{cite:dodge2008}} (p. 226)
:::
:::

## Generalizations
The identity is about one waiting time. A sum of $k$ independent exponential waits with the same rate is a Gamma law of integer shape $k$, and that sum is not memoryless once $k>1$: having already waited a long time makes the remaining stages fewer. The minimum of independent exponential clocks is exponential with rate equal to the sum of the rates, and that minimum is memoryless. The identity does not pass to a maximum of two independent exponential clocks.{{cite:grinstead_snell1997}} (pp. 206–207, exponential survival)

At non-integer times a geometric random variable is not being asked the continuous question. The survival identity used above is stated at integer ages. Interpolating it to a real age, as if the geometric clock were an exponential clock, uses a model that was not assumed.

## Related concepts
The constant-hazard reading is the exponential special case of a lifetime model. A hazard that rises or falls with age is a different family, and the Weibull calculation above is one concrete failure. Discrete memorylessness is the geometric law, with the failures-before-success indexing shifted by one trial relative to the trials-until-success indexing.{{cite:dodge2008}} (pp. 194, 226){{cite:grinstead_snell1997}} (pp. 186, 206–207)

## Statistical use — When a residual wait equals a new wait
Use the property when the scientific story really is a constant hazard: radioactive emission, or a component that does not wear in the time window under study. The residual mean is then the full mean $1/\lambda$, and a forecast interval for the remaining wait is the same interval one would quote for a new item. If wear, maintenance, or a changing arrival rate is part of the story, the exponential residual formula is the wrong forecast even though the algebra is correct for the exponential law.{{cite:grinstead_snell1997}} (pp. 68, 164, bus paradox)

## Worked example
Let $X$ be the lifetime in hours of a lamp with $X\sim\operatorname{Exp}(\lambda)$ and $\lambda=1/1000$, so the mean life is $1000$ hours. The lamp has already burned for $1000$ hours. The probability that it burns at least $500$ hours more is
\[
\Pr(X>1500\mid X>1000)=e^{-500/1000}=e^{-1/2}\approx 0.6065.
\]
A new lamp has the same probability of lasting $500$ hours, because $e^{-1/2}$ does not use the age $1000$. The conditional mean remaining life is $1000$ hours, not $0$.{{cite:grinstead_snell1997}} (pp. 206–207){{cite:dodge2008}} (p. 194, mean $1/\theta$)

For a discrete clock, let $X$ be the trial of the first success with $p=1/4$, so $q=3/4$ and the mean number of trials is $4$. After two trials have failed,
\[
\Pr(X>6\mid X>2)=(3/4)^4=81/256=0.31640625,
\]
which equals $\Pr(X>4)$. Counting failures before the first success instead, the mean is $q/p=3$, and the probability of at least four further failures is the same $81/256$. The two means differ by $1$ because one count includes the successful trial and the other does not.{{cite:dodge2008}} (p. 226){{cite:grinstead_snell1997}} (p. 186)

**Your turn.** An exponential wait has rate $1/8$ per hour. It has already lasted $5$ hours. Find the probability that it lasts at least $3$ hours more, and state the conditional mean of the remaining wait.

::: {.callout-tip collapse="true" title="Answer"}
The probability is $e^{-3/8}\approx 0.6873$. The conditional remaining mean is $8$ hours, the same as the unconditional mean. The $5$ hours already elapsed cancel in the survival ratio and do not reduce the mean.
:::

**Check yourself.**

1. Buses arrive as a Poisson process with mean gap $30$ minutes. You arrive at a stop at a random moment. What is the mean wait under the exponential model, and what mean wait would a perfectly regular $30$-minute timetable have given?

::: {.callout-tip collapse="true" title="Answer"}
The exponential model is memoryless, so the mean residual wait is $30$ minutes. A deterministic gap of $30$ minutes, with an arrival time uniform inside a gap, has mean wait $15$ minutes. The two stories use different interarrival laws, so the two means are not in conflict.
:::

2. For the geometric trial count with success probability $1/4$, you have already seen $2$ failures. Is $\Pr(X>6\mid X>2)$ equal to $\Pr(X>6)$?

::: {.callout-tip collapse="true" title="Answer"}
No. Memorylessness equates the conditional probability with $\Pr(X>4)=(3/4)^4=81/256=0.31640625$. The unconditional $\Pr(X>6)=(3/4)^6=729/4096=0.177978515625$ is smaller, because it does not condition on having reached trial $2$.
:::

3. A lifetime has survival $\exp(-t^2)$. Does $\Pr(T>2\mid T>1)$ equal $\Pr(T>1)$?

::: {.callout-tip collapse="true" title="Answer"}
No. The left side is $e^{-3}\approx 0.0498$ and the right side is $e^{-1}\approx 0.3679$. Shape $2$ is not the exponential case, so the residual probability is smaller than the probability from a fresh start.
:::

## Common misconceptions — Age is not subtracted from the mean
The remaining mean is not the original mean minus the age already observed. For an exponential mean of $30$ months, survival past $15$ months leaves a remaining mean of $30$, not $15$. A deterministic schedule does subtract in that way, and that is why the bus calculation feels paradoxical: the timetable intuition is the uniform-arrival calculation, and the exponential model refuses it.{{cite:grinstead_snell1997}} (pp. 68, 164)

A second confusion is the indexing of the geometric law. Mean $1/p$ counts the successful trial. Mean $q/p$ counts only the failures. Quoting one mean for the other variable shifts every forecast by one trial.{{cite:dodge2008}} (p. 226){{cite:grinstead_snell1997}} (p. 186)

A third confusion treats every right-skewed positive law as memoryless. The Weibull comparison with shape $2$ has a residual probability $e^{-3}\approx 0.0498$ against a fresh probability $e^{-1}\approx 0.3679$. Skewness alone did not produce the cancellation.{{cite:grinstead_snell1997}} (pp. 206–207)

## History
The exponential density, written with rate $\theta$ as $\theta e^{-\theta x}$ for $x\ge 0$, has distribution function $1-e^{-\theta x}$, mean $1/\theta$ and variance $1/\theta^2$. That entry records the law and its gamma and geometric analogies, and it does not name the memoryless identity.{{cite:dodge2008}} (p. 194)

The identity itself is the exponential calculation $e^{-\lambda(r+s)}/e^{-\lambda r}=e^{-\lambda s}$, together with the statement that the exponential density is the only continuous density with the property. The geometric survival $q^k$ gives the same cancellation on the positive integers, which is why a service time with that law does not become shorter in probability merely because service has already lasted $r$ units.{{cite:grinstead_snell1997}} (pp. 68, 186, 206–207)
