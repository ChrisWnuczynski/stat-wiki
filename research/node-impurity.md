# Node impurity — research record

## Sources opened

- Therneau and Atkinson, *An Introduction to Recursive Partitioning Using the RPART Routines* (2023), full official R documentation PDF at `https://stat.ethz.ch/R-manual/R-devel/library/rpart/doc/longintro.pdf`, §§1–3.2 and §4. Read the motivation for smoother splitting criteria, Gini/information rules and pruning.
- Townshend, Stanford CS229 *Decision Trees* lecture notes (2018), full Stanford-hosted original, §§2–4, especially §3 pp. 4–5 for impurity definitions, weighted split loss, entropy convention and misclassification's flat regions. This is the mathematical source cited in the article.
- scikit-learn official decision-tree user guide, full §§1.10.6–1.10.9 at `https://scikit-learn.org/stable/modules/tree`, read mathematical formulation, weighted child impurity, Gini/entropy and cost-complexity pruning.
- Dodge (2008), printed p. 231, "Gini Index" entry; this concerns the income-inequality Gini coefficient, *not* tree-classification impurity. Read to avoid conflating them.
- Baseline article (1131 words, zero figures), including all three formulas and the .8/.2 split example, compared and retained.

## Claim ledger

- **Checked:** Classification node impurity is computed from within-node class proportions; weighted child impurity is minimized in greedy split search (Stanford CS229 §§2–3). The software guides confirm specific implementation choices.
- **Checked:** Gini and entropy are smooth, concave criteria that can reward a split whose child majority labels stay the same, whereas misclassification reduction can remain zero (Stanford CS229 §3 pp. 4–5; Therneau–Atkinson §3.1, explicit 80% implementation example).
- **Checked by algebra and code:** The baseline 80/20, 70/30 and 90/10 example and the new 20-case worked split are recomputed in `checks/node-impurity.py`. Jensen's inequality gives nonnegative weighted reduction for concave impurity on empirical proportions.
- **Checked:** A local training impurity decrease is not an out-of-sample improvement; tree growth and cost-complexity pruning are different stages (Therneau–Atkinson §§1, 4; scikit-learn §§1.10.7–1.10.9).
- **Checked:** Dodge p. 231 calls the income-inequality measure "Gini index"; the identical name does not make it the class-proportion formula used by trees.
- **Assumed:** The synthetic case counts have equal observation weights and two classes; no claims about an actual clinical or other population are made.
- **Disputed/limited:** A pure training node can still generalize poorly if it contains very few cases; zero *empirical* impurity is not proof of a deterministic population class rule.
