# Boosting

Rank 338. Lighter tier. Concept page.

## Facts checked

- Schapire (1990), Machine Learning 5, pp. 197–198, as printed in the opened PDF: weak learnability means accuracy only slightly better than chance, and the paper shows this is equivalent to strong learnability.
- Freund and Schapire, December 1996 preprint of the 1997 JCSS paper, p. 12: AdaBoost, and the footnote that a Boolean update makes the error of the latest hypothesis exactly \(1/2\) on the next weights.
- Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, 2nd ed., p. 339, Algorithm 10.1: vote weight \(\log((1-\mathrm{err})/\mathrm{err})\), and misclassified weights multiplied by the exponential of that coefficient. Checked that this is twice the half-log coefficient used on the page, with the same wrong-to-correct weight ratio \((1-\varepsilon)/\varepsilon\) and the same sign of the vote.
- Half-log arithmetic for \(\varepsilon=1/4\): new weights \(1/6\) and \(1/2\), \(\alpha=\frac12\log 3\approx 0.5493\). For \(\varepsilon=1/5\), relative factor \(4\). For \(\varepsilon=0.4\), \(\alpha\approx 0.2027\) and relative factor \(1.5\). Vote \(0.6-0.2=0.4\).

## Assumed

- The half-log form already displayed on the page is the update being illustrated. The ESL full-log form is recorded as an equivalent normalisation, not as a different ensemble sign.

## Disputed

- None.

## Not opened

- Friedman, Hastie and Tibshirani (2000) on exponential loss was not opened. The exponential-loss derivation is not added. Dodge has no boosting entry in the index or in a page search.
