

## Lead context

Ore grade, rainfall, and a soil pollutant are not sprinkled independently across a map. Nearby sites tend to be alike, and a histogram of the samples throws that map away. Geostatistics is the statistical treatment of measurements that come with coordinates, used to describe and to predict how a quantity is arranged in space and, when the records support it, in time.{{cite:dodge2008}} (p. 229){{cite:matheron1963}} (p. 1246)

## Definition

In the mining problems that gave the field its modern form, the targets are quantities an engineer can use: grade, thickness, accumulation, and the error of an estimate of reserves. The same idea applies to any regionalised measurement. A classical sample mean and variance can be computed from the grades, and they answer how often a grade occurs. They do not answer where the high grades sit, or how large a payable body is. The spatial arrangement is the part of the phenomenon that the estimate of reserves actually needs.{{cite:matheron1963}} (p. 1246, introduction and "Insufficiency of classical statistical concepts")

A working description used outside mining is that the data are spatial, the coordinates are known, and the analysis can be hierarchical: simple models are built locally, and those local pieces are assembled into a joint model that is still analysable. Prediction of the value at an unsampled place, and of precipitation, porosity, or a contaminant concentration, sits in that frame. Satellite images are another domain, because a pixel is a measurement with a location.{{cite:dodge2008}} (pp. 229–230)

## Statistical use

The dependence between two sites is summarised as a function of how far apart they are. The [variogram](variogram.qmd) is the usual tool: half the expected squared difference between values separated by a given lag. A variogram that rises and then levels off says that nearby samples share information and that samples beyond some range do not. Kriging uses that structure to predict a value at an unsampled location as a weighted average of the samples, with weights chosen so that the prediction error is controlled. The weights depend on the variogram and on the sample geometry, which is why a cluster of samples in one corner does not count as five independent looks at the region.{{cite:dodge2008}} (p. 230){{cite:matheron1963}} (p. 1246)

The same geometry changes every other procedure that assumes independent replicates. A [confidence interval](confidence-interval.qmd) for a regional mean that uses the ordinary sample variance treats widely scattered boreholes and a tight cluster as equivalent. A [regression](least-squares.qmd) of grade on depth that ignores location can attribute to depth a pattern that is really a patch of rich ore. [Spatial Poisson processes](spatial-poisson-process.qmd) are the point-process analogue when the data are events on a map rather than a continuous grade.

Global summaries still have a role. The histogram, the mean, and the proportion above a cutoff describe the composition of the deposit. They become misleading only when they are asked to say where the cutoff grade occurs. A reserve calculation needs both: the amount of metal and its position.{{cite:matheron1963}} (p. 1246)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 18. Their total is 171, so their mean is 9.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 7.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Geostatistics has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 9.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [variogram](variogram.qmd), [confidence interval](confidence-interval.qmd), [regression](least-squares.qmd), [Spatial Poisson processes](spatial-poisson-process.qmd).

Two further limits are algebraic. The sum of deviations from the mean 9.5 is zero, so the mean is the least-squares centre of these 18 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 9.5.

## Connections

[Time series](time-series.qmd) is the one-dimensional relative: dependence depends on lag, and a variogram is a spatial cousin of a structure function. A [spatial Poisson process](spatial-poisson-process.qmd) describes the locations themselves when the data are events on a map, such as disease cases or trees, rather than a continuous grade. Soil contamination and satellite images use the same maps when the variable is a concentration or a pixel. Location is part of the observation, and a summary that discards it answers a different question.{{cite:dodge2008}} (pp. 229–230)

## History

Hart used the word in 1954 for statistical methods applied to observations spread over a region, in a geographical setting. The theory that mining engineers now call geostatistics was formulated by Georges Matheron in the early 1960s at the École des Mines in Paris, in order to estimate reserves from samples with coordinates. He treated the grade as a regionalised variable and replaced the assumption of independent draws with a structure that could be estimated from the samples themselves. Later applied work extended the same maps to soil contamination, natural-resource evaluation, and image data.{{cite:dodge2008}} (pp. 229–230){{cite:matheron1963}} (p. 1246)
