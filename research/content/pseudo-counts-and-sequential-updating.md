## Motivating example
Suppose a laboratory records whether each test succeeds. The first five trials contain three successes, and the next five contain four. A Beta prior lets the laboratory update after the first batch and then use that posterior as the starting point for the second. The final answer must match an update using all ten results at once if the trials share one success probability. Pseudo-counts make that arithmetic easy to see, while also exposing how strongly the prior influences a small sample.{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270, beta-binomial example)

## Intuition
The Beta density contains a power of $\theta$ and a power of $1-\theta$. A binomial likelihood contributes the same two powers for observed successes and failures. Multiplication therefore adds the observed counts to the two Beta parameters. This is conjugacy: the posterior stays in the same distribution family. Counts from successive independent batches also add, so the order of updating cannot affect the final posterior. The prior parameters are *analogous* to counts, but their precise count interpretation changes with the posterior summary being used.{{cite:diaconis_ylvisaker1979}} (§1, p. 269)

## Definition
Let $X_i\mid\theta$ be conditionally independent Bernoulli trials with a common success probability $\theta$, and begin with $\theta\sim\operatorname{Beta}(\alpha,\beta)$, where $\alpha,\beta>0$. A batch of $n$ trials with $x$ successes gives $\theta\mid x\sim\operatorname{Beta}(\alpha+x,\beta+n-x)$. The posterior mean is $(\alpha+x)/(\alpha+\beta+n)$, a weighted average of the sample proportion and prior mean. For this *mean* interpretation, $\alpha$ and $\beta$ play the roles of prior success and failure counts, with total weight $\alpha+\beta$.{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270, beta posterior and linear posterior expectation){{cite:dodge2008}} (p. 40, Beta mean)

The posterior mode, when both updated shapes exceed one, is $(\alpha+x-1)/(\alpha+\beta+n-2)$. Its algebra suggests prior counts $\alpha-1$ and $\beta-1$. This is a different convention tied to a different summary, not a disagreement about the posterior distribution. If either shape is at most one, the mode may be on the boundary and the interior formula cannot be used. A fractional pseudo-count expresses prior weight; no fractional physical trial occurred.{{cite:dodge2008}} (p. 40, Beta density and mean){{cite:diaconis_ylvisaker1979}} (§1, p. 269, Beta density)

## Properties
For two batches $(x_1,n_1)$ and $(x_2,n_2)$, the final shape parameters are $\alpha+x_1+x_2$ and $\beta+(n_1-x_1)+(n_2-x_2)$. Reversing batches or combining them first gives the same pair. This *sequential coherence* is an identity within the fixed common-$\theta$ model. It does not say the model remains plausible if the mechanism changes between batches.{{cite:diaconis_ylvisaker1979}} (§1, p. 269, closure under sampling)

As the number of trials grows with a stable sampling process, the weight $n/(n+\alpha+\beta)$ on the sample proportion grows. With few trials, the prior mean can pull the posterior mean substantially. The equivalent sample-size reading applies to this Beta-Bernoulli mean, not automatically to every prior, parameter or prediction target. The additional warning in the original section about $\operatorname{Beta}(5,5)$ compares mode-based parameters with a $\operatorname{Beta}(1,1)$ baseline: four extra successes and four extra failures, eight extra trial units.{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270){{cite:dodge2008}} (p. 40, uniform special case)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The prior density is proportional to $\theta^{\alpha-1}(1-\theta)^{\beta-1}$; a binomial batch contributes $\theta^x(1-\theta)^{n-x}$. Multiplication gives posterior powers $\alpha+x-1$ and $\beta+n-x-1$, hence the stated Beta law. Multiplying by a second batch adds its two exponents, so updating in either order equals pooling the counts.{{cite:diaconis_ylvisaker1979}} (§1, p. 269)

The Beta mean is $a/(a+b)$, giving $(\alpha+x)/(\alpha+\beta+n)=\frac{n}{n+\alpha+\beta}\frac{x}{n}+\frac{\alpha+\beta}{n+\alpha+\beta}\frac{\alpha}{\alpha+\beta}$. For $a,b>1$, differentiating $(a-1)\log\theta+(b-1)\log(1-\theta)$ and setting its derivative to zero gives the mode $(a-1)/(a+b-2)$. Substituting $a=\alpha+x$ and $b=\beta+n-x$ proves the two pseudo-count conventions.{{cite:dodge2008}} (p. 40, Beta density and mean)
:::
:::

