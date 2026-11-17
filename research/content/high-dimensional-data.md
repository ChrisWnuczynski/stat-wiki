## Motivating example — Many measurements on few independent units
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
