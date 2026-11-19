## Lead context
A posterior hypothesis probability is the probability, after the data are seen, that the parameter lies in the region the hypothesis names.

## Motivating example
A coin is tossed 10 times and lands heads 7 times. Before the tosses, the unknown heads probability $p$ is given a uniform prior, which is a $\mathrm{Beta}(1,1)$ distribution. After the data the posterior is $\mathrm{Beta}(8,4)$. The hypothesis $H_0:p\le1/2$ then has posterior probability $0.1133$, and $H_1:p>1/2$ has probability $0.8867$. Those two numbers add to 1. They are probabilities for regions of $p$, computed from one posterior, not long-run error rates of a rejection rule.{{cite:dodge2008}} (pp. 32–33, hypothesis testing from the posterior)

## Intuition
A hypothesis here is a set of parameter values. The prior spreads probability over the parameter. The likelihood reweights that spread by how well each value fits the sample. The posterior hypothesis probability is the posterior mass of the set. If the set is half the line and the posterior is concentrated elsewhere, the hypothesis can have small probability even though it is a large set. If the posterior is flat, a large set keeps a large probability. The number moves when the prior moves, because it is a probability in a model that includes the prior, not a property of the sample alone.{{cite:dodge2008}} (p. 33, the posterior carries the information used for a hypothesis about the parameter)

## Definition
Partition the parameter space into $\Omega_0$ and $\Omega_1$, and write $H_0$ for the statement that the parameter lies in $\Omega_0$. The posterior hypothesis probability is
$$
\Pr(H_0\mid x)=\int_{\Omega_0}p(\theta\mid x)\,d\theta,
$$
when the posterior has density $p(\theta\mid x)$. A discrete parameter replaces the integral by a sum. If the two regions exhaust the support and do not overlap, the two probabilities sum to 1. A point null inside a continuous parameter has posterior probability 0, so a test of $\theta=\theta_0$ against $\theta\neq\theta_0$ needs a different summary, such as a region around $\theta_0$ or a model comparison with a positive prior mass on the point.{{cite:dodge2008}} (p. 33, calculating the posterior and then testing a value)

## Interpretation — Probability, odds, and a decision
The odds of $H_0$ against $H_1$ are $\Pr(H_0\mid x)/\Pr(H_1\mid x)$. In the coin example that ratio is $0.1133/0.8867=0.1278$. An action is a further choice. If calling $H_0$ true when $H_1$ is true costs $L_{01}$, and the reverse mistake costs $L_{10}$, the posterior expected losses are $L_{01}\Pr(H_1\mid x)$ and $L_{10}\Pr(H_0\mid x)$. With equal costs the smaller expected loss is the hypothesis with the larger posterior probability, so the coin data pick $H_1$. With unequal costs the threshold moves. A posterior probability of 0.8867 is not by itself an instruction to act.{{cite:dodge2008}} (p. 33, summaries computed from the posterior)

## Properties — Conjugacy and a continuous boundary
For a binomial likelihood and a $\mathrm{Beta}(a,b)$ prior, $s$ successes in $n$ trials give a $\mathrm{Beta}(a+s,\ b+n-s)$ posterior. The uniform prior is $a=b=1$, so 7 successes and 3 failures give $\mathrm{Beta}(8,4)$. The mean is $8/12=0.6667$. The probability $\Pr(p\le1/2)$ is the beta distribution function at $1/2$, equal to $0.11328125$, which rounds to $0.1133$.

A continuous posterior gives the boundary itself probability 0. Putting $p=1/2$ into $H_0$ or into $H_1$ does not change $\Pr(H_0\mid x)$. That is a fact about the continuous distribution of $p$, not about the coin tosses, which are discrete. An equal-tailed 95% interval for the same posterior runs from $0.3903$ to $0.8907$ and contains $1/2$, even though only $0.1133$ of the posterior mass is at or below $1/2$. The interval spends 2.5% in each tail. A hypothesis probability spends its mass on a fixed region. Containing $1/2$ and putting most mass above $1/2$ answer different questions.{{cite:dodge2008}} (p. 33, mean and hypothesis summaries from one posterior)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The $\mathrm{Beta}(a,b)$ density is proportional to $p^{a-1}(1-p)^{b-1}$ on $(0,1)$. An independent binomial likelihood is proportional to $p^{s}(1-p)^{n-s}$. The product is proportional to $p^{a+s-1}(1-p)^{b+n-s-1}$, which is the $\mathrm{Beta}(a+s,\,b+n-s)$ kernel. The normalising constant of that beta density integrates to 1, so the posterior probabilities of $p\le1/2$ and $p>1/2$ sum to 1.

