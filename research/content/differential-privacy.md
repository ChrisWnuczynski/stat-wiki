## Lead context
A hospital can publish a table of average lengths of stay and still reveal a particular patient's record, if the table is fine enough and the listener knows that the patient was included. Differential privacy is a mathematical promise about that risk: the output of the analysis should have nearly the same distribution whether or not any one person's data are in the file.

## Motivating example
An insurer is about to see a published average. Suppose the file is a list of binary indicators, one per person, and the published number is the exact count of the sensitive indicator. Two files that differ only in one person's bit produce counts that differ by one. Some outputs that are certain for one file are impossible for the other. The insurer's decision can therefore depend on that one bit. A promise that is only about "anonymous" tables, with names removed, does not speak to this calculation. The count is already anonymous, and it still moves when one person is added or removed.{{cite:dwork2006}} (p. 1, introduction; p. 9, Definition 2){{cite:dwork_roth2014}} (pp. 11, 17–18)

## Intuition
The curator holds one row per person and will answer questions about the whole file. Privacy is not a claim that an attacker learns nothing. An attacker who already knows a great deal can combine that knowledge with a published average and learn something new. The demand is narrower and enforceable. Participating in the file should not change the attacker's odds by more than a chosen factor. If a bad outcome happens, it should not be the presence of one person's row that made it happen.{{cite:dwork2006}} (p. 1, introduction){{cite:dwork_roth2014}} (p. 17)

## Definition
A randomised algorithm \(\mathcal M\) is \((\varepsilon,\delta)\)-differentially private if, for every set \(S\) of possible outputs and for every pair of databases \(x\) and \(y\) whose rows differ by at most one person,
\[
\Pr[\mathcal M(x)\in S] \le e^{\varepsilon}\,\Pr[\mathcal M(y)\in S]+\delta.
\]
The probability is over the randomness in \(\mathcal M\). When \(\delta=0\), \(\mathcal M\) is \(\varepsilon\)-differentially private: every output that can arise from \(x\) can arise from \(y\), and the probabilities differ by at most the factor \(e^{\varepsilon}\). The same definition, with databases that differ in one element, is the 2006 form.{{cite:dwork_roth2014}} (p. 17, Definition 2.4){{cite:dwork2006}} (p. 9, Definition 2)

The curator may publish a synthetic file, a table of summaries, or answers to questions one at a time. In the interactive case the analyst can choose the next question after seeing earlier answers. The definition applies to the whole mechanism, including that adaptivity.{{cite:dwork_roth2014}} (p. 11)

## Properties
The inequality is a worst-case statement over pairs of neighbouring files and over output events. A small \(\delta\), much smaller than one over the number of rows, is the regime of interest. A \(\delta\) on the order of \(1/n\) can be met by a mechanism that publishes a few complete records and is careful with the rest, which defeats the point of the definition. Even a tiny \(\delta\) changes the logic: \((\varepsilon,0)\)-privacy says that every output is nearly equally likely on every neighbouring file, while \((\varepsilon,\delta)\)-privacy allows a small set of outputs to break that rule.{{cite:dwork_roth2014}} (pp. 17–18)

Group privacy follows by repeating the one-person bound. If \(c\) people are considered together, the factor \(e^{\varepsilon}\) becomes \(e^{c\varepsilon}\) in the pure case. The bound gets weaker as the group grows, which matches the aim of releasing facts about large groups.{{cite:dwork2006}} (p. 9)

## Statistical use
The release is a randomised algorithm, so the same file can produce different outputs. The privacy parameter \(\varepsilon\) sets how far the output probabilities on neighbouring files may separate. A mean or a count that is published exactly will usually break the inequality, because one person's row moves the number onto a value the neighbouring file cannot produce. Group privacy repeats the one-person factor: \(c\) people considered together are protected by \(e^{c\varepsilon}\) rather than by \(e^{\varepsilon}\). [K-anonymity](k-anonymity.qmd) is a different guarantee, about repeated quasi-identifiers in a released table, and it does not bound this ratio of probabilities.{{cite:dwork_roth2014}} (pp. 17–18){{cite:dwork2006}} (p. 9)

## Worked example
Take \(\delta=0\) and \(e^{\varepsilon}=2\), so \(\varepsilon=\ln 2\). Suppose that on database \(y\) the probability of an output set \(S\) is \(0.1\). The definition requires
\[
\Pr[\mathcal M(x)\in S] \le 2\times 0.1 = 0.2
\]
for every neighbour \(x\) of \(y\). A mechanism that puts probability \(0.25\) on \(S\) when the database is \(x\) fails the definition for this pair, even if the two databases differ by a single row.{{cite:dwork_roth2014}} (p. 17, Definition 2.4)

**Your turn.** Keep \(\delta=0\) and \(e^{\varepsilon}=2\). If \(\Pr[\mathcal M(y)\in S]=0.3\), what is the upper bound on \(\Pr[\mathcal M(x)\in S]\) for a neighbour \(x\)?

::: {.callout-tip collapse="true" title="Answer"}
The bound is \(2\times 0.3=0.6\).
:::

## Common misconceptions
Differential privacy is not a promise that an attacker learns nothing about a person. Auxiliary information can already determine a fact; the guarantee is about the additional effect of being in the file. It is not achieved by deleting names. It is not a property of a data set alone: it is a property of the randomised algorithm that releases information. A mechanism can be private and useless, if the noise is so large that the published number does not track the file. The definition does not by itself choose \(\varepsilon\). That choice is a policy about how large a change in odds is acceptable.{{cite:dwork2006}} (pp. 1, 9){{cite:dwork_roth2014}} (p. 17)

## Assumptions and limits
The definition assumes a clear notion of neighbouring databases, usually files that differ in one person's row. It assumes the randomness in the mechanism is the only randomness the inequality quantifies. The group bound grows with the number of people who are considered together, so a fact about a very small group is weakly protected. The curator model, in which one party holds the file, is the basic setting; the book notes that a protocol among the individuals can replace that party.{{cite:dwork_roth2014}} (pp. 11, 17–18){{cite:dwork2006}} (p. 9)

## Connections
[K-anonymity](k-anonymity.qmd) limits how rare a combination of quasi-identifiers is in a released table. Differential privacy limits how much one person can move the distribution of any release. [Sampling](random-sample.qmd) and [confidence intervals](confidence-interval.qmd) describe uncertainty from a random sample; the noise here is added on purpose, on top of whatever sampling produced the file. Official releases of tabular data are the setting in which both ideas are used.

## History
A 1977 desideratum asked that nothing about an individual be learnable from a statistical database that could not be learned without it. That absolute goal cannot be formalised in the style of semantic security, because auxiliary information plus a harmless-looking average can reveal a person who is not even in the file. The 2006 definition replaced that absolute goal with a relative one: the probability of any output shifts by at most a factor \(e^{\varepsilon}\) when one person is added or removed. The 2014 monograph records the \((\varepsilon,\delta)\) form, in which a small additive slack is allowed.{{cite:dwork2006}} (pp. 1, 9){{cite:dwork_roth2014}} (pp. 17–18)
