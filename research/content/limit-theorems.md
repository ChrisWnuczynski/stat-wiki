## Lead context
Limit theorems describe what a sample average, or a centred and scaled sum, does as the number of observations grows.

## Motivating example
A fair coin tossed $100$ times has mean $50$ and standard deviation $5$. The chance of $60$ or more heads is $0.0284$. A normal approximation that ignores the lattice, $1-\Phi(2)$, gives $0.0228$. Shifting the threshold to $59.5$ gives $1-\Phi(1.9)=0.0287$, within $0.0003$ of the exact value. The limit theorem does not compute the binomial sum. It explains why a normal number, read at the right place, is already close.{{cite:durrett2019}} (Thm. 3.4.1, p. 144)

## Intuition
Three different limits are easy to mix. The weak law says that the probability of an error larger than a fixed $\varepsilon$ tends to zero. The strong law says that, on almost every sequence, the error itself eventually stays small. The central limit theorem says that the error, multiplied by $\sqrt{n}$, settles on a normal shape. The first is a probability at each $n$. The second is a path. The third is a distributional approximation, and it needs a finite positive variance that the strong law does not.{{cite:durrett2019}} (Thm. 2.4.1, p. 76; Thm. 3.4.1, p. 144){{cite:dodge2008}} (pp. 66 and 298–299)

## Definition
Let $X_1,X_2,\ldots$ be independent and identically distributed with mean $\mu$, and write $S_n=X_1+\cdots+X_n$. If $\E|X_1|<\infty$, then $S_n/n\to\mu$ almost surely. If also $\mathrm{Var}(X_1)=\sigma^2<\infty$, then for every $\varepsilon>0$,
$$
\mathrm{P}(|S_n/n-\mu|>\varepsilon)\le\frac{\sigma^2}{n\varepsilon^2}\to 0.
$$
If $0<\sigma^2<\infty$, then $(S_n-n\mu)/(\sigma\sqrt{n})$ converges in distribution to a standard normal variable.{{cite:durrett2019}} (Thm. 2.4.1; Thm. 3.4.1)

## Interpretation — What each theorem spends
Chebyshev's inequality spends only the variance, and it proves the weak law under that hypothesis. It does not prove the strong law, because $\sum 1/n$ diverges. The strong law spends an absolute mean and a truncation or a moment argument, and it returns a pathwise limit with no rate. The central limit theorem spends a finite positive variance and returns the shape of the error. A variance of zero makes the centred sum identically zero, and the normal limit is then a point mass, which the statement excludes by asking for $\sigma^2>0$.{{cite:durrett2019}} (Thm. 3.4.1, p. 144)

The normal limit runs from de Moivre's binomial case through Laplace, Poisson, Chebyshev, Liapunov's characteristic functions, and Markov's extension beyond identical distributions. Pólya attached the qualifier "central" in 1920.{{cite:dodge2008}} (p. 66)

## Properties
The weak-law bound is Chebyshev's inequality. The normal limit is the characteristic-function argument Durrett records for identical summands.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
If $\mathrm{Var}(X_i)=\sigma^2$, the variance of $S_n/n$ is $\sigma^2/n$. Chebyshev's inequality at level $\varepsilon$ is the display above, and the right-hand side tends to zero. That is the weak law under a finite variance.{{cite:durrett2019}} (Thm. 1.6.4)

For the normal limit, centre the variables so that $\mu=0$. The characteristic function admits $\varphi(t)=1-\sigma^2 t^2/2+o(t^2)$. The standardised sum then has characteristic function
$$
\bigl(1-t^2/(2n)+o(n^{-1})\bigr)^n,
$$
which tends to $e^{-t^2/2}$. Convergence of characteristic functions to a normal characteristic function yields convergence in distribution to the standard normal law.{{cite:durrett2019}} (Thm. 3.4.1, p. 144)

The fair-coin tail is a binomial probability. With $n=100$ and $p=1/2$, $\mathrm{P}(S_{100}\ge 60)=1-\mathrm{P}(S_{100}\le 59)=0.0284$. The continuity correction uses the half-unit shift $(59.5-50)/5=1.9$.
:::
:::

