## Lead context
Loadings are the coordinates of a unit-length principal-component direction, so each one says how strongly that variable moves the component score.

## Intuition — Weights on a unit direction
A principal component direction is a unit eigenvector of the covariance or correlation matrix used in the analysis. The score of a centred, and possibly scaled, row $z$ is the inner product of that direction with $z$. A large absolute loading means that coordinate moves the score strongly. The sign of the whole vector is arbitrary: the opposite vector spans the same line, carries the same variance, and only reverses the sign of every score.{{cite:hastie_esl2009}} (§14.5.5, p. 550, direction vectors as loadings)

## Definition — Entries of the unit eigenvector
If $v=(v_1,\ldots,v_p)^\top$ is a unit eigenvector with eigenvalue $\lambda$, the loadings of that component are the entries $v_j$. The component variance is $\lambda=v^\top Mv$, where $M$ is the matrix being decomposed. When $M$ is a correlation matrix, each coordinate was standardised to variance one, and the correlation between coordinate $j$ and the score $v^\top z$ equals $v_j\sqrt\lambda$.{{cite:hastie_esl2009}} (§14.5.5, p. 550, direction vectors as loadings)

## Properties — Flipping the direction keeps the variance
If $v$ is a unit eigenvector, so is $-v$, and $(-v)^\top M(-v)=v^\top Mv$. Sparse loadings set some of these entries exactly to zero, so that only a subset of the variables is used to read the component.{{cite:hastie_esl2009}} (§14.5.5, p. 550, sparse loadings)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The quadratic form satisfies $(-v)^\top M(-v)=v^\top M v$ because the two minus signs cancel. If $Mv=\lambda v$ and $v^\top v=1$, then $\lambda=v^\top Mv$, so the component variance is unchanged by the sign flip. For a correlation matrix the coordinates have variance one, and $\operatorname{Cov}(z_j,v^\top z)=(Mv)_j=\lambda v_j$. Dividing by the score standard deviation $\sqrt\lambda$ gives the correlation $v_j\sqrt\lambda$.{{cite:hastie_esl2009}} (§14.5.5, p. 550)
:::
:::

## Worked example
The correlation matrix $\begin{pmatrix}1&0.8\\0.8&1\end{pmatrix}$ has eigenvalues $1.8$ and $0.2$, because the characteristic equation is $\lambda^2-2\lambda+0.36=0$. A leading unit eigenvector is $(1/\sqrt2,\,1/\sqrt2)^\top$. Both loadings equal about $0.707$, and the first component accounts for $1.8/2=0.9$ of the total standardised variance. Each variable's correlation with the score is $\sqrt{0.9}\approx 0.949$. The second eigenvalue $0.2$ is the rest of the trace.{{cite:hastie_esl2009}} (§14.5.5, p. 550, loadings and component variance)

**Your turn.** Flip the leading vector to $(-1/\sqrt2,-1/\sqrt2)^\top$. What happens to the variance $1.8$, and what happens to the sign of a score?

::: {.callout-tip collapse="true" title="Answer"}
The variance stays $1.8$, because the quadratic form is unchanged. Every score changes sign.{{cite:hastie_esl2009}} (§14.5.5, p. 550)
:::

## Connections
The loadings are the entries that a [principal component direction](principal-component-directions-and-scores.qmd) uses to name a line. A correlation loading $v_j\sqrt\lambda$ is a correlation, not a second copy of the unit-vector entry. Setting some loadings to zero is a sparse variant of the same direction, obtained by adding an absolute-value penalty.{{cite:hastie_esl2009}} (§14.5.5, p. 550)

## Check yourself — Trace and a correlation
**1.** In the worked correlation matrix, what fraction of the standardised variance is left for the second component?

::: {.callout-tip collapse="true" title="Answer"}
The eigenvalues sum to the trace $2$, so the second component accounts for $0.2/2=0.1$.{{cite:hastie_esl2009}} (§14.5.5, p. 550)
:::

**2.** A unit loading of $0.6$ belongs to a component of variance $0.25$. What is the correlation between that variable and the score?

::: {.callout-tip collapse="true" title="Answer"}
The correlation is $0.6\sqrt{0.25}=0.6\times 0.5=0.3$.{{cite:hastie_esl2009}} (§14.5.5, p. 550, the correlation with the score)
:::
