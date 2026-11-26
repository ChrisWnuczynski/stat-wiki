## Motivating example
A sequence of estimators can look stable in its distributions while individual realizations keep moving. To say what “approaches a limit” means, specify whether the claim concerns sample paths, the chance of a large error, the average size of an error, or only the distributions. Each answer supports different conclusions about an estimator or stochastic process.{{cite:siegrist_convergence_prob}} (Convergence, Convergence in Probability and With Probability 1){{cite:siegrist_convergence_dist}} (Convergence in Distribution, Definition)

## Intuition
Almost-sure convergence follows nearly every infinite sample path until its values settle toward the limit. Convergence in probability permits bad paths at every finite $n$, as long as their probability vanishes. $L^p$ convergence controls the average $p$th power of the error, so a rare but huge error can prevent it. Distributional convergence is weaker still: it compares the shapes of the laws and need not put $X_n$ and $X$ close on the same sample path. The four definitions below turn those distinctions into tests.{{cite:siegrist_convergence_prob}} (Convergence, two modes){{cite:siegrist_convergence_lp}} (Vector Spaces, Convergence in Mean){{cite:siegrist_convergence_dist}} (Convergence in Distribution, Definition)

## Definition — Four questions about a limit
The first three modes compare $X_n$ and $X$ on a common probability space. Almost-sure convergence asks whether $X_n(\omega)\to X(\omega)$ for all $\omega$ outside a null event. In-probability convergence asks whether $P(|X_n-X|>\varepsilon)\to0$ for every fixed $\varepsilon>0$. $L^p$ convergence asks whether $\E|X_n-X|^p\to0$ for a specified $p\ge1$. Distributional convergence asks only whether the CDFs $F_{X_n}(t)$ approach $F_X(t)$ at every *continuity point* of $F_X$; $X_n$ and $X$ need not even be defined together.{{cite:siegrist_convergence_prob}} (Convergence, definitions){{cite:siegrist_convergence_lp}} (Vector Spaces, Convergence in Mean){{cite:siegrist_convergence_dist}} (Convergence in Distribution, Definition)

## Properties — Which claims imply which
Almost-sure convergence and $L^p$ convergence each imply convergence in probability; convergence in probability implies convergence in distribution. Also $L^p$ implies $L^q$ when $p\ge q\ge1$, under finite relevant moments. Almost-sure and $L^p$ convergence are otherwise incomparable without additional assumptions. An important exception to the weakness of distributional convergence is a *constant* limit: if $X_n$ converges in distribution to the constant $c$, then $X_n\to c$ in probability.{{cite:siegrist_convergence_prob}} (Convergence, relationships){{cite:siegrist_convergence_lp}} (Vector Spaces, Convergence in Mean){{cite:siegrist_convergence_dist}} (Convergence in Distribution, relationships)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
If $\E|X_n-X|^p\to0$, Markov's inequality gives $P(|X_n-X|>\varepsilon)\le \E|X_n-X|^p/\varepsilon^p\to0$. If $X_n\to X$ almost surely, the indicators $1_{\{|X_n-X|>\varepsilon\}}$ tend to zero almost surely and are bounded by one; bounded convergence yields the same probability limit. If $X_n\to X$ in probability and $t$ is a continuity point of $F_X$, for any $\delta>0$ the event inclusions give $F_X(t-\delta)-P(|X_n-X|>\delta)\le F_{X_n}(t)\le F_X(t+\delta)+P(|X_n-X|>\delta)$. Let $n\to\infty$, then $\delta\downarrow0$, to obtain $F_{X_n}(t)\to F_X(t)$. Finally, if the distributional limit is constant $c$, the CDF values at $c-\varepsilon$ and $c+\varepsilon$ tend to $0$ and $1$; their difference shows $P(|X_n-c|>\varepsilon)\to0$.{{cite:siegrist_convergence_prob}} (Convergence, relationships){{cite:siegrist_convergence_dist}} (Convergence in Distribution, relationships)
:::
:::

## Worked example
Let $Y_n=n^2$ with probability $1/n^3$, and $Y_n=0$ otherwise. For $n=10$, the spike occurs with probability $0.001$, while $\E|Y_{10}|=0.1$ and $\E(Y_{10}^2)=10$. In general $P(|Y_n|>\varepsilon)=1/n^3$ once $n^2>\varepsilon$, so $Y_n\to0$ in probability. Its mean absolute error is $1/n\to0$, hence it also converges in $L^1$. But its mean squared error is $n\to\infty$, so it does not converge in $L^2$. A rare error can vanish in probability and in mean while still dominating a squared-error criterion.{{cite:siegrist_convergence_lp}} (Vector Spaces, Convergence in Mean and Counterexamples)

**Your turn.** Suppose $Z_n=n$ with probability $1/n^2$ and zero otherwise. At $n=10$, compute its nonzero probability, mean absolute error and mean squared error. Which of convergence in probability, $L^1$ and $L^2$ to zero hold?

::: {.callout-tip collapse="true" title="Answer"}
The probability is $0.01$, $\E|Z_{10}|=10/100=0.1$, and $\E(Z_{10}^2)=100/100=1$. In general the corresponding values are $1/n^2$, $1/n$ and $1$. Thus $Z_n\to0$ in probability and $L^1$, but not in $L^2$. The $L^2$ error remains fixed even while spikes become rare.
:::

## Common misconceptions
The same distribution is not the same as closeness on a shared sample space: if $U$ is Bernoulli$(1/2)$, $X_n=U$ and $X=1-U$, their laws agree for every $n$, yet $|X_n-X|=1$ always. Almost-sure convergence does not force convergence of means: the spike example $n1_{\{U\le1/n\}}$ vanishes on every path with $U>0$ but has mean $1$ throughout. Nor does convergence in distribution require CDF convergence at the limiting CDF's jumps: constants $1/n$ converge in distribution to $0$, although $F_{1/n}(0)=0$ and $F_0(0)=1$.{{cite:siegrist_convergence_dist}} (Convergence in Distribution, continuity-point definition){{cite:siegrist_convergence_lp}} (Vector Spaces, Counterexamples)

## Assumptions and limits — Bad events can keep returning
If $A_n$ are independent with $P(A_n)=1/n$ and $X_n=1_{A_n}$, then $P(X_n\ne0)=1/n\to0$ and $\E(X_n^2)=1/n\to0$. Thus $X_n$ converges to zero in probability and $L^2$. Yet $\sum_n P(A_n)$ diverges, and the second Borel–Cantelli lemma says the value $1$ recurs infinitely often almost surely; the sequence does not converge almost surely. Change the probabilities to $1/n^2$ and the first Borel–Cantelli lemma gives only finitely many spikes almost surely, without needing independence. This pair makes the gap between “unlikely now” and “eventually absent on a path” concrete.{{cite:siegrist_convergence_prob}} (Convergence, Coins){{cite:siegrist_convergence_lp}} (Vector Spaces, Counterexamples)

## Connections
[L2 convergence and probability](../questions/ex-sp-l2-markov.qmd) asks for the Markov bound used in the proof. [Two series of events](../questions/ex-sp-borel-cantelli.qmd) distinguishes recurring from eventually absent bad events, the key difference behind the almost-sure counterexample. The weak law of large numbers gives convergence in probability of a sample mean; a strong law gives almost-sure convergence under its stated assumptions.{{cite:siegrist_convergence_prob}} (Convergence, relationships and Coins)
