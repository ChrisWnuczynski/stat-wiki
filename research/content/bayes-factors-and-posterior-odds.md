## Lead context
Posterior odds multiply two distinct choices: prior odds between models and a likelihood ratio averaged over each model's parameter prior. A Bayes factor omits prior model odds but still depends on within-model priors.{{cite:downey2020_thinkbayes2}} (Ch. 10, “Evidence” and “Bayesian Hypothesis Testing”)

## Motivating example
Three successes and one failure are more likely at a fitted success probability $3/4$ than at $1/2$. Yet a model allowing every success probability must average across its prior, including values that predict these observations poorly. Maximised and marginal likelihoods can therefore favour different comparisons.{{cite:downey2020_thinkbayes2}} (Ch. 10, “Evidence”)

## Properties — Integrate within each model before comparing
If $m_j(x)=\int p(x\mid\theta_j,M_j)\pi_j(\theta_j)\,d\theta_j$ and $\pi_j=P(M_j)>0$, then Bayes' rule gives $P(M_j\mid x)=\pi_jm_j(x)/\sum_k\pi_km_k(x)$. Dividing two such equations cancels the common normaliser, yielding posterior odds $=(m_1/m_0)(\pi_1/\pi_0)$. The model label is discrete even when observations and model parameters are continuous. The within-model integral uses a normalised parameter prior.{{cite:downey2020_thinkbayes2}} (Ch. 6, “Bayes's Rule”; Ch. 10, “Evidence”)

A posterior parameter probability such as $P(p>1/2\mid x)$ belongs to a single continuous model. A point model $p=1/2$ needs a separate prior point mass if it is to receive positive posterior model probability. These constructions can be combined, but their normalising constants must follow the stated model space.{{cite:downey2020_thinkbayes2}} (Ch. 10, fair and biased coin models)

## Worked example
For a particular ordered sequence with three successes and one failure, $M_0$ fixes $p=1/2$ and gives $m_0=1/16$. Under $M_1$, put a uniform prior on $0<p<1$. Then
$$
m_1=\int_0^1p^3(1-p)\,dp=\frac14-\frac15=\frac1{20},
\qquad \mathrm{BF}_{10}=\frac{1/20}{1/16}=\frac45.
$$
The data slightly favour the fixed fair model even though $M_1$ contains the maximum-likelihood value. If prior probability of $M_1$ is $1/4$, its prior odds are $1/3$, posterior odds are $4/15$, and posterior probability is $4/19=0.21053$. If the observation is the unordered success count, the binomial coefficient $\binom43=4$ multiplies both marginal likelihoods and cancels from the factor.{{cite:downey2020_thinkbayes2}} (Ch. 10, binomial likelihood and averaging over biased models)

**Your turn.** Keep the Bayes factor $4/5$ but give the two models equal prior probability. Find the posterior probability of $M_1$.

::: {.callout-tip collapse="true" title="Answer"}
Its posterior odds are $4/5$, giving posterior probability $(4/5)/(1+4/5)=4/9$.
:::

## Assumptions and limits
An improper prior is specified only up to an arbitrary multiplicative constant. That constant cancels from a within-model parameter posterior if the normalising integral is finite, but it multiplies the marginal likelihood and generally does not cancel between different models. Posterior propriety alone therefore does not define a Bayes factor. Even formal reference-prior use requires care about proper approximations and the target of inference.{{cite:bernardo2005_reference}} (§2.3, def. 3; §3.1, def. 6)

## Intuition
A Bayes factor compares how well two models predicted the data, after each model's parameters have been averaged against that model's prior. It is not a comparison of the highest points on the two likelihoods. A model that can set its success probability to $3/4$ will beat a model stuck at $1/2$ if only the peaks are compared. Once the flexible model is forced to pay for the prior probability it placed on poor values of the success probability, the comparison can reverse. Posterior odds then multiply that evidence by the prior odds of the model labels. The Bayes factor itself does not contain those model-label probabilities.{{cite:downey2020_thinkbayes2}} (Ch. 10, “Evidence” and “Bayesian Hypothesis Testing”)

