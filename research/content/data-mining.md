

## Lead context

Large files of transactions, clicks, and instrument readings created a statistical job that is not a single method. Data mining is the practice of extracting patterns from those files with algorithms, inside a wider effort to turn the records into something a person can use.{{cite:fayyad_piatetsky_smyth1996}} (pp. 39–40) {{cite:hastie_esl2009}} (p. xi)

## Definition

Two nested meanings have to be kept apart. Knowledge discovery in databases is the whole process of finding useful knowledge in data. Data mining is one step in that process: the application of specific algorithms that extract patterns, an enumeration of patterns or models, from the prepared data. The other steps, selecting and cleaning the records, bringing in what is already known, and interpreting what the algorithm returns, are what keep the patterns from being accidents.{{cite:fayyad_piatetsky_smyth1996}} (pp. 39–40)

A statistical account of the same period describes the pressure that named the activity. Once computers made storage, organisation, and search the bottleneck, a new field grew up around those problems, and the statistician's share of it was to extract patterns and trends and to say what the data say. That share is also called learning from data, and it splits into supervised prediction of an outcome and unsupervised description of associations among inputs.{{cite:hastie_esl2009}} (p. xi)

In commercial and industrial settings the files are large in both rows and columns, the columns are a mixture of types, missing values and outliers are ordinary, and only a small fraction of the recorded inputs matter. The fitted rule is asked to be fast enough to build, readable enough to discuss, and accurate enough to act on. Predictive learning is one part of the activity, not the whole of the discovery process.{{cite:hastie_esl2009}} (pp. 350–352, §10.7)

## Statistical use

A [decision tree](decision-tree.qmd) is the method closest to an off-the-shelf procedure for this kind of file. It takes mixed inputs, tolerates missing values, is unchanged by a monotone rescaling of a numeric input, and performs its own selection of variables. Its weakness is accuracy. Boosting trees improves that accuracy and gives up some of the speed and the readability. [Binary logistic regression](binary-logistic-regression.qmd) and [nearest neighbours](nearest-neighbours.qmd) remain available when the file is clean enough for them. A neural network can predict well and is a poor explanatory tool for the same file.{{cite:hastie_esl2009}} (pp. 350–352)

Unsupervised summaries belong in the same practice. [Cluster analysis](cluster-analysis.qmd), through [hierarchical clustering](hierarchical-clustering.qmd) and K-means, looks for groups of rows. The [Apriori algorithm](apriori-algorithm.qmd) lists frequent item sets in a basket file. [Classification](classification.qmd) is the supervised piece, when the file already contains the label one wants to predict. [Cross-validation](cross-validation.qmd) is the check on a predictor. It is not, by itself, a check on an unsupervised list of rules.{{cite:hastie_esl2009}} (pp. 486–487, 492; §10.7)

The statistical obligation in the discovery process is the uncertainty of a pattern that was found by searching. A long search through even a random table produces patterns that look special. Using the algorithm and ignoring that search is the failure mode that statisticians had already called data dredging.{{cite:fayyad_piatetsky_smyth1996}} (p. 40)

## History

The phrase knowledge discovery in databases was coined at the first workshop of that name in 1989, to stress that knowledge, not the raw output of an algorithm, was the product. Data mining was already the name used by statisticians, data analysts, and information-systems groups, and it had carried a warning since the 1960s: search long enough, and a meaningless pattern appears. The discovery literature's answer was to treat mining as one step and to insist on the surrounding process.{{cite:fayyad_piatetsky_smyth1996}} (pp. 39–40)

On the statistical side, the same years put predictive and descriptive learning into one framework, with computational remarks aimed at large applications and with association rules among the successes on commercial databases.{{cite:hastie_esl2009}} (p. xi; pp. 350–352; p. 492)



A numerical boundary keeps the definition attached to a calculation. List the integers from 1 through 13. Their total is 91, so their mean is 7.0. The first three integers have mean 2. The difference between the full-list mean and that three-integer mean is 5.0. The difference is a property of which units entered the average. It is not a property of the name of the field. A procedure that averages every eligible unit estimates the mean of that list. A procedure that averages only the first three estimates a different list. Data mining has to say which list is the target before the average is interpreted.

The same arithmetic limits a model fitted to the observed rows. The mean 7.0 describes the integers that were listed. Substituting a unit that was never on the list, or a unit that was excluded by the design, replaces the target. A [confidence interval](confidence-interval.qmd) for a mean is a statement about the estimator under a stated sampling model. A [standard error](standard-error.qmd) is the standard deviation of that estimator. Neither object repairs a list that was the wrong list. The procedures already named here include [decision tree](decision-tree.qmd), [Binary logistic regression](binary-logistic-regression.qmd), [nearest neighbours](nearest-neighbours.qmd), [Cluster analysis](cluster-analysis.qmd).

Two further limits are algebraic. The sum of deviations from the mean 7.0 is zero, so the mean is the least-squares centre of these 13 numbers. A robust centre, or a median, answers a different minimisation. Reporting the mean and calling it robust does not change the criterion that was minimised. And a second variable that moves in step with these integers can dominate a regression slope. The slope then describes the joint list, which is a larger object than the one-column mean 7.0.

## Connections

[Machine learning](machine-learning.qmd) is the statistical-learning name for estimating a prediction or description rule. Data mining, in the narrower sense, is the algorithmic step that produces candidate patterns; in the broader industrial sense, it is the setting in which those rules are asked to run on messy, large files. [Supervised learning](supervised-learning.qmd) and [unsupervised learning](unsupervised-learning.qmd) are the two organisations of the rules. Pattern recognition and database research contributed procedures and the machinery for moving data that do not fit in memory. Statistics contributes the language for saying whether a discovered pattern would be expected from the search that found it.{{cite:fayyad_piatetsky_smyth1996}} (pp. 39–40) {{cite:hastie_esl2009}} (p. xi)
