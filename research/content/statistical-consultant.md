

## Lead context

Someone asks a statistician to design a survey, to say what a messy data set can support, or to explain why a significant test is not the decision. That person may be called a consultant, an analyst, or a collaborator. The work is the same activity the ethical guidelines call statistical practice: designing collection, summarising, analysing, interpreting, and presenting data, and deploying models. The client relationship adds a duty to say what the analysis cannot do.

## Definition

A statistical consultant is a practitioner who advises a client on the design, analysis, or interpretation of data. The American Statistical Association's guidelines use a wider term, statistical practitioner, precisely so that the role is not confined to people whose job title is consultant. Practice includes designing the collection of data, summarising, processing, analysing, interpreting, and presenting it, and developing or deploying models and algorithms. The guidelines are written for individuals and are also relevant to organisations that do this work. A consultant in a university, a government agency, or a firm is inside that definition. So is a researcher doing the same tasks without the title.{{cite:asa_ethical2022}} (Purpose)

The scope is the advice and the analysis, not the client's subject matter. Deming's consulting after 1946 was statistical studies and, in Japan, sampling methods and management ideas carried to industry. The client's product was not the statistician's product. The statistician's product was the design and the interpretation.{{cite:dodge2008}} (p. 155)

## Statistical use

The consultant's technical work is whatever the question requires: a [sample](sample.qmd) design, a [randomised controlled trial](randomised-controlled-trial.qmd), a regression, a [control chart](statistical-process-control.qmd). The ethical constraint on that work is specific. The practitioner seeks to understand and mitigate known or suspected limitations, defects, or biases in the data or the methods, and communicates the consequences for the interpretation, the conclusions, and the decisions. An analysis that hides a [confounding variable](confounding-variable.qmd), a [sampling bias](sampling-bias.qmd), or a fragile model is a failure of the role even when the arithmetic is correct. Professional integrity, in the guidelines, means taking responsibility for one's work and supporting decisions with appropriate methodology, and it means representing one's capabilities honestly.{{cite:asa_ethical2022}} (Purpose)

A consulting engagement therefore has two outputs. One is an estimate, a test, or a design. The other is a statement of what would change the conclusion. The second output is not a disclaimer pasted on a report. It is part of the analysis.{{cite:asa_ethical2022}} (Purpose)



The integer list used above is a device for keeping the target fixed. With 14 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.
## History

Consulting as a named career sits beside academic statistics from early in the twentieth century. Deming's path is a documented one. After a doctorate in physics he worked for the Department of Agriculture, moved to the Census Bureau in 1939, and there started sample censuses that were later copied elsewhere. In 1946 he left the bureau to become a consultant in statistical studies and a professor at New York University. In 1947 he went to Tokyo as a consultant on sampling. From 1950, Japanese industry adopted his management teaching. The episode is a reminder that the consultant's influence can be institutional, through a census method or a factory system, and not only a single client's data set.{{cite:dodge2008}} (p. 155)

The 2022 ethical guidelines, approved by the ASA Board on 1 February 2022, are the current professional statement of what anyone in that role owes the people who rely on the work.{{cite:asa_ethical2022}} (Purpose)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 14. Their total is 105, so their mean is 7.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 5.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Statistical consultant has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 7.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [sample](sample.qmd), [randomised controlled trial](randomised-controlled-trial.qmd), [control chart](statistical-process-control.qmd), [confounding variable](confounding-variable.qmd).

Two further limits are algebraic. The sum of deviations from the mean 7.5 is zero, so the mean is the least-squares centre of these 14 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 7.5.

## Connections

Consulting is how [medical statistics](medical-statistics.qmd), [official statistics](official-statistics.qmd), and [quality control](quality-control.qmd) often meet a subject-matter specialist who is not a statistician. It is also where [misuse of statistics](misuse-of-statistics.qmd) is either interrupted or laundered. A client who wants a significant result is asking for a different service from a client who wants to know what the study can support. The guidelines' answer is that the practitioner does not exploit gaps in the rules to justify an unethical analysis. The statistical answer is the same: the design and the uncertainty stay visible in the advice.{{cite:asa_ethical2022}} (Purpose){{cite:dodge2008}} (p. 155)
