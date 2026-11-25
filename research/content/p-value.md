## Motivating example
Suppose a fair-coin model is challenged after unusually many heads. A head count alone is hard to judge: fifteen heads in twenty tosses sounds different from fifteen in a thousand. A p-value turns the observed statistic into a null-model tail area, so the same planned test can be assessed at a stated error threshold. The tail must be chosen from the scientific question before seeing the count.{{cite:siegrist2022_testing}} (§9.1, P-value)

## Intuition — Extremeness belongs to a test
The p-value is calculated as though the null model generated the data. A one-sided question about an excess of heads counts outcomes at least as high as the observation; a two-sided question also counts a specified set of deficits. “As extreme” has no meaning until the statistic and alternative are specified. In the normal and Student $t$ examples below, symmetry makes the usual two-sided tail twice a one-sided tail beyond the absolute statistic. For a discrete and asymmetric null distribution, different defensible two-sided orderings need not agree, so the rule should be stated.{{cite:siegrist2022_testing}} (§9.1, P-value and parametric tests)

## Properties — A level has a frequency meaning
A valid p-value calculated from a test chosen in advance satisfies $\Pr_{H_0}(p\le\alpha)\le\alpha$ for every $0\le\alpha\le1$. Thus rejecting when $p\le0.05$ controls the probability of a false rejection at no more than $0.05$ under the stated null conditions. Equality holds for many continuous null statistics; discrete tails jump, so the test can be conservative. The inequality is about repeated data under $H_0$, not the probability that $H_0$ is true after observing this dataset. For a composite null, a valid calibration must control the error across its allowed parameter values.{{cite:siegrist2022_testing}} (§9.1, Tests and P-value)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For a prespecified statistic $T$ where large values contradict $H_0$, let $p(t)=\Pr_{H_0}(T'\ge t)$, with $T'$ an independent draw under the null. If $p(T)\le\alpha$, then $T$ lies in the upper rejection tail whose null probability is at most $\alpha$ by construction. Hence $\Pr_{H_0}\{p(T)\le\alpha\}\le\alpha$. If the distribution is continuous, the probability integral transform makes the tail area uniform on $(0,1)$, giving equality. For a discrete statistic, attainable tail areas are separated by jumps, giving possible strict inequality. The proof assumes the test statistic, tail and null distribution were fixed before looking at the observed data.{{cite:siegrist2022_testing}} (§9.1, P-value)
:::
:::

## Statistical use — Report the model and the question
Report the null and alternative, the statistic, the direction of the tail, the numerical p-value, and an effect estimate with uncertainty. A p-value near a conventional cutoff does not turn into a qualitatively different kind of evidence when a rounding digit changes. A small p-value can accompany a tiny but precisely measured difference, while a large one can reflect a small sample with poor power. The ASA's 2016 statement says conclusions should not rest only on crossing a threshold and that a p-value does not measure effect size or the probability a hypothesis is true.{{cite:asa2016_pvalues}} (six principles, pp. 1–2)

## Worked example — Which coin tail?
Under $H_0:p=0.5$, toss a coin independently $20$ times and observe $15$ heads. For the prechosen alternative $p>0.5$, the exact p-value is $\Pr(K\ge15)=\sum_{j=15}^{20}{20\choose j}/2^{20}=0.020695$ for $K\sim\operatorname{Binomial}(20,0.5)$. This is below $0.05$. If the prechosen alternative was $p\ne0.5$, symmetry gives the exact two-sided tail $\Pr(K\le5\text{ or }K\ge15)=2(0.020695)=0.041389$, also below $0.05$. The two numbers answer different questions; the second tail was not selected after seeing which result looked more favorable. Neither number says the coin is biased with probability $97.9\%$.{{cite:siegrist2022_testing}} (§9.1, P-value)

Now observe $0$ successes in $10$ independent Bernoulli trials with a common success probability $p$, testing $H_0:p=p_0=0.30$ against $p\ne0.30$. Under the null, $K\sim\operatorname{Binomial}(10,0.30)$ has mass $q(j)=\Pr_{H_0}(K=j)={10\choose j}0.3^j0.7^{10-j}$.{{cite:siegrist2022_binomial_distribution}} (§11.2, Distribution Functions, binomial mass formula) Probability-mass ordering includes counts whose null mass is no greater than $q(0)$: exactly $0$ and $7$–$10$. Its exact two-sided p-value is
$$
p_{\rm mass}=q(0)+\sum_{j=7}^{10}q(j)=0.0388396033\approx0.03883960.
$$
Twice the smaller inclusive tail, capped at one, instead gives $p_{\rm double}=\min\{1,2\min[\Pr_{H_0}(K\le0),\Pr_{H_0}(K\ge0)]\}=2(0.7^{10})=0.0564950498\approx0.05649505$. At level $0.05$, the first test rejects and the second does not. These are different two-sided tests of the same null; discrete, asymmetric distributions need not give the same result under these conventions.{{cite:agresti1992_exact_survey}} (p. 135, §2.1, two-sided conventions) Prespecify the convention: choosing the smaller p-value after seeing the data changes the testing procedure.

**Your turn.** With a fair-coin null, $9$ heads appear in $12$ independent tosses. Calculate the exact p-value for a prechosen excess-heads alternative and, separately, for a two-sided alternative. Would either reject at level $0.05$?

::: {.callout-tip collapse="true" title="Answer"}
$\Pr(K\ge9)=299/4096\approx0.072998$ for $K\sim\operatorname{Binomial}(12,0.5)$. The symmetric two-sided tail is $2(299/4096)\approx0.145996$. Neither is at most $0.05$, so neither test rejects. This is a failure to reject the fair-coin model, not proof that the coin is fair.
:::

## Common misconceptions
The p-value is not $\Pr(H_0\mid\text{data})$: it conditions on $H_0$, while a posterior probability would need a prior and an alternative model. Its complement $1-p$ is not the probability that the alternative is true. A small p-value does not quantify effect magnitude or practical importance. A large p-value does not establish equivalence or the truth of the null. See the worked example “Caffeine in cola” for how a one-sided test at the 1% level ($p\approx0.007$) and a two-sided 99% confidence interval that includes 19 mg answer different questions. Finally, a p-value is not the probability that “chance alone” produced the data: all outcomes in a stochastic model involve chance, and the tail calculation also depends on the model and test design.{{cite:asa2016_pvalues}} (principles 1–6, pp. 1–2)

## Assumptions and limits — When the reference experiment changes
The coin calculation fails as a calibrated binomial test if tosses influence one another or the probability of heads changes during the sequence. Optional stopping or choosing the more favorable of several outcomes after inspection changes the reference experiment. For example, with $20$ independent null tests each run at level $0.05$, the chance of at least one false rejection is $1-0.95^{20}\approx0.6415$, far above $0.05$ if only the smallest p-value is reported. An approximate normal tail can also miscalibrate a very small or skewed sample; an exact null calculation or justified simulation may be needed. All these problems concern how the tail was generated, not a cosmetic choice of cutoff.{{cite:asa2016_pvalues}} (principle 4, full reporting){{cite:siegrist2022_testing}} (§9.1, P-value)

## Connections
[A later poll](../questions/ex-da-brexit-poll.qmd) uses a two-sided normal tail; [the possum counts](../questions/ex-da-possums.qmd) use an upper chi-square tail; [an additive-model term](../questions/q-37.qmd) illustrates why the precise null tested matters. A [confidence interval](confidence-interval.qmd) shows effect sizes compatible with data; [power](power-function.qmd) describes the ability of a test to detect specified alternatives.{{cite:siegrist2022_testing}} (§9.1, Power and P-value)

## History
The American Statistical Association issued a public statement on p-values in 2016 after concern about threshold-based and selective reporting. Its six principles clarified the interpretation of a null-model tail area and urged full reporting and scientific context.{{cite:asa2016_pvalues}} (pp. 1–2, principles 1–6)
