## Motivating example
With a beta prior, adding observed successes and failures to the two shapes gives another beta distribution. This makes it tempting to translate the prior into a fixed number of earlier trials. That translation depends on the summary being matched. The mean and an interior mode use different expressions, even though they come from the same probability density. Confusing them changes both the claimed prior strength and the resulting estimate.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”)

## Definition — Shapes for a mean, exponents for a mode
For positive $a,b$, the beta mean is $a/(a+b)$. When $a,b>1$, the unique interior mode is $(a-1)/(a+b-2)$. The density's powers are $a-1,b-1$, whereas its moments use $a,b$. Thus the same beta prior has a mean-based concentration $a+b$ and a mode-based concentration $a+b-2$. The second expression has a useful positive-count interpretation only when its component exponents are nonnegative.{{cite:dodge2008}} (p. 40, beta density and moments)

An interior maximum can be found directly from the density. Differentiating its log gives $(a-1)/p-(b-1)/(1-p)=0$, whose solution is $(a-1)/(a+b-2)$. Its second derivative is negative when both shapes exceed one, establishing that the stationary point is the unique maximum.

## Properties — A weighted average needs its denominator
After $x$ successes out of $n>0$ trials, the posterior mean can be written
$$\frac{x+a}{n+a+b}=\frac{n}{n+a+b}\frac{x}{n}+\frac{a+b}{n+a+b}\frac{a}{a+b}.$$
The weights sum to one. On this scale, the prior contributes $a$ success units and $b$ failure units. This statement describes shrinkage towards a prior mean, rather than claiming that those trials actually occurred. The posterior shapes follow by adding likelihood exponents to prior exponents.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”)

If the posterior shapes both exceed one, its mode is $(x+a-1)/(n+a+b-2)$. When $a,b>1$, the same decomposition uses weights $n$ and $a+b-2$ and prior centre $(a-1)/(a+b-2)$. A uniform $\operatorname{Beta}(1,1)$ prior has two units of concentration on the mean scale, but zero extra exponents on the mode scale. Its interior posterior mode equals the sample proportion when both outcomes have occurred. These are compatible properties of one uniform density.{{cite:dodge2008}} (p. 40)

## Interpretation — A convention is tied to an estimator
For a $\operatorname{Beta}(5,5)$ prior, the mean calculation uses ten prior units, split equally. An interior-mode calculation uses eight, again split equally. Their centres both equal one half because of symmetry, but their weights on the sample differ. For unequal shapes the centres can differ too. A phrase such as “equivalent to eight observations” therefore needs the estimator and the reference convention attached to it. The conjugate algebra supplies the weights; it does not identify a unique historical sample behind a prior.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”)

## Worked example — The same posterior, two estimates
Take $a=b=5$ and observe eight successes in ten trials. The posterior is $\operatorname{Beta}(13,7)$. Its mean is $13/20=0.65$, while its mode is $12/18=2/3\approx0.666667$. The mean is the equally weighted average of $0.8$ and $0.5$. For the mode the weights are ten and eight, giving $(10\times0.8+8\times0.5)/18=2/3$.

For a $\operatorname{Beta}(1,1)$ prior and those same data, the posterior mean is $9/12=0.75$ and the mode is $8/10=0.8$. Neither summary changes the posterior density. Choosing a point estimate requires choosing the quantity to report or the loss function it is intended to minimise.

**Your turn.** Under a $\operatorname{Beta}(2,4)$ prior, observe three successes in six trials. Find the posterior mean and mode.

::: {.callout-tip collapse="true" title="Answer"}
The posterior is $\operatorname{Beta}(5,7)$. Its mean is $5/12$ and its interior mode is $4/10=0.4$.
:::

## Assumptions and limits — Endpoint shapes break the interior formula
The density is integrable whenever its shapes are positive. That condition is weaker than the condition for an interior mode. A posterior shape at most one can put the maximum on a boundary or give an unbounded boundary density. Substituting such shapes into the interior-mode formula can give an irrelevant value outside the unit interval. Check the shape conditions before interpreting exponent-based pseudo-counts.{{cite:dodge2008}} (p. 40)

## Statistical use — Uniform priors sit at different places on the two scales
A $\operatorname{Beta}(1,1)$ density is flat on $(0,1)$. Its mean is $1/2$ and its mean-scale concentration is $1+1=2$. The interior-mode formula would divide by $a+b-2=0$ and is not used: the exponents $a-1$ and $b-1$ are zero, so there is no unique interior mode. The mode-scale prior sample size is $0$. After eight successes in ten trials the posterior is $\operatorname{Beta}(9,3)$, the mean is $9/12=0.75$ and an interior mode exists at $8/10=0.8$ because both posterior shapes exceed one. The mode matches the sample proportion. The mean is pulled toward $1/2$ by the two mean-scale prior units. Both statements describe the same posterior density.{{cite:dodge2008}} (p. 40){{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”)

A $\operatorname{Beta}(5,5)$ prior has mean-scale size $10$ and mode-scale size $8$, and both centres equal $1/2$ by symmetry. A $\operatorname{Beta}(4,2)$ prior has mean $4/6=2/3$ and interior mode $(4-1)/(6-2)=3/4$. One success in four trials produces $\operatorname{Beta}(5,5)$. The posterior mean is $5/10=0.5$, and the interior mode is $(5-1)/(10-2)=0.5$. The mean-scale calculation puts weight $4/10$ on the sample proportion $1/4$ and weight $6/10$ on the prior mean $2/3$: $0.4\times0.25+0.6\times2/3=0.5$. The mode-scale calculation uses prior size $4$ and prior mode $3/4$, and $(4\times1/4+4\times3/4)/8=0.5$ as well. Equal posterior shapes force the two summaries together even though the prior mean and prior mode differed.{{cite:dodge2008}} (p. 40, beta density and moments)

### Interpretation — The weight is an algebraic share of a point estimate
The posterior-mean identity
$$\frac{x+a}{n+a+b}=\frac{n}{n+a+b}\frac{x}{n}+\frac{a+b}{n+a+b}\frac{a}{a+b}$$
assigns the data weight $n/(n+a+b)$. For $a=b=5$ and eight successes in ten trials, the weight on $0.8$ is $10/20=1/2$ and the mean is $0.65$. The mode identity, available because every shape exceeds one, puts weight $10/18$ on the sample proportion and weight $8/18$ on the prior mode $1/2$, returning $2/3$. Saying that the prior is “worth eight observations” is a statement about the mode. Saying that it is “worth ten” is a statement about the mean. The density is the same object either way.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”)

## Connections
These two counts are the concentration $s=a+b$ that appears in a [prior sensitivity](prior-sensitivity.qmd) calculation for the posterior mean, and the count $a+b-2$ that would appear if the functional were the interior mode. A sensitivity table should say which one was varied. The beta law is also the free coordinate of a two-category Dirichlet prior, so the same mean-scale addition of counts is the Dirichlet update when the second category is the complement.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood” and “The Dirichlet Distribution”)
