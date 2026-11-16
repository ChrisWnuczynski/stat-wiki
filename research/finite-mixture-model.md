# Finite mixture model

Type: Concept/definition. Rank 59.

## Material checked

- **Checked:** The frozen article has 736 body words, no figures, the Gaussian $0.3N(0,1)+0.7N(4,1)$ example, label-switching and likelihood-singularity warnings, a binary-coordinate location-model extension, an infobox and ten question links. Those are preserved. The malformed “surveyed by .” wording in the source chapter was corrected.
- **Checked:** McLachlan and Peel's Wiley publisher page establishes the 2000 book's scope and the contents of Chs. 1, 2, 5 and 6; Ch. 5's contents list GLM mixtures. The full chapter text was unavailable, so the article cites this page only for scope and summaries, not for detailed proofs. Official scikit-learn §2.1 supports Gaussian component models, EM, covariance constraints, singularities, initialization and model-count assessment. The independently derived mixture equations are proved on the page.
- **Checked:** Pearson's 1894 public-domain original, pp. 71–72, explicitly considers a skew curve arising from two or more normal groups. Its DOI and publication information were checked on the Royal Society publisher record. The 1977 Dempster–Laird–Rubin publisher abstract supports its incomplete-data EM scope; the full paper was not accessible here.
- **Checked by code:** the inherited mean $2.8$ and variance $4.36$, worked posterior $0.9590$, practice posterior $0.007788$, covariance-parameter count $17$, and embedded bank-question arithmetic are in `checks/finite-mixture-model.py`.
- **Assumed:** The generative and iid likelihood passages condition on one fixed component family and $H$, with all component densities taken against a common measure. The singularity proof assumes at least two components with positive weights and a fixed positive-variance Gaussian component covering every observation.
- **Disputed:** Fitted components are not automatically physical groups. The number of components need not equal the number of modes. An unconstrained Gaussian mixture need not have a finite maximum-likelihood estimator. These limitations are stated with examples.

## Sources opened and used

1. McLachlan and Peel, [*Finite Mixture Models*](https://onlinelibrary.wiley.com/doi/book/10.1002/0471721182), Wiley (2000), publisher book description and chapter contents, especially Chs. 1, 2, 5, 6. Existing key `mclachlan_peel2000_book`.
2. scikit-learn developers, [*Gaussian mixture models*](https://scikit-learn.org/stable/modules/mixture.html), official §2.1, especially §2.1.1. New key `sklearn_mixture2026`.
3. Pearson, [*Contributions to the Mathematical Theory of Evolution*](https://www2.stat.duke.edu/~mukee002/CBB2012/pearson.pdf), *Philosophical Transactions A* **185** (1894), pp. 71–110, especially pp. 71–72. Public-domain original scan at a university host; publisher DOI 10.1098/rsta.1894.0003. New key `pearson1894_mixture`.
4. Dempster, Laird and Rubin, [*Maximum Likelihood from Incomplete Data via the EM Algorithm*](https://doi.org/10.1111/j.2517-6161.1977.tb01600.x), *JRSS B* **39** (1977), abstract only for history. Existing key `dempster_laird_rubin1977`.

Dodge index directory was absent from `~/statwiki-sources/dodge2008`.

## Changes and checks

The generated article has 3,173 body words and zero figures. The article adds a context lead, latent-label interpretation, moment and responsibility derivations, Gaussian singularity proof, worked numeric posterior, hidden-answer practice, distinct misconceptions and concrete limits, two answered bank questions, and sourced history. The original definition, example, binary-coordinate discussion, infobox and links remain. Verification: the generator built 718 articles and 557 questions; all 67 Python tests pass; offline bibliography verification covers 445 entries; `git diff --check` passes. Full Quarto HTML rendering is unavailable because Quarto is not installed; the generator uses the system Pandoc shim.

Final rank-67 citation gate standardized publisher-section locators in this article’s research content; the rebuilt page has 3,170 body words. The numerical check and full 67-test suite pass.
