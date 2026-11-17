## Motivating example
A screening procedure can detect most affected cases while also producing many false alarms in a population where the condition is rare. Sensitivity and specificity describe the two conditional success rates of a binary test. They must be distinguished from the probability that an individual positive result is a true positive, because that reverses the conditioning and depends on the population prevalence as well.{{cite:fda2007_diagnostic}} (“General Guidance”, “Measures that describe diagnostic accuracy”)

## Definition — Condition on the reference classification
Let $D$ mean that the target condition is present and $T+$ mean that the test reports positive. Sensitivity is $\Pr(T+\mid D)$ and specificity is $\Pr(T-\mid D^c)$. For a table with true-positive count $a$, false-negative count $b$, false-positive count $c$ and true-negative count $d$, their estimates are
$$\widehat{\mathrm{Se}}=\frac{a}{a+b},\qquad\widehat{\mathrm{Sp}}=\frac{d}{c+d}.$$
Each denominator identifies the cases on which the rate is conditioned. If a denominator is zero, the corresponding rate cannot be estimated from that sample. The table should state which label is positive and how the reference condition was determined.{{cite:fda2007_diagnostic}} (“Sensitivity and specificity”; Appendix, diagnostic accuracy table)

False-negative rate is $1-\mathrm{Se}$ and false-positive rate is $1-\mathrm{Sp}$. If rows are reference classes and columns are test outputs, diagonal row proportions give sensitivity and specificity. Off-diagonal row proportions are their error-rate complements. A table using the reverse orientation contains the same counts but requires the corresponding change in denominator.{{cite:fda2007_diagnostic}} (Appendix, calculations of sensitivity and specificity)

## Properties — Prevalence enters the reverse conditional probability
Let prevalence be $\pi=\Pr(D)$. The positive predictive value is
$$\Pr(D\mid T+)=\frac{\pi\mathrm{Se}}{\pi\mathrm{Se}+(1-\pi)(1-\mathrm{Sp})},$$
when the denominator is positive. This follows by dividing the joint true-positive probability by the total positive probability. Similarly,
$$\Pr(D^c\mid T-)=\frac{(1-\pi)\mathrm{Sp}}{(1-\pi)\mathrm{Sp}+\pi(1-\mathrm{Se})}.$$
These identities are applications of Bayes' rule, not definitions of sensitivity or specificity. A population with different prevalence can have different predictive values even if the two conditional test rates transfer exactly.{{cite:openintro2019}} (Chapter 3, “Conditional probability”, “Bayes' Theorem”)

For a threshold on a score where larger values are called positive, raising the threshold cannot increase the number of positive calls on a fixed sample. Sensitivity is therefore non-increasing and specificity is non-decreasing, allowing flat portions when no scores lie between two cuts. The particular balance should reflect the intended use and the consequences of the two error types.{{cite:fda2007_diagnostic}} (“Measures that describe diagnostic accuracy”, ROC analysis and intended use)

## Worked example — Separate the two row rates from predictive value
Suppose a study contains 50 affected cases and 200 unaffected cases. The test detects 40 affected cases and falsely calls 10 unaffected cases positive. Its sensitivity is $40/50=0.80$, specificity is $190/200=0.95$, and overall accuracy is $230/250=0.92$. Positive predictive value in this study is $40/(40+10)=0.80$. The equality of sensitivity and positive predictive value here is a numerical coincidence: their denominators refer to different sets of cases.

If prevalence in a target population is $0.01$ and the two conditional rates transfer, the expected positive fraction is $0.01(0.80)+0.99(0.05)=0.0575$. Positive predictive value is then $0.008/0.0575=0.139130$. Among 10,000 representative cases, the corresponding expected counts are 80 true positives and 495 false positives. This is a hypothetical probability calculation, rather than an empirical claim about a particular clinical test.

**Your turn.** With the same sensitivity and specificity but prevalence one half, what is positive predictive value?

::: {.callout-tip collapse="true" title="Answer"}
It is 0.4/(0.4+0.025)=16/17=0.941176. The higher prevalence changes the relative numbers of true and false positives.
:::

## Statistical use — Validate the reference and the study population
Estimates from a study are uncertain because they use finitely many cases. Confidence intervals should reflect the appropriate denominators for the two conditional rates. Reporting only a combined accuracy can hide a poor sensitivity when unaffected cases dominate the sample. Likewise, a case-control study can estimate conditional rates without directly reproducing target-population predictive values through its artificially chosen case fraction.{{cite:fda2007_diagnostic}} (“Sensitivity and specificity”, statistical uncertainty; “Study population”)

A flawed reference standard can bias estimated performance, and a different spectrum of affected or unaffected cases can change the conditional rates themselves. Treating sensitivity and specificity as prevalence-free algebraic definitions does not establish that they are constant across populations. The transfer assumption belongs to the study design and the intended-use setting.{{cite:fda2007_diagnostic}} (“Reference standard”; “Bias”; “Intended use population”)

## Common misconceptions — A negative result does not prove absence
Specificity conditions on absence of the condition; it is not the probability of absence after a negative result. Likewise, sensitivity conditions on presence, rather than on a positive test output. Writing the two events on the correct sides of the conditioning bar prevents this reversal and makes the role of prevalence explicit.{{cite:openintro2019}} (Chapter 3, “Defining conditional probability” and “Bayes' Theorem”)
