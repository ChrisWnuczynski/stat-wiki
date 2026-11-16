## Motivating example
A quality-control system raises an alarm that is more likely when a unit is defective. The alarm's likelihood ratio measures how strongly the observation favours a defect, but it cannot by itself say how probable a defect is afterward. Prior odds encode how common the two states were judged to be before the alarm; multiplying them by the evidence ratio gives the posterior odds. The arithmetic separates background prevalence from what this particular observation adds.{{cite:gelman_bda2013}} (Ch. 1, §§1.3–1.4, pp. 7–9)

## Intuition
Odds compare two probabilities by division. If $M_1$ and $M_0$ exhaust the possibilities and $P(M_1)=p$, their prior odds in favour of $M_1$ are $p/(1-p)$. Odds of $1:9$ mean that $M_0$ had nine times the prior probability; they do not mean a 1% chance of $M_1$. Evidence can move these odds up or down without necessarily reversing which model is more probable. The order of the ratio matters: reversing the named models takes the reciprocal of both prior odds and evidence factor.{{cite:gelman_bda2013}} (Ch. 1, §1.3, p. 8; Ch. 7, §7.4, pp. 182–183)

## Definition
For hypotheses or models $M_1,M_0$ with positive prior probabilities, the prior odds are $O_{10}=P(M_1)/P(M_0)$. When the pair is exhaustive, $P(M_1)=O_{10}/(1+O_{10})$. For model comparison, the data's factor is $B_{10}=p(y\mid M_1)/p(y\mid M_0)$, where each model's marginal likelihood averages over its own parameter prior. The posterior odds are $O_{10}(y)=B_{10}O_{10}$. If the two models are simple point hypotheses, the Bayes factor reduces to their ordinary likelihood ratio.{{cite:gelman_bda2013}} (Ch. 1, §1.3, p. 8, equation 1.5; Ch. 7, §7.4, p. 183, equation 7.16)

## Interpretation
The existing factorisation cancels the common predictive normaliser $p(y)$ and shows exactly where the prior odds enter. A factor greater than one says the observed data favour $M_1$ *relative to the prior*. It does not say $M_1$ is now more probable than $M_0$: that conclusion requires $B_{10}O_{10}>1$. For two non-exhaustive models among several possibilities, their pairwise odds still update by the same ratio, but $O/(1+O)$ is then a probability conditional on the pair, not the unconditional probability of $M_1$.{{cite:gelman_bda2013}} (Ch. 7, §7.4, pp. 182–183)

## Properties
Successive observations contribute multiplicative evidence only through the appropriate conditional likelihood ratios. If $Y_1$ and $Y_2$ are conditionally independent under each model, $B_{10}(y_1,y_2)=B_{10}(y_1)B_{10}(y_2)$. Without that condition, the second factor must be $p(y_2\mid y_1,M_1)/p(y_2\mid y_1,M_0)$; multiplying marginal factors would count a repeated signal twice. Log odds turn the valid product into a sum, useful when many independent measurements are processed.{{cite:gelman_bda2013}} (Ch. 1, §§1.3–1.4, pp. 8–10)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Bayes' rule gives $P(M_j\mid y)=p(y\mid M_j)P(M_j)/p(y)$. Dividing the expression for $j=1$ by the expression for $j=0$ cancels $p(y)$ and yields $O_{10}(y)=B_{10}O_{10}$. For two observations, the chain rule gives $p(y_1,y_2\mid M_j)=p(y_1\mid M_j)p(y_2\mid y_1,M_j)$. Taking the ratio across $j$ proves the conditional-factor formula; conditional independence replaces the second conditional likelihood by $p(y_2\mid M_j)$. Finally, if only $M_1,M_0$ are possible, let $p=P(M_1)$ and solve $O=p/(1-p)$ to get $p=O/(1+O)$.{{cite:gelman_bda2013}} (Ch. 1, §1.3, pp. 7–8; Ch. 7, §7.4, pp. 182–183)
:::
:::

