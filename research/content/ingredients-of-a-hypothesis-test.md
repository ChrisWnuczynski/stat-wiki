## Motivating example
A tennis player has thirteen successful serves out of fifteen after coaching, against a reference success probability of $0.6$. Success frequency is an estimate; deciding whether the result challenges the reference requires a model, hypotheses, a statistic and a rule for what counts as extreme. Changing the alternative after seeing the result changes the question being tested.{{cite:openintro2019}} (§5.3.1, hypothesis testing framework)

## Intuition
The model describes possible data under different parameter values. The null selects a subset of those values, and the alternative determines the departures the test should detect. A significance level specifies the maximum intended false-rejection probability under the null. It is not a probability that the null is true. The test's critical region implements the decision rule.{{cite:dodge2008}} (p. 250, mathematical aspects of hypothesis testing)

## Properties — Calibration is a probability statement
Write $\varphi(X)=1$ for rejection and zero otherwise. A level-$\alpha$ test satisfies $\sup_{\theta\in\Theta_0}E_\theta\varphi(X)\le\alpha$. Its power at $\theta$ is $E_\theta\varphi(X)$. For a simple continuous null with CDF $F_0$ and an upper-tail test, $p=1-F_0(T)$ is uniform under that null: for $0<u<1$,
$$P_0(p\le u)=P_0\{T\ge F_0^{-1}(1-u)\}=u.$$
Therefore rejecting when $p\le\alpha$ has size $\alpha$. For discrete data, tail probabilities jump, so a nonrandomized test is often conservative. The critical region is defined through the null sampling distribution.{{cite:dodge2008}} (p. 452, “Rejection Region”)

## Worked example — A discrete upper tail
Under $H_0:p=0.6$, the serve count is $X\sim\operatorname{Bin}(15,0.6)$. Against improvement, the observed count thirteen has $p$-value
$$P_{0.6}(X\ge13)=\sum_{j=13}^{15}\binom{15}{j}0.6^j0.4^{15-j}=0.02711.$$
The 5% rejection region is $X\ge13$, whose actual null probability is $0.02711$. Including twelve would raise it to $0.09050$, exceeding 5%. This demonstrates why choosing a nominal level need not produce that exact error probability. Independence and a common success probability across serves are the binomial model's substantive assumptions.{{cite:openintro2019}} (§6.1.3, tests for a proportion)

**Your turn.** A fair coin is tossed five times and all tosses are heads. Find the one-sided $p$-value for excess heads. Would the rule reject at 5%?

::: {.callout-tip collapse="true" title="Answer"}
The upper-tail probability is $P(X=5)=1/32=0.03125$. The one-sided rule rejects at 5%. A symmetric two-sided tail convention counts all heads and all tails, giving $2/32=0.0625$ and a different decision.
:::

## Statistical use — Distinguish evidence, decision and magnitude
The blood-pressure illustration assumes 101 independent readings with known standard deviation 7, a reference mean of 127 and observed mean 130. Its standardized deviation is $3\sqrt{101}/7=4.3071$, giving two-sided $p\approx1.65\times10^{-5}$. The magnitude is a three-unit difference, a separate quantity from its strength of evidence. Conventional cutoffs cannot establish whether that difference matters for a particular decision.{{cite:openintro2019}} (§5.3, “Choosing a significance level” and “Statistical significance versus practical significance”)

## Assumptions and limits
A test can reject because its sampling assumptions fail, rather than because the scientific explanation of interest holds. Conversely, failure to reject may reflect low power. For composite nulls, nuisance parameters must be eliminated, estimated with a justified reference argument, or controlled uniformly. A two-sided $p$-value requires an extremeness convention; equal tails work naturally for continuous symmetric location tests but are not the unique choice for discrete or asymmetric laws.{{cite:openintro2019}} (§5.3.3–5.3.4, decision errors and formal p-values)

## Lead context
A hypothesis test starts from a model for the data, a null statement inside that model, a statistic, and a rule that says which values of the statistic count as evidence against the null. The probability of those values, computed as if the null were true, is the size of the test when the null is simple. A tail probability computed from the observed statistic is not the same number as the power at some other parameter value.{{cite:openintro2019}} (§5.3.1, hypothesis testing framework)

## Definition
For a $\mathrm{Binomial}(15,0.6)$ count, the upper $5\%$ rule that rejects for $X\ge 13$ has null probability about $0.02711$. The event $X\ge 12$ has null probability about $0.09050$, which is already above $5\%$. The discrete distribution cannot spend exactly $5\%$. If the true success probability is $0.8$, the probability of $X\ge 13$ is about $0.398$. That is the power at $0.8$. It uses the same rejection region and a different probability. Five heads in five fair tosses have probability $1/32=0.03125$. The two-sided event, five heads or five tails, has probability $2/32=0.0625$.{{cite:openintro2019}} (§6.1.3, tests for a proportion)

## Interpretation
A $p$-value is the null probability of a result at least as extreme as the one observed, for a chosen ordering of the sample space. For the one-sided $t_{39}$ comparison with observed statistic $2.575$, the upper tail is $0.007$ and the $0.99$ quantile is $2.43$. The blood-pressure statistic $4.3071$ has two-sided tail probability about $1.65\times 10^{-5}$, which rounds to $0.000017$ at six decimals. These numbers are calculations under the stated model and the stated null.{{cite:dodge2008}} (p. 452, “Rejection Region”){{cite:openintro2019}} (§5.3, “Choosing a significance level” and “Statistical significance versus practical significance”)

## Common misconceptions
The model and the null are different ingredients. The binomial model says the count is binomial; the null says the success probability is $0.6$. Rejecting $X\ge 13$ is evidence against that success probability inside the binomial model. It is not evidence against every other model that could produce counts between $0$ and $15$. A second confusion is to treat the achieved size $0.02711$ as a defect. The test was built to stay at or below $5\%$, and the next smaller critical value would exceed $5\%$. A third confusion is to read power as a $p$-value. Power is the rejection probability at a specified alternative. The $p$-value is computed from the observed statistic under the null. Changing the true success probability from $0.6$ to $0.8$ changes the power and leaves the observed $p$-value's reference distribution unchanged.{{cite:openintro2019}} (§5.3.3–5.3.4, decision errors and formal p-values){{cite:dodge2008}} (p. 250, mathematical aspects of hypothesis testing)

## Connections
Size and power use the same rejection region and different probabilities. For $X\sim\mathrm{Binomial}(15,0.6)$, the region $X\ge 13$ has null probability about $0.02711$. The region $X\ge 12$ has null probability about $0.09050$, already above $5\%$. If the true success probability is $0.8$, the probability of $X\ge 13$ is about $0.398$. That number is the power at $0.8$. The null tail stays $0.02711$ because the reference distribution was computed at $0.6$.

Five heads in five fair tosses have probability $1/32=0.03125$. Counting five heads or five tails gives $2/32=0.0625$. The two calculations share the data and use different rejection regions. A $p$-value is the null probability of results at least as extreme as the one observed, for a stated ordering. The caffeine comparison with statistic $2.575$ on $39$ degrees of freedom has a one-sided tail of $0.007$, and the $0.99$ quantile of that reference is $2.43$. The blood-pressure statistic $4.3071$ has a two-sided tail near $1.65\times 10^{-5}$. None of these tails is the probability that the null hypothesis is true.{{cite:openintro2019}} (§5.3.3–5.3.4, decision errors and formal p-values)
