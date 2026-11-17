## Lead context

A person claims to be able to taste whether milk or tea was poured into the cup first. The Lady tasting tea is the experiment R. A. Fisher used to show how such a claim should be tested: a fixed design, a random order, and a probability that is computed entirely from the design under the assumption that the claim is false.

## Motivating example

Eight cups are prepared, four with milk added first and four with tea added first. The taster is told that design in advance and is asked to divide the eight cups into two groups of four. If the division matches the way the cups were actually made, the claim looks strong. If the taster has no ability to tell the cups apart, there are many wrong divisions and only one perfect one. The experiment is a way of counting those divisions before anyone tastes.{{cite:fisher1935_doe}} (pp. 11–12)

## Intuition

Guessing would be too easy to interpret if the taster were not told the design, or if the order were chosen to suit a hoped-for result. Fixing four cups of each kind, and choosing their labels by a physical random device, makes every admissible division equally likely when taste confers no information. A perfect score is then one particular division out of a list that can be counted. The rarity of that one division is the evidence, not the drama of the claim.{{cite:fisher1935_doe}} (pp. 12, 20){{cite:senn1993}} (p. 2)

## Definition

The experiment uses eight cups, four of each preparation, presented in random order. The order is not picked by the experimenter to taste. It comes from the physical apparatus of a [game of chance](game-of-chance.qmd), such as cards, dice, or a roulette, or from a table of random sampling numbers that records such a draw. The taster, who knows that there are four cups of each kind, must partition the eight cups into two sets of four.{{cite:fisher1935_doe}} (p. 11)

The null hypothesis is that the taster has no sensory discrimination of the kind claimed. Under that hypothesis the seventy possible choices of four cups out of eight are equally likely. There are \(8\times 7\times 6\times 5=1680\) ordered ways to pick four cups, and \(4\times 3\times 2\times 1=24\) orders of any one set of four, so the number of distinct sets is
\[
\frac{1680}{24}=70.
\]
A taster with no discrimination names the correct set in one trial out of seventy, a probability of \(1/70\).{{cite:fisher1935_doe}} (p. 12){{cite:senn1993}} (p. 2)

## Properties

The possible scores are not all equally likely. Classifying all four of one kind correctly can happen in only one way. Classifying three correctly and one incorrectly can happen in \(16\) ways: choose \(3\) of the \(4\) true cups of that kind and \(1\) of the \(4\) cups of the other kind, which is \(\binom{4}{3}\binom{4}{1}=16\). The chance of that score is \(16/70\), a bit more than one fifth. It is not the best possible score. A test that asks whether the result is at least this good must include the perfect score as well, and \(16+1=17\) of the \(70\) sets are at least that good. The tail probability is \(17/70\).{{cite:fisher1935_doe}} (pp. 14–15)

Random assignment is what makes the \(1/70\) exact. Cups will differ in thickness, in the amount of milk, and in temperature as the tasting proceeds. If those disturbances are fixed first, and only then four of the eight cups are assigned at random to each preparation, every set of four still has probability \(1/70\) of being the set that received milk first. The disturbances can change how the taster would label cups. They do not, under this order of operations, change the null probability of a perfect match.{{cite:fisher1935_doe}} (p. 20)

The taster is told the randomisation. The probability of naming every cup correctly cannot be smaller than one over the number of sequences the design actually uses. With seventy divisions that lower bound is \(1/70\). If the design had only two alternating patterns, chosen by a coin, the same bound would be \(1/2\), and a perfect score would be weak. Hiding the true design in the hope of making a guess look rarer than the randomisation allows is not part of the experiment.{{cite:senn1993}} (p. 2)

## Statistical use

Before the cups are tasted, the experimenter has to say what will count as evidence. Fisher treats a perfect classification as the result on which the claim would be admitted, and treats three right and one wrong as too common under the null to carry the same conclusion. The [significance level](significance-level.qmd) is the small null probability the experimenter requires. An experiment in which no possible result would meet that bar would be useless, and a much smaller tasting would make even a perfect score unsurprising.{{cite:fisher1935_doe}} (pp. 12–13)

The procedure is a [permutation test](a-permutation-test.qmd). The observed partition is compared with the partitions that the random assignment could have produced, holding the cups' other properties fixed. It is also the pattern of a [designed experiment](designed-experiment.qmd): the treatments and the number of each are chosen first, the assignment is random, and the null distribution comes from that assignment rather than from a model for how strong the tea tasted. The null is available to be disproved by a rare match. A failure to match does not prove that the taster lacks the ability; it fails to demonstrate the ability at the standard that was set.{{cite:fisher1935_doe}} (pp. 16–17)

