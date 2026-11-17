## Lead context

A positive test is more common among people who have a condition than among people who do not. The likelihood ratio of that result is how many times more common. Multiplied by the prior odds of the condition, it gives the posterior odds. Sensitivity alone does not. The ratio uses both the true-positive rate and the false-positive rate, and the base rate stays outside it, in the prior odds.{{cite:gelman_bda2013}} (Ch. 1, p. 8){{cite:openintro2019}} (Ch. 3, Example 3.42, pp. 105–106)

## Motivating example

A mammogram is positive with probability $0.89$ if cancer is present and with probability $0.07$ if it is not. The likelihood ratio of a positive result is $0.89/0.07\approx 12.7$. A positive mammogram is about thirteen times more likely under cancer than under no cancer. In a population where the base rate is $0.0035$, the prior odds are about $0.0035/0.9965\approx 0.00351$. Posterior odds are prior odds times $12.7$, about $0.0447$, and the posterior probability is about $0.043$. The ratio was moderately large. The prior odds were tiny. The product is still a small probability.{{cite:openintro2019}} (Ch. 3, Example 3.42, pp. 105–106){{cite:gelman_bda2013}} (Ch. 1, p. 8)

## Intuition

Bayes’ theorem in probability form hides a cancellation. Write the odds of “condition present” against “condition absent.” The marginal probability of the data appears in both the numerator and the denominator and drops out. What remains is the prior odds multiplied by $p(y\mid\text{present})/p(y\mid\text{absent})$. That quotient is the likelihood ratio of the observed result. It scores how the result redistributes belief between the two states. It does not contain the base rate, so the same test result has the same likelihood ratio in a screening clinic and in a high-risk clinic. The clinics differ in the prior odds the ratio multiplies.{{cite:gelman_bda2013}} (Ch. 1, p. 8)

## Definition

For two states $\omega_1$ and $\omega_2$ and an observed result $y$, the likelihood ratio of $y$ for $\omega_1$ against $\omega_2$ is $p(y\mid\omega_1)/p(y\mid\omega_2)$. Posterior odds equal prior odds times this ratio:

$$
\frac{p(\omega_1\mid y)}{p(\omega_2\mid y)}=\frac{p(\omega_1)}{p(\omega_2)}\cdot\frac{p(y\mid\omega_1)}{p(y\mid\omega_2)}.
$$

In diagnostic testing, $\omega_1$ is “condition present,” $\omega_2$ is “condition absent,” and $y$ is the test result. For a positive result, $p(y\mid\omega_1)$ is the sensitivity and $p(y\mid\omega_2)$ is the false-positive rate, one minus the specificity. Their quotient is the likelihood ratio of a positive test. For a negative result the numerator is the false-negative rate and the denominator is the specificity.{{cite:gelman_bda2013}} (Ch. 1, p. 8){{cite:openintro2019}} (Ch. 3, Example 3.42, pp. 105–106)

This ratio is not the likelihood-ratio statistic used to compare two parameter values inside a parametric model by maximising a likelihood. The diagnostic ratio is a ratio of two sampling probabilities for one observed test result, under two states of the patient.{{cite:gelman_bda2013}} (Ch. 1, p. 8)

## Properties

A likelihood ratio of $1$ leaves the odds unchanged. A ratio above $1$ raises the odds of the condition; a ratio below $1$ lowers them. Because sensitivity and the false-positive rate are both probabilities, the positive likelihood ratio is at most $1/\alpha$ when the false-positive rate is $\alpha$, and it is large when a positive result is rare among people without the condition. The mammogram’s positive ratio $0.89/0.07\approx 12.7$ is modest beside ratios in the hundreds, which is why a low base rate still dominates the posterior.{{cite:openintro2019}} (Ch. 3, Example 3.42, pp. 105–106){{cite:gelman_bda2013}} (Ch. 1, p. 8)

The bronchoscopy figures give a sharper positive ratio and a negative ratio below one. Detection probability $0.70$ and false-positive probability $0.02$ yield a positive likelihood ratio $0.70/0.02=35$. A negative result has probability $0.30$ if cancer is present and $0.98$ if it is not, so the negative likelihood ratio is $0.30/0.98\approx 0.306$. Starting from prior odds $0.9/0.1=9$, a positive result moves the odds to $9\times 35=315$, hence a probability $315/316\approx 0.997$. A negative result moves the odds to $9\times 0.306\approx 2.76$, hence a probability $2.76/3.76\approx 0.73$. Those are the posteriors obtained from the probability form of Bayes’ theorem in the same example. The likelihood ratio is the bookkeeping that makes the multiplication visible.{{cite:gelman_bda2013}} (Ch. 9, §9.3, pp. 245–246; Ch. 1, p. 8)

The positive predictive value is a probability, not a likelihood ratio. It folds the base rate in. Two populations with the same likelihood ratio and different base rates have different predictive values and the same likelihood ratio.{{cite:openintro2019}} (Ch. 3, Example 3.42, pp. 105–106)

