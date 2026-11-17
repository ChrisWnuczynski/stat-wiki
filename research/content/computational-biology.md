

## Lead context

A genome is a string, an expression assay is a table, and a protein structure is a set of coordinates. Computational biology is the development and use of data-analytic, theoretical, and simulation methods on biological systems, as distinct from the tools that only store and display those data.

## Definition

The NIH Biomedical Information Science and Technology Initiative, in a definition released on 17 July 2000, separated two overlapping activities. Bioinformatics is the research, development, or application of computational tools for acquiring, storing, organising, archiving, analysing, or visualising biological, medical, behavioural, or health data. Computational biology is the development and application of data-analytical and theoretical methods, mathematical modelling, and computational simulation to the study of biological, behavioural, and social systems. Both sit in the life sciences and in computing, and the consortium noted that no wording removes the overlap.{{cite:nih_bistic2000}} (17 July 2000, Preamble and Definition)

A later encyclopedia account of the same boundary says that bioinformatics is often treated as the practical side, with the emphasis on software and data analysis, and computational biology as the more theoretical side, with the emphasis on methods. In practice the labels are used interchangeably, and papers tagged with one keyword or the other are not cleanly separated by their topics.{{cite:makalowski2018}} (section "Bioinformatics versus Computational Biology")

## Statistical use

The data-analytic half of the NIH definition is ordinary statistics on biological objects. [Maximum likelihood](maximum-likelihood.qmd) and [regression](least-squares.qmd) fit a sequence model or a dose–response. [Clustering](hierarchical-clustering.qmd) and [principal components](principal-component-directions.qmd) organise expression tables and other high-dimensional assays. Simulation is used when a stochastic model of a pathway or a population is easier to run than to solve. The theoretical half is the design of those methods: an algorithm for alignment, a model for evolution along a tree, or a likelihood for an unobserved history.{{cite:nih_bistic2000}} (Definition){{cite:makalowski2018}} (section "Bioinformatics versus Computational Biology")

[Biostatistics](biostatistics.qmd) is the neighbour that grew up around clinical and epidemiological designs. Computational biology is the neighbour that grew up around molecular data and the models those data can identify. A methods paper can belong to both.{{cite:nih_bistic2000}} (Preamble)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 8. Their total is 36, so their mean is 4.5. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 2.5. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Computational biology has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 4.5 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [Maximum likelihood](maximum-likelihood.qmd), [regression](least-squares.qmd), [Clustering](hierarchical-clustering.qmd), [principal components](principal-component-directions.qmd).

Two further limits are algebraic. The sum of deviations from the mean 4.5 is zero, so the mean is the least-squares centre of these 8 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 4.5.

## Connections

[Biostatistics](biostatistics.qmd) shares likelihood, regression, and the design of comparative studies. [Epidemiology](epidemiology.qmd) shares the population questions when the biological system is a group of hosts rather than a molecule. Sequence comparison, phylogenetic models, and gene prediction are the molecular toolkit usually filed under bioinformatics and used by computational biology without a clean hand-off. The statistical content is the model and the inference. The computational content is the scale at which that inference has to run.{{cite:nih_bistic2000}} (Definition){{cite:makalowski2018}} (section "Bioinformatics versus Computational Biology")



The integer list used above is a device for keeping the target fixed. With 8 integers the mean is determined by their total, and any smaller subset has a different mean. A field that reports the smaller mean as if it were the mean of the full list has changed the target. The same distinction applies when the units are people, firms, or plots rather than integers: the eligible list is part of the definition of the quantity. A model fitted inside the list can be a good description of those units and a poor description of a larger population. Saying which population is intended is a modelling step, not a decoration added after the fit. Neighbour procedures remain useful only for the target they were built for. A confidence interval inherits the sampling model. A regression slope inherits the conditional-mean model. A survival probability inherits the rule for censored times. None of those procedures chooses the eligible list.
## History

Molecular biologists were building databases and comparing sequences in the 1960s, before either name was stable. The NIH consortium wrote the working definitions in 2000 precisely because the two phrases were already being used for overlapping work. Subsequent reviews have kept the practical-versus-theoretical contrast and have also reported that the contrast does not sort the published literature into two piles. The volume of sequence data is what made the distinction urgent: instruments that read hundreds of gigabases a day produce tables that have to be assembled, compared, and modelled, not merely stored.{{cite:makalowski2018}} (Introduction; section "Bioinformatics versus Computational Biology"){{cite:nih_bistic2000}} (17 July 2000)
