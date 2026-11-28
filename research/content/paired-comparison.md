## Motivating example
A taste test records which of two drinks is preferred without measuring either drink on a common numerical scale. A sports match likewise supplies a winner rather than a direct measurement of team strength. Paired-comparison models combine such binary outcomes into a scale of relative ability.{{cite:turner_firth2012_bradley_terry}} (§1, pp. 1–2)

## Definition — Preferences between two items
For items $i$ and $j$ with log abilities $\lambda_i$ and $\lambda_j$, the Bradley–Terry model specifies
$$
\mathbb{P}(i\text{ beats }j)=\frac{e^{\lambda_i}}{e^{\lambda_i}+e^{\lambda_j}},\qquad
\log\frac{\mathbb{P}(i\text{ beats }j)}{\mathbb{P}(j\text{ beats }i)}=\lambda_i-\lambda_j.
$$
The model is for contests without ties. A pair of matched numerical measurements, analysed through their difference, is a different type of paired-data analysis.{{cite:turner_firth2012_bradley_terry}} (§1, eq. 1, pp. 1–2)

Only differences of log abilities enter the probabilities. Adding one constant to every $\lambda_i$ changes no contest probability. A reference item with ability zero, or a sum-to-zero constraint, fixes that arbitrary location. Comparing items in disconnected groups requires additional information that joins their ability scales.{{cite:turner_firth2012_bradley_terry}} (§2.1, standard model)

## Statistical use — Turning contests into a likelihood
If independent contests between $i$ and $j$ yield $w_{ij}$ wins out of $n_{ij}$, their likelihood contribution is proportional to $p_{ij}^{w_{ij}}(1-p_{ij})^{n_{ij}-w_{ij}}$. Each contest supplies a contrast row with $+1$ for one item and $-1$ for the other. The linear predictor is therefore an ability difference, making the model a structured binomial logistic regression.{{cite:turner_firth2012_bradley_terry}} (§§1–2, pp. 2–3){{cite:nelder_wedderburn1972}} (§3.3, binomial models, pp. 379–380)

An item that wins every observed contest can drive a fitted ability contrast toward infinity. Schedule connectivity establishes which differences are identified, while finite maximum-likelihood estimates also depend on the directions of the outcomes. Repeated judgements by the same person or contests sharing unmodelled conditions may also violate independence.{{cite:turner_firth2012_bradley_terry}} (§§2.3, 3, bias reduction and model extensions)

## Worked example
Assign abilities $\lambda_A=0$, $\lambda_B=0.8$, and $\lambda_C=1.4$. Then the fitted probabilities that B beats A, C beats A, and C beats B are respectively $0.689974$, $0.802184$, and $0.645656$. Adding $5$ to all three abilities gives the same probabilities. The odds satisfy a consistency restriction: the odds of C beating A equal the product of the odds of C beating B and B beating A, because $1.4=0.6+0.8$.{{cite:turner_firth2012_bradley_terry}} (§1, eq. 1)

Three arbitrary observed proportions need not satisfy that multiplicative restriction. For example, a cycle with probability $0.8$ for A beating B, B beating C, and C beating A cannot be represented exactly by a single set of abilities: adding the three log-odds would give a positive number, whereas the three ability differences sum to zero.

**Your turn.** If B's odds of beating A are $2$ and C's odds of beating B are $3$, what is C's probability of beating A under this model?

::: {.callout-tip collapse="true" title="Answer"}
The odds multiply to $6$, so the probability is $6/(1+6)=6/7$.
:::

## Check yourself

### The head-to-head model {#self-check-c-26}

[Practice question](../questions/c-26.qmd)

What is the Bradley--Terry model for a head-to-head contest with no ties?

::: {.callout-tip collapse="true" title="Answer"}
**Definitions/notation.** For a contest with no ties, assign real-valued log-abilities $\lambda_j$; the model specifies $\mathbb{P}(j\text{ beats }k)=e^{\lambda_j}/(e^{\lambda_j}+e^{\lambda_k})$, equivalently odds $e^{\lambda_j-\lambda_k}$. Only ability differences are identifiable, so a reference such as $\lambda_1=0$ is needed.
:::

### Model discrepancy {#self-check-c-29}

[Practice question](../questions/c-29.qmd)

What is a saturated model, and what does deviance compare? Distinguish deviance from scaled deviance.

::: {.callout-tip collapse="true" title="Answer"}
**Definitions/notation.** A saturated mean model fits each observed response exactly ($\tilde\mu_i=y_i$, possibly as a boundary limit); at common dispersion $\phi$, the scaled deviance is $D/\phi=2\{\ell(\tilde\mu;y,\phi)-\ell(\hat\mu;y,\phi)\}$. Thus the unscaled deviance $D$ is $\phi$ times that log-likelihood-ratio discrepancy, and equals the scaled deviance when $\phi=1$.
:::
