# Histogram: source and verification notes

Type: concept/method. Baseline: 189 words and zero figures. Preserve the inherited definition, the creatinine shape example and its three citations, infobox, and the two question backlinks. The new content reuses the existing three-panel creatinine figure from the source chapter (one figure after the build), adds area-normalised density bins, a checked worked example and two exact new bank questions.

## Checked

- NIST/SEMATECH e-Handbook, “1.3.3.14 Histogram,” full official page https://www.itl.nist.gov/div898/handbook/eda/section3/histogra.htm. Read its Definition, two normalisations, Questions and Related Techniques. It distinguishes count, relative-frequency and density heights, and warns that area is the density scale.
- David W. Scott (1979), original full paper hosted on his Rice University faculty site, https://www.stat.rice.edu/~scottdw/stat550/DEMOS/09-19-hist-bw/scott-hist-biometrika.pdf. Read §§1–5, pp. 605–609, especially asymptotic integrated MSE and normal-reference width. It supports the $n^{-1/3}$ width order and $3.49s n^{-1/3}$ working rule, with caution on small samples and non-Gaussian shapes.
- Dodge (2008), authorised extracted text `/workspace/statwiki-sources/dodge2008/pages/pdf-0245.txt`, printed p. 243, “Histogram,” read. It gives area scaling, limitations and Pearson's 1895 terminology.
- NumPy official `histogram_bin_edges` documentation https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html, Notes (`fd`, `scott`, Examples), read. It gives the Freedman–Diaconis IQR formula and cautions that automatic choices are starting points.
- R official `nclass` documentation https://stat.ethz.ch/R-manual/R-devel/library/grDevices/html/nclass.html, Details and References, read. It documents the IQR rule and fallback when IQR is zero.
- Chicco and Jurman (2020), original open-access Springer article https://doi.org/10.1186/s12911-020-1023-5, Methods, read. It confirms the 299-patient heart-failure dataset. The existing three-panel creatinine figure and summary values come from `sources/stat1301/chapters/da-02-descriptive-statistics.qmd`, inspected directly.
- Pearson's 1895 original article has a public Zenodo record with DOI and PDF, https://zenodo.org/records/1432104. The PDF was too large for the browsing tool; the historical first-use claim comes from Dodge instead.
- Freedman and Diaconis (1981), original Springer publisher record https://doi.org/10.1007/BF01025868, inspected for title, authors and publication date. Full publisher text was unavailable; the IQR rule is cited to NumPy/R documentation.
- All toy bin counts, heights, areas, widths and alternative origins are recomputed in `checks/histogram.py`.

## Assumed or qualified

- The twelve- and eight-value examples and the four-value origin counterexample are constructed data, not samples from a named study.
- The figure's numeric creatinine details originate in the repository's descriptive-statistics chapter; the original research article confirms the 299 patients but does not give the histogram's exact bin edges.
- The Scott and Freedman–Diaconis choices are starting rules under assumptions, not guarantees of an optimal display for arbitrary data.

## Disputed or unavailable

- A full authorised PDF of Freedman and Diaconis's 1981 published paper and the original Pearson paper could not be opened in the browser; no unverified paper-specific theorem is asserted. The inherited Pearson, Tukey and Wasserman citations remain untouched.
- Existing question backlinks address shape indirectly or a simulation marginal, so two exact histogram questions are proposed in pending rather than claiming these test bin arithmetic.
