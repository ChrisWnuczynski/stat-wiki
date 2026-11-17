

## Lead context

A screening test finds a disease in a woman drawn from a population where the disease is rare. The chance she truly has it, given the positive result, is not the sensitivity of the test. It depends on how common the disease was before the test was read. That prior probability is the base rate. Leave it out, and a very sensitive test is mistaken for a very informative positive result.{{cite:openintro2019}} (Ch. 3, §3.2.8){{cite:gelman_bda2013}} (Ch. 1, p. 8)

## Motivating example

In Canada, about $0.35\%$ of women over 40 develop breast cancer in a given year. A mammogram misses about $11\%$ of cancers and raises a false alarm for about $7\%$ of women without cancer. Among positive mammograms, the probability of cancer is about $0.043$. Most positive results in this population are false alarms, not because the test is careless, but because the base rate $0.0035$ is so low that the many healthy women produce more false positives than the few cases produce true positives. The same test, read in a clinic where the condition is common, would have a much higher positive predictive value. The test characteristics did not change. The base rate did.{{cite:openintro2019}} (Ch. 3)

## Intuition

Bayes’ theorem mixes two kinds of number. One kind describes the test: the probability of a positive result if the condition is present, and if it is absent. The other kind describes the population: the probability of the condition before the result is known. The second number weights how many people of each kind the test will see. A rare condition means the positive column of a large sample is dominated by false positives unless the false-positive rate is tiny beside the base rate.{{cite:openintro2019}} (Ch. 3, §3.2.8)

In odds form the same weighting is multiplication. The prior odds of the condition against its absence are the base rate divided by one minus the base rate. The data multiply those odds by a likelihood ratio. A base rate near zero is a prior odds near zero, and a likelihood ratio has to be enormous before the posterior odds become large.{{cite:gelman_bda2013}} (Ch. 1, p. 8)

## Definition

The base rate of a condition is its probability in the population to which the test is applied, before the test result is taken into account. In the notation of Bayes’ theorem it is the marginal probability $P(A_1)$ of the outcome “condition present,” as distinct from the conditional probabilities $P(B\mid A_1)$ and $P(B\mid A_2)$ that describe the test result $B$ given each state. Applying the theorem starts by identifying those marginal probabilities.{{cite:openintro2019}} (Ch. 3, §3.2.8)

If $p$ is the base rate, the prior odds of the condition are $p/(1-p)$. After a result $y$, the posterior odds equal those prior odds times the likelihood ratio $p(y\mid\text{present})/p(y\mid\text{absent})$. The base rate is the whole of the prior factor. Sensitivity and specificity do not contain it.{{cite:gelman_bda2013}} (Ch. 1, p. 8){{cite:openintro2019}} (Ch. 3, §3.2.8)

The [fallacy of the transposed conditional](fallacy-of-the-transposed-conditional.qmd) is the habit of quoting a conditional probability in the wrong direction. Neglect of the base rate is how that habit becomes a number: the conditional probability of a positive test given the condition is treated as if it were the conditional probability of the condition given a positive test, which is true only for special base rates.{{cite:openintro2019}} (Ch. 3)

When a positive predictive value, a posterior probability, or a decision about a test is reported, state the base rate that was used, and say which population it refers to. A rate from a screening programme is not the rate in a ward of already suspected cases. If the base rate is uncertain, recompute the predictive value on a small grid of rates. The grid is the sensitivity analysis. A single impressive sensitivity is not a substitute for it.{{cite:openintro2019}} (Ch. 3){{cite:gelman_bda2013}} (Ch. 9, §9.3, p. 245)

The [positive predictive value](positive-predictive-value.qmd) is the probability of the condition given a positive result, and it is the function of the base rate displayed above. [Prior odds](prior-odds.qmd) are the base rate converted to an odds. [Sensitivity and specificity](sensitivity-and-specificity.qmd) are the conditional performance of the test and do not include the base rate.

The base rate is not the sensitivity and not the positive predictive value. It is not updated by one patient’s result when one is describing the population the next patient will be drawn from; the updated number is that patient’s posterior probability. A base rate taken from a specialist clinic is the wrong weight for a screening programme, and the screening rate is the wrong weight in the clinic. Dropping the base rate and reading the sensitivity as a predictive value is a mistake about two different conditional probabilities. The base rate is the missing weight, not the name of the mistake.{{cite:openintro2019}} (Ch. 3, §3.2.8)