## Definition
The marginal likelihood of model $M_j$ is the integral of the sampling density against the parameter prior $\pi_j$. With prior model probabilities $\pi_j=P(M_j)>0$, the posterior model probabilities are proportional to $\pi_j m_j(x)$. The ratio of two posterior probabilities is
$$
\frac{P(M_1\mid x)}{P(M_0\mid x)}=\frac{m_1(x)}{m_0(x)}\times\frac{P(M_1)}{P(M_0)}.
$$
The first factor on the right is the Bayes factor. The second is the prior odds. For one particular sequence of three successes and one failure, a point model at $p=1/2$ has marginal likelihood $1/16$. A uniform prior on $(0,1)$ has marginal likelihood $\int_0^1 p^3(1-p)\,dp=1/20$. The Bayes factor in favor of the uniform model is $4/5$.{{cite:downey2020_thinkbayes2}} (Ch. 6, “Bayes's Rule”; Ch. 10, “Evidence”)

## Interpretation
Prior odds of $1/3$, from $P(M_1)=1/4$, become posterior odds $(4/5)(1/3)=4/15$. The posterior probability of $M_1$ is $(4/15)/(1+4/15)=4/19\approx 0.21053$. Equal prior probabilities leave the posterior odds equal to $4/5$, so the posterior probability is $4/9$. Recording the data as an unordered count multiplies both marginal likelihoods by $\binom{4}{3}=4$ and cancels in the ratio. A posterior probability such as $P(p>1/2\mid x)$ inside the uniform model is a different object: it conditions on $M_1$ and does not allocate probability to the point model $M_0$. Giving $M_0$ positive posterior probability requires a prior point mass on that model.{{cite:downey2020_thinkbayes2}} (Ch. 10, binomial likelihood and averaging over biased models)

## Common misconceptions
The model with the higher fitted likelihood need not have the higher marginal likelihood. Here the uniform model contains the maximum-likelihood value $3/4$, and the Bayes factor still slightly favors the point model at $1/2$. An improper prior is a second trap. A constant factor in an improper weight cancels inside one model's parameter posterior when that posterior is proper, but it multiplies the marginal likelihood. Two improper priors that differ by a factor of ten do not yield a well-defined Bayes factor merely because each posterior can be normalised. Prior probabilities of the model labels are absent from the Bayes factor and are required as soon as the factor is turned into posterior odds.{{cite:bernardo2005_reference}} (§2.3, def. 3; §3.1, def. 6){{cite:downey2020_thinkbayes2}} (Ch. 10, fair and biased coin models)

## Statistical use
A report can stop at the Bayes factor or continue to a posterior probability. Those are different sentences. With the factor $4/5$ in favor of the uniform model, equal prior probabilities leave the posterior odds at $4/5$. The posterior probability of the uniform model is then $(4/5)/(9/5)=4/9\approx 0.44444$. Prior odds of $2$, meaning the uniform model starts twice as probable as the point model, produce posterior odds $(4/5)\times 2=8/5$ and posterior probability $(8/5)/(13/5)=8/13\approx 0.61538$. The data did not change between these two reports. The prior odds of the model labels did. Quoting $4/5$ alone does not say which of those probabilities was intended.

The same distinction appears when the observation is recorded as a sequence or as a count. The binomial coefficient $4$ multiplies both marginal likelihoods and cancels in $4/5$. It does not cancel a prior odds of $1/3$ or of $2$. Publishing the factor, the prior odds, and the resulting posterior probability makes the arithmetic checkable. Publishing only a posterior probability hides which part came from the data and which part came from the model labels.{{cite:downey2020_thinkbayes2}} (Ch. 10, “Evidence” and “Bayesian Hypothesis Testing”)
