

## Lead context

The numbers that come off the instrument or the questionnaire, before anyone has replaced them by a mean or a table of counts, are the raw data. Summaries are made from them. They are not the same object as the summary. {{cite:openintro2019}} {{cite:nist_glossary2002}} (Glossary, "data reduction")

## Motivating example

A stent trial recorded, for each patient, the assignment and whether a stroke occurred. A table that collapses those records into 45 strokes among 224 treated patients and 28 strokes among 227 control patients is a summary. The patient-level records that the table compresses are the raw data. The summary is easier to read, and it has thrown away which patient was which. {{cite:openintro2019}} {{cite:openintro2019}}

## Definition

Raw data are the observations as recorded on the units, before they are reduced to a smaller set of summaries. A data matrix is the usual arrangement: each row is a case and each column is a variable. {{cite:openintro2019}} {{cite:openintro2019}}

Data reduction is the calculation that turns several numbers into one or fewer. The average and the standard deviation of nine readings are a reduction from nine numbers to two. The usual benefits are simplicity, a sharper focus on the question, and a smaller file. {{cite:nist_glossary2002}} (Glossary, "data reduction")

Data reduction replaces several numbers by fewer numbers. Nine readings across a wafer become a mean and a standard deviation, two numbers instead of nine. The gain is simplicity. The loss is every contrast among the nine that the two summaries do not preserve. Raw data are the observations on the upstream side of that replacement. {{cite:nist_glossary2002}} (Glossary, "data reduction")

Description often begins by reducing the raw file to counts or means so that the pattern is visible. The stent table is that step: the individual outcomes are still the data, and the table is a more helpful view of them. {{cite:openintro2019}} Modelling then treats the reduced or the row-level numbers as the observations in an equation such as \(Y = \beta_0 + \beta_1 X + \varepsilon\). The residual is a comparison of the fitted value with the observation that entered the fit, so the observation has to have been retained at the level the model claims to describe. {{cite:openintro2019}} {{cite:dodge2008}} (p. 354)

A published table is not the raw data. It is a reduction. Two different patient lists can share the counts 45 and 28, and the lists are not recoverable from the counts. {{cite:openintro2019}} {{cite:nist_glossary2002}} (Glossary, "data reduction")

Raw does not mean correct. A wrong answer written on a form is a raw wrong answer. Cleaning and reduction are later steps, and neither is implied by calling the file raw. {{cite:nist_glossary2002}} (Glossary, "respondent error") {{cite:dodge2008}} (p. 182)

[Data collection](data-collection.qmd) is how the rows arrived. [Secondary data](secondary-data.qmd) are rows that were recorded for some other purpose. [Data quality](data-quality.qmd) is whether those rows are fit to summarise. A [statistical model](statistical-model.qmd) is a later description of the rows or of summaries computed from them. The [variable](variable.qmd) is the column.

## Properties

The raw file has one row per observational unit and one column per characteristic. New cases are new rows. New variables are new columns. {{cite:openintro2019}} A summary such as a mean has one number per group, or one number for the whole file, and the link from that number back to a named unit is gone.

Reduction is not neutral. The mean of the nine wafer readings describes their centre and does not describe which position on the wafer was high. Keeping the raw layout is what makes that positional question still answerable. {{cite:nist_glossary2002}} (Glossary, "data reduction")

A register of births or of sales is already a recording. It is raw relative to a later summary, and it may itself be secondary for a study that did not design the register. {{cite:dodge2008}} (p. 152)

## Worked example

Five reaction times, in seconds, are 8, 11, 9, 10, and 12. Their sum is 50 and their mean is \(50/5 = 10\). The deviations from 10 are \(-2, 1, -1, 0, 2\), which sum to 0. Replacing the five numbers by the single mean 10 is a reduction from five numbers to one. The largest time, 12, is no longer visible in the mean. {{cite:nist_glossary2002}} (Glossary, "data reduction") {{cite:openintro2019}}

**Your turn.** A sixth time, 16 seconds, is appended. What are the new sum and the new mean?

::: {.callout-tip collapse="true" title="Answer"}
The sum is \(50 + 16 = 66\). The mean is \(66/6 = 11\).
:::

## Assumptions and limits

What counts as raw depends on the question. A laboratory mean of three instrument replicates is raw for a clinical data set and already reduced for the instrument log. {{cite:nist_glossary2002}} (Glossary, "data reduction") The data matrix assumes that each row is one case. A design in which one person contributes many times needs a decision about what the row is, or the later analysis will treat repeated times as if they were different people. {{cite:openintro2019}} {{cite:dodge2008}} (p. 322)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 13. Their total is 91, so their mean is 7.0. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 5.0. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Raw data has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 7.0 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [Data collection](data-collection.qmd), [Secondary data](secondary-data.qmd), [Data quality](data-quality.qmd), [statistical model](statistical-model.qmd).

Two further limits are algebraic. The sum of deviations from the mean 7.0 is zero, so the mean is the least-squares centre of these 13 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 7.0.

## History

Organising observations as a rectangular array, one case per row, is the arrangement a spreadsheet still uses, and it is the arrangement recommended for recording unless there is a reason to do otherwise. {{cite:openintro2019}} The habit of replacing repeated observations by their mean, as an approximation to a reference value, is much older: it is the use Simpson and his successors made of an arithmetic mean in the eighteenth century. {{cite:dodge2008}} (p. 182)
