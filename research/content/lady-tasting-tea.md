## Lead context

A woman says she can tell, by taste, whether the milk or the tea was poured first. The claim is about one person and one sitting. R. A. Fisher’s design turns it into a count: eight cups, four of each kind, presented in random order, and a null probability that comes from the number of ways the cups can be divided. The experiment is the opening illustration of *The Design of Experiments*. {{cite:fisher1935_doe}} (pp. 11–12) {{cite:senn1993}} (p. 2)

## Motivating example

The subject is told the rules in advance. She will taste eight cups. Four were made with milk first and four with tea first. The order is fixed by a physical randomisation — cards, dice, a roulette, or a published table of random sampling numbers — and not by the experimenter’s choice. Her task is to divide the eight cups into two sets of four, matching the treatments if she can. A taster with no discrimination is then choosing one of the possible divisions at random. The design makes that statement exact. {{cite:fisher1935_doe}} (pp. 11–12) {{cite:senn1993}} (p. 2)

## Definition

There are 70 ways to choose 4 cups out of 8. Choosing in order would allow \(8\times 7\times 6\times 5=1680\) sequences, and each set of four cups can be ordered in \(4\times 3\times 2\times 1=24\) ways, so the number of distinct sets is \(1680/24=70\). A taster who labels every cup correctly has named one particular set. Under the null hypothesis of no discrimination, that set is 1 of the 70, and the probability of a perfect score is \(1/70\). {{cite:fisher1935_doe}} (p. 12)

The null hypothesis is that the subject has no sensory discrimination of the kind claimed. The frequency distribution attached to it is the equal frequency of the 70 assignments of eight objects to two classes of four. The test of significance divides the possible results into those that are counted against the null and those that are not. Fisher takes a perfect classification as a positive result at the conventional 5 percent standard, because an event that would occur once in 70 trials under the null is rarer than 1 in 20. A score of three correct is not, on the same standard, a demonstration. {{cite:fisher1935_doe}} (pp. 13–16)

## Properties

The possible scores are not equally likely. Classifying all four of one kind correctly can happen in one way. Classifying three correctly and one incorrectly can happen in 16 ways: the three right cups may be chosen from the four of that kind in 4 ways, and the one wrong cup from the four of the other kind in 4 ways. The chance of that score is \(16/70\). It is not the best possible score. A test that asks whether the result is at least this good must include the perfect score as well, and \(16+1=17\) of the 70 sets are at least that good. The tail probability is \(17/70\), more than 20 percent, so three correct is not significant on Fisher’s 5 percent convention. Two correct and two wrong can happen in 36 ways. {{cite:fisher1935_doe}} (pp. 13–14)

Random assignment is what makes the \(1/70\) exact. Cups differ in thickness, in the amount of milk, and in temperature. If those disturbances are fixed first, and only then four of the eight cups are assigned at random to each preparation, every set of four still has probability \(1/70\) of being the set that received milk first. The disturbances can change how the taster would label cups. They do not, under this order of operations, change the null probability of a perfect match. If instead every milk-first cup had sugar and every tea-first cup had none, the taster could sort on the sugar, and the probability of a perfect match would be \(35/70\), not \(1/70\). The test would be vitiated by a difference that was not the one under study. {{cite:fisher1935_doe}} (pp. 18, 20)

The taster is told the randomisation. Senn’s reading of the same passage is that the probability of naming every cup correctly cannot be smaller than one over the number of sequences the design actually uses. With seventy divisions that lower bound is \(1/70\). If the design had only two alternating patterns, chosen by a coin, the same bound would be \(1/2\), and a perfect score would be weak. Hiding the true design, in the hope of making a guess look rarer than the randomisation allows, is not part of the experiment. Fisher explains the procedure. {{cite:senn1993}} (p. 2) {{cite:fisher1935_doe}} (p. 12)

## Statistical use

The experimenter chooses how small a null probability must be before a positive result is admitted. An experiment in which no possible result meets that bar is useless. With only three cups of each kind there are \(\binom{6}{3}=20\) divisions, and a perfect score occurs by chance in 5 trials out of 100, which is the 5 percent line and not a stricter one. Fisher treats 5 percent as the usual standard and treats the eight-cup perfect score, at \(1/70\), as decidedly significant in the statistical sense. He also says what that significance is not: one isolated significant result does not experimentally demonstrate a natural phenomenon. What is required is a method of procedure that rarely fails to give a significant result when the phenomenon is real. {{cite:fisher1935_doe}} (pp. 13–14)

