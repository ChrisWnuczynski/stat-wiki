## Lead context
The strong law says that the running average along one endless sequence of repeated measurements settles on the theoretical mean, except on a set of sequences whose total probability is zero.

## Motivating example
A fair coin has mean $1/2$. After $100$ tosses, Chebyshev's inequality only says that the proportion of heads lands more than $0.1$ away from $1/2$ with probability at most $0.25$. That bound is about one sequence in four at the single time $n=100$. It does not say whether one particular sequence eventually stays close to $1/2$ forever. The strong law is the pathwise statement: for almost every sequence the proportion does settle at $1/2$.{{cite:durrett2019}} (Thm. 2.4.1, p. 76){{cite:dodge2008}} (pp. 298–299)

## Statement
Durrett's form needs only pairwise independence, identical distribution, and $\E|X_i|<\infty$. The sample average then converges almost surely to the mean. Full independence, as in the displayed theorem, is more than enough for that result. A finite variance is not required.{{cite:durrett2019}} (Thm. 2.4.1, p. 76)

If the positive part has infinite mean and the negative part has finite mean, the average tends to $+\infty$ almost surely. A symmetric Cauchy law has no mean at all, and the average of independent copies stays Cauchy, so there is no constant for the average to approach.{{cite:durrett2019}} (Thm. 2.4.5, p. 78)

## Intuition
Almost-sure convergence asks for one set of outcomes, of probability $1$, on which the numerical sequence of averages converges. Convergence in probability asks only that, at each large $n$, the chance of a large error is small. The bad set is allowed to move with $n$. A bound of order $1/n$ tends to zero and proves the weak law, and $\sum 1/n$ diverges, so those bounds do not feed the first Borel–Cantelli lemma. A bound of order $1/n^2$ is summable, and then only finitely many large errors occur, on a single set of probability $1$.{{cite:durrett2019}} (§2.4, pp. 76–78){{cite:dodge2008}} (pp. 298–299)

## Key results
Under a fourth-moment assumption the summable bound is elementary. If the centred variables have $\E Z_i=0$, $\sigma^2=\E Z_i^2$, and $\mu_4=\E Z_i^4<\infty$, independence gives
$$
\E\Bigl(\sum_{i=1}^n Z_i\Bigr)^4=n\mu_4+3n(n-1)\sigma^4.
$$
Dividing by $n^4$ leaves a fourth-moment of the average of order $1/n^2$. Markov's inequality at that power is summable in $n$.

The finite-mean theorem removes the fourth-moment hypothesis by truncation. Durrett follows Etemadi: replace $X_k$ by $X_k 1_{|X_k|\le k}$, prove the truncated averages converge along the subsequence $k(n)=\lfloor\alpha^n\rfloor$, and fill the gaps by monotonicity after splitting into positive and negative parts. Pairwise independence is enough for that argument.{{cite:durrett2019}} (Thm. 2.4.1, pp. 76–78)

## Proof
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $Z_i$ be i.i.d. with mean $0$, variance $\sigma^2$, and fourth moment $\mu_4<\infty$. Expand $\E(\sum_i Z_i)^4$ as a sum over four indices. Any term in which some index appears once has a factor $\E Z_j=0$ after independence is used, so it vanishes. The surviving patterns are one index repeated four times, and two distinct indices each repeated twice.

There are $n$ terms of the first kind, each equal to $\mu_4$. For the second kind there are $\binom{n}{2}$ choices of the indices and $4!/(2!2!)=6$ ways to place them in the product, giving $3n(n-1)$ terms each equal to $\sigma^4$. Hence
$$
\E\Bigl(\sum_{i=1}^n Z_i\Bigr)^4=n\mu_4+3n(n-1)\sigma^4.
$$
The average $\overline Z_n$ therefore satisfies $\E|\overline Z_n|^4=O(n^{-2})$. For $\varepsilon>0$,
$$
\mathbb{P}(|\overline Z_n|>\varepsilon)\le\frac{\E|\overline Z_n|^4}{\varepsilon^4},
$$
and the right-hand side sums over $n$. The first Borel–Cantelli lemma gives, for each fixed $\varepsilon>0$, only finitely many exceedances, with probability $1$. Intersecting the countably many probability-$1$ sets for $\varepsilon=1/m$ yields $\overline Z_n\to 0$ almost surely.

The finite-mean case, without a fourth moment, is the truncation argument in the same section. The truncation $Y_k=X_k 1_{|X_k|\le k}$ changes only finitely many terms almost surely, because $\sum\mathbb{P}(|X_k|>k)\le\E|X_1|<\infty$. The variances of the truncated variables satisfy $\sum\mathrm{Var}(Y_k)/k^2<\infty$, and a geometric subsequence plus monotonicity of the positive and negative parts upgrades convergence along that subsequence to convergence along every $n$.{{cite:durrett2019}} (Thm. 2.4.1, pp. 76–78)
:::
:::

## Generalizations
The same almost-sure average applies to indicators. If $F_n$ is the empirical distribution function of an i.i.d. sample, the strong law at each fixed $x$ gives $F_n(x)\to F(x)$ almost surely, and the Glivenko–Cantelli theorem upgrades the pointwise limit to a uniform one. A renewal counting process obeys $N_t/t\to 1/\mu$ almost surely when the interarrival mean is $\mu\in(0,\infty]$.{{cite:durrett2019}} (Thm. 2.4.7 and Thm. 2.4.9, pp. 78–80)

