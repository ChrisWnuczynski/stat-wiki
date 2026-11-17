## Lead context
Principal-component directions are the orthogonal axes of greatest sample variance, and the scores are the coordinates of the centred observations on those axes.{{cite:hastie_esl2009}} (Ch. 14, §14.5.1, p. 535, Eqs. 14.51–14.52)

## Motivating example
The covariance
\[
S=\begin{pmatrix}2&1\\1&2\end{pmatrix}
\]
has eigenvalues \(3\) and \(1\), because \((2-\lambda)^2-1=0\). Unit eigenvectors are \(a_1=(1,1)^\top/\sqrt{2}\) and \(a_2=(1,-1)^\top/\sqrt{2}\). A centred point \((2,0)\) has scores
\[
a_1^\top(2,0)=\sqrt{2},\qquad a_2^\top(2,0)=\sqrt{2}.
\]
The first component carries \(3/(3+1)=3/4\) of the total sample variance. Its rank-one reconstruction is \(\sqrt{2}\,a_1=(1,1)\), and the residual \((2,0)-(1,1)=(1,-1)\) has squared length \(2\).

## Intuition — A line that keeps the most spread
After the sample mean is subtracted, the cloud has a sample covariance \(S\). A unit vector \(a\) produces the projected values \(a^\top(x_i-\bar x)\). The direction that makes those projected values as variable as possible is the first principal-component direction, and the projected values are the scores. The next direction is chosen orthogonal to the first, so it records spread that the first axis did not already capture. Flipping the sign of \(a\) flips every score and leaves the line unchanged.{{cite:hastie_esl2009}} (Ch. 14, §14.5.1, p. 535, Eqs. 14.51–14.52)

## Definition — Eigenvectors and projected coordinates
Let the centred data matrix have singular-value decomposition \(X=UDV^\top\), with the columns of \(V\) orthonormal. The first \(q\) principal-component directions are the first \(q\) columns of \(V\), and the scores of a centred point \(x_i-\bar x\) are
\[
\hat\lambda_i=V_q^\top(x_i-\bar x).
\]
{{cite:hastie_esl2009}} (Ch. 14, §14.5.1, p. 535, Eqs. 14.51–14.52) The same directions are the unit eigenvectors of the sample covariance, because that matrix is a positive multiple of \(X^\top X\) and \(X^\top X=VD^2V^\top\). The \(j\)th eigenvalue is the sample variance of the \(j\)th score.

## Properties — The score is the nearest coordinate
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Fix a unit vector \(a\). For a centred point \(x\), the squared distance from \(x\) to \(c\,a\) is \(\|x\|^2-2c\,a^\top x+c^2\). The quadratic in \(c\) is minimised at \(c=a^\top x\), and the minimal squared distance is \(\|x\|^2-(a^\top x)^2\). The number \(a^\top x\) is the score of \(x\) on the line through \(a\). Summing over the sample, \(\sum_i(a^\top x_i)^2=(n-1)\,a^\top S a\) when \(S\) uses the divisor \(n-1\). Maximising the sum of squared scores among unit vectors is the same problem as maximising \(a^\top S a\).
:::
:::

## Worked example — A \(2\times 2\) covariance

**Your turn.** Using the same directions, give the two scores of the centred point \((0,2)\).

::: {.callout-tip collapse="true" title="Answer"}
\(a_1^\top(0,2)=\sqrt{2}\) and \(a_2^\top(0,2)=-\sqrt{2}\). The second score changed sign because \(a_2\) points opposite the second coordinate. The squared scores are both \(2\), as they were for \((2,0)\).
:::

## Connections — Singular vectors and a regression line
The directions are [eigenvectors](eigenvalues-and-eigenvectors.qmd) of \(S\) and the right singular vectors in the [singular value decomposition](singular-value-decomposition.qmd) of the centred data. [Principal component directions](principal-component-directions.qmd) names the same axes; the scores are the coordinates along them. A least-squares line minimises squared error in one designated response. A principal-component line minimises squared distance to the line in all coordinates at once, which is why the two lines need not agree.

