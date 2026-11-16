# Adjusted Rand index

Rank 318. Lighter tier. Concept page.

## Sources read

- The chance correction is derived on the page from the hypergeometric falling factorial for a contingency table with fixed margins. Hubert and Arabie (1985) is cited by the source paragraph and was not reopened, so the new algebra is not given a page in that paper.

## Checked

- Table $\begin{pmatrix}2&1\\1&2\end{pmatrix}$, margins $(3,3)$, $n=6$.
- $C(3,2)=3$, pair totals $6$, $C(6,2)=15$, $I=2$.
- Apart-in-both pairs $15-6-6+2=5$. Agreeing pairs $7$. Rand index $7/15=0.4666\ldots$, printed $0.4667$.
- Expectation $6\cdot 6/15=2.4$. Ceiling $6$. Adjusted index $(2-2.4)/(6-2.4)=-1/9\approx -0.111$.
- A diagonal table with the same margins has $I=6$ and adjusted index $1$.
- All-singleton margins make the denominator zero.

## Lead

The stored lead stops at "identical partitions score". The pending file gives the plain-language completion. `article_leads.json` was not edited.
