

## Lead context

A firm that records every sale still has to decide what to stock, what to charge, and which customers to contact. Business analytics is the use of data, statistical and quantitative analysis, and explanatory or predictive models to drive those decisions.

## Definition

The Institute for Operations Research and the Management Sciences describes analytics as turning data into information and information into insights for better decisions. It distinguishes three kinds. Descriptive analytics summarises what has happened, or what is happening, from historical or current data. Predictive analytics uses relationships in the data to say what is likely to happen. Prescriptive analytics recommends an action aimed at an objective such as profit or service. Operations research is the close relative that applies scientific and mathematical methods, including optimisation, simulation, probability, and statistics, to decisions in complex systems.{{cite:informs_analytics}} ("What are Operations Research and Analytics?")

A management account of the same activity, following Davenport and Harris, is the extensive use of data, statistical and quantitative analysis, explanatory and predictive models, and fact-based management to drive decisions and actions. The emphasis is that the insight has to be actionable. Volume, velocity, and variety of data change the practical problem. They do not replace the decision the analysis is for.{{cite:vidgen2017}} (Introduction)

## Statistical use

Descriptive work is the reporting of what the files contain: tables, averages, and segments. Predictive work is [regression](least-squares.qmd), classification, and other models scored on new cases, with [cross-validation](cross-validation.qmd) or a held-out period as the check. Prescriptive work takes those predictions into a choice: an inventory level, a price, or an offer. [Data science](data-science.qmd) supplies much of the modelling and computing. The organisational claim in studies of analytics practice is that the models do not create value until the firm has a strategy for the data, people who can change decisions, and rules for the ethics of using the data.{{cite:vidgen2017}} (Introduction){{cite:informs_analytics}} ("What are Operations Research and Analytics?")

Machine learning adds pattern-finding that does not start from a subject-matter equation. That is useful, and it is not a substitute for a designed collection of data. A large observational file can still be the wrong file for the decision.{{cite:vidgen2017}} (Introduction)



The integer list used above is a device for keeping the target fixed. With 12 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.
## History

Operations research and management science are the older professional homes of quantitative business decisions. The phrase business analytics spread with the argument that firms which compete on quantitative analysis use data and models in routine management, not only in a specialist study. INFORMS's public definition of analytics as a scientific process from data to decisions became a standard short form. Empirical work on managers then treated the obstacle as organisational: strategy, skills, and ethics, alongside the statistical tools.{{cite:informs_analytics}} ("What are Operations Research and Analytics?"){{cite:vidgen2017}} (Introduction)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 12. Their total is 78, so their mean is 6.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 4.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Business analytics has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 6.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [regression](least-squares.qmd), [cross-validation](cross-validation.qmd), [Data science](data-science.qmd), [Econometrics](econometrics.qmd).

Two further limits are algebraic. The sum of deviations from the mean 6.5 is zero, so the mean is the least-squares centre of these 12 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 6.5.

## Connections

[Econometrics](econometrics.qmd) is the parallel activity when the decisions are macroeconomic or the data are markets and households in the economist's sense. [Data science](data-science.qmd) overlaps the predictive and computing parts. [Engineering statistics](engineering-statistics.qmd) overlaps the prescriptive part when the decision is a process setting rather than a customer offer. Official and scientific [data sharing](data-sharing.qmd) is a different release problem. Business analytics is the release of a decision inside the organisation that holds the file.{{cite:vidgen2017}} (Introduction){{cite:informs_analytics}} ("What's the difference between the two fields?")
