# Gram matrix

Type: Concept. Rank 278. Tier: lighter.

## Facts

- **Checked:** Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, 12th corrected printing, define \(K(x,x')=\langle h(x),h(x')\rangle\) and require a symmetric positive semidefinite kernel (Ch. 12, §12.3, p. 424, Eq. 12.21). On p. 437, Eq. 12.48, the \(N\times N\) matrix \(HH^\top\) has entries \(K(x_i,x_{i'})\).
- **Checked by code:** For inputs \((1,0)\), \((0,1)\), \((1,1)\) the linear Gram matrix is as printed, with eigenvalues \(0,1,3\). The quadratic form at \(c=(1,-1,1/2)\) equals \(2.5\). The two-point matrix on \(1\) and \(-1\) has eigenvalues \(0\) and \(2\), and \(c=(1,1)\) gives quadratic form \(0\). The orthogonal pair \((2,0)\), \((0,3)\) gives \(\operatorname{diag}(4,9)\). The cancellation \(c=(1,1,-1)\) gives \(0\).
- **Assumed:** The feature map takes values in a real inner-product space, so the squared norm identity applies.
- **Disputed:** Nothing in the numerical identities. Mercer's theorem on continuous domains was not opened; the article proves only the finite inner-product case.

## Sources opened

1. Hastie, Tibshirani and Friedman (2009), ESL 12th printing, pp. 424, 428 and 437. Key `hastie_esl2009`, author-hosted PDF.
2. Dodge (2008) index: no Gram-matrix entry. Not cited.

## Proofs

Finite positive-semidefiniteness is proved on the page. The spectral form of Mercer's theorem is not.
