## Lead context

A positive test is more common among people who have a condition than among people who do not. The likelihood ratio of that result is how many times more common. Multiplied by the prior odds of the condition, it gives the posterior odds. Sensitivity alone does not. The ratio uses both the true-positive rate and the false-positive rate, and the base rate stays outside it, in the prior odds. {{cite:gelman_bda2013}} (Ch. 1, §1.3, p. 8) {{cite:openintro2019}} (Ch. 3, §3.2.8)

## Motivating example

In Canada, about 0.35 percent of women over 40 develop breast cancer in a given year. A mammogram gives a false negative in about 11 percent of women who have cancer, so the sensitivity is \(1-0.11=0.89\). It gives a false positive in 7 percent of women who do not. A positive mammogram is therefore \(0.89/0.07\approx 12.7\) times as likely if cancer is present as if it is not. In a population where the base rate is \(0.0035\), the prior odds are about \(0.0035/0.9965\approx 0.00351\). Posterior odds are prior odds times \(12.7\), about \(0.0447\), and the posterior probability is about \(0.043\). The ratio was moderately large. The prior odds were tiny. The product is still a small probability. OpenIntro’s direct calculation gives the same conclusion: \(0.0035\times 0.89=0.00312\), the marginal probability of a positive test is \(0.07288\), and \(0.00312/0.07288\approx 0.0428\). {{cite:openintro2019}} (Ch. 3, §3.2.8) {{cite:gelman_bda2013}} (Ch. 1, §1.3, p. 8)

## Intuition

Bayes’ theorem in odds form is a product. The posterior odds of one state against another equal the prior odds multiplied by the likelihood ratio \(p(y\mid\omega_1)/p(y\mid\omega_2)\). The marginal probability of the data cancels, which is why the ratio, and not the two conditional probabilities separately, is the factor the test contributes. A ratio of 1 leaves the odds unchanged. A ratio above 1 raises the odds of the condition. A ratio below 1 lowers them. The base rate never enters the ratio. It enters the prior odds. Two populations with the same test and different base rates share the likelihood ratio and do not share the posterior probability. {{cite:gelman_bda2013}} (Ch. 1, §1.3, p. 8)

## Definition

In diagnostic testing, \(\omega_1\) is “condition present,” \(\omega_2\) is “condition absent,” and \(y\) is the test result. For a positive result, \(p(y\mid\omega_1)\) is the sensitivity and \(p(y\mid\omega_2)\) is the false-positive rate, one minus the specificity. Their quotient is the positive likelihood ratio. For a negative result the numerator is the false-negative rate and the denominator is the specificity. The posterior odds are
\[
\frac{P(\omega_1\mid y)}{P(\omega_2\mid y)}=\frac{P(\omega_1)}{P(\omega_2)}\cdot\frac{p(y\mid\omega_1)}{p(y\mid\omega_2)}.
\]
The posterior probability is the posterior odds divided by one plus the posterior odds. {{cite:gelman_bda2013}} (Ch. 1, §1.3, p. 8) {{cite:openintro2019}} (Ch. 3, §3.2.8)

The bronchoscopy figures in Gelman’s decision analysis give a sharper positive ratio. Detection probability \(0.70\) and false-positive probability \(0.02\) yield a positive likelihood ratio \(0.70/0.02=35\). A negative result has probability \(0.30\) if cancer is present and \(0.98\) if it is not, so the negative likelihood ratio is \(0.30/0.98\). Starting from prior probability \(0.90\), prior odds \(9\), a positive result moves the probability to
\[
\frac{0.9\cdot 0.7}{0.9\cdot 0.7+0.1\cdot 0.02}=0.997.
\]
A negative result moves it to
\[
\frac{0.9\cdot 0.3}{0.9\cdot 0.3+0.1\cdot 0.98}=0.734.
\]
The likelihood ratio is the factor that makes that update a multiplication. The decision of whether to run the test is a further question: it needs the losses, not only the updated probability. {{cite:gelman_bda2013}} (Ch. 9, §9.3, pp. 245–246)

## Statistical use

