## Motivating example

An estimator can tend to zero on almost every simulated path while keeping mean one. A shrinking probability of a growing value can carry a fixed amount of expectation. Uniform integrability checks the contribution of the far tail across the whole family, preventing that lost expectation.{{cite:durrett2019}} (§4.6, pp. 244–245)

## Definition — A uniform bound on tail contributions

A family of integrable random variables $\{X_i:i\in I\}$ is uniformly integrable if
$$
\lim_{K\to\infty}\sup_{i\in I}E\bigl[|X_i|1_{\{|X_i|>K\}}\bigr]=0.
$$
The supremum precedes the limit. Each individual integrable variable has a vanishing tail expectation; uniform integrability asks for one cutoff that works for every member. In contrast, $\sup_iE|X_i|<\infty$ bounds total expectations without requiring tails to shrink uniformly.{{cite:durrett2019}} (§4.6, p. 244)

## Properties — From convergence in probability to mean convergence

If $X_n\to X$ in probability and $\{X_n\}$ is uniformly integrable, then $E|X_n-X|\to0$ and $X$ is integrable. Conversely, convergence in $L^1$ implies uniform integrability of the sequence. The probability limit and tail control together determine convergence in mean.{{cite:durrett2019}} (§4.6, Thm. 4.6.3, p. 245) Here the $L^1$ distance is exactly the expected absolute difference, which also bounds the difference of means by $|EX_n-EX|\le E|X_n-X|$.{{cite:siegrist_convergence_lp}} (Vector Spaces of Random Variables, Convergence)

A useful sufficient condition is $\sup_iE|X_i|^{1+\delta}\le M$ for some $\delta>0$. On $|X_i|>K$, $|X_i|\le |X_i|^{1+\delta}/K^\delta$, so the tail expectation is at most $M/K^\delta$. An integrable common dominant also suffices: if $|X_i|\le Y$, every tail expectation is bounded by $E[Y1_{\{Y>K\}}]$.{{cite:durrett2019}} (§4.6, Thm. 4.6.2, p. 245)

::: {.callout-note collapse="true" title="Proof of the convergence implication"}
::: {.proof}
Clip variables to $[-K,K]$ using $c_K(x)=\max(-K,\min(x,K))$. Boundedness and convergence in probability imply $E|c_K(X_n)-c_K(X)|\to0$: split that expectation at any positive error threshold. A subsequence converges almost surely, so Fatou's lemma gives $E(|X|-K)_+\le\liminf_nE(|X_n|-K)_+$. Uniform integrability makes these truncation errors small uniformly for large $K$. Finally apply the triangle inequality to $X_n-c_K(X_n)$, $c_K(X_n)-c_K(X)$, and $c_K(X)-X$.{{cite:durrett2019}} (§4.6, proof of Thm. 4.6.3, pp. 245–246)
:::
:::

## Worked example

Let $U$ be uniform on $(0,1)$ and put $X_n=n1_{\{U\le1/n\}}$. Its expectation is $n(1/n)=1$. For each fixed $U>0$, sufficiently large $n$ makes $X_n=0$, so $X_n\to0$ almost surely. Nevertheless, for every cutoff $K$, choosing an integer $n>K$ gives tail expectation one. The supremum never shrinks.

Change the height to $Y_n=\sqrt n1_{\{U\le1/n\}}$. Now $EY_n=1/\sqrt n$, and the tail expectation is nonzero only when $n>K^2$. Its supremum is at most $1/K$, which tends to zero. For example, at $n=100$ the two means are one and $0.1$, respectively. Both sequences vanish almost surely, but only the second has vanishing $L^1$ norm. The example separates bounded means from uniform tail control.{{cite:durrett2019}} (§4.6, pp. 244–245)

**Your turn.** Is the family $Z_n=U^n$ uniformly integrable?

::: {.callout-tip collapse="true" title="Answer"}
Yes: $0\le Z_n\le1$, so every tail expectation is zero once $K\ge1$. Also $EZ_n=1/(n+1)\to0$, agreeing with its almost-sure limit zero.
:::

## Check yourself

### [Minimum and average of uniform draws](../questions/ex-prob-min-and-mean.qmd) {#self-check-ex-prob-min-and-mean}

Why does the family of these sample averages have uniform tail control?

::: {.callout-tip collapse="true" title="Answer"}
Every average lies in $[0,1]$, so its tail expectation is zero for cutoffs at least one. Its expectation is $1/2$, and its variance is $1/(12n)$.
:::

### [Square of a uniform variable](../questions/ex-prob-square-uniform.qmd) {#self-check-ex-prob-square-uniform}

If $Y=U^2$, is it integrable, and what bounds its tail expectation?

::: {.callout-tip collapse="true" title="Answer"}
$0\le Y\le1$ and $EY=\int_0^1u^2du=1/3$. Its tail expectation is zero for $K\ge1$; the same bound works for any family bounded by one.
:::