Bayes’ theorem is the eighteenth-century rule that puts a marginal probability and a conditional probability together. Screening arithmetic made the marginal probability impossible to skip: a worked mammogram problem with a base rate of $0.35\%$ yields a positive predictive value near $4\%$, which is the numerical content of the warning that a rare condition floods the positive results with false alarms. Odds form writes the same fact as a product, prior odds times likelihood ratio, and makes the base rate the prior factor rather than a detail of the test. Clinical decision calculations use the same split when they start from a stated probability that the condition is present, such as $0.90$ for a suspected malignancy, and only then fold in what a further test would show.{{cite:openintro2019}} (Ch. 3, §3.2.8){{cite:gelman_bda2013}} (Ch. 1, p. 8; Ch. 9, §9.3, p. 245)

## Properties

With sensitivity $1-\beta$ and false-positive rate $\alpha$, the positive predictive value is

$$
P(\text{present}\mid\text{positive})=\frac{p(1-\beta)}{p(1-\beta)+(1-p)\alpha}.
$$

It is increasing in the base rate $p$ when the test is better than a coin toss in the sense $1-\beta>\alpha$. At $p=0.0035$, $1-\beta=0.89$, and $\alpha=0.07$, the denominator is dominated by $(1-p)\alpha$, and the predictive value is about $0.043$. Raise $p$ and the same fraction climbs, because the numerator and the true-positive part of the denominator both gain weight.{{cite:openintro2019}} (Ch. 3)

The base rate is not a property of the device. A bronchoscopy example with a prior probability $0.90$ that a tumour is malignant is a high base rate, and the posterior probability after a negative test remains $0.73$. The same likelihood ratio attached to a screening base rate of $0.0035$ would leave the posterior small. Quoting a test’s sensitivity without the base rate quotes the wrong factor.{{cite:gelman_bda2013}} (Ch. 9, §9.3, pp. 245–246){{cite:openintro2019}} (Ch. 3, §3.2.8)

## Worked example

For the mammogram figures, $p=0.0035$, $P(\text{positive}\mid\text{cancer})=0.89$, and $P(\text{positive}\mid\text{no cancer})=0.07$. The joint probability of cancer and a positive test is $0.0035\times 0.89=0.003115$. The probability of a positive test is $0.003115+0.9965\times 0.07=0.07287$. The positive predictive value is $0.003115/0.07287\approx 0.0427$. The base rate entered only as $0.0035$. Replacing it by $0.20$, and leaving the test unchanged, gives

$$
\frac{0.20\times 0.89}{0.20\times 0.89+0.80\times 0.07}=\frac{0.178}{0.234}\approx 0.761.
$$

The test did not improve. The population did.{{cite:openintro2019}} (Ch. 3)

**Your turn.** A condition has base rate $0.01$. The test has sensitivity $0.90$ and false-positive rate $0.05$. Compute the positive predictive value.

::: {.callout-tip collapse="true" title="Answer"}
The numerator is $0.01\times 0.90=0.009$. The denominator is $0.009+0.99\times 0.05=0.0585$. The positive predictive value is $0.009/0.0585=0.1538$, about $15\%$. One percent prevalence and a five percent false-positive rate still leave most positives false.
:::

## Assumptions and limits

The calculation assumes that the base rate is the probability for the person being tested, not a rate from a different population, and that the sensitivity and false-positive rate were estimated in a way that applies to this test and this spectrum of disease. Dependence between tests, or a base rate that itself depends on unrecorded symptoms, changes the arithmetic. A base rate of uncertain provenance should be shown as a range. The formula does not manufacture a base rate the study did not measure.{{cite:openintro2019}} (Ch. 3, §3.2.8){{cite:gelman_bda2013}} (Ch. 9, §9.3, p. 245)

## Connections

The [positive predictive value](positive-predictive-value.qmd) and the [negative predictive value](negative-predictive-value.qmd) are the two posterior probabilities a base rate feeds. A [likelihood ratio in diagnostic testing](likelihood-ratios-in-diagnostic-testing.qmd) is the factor that multiplies the prior odds. The [fallacy of the transposed conditional](fallacy-of-the-transposed-conditional.qmd) is what it looks like to ignore the base rate and read a conditional probability backwards. [Prior odds](prior-odds.qmd) are the base rate in odds form.