The mean of $\mathrm{Beta}(a',b')$ is $a'/(a'+b')$. Here $a'=8$, $b'=4$, and the mean is $8/12$. The distribution function at $1/2$ for integer parameters can be written with binomial probabilities,
$$
\Pr(p\le1/2)=\sum_{j=8}^{11}\binom{11}{j}(1/2)^{11}=29/256=0.11328125,
$$
because a $\mathrm{Beta}(8,4)$ probability below $1/2$ matches the upper tail of a $\mathrm{Bin}(11,1/2)$ count. The equal-tail interval is the pair of beta quantiles at $0.025$ and $0.975$. Those quantiles solve a tail-probability problem. They are not the set $\{p:\Pr(p\le1/2\mid x)\le0.05\}$.{{cite:dodge2008}} (p. 33, Bayes' theorem produces the posterior from which the probability is calculated)
:::
:::

## Statistical use — Reporting the probability and the action separately
Report the posterior probability of each region, the prior that produced it, and, if a decision is required, the losses. A probability above $1/2$ is not a universal decision threshold: if a false claim that $p>1/2$ is costly, the loss ratio can demand a probability well above $1/2$ before that claim is acted on. Model comparison is the same arithmetic on a discrete set of models. The posterior odds equal the prior odds times the Bayes factor, the ratio of marginal likelihoods. A hypothesis probability inside one model, such as $\Pr(p\le1/2\mid x)$ for this coin, is not a Bayes factor. It does not compare two sampling models. It splits one posterior.{{cite:dodge2008}} (p. 33, hypothesis testing on the parameter after the posterior is obtained)

## Worked example
Prior $\mathrm{Beta}(1,1)$, data 7 heads in 10 tosses, posterior $\mathrm{Beta}(8,4)$. Then
$$
\Pr(p\le1/2\mid x)=0.1133,\qquad \Pr(p>1/2\mid x)=0.8867,
$$
and the odds of the first against the second are $0.1278$. The posterior mean is $0.6667$. The equal-tailed 95% interval is $(0.3903,\ 0.8907)$. It contains $1/2$. The hypothesis probability says that only about 11% of the posterior is on $p\le1/2$. Both statements are right, and they are not substitutes. Equal losses pick $p>1/2$, because $0.8867>0.1133$. Now let the cost of declaring $p>1/2$ when in fact $p\le1/2$ be 10, and the cost of the reverse mistake be 1. The expected loss of declaring $p>1/2$ is $10\times0.1133=1.133$. The expected loss of declaring $p\le1/2$ is $1\times0.8867=0.8867$. The second is smaller, so the tenfold cost reverses the action. The probability $0.8867$ was not large enough to pay for that cost.{{cite:dodge2008}} (p. 33, decisions use the posterior)

**Your turn.** The same uniform prior meets 3 heads in 10 tosses. Find the posterior, its mean, and $\Pr(p\le1/2\mid x)$.

::: {.callout-tip collapse="true" title="Answer"}
The posterior is $\mathrm{Beta}(4,8)$, with mean $4/12=0.3333$. By symmetry with the 7-heads case, $\Pr(p\le1/2\mid x)=1-0.1133=0.8867$. Most of the posterior now lies at or below one half. The likelihood has swapped the two beta parameters, and the hypothesis probability swaps with them.
:::

## Common misconceptions
A posterior hypothesis probability is not a $p$-value. A $p$-value is the probability of a sample statistic at least as extreme as the one observed, computed while treating the null as true. The coin's posterior probability 0.1133 is the probability of a region of $p$ after the sample. A small $p$-value does not supply that number. An equal-tailed interval that contains the boundary is not a statement that the hypothesis on one side has posterior probability near one half. And the probability depends on the prior. A $\mathrm{Beta}(10,10)$ prior, much more concentrated at one half, would not move to $\mathrm{Beta}(8,4)$ after seven heads, and $\Pr(p\le1/2)$ would be larger than 0.1133.

## Assumptions and limits — When the integral is not the scientific hypothesis
The integral is right for the model that was written down. If the tosses are not independent, or the heads probability changes through the ten tosses, the beta update is the posterior of a different experiment from the one performed. A point hypothesis $\theta=\theta_0$ inside a continuous parameter still has posterior probability 0 under a continuous prior, however close the data sit to $\theta_0$. The calculation is then silent, because the hypothesis was given no prior mass. Putting a lump of prior probability on the point, and a density on the alternative, turns the comparison into a Bayes factor. The region probability and that factor are different objects, and a large region probability does not imply a large Bayes factor.

A further limit is the loss. The tenfold-cost calculation picks $H_0$ even though $\Pr(H_1\mid x)=0.8867$. Quoting the probability without the loss reports the evidence the model assigned. It does not report a decision.

## Connections
[Bayes' rule](bayes-rule.qmd) is the reweighting that produces the posterior. A [Bayes factor](marginal-likelihood-and-bayes-factor.qmd) compares marginal likelihoods of two models, whereas a hypothesis probability splits one posterior. A [credible interval](bayesian-credible-interval.qmd) is a region with a stated posterior probability, not a region hypothesis. The [significance level](significance-level.qmd) is a long-run false-rejection probability and is not $\Pr(H_0\mid x)$.{{cite:dodge2008}} (pp. 32–33, posterior summaries contrasted with a frequency interpretation of probability)

## History
Bayesian statistics separates a probability used as a degree of uncertainty from a probability used as a long-run frequency. Once a posterior distribution for the parameter has been obtained from Bayes' theorem, hypothesis testing on that parameter is one summary the posterior supports, together with a mean and an interval. Thomas Bayes's essay, published by Richard Price in 1763, is the source of the doctrine of chances on which that calculation rests. The coin arithmetic above is the beta-binomial case of the same update.{{cite:dodge2008}} (pp. 32–33, Bayes's 1763 essay and Bayesian hypothesis summaries)
