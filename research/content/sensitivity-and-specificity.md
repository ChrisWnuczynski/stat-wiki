## Motivating example
A screening procedure can detect most affected cases while also producing many false alarms in a population where the condition is rare. Sensitivity and specificity describe the two conditional success rates of a binary test. They must be distinguished from the probability that an individual positive result is a true positive, because that reverses the conditioning and depends on the population prevalence as well.

## Definition — Condition on the reference classification
Let $D$ mean that the target condition is present and $T+$ mean that the test reports positive. Sensitivity is $\Pr(T+\mid D)$ and specificity is $\Pr(T-\mid D^c)$. For a table with true-positive count $a$, false-negative count $b$, false-positive count $c$ and true-negative count $d$, their estimates are
$$\widehat{\mathrm{Se}}=\frac{a}{a+b},\qquad\widehat{\mathrm{Sp}}=\frac{d}{c+d}.$$
Each denominator identifies the cases on which the rate is conditioned. If a denominator is zero, the corresponding rate cannot be estimated from that sample. The table should state which label is positive and how the reference condition was determined.{{cite:fda2007_diagnostic}} (“Sensitivity and specificity”; Appendix, diagnostic accuracy table)

False-negative rate is $1-\mathrm{Se}$ and false-positive rate is $1-\mathrm{Sp}$. If rows are reference classes and columns are test outputs, diagonal row proportions give sensitivity and specificity. Off-diagonal row proportions are their error-rate complements. A table using the reverse orientation contains the same counts but requires the corresponding change in denominator. (Appendix, calculations of sensitivity and specificity)

## Properties — Prevalence enters the reverse conditional probability
Let prevalence be $\pi=\Pr(D)$. The positive predictive value is
$$\Pr(D\mid T+)=\frac{\pi\mathrm{Se}}{\pi\mathrm{Se}+(1-\pi)(1-\mathrm{Sp})},$$
when the denominator is positive. This follows by dividing the joint true-positive probability by the total positive probability. Similarly,
$$\Pr(D^c\mid T-)=\frac{(1-\pi)\mathrm{Sp}}{(1-\pi)\mathrm{Sp}+\pi(1-\mathrm{Se})}.$$
These identities are applications of Bayes' rule, not definitions of sensitivity or specificity. A population with different prevalence can have different predictive values even if the two conditional test rates transfer exactly.{{cite:openintro2019}} (§3.2.8, pp. 104–106, Bayes' theorem){{cite:gelman_bda2013}} (Ch. 1, p. 8)

For a threshold on a score where larger values are called positive, raising the threshold cannot increase the number of positive calls on a fixed sample. Sensitivity is therefore non-increasing and specificity is non-decreasing, allowing flat portions when no scores lie between two cuts. The particular balance should reflect the intended use and the consequences of the two error types.

## Worked example — Separate the two row rates from predictive value
Suppose a study contains 50 affected cases and 200 unaffected cases. The test detects 40 affected cases and falsely calls 10 unaffected cases positive. Its sensitivity is $40/50=0.80$, specificity is $190/200=0.95$, and overall accuracy is $230/250=0.92$. Positive predictive value in this study is $40/(40+10)=0.80$. The equality of sensitivity and positive predictive value here is a numerical coincidence: their denominators refer to different sets of cases.

If prevalence in a target population is $0.01$ and the two conditional rates transfer, the expected positive fraction is $0.01(0.80)+0.99(0.05)=0.0575$. Positive predictive value is then $0.008/0.0575=0.139130$. Among 10,000 representative cases, the corresponding expected counts are 80 true positives and 495 false positives. This is a hypothetical probability calculation, rather than an empirical claim about a particular clinical test.

**Your turn.** With the same sensitivity and specificity but prevalence one half, what is positive predictive value?

::: {.callout-tip collapse="true" title="Answer"}
It is 0.4/(0.4+0.025)=16/17=0.941176. The higher prevalence changes the relative numbers of true and false positives.
:::

## Statistical use — Validate the reference and the study population
Estimates from a study are uncertain because they use finitely many cases. Confidence intervals should reflect the appropriate denominators for the two conditional rates. Reporting only a combined accuracy can hide a poor sensitivity when unaffected cases dominate the sample. Likewise, a case-control study can estimate conditional rates without directly reproducing target-population predictive values through its artificially chosen case fraction.

A flawed reference standard can bias estimated performance, and a different spectrum of affected or unaffected cases can change the conditional rates themselves. Treating sensitivity and specificity as prevalence-free algebraic definitions does not establish that they are constant across populations. The transfer assumption belongs to the study design and the intended-use setting.

## Common misconceptions — A negative result does not prove absence
Specificity conditions on absence of the condition; it is not the probability of absence after a negative result. Likewise, sensitivity conditions on presence, rather than on a positive test output. Writing the two events on the correct sides of the conditioning bar prevents this reversal and makes the role of prevalence explicit.{{cite:openintro2019}} (§3.2, p. 95; §3.2.8, pp. 104–106, conditional probability and Bayes' theorem){{cite:gelman_bda2013}} (Ch. 1, p. 8)

## Intuition — The same conditional rates support very different predictive values
With sensitivity $0.80$ and specificity $0.95$, prevalence $0.01$ gives positive predictive value $0.139130$. Prevalence one half gives $0.4/(0.4+0.025)=0.941176$. Write the positive predictive value as $\pi a/(\pi a+(1-\pi)b)$ with $a=0.80$ and false-positive rate $b=0.05$. Its derivative with respect to $\pi$ has numerator proportional to $ab$, so the value increases with prevalence when both rates are positive. At prevalence $0.01$ the negative predictive value is $(0.99\times0.95)/(0.99\times0.95+0.01\times0.20)=0.9405/0.9425=0.997878$. A negative result is then very likely to be a true negative largely because the condition is rare. Quoting $0.997878$ as if it were the specificity would swap a joint calculation for a row rate.{{cite:gelman_bda2013}} (Ch. 1, p. 8)

A study with no reference-positive cases has $a+b=0$. The sensitivity ratio is undefined, whatever the test called on the reference-negative cases. A study with no reference-negative cases leaves specificity undefined. Overall accuracy can still be computed when the table is nonempty, and that single ratio then describes only the class that was observed. The two conditional rates require their own denominators.{{cite:fda2007_diagnostic}} (“Sensitivity and specificity”; Appendix, diagnostic accuracy table)

## Interpretation — A higher threshold moves the two row rates in opposite directions
On a fixed sample, raising a positive-call threshold can only keep or reduce the set of positive calls. Every case that stays positive was already positive, so false positives do not increase and specificity does not fall. True positives do not increase, so sensitivity does not rise. Either rate can stay constant when no score lies strictly between the old and new cuts. The worked test detected $40$ of $50$ affected cases. A stricter cut that misses five of those detections lowers sensitivity from $0.80$ to $35/50=0.70$ and, if it also removes some of the $10$ false positives, raises specificity. The two changes are linked by the threshold and are still separate rows of the table.

## Connections
The positive predictive value is the probability that the condition is present after a positive call. It is the quantity a [base rate](base-rate.qmd) changes when the conditional rates are held fixed. Sensitivity and specificity are the conditional rates. A screening programme and a clinic can share those rates in a calculation and still produce different predictive values, because the people who arrive already differ in prevalence.{{cite:gelman_bda2013}} (Ch. 1, p. 8)