Report the likelihood ratio of the result that was observed, and report the prior odds separately. A positive ratio near \(1\) will not move a decision. A large positive ratio still leaves a small posterior probability when the prior odds are small enough, which is the usual screening case. OpenIntro’s mammogram is that case: doctors often run more tests after a first positive result, because a rare condition and an imperfect test leave the posterior probability near 4 percent. For a negative result, quote the negative ratio rather than repeating the sensitivity. Sequential independent updates multiply likelihood ratios. Gelman’s hemophilia calculation is the same arithmetic on a different datum: prior odds \(1\), likelihood ratio \(0.25\) from two unaffected sons, posterior odds \(0.25\). A third observation uses the previous posterior as the next prior. The multiplication is valid when the conditional probabilities factor. {{cite:openintro2019}} (Ch. 3, §3.2.8) {{cite:gelman_bda2013}} (Ch. 1, §1.3–1.4, pp. 8–9)

## Worked example

Mammogram: sensitivity \(0.89\), false-positive rate \(0.07\), base rate \(0.0035\). The positive likelihood ratio is \(0.89/0.07=12.714\). Prior odds are \(0.0035/0.9965=0.003512\). Posterior odds are \(12.714\times 0.003512=0.04466\). The posterior probability is \(0.04466/(1+0.04466)=0.0427\), matching the direct Bayes calculation that divides \(0.0035\times 0.89\) by the marginal probability of a positive test. {{cite:openintro2019}} (Ch. 3, §3.2.8) {{cite:gelman_bda2013}} (Ch. 1, §1.3, p. 8)

**Your turn.** Sensitivity is \(0.80\), the false-positive rate is \(0.10\), and the base rate is \(0.20\). Compute the positive likelihood ratio, the prior odds, the posterior odds, and the posterior probability.

::: {.callout-tip collapse="true" title="Answer"}
The likelihood ratio is \(0.80/0.10=8\). The prior odds are \(0.20/0.80=0.25\). The posterior odds are \(8\times 0.25=2\). The posterior probability is \(2/(1+2)=2/3\).
:::

## Common misconceptions

The likelihood ratio is not a probability and need not lie between 0 and 1. It is not the positive predictive value. The predictive value folds the base rate in. It is not the likelihood-ratio test statistic that compares maximised parametric likelihoods. A large ratio does not mean the condition is probably present. That depends on the prior odds. Quoting only the sensitivity uses the numerator and drops the denominator, which is where a common false positive shrinks the ratio. {{cite:gelman_bda2013}} (Ch. 1, §1.3, p. 8) {{cite:openintro2019}} (Ch. 3, §3.2.8)

The ratio uses conditional probabilities for the same kind of patient and the same decision threshold that will be used in practice. A sensitivity from a study of advanced disease overstates the numerator for early screening. The multiplication into prior odds assumes the two states are the only alternatives being weighed. Independent multiplication across repeated tests fails if the tests share errors. The ratio does not include the harm of the test. In the bronchoscopy example the updated probabilities, positive or negative, did not change the preferred treatment, and the test itself carried a risk. Whether to run the test is a decision problem that needs losses as well as this factor. {{cite:gelman_bda2013}} (Ch. 9, §9.3, pp. 245–246) {{cite:openintro2019}} (Ch. 3, §3.2.8)

## Connections

[Bayes’ rule](bayes-rule.qmd) is the inversion that turns the likelihood ratio and the prior odds into a posterior. A [base rate](base-rate.qmd) is the prior probability that the ratio deliberately leaves out. [Posterior probability](posterior-probability.qmd) is what the odds are converted back into. A [likelihood-ratio test](likelihood-ratio-test.qmd) is a different object: a comparison of maximised likelihoods inside a parametric model, not the diagnostic factor \(p(y\mid\omega_1)/p(y\mid\omega_2)\). The mammogram arithmetic and the bronchoscopy arithmetic are the diagnostic factor. The name is shared. The calculation is not. {{cite:gelman_bda2013}} (Ch. 1, §1.3, p. 8; Ch. 9, §9.3, p. 246) {{cite:openintro2019}} (Ch. 3, §3.2.8)
