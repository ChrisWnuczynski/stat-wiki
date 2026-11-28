## Motivating example
Seventy earlier rat studies can help estimate the tumour rate in a new study only if the old and new rates are comparable in a stated sense. The rats, sample sizes and observed counts need not match. A hierarchical model instead asks whether the *study-specific rates*, before the outcomes are observed and given what is known about the studies, have a distribution that is unchanged by relabelling the studies. This symmetry is exchangeability. It gives a reason to share information while still allowing different rates.{{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.2, pp. 102–105)

## Intuition
Imagine shuffling the labels on a collection of sealed study reports. If the labels themselves carry no information about the unknown rates, assigning those labels in another order should not change their joint probability. Exchangeability formalizes that judgement. It is weaker than independence: observing one study can change what is plausible for another when both depend on an unknown population distribution. It is also weaker than equality: distinct studies may have distinct rates.{{cite:gelman_bda2013}} (Ch. 5, §5.2, pp. 104–106)

## Definition
A vector $(X_1,\ldots,X_J)$ is exchangeable if, for every permutation $\pi$ of its indices, $(X_1,\ldots,X_J)$ and $(X_{\pi(1)},\ldots,X_{\pi(J)})$ have the same joint distribution. When a joint density exists, the density expression is

$$
p(\theta_1,\ldots,\theta_J)=p(\theta_{\pi(1)},\ldots,\theta_{\pi(J)}).
$$

The definition concerns the joint law, not just equal marginal distributions. An infinite sequence is exchangeable when every finite prefix has this symmetry. The distinction matters because an infinite Bernoulli sequence has a representation that an arbitrary *finite* exchangeable vector need not have.{{cite:gelman_bda2013}} (Ch. 5, §5.2, pp. 104–105)

## Interpretation — What labels may reveal
For the rat studies, let $Y_j\mid\theta_j,n_j\sim\operatorname{Bin}(n_j,\theta_j)$, with latent tumour rate $\theta_j$. Conditional on common hyperparameters $(\alpha,\beta)$, the usual hierarchy has $\theta_j\stackrel{\mathrm{iid}}{\sim}\operatorname{Beta}(\alpha,\beta)$ and hence

$$
p(\boldsymbol\theta\mid\alpha,\beta)=\prod_{j=1}^Jp(\theta_j\mid\alpha,\beta).
$$

This joint prior is exchangeable. Unequal $n_j$ do not by themselves break exchangeability of the *rates*, provided sample size does not signal the rate. The observed counts are not identically distributed when the $n_j$ differ. If studies in one laboratory systematically have higher risks than those in another, a single exchangeable prior across all labels conceals known structure; laboratory or protocol belongs in the model.{{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.2, pp. 102–105)

Exchangeability is specified relative to the information available before examining the outcomes under analysis. Learning that the new study used a different strain, laboratory or calendar period can defeat the original symmetry. Conversely, grouping comparable studies and conditioning on their recorded differences can support a more refined conditional or partial exchangeability claim. The label judgment is scientific, not a mechanical consequence of fitting a beta prior.{{cite:gelman_bda2013}} (Ch. 5, §5.2, pp. 105–106)

## Properties — Symmetry, mixtures and dependence
An iid sample is exchangeable because multiplication is unchanged by reordering. The converse fails for a finite sample. Consider one red and one blue ball drawn without replacement: the ordered colours are red–blue or blue–red with equal probability, so the pair is exchangeable, but the second colour is determined by the first. Equal one-dimensional marginals alone also do not certify symmetry of the whole joint law.{{cite:gelman_bda2013}} (Ch. 5, §5.2, finite-mixture qualification)

For an infinitely exchangeable sequence of zero–one variables, de Finetti's representation gives a probability distribution $F$ on $[0,1]$ such that

$$
\mathbb{P}(X_1=x_1,\ldots,X_n=x_n)=\int_0^1\prod_{i=1}^n t^{x_i}(1-t)^{1-x_i}\,dF(t).
$$

The sequence is therefore conditionally iid Bernoulli given a latent success probability $t$. Unconditionally the observations generally depend on one another. This representation requires an *infinite* exchangeable sequence, or a finite vector extendible consistently to all lengths; a symmetric vector of a fixed size alone does not qualify.{{cite:gelman_bda2013}} (Ch. 5, §5.2, p. 105)

::: {.callout-note collapse="true" title="Proof"}
Suppose $X_i\mid\Theta=t$ are iid Bernoulli$(t)$ and $\Theta$ has distribution $F$. For a vector containing $s$ ones, its conditional probability is $t^s(1-t)^{n-s}$, which is unchanged by any permutation. Integration over $F$ preserves that equality, proving exchangeability. Moreover, $\E(X_i)=\E(\Theta)$ and, for $i\ne j$, $\E(X_iX_j)=\E(\Theta^2)$; hence $\operatorname{Cov}(X_i,X_j)=\operatorname{Var}(\Theta)\ge0$. For the two-ball draw without replacement, $\E(X_i)=1/2$ and $\E(X_1X_2)=0$, giving covariance $-1/4$. That finite exchangeable pair cannot arise from an iid Bernoulli mixture. This proves the forward mixture implication and the finite counterexample; the converse representation for infinite sequences requires the separate limiting argument.{{cite:gelman_bda2013}} (Ch. 5, §5.2, p. 105)
:::

## Statistical use — Borrowing strength carefully
In a hierarchical model, exchangeability of latent rates justifies a common population distribution. Updating its unknown hyperparameters with all studies makes one study informative about another, which is the basis of partial pooling. Complete pooling would impose a single identical rate; no pooling would estimate each rate without that shared distribution. The rat-tumour example has $4$ tumours among $14$ rats in the current study and $70$ historical studies. A one-study $\operatorname{Beta}(\alpha,\beta)$ prior gives a $\operatorname{Beta}(\alpha+4,\beta+10)$ posterior; the older studies can inform $(\alpha,\beta)$ only under a defensible comparability model.{{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.2, pp. 102–105)

The distinction between latent parameters and observations also matters in repeated-measures analysis. An “exchangeable correlation” matrix uses the same pairwise correlation for every pair of visits; that covariance pattern does not, by itself, assert that visit outcomes have a permutation-invariant *joint distribution*. Visits with a time trend can violate exchangeability even when a constant working correlation is used for robust estimating equations.{{cite:gelman_bda2013}} (Ch. 5, §5.2, discussion of label information)

If all historical rat studies came from laboratory A while the new study came from laboratory B, lab membership distinguishes the new rate before any tumour count is observed. If risk changes over calendar time, permuting years discards a meaningful order. If larger studies were deliberately assigned to high-risk strains, $n_j$ itself can reveal information about $\theta_j$. In each case an unqualified exchangeable-rate prior can overpool unlike studies; use strata, covariates or separate hierarchies. A fixed finite collection may also be exchangeable without an iid-mixture representation, as the negatively dependent two-ball example shows.{{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.2, pp. 103–106)

## Worked example
Suppose a common success probability $\Theta$ has a $\operatorname{Beta}(2,3)$ distribution and $X_1,X_2$ are Bernoulli trials conditional on $\Theta$. Then $\E\Theta=2/5=0.4$ and $\E\Theta^2=2(3)/(5\cdot6)=0.2$. The ordered probabilities are $\mathbb{P}(1,1)=0.2$, $\mathbb{P}(1,0)=\mathbb{P}(0,1)=\E[\Theta(1-\Theta)]=0.2$, and $\mathbb{P}(0,0)=0.4$. The two middle sequences have equal probability, confirming exchangeability; yet $\operatorname{Cov}(X_1,X_2)=0.2-0.4^2=0.04$, confirming dependence. After observing a success, the predictive probability of another success is $3/6=0.5$; after a failure it is $2/6=1/3\approx0.333333$. The first result changes the prediction because it updates the common latent probability.{{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.2)

**Your turn.** A bag contains exactly one red and one blue ball. Draw both without replacement and mark red by $1$. Find the two ordered probabilities, each marginal mean and the covariance. Is this pair exchangeable? Could it be two draws from a mixture of iid Bernoulli laws?

::: {.callout-tip collapse="true" title="Answer"}
The outcomes $(1,0)$ and $(0,1)$ each have probability $1/2$. Each marginal mean is $1/2$, while $\E(X_1X_2)=0$, so the covariance is $0-(1/2)^2=-1/4$. Swapping the labels exchanges the two equally likely outcomes, hence the pair is exchangeable. An iid Bernoulli mixture has covariance $\operatorname{Var}(\Theta)\ge0$, so it cannot produce this pair.
:::

## Common misconceptions
Exchangeability does not require equal observations or equal unknown rates; it requires symmetry of their joint *distribution*. It does not make observations independent: a shared unknown probability usually creates positive marginal association. Nor does finite exchangeability alone entitle us to a de Finetti iid-mixture representation: the two-ball pair is an exact counterexample. Finally, an exchangeable working *correlation* is a matrix specification, not a complete claim about all permutations of a joint distribution.{{cite:gelman_bda2013}} (Ch. 5, §5.2, pp. 104–106)

## Assumptions and limits — Symmetry is not independence
Exchangeability does not require equal observations or equal unknown rates; it requires symmetry of their joint *distribution*. {{cite:gelman_bda2013}} (Ch. 5, §5.2, pp. 104–106)

## Connections
An exchangeable prior on study rates is a key input to a [hierarchical Bayesian model](hierarchical-bayesian-model.qmd) and to [partial pooling](complete-pooling-no-pooling-and-partial-pooling.qmd). A [Beta distribution](beta-distribution.qmd) can model a common population of binomial rates, whereas an [exchangeable correlation](exchangeable-correlation.qmd) is only a covariance structure. Distinguishing these uses of symmetry helps interpret what information a pooled analysis is allowed to share.{{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.2)

## History
De Finetti's 1937 paper developed exchangeable sequences in a theory of prediction. The Bernoulli representation bearing his name explains how an infinite sequence with permutation symmetry can be understood as a mixture of iid Bernoulli sequences; later hierarchical modelling uses the same mixture idea for latent study parameters. The finite-sequence qualification is essential to that historical result.{{cite:gelman_bda2013}} (Ch. 5, §5.2, p. 105)
