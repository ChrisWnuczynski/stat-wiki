## Motivating example
A manufacturer says that a new assembly method raises the probability that a component passes inspection. Before looking at the data, the investigator must decide what “raises” means. If the established pass probability is one half, a useful alternative is $p>1/2$; unusually *many* passes count against the null. A result with unusually few passes would not support improvement, even though it would be surprising under exactly one half. The alternative therefore determines which observations count as evidence and which tail of a sampling distribution is relevant.{{cite:neyman_pearson1933}} (pp. 293–298, choice of a critical region)

## Intuition
The null $H_0$ is the claim for which the test promises control of mistaken rejection. The alternative $H_1$ identifies the departures the test is meant to detect. This asymmetry is deliberate: a critical region is chosen so that landing there is rare under the null, while being common under relevant alternatives. The hypotheses are statements about a population distribution or model parameter, not descriptions of the observed sample itself. They must be fixed before deciding whether the observed result is extreme.{{cite:neyman_pearson1933}} (pp. 293–295, sample and critical regions){{cite:dodge2008}} (p. 249, “Hypothesis”)

The words “no effect” are common shorthand for a null, but a null can assert any scientifically meaningful restriction. A regulator might test that a defect rate does not exceed a legal limit; a trial might test that an improvement is no greater than a minimum useful amount. The null can also include many parameter values rather than one. Stating the parameter and the relevant inequalities prevents a directional claim from being silently treated as a two-sided claim.{{cite:neyman_pearson1933}} (pp. 294, 312, simple and composite hypotheses)

## Definition
For a statistical model indexed by $\theta\in\Theta$, choose disjoint sets $\Theta_0$ and $\Theta_1$. Write $H_0:\theta\in\Theta_0$ for the **null hypothesis** and $H_1:\theta\in\Theta_1$ for the **alternative hypothesis**. A *simple* hypothesis specifies one distribution completely; a *composite* hypothesis permits more than one. If $\Theta_0$ and $\Theta_1$ together cover the candidate parameter space, the two claims are exhaustive, but disjointness is the essential condition for assigning errors without ambiguity.{{cite:neyman_pearson1933}} (p. 294, simple and composite hypotheses)

A test chooses a rejection region $R$ in the sample space. It rejects $H_0$ when the observed data fall in $R$. Its type I error probability at a null parameter is $\Pr_\theta(X\in R)$, while its power at an alternative parameter is the same probability evaluated under that alternative. For a composite null, the test's size is $\sup_{\theta\in\Theta_0}\Pr_\theta(X\in R)$; a level-$\alpha$ test keeps this supremum at most $\alpha$. Type II error at a particular alternative is $1-\Pr_\theta(X\in R)$.{{cite:neyman_pearson1933}} (pp. 293–298, critical region and alternatives)

## Interpretation
The statement $H_0:p=1/2$ versus $H_1:p>1/2$ is one-sided: low counts are not evidence for the stated improvement. A two-sided $H_1:p\ne1/2$ would instead treat unusually low *and* unusually high counts as evidence. The same data can therefore produce different $p$-values under these two predeclared questions. A test outcome is “reject” or “do not reject” the null. Failure to reject can arise because the null is close to the truth, because the sample is small, or because the test has little power against the relevant alternative; it does not establish that the null is true.{{cite:neyman_pearson1933}} (pp. 293–298, design of critical regions)

If $H_0:p\le1/2$ and $H_1:p>1/2$, the null is composite. For a binomial count and an upper-tail rejection region, the largest false-rejection probability among all $p\le1/2$ occurs at the boundary $p=1/2$. Checking that boundary is enough *for this monotone count test*. For another model or a differently shaped rejection region, the least favourable null value must be found rather than assumed.{{cite:neyman_pearson1933}} (pp. 312–317, composite hypotheses)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $X_p=\sum_{i=1}^n\mathbf1\{U_i\le p\}$ for independent uniform random variables $U_i$. Then $X_p\sim\operatorname{Bin}(n,p)$. If $p\le q$, each indicator at $p$ is no larger than the corresponding indicator at $q$, so $X_p\le X_q$ for every outcome of the uniforms. Consequently, for any fixed upper-tail rule $R=\{X\ge c\}$, $\Pr_p(R)\le\Pr_q(R)$. Thus $\sup_{p\le p_0}\Pr_p(X\ge c)=\Pr_{p_0}(X\ge c)$, proving that the boundary controls the whole composite null in this binomial test. By the definitions of the two errors, at an alternative value $p$ the non-rejection probability is $1-\Pr_p(R)$.{{cite:neyman_pearson1933}} (pp. 293–298, critical regions; pp. 312–317, composite hypotheses)
:::
:::