Enlarging the experiment, or repeating the whole eight-cup test and counting how often all eight are right, changes the null probability of a striking result. With success probability \(1/70\) on each independent occasion, two or more perfect occasions in ten trials fall below the 5 percent standard even though the subject may err on eight of the ten occasions. Dropping the unsuccessful occasions would remove the basis of the count. {{cite:fisher1935_doe}} (p. 22)

## Worked example

The design has \(\binom{8}{4}=70\) divisions. Under the null, a perfect division has probability \(1/70\). A score of three correct and one incorrect has probability \(16/70\). The probability of a score at least that good is \(17/70\). A rule that rejects the null only on a perfect score has null rejection probability \(1/70\). A rule that also rejects on three correct has null rejection probability \(17/70\), which is not a small significance level. {{cite:fisher1935_doe}} (pp. 12–14)

**Your turn.** Suppose the tasting uses six cups, three of each kind, and the taster must name a set of three. How many divisions are there? What is the null probability of a perfect score, and of a score with exactly two of the three correct?

::: {.callout-tip collapse="true" title="Answer"}
There are \(\binom{6}{3}=20\) divisions, so a perfect score has null probability \(1/20\). Exactly two correct can happen in \(\binom{3}{2}\binom{3}{1}=9\) ways, with probability \(9/20\).
:::

## Common misconceptions

A single perfect score is not a proof that the ability exists in general. An event of probability \(1/70\) remains possible when the null is true. Fisher’s standard was that one significant isolated result does not amount to an experimental demonstration. One tea party is one trial of a procedure. {{cite:fisher1935_doe}} (pp. 13–14)

The experiment is not a paired tasting in which each cup is independently milk-first or tea-first with equal probability. That different design gives probability \(1/2^8=1/256\) of classifying every cup correctly by chance, and it allows a score of seven correct. Fisher notes the gain in sensitivity and sets it aside for this psycho-physical test, because the independent design can treat all eight cups the same way and bewilder the subject. Quoting \(1/256\) for the eight-cup design that was actually described is the probability of a different experiment. {{cite:fisher1935_doe}} (pp. 22–23)

The \(1/70\) null probability assumes that the assignment really was one of those seventy sets, drawn at random after other differences among the cups were fixed. The sugar example shows the failure mode. If the treatments are tied to a difference the taster can detect, the null probability of a perfect classification can become \(35/70\). The arithmetic of combinations does not repair a design that never made the seventy sets equally available. {{cite:fisher1935_doe}} (p. 18)

## History

Fisher published the experiment in 1935 as the worked illustration that opens the principles of experimentation. The chapter states the claim, fixes eight cups and four of each kind, counts the seventy divisions, and uses that count to introduce a test of significance, the null hypothesis, and randomisation as the physical basis of the test. The numerical skeleton, seventy divisions and a null probability of \(1/70\) for a complete success, is the one later writers quote. Senn reads the same passage as the first example, in the first book on the statistical design of experiments, of a trial on one subject: an n-of-1 trial in which the lady divides eight cups into two labelled sets of four. {{cite:fisher1935_doe}} (pp. 11–16, 20) {{cite:senn1993}} (p. 2)

## Connections

The random order is produced by a [game of chance](game-of-chance.qmd) or by a table that stands in for one. The whole plan is a [designed experiment](designed-experiment.qmd). The threshold against which \(1/70\) is judged is a [significance level](significance-level.qmd). The same margin-conditioned counting, moved to a \(2\times 2\) table of two binary classifications, is the idea behind [Fisher's exact test](fisher-s-exact-test.qmd). A [randomised controlled trial](randomised-controlled-trial.qmd) uses the same separation between the assignment, which the experimenter controls, and the response, which the subject produces. Senn’s warning about masking travels with that separation: the chance of guessing every assignment cannot be smaller than one over the number of sequences the randomisation actually uses. {{cite:fisher1935_doe}} (pp. 11–12, 20) {{cite:senn1993}} (p. 2)
