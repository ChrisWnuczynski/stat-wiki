## Lead context
They compare how likely an event is to happen with how likely it is not to happen. Odds are useful in binary regression and Bayesian updating because multiplying odds becomes addition after taking logarithms, but a probability and its odds have different numerical scales.{{cite:nelder_wedderburn1972}} (§3.3, p. 379){{cite:kass_raftery1995}} (§3.1, p. 777)

## Motivating example
Suppose an event has probability $0.8$. Its odds are $0.8/0.2=4$, often read “four to one in favour.” If the event instead has probability $0.2$, its odds are $0.2/0.8=1/4$, or one to four. The odds value $4$ corresponds to probability $4/5$; it is a ratio rather than a probability.{{cite:kass_raftery1995}} (§3.1, p. 777)

## Intuition
Probability compares the event with *all* possibilities, including itself; odds compare it with the complementary event. The ratio is one when both events are equally likely. Above one the event is more likely than its complement, and below one it is less likely. This comparison of two mutually exclusive possibilities is why odds work naturally for a yes-or-no response or for two competing hypotheses. The direction must always be stated: odds *for* an event are the reciprocal of odds *against* it.{{cite:kass_raftery1995}} (§3.1, p. 777)

## Definition
For an event $A$ with probability $p=\mathbb P(A)$, the odds *in favour of* $A$ are

$$
O(A)=\frac{\mathbb P(A)}{\mathbb P(A^c)}=\frac{p}{1-p},
$$

where $A^c$ is the complement of $A$ and $\mathbb P(A^c)=1-p$. If $0<p<1$, this is a positive finite number. The inverse conversion is $p=O(A)/\{1+O(A)\}$. At $p=0$, the odds are zero; at $p=1$, they have an infinite limit and the denominator of the literal ratio is zero. A statement such as “odds of four to one” means $O(A)=4$ and hence $p=4/5$, provided the event and its complement are the two alternatives under discussion.{{cite:kass_raftery1995}} (§3.1, p. 777){{cite:nelder_wedderburn1972}} (§3.3, p. 379)

For a binary random response $Y$ coded as one for the event and zero for its complement, write $p=\mathbb P(Y=1\mid\mathbf x)$ at observed covariates $\mathbf x$. The conditional odds are $p/(1-p)$. In a logistic model, the *log* of these odds, rather than the odds themselves, equals a linear predictor. This distinction matters: a coefficient adds to log odds and multiplies odds.{{cite:kass_raftery1995}} (§3.1, p. 777){{cite:nelder_wedderburn1972}} (§3.3, p. 379)

## Properties
The odds function $p/(1-p)$ increases strictly as $p$ increases from zero to one. The odds against $A$ are $(1-p)/p=1/O(A)$ when $0<p<1$. Converting odds back using $p=O/(1+O)$ recovers the starting probability. This makes it possible to update or model odds and still report results on the more familiar probability scale.{{cite:nelder_wedderburn1972}} (§3.3, p. 379){{cite:kass_raftery1995}} (§3.1, pp. 777–778)

For two groups with event probabilities $p_1$ and $p_0$, their [odds ratio](odds-ratio.qmd) is $\{p_1/(1-p_1)\}/\{p_0/(1-p_0)\}$. Their risk ratio is $p_1/p_0$ when $p_0>0$. These are generally different: with probabilities $0.6$ and $0.3$, the odds ratio is $3.5$, while the risk ratio is $2$. Thus an odds ratio of $3.5$ must not be described as a 3.5-fold probability.{{cite:nelder_wedderburn1972}} (§3.3, p. 379){{cite:kass_raftery1995}} (§3.1, pp. 777–778)

For two exhaustive hypotheses $H_1,H_0$ and observed data $D$, [posterior odds](posterior-odds-factorisation.qmd) equal prior odds times the [Bayes factor](marginal-likelihood-and-bayes-factor.qmd):

$$
\frac{\mathbb P(H_1\mid D)}{\mathbb P(H_0\mid D)}
=\frac{\mathbb P(H_1)}{\mathbb P(H_0)}
\frac{\mathbb P(D\mid H_1)}{\mathbb P(D\mid H_0)}.
$$

Here $D$ denotes the observed evidence and the likelihood ratio on the right is the Bayes factor when each hypothesis specifies a single data law, or when its within-hypothesis parameters have been integrated using proper priors. The formula requires the conditioning probabilities to be defined and nonzero where divided. It shows why an evidence factor alone does not determine a posterior probability.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Since $\mathbb P(A^c)=1-p$, the conversion formula follows by solving $O=p/(1-p)$: $O(1-p)=p$, so $p=O/(1+O)$. Differentiating $p/(1-p)$ gives $1/(1-p)^2>0$ for $0<p<1$. Replacing $p$ by $1-p$ gives reciprocal odds. For $p_1=0.6$ and $p_0=0.3$, the two odds are $3/2$ and $3/7$; their ratio is $7/2=3.5$, while $p_1/p_0=2$.{{cite:nelder_wedderburn1972}} (§3.3, p. 379){{cite:kass_raftery1995}} (§3.1, pp. 777–778)

