## Lead context
A statistical claim starts from recorded measurements, not from the population feature the measurements are meant to describe. {{cite:abs_glossary2023}} (Glossary, “Data”) {{cite:dodge2008}} (p. 150)

## Motivating example
A clinic writes down the age, the sex, and the serum creatinine of each admitted patient. Those three columns are data. The mean creatinine is a summary of the column; it is not itself the data. The decision to admit the patients, and the rule that says which patients belong in the study, are not data either. {{cite:abs_glossary2023}} (Glossary, “Data”) {{cite:dodge2008}} (p. 150)

## Intuition
Think of data as the raw material a later calculation is allowed to see. Anything that was not written down from a unit cannot be recovered by a cleverer formula. Organising the same numbers into a table does not create new information; it only makes the information easier to read. {{cite:dodge2008}} (p. 150) {{cite:abs_glossary2023}} (Glossary, “Dataset”)

## Definition
Data are measurements or observations collected as a source of information. {{cite:abs_glossary2023}} (Glossary, “Data”) In a study they are tied to the variable being recorded: quantitative when that variable is quantitative, qualitative when it is qualitative, and discrete or continuous in the same way. {{cite:dodge2008}} (p. 150) One row of a table is one unit's record. The whole table is the data only when every recorded value that the analysis will use is in it. {{cite:abs_glossary2023}} (Glossary, “Dataset”)

The organised collection is a [dataset](dataset.qmd). Each row is one unit in a [population](population.qmd) or a [sample](sample.qmd), and each column is a [variable](variable.qmd). {{cite:abs_glossary2023}} (Glossary, “Data unit”)

## Properties
Data inherit the scale of the variable. A name such as a blood type can be counted. A rank can be ordered. A length can be averaged. Coding a name as 1, 2, or 3 does not turn the code into a length. {{cite:dodge2008}} (p. 439) {{cite:abs_glossary2023}} (Glossary, “Qualitative data”) {{cite:abs_glossary2023}} (Glossary, “Quantitative data”)

The same data can be rearranged into a frequency table, a plot, or a model matrix. Those rearrangements are summaries or inputs. They are not a second set of observations. {{cite:dodge2008}} (p. 150) {{cite:abs_glossary2023}} (Glossary, “Descriptive (or summary) statistics”)

## Statistical use
The first use is to see what was actually recorded: how many units, which variables, which values are missing, and whether a value is possible. Confirmatory calculations, an estimate or a test, come after that inspection and still use only the recorded values and the stated model. {{cite:dodge2008}} (p. 151) {{cite:abs_glossary2023}} (Glossary, “Estimate”)

## Worked example
Five seedlings are measured after one week. The table has columns for pot, height in centimetres, and whether the leaf is spotted.

| Pot | Height (cm) | Spotted |
|:--|--:|:--|
| A | 4.2 | no |
| B | 3.8 | yes |
| C | 4.0 | no |
| D | 5.1 | no |
| E | 3.9 | yes |

There are 5 units and 3 variables, so 15 recorded values. The heights are quantitative. The spotted column is qualitative. {{cite:dodge2008}} (p. 150) {{cite:abs_glossary2023}} (Glossary, “Quantitative data”)

**Your turn.** A sixth column is added, the day of measurement, and pot C is removed because the pot broke. How many units and how many variables remain?

::: {.callout-tip collapse="true" title="Answer"}
Four units remain, and there are four variables: pot, height, spotted, and day. The broken pot's three original values leave with it.
:::

## Common misconceptions
A published mean is not the data. Neither is a fitted coefficient, nor a sentence in the paper that describes the study. Those are products of the data. A spreadsheet that stores the same heights twice does not contain twice as much information. {{cite:abs_glossary2023}} (Glossary, “Data”) {{cite:dodge2008}} (p. 150)

## Assumptions and limits
Calling a table "the data" does not say how the units were chosen. A census and a convenience list can produce tables of the same shape. What the table can support depends on that choice, which is a fact about the [population](population.qmd) and the [sample](sample.qmd), not about the arithmetic. {{cite:dodge2008}} (p. 64) {{cite:abs_glossary2023}} (Glossary, “Census (complete enumeration)”)

## Connections
[Summary statistics](summary-statistics.qmd) compress data. A [statistic](statistic.qmd) computed from a [sample](sample.qmd) is the usual route to a claim about a [parameter](parameter.qmd). The [history of statistics](../history.qmd) is, in large part, a history of new ways to read incomplete records. {{cite:dodge2008}} (p. 518) {{cite:abs_glossary2023}} (Glossary, “Inferential statistics”)

## History
Governments counted people, births, and trade long before those counts were treated as a mathematical subject. The word statistics itself grew out of that state business of counting. {{cite:dodge2008}} (p. 518) The modern discipline is the set of techniques for getting knowledge from data that are incomplete, once the records can be put into numerical form. {{cite:dodge2008}} (p. 518) {{cite:abs_glossary2023}} (Glossary, “Data”)
