# Kernel density estimator — rank 131

Type: Concept/definition. Baseline: 608 body words, zero figures, three direct question links. Read the generated page and the source chapter definition. Preserved the matrix-bandwidth formula, the $-1,0,2$ Gaussian example, lab link, infobox, question links and inherited history/citations.

## Material checked

- **Checked:** Larry Wasserman's author-hosted [36-705 lecture 26](https://stat.cmu.edu/~larry/=stat705/Lecture26.pdf), §§1–2 pp. 1–3, was opened in full. It develops kernel normalization, the density estimator, pointwise bias and variance, $h\asymp n^{-1/5}$ in one dimension, and the bandwidth tradeoff. The [course syllabus](https://www.stat.cmu.edu/~larry/=stat705/syllabus.pdf) identifies the course as Fall 2020, supplying the bibliography year for the undated PDF.
- **Checked:** R Core Team's official [density manual](https://search.r-project.org/R/refmans/stats/html/density.html), “Usage,” “Arguments” and “Details,” was opened. It documents Gaussian default, `bw = "nrd0"`, `adjust`, and the warning that the default is historical rather than a general recommendation.
- **Checked by code:** Gaussian ordinates, the inherited $-1,0,2$ example, new $0,0,2$ worked example, bandwidth-two calculation and hidden $0,2$ practice arithmetic are asserted in `checks/kernel-density-estimator.py`.
- **Assumed:** both small samples are illustrative independent draws from a smooth continuous population. Bias and variance approximations require an interior point, a symmetric centred kernel and smooth true density.
- **Disputed:** Wasserman's lecture-note transcription appears to assign the variance constant $c_2$ to $\int t^2K(t)dt$ while the preceding algebra uses $\int K(t)^2dt$. The page derives the latter explicitly and uses the correct $R(K)$ constant.

## History and Dodge

The official Project Euclid pages for Rosenblatt (1956) and Parzen (1962) were opened, but exposed only an embedded reader in the research interface. Stanford's official technical-report listing for Parzen's August 1961 manuscript was opened; its full repository item was inaccessible. The reader-facing attribution now cites Bowman and Azzalini (1997), §1.2 p. 4, from the authorized Oxford University Press preview (https://api.pageplace.de/preview/DT0400.9780191545696_A37880811/preview-9780191545696_A37880811.pdf). This passage explicitly names Rosenblatt (1956), Whittle (1958), and Parzen (1962) and describes the kernel smoothing construction. The original-paper metadata remains in the bibliography but is not cited for unread mathematical claims. Dodge has no direct kernel-density entry in its authorized index.

## Question bank and result

Answered bank items `ex-sl-07-5` and `ex-sl-07-6` test the training-likelihood pitfall and the bandwidth/mode interpretation; neither repeats the article's numeric example. One collapsed proof covers density normalization and the stated interior bias–variance orders. No new result remains unproved. No figure was removed.