## Statistical use — Updating without recounting
Store the current posterior parameters rather than reprocessing all earlier Bernoulli outcomes. For the next batch, add its successes to the first shape and its failures to the second. The posterior mean can then be reported with the prior and new-data weights visible. This is convenient for repeated data arrivals or distributed batches, but it assumes the current posterior summarizes all relevant earlier information and that the new likelihood uses the same $\theta$. If the prior was chosen using the same data and that data are added again as a batch, the evidence is counted twice.{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270, updating and closure)

## Worked example
Start with $\theta\sim\operatorname{Beta}(2,3)$, whose mean is $2/5=0.4$. Three successes in five trials yield $\operatorname{Beta}(5,5)$ with mean $5/10=0.5$. Four successes in another five yield $\operatorname{Beta}(9,6)$ with mean $9/15=0.6$. Pooling the batches gives seven successes and three failures, so the direct update is also $\operatorname{Beta}(2+7,3+3)=\operatorname{Beta}(9,6)$. The posterior mean has moved toward the observed success rate $7/10=0.7$ but remains below it because the prior favored a smaller rate. The final interior posterior mode is $8/13\approx0.6154$, illustrating that a mode-based pseudo-count reading differs from the mean-based one.{{cite:diaconis_ylvisaker1979}} (§1, p. 269, beta-binomial update)

**Your turn.** Start with $\operatorname{Beta}(1,1)$. A first batch has two successes in four trials and a second has three successes in five. Find the posterior after each batch, its final mean and its final interior mode.

::: {.callout-tip collapse="true" title="Answer"}
The first posterior is $\operatorname{Beta}(3,3)$. The second adds three successes and two failures, giving $\operatorname{Beta}(6,5)$. Its mean is $6/11\approx0.5455$ and its mode is $5/9\approx0.5556$. Updating with all nine trials at once gives five successes and four failures, hence the same $\operatorname{Beta}(6,5)$.{{cite:diaconis_ylvisaker1979}} (§1, p. 269)
:::

## Common misconceptions
Pseudo-counts are not literal historical observations: a prior can have fractional parameters and can encode judgment or earlier evidence of a different kind. The mean-based count total $\alpha+\beta$ should not be substituted into the mode formula, whose baseline subtracts one from each parameter. Sequential updating does not make observations independent; conditional independence and a common parameter are model assumptions. Nor does a posterior mean of $0.6$ say the next observed outcome must be a success; it gives a predictive success probability under the model.{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270)

## Assumptions and limits — When counts cannot simply be added
If the success chance changes after a treatment change, pooling before and after trials under one $\theta$ can conceal that change. If tests from one patient share an unmodeled risk factor, treating them as conditionally independent Bernoulli trials exaggerates the effective information. For a non-Beta prior, multiplication by the binomial likelihood still gives a posterior, but two Beta shape parameters may no longer describe it. These failures concern the sampling model or conjugate representation, not Bayes' rule.{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270, conjugate family and its broader alternatives)

## Connections
[Beta–Binomial conjugacy](beta-binomial-conjugacy.qmd) gives the full posterior update; [two pseudo-count conventions](two-pseudo-count-conventions.qmd) distinguishes mean and mode readings. [Sequential coherence](sequential-coherence.qmd) is the order-invariance result, and [prior sensitivity](prior-sensitivity.qmd) asks how the answer changes under different plausible priors.{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270)

## History
Bayes's essay was published after his death in 1763 through Richard Price; Dodge records that publication in its entry on Bayes. The later conjugate-prior framework made repeated updating particularly transparent. Diaconis and Ylvisaker's 1979 paper begins with the Beta-Binomial example and relates its linear posterior mean to a broader class of exponential-family conjugate priors. The pseudo-count reading here is the elementary algebra of that posterior mean, with the chosen summary made explicit.{{cite:dodge2008}} (p. 32, Bayes entry){{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270)
