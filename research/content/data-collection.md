

## Lead context

Before a mean or a model is computed, someone has to decide why the numbers are needed, which numbers those are, and how they will be obtained. Data collection is that decision and the work that carries it out. {{cite:dodge2008}} (p. 151)

## Motivating example

A question about the average time to graduation refers to a target population of graduates. The data that can answer it are the times for cases from that population, not a handful of memorable students. How those cases are obtained, by a register of completions, by a sample, or by an experiment that assigns a condition, is the collection plan. {{cite:openintro2019}} {{cite:dodge2008}} (p. 151)

## Intuition

Three different activities are easy to blur. Reading a register that already exists, drawing a sample or counting everyone, and assigning treatments in an experiment all produce numbers. They do not produce the same kind of warrant for a later conclusion. The collection method is part of what the conclusion is allowed to say. {{cite:dodge2008}} (p. 152) {{cite:openintro2019}}

## Definition

Collecting data starts from three questions: why the data are needed, which data serve that purpose, and how they will be obtained. {{cite:dodge2008}} (p. 151) Three approaches cover the "how". A register uses records that already exist, such as births, deaths, marriages, temperatures, rainfall, or sales. Sampling and census obtain observations from a population, either from a part or from all of it. Experimental research assigns conditions and records the response. {{cite:dodge2008}} (p. 152)

Observational studies and experiments are the two primary types in the language of a first course. An observational study collects data without applying or withholding a treatment: surveys, records, or a cohort followed through time. An experiment assigns treatments to cases. {{cite:openintro2019}} {{cite:openintro2019}}

The collection plan decides which analyses are honest. Estimates and their errors presume a random framework when the data are observational. {{cite:openintro2019}} A causal connection is the aim that leads to a randomised experiment rather than to a survey. {{cite:openintro2019}} Data that are unrelated to the stated goal do not become relevant by being carefully stored. The variables have to be the ones the question names. {{cite:dodge2008}} (p. 151) {{cite:openintro2019}}

Collecting more rows is not the same as collecting the right rows. A convenience pile can be large and still fail to represent the population named in the question. {{cite:openintro2019}} {{cite:nist_glossary2002}} (Glossary, "convenience sample")

An observational collection does not become an experiment because the investigator hoped for a causal sentence. The experiment is the collection in which treatments are assigned. {{cite:openintro2019}} {{cite:openintro2019}}

The oldest mass collection is the census. A statistician is attested in China in the Chow dynasty, Augustus ordered a count of soldiers, ships, and wealth, and the Gospel of Luke records a decree that each person be enrolled in his own town. The word statistics itself comes from Latin *status*, the state. {{cite:dodge2008}} (p. 152) {{cite:dodge2008}} (p. 518) Experimental designs as a systematic programme arrived much later, in the agricultural work of the 1920s. {{cite:dodge2008}} (p. 162)

## Properties

A register has no general recipe that turns the series into a conclusion. Each series is judged on its own, and inference to a wider population is the step that needs care. {{cite:dodge2008}} (p. 152)

Sampling methods split into random and nonrandom. Random methods use a probabilistic rule, so the probability that a unit is selected is known and a sampling error can be calculated. The main random methods are simple random sampling, stratified sampling, systematic sampling, and batch sampling. Quota sampling is the usual nonrandom method. A census observes every object in the population and is costly when the population is large, which is why it is infrequent. {{cite:dodge2008}} (p. 152)

An experiment specifies the levels of the factors under study. The design is the programme for those levels. {{cite:dodge2008}} (p. 162)

## Worked example

A population has 500 shops. A register already holds last year's sales for all 500, so the collection fraction is \(500/500 = 1\) and there is no sampling error from a draw. A sample of 40 shops for a new question that the register does not contain has collection fraction \(40/500 = 0.08\). An experiment that assigns a new layout to 15 of the 40 and leaves 25 unchanged is a third collection: the layout was assigned, which neither the register nor the sample of the old layout did. {{cite:dodge2008}} (p. 152) {{cite:openintro2019}}

**Your turn.** The sample for the new question is enlarged from 40 shops to 50, and 20 of the 50 are assigned the new layout. What is the new sampling fraction out of 500?

::: {.callout-tip collapse="true" title="Answer"}
The sampling fraction is \(50/500 = 0.1\).
:::

## Assumptions and limits

A register supports a description of what was recorded. It supports a wider inference only with an argument that the recorded units are the population of interest. {{cite:dodge2008}} (p. 152) A sampling error can be calculated when selection probabilities are known, which nonrandom methods do not provide. {{cite:dodge2008}} (p. 152) An experiment's conclusion is about the factors and levels that were actually run. {{cite:dodge2008}} (p. 162)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 10. Their total is 55, so their mean is 5.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 3.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Data collection has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 5.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [Sampling](sampling.qmd), [statistical survey](statistical-survey.qmd), [designed experiment](designed-experiment.qmd), [Secondary data](secondary-data.qmd).

Two further limits are algebraic. The sum of deviations from the mean 5.5 is zero, so the mean is the least-squares centre of these 10 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 5.5.

## Connections

[Sampling](sampling.qmd) and the [statistical survey](statistical-survey.qmd) are the middle approach. A [designed experiment](designed-experiment.qmd) is the third. [Secondary data](secondary-data.qmd) are what a register becomes when a later study uses it. [Raw data](raw-data.qmd) are the observations before they are reduced to summaries. The [population](population.qmd) is the set the collection is trying to reach.