Bayes' rule gives $\mathbb P(H_j\mid D)=\mathbb P(D\mid H_j)\mathbb P(H_j)/\mathbb P(D)$ for $j=0,1$. Dividing the $j=1$ equation by the $j=0$ equation cancels the shared evidence probability and yields the displayed posterior-odds identity. If a hypothesis contains unknown parameters, replace its conditional data probability by the corresponding marginal likelihood before taking the ratio.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

Finally, if a logistic predictor changes by $\beta_1$ while all other terms stay fixed, its odds change from $e^\eta$ to $e^{\eta+\beta_1}=e^\eta e^{\beta_1}$. This gives the odds multiplier for the regression coefficient.{{cite:nelder_wedderburn1972}} (§3.3, p. 379)
:::
:::

## Worked example
Suppose a screening programme has a predicted event probability of $0.30$ in a reference group and $0.60$ in a comparison group. Their odds are $0.30/0.70=3/7$ and $0.60/0.40=3/2$. The comparison-to-reference odds ratio is $(3/2)/(3/7)=7/2=3.5$. The probability ratio is $0.60/0.30=2$, and the probability difference is $0.30$. Give the actual probabilities with the odds ratio: each answers a different question.{{cite:nelder_wedderburn1972}} (§3.3, p. 379){{cite:kass_raftery1995}} (§3.1, p. 777)

**Your turn.** Two exhaustive models have prior probabilities $0.25$ and $0.75$. The data have Bayes factor $6$ in favour of the first. Find its posterior odds and posterior probability.

::: {.callout-tip collapse="true" title="Answer"}
The prior odds for the first model are $0.25/0.75=1/3$. Multiplication by $6$ gives posterior odds $2$ to $1$, hence posterior probability $2/(1+2)=2/3$. The Bayes factor $6$ is the multiplier applied to the prior odds.{{cite:kass_raftery1995}} (§3.1, p. 777)
:::

## Common misconceptions
Odds of $4$ mean probability $4/5$, not probability $4$. “Four to one against” reverses the direction and means probability $1/5$ for the named event. Odds ratios compare *two odds* and need not equal probability ratios or differences. The odds of two different hypotheses are meaningful only after specifying which hypotheses are compared and whether they exhaust the alternatives. Bayes factors multiply prior odds; they are not themselves posterior probabilities. Zero successes in a finite sample give empirical odds zero but do not prove that the population event is impossible.{{cite:nelder_wedderburn1972}} (§3.3, p. 379){{cite:kass_raftery1995}} (§3.1, p. 777)

## Connections
The [logit link](logit-link.qmd) is the logarithm of the odds, mapping a probability to an unrestricted linear-predictor scale. An [odds ratio](odds-ratio.qmd) divides the odds of one group by those of another. [Prior odds](prior-odds.qmd) describe the balance between two hypotheses before observing data, while [posterior odds](posterior-odds-factorisation.qmd) describe it after a Bayes-factor update. These uses share the same probability-to-odds conversion; they differ in which event is being compared with its complement.{{cite:nelder_wedderburn1972}} (§3.3, p. 379){{cite:kass_raftery1995}} (§3.1, p. 777)

## History
In the 1763 essay published after Thomas Bayes's death and communicated by Richard Price, the problem was to infer an unknown chance from observations of whether an event happened. Modern Bayesian model comparison expresses the shift from prior to posterior probabilities as a multiplication of odds.{{cite:bayes1763}} (Price’s letter, pp. 370–371){{cite:kass_raftery1995}} (§3.1, p. 777)

Joseph Berkson's 1944 bioassay paper used a logistic curve to describe the fraction of subjects showing an all-or-none response at different doses. It called the logarithm of an outcome-to-complement ratio a *logit*, giving a linear scale for those response probabilities.{{cite:berkson1944}} (pp. 357–359)

David Cox's 1958 work treated sequences of binary outcomes whose probabilities depended on explanatory variables. In that regression setting, a predictor change became an additive log-odds change and a multiplicative odds change. This regression interpretation distinguishes an odds multiplier from a change in probability.{{cite:cox1958_logistic}} (Summary; reproduced excerpt, p. 216){{cite:nelder_wedderburn1972}} (§3.3, p. 379)
