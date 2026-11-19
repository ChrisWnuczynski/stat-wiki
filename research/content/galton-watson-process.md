## Lead context
A Galton–Watson process is a generation count in which each living individual independently produces a random number of offspring from one common distribution, and the next generation is the sum of those offspring.

## Motivating example
A surname is carried by one person, who has either no children or two, with probabilities $1/4$ and $3/4$. The mean number of children is $3/2$, which is greater than 1, so the family tends to grow: the expected size of generation $n$ is $(3/2)^n$. Growth of the expectation does not save every family. The probability that the surname eventually disappears is $1/3$, and the probability that it survives forever is $2/3$. The mean says the typical generation gets larger. The extinction probability says a substantial minority of lineages still hit zero and stay there.{{cite:durrett2019}} (pp. 230–232, Galton–Watson process and the supercritical extinction root)

## Intuition
The state $Z_n$ is the number of individuals in generation $n$, starting from $Z_0=1$. Each of those individuals is replaced by an independent copy of an offspring count $\xi$. The state 0 is absorbing: nobody is left to have children. The one-step conditional mean is $m Z_n$, where $m=\E\xi$. Taking expectations gives $\E Z_n=m^n$. That recursion is linear, which is why the expectation is easy. The extinction event is not a statement about the expectation. It is the event that $Z_n$ hits 0. Because 0 is absorbing, these events nest, and the probability increases to the chance of eventual extinction.{{cite:durrett2019}} (p. 230, the generation recursion and the martingale property)

## Definition
Let $\xi_{n,i}$ be independent and identically distributed on the non-negative integers, with $\Pr(\xi=k)=p_k$ and mean $m\in(0,\infty)$. Set $Z_0=1$ and
$$
Z_{n+1}=\sum_{i=1}^{Z_n}\xi_{n+1,i}
$$
when $Z_n>0$, and $Z_{n+1}=0$ when $Z_n=0$. Durrett calls $Z_n$ a Galton–Watson process and $p_k$ the offspring distribution. The offspring probability generating function is $f(s)=\E(s^\xi)=\sum_k p_k s^k$ for $s\in[0,1]$. Then $f(1)=1$, and $f'(1-)=m$ when the mean is finite. The generating function of $Z_n$ is the $n$-fold composition of $f$ with itself.{{cite:durrett2019}} (pp. 230–232, §4.3.4)

## Interpretation — Mean, extinction, and a root of $f$
Write $q=\Pr(Z_n=0\text{ for some }n)$. Then $q=f(q)$, and $q$ is the smallest root of that equation in $[0,1]$. Durrett's theorem splits on the mean, for a non-degenerate offspring law. If $m<1$, then $\Pr(Z_n>0)\le m^n$, so extinction has probability 1 and the approach is exponentially fast. If $m=1$ and $\Pr(\xi=1)<1$, extinction still has probability 1, but the bound $m^n$ no longer moves. If $m>1$ and $p_0>0$, there is a root in $[0,1)$ and the extinction probability is that root, so survival has positive probability. The deterministic law $\xi=1$ has mean 1 and extinction probability 0. It is the degenerate case the critical theorem excludes.{{cite:durrett2019}} (pp. 231–232, subcritical, critical and supercritical extinction)

## Properties — The mean, a variance recurrence, and the critical limit
Conditioning on $Z_n$ gives $\E(Z_{n+1}\mid Z_n)=m Z_n$, so $\E Z_n=m^n$ from $\E Z_0=1$. The law of total variance gives the recurrence $\Var(Z_{n+1})=m^2\Var(Z_n)+\sigma^2 m^n$, where $\sigma^2=\Var(\xi)$, because the conditional variance is $\sigma^2 Z_n$ and the variance of the conditional mean is $m^2\Var(Z_n)$. For $m\neq1$ the solution with $\Var(Z_0)=0$ is
$$
\Var(Z_n)=\sigma^2 m^{n-1}\frac{m^n-1}{m-1}.
$$
At $m=1$ the same limit is $\Var(Z_n)=n\sigma^2$. The formula at $n=1$ returns $\sigma^2$, which is the variance of a single offspring count.{{cite:durrett2019}} (p. 231, $\E Z_n=m^n$ from the martingale mean)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The empty sum is 0, so $Z_n=0$ implies $Z_{n+1}=0$. Thus $\{Z_n=0\}\subset\{Z_{n+1}=0\}$ and $q_n=\Pr(Z_n=0)$ increases to $q$. The generating-function recursion is $q_{n+1}=f(q_n)$ with $q_0=0$, so the limit satisfies $q=f(q)$.

