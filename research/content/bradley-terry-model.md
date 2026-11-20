## Motivating example

Two teams with the same number of wins may have faced different opponents. A paired-comparison model estimates strengths using who played whom, then predicts a future head-to-head result. The Bradley–Terry construction describes contests with two possible outcomes using one positive strength per competitor.{{cite:caron_doucet2012_bt}} (§1, eq. 1)

## Definition — Strength ratios and log-strength differences

Write strengths as $a_j>0$ and log strengths as $\lambda_j=\log a_j$. The model specifies
$$
P(j\text{ beats }k)=\frac{a_j}{a_j+a_k},\qquad
\log\frac{P(j\text{ beats }k)}{P(k\text{ beats }j)}=\lambda_j-\lambda_k.
$$
Only relative strengths are identified. Multiplying all $a_j$ by a common positive factor, or adding a common constant to all $\lambda_j$, leaves every probability unchanged. A reference strength or a sum constraint supplies a parameterisation.{{cite:turner_firth2012_bradley_terry}} (§1, eq. 1)

Reciprocal odds alone do not force this model. With three competitors, reciprocal pairwise odds can form a cycle. Bradley–Terry imposes the stronger relation that log odds add across comparisons: $(\lambda_i-\lambda_j)+(\lambda_j-\lambda_k)=\lambda_i-\lambda_k$. This is a restriction to assess against the competition structure, not an automatic consequence of two-outcome results.{{cite:caron_doucet2012_bt}} (§1, eq. 1)

## Properties — Fitting comparisons and venue effects

If independent contests give $w_{jk}$ wins for $j$ against $k$ out of $n_{jk}$ comparisons, the log likelihood, apart from data-only constants, is
$$
\ell(\lambda)=\sum_{j<k}\left[w_{jk}(\lambda_j-\lambda_k)-n_{jk}\log\{1+e^{\lambda_j-\lambda_k}\}\right].
$$
Each comparison has design row $e_j-e_k$, making the fit a binomial logistic model on strength differences. A disconnected schedule cannot identify relative strengths across its disconnected groups from their match results alone.{{cite:turner_firth2012_bradley_terry}} (§1){{cite:caron_doucet2012_bt}} (§2, log-likelihood formulation)

A venue term $\alpha$ can enter the log odds for the home side. For the same ordered pair of competitors, the home and away logits are $\lambda_j-\lambda_k+\alpha$ and $\lambda_j-\lambda_k-\alpha$. Their odds ratio is $e^{2\alpha}$; the home-to-neutral odds ratio is $e^\alpha$. These are different comparisons. Models for home advantage and ties extend the basic no-tie likelihood.{{cite:caron_doucet2012_bt}} (§3, standard extensions)

## Worked example

Take strengths $a_A=3$, $a_B=2$ and $a_C=1$. The neutral probabilities are $P(A>B)=3/5$, $P(B>C)=2/3$ and $P(A>C)=3/4$. The corresponding odds are $3/2$, $2$ and $3$, whose first two multiply to the third. Choosing competitor $C$ as reference gives log strengths $(\log3,\log2,0)$; centring them changes none of those probabilities.

For a home term $\alpha=0.3957$, the home-to-neutral odds multiplier is approximately $1.48542$ and the home-to-away multiplier is approximately $2.20648$. A neutral log-strength difference $0.2292$ gives home logit $0.6249$ and probability approximately $0.651332$. These are direct substitutions into the venue extension.{{cite:caron_doucet2012_bt}} (§3, home advantage)

**Your turn.** If every log strength increases by five, what happens to the probability $P(A>B)$?

::: {.callout-tip collapse="true" title="Answer"}
It remains $3/5$. The difference $(\log3+5)-(\log2+5)$ equals $\log(3/2)$.
:::

## Connections — Ties and point systems

A draw is a third possible outcome, so modelling its probability requires an outcome model that allows ties. Treating a draw as half a win and half a loss is a possible scoring convention for a two-outcome estimating procedure; it does not supply a probability model for the draw. League-table point allocations also do not determine the probability of a win in a paired-comparison model. The target likelihood and treatment of draws must be specified separately.{{cite:caron_doucet2012_bt}} (§3, models with ties)

## Check yourself

### [Bradley–Terry](../questions/c-26.qmd) {#self-check-c-26}

State the no-tie probability in terms of log strengths and explain one identifying constraint.

::: {.callout-tip collapse="true" title="Answer"}
It is $e^{\lambda_j}/(e^{\lambda_j}+e^{\lambda_k})$. Setting one log strength to zero fixes the arbitrary common shift while preserving every fitted probability.
:::

### [Multinomial logistic regression](../questions/q-46.qmd) {#self-check-q-46}

Why do probabilities stay fixed when the reference score changes?

::: {.callout-tip collapse="true" title="Answer"}
Subtracting the new reference score from every score multiplies every exponentiated score by the same positive factor. That factor cancels from each probability ratio.
:::
