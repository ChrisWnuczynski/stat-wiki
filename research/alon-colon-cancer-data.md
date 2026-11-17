# Alon colon cancer data

Rank 423. Depth pass, batch X.

## Material checked

The full Alon paper and Ambroise–McLachlan paper were opened. Dimensions, gene selection convention and two-way clustering come from the original study; leakage and complete-pipeline cross-validation come from the peer-reviewed bias analysis. New matrix-rank and accuracy examples are independently checked. Exact source alon.rda preprocessing/seed is absent: copied PCA p-values, 173-gene discovery list and 14-gene lasso fit remain in place but cannot be independently refit; this limitation is staged as a todo for root.

Frozen article baseline: 544 words and 0 figures. Source examples, figures, code and results are preserved by extending generator inputs.

## Opened sources and verified locations

- `alon1999`: (§Introduction, pp. 6745–6746); (§Materials and Methods and Fig. 2, pp. 6745–6747); (§Two-Way Clustering of Gene Expression Data, Fig. 2); (§Discussion, pp. 6748–6750). [Full source](https://www.pnas.org/doi/full/10.1073/pnas.96.12.6745).
- `ambroise_mclachlan2002`: (§Introduction, p. 6562); (§Introduction, high-dimensional discrimination, p. 6562); (§Correction for Bias Selection, pp. 6563–6564); (§Correction for Bias Selection); (§Correction for Bias Selection and §Discussion, pp. 6563–6566). [Full source](https://pmc.ncbi.nlm.nih.gov/articles/PMC124442/).

Further source verification: Friedman–Hastie–Tibshirani (2010), full final JSS paper, [UC Davis copy](https://dmrocke.ucdavis.edu/Class/BST226.2014.Winter/Friedman%20Hastie%20Tibshirani%20JSS%202008.pdf), §3 pp. 8–9 eqs. 13–14 (penalised logistic likelihood), §6 pp. 16–18 and Fig. 2 (cross-validated binomial deviance and lambda choices). These support the method descriptions, not an independent reproduction of the particular 14-gene fit.

## Checks and validation

The independent check is `checks/alon-colon-cancer-data.py`. It recomputes the worked example, practice answer and numerical self-check answers, and inspects the generated article for the required results, citations and hidden exercises. Mathematical assumptions and calculation methods are stated above. Final build, offline citation verification, all 15 assigned numerical checks, full unit suite, generated-citation locator audit and diff checks are recorded in `/workspace/statwiki-run/report-x.json` after completion.

Further source verification: the full original Benjamini–Hochberg1995 paper was opened successfully through [Yekutieli’s university copy](https://www.math.tau.ac.il/~yekutiel/eBayes/bh_1995.pdf). Its §2.1 p.291 defines FDR as an expectation with zero convention at no rejections; §3.1 Thm.1 p.293 states the ordered-p-value rule and control for independent test statistics. The source method description receives that exact locator; the failed author/CMU/ISLR attempts are superseded by this full primary source.

Final validation: full generator build passed (718 articles, 626 questions, 88 figures); all 15 batch calculation/article scripts passed; offline bibliography schema passed (648 entries); all 68 unit tests passed. The exact generated-citation locator audit found zero unlocated markers in the 15 pages, hidden answers contain no citations, both preservation baselines pass, and the global whitespace check is clean. Shared source/fixture/renderer changes were validated as uncommitted orchestrator inputs; the batch commit contains only assigned research content, logs and checks.
