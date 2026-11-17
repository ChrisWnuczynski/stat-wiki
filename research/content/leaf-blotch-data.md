## Motivating example
A measured disease proportion lies between zero and one, but it is not automatically a binomial count divided by a known number of independent trials. The barley leaf-blotch dataset illustrates why modeling a conditional mean and modeling its variance are separate decisions. A logit mean can remain useful while the variance model changes. Generalized and quasi-likelihood fitting organize these choices through a link and a variance function.{{cite:guan_gutierrez2002_glm}} (§§1–2, pp. 379–380)

In R's faraway dataset, the response is the proportion of leaf area affected, with site and variety stored as factors. The software object has 90 observations: ten varieties at nine sites, one observation per cell. These are properties of the distributed data object, not an assertion that the response consists of 90 independent Bernoulli trials.

## Definition — An additive mean on the logit scale
For variety i and site j, write $\operatorname{logit}(\mu_{ij})=a_i+b_j$. A reference constraint, or an equivalent intercept-plus-contrasts parameterization, is needed because adding a constant to every a and subtracting it from every b leaves the predictor unchanged. The main-effects design has $1+(10-1)+(9-1)=18$ independent columns. With 90 observations it has 72 residual degrees of freedom. The use of indicator columns for qualitative factors follows the GLM design-matrix construction.{{cite:nelder_wedderburn1972}} (§1.2, p. 372)

A complete site-by-variety interaction has 90 cell-mean parameters and uses every observation. It can interpolate the cells but leaves no residual degrees of freedom for estimating a free dispersion from those cells. Thus the data do not support a fully interacted model and a separately estimated residual scale by this procedure. Structured interactions or additional replication are different possibilities.

## Interpretation — Dispersion is relative to the variance function
A quasi-binomial specification uses $\operatorname{Var}(Y_{ij})=\phi\mu_{ij}(1-\mu_{ij})$ for these unit-weight proportions. The fitted dispersion is relative to that particular variance function and denominator convention. It need not equal one, because a continuously measured proportion is different from a single Bernoulli variable. A fitted value below one does not, by itself, diagnose a mechanism such as dependence or pseudoreplication.{{cite:guan_gutierrez2002_glm}} (§2, p. 379, mean–variance specification)

For a general variance function V and logit link, $d\mu/d\eta=\mu(1-\mu)$. The quasi-score for coefficients is proportional to $X^\top D V^{-1}(y-\mu)$, where D contains those mean derivatives. A common positive $\phi$ multiplies all score components by the same factor, so the coefficient root does not depend on it. The estimated covariance and standard errors do depend on the scale.{{cite:guan_gutierrez2002_glm}} (§2, eq. 1, p. 380)

## Worked example — Refit and inspect the weighting
Using R's distributed leafblotch values, a main-effects quasi-binomial fit gives intercept $-8.054596$, dispersion $0.088781$ and 72 residual degrees of freedom. The coefficient comparing variety two with variety one is $0.150083$, with standard error $0.723685$ and t statistic $0.207388$. The estimated odds multiplier is $e^{0.150083}=1.161931$. It describes a conditional mean comparison at a common site, rather than a ratio of unadjusted disease proportions. The model structure follows the specified logit mean.{{cite:nelder_wedderburn1972}} (§1.2, p. 372)

Consider instead the variance function $V(\mu)=\mu^2(1-\mu)^2$. For the same logit link, its Fisher-scoring weight $(d\mu/d\eta)^2/V(\mu)$ equals one. The iteratively weighted least-squares information therefore has the balanced-design geometry of $X^\top X$, multiplied by the dispersion scale. A refit gives the variety-two contrast $-0.467277$ and common variety-contrast standard error $0.468680$. The change in sign shows that a variance assumption can affect coefficient estimates through weighting, even when the link and design stay fixed.{{cite:guan_gutierrez2002_glm}} (§2, eq. 1 and Fisher scoring, pp. 379–380)

At a hypothetical fitted mean $\mu=0.1$, the quasi-binomial variance function is $0.09$, while the squared function is $0.0081$. Their ratio is $0.09$. A comparison of unscaled functions is not a comparison of fitted variances unless the respective dispersion estimates are also included.

**Your turn.** At mean one-half, calculate both variance functions and the Fisher-scoring weight for each under a logit link, omitting the common dispersion factor.

::: {.callout-tip collapse="true" title="Answer"}
The functions are $1/4$ and $1/16$. Since the squared derivative is $1/16$, their scoring weights are $1/4$ and one, respectively.
:::

## Assumptions and limits — Diagnostics assess a chosen mean–variance pair
Residual plots should be read against the specified conditional mean and variance. Discrete responses produce lattice patterns even under a correct mean; continuously measured proportions have a different geometry. Changing the variance function to address a residual pattern also changes weighting and coefficient precision, so fitted contrasts should be recalculated.{{cite:guan_gutierrez2002_glm}} (§§1–2, pp. 378–380)

A quasi-likelihood specifies enough mean–variance structure for an estimating equation without necessarily specifying a full response distribution. It does not by itself provide a mechanism for generating new observations or a normalized likelihood for arbitrary model comparisons. The adequacy of the scientific sampling assumptions and the finite-sample calibration of tests remain separate questions.{{cite:guan_gutierrez2002_glm}} (§2, p. 380)

The displayed fits describe the mean proportion and a dispersion estimate for these plots. They do not supply a joint distribution from which new leaf measurements could be drawn.