If only the positive part of the mean is infinite, the average tends to infinity rather than to a finite limit. That is still a strong law, with an infinite limit.{{cite:durrett2019}} (Thm. 2.4.5, p. 78)

## Related concepts
The [weak law](law-of-large-numbers.qmd) is convergence in probability of the same average. [Chebyshev's inequality](chebyshev-s-inequality.qmd) proves it when the variance is finite. The [Borel–Cantelli lemmas](borel-cantelli-lemmas.qmd) turn a summable series of tail probabilities into an almost-sure statement. The [central limit theorem](central-limit-theorem.qmd) describes the size of the error at a large but finite $n$, which the strong law does not.{{cite:durrett2019}} (§2.4, p. 76){{cite:dodge2008}} (pp. 298–299)

## Statistical use — Reading a long-run frequency
A relative frequency is a sample average of indicators. The strong law is the reason a long sequence of identical trials has a proportion that settles on the success probability, on almost every sequence. It does not give a numerical error at a finite $n$. For that, a variance bound or a normal approximation is a different theorem. Estimating a mean by an average is justified, as a pathwise limit, when the absolute mean is finite. When the mean fails to exist, the average need not settle, and reporting it as an estimate of a centre has no strong-law warrant.{{cite:durrett2019}} (Thm. 2.4.1 and Thm. 2.4.5)

## Common misconceptions
Almost-sure convergence is not a statement about the expectation of the average. A rare spike can keep $\E|\overline Y_n-\mu|$ from tending to zero even while the average converges on almost every path. The converse confusion is to treat a Chebyshev bound of order $1/n$ as a proof of the strong law. The bound tends to zero, which is the weak law, and the series of bounds diverges.

A finite variance is not part of the hypothesis. It is a convenient extra assumption for the elementary proof above. The Cauchy average shows the other edge: without a finite absolute mean, identical distribution and independence do not force the average to a constant.{{cite:durrett2019}} (Thm. 2.4.5, p. 78)

## History
Bernoulli's 1713 argument treated a relative frequency in repeated trials. The Bienaymé–Chebyshev inequality came next, and the strong law is the probability-one limit of the sample average. A general form of the law of large numbers is associated with Khintchin. A vanishing probability of a large error is not the same as a pathwise limit.{{cite:dodge2008}} (pp. 298–299) The finite-mean proof cited here is Etemadi's truncation argument, as given by Durrett for pairwise independent variables.{{cite:durrett2019}} (Thm. 2.4.1, p. 76)

## Worked example
Let $Y_i$ be $1$ or $0$ with equal probability $1/2$, and let $\overline Y_n$ be the proportion of ones. Then $\mu=1/2$, $\sigma^2=1/4$, and the centred fourth moment is $\mu_4=(1/2)^4=1/16$. At $n=100$ and $\varepsilon=0.1$,
$$
\mathbb{P}(|\overline Y_{100}-1/2|>0.1)\le\frac{1/4}{100\cdot 0.01}=0.25
$$
by Chebyshev. The fourth-moment identity gives
$$
\E\Bigl(\sum_{i=1}^{100} Z_i\Bigr)^4=\frac{100+3\cdot 100\cdot 99}{16}=1862.5,
$$
so $\E|\overline Y_{100}-1/2|^4=1862.5/100^4=0.000018625$. Markov's inequality at the fourth power divides by $(0.1)^4=0.0001$ and yields the tighter bound $0.18625$. Both numbers are upper bounds, not the true probability. The strong law says that, whatever these bounds are at $n=100$, the proportion eventually stays inside every fixed neighbourhood of $1/2$, for almost every sequence.{{cite:durrett2019}} (Thm. 1.6.4, p. 30; Thm. 2.4.1)

**Your turn.** With the same coin and $\varepsilon=0.2$, compute the Chebyshev bound at $n=50$, and the fourth-moment bound $\E|\overline Y_{50}-1/2|^4/(0.2)^4$.

::: {.callout-tip collapse="true" title="Answer"}
The variance of the average is $(1/4)/50=0.005$, and $0.2^2=0.04$, so the Chebyshev bound is $0.005/0.04=0.125$. The fourth-moment sum is $(50+3\cdot 50\cdot 49)/16=462.5$, and $462.5/50^4=0.000074$. Dividing by $0.2^4=0.0016$ gives $0.04625$.
:::

**Check yourself.** Three further checks use the same coin.

A bound of $0.25$ at $n=100$ does not mean the proportion is outside $[0.4,0.6]$ a quarter of the time. What does it mean?

::: {.callout-tip collapse="true" title="Answer"}
It means the probability is at most $0.25$. The true probability can be much smaller. The bound uses only the variance.
:::

Why does the series of Chebyshev bounds $\sum_n 0.25\cdot(100/n)$, more cleanly $\sum_n \sigma^2/(n\varepsilon^2)$, fail to prove the strong law?

::: {.callout-tip collapse="true" title="Answer"}
The general term is a constant over $n$, and $\sum 1/n$ diverges. Borel–Cantelli needs a summable series before it can conclude that only finitely many exceedances occur.
:::

If $\E|Y_1|=\infty$, which conclusion of the worked example can fail?

::: {.callout-tip collapse="true" title="Answer"}
The almost-sure settlement on a finite mean can fail. A standard Cauchy sample has no mean, and the average remains standard Cauchy at every $n$, so it does not converge in probability to a constant.
:::
