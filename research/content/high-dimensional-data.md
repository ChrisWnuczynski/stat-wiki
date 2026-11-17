## Motivating example
A measurement system can record many features for each subject without creating more independent subjects. In regression, each feature adds a direction in which coefficients may vary, while the observed design distinguishes only a limited number of such directions. High dimensionality therefore concerns the relation among sample size, design rank and the complexity of the fitted procedure. Collecting more columns and collecting more independent rows supply different information.{{cite:zhang_d2l2023}} (Ch. 3, “Generalization”, “Model Complexity” and “Dataset Size”)

## Intuition — Prediction can be identified when coefficients are not
If a design matrix $X$ has a nonzero vector $v$ in its null space, then $X(\beta+tv)=X\beta$ for every scalar $t$. All these coefficient vectors give the same fitted training values. A least-squares objective therefore cannot distinguish them. Their predictions at a new row $x_*$ differ by $t x_*^\top v$, which can be nonzero. Equal training fits alone do not imply equal predictions away from the training design. Matrix–vector multiplication makes that distinction explicit.{{cite:zhang_d2l2023}} (§2.3, “Matrix–Vector Products”)

## Properties — Centre first, then count available directions
For $n$ observations with $p$ features, write $X_c$ for the matrix whose columns are centred. Its rows add to the zero vector, so $\operatorname{rank}(X_c)\le\min(n-1,p)$. Since $S=X_c^\top X_c/(n-1)$ and a vector is in the null space of $X_c^\top X_c$ exactly when its squared norm $\|X_cv\|^2$ is zero, the sample covariance has the same rank. Thus $p>n-1$ forces singularity; $p\le n-1$ merely makes invertibility possible. Collinearity can still prevent it.{{cite:zhang_d2l2023}} (§2.3, “Matrix–Matrix Multiplication” and “Norms”)

Adding a positive ridge value $\lambda$ to the diagonal gives $S+\lambda I$. For any nonzero $v$, its quadratic form is $v^\top Sv+\lambda\|v\|^2>0$, so the regularised matrix is invertible. This operation imposes structure; it does not turn the unregularised sample covariance into an invertible matrix. The choice of penalty affects fitted coefficients and predictions and should be assessed as part of model selection.{{cite:zhang_d2l2023}} (Ch. 3, “Generalization”, “Model Selection”)

## Worked example — A visible null direction
Take three rows on four features:
$$(0,0,0,0),\quad(1,0,1,0),\quad(0,1,0,1).$$
After centring, the covariance rank is two. The vectors $(1,0,-1,0)$ and $(0,1,0,-1)$ are null directions because the first and third columns agree, as do the second and fourth. The covariance eigenvalues are $1,1/3,0,0$. Adding $0.5I$ gives eigenvalues $1.5,5/6,0.5,0.5$, making inversion possible.

For a regression through the origin on these rows, coefficient vectors $(1,2,0,0)$ and $(0,0,1,2)$ both predict $(0,1,2)$ in the training sample. At a new row $(1,0,0,0)$ they predict one and zero. The data's failure to distinguish the coefficient vectors has a concrete consequence for extrapolation.

**Your turn.** What is the largest possible sample covariance rank for four observations on ten variables?

::: {.callout-tip collapse="true" title="Answer"}
Centring limits the rank to at most $4-1=3$. At least seven covariance eigenvalues must therefore be zero.
:::

## Statistical use — Separate selection from evaluation
When many predictor combinations are tried, a favourable training or validation result can reflect the search itself. Model selection must be included within the training part of an evaluation procedure. A final test set addresses the performance of the selected procedure; repeatedly inspecting it while choosing features changes its role. Training-set improvements from adding variables are not alone evidence of better prediction.{{cite:openintro2019}} (§9.2, “Model selection”); {{cite:zhang_d2l2023}} (Ch. 3, “Generalization”, “Training, Validation, and Test Data”)

