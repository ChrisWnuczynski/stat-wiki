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
