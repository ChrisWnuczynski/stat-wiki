## Motivating example
A survey records one of several mutually exclusive categories for each respondent. The estimated shares fluctuate together: if one category's share rises, the others must collectively fall because the total is one. Separate independent normal approximations miss this constraint. The multinomial central limit theorem gives one joint Gaussian approximation on the lower-dimensional sum-zero fluctuation space.{{cite:durrett2019}} (§3.10, thm. 3.10.7 and ex. 3.10.9, pp. 200–201)

A multinomial count vector arises from a fixed number of independent trials with common category probabilities. Its cell counts are not independent, although the trials are. Distinguishing those two levels of dependence is essential before approximating their sampling distribution.{{cite:dodge2008}} (pp. 363–364)

## Statement
For $N\sim\operatorname{Multinomial}(n,p)$ with fixed $K$-component probability vector $p$, put $\widehat p=N/n$ and $\Sigma=\operatorname{diag}(p)-pp^\top$. Then
$$\sqrt n(\widehat p-p)\ \Rightarrow\ N_K(0,\Sigma).$$
The Gaussian can be singular. If every $p_k>0$, the covariance has rank $K-1$ and its null space is the span of the all-ones vector. If some probabilities are zero, the corresponding counts are zero almost surely and the rank can be smaller. The number of categories is fixed in this statement.{{cite:durrett2019}} (§3.10, thm. 3.10.7, ex. 3.10.9)

## Proof
Represent trial $i$ by a one-hot vector $Z_i$, which equals coordinate vector $e_k$ with probability $p_k$. Then $E(Z_i)=p$, $E(Z_{ij}Z_{ik})=0$ for distinct categories and $E(Z_{ik}^2)=p_k$. Consequently $\operatorname{Cov}(Z_i)=\operatorname{diag}(p)-pp^\top$. The count vector is $\sum_iZ_i$, so the vector central limit theorem gives the displayed limit.{{cite:durrett2019}} (§3.10, thm. 3.10.7 and its proof, pp. 200–201)

More explicitly, for every fixed contrast vector $a$, the scalar variable $a^\top Z_i$ is bounded and has variance $a^\top\Sigma a$. The scalar central limit theorem applies to its sample mean. The Cramér–Wold device combines all of these scalar conclusions into the joint vector conclusion, including zero-variance directions. This avoids requiring an invertible covariance matrix in the theorem.{{cite:durrett2019}} (§3.10, thm. 3.10.6)

To identify the null space, observe $a^\top\Sigma a=\sum_kp_ka_k^2-(\sum_kp_ka_k)^2$. This is the variance of the value $a_k$ under probabilities $p_k$. With all probabilities positive, it vanishes precisely when all $a_k$ are equal. The all-ones direction also has exactly zero realized error because $\sum_k(\widehat p_k-p_k)=0$.

## Worked example — A difference of two category shares
Take $p=(0.2,0.3,0.5)$ and $n=100$. The single-trial covariance is
$$\Sigma=\begin{pmatrix}0.16&-0.06&-0.10\\-0.06&0.21&-0.15\\-0.10&-0.15&0.25\end{pmatrix}.$$
The covariance of $\widehat p$ is exactly $\Sigma/100$, whether or not a normal approximation is accurate. The Gaussian shape is the asymptotic part. Every row of $\Sigma$ sums to zero, and its determinant is zero. These properties follow from the multinomial count structure.{{cite:dodge2008}} (pp. 363–364){{cite:durrett2019}} (§3.10, ex. 3.10.9)

For the contrast $\widehat p_1-\widehat p_2$, the true mean is $-0.1$. Its variance is $(0.16+0.21-2(-0.06))/100=0.0049$ and its standard deviation is $0.07$. Ignoring the negative covariance would instead use $0.0037$ and understate this contrast's uncertainty. The normal approximation is thus approximately $N(-0.1,0.0049)$ for the unscaled contrast.

**Your turn.** Combine categories one and two into a single category. Find the exact variance of their combined estimated share at n=100.

::: {.callout-tip collapse="true" title="Answer"}
Their combined probability is $0.5$. The variance is $0.5(1-0.5)/100=0.0025$. The matrix calculation gives $(0.16+0.21+2(-0.06))/100=0.0025$ as well.
:::

## Statistical use — Work with contrasts or remove one coordinate
A full inverse of $\Sigma$ does not exist for an interior probability vector. One approach drops one redundant coordinate; another works directly with contrasts that remove the sum constraint. The omitted category is still represented through the requirement that all shares sum to one. Treating singularity as a numerical rounding accident would obscure the exact geometry.{{cite:durrett2019}} (§3.10, ex. 3.10.9, p. 201)

Rare categories can make a normal approximation poor even when total sample size looks large. The fixed-probability theorem does not provide a universal finite-sample cutoff, and it does not directly cover an increasing number of categories or probabilities tending to zero with n. Exact multinomial calculations, a category-appropriate approximation or a carefully specified simulation can assess the relevant finite-sample quantities.
