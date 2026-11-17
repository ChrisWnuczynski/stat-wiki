## Motivating example
A group of twenty-three people offers a useful distinction between matching one specified birthday and finding any matching pair. A match to the host involves only twenty-two comparisons. A match anywhere involves $\binom{23}{2}=253$ pairs. Counting pairs is a combination calculation, since the order of the two people does not create a different pair.{{cite:dodge2008}} (p. 98, “Combination”)

## Intuition
Birthdays provide a model for repeated random labels: hash values, identification codes, or occupied locations. Let there be $m$ equally likely labels and $n$ independent draws. Avoiding every collision is easier to count than listing all the ways collisions can occur. After $j$ distinct draws, the next draw avoids them with probability $1-j/m$. Multiplying these conditional probabilities gives the no-collision probability.{{cite:grinstead_snell1997}} (§3.1, ex. 3.3, pp. 77–79)

## Properties — Counting and approximating the complement
For $0\le n\le m$,
$$
P(\text{collision})=1-\frac{m!}{(m-n)!m^n}.
$$
For $n>m$ the probability is one. The numerator counts ordered distinct labels; choosing an unordered set would require multiplying $\binom mn$ by $n!$. Using $\binom mn$ alone would compare an unordered count against an ordered sample space.{{cite:dodge2008}} (pp. 98–99, combinations and combinatory analysis)

Writing the product on a logarithmic scale explains the square-root threshold:
$$
\log P(\text{no collision})=\sum_{j=0}^{n-1}\log(1-j/m)
\approx-\frac{n(n-1)}{2m}.
$$
Thus a collision probability near one half occurs around $n(n-1)=2m\log2$. The approximation applies when the individual ratios $j/m$ are small; it should be checked against the product near a decision threshold.{{cite:grinstead_snell1997}} (§3.1, ex. 19, pp. 90–91)

::: {.callout-note collapse="true" title="Derivation"}
Let $I_{ab}$ indicate that draws $a$ and $b$ match, and put $C=\sum_{a<b}I_{ab}$. Each indicator has mean $1/m$, so linearity gives $E(C)=\binom n2/m$, without needing independence among indicators. Moreover $1_{\{C\ge1\}}\le C$, hence $P(C\ge1)\le E(C)$. The exponential approximation follows by using $\log(1-u)=-u+O(u^2)$ in the product; its log error is of order $n^3/m^2$. This derives both the expected pair count and its relationship to the collision probability.
:::

### Why pair indicators are not a binomial count
For uniform independent labels, any two distinct pair-match indicators are pairwise independent. Disjoint pairs involve disjoint draws. Pairs sharing one draw, such as $I_{12}$ and $I_{13}$, both equal one precisely when three labels coincide, an event of probability $1/m^2$; this equals the product of the two marginal match probabilities. Therefore
$$\operatorname{Var}(C)=\binom n2\frac1m\left(1-\frac1m\right).$$
Nevertheless the indicators are not jointly independent: $I_{12}=I_{13}=1$ forces $I_{23}=1$. Treating the total number of matching pairs as binomial would therefore give the wrong full distribution despite matching its mean and variance. At $n=23$, $m=365$, the expected pair count is $253/365\approx0.6932$, while the probability of any match is about $0.5073$. The two values answer different questions. The counting distinction rests on pairs as unordered combinations.{{cite:dodge2008}} (p. 98, combinations without repetition)

## Worked example — A small code space
Suppose five records receive independent uniform codes from ten possible values. There are $10^5$ ordered assignments, but only $10\cdot9\cdot8\cdot7\cdot6=30240$ distinct-code assignments. The collision probability is therefore $0.6976$. The expected number of matching pairs is $\binom52/10=1$, which is larger than the probability of at least one match: several pairs can match in one assignment. The complement calculation is the same counting argument used for birthdays.{{cite:grinstead_snell1997}} (§3.1, ex. 3.3, pp. 77–79)

**Your turn.** Four records receive uniform codes from ten values. Find the collision probability and expected number of matching pairs.

::: {.callout-tip collapse="true" title="Answer"}
The no-collision probability is $10\cdot9\cdot8\cdot7/10^4=0.504$, so the collision probability is $0.496$. There are six pairs and each matches with probability $0.1$, giving expected pair count $0.6$.
:::

## Assumptions and limits
Uniformity and independence concern the generating mechanism. For independent but nonuniform birthdays with probabilities $p_d$, a given pair matches with probability $\sum_dp_d^2$, which is at least $1/m$ because $\sum_d(p_d-1/m)^2\ge0$. This proves that uniformity minimizes the pair-match probability; it does not by itself establish a formula for the probability of any collision. Dependence, such as twins entering together, changes the model more fundamentally. The usual birthday calculation explicitly assumes equally likely independent dates.{{cite:grinstead_snell1997}} (§3.1, ex. 3.3, p. 78)

## Lead context
The birthday calculation is a collision probability for independent uniform labels.

With $365$ equally likely days, the chance that at least two people in a group share a birthday crosses one half at $23$ people. That event is not the event that someone matches a single specified person. Matching one host uses $22$ comparisons. A shared birthday anywhere in the group uses $\binom{23}{2}=253$ pairs. The two probabilities answer different questions, and the pair count has an expectation of its own.{{cite:dodge2008}} (p. 98, “Combination”)

## Definition
If $n$ independent draws are made from $m$ equally likely labels, and $n\le m$, the probability of at least one repeated label is
$$
1-\frac{m(m-1)\cdots(m-n+1)}{m^n}.
$$
For $n>m$ the probability is one, by the pigeonhole principle. The numerator of the complementary probability counts injections from people to labels. The probability that at least one of $22$ people matches a specified host, under the same uniform model, is $1-(364/365)^{22}\approx 0.0586$. Every comparison is with the host, so this is much smaller than the $0.507$ chance of some shared birthday among $23$ people.{{cite:grinstead_snell1997}} (§3.1, ex. 3.3, pp. 77–79)

## Statistical use
Linearity gives the expected number of matching pairs without finding the collision probability. There are $\binom{n}{2}$ pairs and each matches with probability $1/m$, so the expectation is $\binom{n}{2}/m$. At $n=23$ and $m=365$ this is $253/365\approx 0.693$. At $n=50$ it is $1225/365\approx 3.356$, which is larger than one. An expectation above one is possible because one outcome can contain several matching pairs. The collision probability cannot exceed one. The indicators are pairwise uncorrelated for uniform independent labels, but they are not mutually independent: if persons $1$ and $2$ match and persons $1$ and $3$ match, then persons $2$ and $3$ match as well. A binomial distribution for the pair count would match the mean and variance and still get the joint distribution wrong.{{cite:dodge2008}} (p. 98, combinations without repetition){{cite:grinstead_snell1997}} (§3.1, ex. 19, pp. 90–91)

## Common misconceptions
The square-root approximation $\exp\{-n(n-1)/(2m)\}$ is a guide to where the probability becomes appreciable. It is not a substitute for the product when a decision sits near one half. The product for $23$ people should be computed directly and compared with the approximation before the threshold is quoted. Nonuniform day probabilities make a given pair more likely to match, because $\sum_d p_d^2\ge 1/m$. That inequality does not by itself produce a closed form for the probability that some pair matches. Twins, seasonal birth patterns, and a $366$-day calendar all change the model. The classical one-half threshold is a statement about $365$ independent uniform days, not a fact about every human gathering.{{cite:grinstead_snell1997}} (§3.1, ex. 3.3, p. 78)
