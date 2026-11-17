## Lead context
The calculation combines the starting frequency of a hypothesis with the probability of the finding under each alternative.{{cite:wang2025_foundations}} (Ch. 1, §2.11.2, Thm. 45; §2.12.1)

## Motivating example
A positive test result is more informative when the tested condition is common than when it is rare, even if the test has the same sensitivity. Bayes’ rule combines the test’s behaviour with the condition’s prevalence to answer the question a patient actually asks: among positive results, how many indicate the condition?{{cite:wang2025_foundations}} (Ch. 1, §2.12.1, Example 46)

## Statement
The event formula above requires both conditional probabilities to exist: $\mathbb P(A)>0$ to define $\mathbb P(B\mid A)$, and $\mathbb P(B)>0$ to define the posterior $\mathbb P(A\mid B)$. Here $A$ is the hypothesis event, $B$ is the observed event, $\mathbb P(A)$ is the prior probability, and $\mathbb P(B\mid A)$ is the probability of the observation if $A$ occurs. The denominator is the overall probability of $B$.{{cite:wang2025_foundations}} (Ch. 1, §2.11.2, Thm. 45)

For the density formula, let $\Theta$ be a parameter with prior density $p(\theta)$ and let $X$ be data with conditional density $p(x\mid\theta)$. The lower-case $x$ and $\theta$ are realised values. The joint density is $p(x,\theta)$; $p(\theta\mid x)$ is the posterior density. The marginal density of the data is
\[
p(x)=\int p(x\mid t)p(t)\,dt,
\]
where $t$ ranges over the parameter space. A discrete parameter uses a sum instead of this integral. The posterior formula applies where this marginal density is positive and finite.{{cite:hoff2013_bayes_estimators}} (§2.2, pp. 3–4) {{cite:wang2025_foundations}} (Ch. 20, §23, Defs. 3–4)

## Intuition
Bayes' rule reverses the direction of a conditional probability. A test's sensitivity concerns a positive result among people who have a condition; the probability of the condition among people with a positive result also depends on how common the condition is and how often the test is positive without it. The denominator counts all routes to a positive result.{{cite:wang2025_foundations}} (Ch. 1, §§2.11.2–2.12.1)

In the density version, the likelihood $p(x\mid\theta)$ reweights the prior at each parameter value. Dividing by $p(x)$ makes the reweighted density integrate to one. Likelihood as a function of $\theta$ is not itself a posterior probability density; the prior and its normalising integral are needed.{{cite:hoff2013_bayes_estimators}} (§2.2, pp. 3–4)

## Key results
If $A_1,\ldots,A_m$ are mutually exclusive and exhaustive events, each with positive probability, then for $\mathbb P(B)>0$,
\[
\mathbb P(A_j\mid B)=
\frac{\mathbb P(B\mid A_j)\mathbb P(A_j)}
{\sum_{i=1}^{m}\mathbb P(B\mid A_i)\mathbb P(A_i)}.
\]
The sum accounts for every hypothesis in the partition that can produce $B$. Omitting a term with positive probability changes the denominator.{{cite:wang2025_foundations}} (Ch. 1, §2.11.2, Thm. 45)

If $p(\theta)=0$ throughout a region, then $p(\theta\mid x)=0$ there whenever the posterior is defined. Data can change the relative weights of parameter values in the prior's support, but multiplication by a likelihood cannot give positive posterior density to a region assigned zero prior density. In the question below, this is why 80 successes out of 100 cannot put posterior mass above $1/2$ when the prior rules out that region.{{cite:wang2025_foundations}} (Ch. 20, §23, Def. 4)

## Proof
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
When $\mathbb P(A)>0$ and $\mathbb P(B)>0$, the two definitions of conditional probability give $\mathbb P(A\cap B)=\mathbb P(B\mid A)\mathbb P(A)$ and $\mathbb P(A\cap B)=\mathbb P(A\mid B)\mathbb P(B)$. Equating them and dividing by $\mathbb P(B)$ proves the event formula. For a partition, the disjoint events $A_i\cap B$ cover $B$, so $\mathbb P(B)=\sum_i\mathbb P(B\mid A_i)\mathbb P(A_i)$. Substitution proves the displayed partition formula.{{cite:wang2025_foundations}} (Ch. 1, §2.11.2, Thm. 45)

For densities, the product rule gives $p(x,\theta)=p(x\mid\theta)p(\theta)=p(\theta\mid x)p(x)$ almost everywhere. Integrating the first factorisation over $\theta$ gives $p(x)=\int p(x\mid t)p(t)\,dt$. Dividing the joint-density equality by this positive, finite value proves the density formula. Its integral over $\theta$ is one because the numerator integrates to $p(x)$. If the prior density vanishes on a region, so does the product in the numerator, proving the support statement.{{cite:hoff2013_bayes_estimators}} (§2.2, pp. 3–4) {{cite:wang2025_foundations}} (Ch. 20, §23, Defs. 3–4)
:::
:::

## Statistical use
For diagnostic tests, specify prevalence, sensitivity, and false-positive probability for the population being tested. A positive predictive probability then follows from the partition formula. The result may differ greatly from sensitivity when prevalence is low. For models, use each model's marginal likelihood, which averages its sampling density over that model's parameter prior, when updating model probabilities.{{cite:wang2025_foundations}} (Ch. 1, §2.12.1) {{cite:kass_raftery1995}} (§3.1, pp. 777–778)

When reporting a posterior, state the prior and the likelihood alongside it. In particular, a prior that excludes scientifically plausible parameter values deserves attention before analysing more data, because the posterior retains that exclusion.{{cite:wang2025_foundations}} (Ch. 20, §23, Defs. 1–4)

## Worked example
Suppose a condition affects $1\%$ of a population, a test is positive for $90\%$ of those with the condition, and it is positive for $5\%$ of those without it. Among $10{,}000$ people with these proportions, the model expects $100$ to have the condition and $90$ of those to test positive. It expects $9{,}900$ not to have it and $495$ of those to test positive. Thus a positive result has probability
\[
\frac{90}{90+495}=\frac{2}{13}\approx0.1538
\]
of indicating the condition under this model. The test sensitivity is $0.90$; the positive predictive probability is about $0.154$ because the false positives come from a much larger group.{{cite:wang2025_foundations}} (Ch. 1, §2.12.1, Example 46)

**Your turn.** With the same prevalence and sensitivity, suppose the false-positive probability falls to $1\%$. What is the positive predictive probability?{{cite:wang2025_foundations}} (Ch. 1, §2.12.1, Example 46)

::: {.callout-tip collapse="true" title="Answer"}
The expected true positives remain $90$, while expected false positives fall to $99$. The probability is $90/(90+99)=10/21\approx0.4762$.
:::

## Common misconceptions
Sensitivity and positive predictive probability condition in opposite directions. A posterior probability also differs from a likelihood: the former normalises a likelihood weighted by a prior across possible hypotheses or parameter values. Repeated observations do not restore a region to which the prior assigned zero probability.{{cite:wang2025_foundations}} (Ch. 1, §§2.11.2–2.12.1; Ch. 20, §23, Defs. 2–4)

## History
Bayes's essay was framed as a way to reason from observed successes and failures to an unknown chance of success. Richard Price communicated it after Bayes's death, and it appeared in the 1763 *Philosophical Transactions*. Its repeated-trials problem became an early example of inverse probability.{{cite:bayes1763}} (pp. 370–372)

Kass and Raftery's 1995 review describes the later use of posterior odds and Bayes factors for comparing scientific models. For two models, their calculation separates the starting odds from the evidence supplied by the observations.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)
