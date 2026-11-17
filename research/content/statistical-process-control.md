

## Lead context

A process that is left alone wanders. Tools wear, a supplier changes a batch, an operator resets a machine. Statistical process control is the habit of plotting a quality characteristic as production continues, so that a real change is noticed and ordinary variation is not mistaken for one. The chart does not repair the process. It says when someone should go and look, and the limits are set so that those looks are rare when nothing has changed.

## Definition

Statistical process control is the routine monitoring of a process by control charts, and the actions taken when the chart says the process is no longer in the state the limits describe. A control chart is a time-sequence plot of a statistic or of individual measurements, with a central line and one or more statistically derived control limits. Univariate charts track one characteristic. Multivariate charts track a summary of several. Process control, as distinct from the monitoring, is the change made once an out-of-control signal appears: a person follows an action plan, or an automated loop adjusts the process. Monitoring without that response is a record. Adjustment without a signal is tampering.{{cite:nist_glossary2002}} (Glossary, "control chart"){{cite:nist_pmc13_2002}} (§6.1.3){{cite:nist_pmc31_2002}} (§6.3.1)

The subject is a part of [quality control](quality-control.qmd), not the whole of it. Acceptance sampling judges a lot. Capability judges whether a stable process can meet a specification. A control chart judges whether the process is still the same process.

Process control sits downstream of monitoring and upstream of designed experiments. If the chart says the process is stable and the output is still unacceptable, the next step is to change the process, not to tighten the limits until ordinary variation looks special. The risk being spent is the risk of searching for an assignable cause when none exists, and that risk is chosen by where the limits are drawn. A [confidence interval](confidence-interval.qmd) for a mean answers a different question: it estimates a fixed quantity. A control limit is a boundary for future points from a process that is supposed to stay put.{{cite:nist_pmc31_2002}} (§6.3.1){{cite:nist_pmc13_2002}} (§6.1.3)

## Statistical use

The centre line is a mean for the in-control process. The upper and lower control limits are placed so that nearly all points fall inside them while only chance causes operate. If the plotted statistic is normal, limits at three standard deviations leave about 0.00135 of the probability in each tail, or about 0.0027 in both, which is why three-sigma limits are treated as a practical stand-in for 0.001 probability limits. The multiple 3 is a convention, used in the United States whether or not the statistic is exactly normal, and it may be a known standard deviation, an estimate, or a standard value adopted for the chart. British practice has more often preferred limits that are true probability limits.{{cite:nist_pmc31_2002}} (§6.3.1)

A point outside the limits is a prompt to look for an assignable cause. Points that stay inside the limits can still be out of control if the pattern is systematic: a long run on one side of the centre line is not the random scatter the limits assume. "In control" means both that the points lie between the limits and that they do not form a pattern. Skewness moves the chance of a false signal. For a Poisson count with mean 0.8, the upper three-sigma limit is $0.8+3\sqrt{0.8}=3.48$, and the chance of exceeding three successes is about 0.009 rather than 0.001. The chart is then a little more willing to declare a high count special than a normal calculation would suggest.{{cite:nist_pmc31_2002}} (§6.3.1)

Shewhart charts for means and ranges, charts for individuals, cumulative-sum charts, and exponentially weighted moving-average charts are variants of the same display: a statistic in time order, judged against limits built from the in-control process.{{cite:nist_pmc2002}} (Ch. 6)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 15. Their total is 120, so their mean is 8.0. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 6.0. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Statistical process control has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 8.0 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [quality control](quality-control.qmd), [confidence interval](confidence-interval.qmd).

Two further limits are algebraic. The sum of deviations from the mean 8.0 is zero, so the mean is the least-squares centre of these 15 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 8.0.

## History

Shewhart's 16 May 1924 memorandum sketched the chart, and his 1931 book set the pattern for later process control. The distinction he used, between chance causes and assignable causes, is the distinction the limits still encode. Sampling inspection, developed alongside the charts at Bell Laboratories, is a sister method rather than a chart. Deming's later consulting carried statistical control into industrial management, especially in Japan after 1950, but the chart itself is Shewhart's device.{{cite:nist_pmc11_2002}} (§6.1.1){{cite:dodge2008}} (p. 155)
