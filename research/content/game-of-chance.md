## Lead context

Dice, cards, and roulette are small worlds. The rules list every result, and a probability can be attached to each one before anyone plays. A game of chance is that kind of play. It is where the expectation of a numerical payoff was first written as a calculation, and it is still the cleanest place to see the arithmetic.

## Motivating example

A fair die is thrown once. The player wins one euro on an even face, wins two euros on a 1 or a 3, and loses three euros on a 5. The payoff is a number attached to each face, and the faces are equally likely. The average payoff per throw is not found by playing a long evening and hoping. It is the probability-weighted sum of those three payoffs. {{cite:dodge2008}} (p. 190)

## Definition

A game of chance is a repeatable random experiment whose outcomes are fixed by stated rules, together with a probability for each outcome and a numerical payoff. Rolling one fair die has outcomes \(1,2,3,4,5,6\). The probability that the face is at most 4 is \(4/6=2/3\), because four of the six faces are favourable and the probabilities are equal. Tossing a fair coin has two outcomes, each with probability \(1/2\), unless there is a reason to think one face lands more often than the other. The payoff is a [random variable](random-variable.qmd) on that outcome list. {{cite:grinstead_snell1997}} (§1.1, p. 2) {{cite:dodge2008}} (p. 190)

In the euro game the payoff \(X\) takes three values. Even faces \(\{2,4,6\}\) give \(X=1\), with probability \(3/6\). The faces \(\{1,3\}\) give \(X=2\), with probability \(2/6\). The face \(5\) gives \(X=-3\), with probability \(1/6\). Every face is in exactly one of those classes. The [sample space](sample-space.qmd) is the list the rules allow. The probability says how the rules, or a physical symmetry, spread belief across that list. The payoff says what is won or lost. Skill, and anything the rules do not list, sit outside the model. {{cite:dodge2008}} (p. 190)

The same skeleton covers a coin, a card draw, and a roulette wheel. It does not cover a game in which a player can choose a better action after seeing the position, unless that choice has already been written into the payoff. Games of this sort were the early models of random phenomena because the rules can be repeated and the outcomes can be enumerated. Huygens’s *De ratiociniis in aleae ludo* of 1657 is the text in which the mathematical expectation of such a payoff was set out, and it shaped the later work of Pascal and Fermat. {{cite:dodge2008}} (pp. 190, 468)

## Properties

For a payoff that takes values \(x_i\) with probabilities \(p_i\),
\[
E[X]=\sum_i x_i p_i,
\]
when the sum is finite. In the euro game
\[
E[X]=-3\cdot\frac{1}{6}+1\cdot\frac{3}{6}+2\cdot\frac{2}{6}=\frac{-3+3+4}{6}=\frac{2}{3}.
\]
The player gains, on average, two-thirds of a euro per throw. That is a property of the rules, not a promise about the next throw. {{cite:dodge2008}} (p. 190)

A fair six-sided die, scored by the face itself, has
\[
E[X]=\frac{1+2+3+4+5+6}{6}=\frac{21}{6}=\frac{7}{2}.
\]
Linearity holds whether or not the payoffs are independent: \(E[X+Y]=E[X]+E[Y]\), and \(E[aX+b]=aE[X]+b\). If \(X\) and \(Y\) are independent, the expectation of the product factors as well. A constant shift of the payoff shifts the expectation by the same constant, which is why a game that is favourable by \(c\) becomes fair when the stake is raised by \(c\). {{cite:dodge2008}} (p. 190)

A fair game, in this arithmetic, is one whose expected payoff is zero. A positive expectation is favourable to the player who receives the payoff. Repeating an independent play adds the expectations. It does not make the next play equal the expectation.

## Worked example

A fair coin pays \(+3\) on heads and \(-1\) on tails. The expected payoff is
\[
\frac{1}{2}\cdot 3+\frac{1}{2}\cdot(-1)=1.
\]
The euro die has expectation \(2/3\). Adding an independent play of the coin game to an independent play of the die game gives expected total
\[
1+\frac{2}{3}=\frac{5}{3},
\]
by linearity. The coin is favourable by one unit per toss. The die is favourable by two-thirds of a unit per throw. Neither figure is a prediction that the next combined play equals \(5/3\). {{cite:dodge2008}} (p. 190) {{cite:grinstead_snell1997}} (§1.1, p. 2)

**Your turn.** A wheel pays \(4\) with probability \(1/4\), pays \(0\) with probability \(1/2\), and pays \(-2\) with probability \(1/4\). Find the expected payoff. Is the game fair?

::: {.callout-tip collapse="true" title="Answer"}
The expectation is \(4\cdot(1/4)+0\cdot(1/2)+(-2)\cdot(1/4)=1-1/2=1/2\). The game is not fair, because the expected payoff is not \(0\).
:::

## Assumptions and limits

The calculation uses the probabilities the rules state. A die that is worn, a wheel that is biased, or a deck that was not shuffled is a different experiment, and the expectation computed from the fair rules does not describe it. Grinstead and Snell’s frequency reading makes the same point from the other direction: if an outcome has probability \(p\), the fraction of repetitions in which it appears should be about \(p\) when the experiment is repeated in the same way. Buffon’s 4,040 coin tosses, with 2,048 heads, and Wolf’s 100,000 throws of a die are checks of that kind. They are not proofs that the next toss equals the average. {{cite:grinstead_snell1997}} (§1.1, pp. 2, 9)

The model also stops where the rules stop. A payoff that depends on a choice the player has not yet written down is not yet a random variable on a fixed list. Expectation is undefined, in the formula above, if the sum of \(x_i p_i\) does not converge. A game that pays \(2^k\) with probabilities that make the sum diverge is outside the arithmetic used here.

Independence is required for the product formula and is not required for the sum. Adding the euro game to the coin game uses only linearity. Treating the two plays as one random mechanism would need a joint distribution the separate expectations do not supply.

## History

Huygens published the expectation of a chance payoff in 1657. Pascal and Fermat’s correspondence on the division of stakes is the other seventeenth-century source of the same arithmetic. Early probability problems were often suggested by gambling, and anyone who plays the same game repeatedly is, in Grinstead and Snell’s phrase, already running a simulation. Later statistical work kept the three pieces — an outcome list, a probability, and a numerical score — and applied them to mortality, measurement error, and samples, where the list is harder to write down. The die and the coin remain the place where the expectation can be computed before any data arrive. {{cite:dodge2008}} (pp. 190, 468) {{cite:grinstead_snell1997}} (§1.1, p. 9)
