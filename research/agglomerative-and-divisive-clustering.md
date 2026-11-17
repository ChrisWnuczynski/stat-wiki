# Agglomerative and divisive clustering

Rank 422. Depth pass, batch X.

## Material checked

Dodge printed pp. 82–84 and the full Murtagh–Contreras author manuscript were read. The cited paper is the peer-reviewed 2012 WIREs article; the accessible manuscript is the 2011 arXiv1105.0121 version titled Methods of Hierarchical Clustering. Section/Table locators refer to that full author version rather than guessed published page locations. Linkage definitions, inversions and divisive methods are distinguished. SciPy supplies an independent numerical cross-check, not mathematical citation evidence.

Frozen article baseline: 502 words and 0 figures. Source examples, figures, code and results are preserved by extending generator inputs.

## Opened sources and verified locations

- `dodge2008`: (pp. 82–84, Classification and Cluster Analysis); (p. 83, agglomerating and dividing techniques); (pp. 83–84, domains and limitations). [Full source](Private authorized copy: Encyclopedia of Statistics, printed pages recorded below.).
- `murtagh_contreras2012`: (§§4, 6); (§4, Table 1); (§4, dissimilarity update formulas); (§§2, 5). [Full source](https://www.cs.umb.edu/~rvetro/vetroBioComp/Clustering/Murtagh2011a%20Methods%20of%20Hierarchical%20Clustering.pdf).

## Checks and validation

The independent check is `checks/agglomerative-and-divisive-clustering.py`. It recomputes the worked example, practice answer and numerical self-check answers, and inspects the generated article for the required results, citations and hidden exercises. Mathematical assumptions and calculation methods are stated above. Final build, offline citation verification, all 15 assigned numerical checks, full unit suite, generated-citation locator audit and diff checks are recorded in `/workspace/statwiki-run/report-x.json` after completion.

Final validation: full generator build passed (718 articles, 626 questions, 88 figures); all 15 batch calculation/article scripts passed; offline bibliography schema passed (648 entries); all 68 unit tests passed. The exact generated-citation locator audit found zero unlocated markers in the 15 pages, hidden answers contain no citations, both preservation baselines pass, and the global whitespace check is clean. Shared source/fixture/renderer changes were validated as uncommitted orchestrator inputs; the batch commit contains only assigned research content, logs and checks.
