## Motivating example
A large collection of correlated measurements may be compressed to a few scores for visualization or storage. The useful number of scores depends on what compression is meant to preserve. Retaining most predictor variation is a reconstruction goal; retaining information about a response is a different goal. PCA orders orthogonal directions by their variances.{{cite:jolliffe_cadima2016}} (§2(a), eq. 2.1–2.4)

## Properties — What a variance threshold guarantees
For a centered $n\times p$ data matrix $X$, let $S=X^\top X/(n-1)$ have eigenvalues $\lambda_1\ge\cdots\ge\lambda_p\ge0$. If $V_k$ contains its first $k$ eigenvectors, the reconstruction is $\widehat X_k=XV_kV_k^\top$. Expanding in the full orthonormal eigenbasis gives
$$\|X-\widehat X_k\|_F^2=(n-1)\sum_{j>k}\lambda_j.$$
The total centered sum of squares is $(n-1)\sum_j\lambda_j$. A 90% variance rule therefore bounds the relative squared reconstruction error by 10%. If the total variance is zero, the proportion is undefined: every observation equals the same point after centering. PCA's rank reduction and its SVD representation express this compression directly.{{cite:holmes_huber2019_msmb}} (§7.6, rank reduction)

::: {.callout-note collapse="true" title="Why leading directions minimize reconstruction error"}
For any rank-$k$ orthogonal projector $P$, the captured variance is $\operatorname{tr}(PS)=\sum_j\lambda_jw_j$, where $w_j=v_j^\top Pv_j$ lies in $[0,1]$ and $\sum_jw_j=k$. Moving weight from a smaller eigenvalue to a larger one cannot decrease this sum. Its maximum is $\sum_{j=1}^k\lambda_j$, attained by projection onto the leading eigenvectors. Subtracting captured from total variance proves the reconstruction identity and its optimality among rank-$k$ orthogonal projections.
:::

## Worked example — A threshold with a clear meaning
For eigenvalues $(5,2,1,0)$, total variance is eight. One component explains $62.5\%$, two explain $87.5\%$, and three explain $100\%$. A 90% rule chooses three; an 85% rule chooses two. With two components the discarded squared-error fraction is $1/8$. A zero eigenvalue does not add reconstruction information. The selection should specify both the target fraction and the covariance or correlation scaling used.{{cite:jolliffe_cadima2016}} (§2(a), eigenvalues and low-rank approximation)

**Your turn.** For eigenvalues $(6,3,1)$, how many components reach at least 90%? What fraction of squared reconstruction error remains?

::: {.callout-tip collapse="true" title="Answer"}
Two components explain $(6+3)/10=0.9$, reaching the threshold exactly. The discarded fraction is $1/10=0.1$.
:::

## Statistical use — A low-variance signal
Suppose independent centered predictors have variances 100 and 1, and a response is exactly the second predictor. The leading component captures $100/101\approx99.01\%$ of predictor variance while discarding all response information. Reconstruction and prediction can therefore select different dimensions. A prediction workflow selects dimension using validation with preprocessing fitted within each training split. The purely descriptive PCA representation itself uses the predictors.{{cite:holmes_huber2019_msmb}} (§7.5, PCA workflow; §12.4.1 and §12.7.1, validation and method selection)

For the eight-dimensional correlation example below, six components reach 90%, while three reach 75%. Neither answer is automatically preferable: they correspond to different reconstruction tolerances. For the twelve paired measurements, covariance PCA explains approximately 96.05% in its first direction, while correlation PCA explains approximately 95.67%. Rescaling changes the objective's weighting across coordinates.{{cite:jolliffe_cadima2016}} (§2(c), standardizing variables)

## Assumptions and limits
A bend in a scree diagram is a visual choice and can be ambiguous. Eigenvalues close together make individual directions unstable even when their combined subspace is useful. The sign of an eigenvector is arbitrary, so reversing a loading vector and all its scores changes no reconstruction. A component count should be recorded along with centering, scaling and the scientific purpose.{{cite:jolliffe_cadima2016}} (§2(a), eigenvector signs; §2(c), scaling)

## Lead context
Principal components order orthogonal directions by how much predictor variance they carry. Choosing how many to keep is a decision about what that ordering is being asked to preserve. A variance threshold controls the squared reconstruction error of the predictors. It does not consult a response. A prediction problem can therefore keep a different number of directions from a compression problem, even on the same matrix.{{cite:jolliffe_cadima2016}} (§2(a), eq. 2.1–2.4)

## Intuition
After centering, the total sum of squares splits into the eigenvalues of the sample covariance. Keeping the first $k$ eigenvectors retains $\sum_{j\le k}\lambda_j$ and discards the rest. For eigenvalues $(5,2,1,0)$ the total is $8$. Two components retain $7/8=0.875$, so a rule that demands at least $90\%$ does not stop at two. It takes the third component and then explains everything that the covariance can explain. A zero eigenvalue adds no further reconstruction. If two leading eigenvalues are tied, as with $(4,4,1,1)$, the first two still explain $0.8$ and the $90\%$ rule still needs the third, which reaches exactly $0.9$. The tie means that any orthonormal basis of the leading plane captures the same variance; the rule does not need a unique first component.{{cite:jolliffe_cadima2016}} (§2(a), eigenvalues and low-rank approximation)

## Definition
Let the columns of $V_k$ be orthonormal eigenvectors for $\lambda_1,\ldots,\lambda_k$. The reconstructed centered matrix is $XV_kV_k^\top$, and the residual Frobenius squared error equals $(n-1)\sum_{j>k}\lambda_j$. Among all orthogonal projections of rank $k$, this choice minimizes that error. The captured fraction is $\sum_{j\le k}\lambda_j/\sum_j\lambda_j$ when the total is positive. A target of $90\%$ means the smallest $k$ whose captured fraction is at least $0.90$. Equality is enough: if two components explain exactly $0.90$, the rule does not ask for a third. Correlation PCA replaces the covariance by the correlation matrix, which is the covariance of the standardized columns. That change reweights variables and can change both the eigenvalues and the selected $k$.{{cite:holmes_huber2019_msmb}} (§7.6, rank reduction)

## Common misconceptions
A component with a tiny variance can be the only direction a response uses. If two centered predictors have variances $100$ and $1$, and the response equals the second predictor, the leading component captures about $99.01\%$ of predictor variance and none of the response. Discarding the small component is correct for reconstruction and fatal for that prediction. A bend in a scree plot is a picture, not a unique integer. Close eigenvalues make the separate directions unstable even when the subspace they span is stable. The sign of a loading vector is arbitrary: reversing the loadings and the scores leaves every reconstruction unchanged. Finally, a variance fraction computed on the full sample is not a validation estimate of prediction error. Selecting $k$ for prediction requires the preprocessing and the choice of $k$ to be refit inside each training split.{{cite:jolliffe_cadima2016}} (§2(c), standardizing variables){{cite:holmes_huber2019_msmb}} (§7.5, PCA workflow; §12.4.1 and §12.7.1, validation and method selection){{cite:jolliffe_cadima2016}} (§2(a), eigenvector signs; §2(c), scaling)
