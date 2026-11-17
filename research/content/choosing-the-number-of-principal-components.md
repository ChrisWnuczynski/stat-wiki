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
