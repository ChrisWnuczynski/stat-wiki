## Lead context

A screening test finds a condition in a person drawn from a population where the condition is rare. The chance the person truly has it, given the positive result, is not the sensitivity of the test. It depends on how common the condition was before the test was read. That prior probability is the base rate. Leave it out, and a sensitive test is mistaken for a very informative positive result.{{cite:openintro2019}} (Ch. 3, §3.2.8){{cite:gelman_bda2013}} (Ch. 1, p. 8)

## Motivating example

In Canada, about \(0.35\%\) of women over 40 develop breast cancer in a given year. A mammogram misses about \(11\%\) of cancers, so the sensitivity is about \(0.89\), and it raises a false alarm for about \(7\%\) of women without cancer. Among positive mammograms, the probability of cancer is about \(0.04\). Most positive results in this population are false alarms, because the base rate \(0.0035\) is so low that the many healthy women produce more false positives than the few cases produce true positives. The same test, read in a clinic where the condition is common, has a much higher positive predictive value. The test characteristics did not change. The base rate did.{{cite:openintro2019}} (Ch. 3, §3.2.8)

## Intuition

Bayes' theorem mixes two kinds of number. One kind describes the test: the probability of a positive result if the condition is present, and if it is absent. The other kind describes the population: the probability of the condition before the result is known. The second number weights how many people of each kind the test will see. A rare condition means the positive column of a large sample is dominated by false positives unless the false-positive rate is tiny beside the base rate.{{cite:openintro2019}} (Ch. 3, §3.2.8)

In odds form the same weighting is multiplication. The prior odds of the condition against its absence are the base rate divided by one minus the base rate. The data multiply those odds by the likelihood ratio \(p(y\mid\text{present})/p(y\mid\text{absent})\). A base rate near zero is a prior odds near zero, and the likelihood ratio has to be large before the posterior odds become large. Gelman and coauthors write the identity as posterior odds equal to prior odds times the likelihood ratio. The base rate is the whole of the prior factor.{{cite:gelman_bda2013}} (Ch. 1, p. 8)

## Definition

The base rate of a condition is its probability in the population to which the test is applied, before the test result is taken into account. In the notation of Bayes' theorem it is the marginal probability of the outcome "condition present," as distinct from the conditional probabilities that describe the test result given each state. Applying the theorem starts by identifying that marginal probability. If \(p\) is the base rate, the prior odds are \(p/(1-p)\). Sensitivity and specificity do not contain \(p\).{{cite:openintro2019}} (Ch. 3, §3.2.8){{cite:gelman_bda2013}} (Ch. 1, p. 8)

The [fallacy of the transposed conditional](fallacy-of-the-transposed-conditional.qmd) is the habit of quoting a conditional probability in the wrong direction. Neglect of the base rate is how that habit becomes a number: the conditional probability of a positive test given the condition is treated as if it were the conditional probability of the condition given a positive test.

## Properties

With sensitivity \(1-\beta\) and false-positive rate \(\alpha\), the positive predictive value is
\[
P(\text{present}\mid\text{positive})=\frac{p(1-\beta)}{p(1-\beta)+(1-p)\alpha}.
\]
It increases in the base rate \(p\) when the test is better than a coin toss in the sense \(1-\beta>\alpha\). At \(p=0.0035\), \(1-\beta=0.89\), and \(\alpha=0.07\), the joint probability of cancer and a positive test is \(0.0035\times 0.89=0.003115\). The probability of a positive test is \(0.003115+0.9965\times 0.07=0.07287\). The positive predictive value is \(0.003115/0.07287\approx 0.0427\), about \(4\%\), which is the figure OpenIntro reports for this screening problem. The denominator is dominated by \((1-p)\alpha\).{{cite:openintro2019}} (Ch. 3, §3.2.8)

Raise the base rate to \(0.20\) and leave the test unchanged:
\[
\frac{0.20\times 0.89}{0.20\times 0.89+0.80\times 0.07}=\frac{0.178}{0.234}\approx 0.761.
\]
The test did not improve. The population did. A third base rate, \(p=0.01\), with sensitivity \(0.90\) and false-positive rate \(0.05\), gives numerator \(0.009\) and denominator \(0.009+0.99\times 0.05=0.0585\), so the positive predictive value is \(0.009/0.0585\approx 0.154\). One percent prevalence and a five percent false-positive rate still leave most positives false.{{cite:openintro2019}} (Ch. 3, §3.2.8)

The base rate is not a property of the device. The same likelihood ratio attached to a screening base rate of \(0.0035\) leaves the posterior small, and the same ratio attached to a high clinical probability leaves it large. Quoting a test's sensitivity without the base rate quotes the factor that does not contain the population weight.

## Worked example

For the mammogram figures, \(p=0.0035\), sensitivity \(0.89\), and false-positive rate \(0.07\). The positive predictive value is \(0.003115/0.07287\approx 0.0427\). Replacing the base rate by \(0.20\) gives approximately \(0.761\), as above.{{cite:openintro2019}} (Ch. 3, §3.2.8)

**Your turn.** A condition has base rate \(0.01\). The test has sensitivity \(0.90\) and false-positive rate \(0.05\). Compute the positive predictive value.

::: {.callout-tip collapse="true" title="Answer"}
The numerator is \(0.01\times 0.90=0.009\). The denominator is \(0.009+0.99\times 0.05=0.0585\). The positive predictive value is \(0.009/0.0585\approx 0.1538\).
:::

## Assumptions and limits

The calculation assumes that the base rate is the probability for the person being tested, not a rate from a different population, and that the sensitivity and the false-positive rate apply to this test and this spectrum of disease. A rate from a screening programme is the wrong weight for a ward of already suspected cases, and the clinic rate is the wrong weight in a screening programme. Dependence between repeated tests, or a base rate that itself depends on unrecorded symptoms, changes the arithmetic. If the base rate is uncertain, the predictive value can be recomputed on a small grid of rates. The formula does not supply a base rate the study did not measure.{{cite:openintro2019}} (Ch. 3, §3.2.8){{cite:gelman_bda2013}} (Ch. 1, p. 8)

## Connections

The [positive predictive value](positive-predictive-value.qmd) and the [negative predictive value](negative-predictive-value.qmd) are the two posterior probabilities a base rate feeds. A [likelihood ratio in diagnostic testing](likelihood-ratios-in-diagnostic-testing.qmd) is the factor that multiplies the prior odds. The [fallacy of the transposed conditional](fallacy-of-the-transposed-conditional.qmd) is what it looks like to ignore the base rate and read a conditional probability backwards. [Prior odds](prior-odds.qmd) are the base rate in odds form, \(p/(1-p)\). [Sensitivity and specificity](sensitivity-and-specificity.qmd) are the conditional performance of the test and do not include the base rate.{{cite:gelman_bda2013}} (Ch. 1, p. 8){{cite:openintro2019}} (Ch. 3, §3.2.8)
