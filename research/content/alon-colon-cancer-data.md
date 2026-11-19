## Lead context
The expression matrix illustrates the difference between finding structure in a dataset and estimating how accurately a complete analysis will predict new tissue samples.

## Motivating example
Can a pattern of gene expression distinguish tumour tissue from normal tissue? The scientific aim motivates a classification problem, but the available number of tissues is much smaller than the number of measured genes. A flexible procedure can find promising contrasts within such a matrix, so its evaluation must account for how those contrasts were selected.{{cite:alon1999}} (§Introduction, pp. 6745–6746){{cite:ambroise_mclachlan2002}} (§Introduction, p. 6562)

## Definition — Tissues, genes and the analysis matrix
The study contains $40$ tumour and $22$ normal colon tissue samples. The arrays measured more than $6500$ genes and expressed sequence tags; the widely analysed matrix uses the $2000$ genes with the largest minimum intensity across the tissues. Its row and column conventions must be stated: a $62\times2000$ matrix has one tissue per row and one gene per column. The transposed matrix represents the same measurements with a different orientation.{{cite:alon1999}} (§Materials and Methods and Fig. 2, pp. 6745–6747)

Clustering genes groups expression profiles across tissues; clustering tissues groups measurements across genes. Those are different distance calculations and answer different questions. Standardising a gene to mean zero and unit variance changes its scale, not the distributional shape of its measurements.{{cite:alon1999}} (§Two-Way Clustering of Gene Expression Data, Fig. 2)

## Properties — The rank bottleneck
Let $X_c$ be the matrix after centring each gene across the $62$ tissues. Its rows sum to zero, so $\operatorname{rank}(X_c)\le61$. Therefore the $2000\times2000$ sample covariance matrix has rank at most $61$, with at least $1939$ zero eigenvalues. The limit follows from a linear dependence, regardless of whether the expression values are normal. The high-dimensional setting also explains why an ordinary unrestricted covariance estimate cannot support every classifier without modification.{{cite:ambroise_mclachlan2002}} (§Introduction, high-dimensional discrimination, p. 6562)

Principal components summarise variance without using the class labels. Selecting particular components after testing their association with the labels is a supervised selection step. Evaluating a classifier on the same labels then reuses information. Proper evaluation repeats that selection within each training split.{{cite:ambroise_mclachlan2002}} (§Correction for Bias Selection, pp. 6563–6564)

## Worked example
An always-tumour classifier correctly labels $40$ of the $62$ tissues, for accuracy $40/62=0.645161$. It misses all $22$ normal tissues. Reporting only overall accuracy hides that failure; class-specific performance and the target prevalence matter.

For a hypothetical evaluation with eight misclassifications among $62$ independently evaluated tissue predictions, the aggregate error fraction is $8/62=0.129032$. The predictions must come from models trained without their respective evaluation outcomes. A count of eight after selecting genes using all $62$ labels would evaluate a different, information-sharing procedure. The arithmetic is the same, but its interpretation changes.{{cite:ambroise_mclachlan2002}} (§Correction for Bias Selection)

**Your turn.** If all $2000$ null hypotheses are true and every marginal $p$-value is uniform under its null, how many $p$-values below $0.05$ are expected before a multiple-testing adjustment?

::: {.callout-tip collapse="true" title="Answer"}
The expected count is $2000(0.05)=100$. Linearity of expectation gives this result without requiring the tests to be independent. Dependence does affect other features of the count's distribution.
:::

## Statistical use — Evaluating the whole selection procedure
An evaluation split must contain the entire analysis learned from its training portion: preprocessing, feature or component selection, tuning and final fitting. A test label used to rank genes has already influenced the model, even if the classifier's last optimisation step did not use that label. Nested resampling separates tuning from evaluation when no independent final test sample is available.{{cite:ambroise_mclachlan2002}} (§Correction for Bias Selection and §Discussion, pp. 6563–6566)

A gene can be useful for prediction without having a direct causal role in tumour development. Gene–gene correlation can make several predictors interchangeable, and tissue composition can contribute broad expression patterns. The study's clustering analysis examines coordinated expression and tissue structure, rather than identifying a causal effect of changing one gene.{{cite:alon1999}} (§Discussion, pp. 6748–6750)
