## Lead context

A hospital can publish a table of average lengths of stay and still reveal a particular patient's record, if the table is fine enough and the listener knows that the patient was included. Differential privacy is a mathematical promise about that risk: the distribution of the released analysis barely changes when one person's row is added or removed. The promise is a property of the randomised algorithm that produces the release. It is a bound on ratios of probabilities, so that a rare output stays rare on every neighbouring file.{{cite:dwork2006}} (pp. 8–9, Definition 2){{cite:wasserman_zhou2010}} (§2, the definition)

## Motivating example

An insurer is about to see a published average. Suppose the file is a list of binary indicators, one per person, and the published number is the exact count of the sensitive indicator. Two files that differ only in one person's bit produce counts that differ by one. Some outputs that are certain for one file are impossible for the other, so the ratio of those probabilities is infinite and no finite $\varepsilon$ satisfies the bound. The count is already free of names, and it still moves when one person is added or removed. An attacker who already knows a great deal can combine that knowledge with a published average and learn something new. The guarantee limits the change in the odds that comes from one person's participation. If a bad outcome happens, the presence of that one row is what the bound keeps from being the cause.{{cite:dwork2006}} (pp. 1–3, the height example; pp. 8–9, Definition 2){{cite:dwork_roth2014}} (pp. 17–18, the definition)

## Definition

A randomised algorithm $\mathcal M$ is $(\varepsilon,\delta)$-differentially private if, for every set $S$ of possible outputs and for every pair of databases $x$ and $y$ whose rows differ by at most one person,

$$
\Pr[\mathcal M(x)\in S] \le e^{\varepsilon}\,\Pr[\mathcal M(y)\in S]+\delta.
$$

The probability is over the coin flips in $\mathcal M$. When $\delta=0$, $\mathcal M$ is $\varepsilon$-differentially private: every output that can arise from $x$ can arise from $y$, and the probabilities differ by at most the factor $e^{\varepsilon}$. The 2006 definition is this pure case, written for data sets that differ in at most one element. The histogram form of the same idea measures neighbours by an $\ell_1$ distance of at most 1. Wasserman and Zhou write the pure bound for a data-release mechanism $Q_n$ as

$$
\sup_{x,y:\,\delta(x,y)=1}\sup_B \frac{Q_n(B\mid X=x)}{Q_n(B\mid X=y)}\le e^{\alpha},
$$

with the ratio read as 1 when both probabilities are 0, and with $\delta(x,y)$ the number of rows on which the two databases differ. Their $\alpha$ is the privacy parameter called $\varepsilon$ above.{{cite:dwork_roth2014}} (pp. 17–18, the definition){{cite:dwork2006}} (pp. 8–9, Definition 2){{cite:wasserman_zhou2010}} (§2, the definition)

The curator may publish a synthetic file, a table of summaries, or answers to questions one at a time. In the interactive case the analyst can choose the next question after seeing earlier answers. The definition applies to the whole mechanism, including that adaptivity. A count query has $\ell_1$ sensitivity 1, so the noise scale is set from that one-person change rather than from the number of cells.{{cite:dwork2006}} (pp. 9–11, Theorems 4 and 5){{cite:dwork_roth2014}} (§2.2, p. 11)

## Interpretation

The inequality is a worst-case statement over pairs of neighbouring files and over output events. Ratios, rather than differences of probabilities, are what protect an output that is rare under both files: a small absolute probability can still jump by a large factor. A small $\delta$, much smaller than one over the number of rows, is the regime in which the additive slack does not swallow the definition. A $\delta$ on the order of $1/n$ can be met by a mechanism that publishes a few complete records and is careful with the rest. Even a tiny $\delta$ changes the logic. $(\varepsilon,0)$-privacy says that every output is nearly equally likely on every neighbouring file. $(\varepsilon,\delta)$-privacy allows a small set of outputs to break that rule.{{cite:dwork_roth2014}} (pp. 17–18){{cite:wasserman_zhou2010}} (§2)

