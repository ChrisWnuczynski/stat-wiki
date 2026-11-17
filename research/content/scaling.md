## Motivating example
A component analysis of height and weight can change when height is recorded in centimetres instead of metres. The people and their measurements have not changed physically, but a variance-based criterion sees a different numerical metric. Scaling specifies that metric. It can express a meaningful scientific comparison or remove an arbitrary unit difference, and its choice should be made before interpreting the resulting directions.{{cite:jolliffe_cadima2016}} (§2(c)(i), covariance and correlation matrix PCA)

## Definition — A transformation with stored constants
For a nonconstant feature $j$, standardisation uses $z_{ij}=(x_{ij}-\bar x_j)/s_j$, where $\bar x_j$ and $s_j>0$ are fitted location and scale constants. If $s_j$ is the sample standard deviation, the transformed training column has mean zero and sample variance one. Let $D=\operatorname{diag}(s_1,\ldots,s_p)$. The transformed covariance is $R=D^{-1}SD^{-1}$, the sample correlation matrix. Its diagonal entries are one and its trace is $p$.{{cite:jolliffe_cadima2016}} (§2(c)(i), equation 2.7)

Centring alone changes location without changing covariance. Multiplying a feature by $c$ multiplies its variance by $c^2$ and its covariance with an unchanged feature by $c$. Thus a common multiplier applied to every feature rescales the whole covariance matrix and preserves eigenvectors, whereas different coordinate multipliers generally change them.{{cite:jolliffe_cadima2016}} (§2(c)(i), changes of measurement units)

## Properties — Equal variance is a choice of objective
Standardisation changes the reconstruction error being minimised. Euclidean error in standardised coordinates corresponds to a weighted squared error in recorded coordinates, with weight $1/s_j^2$ for feature $j$. It therefore gives the same numerical weight to a one-standard-deviation error in each feature. That can be appropriate for mixed units, but it can also give a noisy feature as much variance as a precisely measured one. No algebraic transformation identifies scientific importance by itself.{{cite:goodfellow_bengio_courville2016}} (§2.12, squared-error PCA objective)

For PCA directions, correlation analysis solves the variance-maximisation problem after the transformation. Transforming a loading vector back to the recorded coordinates requires accounting for the scale factors: a score $a^Tz$ equals $a^TD^{-1}(x-\bar x)$. The coefficient of a recorded variable is therefore $a_j/s_j$, not simply $a_j$. Keeping the location, scales and loadings together makes the fitted transformation reproducible.{{cite:jolliffe_cadima2016}} (§2(c)(i), correlation matrix principal components)

## Worked example — Removing a unit-driven variance advantage
Suppose two uncorrelated features have sample covariance $S=\operatorname{diag}(4,1)$. Covariance PCA chooses the first coordinate as its leading direction and assigns it $4/(4+1)=80\%$ of total variance. Standardising by scales 2 and 1 gives $R=I_2$. Both transformed eigenvalues are one, and each accounts for $50\%$ of the transformed total. Every unit vector is now a variance-maximising direction, so the transformed data do not identify a unique first axis.

For a training mean vector $(4,10)$ and scales $(2,5)$, the observation $(6,5)$ becomes $(1,-1)$. A future observation $(8,15)$ becomes $(2,1)$ under those same constants. Refitting the constants on a future batch would define a different coordinate system and would change how a stored rule is applied.

**Your turn.** A variance is $0.01$ in metres squared. What is it when the same length is expressed in centimetres?

::: {.callout-tip collapse="true" title="Answer"}
Centimetres multiply each length by 100, so variance is multiplied by 100². The transformed variance is 100.
:::

## Statistical use — Fit transformations on the training data
A prediction pipeline estimates its preprocessing constants using its training observations. Validation cases then receive the already fitted transformation. Recomputing scales separately on a validation set can change the inputs to the fitted rule and can use information that would not have been available when the rule was trained. A held-out assessment should reproduce the full procedure that will be used for future cases. This is particularly important when scaling changes distances or regularisation weights.{{cite:zhang_d2l2023}} (Chapter “Linear Neural Networks for Regression”, “Generalization”, training and test distributions)

A constant feature has $s_j=0$ and cannot be standardised by division. One must decide how to handle it using the training information, for example by omitting a coordinate with no observed variation. Near-zero scales can also amplify very small differences. Missing-value handling and robust alternatives such as median and interquartile-range scaling define further choices, rather than being interchangeable versions of the same metric.{{cite:jolliffe_cadima2016}} (§2(c)(i), standardisation requiring nonzero scales)

## Common misconceptions — Standardisation does not decorrelate
Unit variances do not imply zero correlations. A correlation matrix with off-diagonal entries 0.8 still has strong dependence after each coordinate is standardised. Whitening requires an additional rotation and rescaling along positive covariance eigendirections. Likewise, neither standardisation nor whitening makes a non-Gaussian distribution Gaussian. These transformations control selected moments, not the entire joint distribution.{{cite:goodfellow_bengio_courville2016}} (§§2.7 and 3.9, eigendecomposition and covariance)
