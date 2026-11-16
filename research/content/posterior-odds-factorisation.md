## Motivating example
Suppose a quality-control manager gives a new process only one chance in five of being the better explanation before seeing inspection results. A run of passes may favour the new process as evidence, yet leave the old process more probable overall. The posterior-odds factorisation separates these two parts of the judgment: the data change the odds by a *Bayes factor*, while the starting odds remain visible. This matters whenever a statement such as “the evidence favours this model” is mistaken for “this model is now most probable.”{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

## Statement
The models $M_1$ and $M_2$ must have positive prior probabilities and defined, positive marginal likelihoods for the observed data. The Bayes factor $\operatorname{BF}_{12}=p(x\mid M_1)/p(x\mid M_2)$ is directed: reversing the model order takes its reciprocal. If the two models are the only candidates, their posterior probabilities add to one, so posterior odds can be converted to a posterior probability. If further models remain in the comparison, the ratio between $M_1$ and $M_2$ is still valid, but those two probabilities do not alone add to one.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

## Intuition
Bayes' rule assigns each model a weight proportional to its prior probability times its predictive probability for the observed data. Taking a ratio removes the common normalising denominator. The factor left from the data is a comparison of how well each *whole model* predicted what was observed, including any uncertainty over its parameters. A Bayes factor above one means the data move the odds towards $M_1$ relative to the prior; it says nothing by itself about whether the final odds exceed one.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

When a model has an unknown parameter, its marginal likelihood integrates the likelihood against that model's parameter prior: $p(x\mid M_j)=\int p(x\mid\theta_j,M_j)p(\theta_j\mid M_j)\,d\theta_j$. This is an average over parameter values that were plausible before the data, not the likelihood at a fitted maximum. A parameter prior and a prior *model probability* occupy different places in the calculation: the former shapes each marginal likelihood, while the latter sets the starting odds between models.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

## Key results — Reading the three ratios
For two exhaustive models, let the prior odds in favour of $M_1$ be $O_{12}=\Pr(M_1)/\Pr(M_2)$. Then the posterior odds are $\operatorname{BF}_{12}O_{12}$ and the posterior probability of $M_1$ is $\operatorname{BF}_{12}O_{12}/(1+\operatorname{BF}_{12}O_{12})$. The same Bayes factor can therefore produce different posterior probabilities for investigators with different stated prior model probabilities. If the prior odds are one, the Bayes factor equals the posterior odds; that special case does not make it a probability.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

For simple models with no unknown parameters, the marginal likelihood is simply the probability or density of the data under that model. With composite models, each parameter prior changes the integrated prediction and may materially alter the Bayes factor. This sensitivity is a reason to state and probe plausible parameter priors, especially where an alternative spreads mass over a wide range of effects.{{cite:kass_raftery1995}} (§§3.1, 5.1, pp. 777–778, 783–784)

## Statistical use — Comparing models honestly
Specify both models, their parameter priors if needed, and their prior model probabilities. Compute each marginal likelihood on the same observation scale, retain constants that belong to the data probability, and form a clearly directed Bayes factor. Multiply it by the prior odds, then convert to a posterior probability only if the model set supports that conversion. Report the Bayes factor and posterior probability separately: one describes the data's relative update, the other includes the starting model weights. Finally, inspect how the answer changes under defensible prior choices and whether either model adequately describes the observations.{{cite:kass_raftery1995}} (§§3.1, 5.1, pp. 777–778, 783–784)

## Worked example
Let $M_0$ fix the pass probability at $p=1/2$ and $M_1$ fix it at $p=3/4$. Suppose four independent components are inspected, exactly three pass, and the prior model probabilities are $\Pr(M_1)=1/5$ and $\Pr(M_0)=4/5$. For the count $X=3$, the two predictive probabilities are
$$
p(X=3\mid M_0)=\binom43(1/2)^3(1/2)=1/4,
\qquad
p(X=3\mid M_1)=\binom43(3/4)^3(1/4)=27/64.
$$
Thus $\operatorname{BF}_{10}=(27/64)/(1/4)=27/16\approx1.6875$. The data favour $M_1$ relative to $M_0$, but the prior odds for $M_1$ are only $1:4$. The posterior odds are $(27/16)(1/4)=27:64$, giving $\Pr(M_1\mid X=3)=27/91\approx0.2967$. The new process gained support, yet it remains less probable than the old process under this two-model analysis.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

**Your turn.** Keep the same models and priors, but suppose all four components pass. Find the Bayes factor in favour of $M_1$, its posterior odds, and its posterior probability.

::: {.callout-tip collapse="true" title="Answer"}
Now $p(X=4\mid M_0)=1/16$ and $p(X=4\mid M_1)=81/256$, so $\operatorname{BF}_{10}=81/16=5.0625$. Multiplying by the prior odds $1/4$ gives posterior odds $81:64$ and $\Pr(M_1\mid X=4)=81/145\approx0.5586$. Here the evidence is strong enough to reverse the original four-to-one preference for $M_0$.
:::

## Common misconceptions
A Bayes factor is not a posterior probability: it can exceed one and has no upper bound of one. A Bayes factor favouring $M_1$ does not guarantee that $M_1$ has the larger posterior probability; prior odds can outweigh a modest update. The ratio of maximised likelihoods is not generally a Bayes factor for composite models, since the latter integrates over parameter priors. Lastly, switching from $\operatorname{BF}_{10}$ to $\operatorname{BF}_{01}$ without inverting the number reverses the evidence. These are distinct mistakes about scale, starting weights, integration, and direction.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

## Generalizations — Limits of the comparison
The identity still holds for any pair inside a larger collection of models, but pairwise odds do not tell the total posterior mass outside that pair. A model assigned zero prior probability cannot acquire positive posterior probability by multiplying odds; it must be included with positive prior mass at the outset. For a composite model with an improper parameter prior, multiplying that prior by an arbitrary constant changes its marginal likelihood, so the Bayes factor is generally not defined without additional construction. And a large factor comparing two poor models establishes only which of the two predicts the observed data better under the stated priors, not that either is an adequate account of the process.{{cite:kass_raftery1995}} (§3.1, pp. 777–778; §5.3 and §6.1, p. 784)

## Related concepts
[Marginal likelihood and Bayes factor](marginal-likelihood-and-bayes-factor.qmd) explain the data ratio, while [prior odds](prior-odds.qmd) represent the model weights before observing data. [Posterior hypothesis probability](posterior-hypothesis-probability.qmd) converts odds to a probability when the model collection is specified. [Bayes action for two hypotheses](bayes-action-for-two-hypotheses.qmd) adds losses to turn posterior probabilities into a decision; the highest posterior probability need not always dictate the action.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

## History
Kass and Raftery trace the practical use of Bayes factors to Harold Jeffreys's work in the 1930s and his later *Theory of Probability*. Dodge records that book's 1939 publication in Jeffreys's biography. The factorisation itself is an elementary consequence of Bayes' rule; its value in model comparison is that it keeps the evidence ratio distinct from prior beliefs and final posterior model probabilities.{{cite:kass_raftery1995}} (p. 773, introduction; §3.1, pp. 777–778){{cite:dodge2008}} (p. 274, “Jeffreys, Harold”)
