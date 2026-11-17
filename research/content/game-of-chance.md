## Lead context

Dice, cards, and roulette are small worlds: the rules list every result, and a probability can be attached to each one before anyone plays. A game of chance is that kind of play. It is where probability first became a calculation, and it is still the cleanest place to see an expectation.

## Motivating example

A fair die is thrown once. The player wins one euro on an even face, wins two euros on a 1 or a 3, and loses three euros on a 5. The payoff is a number attached to each face, and the faces are equally likely. The average payoff per throw is not found by playing a long evening and hoping; it is the probability-weighted sum of those three payoffs.{{cite:dodge2008}} (p. 190)

## Intuition

A game of chance separates three pieces that later statistical work keeps together. The [sample space](sample-space.qmd) is the list of results the rules allow. The probability says how the rules, or a physical symmetry, spread belief across that list. The payoff says what is won or lost. Once those three are fixed, the expected payoff is ordinary arithmetic. Skill, and anything the rules do not list, sit outside the model.{{cite:grinstead_snell1997}} (pp. 1–2)

The same skeleton covers a coin, a card draw, and a roulette wheel. It does not cover a game in which a player can choose a better action after seeing the position, unless that choice has already been written into the payoff.

## Definition

A game of chance is a repeatable random experiment whose outcomes are fixed by stated rules, together with a probability for each outcome and a numerical payoff. Rolling one fair die has outcomes \(1,2,3,4,5,6\), each with probability \(1/6\). Tossing a fair coin has two outcomes, each with probability \(1/2\). The payoff is a [random variable](random-variable.qmd) on that outcome list.{{cite:grinstead_snell1997}} (pp. 1–2)

In the euro game the payoff \(X\) takes only three values. Even faces \(\{2,4,6\}\) give \(X=1\), with probability \(3/6\). The faces \(\{1,3\}\) give \(X=2\), with probability \(2/6\). The face \(5\) gives \(X=-3\), with probability \(1/6\). Every face is in exactly one of those classes.{{cite:dodge2008}} (p. 190)

Games of this sort were treated as the simple models of random phenomena: the rules can be repeated, the outcomes can be enumerated, and a calculated probability can be checked by playing again. Mortality, accidents, and errors of measurement were recognised as random as well, but they were harder to list.{{cite:dodge2008}} (p. 433)

## Properties

For a payoff that takes values \(x_i\) with probabilities \(p_i\),
\[
E[X]=\sum_i x_i p_i,
\]
when the sum is finite. In the euro game
\[
E[X]=-3\cdot\frac{1}{6}+1\cdot\frac{3}{6}+2\cdot\frac{2}{6}=\frac{-3+3+4}{6}=\frac{2}{3}.
\]
The player gains, on average, two-thirds of a euro per throw. That is a property of the rules, not a promise about the next throw.{{cite:dodge2008}} (p. 190)

A fair six-sided die, scored by the face itself, has
\[
E[X]=\frac{1+2+3+4+5+6}{6}=\frac{21}{6}=\frac{7}{2}.
\]
The probability of a face of at most 4 is \(4/6=2/3\), because four of the six faces are favourable and the probabilities are equal.{{cite:grinstead_snell1997}} (p. 1)

When two payoffs \(a\) and \(b\) are equally likely, the expectation is \((a+b)/2\). Huygens obtained that value by matching the bet to a symmetric stake that each player can see is fair, and then adjusted the argument to unequal chances that are rational. The modern weighted sum agrees with those values. Linearity, \(E[X+Y]=E[X]+E[Y]\), holds whether or not the throws are independent; the product formula \(E[XY]=E[X]E[Y]\) needs independence.{{cite:grinstead_snell1997}} (pp. 243–244){{cite:dodge2008}} (p. 190)

A count of successes in independent repetitions, each with the same success probability, is a [binomial distribution](binomial-distribution.qmd). One such trial is a [Bernoulli distribution](bernoulli-distribution.qmd). Those laws were built to answer repeated games: how many times a chosen face appears, or how many trials are won.{{cite:dodge2008}} (pp. 37, 44)

## Statistical use

The expected payoff decides whether a stated game is favourable. If \(E[X]>0\) the rules favour the player who receives \(X\); if \(E[X]<0\) they favour the other side; if \(E[X]=0\) the game is fair in the sense of expectation, even when the chance of a win is not one half. A bet that wins 3 with probability \(1/4\) and loses 1 otherwise has expectation \(3/4-3/4=0\), and the probability of winning is only \(1/4\).

The same devices randomise an experiment. Cards, dice, and roulette were named as physical ways to build an order that is not chosen by the experimenter. A published table of random sampling numbers was offered as a faster substitute for that physical shuffling. The probability calculation is the same one used for the game: each admissible arrangement receives its share under the rules of the draw.{{cite:grinstead_snell1997}} (pp. 1–2)

