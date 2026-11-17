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
