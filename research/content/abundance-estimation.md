## Lead context

A lake is not emptied and counted. A sample of fish is marked and released, and a second sample shows what fraction of the fish still carry marks. Abundance estimation, in this capture–recapture form, turns that fraction into an estimate of how many animals were there. The same ratio is the one to understand before any open-population model is attempted.

## Motivating example

Twenty animals are marked and released. A second sample catches fifteen animals, of which five are marked. If the marked animals mixed through the population, and every animal was equally likely to be caught the second time, the marked fraction in the second sample estimates the marked fraction in the population. Five out of fifteen is one third, so the twenty marked animals are about one third of the population, and the population is about sixty. The fraction \(5/15\) is a sample proportion for a population proportion, and a sample proportion is the ordinary estimator of that population proportion when the second sample is drawn from the population of interest.{{cite:krebs2021}} (Ch. 2, pp. 24–25){{cite:openintro2019}} (Ch. 5, §5.1.1)

## Definition

Let \(M\) be the number marked in the first sample, \(C\) the number caught in the second sample, and \(R\) the number of those that are marked. The population size at the time of marking is the unknown \(N\). Equating the marked fraction in the second sample to the marked fraction in the population gives \(N/M = C/R\), and therefore the Petersen estimator
\[
\hat N = \frac{CM}{R}.
\]
Krebs writes this as equation (2.1). The second sample has to be random with respect to the marks: every animal, marked or not, has the same chance of being caught.{{cite:krebs2021}} (Ch. 2, p. 25, eq. 2.1)

The ratio \(CM/R\) tends to overestimate \(N\), and the bias is serious in small samples. Seber's form, recommended by Krebs for sampling without replacement,
\[
\hat N = \frac{(M+1)(C+1)}{R+1}-1,
\]
is nearly unbiased when there are at least seven recaptures. If the second sample is a series of sightings with replacement, Bailey's estimator \(M(C+1)/(R+1)\) is the nearby alternative, and it too is nearly unbiased once \(R\) is at least 7.{{cite:krebs2021}} (Ch. 2, p. 25, eqs. 2.2–2.3)

A closed population does not change in size during the study: births, deaths, and movement are negligible, which is realistic only over a short interval. An open population changes by those events, and it needs a different method. Absolute abundance is the count \(N\). A density is that count divided by the area or volume of the population that was sampled.{{cite:krebs2021}} (Ch. 2, pp. 24–25)

## Properties

The Petersen estimate is undefined when \(R=0\): the ratio divides by the recapture count, so a second sample with no marks does not yield a finite population size. The Chapman form remains defined at \(R=0\). Under the proportion argument, \(\hat N\) is the number of marks divided by the sample proportion of marks. That sample proportion estimates the population proportion of marks in the same way any sample proportion estimates its population proportion, and the estimate of \(N\) inherits the sampling variability of \(R/C\).{{cite:krebs2021}} (Ch. 2, p. 25){{cite:openintro2019}} (Ch. 5, §5.1.1)

A [confidence interval](confidence-interval.qmd) is part of the estimate. After the interval is calculated, the true \(N\) is either inside it or outside it; the coverage statement is about the procedure across samples, not a certificate for the one interval in hand. With few recaptures the interval is wide. In one artificial population of \(N=1000\), with \(M=400\) and repeated second samples of \(C=50\), 13 of 500 Petersen estimates fell outside the known size, below \(705\) or above \(1570\). A larger second sample, \(C=400\) in the same experiment, still left 22 of 500 intervals missing \(1000\). A narrow interval is the precision goal; it does not guarantee that this particular interval covers.{{cite:krebs2021}} (Ch. 2, pp. 26–27)

The second-sample model is [binomial](binomial-distribution.qmd) when sampling is with replacement, and hypergeometric when it is without. A [census](census.qmd) would count every animal. The Petersen number is an extrapolation from two samples.

The same lake shows how hard the ratio works. Five marked animals in a catch of fifteen give a marked fraction of one third and a Petersen estimate of sixty. Ten marked animals in a catch of the same size give a marked fraction of two thirds and a Petersen estimate of thirty. Nothing about the lake changed except the second catch. Doubling the recaptures halved the estimated abundance, because the estimator is the number of marks divided by the marked fraction. A small second sample makes that fraction a noisy estimate of the population fraction, and the division then stretches the noise into a wide scatter of population sizes. Krebs's artificial population of one thousand animals, with four hundred marks, repeats the draw often enough to see that scatter. Thirteen of five hundred Petersen estimates from second samples of fifty fell below 705 or above 1570. Twenty-two of five hundred estimates from second samples of four hundred still missed the true size. A larger second sample changes the sampling distribution. It does not certify the one interval computed from the catch in hand. Absolute abundance is still a count of animals. A density is that count divided by the area or volume that was sampled, so an estimate of sixty fish becomes a density only after the area of the lake is supplied.{{cite:krebs2021}} (Ch. 2, pp. 25–27){{cite:openintro2019}} (Ch. 5, §5.1.1)

## Worked example

Take \(M=20\), \(C=15\), and \(R=5\). The Petersen estimate is
\[
\hat N = \frac{15\times 20}{5} = 60.
\]
The Chapman estimate is
\[
\hat N = \frac{21\times 16}{6}-1 = 56-1 = 55.
\]
The two answers differ by five animals. The Petersen figure is the one the proportion argument gives directly. The Chapman figure is the small-sample adjustment. Five recaptures are fewer than the seven at which Krebs describes the Chapman form as nearly unbiased, so the five-animal gap is the size of correction the small-sample formula is for.{{cite:krebs2021}} (Ch. 2, p. 25)

**Your turn.** Keep \(M=20\) and \(C=15\), and suppose \(10\) of the \(15\) are recaptures. What is the Petersen estimate?

::: {.callout-tip collapse="true" title="Answer"}
\(\hat N = (15\times 20)/10 = 30\).
:::

## Assumptions and limits

The second sample is random with respect to the marks, which requires that the marked animals mixed back into the population and that marking did not change catchability. The population is treated as closed between the samples. Marks are not lost, and animals are not counted twice. When the second sample is without replacement, an animal enters \(C\) at most once; Bailey's form is the one Krebs gives for sightings that can repeat.{{cite:krebs2021}} (Ch. 2, pp. 24–25)

A zero overlap leaves the Petersen estimator undefined. Fewer than seven recaptures is the range in which the bias of equation (2.1) is the reason to prefer equation (2.2). The artificial experiment with \(N=1000\), \(M=400\), and \(C=50\) shows how wide the sampling distribution remains when recaptures are scarce: estimates below \(705\) and above \(1570\) both occurred. A single pair of samples does not estimate a density until the area of the sampled population is known.{{cite:krebs2021}} (Ch. 2, pp. 25–27)

## History

Tags were first used to study movement. C. G. J. Petersen, a Danish fisheries biologist, applied marking to estimate the size of a fish population in 1896. The closed-population ratio, the Chapman modification for sampling without replacement, and Bailey's form for sampling with replacement are the two-sample estimators Krebs sets out as the starting point. Open populations, in which animals enter and leave, replace that single ratio with a different model.{{cite:krebs2021}} (Ch. 2, p. 24)
