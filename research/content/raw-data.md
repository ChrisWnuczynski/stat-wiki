## Lead context
Raw data are the observations as recorded, before they are replaced by fewer summary numbers. In a study of stents, the record for each patient is a row: the group, and whether a stroke occurred by 30 days and by 365 days. A table of counts, such as 33 strokes in the treatment group by 30 days, is a summary of those rows. The rows are the raw data. The counts are not.{{cite:openintro2019}} (Ch. 1, §1.1)

## Motivating example
Five reaction times, in seconds, are written down as \(8\), \(11\), \(9\), \(10\), and \(12\). The scientific question may eventually be answered by their mean. The mean is one number. The five times are five numbers, and any comparison that needs to know which time was longest, or whether two times were equal, has to be made before the five are replaced. Keeping the five is what makes that comparison possible later.{{cite:openintro2019}} (Ch. 1, §1.2.1){{cite:nist_glossary2002}} (Glossary, "data reduction")

## Definition
A record is raw when it still contains the observational units and the variables that were written down for them. In a data matrix, each row is a case and each column is a variable. The loan table that puts amount, interest rate, term, grade, state, income, and home ownership on one row per loan is that kind of record. A summary replaces several of those numbers by fewer numbers. The NIST glossary calls that replacement data reduction: calculating, from several numbers, one or fewer numbers, as when nine readings are replaced by an average and a standard deviation. The nine readings are the raw data of that reduction. The average and the standard deviation are the reduced data.{{cite:openintro2019}} (Ch. 1, §1.2.1){{cite:nist_glossary2002}} (Glossary, "data reduction")

The same distinction applies to a study that was already a table of counts in the publication. Those counts are raw relative to a further summary, such as a single proportion, and they are reduced relative to the patient-level rows that were counted. "Raw" is a relation to a later summary, not a chemical purity of the file.{{cite:openintro2019}} (Ch. 1, §1.1)

## Properties
Reduction loses comparisons. The five times \(8\), \(11\), \(9\), \(10\), and \(12\) sum to \(50\) and have mean \(10\). The mean does not say that \(12\) was the longest or that no two times were equal. A reader who is given only \(10\) cannot recover either fact. Reduction can also be repeated: the stent rows become the four counts \(33\), \(191\), \(13\), and \(214\), and those counts can be reduced again to two proportions. Each step is a function of the previous record. None of the steps is invertible from the number it prints.{{cite:openintro2019}} (Ch. 1, §1.1){{cite:nist_glossary2002}} (Glossary, "data reduction")

A correction of a mis-keyed value is not a reduction. Changing a recorded \(16\) to a recorded \(10\), because the keying was wrong, changes the record. Replacing five correct times by their mean leaves the record alone and publishes a summary. The two operations answer different questions, and only the second is data reduction.{{cite:nist_glossary2002}} (Glossary, "data reduction")

## Worked example
The times \(8\), \(11\), \(9\), \(10\), and \(12\) sum to \(50\). Their mean is \(50/5=10\). The reduced report "mean \(10\)" is one number in place of five. The order, the largest time, and the gaps between times are no longer in the report.

**Your turn.** A sixth time, \(16\) seconds, is appended. What are the new sum and the new mean?

::: {.callout-tip collapse="true" title="Answer"}
The new sum is \(50+16=66\). The new mean is \(66/6=11\).
:::

## Assumptions and limits
The record is only as good as what was written down. A respondent who answers a survey item incorrectly has already put the error into the raw data. Averaging will not mark which row was wrong. A data matrix that drops the link between a rate and the loan it belongs to has already lost the case, even if every rate is still present as a number.{{cite:nist_glossary2002}} (Glossary, "respondent error"){{cite:openintro2019}} (Ch. 1, §1.2.1)

Reduction is often the right publication. The stent table of counts is easier to read than 451 rows, and the mean of the five times is the right answer to a question about the average. The limit is the question that needed a comparison the summary destroyed. That question has to be asked of the raw record, or of a reduction that was built to keep it.{{cite:openintro2019}} (Ch. 1, §1.1){{cite:dodge2008}} (p. 150)

## History
The practice of organising observations into a rectangular record, one row for each unit, is the data matrix of survey and experimental work. Exploratory analysis, as Tukey set it out, starts from that record: graph it, transform it, and look for values that do not belong, before a model replaces it by a few coefficients. The coefficients are a further reduction. They are not a substitute for the record when the question is what was observed.{{cite:dodge2008}} (pp. 150–151){{cite:openintro2019}} (Ch. 1, §1.2)
