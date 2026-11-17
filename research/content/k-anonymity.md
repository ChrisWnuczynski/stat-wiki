

## Lead context

A hospital removes names from a discharge file and releases ZIP code, date of birth, sex, and diagnosis. A reader who knows one neighbour's ZIP code, birth date, and sex can still find that neighbour's diagnosis if nobody else in the file shares those three values. K-anonymity is a requirement on the released table: every combination of those identifying fields that appears must appear at least k times.

## Motivating example

States collect hospital records that include ZIP code, birth date, sex, and ethnicity, and researchers want a copy they can analyse. The holder can delete the name and still leave a row that matches only one person in a public voter list. Linking on the shared fields attaches the medical fact to a named person. The holder needs a release in which that link does not single anyone out, and in which the medical facts are still useful for research.{{cite:sweeney2002}} (p. 557, abstract and Example 1)

## Intuition

Some fields are not names and still behave like names when they are combined. A birth date is common. A birth date together with a 5-digit ZIP code and a sex is often unique. Those fields are the quasi-identifier: the columns an outsider might already know from another source. K-anonymity does not hide the quasi-identifier. It forces every pattern of it that is published to be shared by at least \(k\) rows, so the outsider's match is a group of size at least \(k\) rather than a single person.{{cite:sweeney2002}} (p. 557; Definition 3)

## Definition

Let \(RT(A_1,\ldots,A_n)\) be a table with one row per person, and let \(QI_{RT}\) be the quasi-identifier associated with it. The table satisfies \(k\)-anonymity if and only if every sequence of values in the projection onto \(QI_{RT}\) appears at least \(k\) times in that projection. Equivalently, the information in the release about any one person cannot be distinguished, on the quasi-identifier, from at least \(k-1\) other people who appear as well.{{cite:sweeney2002}} (p. 557; Definition 3)

The usual ways of producing such a table are generalisation and suppression. A ZIP code \(02138\) becomes \(0213*\). An age \(27\) becomes the interval \(25\)–\(29\). A rare combination that still appears once can be dropped. The diagnosis, or whatever the analysis needs, is left intact inside the group. How far to generalise is the trade against usefulness.{{cite:sweeney2002}} (Definition 3)

The parameter \(k\) is a minimum frequency, not an average. One unique row spoils \(k=2\), no matter how large the rest of the table is. The property is about the quasi-identifier columns only. Two people who share a ZIP code, age, and sex may have different diagnoses; the definition does not require those diagnoses to agree. If they do all agree, an outsider who matches the group learns the diagnosis even though they cannot tell which row is which. That is a limit of the definition, not a failure of the frequency count.{{cite:sweeney2002}} (Definition 3){{cite:dwork_roth2014}} (pp. 17–18)

Re-identification attacks remain possible when the quasi-identifier was chosen too narrowly, or when a later release can be linked to this one. Policies that accompany the model, about which fields count as the quasi-identifier and about what else may be released, are part of the protection Sweeney described. Systems such as Datafly, \(\mu\)-Argus, and \(k\)-Similar were built to enforce the frequency requirement.{{cite:sweeney2002}} (p. 557)

Each row is assumed to describe one person, and no person appears twice. The quasi-identifier has to be the set of fields an outsider might know. If the outsider knows a field that was left out of the quasi-identifier, uniqueness on the declared columns is the wrong test. The definition does not add random noise, so repeated queries of the same table do not spend a budget; they reveal the same groups. Small \(k\) leaves small groups. Large \(k\) forces coarse categories and can erase the contrasts the research needed.{{cite:sweeney2002}} (p. 557; Definition 3){{cite:dwork_roth2014}} (p. 17)

The model was stated for holders such as hospitals and banks who need to publish person-level data. The 2002 formulation gave the frequency condition on the quasi-identifier and discussed attacks that still succeed if the accompanying policies are ignored. It was the guarantee implemented by Datafly, \(\mu\)-Argus, and \(k\)-Similar. Later privacy definitions, differential privacy among them, were introduced because a fixed released table can still leak through linkage and through homogeneous sensitive fields, which a bound on a randomised mechanism is designed to limit directly.{{cite:sweeney2002}} (p. 557){{cite:dwork_roth2014}} (pp. 17–18)

## Statistical use

Before a microdata file is shared, the holder marks the quasi-identifier, chooses \(k\), and coarsens or suppresses until the frequency test passes. Analyses that need only coarse geography and age bands can proceed on the released file. Analyses that need the exact ZIP code cannot, because that precision was the identifying part. [Differential privacy](differential-privacy.qmd) is a different standard: it bounds the change in the distribution of a randomised release when one person is added or removed, and it does not certify a table by counting repeated rows. A table can be \(k\)-anonymous and still move sharply when one person is included, if the sensitive fields inside a group are extreme.{{cite:dwork_roth2014}} (p. 17, the definition){{cite:sweeney2002}} (Definition 3)

## Worked example

A release uses ZIP code and sex as the quasi-identifier. The four rows are:

| ZIP | Sex | Diagnosis |
| --- | --- | --- |
| 02138 | F | asthma |
| 02138 | F | asthma |
| 02139 | M | flu |
| 02138 | F | flu |

The pair \((02138,\mathrm F)\) appears three times. The pair \((02139,\mathrm M)\) appears once. The minimum frequency is 1, so the table is not \(2\)-anonymous.{{cite:sweeney2002}} (Definition 3)

**Your turn.** One more row is added, with ZIP \(02139\), sex M, and diagnosis flu. What is the minimum frequency of a quasi-identifier pair, and does the table satisfy \(2\)-anonymity?

::: {.callout-tip collapse="true" title="Answer"}
The pair \((02138,\mathrm F)\) appears three times and the pair \((02139,\mathrm M)\) appears twice. The minimum frequency is 2, so the table satisfies \(2\)-anonymity.
:::

## Common misconceptions

Deleting names is not \(k\)-anonymity. A table can be free of explicit identifiers and still have unique quasi-identifier rows. The integer \(k\) is not a probability of re-identification; it is a minimum group size against an outsider who knows the quasi-identifier and nothing else in the row. Sharing a \(k\)-anonymous file does not license a second file of the same people with a different coarsening, because the two files can be linked. And \(k\)-anonymity does not mean the sensitive field is hidden from someone who matches the whole group, if everyone in the group has the same sensitive value.{{cite:sweeney2002}} (p. 557; Definition 3)

## Connections

[Differential privacy](differential-privacy.qmd) replaces the frequency test with a bound on output probabilities. [Missing data](missing-data.qmd) is a different incompleteness: values were not observed, rather than deliberately coarsened. Record linkage is the attack this model is built to slow down. Official statistical releases face the same choice between a useful table and a unique row.
