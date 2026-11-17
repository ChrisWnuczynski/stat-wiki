

## Lead context

Not every analysis starts by collecting the observations it analyses. Secondary data are records that were made for another purpose and are later used again: a register of births, a file of medical records, a sales ledger, an official series. {{cite:dodge2008}} (p. 152) {{cite:openintro2019}}

## Motivating example

Researchers who want the relation between an earlier illness and a later outcome can review medical records instead of waiting for new cases to occur. The records were written for care, not for the study. The study is retrospective: the events have already taken place, and the data are being read afterwards. {{cite:openintro2019}} A register of births, deaths, and marriages is the same kind of material on a civic scale. {{cite:dodge2008}} (p. 152)

## Definition

Secondary data are observations originally recorded for a purpose other than the study now using them. A register is the standard form: births, deaths, marriages, daily temperatures, monthly rainfall, car sales, and similar series that are already accessible. {{cite:dodge2008}} (p. 152) Reviewing past events in medical or company records is the retrospective version of the same practice. {{cite:openintro2019}}

Official statistics are the governmental case. They are statistics from data collected by government establishments, or by private agencies working for government, and the census is the best-known example. {{cite:dodge2008}} (p. 393)

Primary collection designs the observation for the question. Secondary use inherits the design somebody else chose: which events were recorded, which were skipped, and what the categories meant at the time. The arithmetic can be excellent and still describe the register rather than the population the new question names. {{cite:dodge2008}} (p. 152) {{cite:nist_glossary2002}} (Glossary, "coverage error")

There is no general method that turns a register into a sound conclusion. Each series has to be judged on its merits, and inference beyond the recorded units is the delicate step. {{cite:dodge2008}} (p. 152)

The coverage of a register is the coverage of whatever list was kept. Units the original system did not record are not in the file, and no reanalysis puts them back. That is coverage error relative to a population wider than the register. {{cite:nist_glossary2002}} (Glossary, "coverage error") {{cite:nist_glossary2002}} (Glossary, "census")

A retrospective file can sit beside prospectively collected variables in the same study. The Nurses' Health Study collects new questionnaires from a cohort. A review of old charts does not. A data set can contain both. {{cite:openintro2019}}

Secondary data support description of what was recorded, and they support a wider claim only with an argument that the recorded units and the recorded variables match the question. {{cite:dodge2008}} (p. 152) They are observational. A causal reading has the usual difficulty of an observational comparison, with the extra difficulty that confounders the original record did not bother to store cannot be adjusted for. {{cite:openintro2019}} Official series are the source for population counts, vital events, and similar public description. {{cite:dodge2008}} (p. 393) {{cite:dodge2008}} (p. 518)

Secondary data are not a cheap census of the question one wishes had been asked. The variables are the ones the original purpose required. A billing file may not contain the clinical detail a later study needs. {{cite:dodge2008}} (p. 151) {{cite:dodge2008}} (p. 152)

Using a register does not assign a treatment. A retrospective review of records is an observational study. {{cite:openintro2019}} {{cite:openintro2019}}

The definitions, the missingness, and the coverage are inherited. A code that meant one thing when it was written cannot be redefined by the later analyst without a record of the change. {{cite:dodge2008}} (p. 152) Inference from the register to a population it did not cover is a coverage problem, not a sample-size problem. {{cite:nist_glossary2002}} (Glossary, "coverage error") Official series share the limits of the administrative systems that produced them. {{cite:dodge2008}} (p. 393)

## Worked example

A hospital file holds 240 admissions and was kept for billing. A study of falls finds a fall recorded for 30 of them. The recorded risk is \(30/240 = 0.125\). The hospital's catchment had 300 admissions in the same period, and 60 were treated elsewhere and are absent from the file. The file covers \(240/300 = 0.8\) of the catchment's admissions. The 0.125 describes the billed admissions, not, without a further argument, the catchment. {{cite:dodge2008}} (p. 152) {{cite:nist_glossary2002}} (Glossary, "coverage error")

**Your turn.** Twelve of the 60 missing admissions are later found, and 3 of those 12 had a fall. What are the new number of admissions in the file and the new recorded fall risk?

::: {.callout-tip collapse="true" title="Answer"}
The file has \(240 + 12 = 252\) admissions and \(30 + 3 = 33\) falls. The recorded risk is \(33/252 = 11/84\).
:::



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 14. Their total is 105, so their mean is 7.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 5.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Secondary data has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 7.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [Data collection](data-collection.qmd), [Raw data](raw-data.qmd), [Data quality](data-quality.qmd), [cohort study](cohort-study.qmd).

Two further limits are algebraic. The sum of deviations from the mean 7.5 is zero, so the mean is the least-squares centre of these 14 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 7.5.

## Connections

[Data collection](data-collection.qmd) lists the register as one of three approaches, beside sampling and experiment. [Raw data](raw-data.qmd) are those records before a new study summarises them. [Data quality](data-quality.qmd) includes the coverage gap. A [cohort study](cohort-study.qmd) can be built by following people forward or by reconstructing the follow-up from records. A [statistical survey](statistical-survey.qmd) that was run for one agency and reanalysed by another is secondary for the second user.

## History

Registers and censuses are the old form of data collection, from the enumerations of antiquity through the Roman counts and the administrative statistics of the modern state. {{cite:dodge2008}} (p. 152) {{cite:dodge2008}} (p. 393) Retrospective review of existing records, as against identifying people and then watching events unfold, is the distinction a first course still uses to separate the two timings of an observational study. {{cite:openintro2019}}