## Statistical use — An average, a frequency, and a normal interval
A sample mean estimates $\mu$ because of the strong law, when the absolute mean is finite. A confidence interval of the form $\overline X\pm 1.96\, s/\sqrt{n}$ uses the normal limit, and it needs a variance that exists. Quoting the interval when the observations have an infinite variance borrows a theorem whose hypothesis has failed. A relative frequency is an average of indicators, which have every moment, so both the strong law and the normal approximation apply. For $100$ fair tosses the normal approximation to $\mathrm{P}(S\ge 60)$ is already within a few thousandths once the continuity correction is used, and the plain value $0.0228$ is the one that sits a little low.

## Worked example
Fair coin, $n=100$. Mean $50$, variance $25$, standard deviation $5$.

$$
\mathrm{P}(S\ge 60)=0.0284.
$$
The uncorrected normal approximation is
$$
1-\Phi\bigl((60-50)/5\bigr)=1-\Phi(2)=0.0228.
$$
The continuity correction is
$$
1-\Phi\bigl((59.5-50)/5\bigr)=1-\Phi(1.9)=0.0287.
$$
The corrected error is $0.0003$. The uncorrected error is $0.0056$. For a coarser event, $20$ tosses and $\mathrm{P}(S\le 8)$, the same pattern appears: the exact value is $0.2517$, the plain normal value is $0.186$, and the continuity correction, at $(8.5-10)/\sqrt{5}$, is about $0.251$.{{cite:durrett2019}} (Thm. 3.4.1)

**Your turn.** For the $100$ fair tosses, compute the Chebyshev bound on $\mathrm{P}(|S/n-1/2|\ge 0.1)$.

::: {.callout-tip collapse="true" title="Answer"}
The variance of the sample proportion is $(1/4)/100=0.0025$, and $0.1^2=0.01$, so the bound is $0.0025/0.01=0.25$. The event $|S-50|\ge 10$ includes $S\ge 60$ and $S\le 40$. The normal approximation to one of those tails is already about $0.023$, so two tails are about $0.046$, far below the Chebyshev number $0.25$.
:::

## Common misconceptions
The central limit theorem does not say that the observations are normal. It says that the centred and scaled sum is approximately normal. A single exponential observation is skewed. The average of many independent copies is not.

Convergence in distribution does not give convergence of the sample paths, and it does not give convergence of expectations without a further uniform-integrability condition. The strong law is the pathwise statement. The weak law is the probability statement. Neither is a normal approximation.

A continuity correction is not a change to the theorem. It is a way of reading a continuous distribution function at a half-integer when the sum is integer-valued. For $n=100$ it moves the approximation from $0.0228$ to $0.0287$. For a very large $n$ the half-unit is small beside $\sigma\sqrt{n}$, and the two readings draw together.

## Assumptions and limits — Infinite variance, and dependence
If the variance is infinite, $(S_n-n\mu)/(\sigma\sqrt{n})$ is not defined, and the normal limit in the identical-summand theorem does not apply. A symmetric stable law with index below $2$ is the classical replacement: the sum grows like $n^{1/\alpha}$ rather than $\sqrt{n}$. The strong law can still hold, because it asks only for an absolute mean.

Dependence breaks the product of characteristic functions that the identical-summand proof uses. A sequence of copies of one variable, $X_n=X$ for every $n$, has average $X$, which does not settle on $\E X$ unless $X$ is constant. The hypotheses are not decorative.

Lindeberg's theorem extends the normal limit to summands that are not identically distributed, under a condition that no one summand dominates the variance. Identical distribution is a convenient special case, not the last word.{{cite:durrett2019}} (Thm. 3.4.10, p. 148)

## Connections
The [strong law](strong-law.qmd) is the pathwise average. [Markov's inequality](markov-s-inequality.qmd) and Chebyshev's inequality are the moment bounds behind the weak law. The [normal distribution](normal-distribution.qmd) is the limit shape. A [binomial distribution](binomial-distribution.qmd) is a sum of Bernoulli trials, which is why the coin calculation is a limit theorem rather than a separate approximation.{{cite:durrett2019}} (Thm. 3.4.1){{cite:dodge2008}} (p. 66)

## History
The central limit theorem runs from de Moivre's binomial argument, through Laplace and Poisson, to Chebyshev's demonstration and Liapunov's characteristic-function form, and Pólya supplied the word "central" in 1920.{{cite:dodge2008}} (p. 66) The strong law, the probability-one limit of the average, is a different statement from the weak law.{{cite:dodge2008}} (pp. 298–299) The identical-summand normal limit used here is Durrett's statement for a finite positive variance, proved by convergence of characteristic functions to $e^{-t^2/2}$.{{cite:durrett2019}} (Thm. 3.4.1, p. 144)
