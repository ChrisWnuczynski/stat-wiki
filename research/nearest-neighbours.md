# Nearest neighbours — source check

## Sources opened
- Cover and Hart (1967), *Nearest Neighbor Pattern Classification*, full original paper hosted on Cover's Stanford author publication page, https://isl.stanford.edu/~cover/papers/transIT/0021cove.pdf. Read pp. 21–23, especially the metric-space rule, Fix–Hodges attribution, local voting discussion and asymptotic risk statement. Bibliography already contains `cover_hart1967` with DOI.
- scikit-learn developers, *Nearest Neighbors* user guide, full §§1.6.1–1.6.4 at https://scikit-learn.org/stable/modules/neighbors.html. Read metric and tie notes, classification, regression, distance weights and search algorithms.
- Hastie, Tibshirani and Friedman (2009), *The Elements of Statistical Learning*, Springer DOI landing page https://link.springer.com/book/10.1007/978-0-387-84858-7. Checked chapter title and pp. 459–483, but the full chapter was not available through that page, so the new prose does not cite it for technical claims.
- Dodge (2008), authorized index and extracted text under `/workspace/statwiki-sources/dodge2008/`. Search found no nearest-neighbours entry; no Dodge citation was added.
- Read the answered local exercise pages `ex-sl-11-2`, `ex-sl-11-4`, `ex-sl-11-7` and the current generated article to preserve its local vote, k/n, scale and Cover–Hart content.

## Fact status
- **Checked:** nearest-neighbour metric-space definition and Cover–Hart historical attribution directly in the author-hosted original, pp. 21–22.
- **Checked:** class vote, regression mean, distance weighting, ties, k choice and tree search against the scikit-learn guide §§1.6.1–1.6.4.
- **Checked:** finite-sample Bernoulli vote expectation and variance by the page proof; all worked-example distances, votes, fractions and averages by `checks/nearest-neighbours.py`.
- **Assumed:** the idealized neighbour labels share one conditional class probability and are independent for the displayed variance; real neighbours need not satisfy that approximation. The page explicitly distinguishes this from a general theorem.
- **Disputed or unresolved:** the Cover–Hart risk bound and growing-k Bayes-consistency theorem remain proof debt; the conditions and results were checked in the original introduction but are not proved on this page.

## Preservation
The definition's one-neighbour and k-neighbour rules, the soft class estimate, training-error caution, k=n behaviour, distance sensitivity, Cover–Hart statement, infobox and all six question backlinks remain in the generated article. There were no figures or worked examples on the baseline article. The pending file records the desired single-sentence lead and three answered bank IDs.
