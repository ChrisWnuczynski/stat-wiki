## Motivating example
Two analysts can agree on a likelihood yet differ about plausible parameter values before seeing the data. A sensitivity analysis asks whether those differences matter for a stated conclusion. Reporting only one posterior mean hides this question. A useful comparison keeps the observations and likelihood fixed, changes a defensible part of the prior specification, and recomputes the decision-relevant posterior summaries. With sparse observations or weak likelihood information, the choice can matter substantially.{{cite:downey2020_thinkbayes2}} (Chapter 5, “Sensitivity to the Prior”)

## Definition — Vary a modelling assumption, then compare a target
Let $\{\pi_\eta(\theta):\eta\in H\}$ be a family of plausible priors. A posterior sensitivity analysis compares the distributions proportional to $L(\theta;D)\pi_\eta(\theta)$, or a specified functional such as $E_\eta(\theta\mid D)$, a tail probability or a predictive decision. Sensitivity is a property of the prior family, the likelihood, the observed information and the target together. Agreement on a posterior mean need not imply agreement on extreme tails.{{cite:bernardo2005_reference}} (§1, prior information, model assumptions and inferential targets)

For binomial data with $x$ successes in $n>0$ independent trials and a beta prior, the posterior is $\operatorname{Beta}(\alpha+x,\beta+n-x)$. Put $s=\alpha+\beta$ and $m_0=\alpha/s$. Its mean can be written
$$m_n=\frac{s}{s+n}m_0+\frac{n}{s+n}\frac{x}{n}.$$
This expresses prior influence on that particular summary through its location $m_0$ and concentration $s$. The concentration is an algebraic weight; interpretations as a literal number of imagined observations depend on the chosen convention.{{cite:downey2020_thinkbayes2}} (Chapter 18, “Binomial Likelihood”)

## Properties — Different ways a prior can matter
Holding $s$ fixed gives $\partial m_n/\partial m_0=s/(s+n)$. Thus increasing $n$ reduces the influence of a change in the prior mean on this posterior mean. Holding $m_0$ fixed instead gives $\partial m_n/\partial s=n(m_0-x/n)/(s+n)^2$. A more concentrated prior pulls towards its own centre, with a direction determined by whether that centre lies above or below the observed fraction. These statements follow by differentiating the displayed weighted average, so they do not require an asymptotic approximation.

Sensitivity can also arise from the tails or the prior's support. If a prior assigns zero mass to a region, finite likelihood values cannot create posterior mass there. A likelihood that barely distinguishes a range of parameter values cannot by itself decide how probability should be allocated across that range. Default-prior constructions therefore still depend on the sampling model and on the parameter of interest.{{cite:bernardo2005_reference}} (§1 and §3, reference priors conditional on a model and parameter ordering)

## Worked example — Compare means and a tail event
For $x=3$ in $n=10$, the priors $\operatorname{Beta}(5,5)$, $\operatorname{Beta}(1,1)$ and $\operatorname{Beta}(0.6,0.6)$ produce posterior means $0.4$, $0.333333$ and $0.321429$. Their posterior probabilities of $\theta<1/2$ are respectively $0.820358$, $0.886719$ and $0.895662$. The likelihood is identical, but the summaries show different degrees of evidence for a probability below one half.

With $x=30$ in $n=100$, the corresponding posterior means are $0.318182$, $0.303922$ and $0.302372$. The range between the largest and smallest mean falls from $0.078571$ to $0.015810$. This particular comparison shows decreasing sensitivity as the binomial information increases; it is not a universal guarantee that every posterior feature becomes insensitive at a given sample size.{{cite:downey2020_thinkbayes2}} (Chapter 5, “Sensitivity to the Prior”, comparison as information increases)

**Your turn.** With concentration $s=10$ and sample size $n=10$, changing the prior mean by 0.2 changes the posterior mean by how much?

::: {.callout-tip collapse="true" title="Answer"}
The weight on the prior mean is 10/(10+10)=1/2, so the posterior mean changes by 0.1.
:::

## Statistical use — Make the comparison relevant to the decision
A useful analysis includes priors that encode plausible alternative assumptions, rather than changing convenient hyperparameters without interpretation. If the final decision uses a tail probability, compare that probability directly. If it uses a predictive interval, compare the predictive distributions. Graphs can show shape changes that a table of means misses, including boundary mass and heavy tails.{{cite:downey2020_thinkbayes2}} (Chapter 5, “Sensitivity to the Prior” and “Power Law Prior”)

When conclusions change materially, the response can include collecting more informative data, explaining which prior assumptions drive the change, or stating a range of decisions across the plausible specifications. A claim of robustness should identify the class of changes actually investigated. Changing only a prior mean says nothing by itself about robustness to dependence, a different likelihood or a different measurement-error model.{{cite:bernardo2005_reference}} (§1, modelling assumptions and the limits of default prior statements)