## Statistical use — Choosing the question before the cutoff
Start with the scientific effect and a model parameter that measures it. Put into $H_1$ the direction and magnitude that would answer the scientific question; place the remaining values in $H_0$ when that partition matches the decision. Choose a statistic that changes predictably under $H_1$, and calibrate its rejection region over *all* null values. A level such as $0.05$ is a design limit on false rejection under the model, not a probability that $H_0$ is true. Reporting the estimate and an interval as well as the test result shows the size and precision of the effect the data support.{{cite:neyman_pearson1933}} (pp. 293–298, test design)

The calculation above assumes twelve independent trials with one shared pass probability. If a machine fault causes failures to arrive in clusters, the count need not be binomial and $79/4096$ is not its null tail probability. If the investigator tries several cutoffs and reports only the one that rejects, the stated size no longer describes the selection procedure. If improvement was the promised question but the data lead to an unplanned two-sided test, the error guarantee belongs to the original design, not the revised story. The hypotheses and sampling protocol together determine the interpretation.{{cite:neyman_pearson1933}} (pp. 293–295, sampling model and critical region)

## Worked example
Suppose $12$ independent components pass or fail inspection with common pass probability $p$, and the investigator asks whether the new method improves on $p=1/2$. Use $H_0:p\le1/2$ against $H_1:p>1/2$. For $X$, the number passing, choose the upper-tail rule “reject if $X\ge10$.” At the null boundary,
$$
\Pr_{1/2}(X\ge10)=\frac{\binom{12}{10}+\binom{12}{11}+\binom{12}{12}}{2^{12}}
=\frac{79}{4096}\approx0.0193.
$$
The coupling proof shows that this is the maximum false-rejection probability over the entire composite null. The rule is therefore a level-$0.05$ test, though its actual size is about $0.0193$. Choosing the lower cutoff $X\ge9$ would give $299/4096\approx0.0730$, which exceeds $0.05$. The discreteness of $X$ prevents these simple nonrandomised cutoffs from hitting $0.05$ exactly.{{cite:neyman_pearson1933}} (pp. 293–298, critical regions)

If $10$ components pass, the one-sided $p$-value is $79/4096\approx0.0193$, so this rule rejects. That result is evidence for an increased pass probability under the assumed binomial model; it is not a $98.07\%$ probability that the method works. At $p=0.7$, the rule's power is $\Pr_{0.7}(X\ge10)\approx0.2528$, and its type II error probability is about $0.7472$. The strong-looking result for this particular sample coexists with poor sensitivity to a moderate real improvement.{{cite:neyman_pearson1933}} (pp. 293–298, power at an alternative)

**Your turn.** Keep the same twelve-trial model and cutoff, but suppose only nine components pass. State the test decision at level $0.05$, give the one-sided tail probability rounded to four decimals, and explain whether that decision proves $p\le1/2$.

::: {.callout-tip collapse="true" title="Answer"}
Nine passes do not reach the cutoff of ten, so the test does not reject. The one-sided tail probability is $\Pr_{1/2}(X\ge9)=299/4096\approx0.0730$, larger than $0.05$. The result does not prove $p\le1/2$; for example, the test misses many samples even when $p=0.7$, as its power calculation shows.
:::

## Common misconceptions
A null need not mean “nothing happens”: $p\le1/2$ is a range of pass rates, and a nonzero threshold can be the null boundary. A two-sided alternative is not interchangeable with a one-sided one after the data are seen, since it changes which outcomes count as extreme. A $p$-value is a probability of data under a specified null model, not a probability of the null given the data. And “do not reject” is not “accept as true”: low power gives the same decision for many genuine alternatives. These errors concern different parts of the testing setup and cannot be repaired by changing only the significance cutoff.{{cite:neyman_pearson1933}} (pp. 293–298, relation of hypotheses and critical regions)

## Connections
[Type I and type II errors](type-i-and-type-ii-errors.qmd) attach consequences to the two possible wrong decisions. A [critical region](critical-region.qmd) translates the alternative into a rejection rule. A [power function](power-function.qmd) compares the rule across alternative parameter values; a [p-value](p-value.qmd) reports the extremeness of the observed statistic under the null. [Tests and confidence intervals](tests-and-confidence-intervals.qmd) can express related questions through inversion, provided their alternatives and coverage rules agree.{{cite:neyman_pearson1933}} (pp. 293–298)

## History
The names of the hypotheses reflect two strands in the history of testing. Fisher's 1935 discussion of the tea-tasting experiment used the term “null hypothesis,” after an earlier habit of testing a no-effect null. Neyman and Pearson's 1933 paper made the distinction between a tested hypothesis and specified alternatives central to choosing a critical region with controlled false rejection and useful power.{{cite:dodge2008}} (pp. 249–250, “Hypothesis” and “Hypothesis Testing”){{cite:neyman_pearson1933}} (pp. 293–298)
