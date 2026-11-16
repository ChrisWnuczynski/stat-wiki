# Principal component directions and scores

Type: Concept. Rank 285. Tier: lighter.

## Facts

- **Checked:** ESL 12th printing, §14.5.1, p. 535, Eqs. 14.51–14.52: the centred mean is \(\bar x\), and the scores on the first \(q\) right singular vectors are \(V_q^\top(x_i-\bar x)\). Page 534 defines principal components as mutually uncorrelated projections ordered by variance.
- **Checked by code:** \(S=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)\) has eigenvalues \(3\) and \(1\). Scores of \((2,0)\) on \(a_1=(1,1)^\top/\sqrt{2}\) and \(a_2=(1,-1)^\top/\sqrt{2}\) are both \(\sqrt{2}\). The rank-one reconstruction is \((1,1)\) and the residual has squared length \(2\). Scores of \((0,2)\) are \(\sqrt{2}\) and \(-\sqrt{2}\). Fractions of trace are \(3/4\) and \(1/4\).
- **Assumed:** The sample covariance uses divisor \(n-1\), so \(\sum_i(a^\top x_i)^2=(n-1)a^\top S a\) for centred data.
- **Disputed:** Nothing numerical. The sign of each eigenvector is a convention. Hotelling (1933) and Pearson (1901) were not opened.

## Sources opened

Hastie, Tibshirani and Friedman (2009), pp. 534–535. Key `hastie_esl2009`.

## Proofs

The one-direction projection identity is proved. The full induction over successive orthogonal directions is not.
