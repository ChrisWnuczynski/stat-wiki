## Motivating example
A model with an intercept and an indicator for every treatment has more coefficients than distinct treatment means. Adding a constant to the intercept and subtracting it from every treatment effect leaves all fitted means unchanged. Constraints choose a unique set of labels for those means. They do not supply more observations or change the underlying comparisons.{{cite:dodge2008}} (p. 113, “Contrast”)

## Definition — Identifying a factor model
For one factor with $J$ levels, write $m_j=\mu+\alpha_j$. A treatment-reference constraint sets $\alpha_1=0$, giving $\mu=m_1$ and $\alpha_j=m_j-m_1$. A sum-to-zero constraint sets $\sum_j\alpha_j=0$, giving $\mu=J^{-1}\sum_jm_j$ and $\alpha_j=m_j-\mu$. Each is a bijective parameterisation of the same $J$ cell means.

A contrast of the means is $C=\sum_jc_jm_j$ with $\sum_jc_j=0$. Its coefficient sum removes the common intercept, so it compares levels rather than their overall location. A contrast is a scientific linear functional; a coding constraint is a rule for choosing coordinates. Their names should not obscure that distinction.{{cite:nist_contrasts2002}} (§7.4.3.6, contrast definition and estimation)

For two factors, write $m_{jk}=\mu+\alpha_j+\beta_k+\gamma_{jk}$. Sum-to-zero coding requires both main-effect sums to vanish, plus every row and column sum of $\gamma$ to vanish. Then $\mu$ is the unweighted average of the cell means, $\alpha_j$ is its row mean minus $\mu$, $\beta_k$ is its column mean minus $\mu$, and $\gamma_{jk}$ is the residual departure from additivity. In a balanced experiment this unweighted average also equals the overall observation mean. With unequal cell sizes those averages can differ.

## Properties — What changes and what is invariant
Full-rank recodings multiply the model matrix by an invertible change-of-coordinates matrix. They leave its column space and least-squares fitted vector unchanged. Residual sums of squares and a test comparing the same nested column spaces are therefore unchanged as well. Individual coefficients can have different interpretations, so testing a coefficient labelled “main effect” without specifying its coding may ask a different question.

For a contrast estimated from independent equal-variance group means, $\hat C=\sum_jc_j\bar Y_j$ and
$$\widehat{\operatorname{Var}}(\hat C)=\mathrm{MSE}\sum_jc_j^2/n_j.$$
This formula follows by adding the independent sampling variances of the weighted means. A Student calibration additionally assumes normal errors and uses the residual degrees of freedom.{{cite:nist_contrasts2002}} (§7.4.3.6, variance and confidence interval for a contrast)

## Worked example — The same four means in two coordinate systems
For the plant means $5,8,7,15$ in low/dry, low/wet, high/dry, high/wet order, reference coding gives intercept $5$, fertiliser coefficient $2$, water coefficient $3$ and interaction $5$. Sum-to-zero coding instead gives intercept $8.75$, fertiliser effects $-2.25,2.25$, and water effects $-2.75,2.75$. The interaction matrix is
$$\begin{pmatrix}1.25&-1.25\\-1.25&1.25\end{pmatrix}.$$
Adding the appropriate terms reconstructs each cell mean exactly. Every row and column sum of that matrix is zero.

Using $u=-1,+1$ for low/high fertiliser and $v=-1,+1$ for dry/wet water compresses this to
$$m(u,v)=8.75+2.25u+2.75v+1.25uv.$$
The difference in water effects is $4(1.25)=5$, whereas the reference-coded interaction coefficient is itself $5$. These coefficients differ by a factor of four because their design columns differ, not because the data show different interactions.{{cite:dodge2008}} (p. 266, two-factor interaction model)

**Your turn.** Three factor means are $4,7,10$. Find the intercept and factor effects under reference coding at the first level and under sum-to-zero coding. Compute the contrast with coefficients $(-1,0,1)$ in either coding.

::: {.callout-tip collapse="true" title="Answer"}
Reference coding gives intercept $4$ and effects $0,3,6$. Sum-to-zero coding gives intercept $7$ and effects $-3,0,3$. The contrast is $10-4=6$ in both cases; the common intercept cancels.
:::

## Statistical use — Read the conditional comparison
With an interaction, a reference-coded fertiliser coefficient measures the fertiliser difference at the reference water level. In the plant example it is $2$ under dry conditions, while under wet conditions the difference is $15-8=7$. The average difference is $4.5$ for equal weighting of the two water levels. All three descriptions are legitimate, but they describe different comparisons. Report the cell means or the explicitly weighted contrast that answers the question.{{cite:nist_contrasts2002}} (§7.4.3.6, estimating linear combinations)

## Assumptions and limits
Constraints address identifiability. Normality, independent errors, constant variance and suitable experimental design address inferential calibration and interpretation. Changing coefficient coding cannot repair an unobserved cell or a confounded design. Also, deciding to drop an interaction after a preliminary test changes the analysis procedure; simply adding its sum of squares to error is an algebraic identity, while treating the resulting tests as if the additive model were fixed in advance needs additional justification.

Two codings of the same design can look different entry by entry and still produce the same fitted means, the same residuals, and the same estimable contrasts.