## Statistical use

Report the likelihood ratio of the result that was observed, and report the prior odds separately. A positive ratio near $1$ will not move a decision. A large positive ratio still leaves a small posterior probability when the prior odds are small enough, which is the usual screening case. For a negative result, quote the negative ratio rather than repeating the sensitivity. Sequential independent tests multiply likelihood ratios. The posterior odds after two independent results are the prior odds times both ratios, provided the conditional probabilities really do factor.{{cite:gelman_bda2013}} (Ch. 1, p. 8){{cite:openintro2019}} (Ch. 3, §3.2.8, pp. 105–106)

[Sensitivity and specificity](sensitivity-and-specificity.qmd) are the two conditional probabilities in the positive ratio. The [base rate](base-rate.qmd) supplies the prior odds. The [positive predictive value](positive-predictive-value.qmd) is what the product becomes after it is turned back into a probability.

## Worked example

Mammogram: sensitivity $0.89$, false-positive rate $0.07$, base rate $0.0035$. The positive likelihood ratio is $0.89/0.07=12.714$. Prior odds are $0.0035/0.9965=0.003512$. Posterior odds are $12.714\times 0.003512=0.04466$. The posterior probability is $0.04466/(1+0.04466)=0.0427$, matching the direct Bayes calculation that divides $0.0035\times 0.89$ by the marginal probability of a positive test.{{cite:openintro2019}} (Ch. 3, Example 3.42, pp. 105–106){{cite:gelman_bda2013}} (Ch. 1, p. 8)

**Your turn.** Sensitivity is $0.80$, the false-positive rate is $0.10$, and the base rate is $0.20$. Compute the positive likelihood ratio, the prior odds, the posterior odds, and the posterior probability.

::: {.callout-tip collapse="true" title="Answer"}
The likelihood ratio is $0.80/0.10=8$. The prior odds are $0.20/0.80=0.25$. The posterior odds are $8\times 0.25=2$. The posterior probability is $2/(1+2)=2/3\approx 0.667$.
:::

## Common misconceptions

The likelihood ratio is not a probability and need not lie between $0$ and $1$. It is not the positive predictive value. It is not the likelihood-ratio test statistic that compares maximised parametric likelihoods. A large ratio does not mean the condition is probably present: that depends on the prior odds. Quoting only the sensitivity uses the numerator and drops the denominator, which is where a common false positive shrinks the ratio.{{cite:gelman_bda2013}} (Ch. 1, p. 8){{cite:openintro2019}} (Ch. 3, Example 3.42, pp. 105–106)

## Assumptions and limits

The ratio uses conditional probabilities estimated for the same kind of patient and the same decision threshold that will be used in practice. A sensitivity from a study of advanced disease overstates the numerator for early screening. The multiplication into prior odds assumes the two states are the only alternatives being weighed. Independent multiplication across repeated tests fails if the tests share errors. The ratio does not include the harm of the test. Whether to run the test is a decision problem that needs losses as well as this factor.{{cite:openintro2019}} (Ch. 3, Example 3.42, pp. 105–106){{cite:gelman_bda2013}} (Ch. 9, §9.3, pp. 245–246)

## Connections

The [base rate](base-rate.qmd) is converted to prior odds before the ratio is applied. [Prior odds](prior-odds.qmd) are that conversion. [Sensitivity and specificity](sensitivity-and-specificity.qmd) determine the positive and negative ratios. The [positive predictive value](positive-predictive-value.qmd) is the posterior probability, not the ratio. The [fallacy of the transposed conditional](fallacy-of-the-transposed-conditional.qmd) treats a conditional probability of the data given the condition as if it were already the posterior probability, skipping both the ratio’s denominator and the prior odds. A [likelihood-ratio test](likelihood-ratio-test.qmd) is a different construction, aimed at parameters of a statistical model.

## History

Odds made Bayes’ theorem a product. The posterior odds of one state against another equal the prior odds multiplied by the likelihood ratio of the observed data, a form singled out because the marginal probability of the data cancels. Diagnostic calculations are the case in which the two states are “condition present” and “condition absent” and the datum is a test result. A mammogram example with sensitivity $0.89$ and false-positive rate $0.07$ is a ratio near $13$ attached to a very small prior odds. A bronchoscopy example with detection probability $0.70$ and false-positive probability $0.02$ is a ratio of $35$, large enough to push a prior probability of $0.90$ still higher, and the matching negative ratio pulls a prior of $0.90$ down only to about $0.73$. The ratio is the part of that arithmetic that belongs to the test. The base rate is the part that belongs to the population.{{cite:gelman_bda2013}} (Ch. 1, p. 8; Ch. 9, §9.3, pp. 245–246){{cite:openintro2019}} (Ch. 3, Example 3.42, pp. 105–106)
