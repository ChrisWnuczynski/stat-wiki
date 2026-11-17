

## Lead context

Statistics is the discipline that obtains knowledge from incomplete numerical data: how the data are collected, organised, analysed, and interpreted. The foundations are the ideas that make that programme a method rather than a pile of techniques. A population and a sample, a model that says how the data arose, and a distinction between describing what was seen and inferring beyond it are the load-bearing ones. {{cite:dodge2008}} (p. 518)

## Definition

Statistics, in the modern sense, is a discipline concerned with numerical data and with a scientific system for collecting them, organising them, analysing them, and interpreting them. Its techniques fall into two groups. Descriptive statistics put the information into a form that can be used. Inferential statistics generalise that information, which means making statements about populations from samples. {{cite:dodge2008}} (p. 518)

The empirical starting point is a set of cases and variables. A data matrix records one case per row and one variable per column. {{cite:openintro2019}} Each research question names a target population. A sample is the subset that is actually observed when the whole population cannot be. {{cite:openintro2019}} The population is the entire set of potential observations one would like to learn about. {{cite:nist_glossary2002}} (Glossary, "population")

A model is the theoretical representation that connects those observations. It contains variables and parameters. A stochastic model adds an unobservable error, so the relation holds up to that error. {{cite:dodge2008}} (p. 353) {{cite:dodge2008}} (p. 354) In the glossary split, a statistical model predicts a measured quantity and a probability model predicts the relative frequency of random outcomes. {{cite:nist_glossary2002}} (Glossary, "model")

Causal questions use a further primitive. An average causal effect is a contrast of mean potential outcomes under two actions, \(\mathrm{E}[Y^{a=1}]\) against \(\mathrm{E}[Y^{a=0}]\), not a contrast of the people who happened to receive those actions. {{cite:hernan_robins2020}} (p. 5) Data alone do not state that contrast. The actions and the population have to be stated, and the assumptions that connect the data to the contrast have to be stated too. {{cite:hernan_robins2020}} (p. vii)

## Statistical use

Description stays inside the observed file: frequencies, means, a fitted line \(y = \beta_0 + \beta_1 x + \varepsilon\) estimated by \(b_0\) and \(b_1\). {{cite:openintro2019}} {{cite:dodge2008}} (p. 518) Inference steps from the sample to the population, and it is reliable in the usual formulas when the sample was drawn in a random framework. {{cite:openintro2019}} {{cite:dodge2008}} (p. 468)

The same division organises applied work. Fundamental research in statistics is research on probabilities, on statistical methods, and on theory. The applied fields, from demography and insurance to medicine and engineering, use those methods on their own numerical records. {{cite:dodge2008}} (p. 519) A randomised experiment is the collection plan that assigns treatments when the inferential target is a causal connection. An observational collection does not assign them. {{cite:openintro2019}}

Bayesian and non-Bayesian procedures share the first two steps of a parametric analysis: name the known observations, and name a family of distributions for them. They part company on whether uncertainty about the parameter is given a prior distribution before the observations are used. {{cite:dodge2008}} (p. 33)

## History

The word statistics comes from Latin *status*, the state. Kendall reports its use by the historian Girolamo Ghilini in 1589, and dates the origin of modern statistics to about 1660. The nineteenth century supplied much of the method because experimental and human sciences needed it. The twentieth century made statistics a separate discipline, with specialised encyclopedias, because the methods had become too numerous to remain a chapter of something else. {{cite:dodge2008}} (p. 518)

The sampling half of the foundation is more recent than the census. Representative samples were still controversial at the 1895 Bern congress, and the choice among sampling methods, rather than the choice between a sample and a complete count, was the question by 1925. {{cite:dodge2008}} (p. 468) {{cite:dodge2008}} (p. 469) Mathematical models for observations were already in use in eighteenth-century astronomy, in the problems of planetary inequality, the Moon, and the shape of the Earth. {{cite:dodge2008}} (p. 353)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 17. Their total is 153, so their mean is 9.0. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 7.0. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Foundations of statistics has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 9.0 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [population](population.qmd), [sample](sample.qmd), [Sampling](sampling.qmd), [statistical model](statistical-model.qmd).

Two further limits are algebraic. The sum of deviations from the mean 9.0 is zero, so the mean is the least-squares centre of these 17 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 9.0.

## Connections

A [population](population.qmd) and a [sample](sample.qmd) are the sets inference connects. [Sampling](sampling.qmd) is how the subset is chosen. A [statistical model](statistical-model.qmd) is the representation that introduces parameters and error. [Causality](causality.qmd) adds potential outcomes when the target is an effect of an action. [Data collection](data-collection.qmd) is the step that decides whether the numbers are a register, a sample, or an experiment. The [philosophy of statistics](philosophy-of-statistics.qmd) asks what those steps assume about probability, models, and causes.
