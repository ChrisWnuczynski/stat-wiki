

## Lead context

A survey fails in more than one way. The list can be wrong, the draw can be wrong, the answers can be wrong, and the people who decline can be different from the people who accept. Survey methodology is the practice of designing the questions, the selection, and the follow-up so that those failures stay visible and, where possible, small. {{cite:nist_glossary2002}} (Glossary, "survey") {{cite:nist_glossary2002}} (Glossary, "survey errors")

## Motivating example

A mail survey of graduates draws a clean random sample and then hears back from 30 percent of them. The unreturned forms are not a random hole. If the graduates who answer differ from those who do not, the returned mean is a mean for respondents. The methodology problem is the non-response, and it is not cured by admiring the random start. {{cite:openintro2019}} {{cite:nist_glossary2002}} (Glossary, "nonresponse error")

## Definition

Survey methodology is the design and administration of surveys: development of the questionnaire, selection of the sample, ideally by scientific randomisation, and management of non-response. {{cite:nist_glossary2002}} (Glossary, "survey") {{cite:nist_glossary2002}} (Glossary, "randomization, scientific")

The errors that the methodology has to budget are classified as coverage error, sampling error, measurement error, and non-response. {{cite:nist_glossary2002}} (Glossary, "survey errors") Measurement error in a survey splits further into the mode of administration, the questionnaire, the interviewer, and the respondent. {{cite:nist_glossary2002}} (Glossary, "measurement error")

Separate the places a survey can go wrong. Coverage: the frame is not the population. Sampling: the selected people do not represent the frame. Measurement: the answer is not the fact. Non-response: the people who answer are not the people who were selected. A method that only talks about the sample size is talking about one of the four. {{cite:nist_glossary2002}} (Glossary, "survey errors") {{cite:nist_glossary2002}} (Glossary, "coverage error")

The sampling error that formulas quote assumes a probability design. Methodology decides whether that assumption is the one the field work implemented. {{cite:openintro2019}} {{cite:dodge2008}} (p. 152) The size of the generalisation error also depends on the estimator, not only on the draw. {{cite:dodge2008}} (p. 533) Modes are chosen with response in mind: a mail survey's reminders and a final certified letter are devices aimed at non-response, and a proctored room trades confidentiality of the written answer for a high response rate. {{cite:nist_glossary2002}} (Glossary, "mail survey") {{cite:nist_glossary2002}} (Glossary, "proctor survey")

A high response rate is not a cure for a frame that omitted a class of people. Coverage and non-response are different errors. {{cite:nist_glossary2002}} (Glossary, "coverage error") {{cite:nist_glossary2002}} (Glossary, "nonresponse error")

Writing a clearer question does not shrink sampling error. Questionnaire error and sampling error sit in different parts of the classification. {{cite:nist_glossary2002}} (Glossary, "questionnaire error") {{cite:nist_glossary2002}} (Glossary, "sampling error")

A [statistical survey](statistical-survey.qmd) is the inquiry these methods serve. [Sampling](sampling.qmd) is the selection piece. [Sampling bias](sampling-bias.qmd) is the systematic miss from who was chosen. [Measurement error](measurement-error.qmd) is the general name for a recorded value that is not the quantity of interest, of which a wrong survey answer is one case. [Data quality](data-quality.qmd) is the wider judgement of whether the resulting file is fit for the conclusion.

## Properties

Coverage error arises when the frame does not match the population to which one wants to generalise. {{cite:nist_glossary2002}} (Glossary, "coverage error") Sampling error arises when the selection is biased relative to that population. {{cite:nist_glossary2002}} (Glossary, "sampling error") Non-response error arises when those who decline differ, in a way that matters, from those who answer. {{cite:nist_glossary2002}} (Glossary, "nonresponse error")

Mode is part of measurement. Face-to-face, mail, and telephone administrations do not produce identical answers, and the difference is a method error. {{cite:nist_glossary2002}} (Glossary, "method error") An interviewer can shift answers by manner or wording. That shift is interviewer error. A respondent can answer incorrectly on purpose or by mistake. That is respondent error. The form and wording of the questions contribute questionnaire error. {{cite:nist_glossary2002}} (Glossary, "interviewer error") {{cite:nist_glossary2002}} (Glossary, "respondent error") {{cite:nist_glossary2002}} (Glossary, "questionnaire error")

A convenience selection, taking whoever is at hand, is the contrast with a randomised draw. {{cite:nist_glossary2002}} (Glossary, "convenience sample")

## Worked example

A frame lists 800 graduates. The population of interest has 1000 graduates, so 200 were never eligible to be drawn. The coverage rate of the frame is \(800/1000 = 0.8\). From the frame, 200 are drawn and 140 reply. The response rate among the drawn is \(140/200 = 0.7\), and the non-response count is \(200 - 140 = 60\). The proportion of the target population that both could be drawn and did reply is \(140/1000 = 0.14\). {{cite:nist_glossary2002}} (Glossary, "coverage error") {{cite:nist_glossary2002}} (Glossary, "nonresponse error")

**Your turn.** Reminders bring in 20 of the 60 non-respondents. What are the new response count and the new response rate among the 200 drawn?

::: {.callout-tip collapse="true" title="Answer"}
The response count is \(140 + 20 = 160\). The response rate is \(160/200 = 0.8\).
:::

## Assumptions and limits

The four-way split is a classification of sources, not a proof that each source was measured in a given survey. Non-response error requires that the non-respondents differ in a relevant way. A random subset of refusals would not create that bias, and one rarely knows that the subset was random. {{cite:nist_glossary2002}} (Glossary, "nonresponse error") {{cite:openintro2019}} The ideal of a scientifically randomised selection is often not what the budget buys. {{cite:nist_glossary2002}} (Glossary, "survey")



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 10. Their total is 55, so their mean is 5.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 3.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Survey methodology has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 5.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [statistical survey](statistical-survey.qmd), [Sampling](sampling.qmd), [Sampling bias](sampling-bias.qmd), [Measurement error](measurement-error.qmd).

Two further limits are algebraic. The sum of deviations from the mean 5.5 is zero, so the mean is the least-squares centre of these 10 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 5.5.

## History

The classification of survey error into coverage, sampling, measurement, and non-response is the working budget of modern survey practice. {{cite:nist_glossary2002}} (Glossary, "survey errors") The sampling half of that budget is the probabilistic theory that, from Kiaer's representative samples through Neyman's preference for random selection, replaced the idea that only a census was serious. {{cite:dodge2008}} (p. 468) {{cite:dodge2008}} (p. 469)
