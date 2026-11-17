## Motivating example
A sequence of approximate expectations may look stable while rare, increasingly large values carry probability mass away from the pointwise limit. Passing a limit through an expectation therefore requires a condition that controls the sequence, not just knowledge of its pointwise limit. The three convergence theorems provide three different forms of control.{{cite:durrett2019}} (§1.6.2, “Integration to the Limit”)

## Statement
For nonnegative $X_n$ increasing almost surely to $X$, monotone convergence gives $E(X_n)\uparrow E(X)$, including an infinite limit. For arbitrary nonnegative $X_n$, Fatou's lemma gives
$$
E(\liminf X_n)\le\liminf E(X_n).
$$
If $X_n\to X$ almost surely and $|X_n|\le Y$ with $E(Y)<\infty$, dominated convergence gives $E(X_n)\to E(X)$ and $E|X_n-X|\to0$.{{cite:durrett2019}} (§1.5, Thms. 1.5.5, 1.5.7–1.5.8, pp. 26–27){{cite:siegrist2022_expectation_integral}} (§3.9, limit theorems)

## Intuition — Increasing mass, escaping mass, and a bound
Monotone convergence permits the expectation to be built from below. Fatou controls the smallest eventual values and allows a strict inequality when peaks disappear pointwise. Dominated convergence prevents large values from escaping beyond a single integrable bound. Its conclusion concerns absolute mean error as well as convergence of signed expectations.{{cite:durrett2019}} (§§1.5–1.6, convergence theorems)

## Proof
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
To prove monotone convergence, fix a nonnegative simple function $s\le X$ and $0<c<1$. On the increasing events $A_n=\{X_n\ge cs\}$, the inequality $X_n\ge cs1_{A_n}$ holds. Wherever $s>0$, eventually $X_n\ge cs$, so continuity of probability on increasing events gives $E(s1_{A_n})\to E(s)$. Hence $\lim E(X_n)\ge cE(s)$. Let $c\uparrow1$ and take the supremum over simple $s\le X$ to obtain $\lim E(X_n)\ge E(X)$. The opposite inequality follows from $X_n\le X$.

Fatou follows by applying monotone convergence to $Z_m=\inf_{n\ge m}X_n$, since $Z_m\uparrow\liminf X_n$ and $E(Z_m)\le\inf_{n\ge m}E(X_n)$. For dominated convergence, $|X|\le Y$ almost surely. Fatou applied to the nonnegative variables $2Y-|X_n-X|$ gives $2E(Y)\le2E(Y)-\limsup E|X_n-X|$. Hence the absolute mean error tends to zero; the difference of expectations is bounded by that error.{{cite:durrett2019}} (§1.5, proofs of Fatou's lemma and dominated convergence)
:::
:::

This proof uses monotone convergence as its starting integral theorem. That theorem follows from defining the nonnegative integral by increasing simple approximations; no finite upper bound on $E(X)$ is necessary.{{cite:siegrist2022_expectation_integral}} (§3.9, definition of the nonnegative integral and monotone convergence)

## Worked example
Let $U$ be uniform on $(0,1)$. The sequence $A_n=\min\{n,1/\sqrt U\}$ increases to $1/\sqrt U$. For $n\ge1$,
$$
E(A_n)=n\frac1{n^2}+\int_{1/n^2}^1u^{-1/2}\,du=2-\frac1n.
$$
Thus the expectations at $n=1,2,10$ are $1,1.5,1.9$, increasing to $2$. Monotone convergence justifies the limit directly.{{cite:durrett2019}} (§1.5, Thm. 1.5.7)

The contrasting spike $B_n=n1_{\{U\le1/n\}}$ tends almost surely to zero but has $E(B_n)=1$. The heights alone do not prove failure of domination: what matters is that the pointwise supremum has infinite expectation. For $U\le1/2$, that supremum is at least $1/(2U)$, whose integral diverges.

**Your turn.** Replace the spike height $n$ by $\sqrt n$. What are its expectation and second moment?

::: {.callout-tip collapse="true" title="Answer"}
For $C_n=\sqrt n1_{\{U\le1/n\}}$, $E(C_n)=1/\sqrt n\to0$, while $E(C_n^2)=1$. It converges to zero in absolute mean but not in mean square.
:::
