## Lead context
They compare how likely an event is to happen with how likely it is not to happen. Odds are useful in binary regression and Bayesian updating because multiplying odds becomes addition after taking logarithms, but a probability and its odds have different numerical scales.{{cite:cox1958_logistic,kass_raftery1995}}

## Motivating example
If 80 of 100 equally likely future cases are expected to have an outcome, its probability is $0.8$ and its odds are $0.8/0.2=4$, often read “four to one in favour.” If instead 20 cases are expected to have it, the odds are $0.2/0.8=1/4$, or one to four. Neither odds value is itself a probability: four is a valid odds value but cannot be a probability.{{cite:agresti2002}}

## Intuition
Probability compares the event with *all* possibilities, including itself; odds compare it with the complementary event. The ratio is one when both events are equally likely. Above one the event is more likely than its complement, and below one it is less likely. This comparison of two mutually exclusive possibilities is why odds work naturally for a yes-or-no response or for two competing hypotheses. The direction must always be stated: odds *for* an event are the reciprocal of odds *against* it.{{cite:agresti2002,kass_raftery1995}}

## Definition
For an event $A$ with probability $p=\mathbb P(A)$, the odds *in favour of* $A$ are

$$
O(A)=\frac{\mathbb P(A)}{\mathbb P(A^c)}=\frac{p}{1-p},
$$

where $A^c$ is the complement of $A$ and $\mathbb P(A^c)=1-p$. If $0<p<1$, this is a positive finite number. The inverse conversion is $p=O(A)/\{1+O(A)\}$. At $p=0$, the odds are zero; at $p=1$, they have an infinite limit and the denominator of the literal ratio is zero. A statement such as “odds of four to one” means $O(A)=4$ and hence $p=4/5$, provided the event and its complement are the two alternatives under discussion.{{cite:agresti2002}}

For a binary random response $Y$ coded as one for the event and zero for its complement, write $p=\mathbb P(Y=1\mid\mathbf x)$ at observed covariates $\mathbf x$. The conditional odds are $p/(1-p)$. In a logistic model, the *log* of these odds, rather than the odds themselves, equals a linear predictor. This distinction matters: a coefficient adds to log odds and multiplies odds.{{cite:cox1958_logistic,nelder_wedderburn1972}}

## Properties
The odds function $p/(1-p)$ increases strictly as $p$ increases from zero to one. The odds against $A$ are $(1-p)/p=1/O(A)$ when $0<p<1$. If a probability is converted to odds and back using $p=O/(1+O)$, the original probability is recovered. This makes it possible to update or model odds and still report results on the more familiar probability scale.{{cite:agresti2002}}

For two groups with event probabilities $p_1$ and $p_0$, their [odds ratio](odds-ratio.qmd) is $\{p_1/(1-p_1)\}/\{p_0/(1-p_0)\}$. Their risk ratio is $p_1/p_0$ when $p_0>0$. These are generally different: with probabilities $0.6$ and $0.3$, the odds ratio is $3.5$, while the risk ratio is $2$. Thus an odds ratio of $3.5$ must not be described as a 3.5-fold probability.{{cite:agresti2002}}

For two exhaustive hypotheses $H_1,H_0$ and observed data $D$, [posterior odds](posterior-odds-factorisation.qmd) equal prior odds times the [Bayes factor](marginal-likelihood-and-bayes-factor.qmd):

$$
\frac{\mathbb P(H_1\mid D)}{\mathbb P(H_0\mid D)}
=\frac{\mathbb P(H_1)}{\mathbb P(H_0)}
\frac{\mathbb P(D\mid H_1)}{\mathbb P(D\mid H_0)}.
$$

Here $D$ denotes the observed evidence and the likelihood ratio on the right is the Bayes factor when each hypothesis specifies a single data law, or when its within-hypothesis parameters have been integrated using proper priors. The formula requires the conditioning probabilities to be defined and nonzero where divided. It shows why an evidence factor alone does not determine a posterior probability.{{cite:bayes1763,kass_raftery1995}}

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Since $\mathbb P(A^c)=1-p$, the conversion formula follows by solving $O=p/(1-p)$: $O(1-p)=p$, so $p=O/(1+O)$. Differentiating $p/(1-p)$ gives $1/(1-p)^2>0$ for $0<p<1$. Replacing $p$ by $1-p$ gives reciprocal odds. For $p_1=0.6$ and $p_0=0.3$, the two odds are $3/2$ and $3/7$; their ratio is $7/2=3.5$, while $p_1/p_0=2$.{{cite:agresti2002}}

Bayes' rule gives $\mathbb P(H_j\mid D)=\mathbb P(D\mid H_j)\mathbb P(H_j)/\mathbb P(D)$ for $j=0,1$. Dividing the $j=1$ equation by the $j=0$ equation cancels the shared evidence probability and yields the displayed posterior-odds identity. If a hypothesis contains unknown parameters, replace its conditional data probability by the corresponding marginal likelihood before taking the ratio.{{cite:bayes1763,kass_raftery1995}}