Group privacy follows by repeating the one-person bound. If $k$ people are considered together, an $(\varepsilon,0)$-private mechanism is $(k\varepsilon,0)$-private for that group: the factor $e^{\varepsilon}$ becomes $e^{k\varepsilon}$. The bound gets weaker as the group grows, which matches the aim of releasing facts about large groups. Post-processing cannot spend the privacy budget again. Any mapping of the released output, chosen without looking at the private file, leaves the same $(\varepsilon,\delta)$.{{cite:dwork2006}} (p. 9){{cite:dwork_roth2014}} (pp. 19–20, the post-processing and group-privacy results)

The same ratio limits a hypothesis test aimed at one person. Suppose $Z$ is released by an $\alpha$-differentially private mechanism. Any level-$\gamma$ test, based on $Z$, of whether subject $i$ equals one value or another has power at most $\gamma e^{\alpha}$. With $e^{\alpha}=2$ and $\gamma=0.05$, the power is at most $0.10$. A test that cannot beat its level by more than that factor cannot reliably say who was in the file. Sampling from an ordinary histogram, with no extra smooth component, does not meet the definition: one row can move a cell count onto a value the neighbouring file gives probability zero. A smoothed histogram that mixes in a positive uniform weight can meet the bound when the number of draws, the number of bins, and that weight satisfy the stated inequality.{{cite:wasserman_zhou2010}} (§2, the testing bound; §4.1)

## Worked example

Take $\delta=0$ and $e^{\varepsilon}=2$, so $\varepsilon=\ln 2$. Suppose that on database $y$ the probability of an output set $S$ is $0.1$. The definition requires

$$
\Pr[\mathcal M(x)\in S] \le 2\times 0.1 = 0.2
$$

for every neighbour $x$ of $y$. A mechanism that puts probability $0.25$ on $S$ when the database is $x$ fails the definition for this pair, even if the two databases differ by a single row.{{cite:dwork_roth2014}} (p. 17, the definition){{cite:wasserman_zhou2010}} (§2, the definition)

**Your turn.** Keep $\delta=0$ and $e^{\varepsilon}=2$. If $\Pr[\mathcal M(y)\in S]=0.3$, what is the upper bound on $\Pr[\mathcal M(x)\in S]$ for a neighbour $x$?

::: {.callout-tip collapse="true" title="Answer"}
The bound is $2\times 0.3=0.6$.
:::

## Connections

[K-anonymity](k-anonymity.qmd) limits how rare a combination of quasi-identifiers is in a released table. Differential privacy limits how much one person can move the distribution of any release. A table can pass a frequency test and still move sharply when one person is included, if the sensitive fields inside a group are extreme. [Sampling](random-sample.qmd) and [confidence intervals](confidence-interval.qmd) describe uncertainty from a random sample. The noise here is added on purpose, on top of whatever sampling produced the file, and the privacy account is a bound on output probabilities rather than a standard error. Official releases of tabular data are the setting in which both the frequency test and the probability bound are discussed.{{cite:dwork_roth2014}} (pp. 17–18){{cite:wasserman_zhou2010}} (§1)

## History

A 1977 desideratum asked that nothing about an individual be learnable from a statistical database that could not be learned without it. That absolute goal cannot be formalised in the style of semantic security, because auxiliary information plus a harmless-looking average can reveal a person who is not even in the file. The Terry Gross example is the illustration: an average height of Lithuanian women, together with the auxiliary fact that she is two inches shorter than that average, reveals her height whether or not she is a row in the file. The 2006 definition replaced that absolute goal with a relative one. The probability of any output shifts by at most a factor $e^{\varepsilon}$ when one person is added or removed. The mechanism that adds symmetric exponential noise scaled to the $\ell_1$ sensitivity meets the pure bound, and the same argument covers an adaptive sequence of queries once the sensitivity is taken over the whole strategy. The 2014 monograph records the $(\varepsilon,\delta)$ form, in which a small additive slack is allowed, together with the post-processing and group-privacy consequences. A statistical reading of the same definition compares release mechanisms by how fast a distribution estimated from the sanitised sample approaches the distribution of the original sample.{{cite:dwork2006}} (pp. 1–3, 8–11){{cite:dwork_roth2014}} (pp. 17–20){{cite:wasserman_zhou2010}} (§1; §2)