If $m<1$, Markov's inequality on the non-negative variable $Z_n$ gives $\Pr(Z_n\ge1)\le\E Z_n=m^n\to0$. If $m=1$ and the offspring law is not concentrated at 1, $Z_n$ is a non-negative integer martingale, so it converges almost surely to a finite limit. The only way an integer process can converge and keep moving with a non-degenerate offspring law is to settle at 0. If $m>1$, $f$ is strictly convex on $[0,1)$ whenever some $p_k>0$ for a $k\ge2$, which is implied by $m>1$. Then $f(s)=s$ has exactly one root in $[0,1)$, and Durrett identifies the extinction probability with that root.{{cite:durrett2019}} (pp. 231–232, the three extinction regimes)
:::
:::

## Statistical use — What to compute before simulating a tree
Compute $m$ first. If $m\le1$ and the law is non-degenerate with $p_0>0$, the extinction probability is 1 and a long simulation should be judged by how fast it hits zero, not by whether a few paths look large at generation 10. If $m>1$, solve $f(s)=s$ on $[0,1)$. The smaller root is the extinction probability. The mean $(m^n)$ and the extinction probability are different functionals of $p_k$: two supercritical laws with the same mean can have different roots, because $f$ uses every $p_k$. A simulation that reports only the average generation size has not estimated $q$.{{cite:durrett2019}} (p. 232, the root depends on the generating function, not only on $m$)

## Worked example
Take $p_0=1/4$ and $p_2=3/4$. Then $m=3/2$ and $\E\xi^2=4\times3/4=3$, so $\sigma^2=3-(3/2)^2=3-9/4=3/4$. The generating function is $f(s)=1/4+(3/4)s^2$. Solving $f(s)=s$ gives $3s^2-4s+1=0$, or $(3s-1)(s-1)=0$. The roots are $1$ and $1/3$. The extinction probability is the smaller one, $q=1/3$. The survival probability is $2/3$.

The mean generation sizes are $1$, $3/2$, $9/4$ for $n=0,1,2$. The variance formula at $n=2$ is
$$
\Var(Z_2)=\frac34\cdot\frac32\cdot\frac{(9/4)-1}{1/2}=\frac{45}{16}=2.8125.
$$
At $n=1$ it returns $3/4$, the offspring variance. Generation 1 is extinct with probability $1/4$, which is smaller than the eventual extinction probability $1/3$: some families that are alive after one generation die later.{{cite:durrett2019}} (pp. 231–232, mean $m^n$ and the extinction root)

**Your turn.** For $\Pr(\xi=0)=2/5$, $\Pr(\xi=1)=1/5$ and $\Pr(\xi=2)=2/5$, find the mean and the extinction probability.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $0\cdot2/5+1\cdot1/5+2\cdot2/5=1$. The law is not concentrated at 1, since $p_0=2/5>0$. The critical case therefore has extinction probability 1. The generating function $f(s)=2/5+s/5+(2/5)s^2$ meets $y=s$ only at $s=1$, because $f(s)-s=(2/5)(s-1)^2$.
:::

## Common misconceptions
A mean greater than 1 does not make extinction impossible. In the two-or-none example the mean is $3/2$ and the extinction probability is still $1/3$. A mean equal to 1 does not leave a positive chance of survival, except in the degenerate case where every individual has exactly one child. The expected size $\E Z_n=m^n$ is not a typical size on the event of extinction: on that event the size is eventually 0, and the large expectation is carried by the surviving paths. And $Z_n$ is a Markov chain, but it is not a random walk. The next step's distribution depends on the current population size, because more parents produce a more variable sum.

## Assumptions and limits — When the generation story fails
The theorems use independent individuals and one offspring distribution that does not change with time or with the current population. A nursery that shares a finite food supply violates the independence: one individual's offspring changes the chances of the others. A mean that itself changes with $n$, because the environment changes, is not the constant $m$ in $\E Z_n=m^n$. If $p_0=0$, extinction is impossible and $q=0$, whatever the mean. The interesting threshold $m=1$ needs a chance of zero children before it can force extinction. Starting from $r$ independent ancestors replaces $q$ by $q^r$, because the $r$ families die out only if each of them dies out. That power is smaller than $q$ when $q<1$, so a larger founding population is harder to extinguish even though each lineage has the same offspring law.{{cite:durrett2019}} (p. 230, independent offspring)

## Connections
The [probability generating function](probability-generating-function.qmd) is $f$, and extinction is its smallest fixed point. A [Markov chain](markov-chain.qmd) is the right dependence structure, with 0 absorbing. [Markov's inequality](markov-s-inequality.qmd) gives the subcritical bound $\Pr(Z_n>0)\le m^n$. The passage from $\sigma^2$ to $\Var(Z_n)$ is the law of total variance.{{cite:durrett2019}} (pp. 230–232, martingale and extinction criteria)

## History
Durrett introduces the process as the generation count $Z_n$ built from independent offspring, names it a Galton–Watson process, and proves the martingale property of $Z_n/m^n$. The extinction criteria he records are the subcritical bound, the critical case excluding a deterministic single child, and the supercritical identification of $q$ with the smaller fixed point of the generating function. Those three theorems are the content of the threshold $m=1$.{{cite:durrett2019}} (pp. 230–232, §4.3.4)