## Statistical use
Define the model pair and its prior probabilities before using the data. Compute each marginal likelihood under a proper within-model prior, then form the Bayes factor in the same numerator order as the prior odds. Report both the prior and posterior odds so that the contribution of the data is visible. Check whether a plausible change in prior model weights or within-model priors changes the conclusion; marginal likelihoods can be especially sensitive to the latter. When models are not a credible exhaustive list, interpret a pairwise comparison as conditional on the selected alternatives.{{cite:gelman_bda2013}} (Ch. 7, §7.4, pp. 182–184)

## Worked example
Suppose 10% of inspected units are defective before a sensor is read, so the prior defect odds are $0.1/0.9=1/9$. An alarm occurs with probability $0.8$ for a defective unit and $0.1$ for a sound unit. The alarm's likelihood ratio is $0.8/0.1=8$, giving posterior odds $8:9$. The posterior defect probability is $8/(8+9)=8/17\approx0.471$. An alarm greatly raises the probability from $0.1$, yet it remains below one half because defects were initially uncommon. The calculation assumes the stated rates apply to the units being inspected.{{cite:gelman_bda2013}} (Ch. 1, §1.3, pp. 7–8, odds form of Bayes' rule)

**Your turn.** A second sensor is used where the prior probability of a defect is $0.25$. Its alarm rates are $0.6$ for defective units and $0.2$ for sound units. Find the likelihood ratio, posterior odds and posterior defect probability after an alarm.

::: {.callout-tip collapse="true" title="Answer"}
The prior odds are $0.25/0.75=1:3$. The alarm likelihood ratio is $0.6/0.2=3$, so the posterior odds are $1:1$ and the posterior defect probability is $1/(1+1)=0.5$. This conclusion concerns the defined defect versus sound pair under the stated sensor model.{{cite:gelman_bda2013}} (Ch. 1, §1.3, p. 8)
:::

## Common misconceptions
A Bayes factor is not a posterior probability; it multiplies prior odds. Prior odds of $1:9$ do not assign probability $1/9$ to $M_1$ when the pair is exhaustive—the probability is $1/10$. Equal prior model odds are a substantive choice, not an automatic consequence of having two labels. A point hypothesis also cannot be given positive posterior probability by putting it inside a continuous parameter model with no point mass; it must be a genuine discrete alternative in the model comparison.{{cite:gelman_bda2013}} (Ch. 1, §1.3, p. 8; Ch. 7, §7.4, pp. 183–184)

## Assumptions and limits — When odds are misread
If the sensor was calibrated on different units and its sound-unit alarm rate is actually $0.4$ rather than $0.1$, the worked example's evidence ratio is $2$ rather than $8$ and its posterior defect probability is only $2/11\approx0.182$. If two alarms arise from the same hidden fault, multiplying their marginal ratios as if conditionally independent exaggerates evidence. For a model with an arbitrary improper parameter prior, the marginal likelihood lacks a defined normalising scale, so a Bayes factor and posterior model odds may be undefined. These failures come from a wrong likelihood or an invalid model comparison, not from the odds identity.{{cite:gelman_bda2013}} (Ch. 1, §1.3, pp. 7–8; Ch. 7, §7.4, pp. 183–184)

## Connections
The [odds](odds.qmd) page handles probability-to-odds conversion, while [posterior odds](posterior-odds-factorisation.qmd) and [marginal likelihood](marginal-likelihood-and-bayes-factor.qmd) develop the evidence factor. The answered [posterior-odds question](../questions/ex-sl-06-1.qmd) converts a model prior and Bayes factor; [evidence versus probability](../questions/q-21.qmd) tests whether a favourable factor overcomes prior odds; [the fair-coin question](../questions/q-44.qmd) distinguishes a point-mass model from a continuous parameter prior.{{cite:gelman_bda2013}} (Ch. 7, §7.4, pp. 182–184)

## History
Bayes' rule is a conditioning identity; its odds form has long been useful because the same evidence ratio can update very different prior beliefs transparently. Dodge's account of Bayes describes Price's 1763 publication of Bayes' essay, while modern model comparison makes the distinction between prior model probabilities and within-model priors explicit. The identity remains valid, but its inputs must be meaningful for the scientific alternatives under comparison.{{cite:dodge2008}} (pp. 30–32, “Bayes' Theorem” and “Bayes, Thomas”){{cite:gelman_bda2013}} (Ch. 7, §7.4, pp. 182–184)
