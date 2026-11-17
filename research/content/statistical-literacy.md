

## Lead context

A news article says that a risk doubled. A chart starts the axis at a flattering height. A poll reports a percentage with no denominator and no sample size. Statistical literacy is the ability to read those claims as a consumer: to see what was measured, what was compared, and what the number does not say. It is not the ability to derive a sampling distribution. Courses aimed at consumers and courses aimed at future producers of analyses are different jobs, and literacy is the first of them.

## Definition

Statistical literacy is the competence of a critical consumer of statistical results, especially results reported in public. The college guidelines distinguish introductory courses that address literacy from courses that address methods, and they describe the distinction as courses for consumers versus courses for producers. The first goal they set for students is to recognise whether a reported result reasonably follows from the study and the analysis that were done. A further goal is to read a graph for what it shows and what it hides. Literacy, on that account, is about claims in the wild, not about fluency with every technique in a methods course.{{cite:gaise2016}} (pp. 7–8)

The scope includes official percentages, medical headlines, and charts in a course. It does not include, by itself, the design of a complex sample or the fitting of a hierarchical model. Those are producer skills. A literate reader knows when a producer is needed.{{cite:gaise2016}} (p. 7){{cite:openintro2019}} (Preface)

The questions a literate reading asks are standard. Was the study an experiment or an observational study? An observational comparison supports an association. It does not, on its own, support a causal sentence, because a [confounding variable](confounding-variable.qmd) can move both the supposed cause and the outcome. Who was actually measured? A convenience sample, or a survey with heavy non-response, describes the people who were reached, which may be a slice of the population named in the headline. What was the baseline? A relative risk without the absolute risk can turn a rare event into an alarming ratio. What would a [sampling bias](sampling-bias.qmd) or a flexible analysis have done to the [p-value](p-value.qmd)? The tools are imperfect, and the preface of a first course says so directly: data are messy, and the tools help when their weaknesses are understood.{{cite:openintro2019}} (Preface; Ch. 1, §1.3.4)

Graphs are part of the same literacy. A display can omit the zero, change the binning, or plot counts where rates were required. The educational goal is to say what the graph does not reveal, not only to name the kind of chart.{{cite:gaise2016}} (p. 8)



The integer list used above is a device for keeping the target fixed. With 10 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.
## History

Statistical education has long included a hope that citizens could read quantitative arguments. The 2005 college guidelines, revised and re-endorsed in 2016, made the consumer goal explicit and separated it from the producer goal. Between those editions, enrolment in introductory statistics rose sharply, and a pre-college report pushed statistical ideas into school standards, including interpretation of categorical and quantitative data. The 2016 report treats literacy courses and methods courses as a standing split in what colleges actually teach, not as a temporary compromise.{{cite:gaise2016}} (pp. 3–4, 7)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 10. Their total is 55, so their mean is 5.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 3.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Statistical literacy has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 5.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [confounding variable](confounding-variable.qmd), [sampling bias](sampling-bias.qmd), [p-value](p-value.qmd), [statistics education](statistics-education.qmd).

Two further limits are algebraic. The sum of deviations from the mean 5.5 is zero, so the mean is the least-squares centre of these 10 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 5.5.

## Connections

Literacy is the public face of [statistics education](statistics-education.qmd) and the defence against [misuse of statistics](misuse-of-statistics.qmd). It is what makes [official statistics](official-statistics.qmd) usable by people who will never see the microdata. A reader who can ask for the denominator, the design, and the absolute risk is exercising the first GAISE goal. A reader who can also build the design is doing something further, which the guidelines call a methods course. Both are legitimate. Only one of them is literacy.{{cite:gaise2016}} (pp. 7–8){{cite:openintro2019}} (Preface)
