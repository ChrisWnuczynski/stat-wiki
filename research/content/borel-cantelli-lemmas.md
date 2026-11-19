## Lead context
The lemmas turn a convergent or divergent series of probabilities into a statement about whether events keep happening forever.

## Motivating example
Independent events with $\mathrm{P}(A_n)=2^{-n}$ have probabilities that sum to $1$. The probability of infinitely many occurrences is $0$. The tail from $n=5$ onwards sums to $1/16$.

## Intuition — A summable tail cannot return forever
The event that $A_n$ occurs for infinitely many $n$ sits inside every tail union $\bigcup_{n\ge m}A_n$. If the probabilities are summable, those tail sums shrink to $0$, and the union bound drags the tail union with them. Independence is not required for that half. The opposite half needs independence: a divergent series of probabilities forces infinitely many occurrences only when a long run of failures factors into a product.{{cite:durrett2019}} (Thm. 2.3.1, p. 68){{cite:durrett2019}} (Thm. 2.3.7, p. 70)

## Worked example
Let the events be independent with $\mathrm{P}(A_n)=2^{-n}$. The series sums to $1$, so the first lemma applies and $\mathrm{P}(A_n\text{ infinitely often})=0$. The tail from $n=5$ onwards sums to $1/16$, and the union bound says the probability of any occurrence from there on is at most $1/16$. The partial sum through $n=4$ is $15/16$.

**Your turn.** Keep the events independent and replace the probabilities by $1/n^2$. Which lemma applies, and what is the probability of infinitely many occurrences?

::: {.callout-tip collapse="true" title="Answer"}
$\sum n^{-2}$ converges, so the first lemma applies whether or not the events are independent, and the probability is $0$. The second lemma is the wrong tool: its hypothesis is a divergent series.
:::

Independent events have $\mathrm{P}(A_n)=1/n$. What is the probability of infinitely many occurrences?

::: {.callout-tip collapse="true" title="Answer"}
The harmonic series diverges and the events are independent, so the second lemma gives probability $1$.
:::

The same event of probability $1/2$ is copied at every $n$, so the events are not independent. The probabilities sum to infinity. What is the probability of infinitely many occurrences?

::: {.callout-tip collapse="true" title="Answer"}
Infinitely many copies occur precisely when that one event occurs, so the probability is $1/2$, not $1$. A divergent series without independence need not force probability $1$.
:::

## Related concepts — Where the lemmas are used
The event of infinitely many occurrences is $\limsup A_n$. The first lemma is the step from a summable series of deviation probabilities to a [strong law](strong-law.qmd). Pairwise independence is not enough for the product in the second lemma; the argument uses the full product over the tail.{{cite:durrett2019}} (Thm. 2.3.7, p. 70)

## Proof
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $N=\sum_n 1_{A_n}$. If $\sum_n\mathrm{P}(A_n)<\infty$, then $\mathrm{E}(N)<\infty$, so $N<\infty$ with probability $1$. That is $\mathrm{P}(A_n\text{ infinitely often})=0$.{{cite:durrett2019}} (Thm. 2.3.1, p. 68)

For the second lemma, independence and $1-x\le e^{-x}$ give, for $N>M$,

$$
\mathrm{P}\Bigl(\bigcap_{n=M}^{N} A_n^c\Bigr)=\prod_{n=M}^{N}\bigl(1-\mathrm{P}(A_n)\bigr)\le\exp\Bigl(-\sum_{n=M}^{N}\mathrm{P}(A_n)\Bigr).
$$


A divergent series sends the exponent to $-\infty$, so every tail union has probability $1$. The tail unions decrease to the infinitely-often event, and the probability passes to the limit.{{cite:durrett2019}} (Thm. 2.3.7, p. 70)
:::
:::

## History
The two lemmas separate a summable series of probabilities, which forces only finitely many occurrences, from an independent series with infinite sum, which forces infinitely many.{{cite:durrett2019}} (Thm. 2.3.1, p. 68; Thm. 2.3.7, p. 70)