Repeated play also supplies the frequency check. If an outcome has probability \(p\), the fraction of plays on which it appears is expected to lie near \(p\) once the number of plays is large. A short session can wander far from \(E[X]\) without the rules having changed.{{cite:grinstead_snell1997}} (p. 2)

## Worked example

The euro die has payoffs \(-3\), \(1\), and \(2\) with probabilities \(1/6\), \(3/6\), and \(2/6\). The expectation is \(2/3\), as above. A second game uses a fair coin. Heads pays \(3\) and tails pays \(-1\), so
\[
E[Y]=\frac{1}{2}\cdot 3+\frac{1}{2}\cdot(-1)=1.
\]
The coin game is favourable by one unit per toss. The die game is favourable by two-thirds of a unit per throw. Adding an independent play of each gives expected total \(1+2/3=5/3\), by linearity.{{cite:dodge2008}} (p. 190){{cite:grinstead_snell1997}} (pp. 243–244)

**Your turn.** A wheel pays \(4\) with probability \(1/4\), pays \(0\) with probability \(1/2\), and pays \(-2\) with probability \(1/4\). Find the expected payoff. Is the game fair?

::: {.callout-tip collapse="true" title="Answer"}
The expectation is \(4/4+0+(-2)/4=1-1/2=1/2\). The game is not fair, because the expected payoff is not \(0\).
:::

## Common misconceptions

A game of chance is not every uncertain situation. A medical risk or an error of measurement can be given a probability model, but the outcomes are not fixed by a short list of rules in the way a die is. The early calculus started with the games because the list was short enough to audit.{{cite:dodge2008}} (p. 433)

Equal probabilities are part of the model of a fair die, not a fact about every cube of plastic. If one face is more likely than another, the expectation \(7/2\) for the face value is the wrong number, and so is \(2/3\) in the euro game. The formula still applies once the unequal probabilities are put in.{{cite:grinstead_snell1997}} (pp. 1–2)

A favourable expectation does not mean a win on the next play. The euro game loses three units whenever a 5 appears, an event of probability \(1/6\), even though the average is positive.

## Assumptions and limits

The calculation assumes that the rules really are the experiment: one throw, an honest die, and a payoff that depends only on the face. If the player can stop early, or if two throws are mixed in one payoff, the random variable has to be rewritten. Independence is an extra assumption when several throws are added or when a product of payoffs is taken.{{cite:dodge2008}} (p. 190)

Huygens's extension from equal chances to unequal chances was stated for rational probabilities, by splitting the bet into equally likely chances. A probability that is not a ratio of whole numbers needs the later definition of expectation as a sum or an integral, not that splitting argument alone.{{cite:grinstead_snell1997}} (pp. 243–244)

The frequency reading, that the proportion of wins approaches \(p\), is a statement about a long sequence of repeats. A single compulsory bet, which cannot be replayed, still has an expectation, but the player cannot check it by averaging this one decision.{{cite:grinstead_snell1997}} (p. 244)

## Connections

The outcome list is a [sample space](sample-space.qmd), and the payoff is a [random variable](random-variable.qmd). One success-or-failure play is a [Bernoulli distribution](bernoulli-distribution.qmd); a fixed number of independent plays is a [binomial distribution](binomial-distribution.qmd). Using cards or dice to assign treatments is the randomisation step in a [designed experiment](designed-experiment.qmd), and the [Lady tasting tea](lady-tasting-tea.qmd) is the classical illustration of an order produced that way. A [statistician](statistician.qmd) who meets data that are not a game still uses the same expectation, after the probabilities have been supplied by a model rather than by the rules of a table.

## History

Gambling with dice is ancient. Probability as a systematic calculation is not. In the sixteenth century, games of chance were what pushed writers to compute chances, and Gerolamo Cardano treated dice under the special case in which every listed outcome is equally likely.{{cite:grinstead_snell1997}} (p. 30) The correspondence of Blaise Pascal and Pierre de Fermat, on two problems from games of chance, is the seventeenth-century starting point usually given for the mathematical theory; Huygens, Bernoulli, and DeMoivre worked in the line those problems opened.{{cite:grinstead_snell1997}} (p. vii) Huygens's *De Ratiociniis in Aleae Ludo* (1657) is where the expected value of a game was first developed as a systematic argument, by reducing unequal payoffs to symmetric stakes.{{cite:grinstead_snell1997}} (pp. 243–244){{cite:dodge2008}} (p. 190)

Jakob Bernoulli's *Ars Conjectandi*, published in 1713, devoted its third part to problems about games of chance, after a commentary on Huygens and a treatment of combinations. The binomial distribution, as a law for the number of successes in repeated trials, is the part of that tradition that counts wins rather than a single payoff.{{cite:dodge2008}} (pp. 37, 44)