Enlarging the experiment, or repeating the whole eight-cup test on further occasions and counting how often all eight are right, changes the null probability of a striking result. With success probability \(1/70\) on each independent occasion, two or more perfect occasions in ten trials are rarer than a single perfect occasion. That is a different experiment, with its own count, not a reinterpretation of one sitting.{{cite:fisher1935_doe}} (p. 22)

## Worked example

The design has \(\binom{8}{4}=70\) divisions. Under the null, a perfect division has probability \(1/70\approx 0.0143\). A score of three correct and one incorrect, for a given kind of cup, has probability \(16/70\approx 0.2286\). The probability of a score at least that good is \(17/70\approx 0.2429\). A rule that rejects the null only on a perfect score therefore has null rejection probability \(1/70\). A rule that also rejects on three correct has null rejection probability \(17/70\), which is not a small significance level.{{cite:fisher1935_doe}} (pp. 12–15)

**Your turn.** Suppose the tasting uses six cups, three of each kind, and the taster must name a set of three. How many divisions are there? What is the null probability of a perfect score, and of a score with exactly two of the three correct?

::: {.callout-tip collapse="true" title="Answer"}
There are \(\binom{6}{3}=20\) divisions. The perfect score has probability \(1/20=0.05\). Exactly two correct means \(\binom{3}{2}\binom{3}{1}=9\) sets, so the probability is \(9/20=0.45\).
:::

## Common misconceptions

A single perfect score is not a proof that the ability exists in general. An event of probability \(1/70\) remains possible when the null is true. Fisher’s own standard was that one significant isolated result does not amount to an experimental demonstration of a natural phenomenon; what is required is a procedure that rarely fails to give a significant result when the phenomenon is real. One tea party is one trial of such a procedure.{{cite:fisher1935_doe}} (pp. 13–14)

The experiment is not a paired tasting in which each cup is independently milk-first or tea-first with equal probability. That different design gives probability \(1/2^8=1/256\) of classifying every cup correctly by chance, and it also allows a score of seven correct. Fisher notes the gain in sensitivity and sets it aside for this psycho-physical test, preferring the fixed margins of four and four. Quoting \(1/256\) for the eight-cup design that was actually described is the probability of a different experiment.{{cite:fisher1935_doe}} (p. 22)

Nor does a significant match identify which physical detail the taster used. If some cups were a different tea, or some milk were boiled, a real discrimination might be a discrimination of those accidents. The test of significance can stay valid while the experiment becomes insensitive to the contrast that was intended, or sensitive to a contrast that was not.{{cite:fisher1935_doe}} (pp. 24–25)

## Assumptions and limits

The \(1/70\) null probability assumes that every set of four is equally likely to be chosen by a taster with no discrimination, and that the assignment really was one of those seventy sets, drawn at random. If the cups have already been grouped by some other factor that the taster can detect, and the treatments are then applied to whole groups, the null probability of a perfect classification can become \(35/70\) rather than \(1/70\). The arithmetic of combinations does not repair a design that never made the seventy sets equally available.{{cite:fisher1935_doe}} (pp. 18–19)

The calculation is conditional on the margins: four cups of each kind, and a response that names four and four. It does not estimate how large a difference in taste would have to be before the taster notices it. A taster who is only sometimes right can fail this particular test at a high rate. Increasing the number of cups, or repeating the test, is the design change that addresses that insensitivity.{{cite:fisher1935_doe}} (pp. 13, 22)

Telling the taster the truth about the randomisation is part of the validity argument. If the announced design is richer than the randomisation that was used, the taster's chance of a complete success is bounded by the poorer design, and a reported \(p\)-value taken from the announced design is too small.{{cite:senn1993}} (p. 2)

## Connections

The random order is produced by a [game of chance](game-of-chance.qmd) or by a table that stands in for one. The whole plan is a [designed experiment](designed-experiment.qmd), and the reference distribution is that of a [permutation test](a-permutation-test.qmd). The threshold against which \(1/70\) is judged is a [significance level](significance-level.qmd). The same margin-conditioned counting, moved to a \(2\times 2\) table of two binary classifications, is the idea behind [Fisher's exact test](fisher-s-exact-test.qmd). A [randomised controlled trial](randomised-controlled-trial.qmd) uses the same separation between the assignment, which the experimenter controls, and the response, which the subject produces.

## History

Fisher published the experiment in 1935 as the worked illustration that opens the principles of experimentation in *The Design of Experiments*. The chapter states the claim, fixes eight cups and four of each kind, counts the seventy divisions, and then uses that count to introduce a test of significance, the null hypothesis, and randomisation as the physical basis of the test. The numerical skeleton, seventy divisions and a null probability of \(1/70\) for a complete success, is the one later writers quote when they treat the tasting as the first fully worked example of a statistically designed experiment.{{cite:fisher1935_doe}} (pp. 11–17, 20){{cite:senn1993}} (p. 2)
