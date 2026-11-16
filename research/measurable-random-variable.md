# Measurable random variable research notes

- **Checked:** Rick Durrett (2019), *Probability: Theory and Examples*, full fifth-edition PDF on the author's Duke site https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf . Read Ch. 1 §§1.2–1.3 pp. 10–17 and Appendix A.2 pp. 462–463. Supports inverse-image definition, threshold generator, closure, induced CDF, and Vitali non-measurability. Existing key `durrett2019`.
- **Checked:** Shafer and Vovk, *The Origins and Legacy of Kolmogorov's Grundbegriffe* (2018 revision), full author-hosted paper https://www.probabilityandfinance.com/articles/04.pdf , §5.1 p. 40. Its detailed overview identifies 1933 publication, chapter III on random variables, and chapter IV on expectation. This full treatment supports the article history claim.
- **Checked:** Springer's publisher table of contents and publication metadata for Kolmogorov (1933), https://link.springer.com/book/10.1007/978-3-642-49888-6 . The original chapter was unavailable; the metadata is retained only in these notes, not used as a reader-facing source.
- **Checked:** Dodge (2008) authorized index has no dedicated measurability entry; no technical Dodge claim used.
- **Checked by code:** All worked/Your turn interval probabilities and finite-space threshold events in `checks/measurable-random-variable.py`; the proposed new bank questions use exact finite calculations checked there too.
- **Assumed:** Real-valued maps with the Borel sigma-algebra on the codomain; probability is countably additive on the stated event sigma-algebra.
- **Disputed:** An arbitrary real function on a sample space need not be a random variable. The finite coarse-sigma-algebra and Vitali examples distinguish failure of measurability from mere discontinuity.
