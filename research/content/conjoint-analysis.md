## Lead context
A buyer never sees a brand, a price, and a colour as separate purchases. They see one product and say which of several products they prefer. Conjoint analysis estimates how much each level of each attribute contributes to that overall preference, so that a product which was never shown can still be scored.{{cite:green1992_classic}} (single-page commentary) {{cite:haaijer1999}} (Ch. 2, §2.2, pp. 6–7)

## Motivating example
A respondent rates product cards that combine a brand and a price. The analyst does not ask how many points the brand is worth by itself. The respondent's rating is one number per card. The decomposition asks which part of that number moves when the brand changes and which part moves when the price changes. Those parts are the part-worths. Adding them back up predicts the rating of a card the respondent did not see, including one the firm has not yet made.{{cite:green1992_classic}} (single-page commentary) {{cite:haaijer1999}} (Ch. 2, §2.2, pp. 6–7)

## Definition
Products are described by a small set of attributes, each at a small set of levels. Respondents rank or rate the resulting profiles, or choose one profile from a set. In the additive case the utility of a profile is the sum of part-worths, one for each attribute level that the profile uses. Haaijer writes the compensatory model as \(U=\sum_s X_s\beta_s\), with the part-worth of level \(s\) equal to \(X_s\beta_s\). Estimation recovers those part-worths from the observed scores and the design of the profiles.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 6–7)

Green's later commentary describes the same decomposition: preferences for descriptions of products are broken into part-worths associated with each attribute, and the part-worths are recombined to predict preference for a new product.{{cite:green1992_classic}} (single-page commentary)

When the response is treated as interval-scaled, ordinary least squares is one of the estimators in the classification Green and Srinivasan gave for this problem, as Haaijer reports it. Methods that assume only an order, including MONANOVA, PREFMAP, and LINMAP, form a second class. Paired comparisons in a choice context are analysed with a binary logit or probit model. Choice data, in which the respondent picks one alternative from a set, are analysed with a multinomial logit.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 8–9; §2.3, pp. 10–11)

## Properties
If preferences add, a weakness on one attribute can be offset by a strength on another. A cheap unfamiliar brand can tie an expensive familiar one. The rank order of profiles is then determined by the sums. The range of part-worths within an attribute, divided by the sum of the ranges, is a rough importance of that attribute, and it is an importance relative to the ranges that were actually shown. When every attribute has the same number of levels, the absolute part-worths indicate relative importance. An attribute that is given more levels tends to look more important in ranking, rating, and choice data. Wittink and co-authors called that the number-of-levels effect. Even with equal numbers of levels, the importances are interpretable with respect to the ranges that were used.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 6–7)

Ranking or rating every possible combination is often impossible. Three attributes with four levels and two with three levels already give \(4^3 \times 3^2 = 576\) profiles. A fractional factorial keeps a subset from which the main effects, and the interactions the design was built to separate, can still be estimated. The design, not the utility formula, decides which interactions can be separated from main effects.{{cite:haaijer1999}} (Ch. 2, §2.2, p. 7)

Holdout profiles, scored by the respondent and withheld from the fit, test whether the sums predict new cards from the same task. They do not by themselves show that the same person would buy the product in a shop. A holdout that repeats the task only speaks to forecasting accuracy under the same conditions.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 9–10)

## Statistical use
The design is a [designed experiment](designed-experiment.qmd) in the attributes. [Least squares](least-squares.qmd) fits rating data when an interval scale is assumed. A [binary logistic regression](binary-logistic-regression.qmd) or a multinomial model fits choices. Individual part-worths can be clustered when the question is a segment rather than one buyer. Predicted utilities are turned into predicted choices by a rule such as first choice, the profile with the highest sum, and those choices are aggregated toward a preference share. Commercial uses that have been listed for the method include new-product identification, pricing, segmentation, advertising, and distribution.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 6–10)

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
The part-worth of a level is not a price in currency until a separate comparison with the price attribute converts utility into money. A high importance is not a property of the attribute in the abstract. It is a property of the levels that were shown. First choice treats a utility gap of \(0.1\) like a gap of \(10\): both predict the same winner. Haaijer notes the same point in probability language: a \(51\%\) chance and a \(99\%\) chance are treated alike by a deterministic first-choice rule, and they are not the same preference. A model fitted to ratings of cards is not yet a model of purchases.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 7–10)

## History
Luce and Tukey set out conjoint measurement in 1964 as a theory of how joint effects of factors determine an order. Marketing took the idea up as a way to measure preference. Green and Rao's 1971 paper introduced the full-profile technique to marketing research. Green later described the 1978 review with Srinivasan, in the *Journal of Consumer Research*, as the paper that organised the measurement, and he dated the introduction of the method to marketing at 1971, with Rao. Choice-based conjoint, in which the respondent picks one alternative from a set, became a standard applied form after the work Louviere and Woodworth published in 1983.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 6–8; §2.3, p. 11) {{cite:green1992_classic}} (single-page commentary)

## Connections
[Least squares](least-squares.qmd) and [logistic regression](binary-logistic-regression.qmd) are the estimators for ratings and for binary choices. [Designed experiments](designed-experiment.qmd) supply the profiles. [Discrete choice](multinomial-logistic-regression.qmd) is the later form in which the respondent picks one alternative from a set rather than scoring every profile. The decomposition is the same idea as a main-effects model: an overall score is written as a sum of pieces, and the pieces are what the design identifies.{{cite:haaijer1999}} (Ch. 2, §§2.2–2.3, pp. 6–11)

Additivity fails when a level is acceptable only together with another level. Unrealistic combinations, such as a luxury brand at a price no firm would charge, still receive a sum if the design includes them. Brand can stand in for unlisted attributes such as quality, so the brand part-worth is not a pure name effect. Rank data are a poor match to ordinary least squares even when the numerical recovery of the part-worths happens to be similar: ranks are an order, and ordinary least squares treats the numbers as an interval scale.{{cite:haaijer1999}} (Ch. 2, §2.2, pp. 7–9)
