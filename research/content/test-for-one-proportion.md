## Motivating example
Eight favourable responses out of ten can sound persuasive until they are compared with what chance alone can produce. If each person independently chooses between two products and the null probability of preferring the new product is one half, the relevant event for an upper-tail test is observing eight or more preferences, not observing exactly eight. A test turns the scientific direction of interest into a tail of a specified sampling distribution.{{cite:dodge2008}} (pp. 47–48, “Binomial Test”)

## Definition
Write $Y_i=1$ for a success and $Y_i=0$ for a failure. The binomial model assumes a fixed number $n$ of independent trials with one common success probability $p$, giving $X=\sum_iY_i\sim\operatorname{Bin}(n,p)$. For the upper alternative, the exact $p$-value is
$$p_{\mathrm{upper}}=\sum_{k=x}^{n}{n\choose k}p_0^k(1-p_0)^{n-k}.$$
All probabilities in this calculation use $p_0$. Substituting the observed proportion into the null distribution would answer a different question.{{cite:openintro2019}} (§6.1, “Hypothesis testing for a proportion”)

For the composite null $p\le p_0$, the same rejection rule controls size at its boundary. To see this, take independent uniform variables $U_i$ and construct $Y_i(p)=1\{U_i\le p\}$. Their sum is nondecreasing in $p$ for every realised collection of uniforms. Thus $\Pr_p(X\ge c)$ is nondecreasing in $p$, and the largest null rejection probability occurs at $p_0$.

## Properties — Discreteness and two-sided choices
For the yoghurt experiment, the upper-tail probabilities at $8$ and $9$ are $56/1024=0.0546875$ and $11/1024=0.0107421875$. There is no integer cutoff with size exactly $0.05$. Using the smallest allowable cutoff, $9$, makes the test conservative: under the null it rejects with probability approximately $0.01074$. Its nonrejection at $8$ does not establish equality of the population preferences.{{cite:dodge2008}} (pp. 47–48, decision rules)

Two-sided exact tests need an explicit convention because there is no single continuous symmetric tail in a general binomial model. One choice rejects using equal tails, allocating at most $\alpha/2$ to each. Another sums probabilities of outcomes whose null probability mass is no greater than that of the observed outcome. They can differ when $p_0\ne1/2$. Report the convention when reproducing an exact result. In the symmetric $n=10,p_0=1/2,x=8$ example, both give two-sided $p$-value $0.109375$.

## Statistical use — The score approximation
For a sufficiently large binomial sample, standardising under the null gives
$$Z=\frac{\hat p-p_0}{\sqrt{p_0(1-p_0)/n}}.$$
The normal approximation requires adequate expected successes and failures under the null, rather than a large $n$ in isolation. With $n=200$, $x=120$ and $p_0=1/2$, $Z=2.8284$ and the upper normal-tail probability is approximately $0.00234$. The exact upper-tail probability is approximately $0.00284$. A continuity correction uses $119.5$ rather than $120$ in the count-scale standardisation and gives approximately $0.00291$. The approximation and exact test are close here but are distinct procedures.{{cite:openintro2019}} (§6.1, normal approximation and success-failure condition)

When $p_0$ is close to an endpoint, an exact binomial calculation is straightforward and avoids relying on a poor normal tail. An observed proportion of zero or one also makes an estimated Wald standard error vanish, whereas the null-based score standard error is positive for $0<p_0<1$.

## Worked example — A rejection rule and its power
For $n=10$ and a one-sided $5\%$ test of $p=1/2$, the critical region is $X\ge9$. If the true success probability is $0.8$, its power is
$$\Pr_{0.8}(X\ge9)=10(0.8)^9(0.2)+(0.8)^{10}\approx0.37581.$$
A real effect can therefore be missed often in a small experiment. A large observed fraction and a weak rejection probability are compatible: precision depends on the sample size as well as the fraction. Power is evaluated at a specified alternative, while a $p$-value is evaluated under the null.{{cite:openintro2019}} (§5.3, “Hypothesis testing”, errors and power)

**Your turn.** With $n=5$, $p_0=1/2$ and an upper alternative, compute the exact $p$-value for five successes. Does a nonrandomised test reject at level $0.05$? What is its size if it rejects only at five successes?

::: {.callout-tip collapse="true" title="Answer"}
The tail contains only $X=5$, with probability $(1/2)^5=1/32=0.03125$. The observation is rejected at $0.05$. The rejection rule has size $0.03125$, below the nominal level because the next possible tail probability is too large.
:::

## Assumptions and limits
Independent people need not supply independent outcomes if they taste products together and influence one another. Repeated preferences from the same person also require a dependence model. Different success probabilities across trials produce a Poisson-binomial distribution rather than a binomial distribution. Optional stopping changes the sampling rule, so a fixed-$n$ tail calculation cannot automatically be reused after repeatedly inspecting accumulating responses. Define the trial, success event, alternative direction and stopping rule before interpreting a reported significance level.