## Assumptions and limits — Dimension is relative to a task
The inequality $p>n$ is a useful warning but does not by itself determine prediction accuracy. Sparsity, low-dimensional representations, measurement quality and design geometry all affect what can be estimated. Conversely, even $p<n$ can be difficult when columns are nearly collinear or signal is weak. Scientific attribution to individual variables requires more than a successful prediction rule and more than an inverse produced by a numerical routine.{{cite:openintro2019}} (§9.1, “Introduction to multiple regression”; §9.3, “Checking model conditions using graphs”)

### Intuition
Each new independent row is a new draw from the measurement process. Each new column is a new coordinate of the same draws. Repeating a column, or recording a column that is the sum of two others, increases $p$ and adds no direction the existing columns could not already represent. The sample covariance sees directions through the centred data matrix. Its rank cannot exceed the number of centred rows, and centring itself uses up one linear constraint because the centred rows sum to zero. Hence $n$ observations support at most $n-1$ positive covariance eigenvalues, however large $p$ becomes.

In the worked matrix the three rows and four columns have centred rank $2$. Two eigenvalues are positive, $1$ and $1/3$, and two are zero. The null vectors $(1,0,-1,0)$ and $(0,1,0,-1)$ are visible in the raw matrix: the third column copies the first, and the fourth copies the second. A coefficient along a null vector changes the parameter and leaves every training fitted value fixed. A new row that is not in the row span of the training design can still feel that coefficient. The training fit and the prediction are different linear forms.

## Interpretation — Ridge fills the zero eigenvalues
If $S$ is a sample covariance and $\lambda>0$, the matrix $S+\lambda I$ has eigenvalues equal to those of $S$, each increased by $\lambda$. A zero eigenvalue becomes $\lambda$, so the regularised matrix is positive definite and invertible. In the worked example the eigenvalues $1,1/3,0,0$ become $1.5,5/6,0.5,0.5$ after adding $0.5I$. The same shift applied to eigenvalues $(4,2,0)$ with increment $0.5$ produces $(4.5,2.5,0.5)$. The algebra does not require the zero eigenvalues to have come from $p>n$. Collinear columns at $p<n$ produce the same zeros, and the same ridge repair.

The repair changes the quadratic form. For a unit vector $v$ in a former null direction, $v^\top Sv=0$ and $v^\top(S+\lambda I)v=\lambda$. Distances and precision matrices computed from the regularised matrix treat that direction as having variance $\lambda$, a number the sample did not estimate. The choice of $\lambda$ is part of the fitted procedure. Comparing predictions across values of $\lambda$ is a model-selection step and belongs inside the training portion of an evaluation.{{cite:zhang_d2l2023}} (Ch. 3, “Generalization”, “Model Selection”)

## Common misconceptions
A square, invertible sample covariance is sometimes treated as proof that every coefficient is scientifically identifiable. Invertibility says that the observed design separates the coefficient vectors: $Xv=0$ implies $v=0$. It says nothing about whether a separated coefficient is large relative to its sampling error, and nothing about whether the column is a cause of the response. With $n=6$ and $p=15$, centring forces at least $15-5=10$ covariance eigenvalues to be zero, so the unregularised covariance cannot be inverted. Collecting more features without collecting more independent subjects widens that null space.

The bound runs the other way as well. Four observations on ten variables have covariance rank at most $4-1=3$, so at least seven eigenvalues are zero. Thirty observations on five variables have room for rank $5$, and a repeated column can still make the rank smaller. The sample size permits full rank. It does not guarantee it.

## Connections
Principal-component analysis reads the same eigendecomposition as a sequence of directions of decreasing sample variance. Directions with zero variance are invisible to a covariance PCA and cannot be recovered by reordering components. A regression on the leading components is a restriction of the linear predictor to the row space of the centred design. That restriction removes the null-space ambiguity and also discards any response signal that lived in a low-variance direction. The discard is a modelling choice. High dimensionality names the setting in which that choice, or a penalty, or a sparsity assumption, has to be made because the unpenalised least-squares fit does not determine a unique coefficient vector.
