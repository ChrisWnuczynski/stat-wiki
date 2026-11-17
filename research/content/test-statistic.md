## Lead context
A hypothesis test reduces the sample to one number and then asks whether that number is surprising under a stated hypothesis. The number is a test statistic: a [statistic](statistic.qmd), so it is a function of the sample, chosen because its distribution is known when the hypothesis is true. {{cite:dodge2008}} (p. 249) {{cite:nist_glossary2002}} (Glossary, "statistic")

## Motivating example
A coin is tossed 8 times and shows 7 heads. The count of heads is a statistic. Under a hypothesis that the coin is fair and the tosses are independent, that count has a binomial distribution with $n=8$ and $p=1/2$. The probability of 7 or 8 heads is $\binom{8}{7}/256+\binom{8}{8}/256=9/256\approx 0.0352$. The test uses the count because that probability can be computed before the tosses are seen. {{cite:openintro2019}} (Ch. 5, §5.3) {{cite:dodge2008}} (p. 249)

## Intuition
Any function of the sample is a statistic. A test statistic is one that has been paired with a hypothesis and a rejection rule. The rule looks at the statistic, not at the whole sample. Information that the statistic discards cannot affect the decision. The distribution used to build the rule is the sampling distribution of the statistic when the hypothesis is true, which is a different object from the distribution of the raw observations. {{cite:nist_glossary2002}} (Glossary, "sampling distribution") {{cite:dodge2008}} (p. 249)

## Definition
Let $X_1,\ldots,X_n$ be the sample and let $T=t(X_1,\ldots,X_n)$ depend only on the sample and on known constants. Then $T$ is a statistic. It is a test statistic for a hypothesis $H_0$ when a test rejects $H_0$ for some set of values of $T$, and the probability of that set is computed under $H_0$. The [significance level](significance-level.qmd) is that probability, or an upper bound on it. {{cite:dodge2008}} (pp. 249–251) {{cite:nist_glossary2002}} (Glossary, "statistic")

## Statistical use
The one-sample $t$ statistic $( \bar X-\mu_0)/(s/\sqrt{n})$ is a test statistic for a normal mean equal to $\mu_0$. The binomial count is a test statistic for a probability. A rank sum is a test statistic for a comparison that does not use the raw scale. In each case the procedure is: name $H_0$, name $T$, and name the values of $T$ that reject $H_0$. The [p-value](p-value.qmd) is the probability, under $H_0$, of a result at least as unfavourable to $H_0$ as the observed value of $T$. {{cite:openintro2019}} (Ch. 5, §5.3) {{cite:dodge2008}} (p. 251)

## Worked example
Eight fair-coin probabilities give $P(T\ge 7)=9/256$. A rule that rejects fairness when $T\ge 7$ therefore has level $9/256\approx 0.0352$ if the coin is fair and the tosses are independent. An observed count of 7 rejects that hypothesis at this level. An observed count of 6 does not, because 6 is not in the rejection set. The level is a property of the rule, computed before the tosses.

**Your turn.** Under the same fair-coin model, what is $P(T=8)$?

::: {.callout-tip collapse="true" title="Answer"}
$P(T=8)=1/256$.
:::

## Common misconceptions
The test statistic is not the hypothesis and it is not the level. A large value of $T$ is evidence against $H_0$ only relative to the rejection rule. A statistic that cannot be computed from the sample, because it still contains an unknown parameter, is not a test statistic. The $t$ statistic replaces the unknown standard deviation by $s$ for that reason. The normal $z$ score that still divides by an unknown $\sigma$ is not a statistic of the sample alone. {{cite:nist_glossary2002}} (Glossary, "statistic") {{cite:dodge2008}} (p. 249)

## Connections
A [statistic](statistic.qmd) is the general object. A test statistic is a statistic tied to a hypothesis. The [sampling distribution](sampling-distribution.qmd) of $T$ under $H_0$ supplies the level. The [Kruskal–Wallis test](kruskal-wallis-test.qmd) is one rank statistic of this kind. A [standard score](standard-score.qmd) is a change of unit, and it becomes a test statistic only when it is paired with a hypothesis and a rejection rule. {{cite:dodge2008}} (pp. 249–251) {{cite:openintro2019}} (Ch. 5, §5.3)
