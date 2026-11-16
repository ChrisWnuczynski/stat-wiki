# Hierarchical Bayesian model

Rank 195. Type: Model/concept. Frozen baseline: 2,923 body words and two figures. Both original figures, three property formulas, four embedded worked examples, the cattle and rat contexts, citations, infobox facts and question links are retained.

## Checked

- **Checked in full source:** Dodge (2008), printed p. 32, “Bayes, Thomas” and “Bayesian Statistics”, records publication of Bayes's essay through Price in 1763 and describes prior–likelihood updating. The complete extracted page `/workspace/statwiki-sources/dodge2008/pages/pdf-0039.txt` was read. It supports the history only, not hierarchical shrinkage.
- **Checked in the original repository book chapter:** `sources/book/chapters/bayes-08-hierarchy.qmd`, especially §§“Why hierarchical Bayes?”, “Where the shrinkage weight comes from”, “A first hierarchy: TG5 cattle studies”, “Rat tumours”, and the grid calculation. The normal precision derivation, Beta-binomial hyperposterior and study-rate conditional in the article were compared with their complete source derivations. The tutorial-class example's interpretation and a general claim about interval widths need the focused shared corrections in pending.
- **Checked by proof:** One collapsed box derives the normal conditional posterior, Beta study conditional, integrated Beta-binomial hyperposterior and law of total variance interpretation. `checks/hierarchical-bayesian-model.py` verifies all printed arithmetic in the new example, Your turn, pending questions and original q-23 example.
- **Assumed:** Conditional independent normal marks and exchangeable class means for the normal worked calculation; its population mean and two variances are treated as known. The Beta-Bernoulli bank example shares one uncertain rate and is conditionally independent given it.
- **Disputed:** Full Bayes propagates hyperparameter uncertainty, but individual credible interval widths need not all exceed those from a chosen plug-in fit. The tutorial example's printed B posterior mean remains higher than A despite much stronger shrinkage, so its question should not imply a demonstrated ordering reversal. The cattle study counts and rat-study figure cannot be reconstructed from raw study data in this worktree; figures and factual source context are preserved rather than recalculated.

## Sources used

- Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), p. 32, Bayes biography and Bayesian Statistics entry; existing `dodge2008` key for history only.
- The repository's original hierarchical Bayes book chapter was read for the mathematical and applied baseline. Its inherited Gelman, Lindley–Smith, Efron–Morris and study-paper citations remain where originally supported; new claims are derived on page rather than assigned to unread full texts.

## Changes

Added motivation, level-by-level interpretation, a consolidated proof of three inherited properties, comparison of the two figures, a fully checked tutorial-class worked example and hidden Your turn, two answered bank questions, limitations and sourced context. The generated page is more than 3,689 words and retains both figures, so its depth exceeds the rank-188 point-forecast benchmark even before these additions. Shared source corrections await integration.
