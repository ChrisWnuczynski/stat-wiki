

## Lead context

Three distributions can share a mean and a standard deviation and still look nothing alike: one with two peaks, one with a single peak, and one with a long right tail. A graph is the comparison that makes those shapes obvious. A mean and a standard deviation, printed alone, do not.{{cite:openintro2019}} (Ch. 2, §2.1.4, the three distributions with mean 0 and standard deviation 1)

## Definition

A statistical graphic plots points, bars, lines or other marks so that a data set can be read at a glance: the general behaviour, and the features that matter for the question in hand. It is a form of data representation, often the picture that accompanies or replaces a frequency table.{{cite:dodge2008}} (p. 236)

Which picture is used depends on the variable and on the question. Charts for categorical counts include the pie chart, the line chart and the pictogram. Frequency charts for a quantitative variable include the histogram and the stem-and-leaf diagram. A Cartesian plot uses perpendicular axes that meet at an origin.{{cite:dodge2008}} (p. 237) A [histogram](histogram.qmd) summarises one numerical variable: centre, spread, skewness, outliers and modes.{{cite:nist_histogram}} (§1.3.3.14, “Purpose” and “Definition”) A [scatterplot](scatterplot.qmd) shows the joint behaviour of two numerical variables, one point per case.{{cite:nist_scatterplot2002}} (§1.3.3.26, “Definition”){{cite:openintro2019}} (Ch. 2, §2.1.1) A [line chart](line-chart.qmd) is the categorical display in that first group, one frequency at each discrete value. [Summary statistics](summary-statistics.qmd) are the numerical companions of these pictures.

Exploratory analysis uses these displays heavily, and the displays are not the whole of that analysis. The analysis is the decision to look before choosing a model. The graphics are the tools used to look.{{cite:nist_eda2002}} (§1.1.1, “Philosophy”)

[Data analysis](data-analysis.qmd) is the larger activity in which these pictures are the first instruments. A [histogram](histogram.qmd) and a [scatterplot](scatterplot.qmd) are the two workhorses for numerical data, and a [line chart](line-chart.qmd) does the corresponding job for a discrete frequency. [Summary statistics](summary-statistics.qmd) report centre and spread after the picture has shown whether those summaries are enough. Shape continues in [skewness](skewness.qmd) and [kurtosis](kurtosis.qmd), and a [normal quantile plot](normal-quantile-plot.qmd) compares the sample with a normal reference more directly than a histogram does.{{cite:nist_histogram}} (§1.3.3.14, distributional model){{cite:nist_eda2002}} (§1.1.1, graphical techniques)

## Statistical use

Use a histogram to ask what population shape is plausible, where the data sit, how spread out they are, whether they are symmetric, and whether a few points stand apart. Interest rates in a sample of fifty loans, drawn as a histogram, pile up under 15% and leave a thin right tail above 20%. Observations that fall on a bin boundary go into the lower bin.{{cite:nist_histogram}} (§1.3.3.14, “Questions”){{cite:openintro2019}} (Ch. 2, §2.1.3)

Use a scatterplot to ask whether two variables move together, whether the relation is linear, whether the vertical spread changes with the horizontal variable, and whether a point is isolated. The plot shows association. A conclusion that one variable causes the other uses subject-matter knowledge beyond the cloud of points. Several scatterplots on one page, or a scatterplot matrix, extend the same idea past two variables.{{cite:nist_scatterplot2002}} (§1.3.3.26, “Questions” and “Causality Is Not Proved By Association”){{cite:openintro2019}} (Ch. 2, §2.1.1)

A pie chart can show how a whole breaks into categories, and a bar plot of the same counts makes the comparison of those categories easier to read. For a loan sample, the excess of mortgages over rentals is immediate in the bar plot and slower in the pie chart.{{cite:openintro2019}} (Ch. 2, §2.2.5) The line chart belongs with those categorical displays.{{cite:dodge2008}} (p. 237)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 11. Their total is 66, so their mean is 6.0. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 4.0. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Statistical graphics has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 6.0 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [histogram](histogram.qmd), [scatterplot](scatterplot.qmd), [line chart](line-chart.qmd), [Summary statistics](summary-statistics.qmd).

Two further limits are algebraic. The sum of deviations from the mean 6.0 is zero, so the mean is the least-squares centre of these 11 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 6.0.

## History

Plotting a point in a coordinate plane goes back to Greek geometry, and the mathematical development of that idea is Descartes’s. Crome used graphical statistical displays as a teaching device, including pie charts, in publications of 1785 and 1820. Playfair’s *Commercial and Political Atlas* of 1786 used line charts for trade. Guerry’s 1833 essay on the moral statistics of France is an early frequency display of crimes. Pearson later gave the histogram its name. Tukey added the box plot in 1972 and the stem-and-leaf diagram in 1977, as part of exploratory analysis. The histogram itself is older, from the eighteenth century.{{cite:dodge2008}} (pp. 192–193, 236–237)
