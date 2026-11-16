# False discovery rate

Rank 342. Lighter tier. Concept page.

## Facts checked

- Hastie, Tibshirani and Friedman, 2nd ed., p. 687: \(\mathrm{FDR}=\mathrm{E}(V/R)\), family-wise error \(\mathrm{P}(V\ge 1)\), and under independence \(\mathrm{FDR}\le (M_0/M)\alpha\le\alpha\) (eq. 18.45). They note that the proof of the procedure's bound is complicated.
- Algorithm 18.2, p. 688: reject up to the largest \(j\) with \(p_{(j)}<\alpha j/M\).
- Sorted \(p\)-values \(0.001,0.04,0.06,0.8\). At level \(0.1\) the thresholds are \(0.025,0.05,0.075,0.1\) and the largest index is \(3\). At level \(0.05\) the thresholds are \(0.0125,0.025,0.0375,0.05\) and the largest index is \(1\), because \(0.04\not<0.025\).
- Two tests at level \(0.05\): thresholds \(0.025\) and \(0.05\), both rejected. The inequality \(Q\le 1_{\{V\ge 1\}}\) was checked on the two cases \(V=0\) and \(V\ge 1\).

## Assumed

- The page's convention \(Q=0\) when \(R=0\) is the quantity whose expectation is bounded by the family-wise error. ESL's displayed \(\mathrm{E}(V/R)\) is cited for the ratio among called genes, not as a claim that they discuss the empty list.

## Disputed

- None.

## Not opened

- Benjamini and Hochberg (1995) and Benjamini and Yekutieli (2001) were not opened. The independence bound is cited from ESL's statement of it, and the original argument is logged rather than reproduced. Dodge has no false-discovery entry.
