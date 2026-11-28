## Lead context
The rare-event limit keeps the expected count finite while increasing the number of independent trials.

## Motivating example — Many independent opportunities, a small chance on each
A component can fail on any one of many independent trials, with a small chance on each trial. For a fixed expected count, evaluating the probability of several failures should not require a different conceptual model each time the number of opportunities changes. The Poisson approximation replaces the two binomial parameters by their product. Independence and small per-trial probabilities are the structural assumptions behind this limit.{{cite:grinstead_snell1997}} (§5.1, pp. 187–189)

## Statement
Suppose $X_n\sim\operatorname{Bin}(n,p_n)$ and $np_n\to\lambda\in[0,\infty)$. Then $X_n$ converges in distribution to a Poisson variable with mean $\lambda$. For each fixed nonnegative integer $k$, the point probabilities converge to $e^{-\lambda}\lambda^k/k!$, with the case $\lambda=0$ interpreted as mass one at zero. This is the identical-probability special case of rare-event convergence for independent indicator arrays.{{cite:durrett2019}} (§3.6.1, Thm. 3.6.1, pp. 167–168)

## Intuition — One expected count survives the limit
Writing $p_n\approx\lambda/n$ makes the mean $np_n$ approximately $\lambda$. The variance $np_n(1-p_n)$ then approaches the same value, since $p_n\to0$. Equal limiting mean and variance are consistent with the Poisson law, although matching moments alone does not prove convergence. The binomial-to-Poisson calculation in the Proof establishes the full fixed-count limit.{{cite:grinstead_snell1997}} (§5.1, pp. 187–189)

Holding $p$ fixed while taking $n$ large is a different regime: the binomial mean then increases without bound. The Poisson limit here requires the probabilities themselves to decrease. Large $n$ by itself therefore does not justify substituting a Poisson distribution with an unrelated mean.{{cite:durrett2019}} (§3.6.1, pp. 167–168)

## Proof
Put $\lambda_n=np_n$. For $\lambda>0$ and fixed $k$, the binomial mass factors as
$$
\mathbb{P}(X_n=k)=\frac{\lambda_n^k}{k!}
\left\{\prod_{j=0}^{k-1}\left(1-\frac jn\right)\right\}
(1-p_n)^n(1-p_n)^{-k}.
$$
The finite product tends to one, $\lambda_n^k\to\lambda^k$, and $(1-p_n)^{-k}\to1$. Also
$$
n\log(1-p_n)=-np_n+O(np_n^2)\longrightarrow-\lambda,
$$
because $np_n^2=(np_n)p_n\to0$. Consequently $(1-p_n)^n\to e^{-\lambda}$, giving the displayed Poisson mass. At $\lambda=0$, $\mathbb{P}(X_n\geq1)\leq \E(X_n)=np_n\to0$, so the count tends to zero in probability. The limiting masses sum to one, giving convergence in distribution.{{cite:grinstead_snell1997}} (§5.1, p. 189);{{cite:durrett2019}} (§3.6.1, pp. 167–168)

## Worked example
For $n=100$ and $p=0.02$, the mean is two. The exact no-failure probability is
$$
\mathbb{P}(X=0)=0.98^{100}\approx0.132620,
$$
whereas the Poisson approximation gives $e^{-2}\approx0.135335$. For exactly three failures, the exact binomial probability is approximately $0.182276$, compared with $e^{-2}2^3/3!\approx0.180447$. The differences have opposite signs, so the approximation is not a uniform upper or lower bound on every individual mass.{{cite:grinstead_snell1997}} (§5.1, p. 189)

**Your turn.** Increase the opportunities to $1000$ while keeping the mean equal to two. What value of $p$ is needed, and what is the exact no-failure probability?

::: {.callout-tip collapse="true" title="Answer"}
Use $p=2/1000=0.002$. The exact probability is $0.998^{1000}\approx0.135065$, closer to $e^{-2}\approx0.135335$ than the corresponding value for $100$ trials.
:::

## Related concepts — Unequal rare-event probabilities
[]{#property-unequal-independent-array}

The same limiting mechanism applies to independent Bernoulli indicators with unequal probabilities when their maximum probability tends to zero and their sum tends to a finite limit. These conditions control the chance of individual nonrare trials. Dependence needs additional arguments; matching the expected count cannot supply independence.{{cite:durrett2019}} (§3.6.1, Thm. 3.6.1, p. 167)
