## Motivating example
A probability forecast can assign probabilities to each possible outcome and be scored by the logarithm of the probability of the outcome that occurs. If the true probabilities are $p$, the best expected score among all probability vectors is achieved by reporting $p$ itself. The gap from any other report is a relative entropy.{{cite:goodfellow_bengio_courville2016}} (§3.13, eqs. 3.50–3.51, pp. 72–73)

## Definition — A nonnegative log-score gap
For probability vectors $p$ and $q$ on a finite set, let
$$D(p\Vert q)=\sum_{i:p_i>0}p_i\log\frac{p_i}{q_i}.$$
If $q_i=0<p_i$ for some coordinate, set the divergence to infinity. A zero $p_i$ contributes zero. Gibbs' inequality says $D(p\Vert q)\ge0$, with equality exactly when $p=q$. Natural logarithms measure the gap in nats.{{cite:goodfellow_bengio_courville2016}} (§3.13, eq. 3.50, p. 72)

The entropy $H(p)=-\sum_i p_i\log p_i$ measures the score of $p$ against itself, with its sign reversed. It depends on the logarithm's base.{{cite:shannon1948}} (§6, Thm. 2) Cross-entropy is $H(p,q)=-\sum_i p_i\log q_i$, and $H(p,q)=H(p)+D(p\Vert q)$.{{cite:goodfellow_bengio_courville2016}} (§3.13, eq. 3.51, p. 73)

## Properties — A proof including zero coordinates
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Suppose $q_i>0$ wherever $p_i>0$, since otherwise the claim follows from infinite divergence. For $u>0$, the function $u-1-\log u$ is minimised at one, where it vanishes. Apply $-\log u\ge1-u$ with $u=q_i/p_i$, multiply by $p_i$ and sum over its positive coordinates:
$$D(p\Vert q)\ge\sum_{p_i>0}(p_i-q_i)=1-\sum_{p_i>0}q_i\ge0.$$
Equality needs both $q_i/p_i=1$ for every positive $p_i$ and no $q$ mass outside that support. These conditions give $p=q$. The support restriction is essential to the equality argument.{{cite:goodfellow_bengio_courville2016}} (§3.13, p. 72)
:::
:::

## Worked example — Two binary forecasts
For $p=(0.9,0.1)$ and $q=(0.5,0.5)$, the expected self-score is $-0.325083$ and the expected score of $q$ is $-0.693147$. Their difference is $0.368064$ nats. Reversing the arguments gives $D(q\Vert p)=0.510826$, demonstrating that a nonnegative divergence need not be a symmetric distance.

**Your turn.** If $p=(1,0)$ and $q=(1/2,1/2)$, what is the divergence?

::: {.callout-tip collapse="true" title="Answer"}
Only the first coordinate contributes, giving $D(p\Vert q)=\log2$. The zero probability in $p$ adds no term.
:::

## Connections — Why an EM entropy term has the right sign
For each observation in a mixture, the current membership probabilities form a probability vector. Applying the inequality to that vector and a candidate membership vector bounds the cross-entropy part of the likelihood decomposition. The nonnegative KL gap is what supplements the rise in the expected complete-data criterion. This algebra concerns likelihood improvement, not convergence to a particular global optimum.{{cite:goodfellow_bengio_courville2016}} (§3.13, pp. 72–73)

