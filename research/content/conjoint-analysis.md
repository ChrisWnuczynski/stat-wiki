

## Lead context

A buyer never sees a brand, a price, and a colour as separate purchases. They see one product and say which of several products they prefer. Conjoint analysis estimates how much each level of each attribute contributes to that overall preference, so that a product which was never shown can still be scored.

## Motivating example

A respondent rates product cards that combine a brand and a price. The analyst does not ask "how many points is the brand worth?" The respondent's rating is one number per card. The decomposition asks which part of that number moves when the brand changes and which part moves when the price changes. Those parts are the part-worths. Adding them back up predicts the rating of a card the respondent did not see, including one the firm has not yet made.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 6–7){{cite:green1992_classic}} (Citation Classic)

## Definition

Products are described by a small set of attributes, each at a small set of levels. Respondents rank or rate the resulting profiles, or choose one profile from a set. The model in the additive case is that the utility of a profile is the sum of part-worths, one for each attribute level that the profile uses. Estimation recovers those part-worths from the observed scores and the design of the profiles. When the response is treated as interval-scaled, ordinary least squares is one of the estimators Green and Srinivasan classified for this problem. Rank data have been analysed with procedures that assume only an order. Choice data, in which the respondent picks one alternative from a set, are analysed with a binary or multinomial logit or probit model.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 6–9)

The part-worths are then recombined to predict preference for a description the respondent did not evaluate. That prediction is the practical product of the method: a new product, a new price, or a new bundle.{{cite:green1992_classic}} (Citation Classic){{cite:haaijer1999}} (Ch. 2, §2.2)

If preferences add, a weakness on one attribute can be offset by a strength on another. A cheap unfamiliar brand can tie an expensive familiar one. The part-worth is the contribution of one level of one attribute, on the scale of the respondent's scores. The utility of a whole profile is the sum of the part-worths of the levels it carries. Ranking or rating every possible combination is often impossible: three attributes with four levels and two with three levels already give \(4^3 \times 3^2 = 576\) profiles. A fractional factorial keeps a subset from which the main effects can still be estimated.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 6–7)

Additivity fails when a level is acceptable only together with another level. Unrealistic combinations, such as a luxury brand at a price no firm would charge, still receive a sum if the design includes them. Brand can stand in for unlisted attributes such as quality, so the brand part-worth is not a pure name effect. Rank data are a poor match to ordinary least squares even when the numerical recovery of the part-worths happens to be similar. The number-of-levels effect means that splitting one attribute into more levels can inflate its apparent importance.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 7–9)

## Properties

With an additive utility, the rank order of profiles is determined by the sums. The range of part-worths within an attribute, divided by the sum of the ranges, is a rough importance of that attribute, and it is an importance relative to the ranges that were actually shown. An attribute that is given more levels tends to look more important in ranking, rating, and choice data, which is a property of the coding rather than of the buyer. A full factorial of many attributes is too large for a respondent, so the design, not the utility formula, decides which interactions can be separated from main effects.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 7–9)

Holdout profiles, scored by the respondent and withheld from the fit, test whether the sums predict new cards from the same task. They do not by themselves show that the same person would buy the product in a shop.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 9–10)

## Statistical use

The design is a [designed experiment](designed-experiment.qmd) in the attributes. [Least squares](least-squares.qmd) fits rating data. A [binary logistic regression](binary-logistic-regression.qmd) or a multinomial model fits choices. Individual part-worths can be clustered when the question is a segment rather than one buyer. Predicted utilities are turned into predicted choices by a rule such as first choice — the profile with the highest sum — and those choices are aggregated toward a preference share. Commercial uses that have been listed for the method include new-product identification, pricing, segmentation, advertising, and distribution.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 6–10)

## Worked example

Two attributes, each with two levels, and additive part-worths: brand A has part-worth \(0\), brand B has \(2\), the low price has \(3\), and the high price has \(0\). The four profiles score
\[
\begin{align*}
U(\text{A, low}) &= 0+3 = 3,\\
U(\text{A, high}) &= 0+0 = 0,\\
U(\text{B, low}) &= 2+3 = 5,\\
U(\text{B, high}) &= 2+0 = 2.
\end{align*}
\]
The highest utility is brand B at the low price. The range for brand is \(2-0=2\) and the range for price is \(3-0=3\). The share of the total range that belongs to price is \(3/(2+3)=3/5\).{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 6–7)

**Your turn.** Using the same part-worths, what is the share of the total range that belongs to brand?

::: {.callout-tip collapse="true" title="Answer"}
The brand range is 2 and the total of the ranges is 5, so the share is \(2/5\).
:::

## Common misconceptions

The part-worth of a level is not a price in currency until a separate comparison with the price attribute converts utility into money. A high importance is not a property of the attribute in the abstract. It is a property of the levels that were shown. First choice treats a utility gap of \(0.1\) like a gap of \(10\): both predict the same winner, and neither is a probability. And a model fitted to ratings of cards is not yet a model of purchases.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 7–10)

## History

Luce and Tukey set out conjoint measurement in 1964 as a theory of how joint effects of factors determine an order. Marketing took the idea up as a way to measure preference. Green and Rao's 1971 paper introduced the technique to marketing research. Green and Srinivasan's 1978 review, which Green later described as a statistical decomposition of preferences into part-worths that can be recombined for new products, organised the choices of response scale, design, and estimator. Choice-based conjoint, joining the attribute design to a random-utility model, became the common applied form after Louviere and Woodworth's work in the early 1980s.{{cite:haaijer1999}} (Ch. 2, §§2.2–2.3, pp. 6–12){{cite:green1992_classic}} (Citation Classic)

## Connections

[Least squares](least-squares.qmd) and [logistic regression](binary-logistic-regression.qmd) are the estimators. [Designed experiments](designed-experiment.qmd) supply the profiles. [Discrete choice](multinomial-logistic-regression.qmd) is the later form in which the respondent picks one alternative from a set rather than scoring every profile. The decomposition is the same idea as a main-effects model: an overall score is written as a sum of pieces, and the pieces are what the design identifies.
