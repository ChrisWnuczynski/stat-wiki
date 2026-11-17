## Lead context

A census asks everyone. A statistical survey asks a restricted part of the population and then generalises, with an error that the design is supposed to keep in view. The restricted part is the sample, and the methods that construct it are the sampling methods.{{cite:dodge2008}} (p. 532)

## Motivating example

A city wants the proportion of households with a working smoke alarm. Knocking on every door is a census. Selecting households and putting the same questions to them is a survey. The answers describe the selected households directly. They describe the city only after an inference, and that inference carries an error that depends on how many households were drawn, how they were drawn, and how the proportion was estimated. The more representative the sample, the smaller that error.{{cite:dodge2008}} (pp. 532–533)

## Intuition

The questionnaire is fixed so that each selected person is asked the same thing. The selection is the part that makes the answers stand for people who were never asked. A survey without a selection rule is a stack of conversations. A selection rule without a shared question is a sample of units and not yet a survey. The two pieces have to be present together: a fixed set of questions, and a part of the population chosen to carry them.{{cite:nist_glossary2002}} (Glossary, "survey"){{cite:dodge2008}} (p. 532)

## Definition

A survey is an inquiry made on a restricted part of a population. That part is the sample. Information is obtained on the sampled units and, by inferential statistics, generalised to the population. The generalisation introduces an error whose size depends on the sample size, on the way the units were chosen, and on the estimator.{{cite:dodge2008}} (pp. 532–533)

As a method of collection, a survey asks a fixed set of questions of selected individuals. The practical issues are the questionnaire, the selection of the sample, ideally at random, and non-response. The same questionnaire can be administered in different ways: a verbal interview with the answer recorded by the interviewer, a mail contact, a telephone call, or a proctored room. Those are modes of one survey, not different definitions of the inquiry.{{cite:nist_glossary2002}} (Glossary, "survey"){{cite:nist_glossary2002}} (Glossary, "interview survey"){{cite:nist_glossary2002}} (Glossary, "mail survey"){{cite:nist_glossary2002}} (Glossary, "telephone survey")

## Statistical use

The estimate from a survey is a statistic computed on the sample and aimed at a population quantity. The sampling error is the part of the miss that comes from who was selected. Coverage error, non-response, and measurement error in the answers are separate contributions and are not removed by a larger draw from a bad frame. Survey errors, in the classification used by the engineering glossary, are coverage error, sampling error, measurement error, and non-response. A census observes every unit and does not pay a sampling error. It can be impossible: observing a unit may destroy it, or the population may be infinite. Surveys are used because they cost less and finish sooner, and the compensation is accepted against the sampling error. A survey is an observational collection: the questions do not assign a treatment, and an observational association is not by itself a causal conclusion.{{cite:nist_glossary2002}} (Glossary, "sampling error"){{cite:nist_glossary2002}} (Glossary, "coverage error"){{cite:nist_glossary2002}} (Glossary, "survey errors"){{cite:nist_glossary2002}} (Glossary, "census"){{cite:dodge2008}} (pp. 532–533){{cite:openintro2019}} (Ch. 1, §1.3.4)

Generalisation uses inferential statistics and therefore inherits their conditions, including a selection mechanism whose probabilities can be stated when a sampling error is to be calculated. The questionnaire has to ask what the conclusion needs. A perfectly drawn sample of the wrong question does not answer the research question.{{cite:dodge2008}} (pp. 151–152, 532){{cite:nist_glossary2002}} (Glossary, "survey")

## Worked example

A population has 1000 households. A survey draws 50 of them and finds that 35 have a working smoke alarm. The sample proportion is \(35/50 = 0.7\). The sampling fraction is \(50/1000 = 0.05\). A census would have used the fraction \(1000/1000 = 1\) and would not have had this sampling error. The survey's 0.7 is an estimate for the city, and the design, not the arithmetic of 35 and 50 alone, decides how far that estimate can be trusted.{{cite:dodge2008}} (pp. 532–533)

**Your turn.** The draw is enlarged to 80 households, of whom 60 have a working alarm. What are the sample proportion and the sampling fraction?

::: {.callout-tip collapse="true" title="Answer"}
The sample proportion is \(60/80 = 0.75\). The sampling fraction is \(80/1000 = 0.08\).
:::

## Common misconceptions

A survey is not a census of a willing minority. People who answer because they were easy to find are a convenience sample, and the population they represent is not the one named in the question. The proportion in the sample is not the city's proportion until the selection and the non-response have been faced. If only a fraction of the drawn households answer, the answered subset can differ from the drawn sample, and that difference is non-response error. A larger draw from a frame that never listed the households of interest does not repair coverage error.{{cite:nist_glossary2002}} (Glossary, "convenience sample"){{cite:nist_glossary2002}} (Glossary, "nonresponse error"){{cite:nist_glossary2002}} (Glossary, "coverage error"){{cite:openintro2019}} (Ch. 1, §1.3.5)

## Connections

[Sampling](sampling.qmd) builds the restricted part. [Survey methodology](survey-methodology.qmd) is the body of technique for the questionnaire, the draw, and the non-response. The [sample](sample.qmd) and the [population](population.qmd) are the two sets in the definition. [Data collection](data-collection.qmd) also includes registers and experiments, which are not surveys. A [cohort study](cohort-study.qmd) may use questionnaires, as the Nurses' Health Study does, and its defining feature is the follow-up rather than a single cross-section. Sampling replaced the presumption that only a complete enumeration was scientific, a presumption still dominant at the 1895 Bern congress and abandoned as a serious alternative by the time of the 1925 Rome congress. The 1936 failure of a telephone frame made the error of a bad survey visible to a wide audience. The administrative ancestor of counting everyone is the census.{{cite:openintro2019}} (Ch. 1, §1.3.4){{cite:dodge2008}} (pp. 152, 468–469)
