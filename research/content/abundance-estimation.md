## Lead context
A lake is not emptied and counted. A sample of fish is marked and released, and a second sample shows what fraction of the fish still carry marks. Abundance estimation, in this capture–recapture form, turns that fraction into an estimate of how many animals were there.

## Motivating example
Twenty animals are marked and released. A second sample catches fifteen animals, of which five are marked. If the marked animals mixed through the population, and every animal was equally likely to be caught the second time, the marked fraction in the second sample estimates the marked fraction in the population. Five out of fifteen is one third, so the twenty marked animals are about one third of the population, and the population is about sixty.{{cite:krebs2021}} (Ch. 2, pp. 24–25)

## Intuition
The first sample plants a known number of marks. The second sample estimates the proportion of the population that carries them. Dividing the number of marks by that proportion recovers the population size. The same arithmetic is used when the "marks" are names on one list and the second sample is another list: the people on both lists play the role of the recaptures.{{cite:brittain2009}} (§3.1, pp. 23–25){{cite:krebs2021}} (Ch. 2, p. 24)

## Definition
Let \(M\) be the number marked in the first sample, \(C\) the number caught in the second sample, and \(R\) the number of those that are marked. The Petersen estimator of the population size at the time of marking is
\[
\hat N = \frac{CM}{R}.
\]
It equates the marked fraction in the second sample, \(R/C\), to the marked fraction in the population, \(M/N\). In the notation of two lists, if \(n_1\) and \(n_2\) are the counts on each list and \(m_2\) is the number seen on both, the same estimator is \(\hat N = n_1 n_2/m_2\).{{cite:krebs2021}} (Ch. 2, p. 25, eq. 2.1){{cite:brittain2009}} (§3.1)

The ratio \(CM/R\) tends to overestimate \(N\), and the bias is serious in small samples. Seber's form,
\[
\hat N = \frac{(M+1)(C+1)}{R+1}-1,
\]
is the Chapman estimator. It is nearly unbiased when there are at least seven recaptures, and it is the form recommended for sampling without replacement. If the second "sample" is a series of sightings with replacement, Bailey's estimator \(M(C+1)/(R+1)\) is the nearby alternative.{{cite:krebs2021}} (Ch. 2, p. 25, eqs. 2.2–2.3)

## Properties
The Petersen estimate is undefined when \(R=0\): a second sample with no marks does not yield a finite ratio. The Chapman form remains defined at \(R=0\), and it is less sensitive to a zero overlap. Under independence of two sources, the unseen count is estimated by \(\widehat{f_{00}}=f_{10}f_{01}/f_{11}\), and adding the three observed cells to that unseen count recovers \(n_1 n_2/m_2\). A [confidence interval](confidence-interval.qmd) is part of the estimate. With few recaptures the interval is wide: in one artificial population of \(1000\), with \(400\) marked and second samples of \(50\), replicate Petersen estimates ran from below \(705\) to above \(1570\).{{cite:krebs2021}} (Ch. 2, pp. 25–28){{cite:brittain2009}} (§3.1)

## Statistical use
Wildlife studies use the closed-population form when births, deaths, and movement are negligible between the two samples. Fisheries tagging and bird banding are classical settings. Epidemiology uses the same estimator on two incomplete lists — hospitals, laboratories, registries — to estimate how many cases were on neither list. Open populations, in which animals enter and leave, need a different model. A single pair of samples does not estimate a density per hectare until the area of the sampled population is known. Absolute abundance is the count. A density is that count divided by area or volume.{{cite:krebs2021}} (Ch. 2, pp. 21–25){{cite:brittain2009}} (pp. 23–24, §1)

## Worked example
Take \(M=20\), \(C=15\), and \(R=5\). The Petersen estimate is
\[
\hat N = \frac{15\times 20}{5} = 60.
\]
The Chapman estimate is
\[
\hat N = \frac{21\times 16}{6}-1 = 56-1 = 55.
\]
The two answers differ by five animals. The Petersen figure is the one the proportion argument gives directly. The Chapman figure is the small-sample adjustment.{{cite:krebs2021}} (Ch. 2, p. 25)

**Your turn.** Keep \(M=20\) and \(C=15\), and suppose \(10\) of the \(15\) are recaptures. What is the Petersen estimate?

::: {.callout-tip collapse="true" title="Answer"}
\(\hat N = (15\times 20)/10 = 30\).
:::

## Common misconceptions
The estimate is not a [census](census.qmd). It is an extrapolation from two samples. A larger second sample does not by itself remove bias from unequal catchability. Treating the Chapman estimate and the Petersen estimate as the same number hides a correction that matters when \(R\) is small. And a capture–recapture estimate of cases on medical lists is not a prevalence until it is divided by the population at risk.{{cite:brittain2009}} (§1, §3.1){{cite:krebs2021}} (Ch. 2, p. 25)

## Assumptions and limits
The second sample has to be random with respect to the marks: marked and unmarked animals are equally catchable, which requires that the marked animals mixed back into the population. The population is treated as closed between the samples. Marks are not lost, and animals are not double-counted. For lists, the two sources are assumed independent, and the same person must be recognisable on both. If the people who avoid one list also avoid the other, the overlap is too small and the population is overestimated. A zero overlap leaves the Petersen estimator undefined.{{cite:krebs2021}} (Ch. 2, pp. 24–25){{cite:brittain2009}} (§3.1)

## Connections
The [binomial](binomial-distribution.qmd) and hypergeometric sampling models sit under the second sample. [Census](census.qmd) undercount is the official-statistics version of the same two-list problem. [Epidemiology](epidemiology.qmd) uses the lists to estimate uncounted cases. [Demography](demography.qmd) meets the method in post-enumeration surveys. Multiple recaptures and open populations replace the single ratio with a likelihood, but the two-sample estimator remains the one to understand first.

## History
John Graunt used a related idea on the population of London in 1662. C. G. J. Petersen, a Danish fisheries biologist, applied marking to estimate the size of a fish population in 1896, after tags had been used to study movement. Lincoln in 1930 estimated duck abundance from band returns. The two-list form under independence, and the Chapman modification, are now standard both for animals and for incomplete human lists.{{cite:krebs2021}} (Ch. 2, p. 24){{cite:brittain2009}} (§3.1)