Finally, if a logistic predictor changes by $\beta_1$ while all other terms stay fixed, its odds change from $e^\eta$ to $e^{\eta+\beta_1}=e^\eta e^{\beta_1}$. This proves the multiplier asserted in the original definition's regression example.{{cite:cox1958_logistic}}
:::
:::

## Statistical use
In a binary-outcome report, give the event definition and response coding before quoting odds. Convert predicted odds back to probabilities for decisions that depend on absolute risk. When reporting an odds ratio, state which group is in the numerator and which covariates are held fixed. A logistic-regression coefficient is a conditional log-odds comparison under its fitted model; a before-and-after probability difference requires a specified starting predictor.{{cite:cox1958_logistic,agresti2002}}

In Bayesian model comparison, first calculate the prior odds between the stated models, then multiply by their Bayes factor, and finally convert the resulting posterior odds to a probability if the two models exhaust the alternatives. The evidence factor records how the data changed the odds; the posterior odds also reflect the starting model probabilities.{{cite:kass_raftery1995}}

## Worked example
Suppose a screening programme has a predicted event probability of $0.30$ in a reference group and $0.60$ in a comparison group. Their odds are $0.30/0.70=3/7$ and $0.60/0.40=3/2$. The comparison-to-reference odds ratio is $(3/2)/(3/7)=7/2=3.5$. The probability ratio is $0.60/0.30=2$, and the probability difference is $0.30$. Give the actual probabilities with the odds ratio: each answers a different question.{{cite:agresti2002}}

**Your turn.** Two exhaustive models have prior probabilities $0.25$ and $0.75$. The data have Bayes factor $6$ in favour of the first. Find its posterior odds and posterior probability.

::: {.callout-tip collapse="true" title="Answer"}
The prior odds for the first model are $0.25/0.75=1/3$. Multiplication by $6$ gives posterior odds $2$ to $1$, hence posterior probability $2/(1+2)=2/3$. The Bayes factor $6$ is neither the posterior odds nor the posterior probability.{{cite:kass_raftery1995}}
:::

## Common misconceptions
Odds of $4$ mean probability $4/5$, not probability $4$. “Four to one against” reverses the direction and means probability $1/5$ for the named event. Odds ratios compare *two odds* and need not equal probability ratios or differences. The odds of two different hypotheses are meaningful only after specifying which hypotheses are compared and whether they exhaust the alternatives. Bayes factors multiply prior odds; they are not themselves posterior probabilities.{{cite:agresti2002,kass_raftery1995}}

## Assumptions and limits
The odds conversion is an algebraic identity and needs no sample or regression model. Estimated odds inherit uncertainty from the estimated probability. A finite sample with zero observed successes has empirical odds zero, but that observation alone does not prove the population event probability is zero. In a logistic model, a common coefficient-based odds multiplier presumes the stated additive predictor and fixed other covariates; an interaction can make the multiplier vary by setting.{{cite:agresti2002,cox1958_logistic}}

## Connections
The [logit link](logit-link.qmd) is the logarithm of the odds, mapping a probability to an unrestricted linear-predictor scale. An [odds ratio](odds-ratio.qmd) divides the odds of one group by those of another. [Prior odds](prior-odds.qmd) describe the balance between two hypotheses before observing data, while [posterior odds](posterior-odds-factorisation.qmd) describe it after a Bayes-factor update. These uses share the same probability-to-odds conversion; they differ in which event is being compared with its complement.{{cite:cox1958_logistic,kass_raftery1995}}

## Check yourself
Try [logit, probit and odds](../questions/c-20.qmd) for the basic definitions. [Posterior odds](../questions/ex-sl-06-1.qmd) asks for a numerical Bayes-factor update. [Odds ratios](../questions/ex-sl-10-2.qmd) asks you to compare an adjusted odds multiplier with two fitted probabilities.

## History
In the 1763 essay published after Thomas Bayes's death and communicated by Richard Price, the problem was to infer a chance from observed times an event happened and failed. The essay concerned event probabilities and their updating, the setting in which modern prior and posterior odds can be written as a ratio. This is historical context for the odds form of Bayesian updating; the essay is not claimed as the first definition of odds.{{cite:bayes1763}}

Joseph Berkson's 1944 bioassay paper used a logistic curve to describe the fraction of subjects showing an all-or-none response at different doses. It called the logarithm of an outcome-to-complement ratio a *logit*, giving a linear scale for those response probabilities.{{cite:berkson1944}}

David Cox's 1958 work treated sequences of binary outcomes whose probabilities depended on explanatory variables. In that regression setting, a predictor change became an additive log-odds change and a multiplicative odds change. Modern categorical-data analysis retains this coefficient interpretation while distinguishing odds ratios from changes in probability.{{cite:cox1958_logistic,agresti2002}}
