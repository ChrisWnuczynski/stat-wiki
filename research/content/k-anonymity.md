## Lead context

A hospital or a bank holds a table of person-specific records and wants to give researchers a copy. Deleting the name does not finish the job. A row that still carries a birth date, a ZIP code, and a sex can match one person on a public voter list, and the medical or financial fact travels with the match. K-anonymity is a requirement on the released table: every pattern of those linking fields appears often enough that the match is a group. {{cite:sweeney2002}} (p. 557, §1)

## Motivating example

States collect hospital records that include ZIP code, birth date, sex, and ethnicity. A voter list carries name, address, ZIP code, birth date, and gender. The two files share the ZIP code, the birth date, and the sex. Linking on those fields attaches a diagnosis to a named person even though the hospital file never contained the name. The holder needs a release in which that link does not single anyone out, and in which the diagnoses are still useful for research. {{cite:sweeney2002}} (pp. 557, 563, §1 and Example 2)

## Intuition

Some fields are not names and still behave like names when they are combined. A birth date is common. A birth date together with a 5-digit ZIP code and a sex is often unique. Those fields are the quasi-identifier: the columns an outsider might already know from another source. Sweeney records the term as Dalenius’s. K-anonymity does not hide the quasi-identifier. It forces every pattern of it that is published to be shared by at least $k$ rows, so the outsider’s match is a group of size at least $k$ rather than a single person. {{cite:sweeney2002}} (pp. 563–564, Definition 2 and Definition 3)

## Definition

Let $RT(A_1,\ldots,A_n)$ be a table with one row per person, and let $QI_{RT}$ be the quasi-identifier associated with it. The table satisfies $k$-anonymity if and only if every sequence of values in the projection onto $QI_{RT}$ appears at least $k$ times in that projection. Equivalently, the information in the release about any one person cannot be distinguished, on the quasi-identifier, from at least $k-1$ other people whose rows appear as well. Each row is assumed to describe one person, and no person appears twice. {{cite:sweeney2002}} (pp. 562–564, §3 and Definition 3)

The usual ways of producing such a table are generalisation and suppression. A ZIP code $02138$ becomes $0213*$. A rare combination that still appears once can be dropped. The diagnosis, or whatever the analysis needs, is left intact inside the group. How far to generalise is the trade against usefulness. The systems Datafly, $\mu$-Argus, and $k$-Similar were built to enforce the frequency requirement. {{cite:sweeney2002}} (p. 562, §3)

## Statistical use

Before a microdata file is shared, the holder marks the quasi-identifier, chooses $k$, and coarsens or suppresses until the frequency test passes. Analyses that need only coarse geography and age bands can proceed on the released file. Analyses that need the exact ZIP code cannot, because that precision was the identifying part. The holder is assumed to know which fields also appear in external information. If that judgment is wrong, and an outsider knows a field that was left out of the quasi-identifier, the frequency test on the declared columns is the wrong test. {{cite:sweeney2002}} (pp. 563–564)

[Differential privacy](differential-privacy.qmd) is a different standard. Dwork’s formulation asks that participation in the database not increase what can be learned about a person, relative to what could be learned without that participation, and treats the release as a randomised mechanism. K-anonymity certifies a table by counting repeated rows. It does not add random noise, and repeated queries of the same table reveal the same groups. A table can be $k$-anonymous and still move sharply when one person is included, if the sensitive fields inside a group are extreme. The two guarantees answer different questions. {{cite:dwork2006}} (§1) {{cite:sweeney2002}} (Definition 3)

## Worked example

Four rows are released with quasi-identifier $(\mathrm{ZIP},\mathrm{sex})$:

| ZIP | Sex | Diagnosis |
| --- | --- | --- |
| 02138 | F | cold |
| 02138 | F | flu |
| 02138 | F | cold |
| 02139 | M | asthma |

The pair $(02138,\mathrm F)$ appears three times. The pair $(02139,\mathrm M)$ appears once. The minimum frequency is 1, so the table is not 2-anonymous. {{cite:sweeney2002}} (Definition 3)

**Your turn.** A second row with ZIP $02139$ and sex M is added. What is the minimum frequency, and does the table satisfy 2-anonymity?

::: {.callout-tip collapse="true" title="Answer"}
Both pairs now appear at least twice. The minimum frequency is 2, so the table satisfies 2-anonymity.
:::

## Common misconceptions

Deleting names is not $k$-anonymity. A table can be free of explicit identifiers and still have unique quasi-identifier rows. The integer $k$ is not a probability of re-identification. It is a minimum group size against an outsider who knows the quasi-identifier and nothing else that distinguishes the rows. Sharing a $k$-anonymous file does not license a second file of the same people with a different coarsening, because the two files can be linked. {{cite:sweeney2002}} (pp. 557, 564)

K-anonymity does not mean the sensitive field is hidden from someone who matches the whole group. If everyone in the group has the same diagnosis, the outsider who knows the quasi-identifier learns the diagnosis without learning which row is which. That homogeneity is a limit of the definition, not a failure of the frequency count. The definition constrains the quasi-identifier columns only. {{cite:sweeney2002}} (Definition 3)

The four-row release makes the count concrete. The pattern 02138 and F occurs three times, and the pattern 02139 and M occurs once, so the minimum frequency is one and the table fails 2-anonymity. One added row with ZIP 02139 and sex M raises the rare pattern from one row to two, and the minimum becomes two. The diagnosis column is never part of that arithmetic. If the three rows that share 02138 and F had all listed the same illness, an outsider who knew that ZIP code and that sex would learn the illness for every person in the pattern, and the frequency test would still pass once every pattern met the threshold. Generalising both ZIP codes to the coarser value 0213* would put all four rows, or all five after the added row, into a single pattern. The frequency test would then be easy to meet, and the geographic detail that distinguished the two hospitals would be gone. The choice of $k$ and the choice of how far to coarsen are the same decision seen from the count and from the usefulness of what remains. {{cite:sweeney2002}} (pp. 562–564, Definition 3)

## Connections

A [statistical disclosure](data-sharing.qmd) problem is the decision to release records that still support research. K-anonymity is one formal constraint on that release. [Differential privacy](differential-privacy.qmd) bounds the change in a randomised analysis when one person is added or removed, which is Dwork’s replacement for a goal that asked the release to teach nothing about a person that could not be learned without the database. Linkage of a medical file to a voter list is the attack Sweeney’s frequency condition is built to block, and it fails open if the quasi-identifier was chosen too narrowly. The policies that accompany the model — which fields count, and what else may be released — are part of the protection. {{cite:sweeney2002}} (pp. 557, 562–564) {{cite:dwork2006}} (§1)
