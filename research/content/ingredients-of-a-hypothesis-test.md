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
