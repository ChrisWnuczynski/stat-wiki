# Odds

Type: Concept/topic.

## Existing material read

- `articles/odds.qmd` before the edit: $p/(1-p)$ definition, probability $0.8$ to odds $4$, conditional logistic-regression coefficient interpretation, three inline citations, and 23 linked questions. Leading body: 202 words; no figures.
- `sources/book/chapters/01-introduction-to-glms.qmd` around Bernoulli natural parameter, logit, and conditional coefficient interpretation.
- `questions/c-20.qmd`, `questions/ex-sl-06-1.qmd`, `questions/ex-sl-10-2.qmd`, and `questions/c-08.qmd`, including available answers.

## Sources opened and facts used

1. Thomas Bayes, [“An Essay towards solving a Problem in the Doctrine of Chances”](https://bayes.wustl.edu/Manual/an.essay.pdf), original 1763 text, especially Richard Price's introduction and Bayes's event-count problem. Existing key `bayes1763`. The article does not attribute the first definition of odds to him.
2. Joseph Berkson, [“Application of the Logistic Function to Bio-Assay”](https://assets.super.so/934de54e-7de8-4a8b-ba45-0cc6967ed8f7/files/4c4d2123-d4b0-422e-9537-292819e1e055/berkson1944.pdf), original 1944 text opened for the preceding logit article. Existing key `berkson1944`.
3. David Cox, [“The Regression Analysis of Binary Sequences”](https://academic.oup.com/jrsssb/article/20/2/215/7027376), 1958 publisher record and description; [reproduced excerpt](https://www.ma.imperial.ac.uk/~hbattey/lshtmSh20221108.pdf) checked for logistic regression. Existing key `cox1958_logistic`.
4. NIST, [“Odds Ratio”](https://itl.nist.gov/div898/software/dataplot/refman2/auxillar/oddratio.htm), opened for the two-odds comparison and coding direction. No new citation key: the article uses existing `agresti2002`, and its formula is independently derived in the Proof box.
5. Kass and Raftery (1995), the bibliography's modern source for the Bayes-factor interpretation; the full paper was unavailable, so the odds update is directly proved with Bayes' rule and numerically checked. Existing key `kass_raftery1995`.

## Verification and decisions

- The original $p/(1-p)$ definition, $0.8\mapsto4$ example, coefficient interpretation, citations, and all 23 question links remain. No figure or example was removed.
- The collapsed proof covers odds conversion and monotonicity, reciprocal odds, the odds-ratio comparison, posterior odds from Bayes' rule, and the logistic coefficient multiplier.
- `checks/odds.py` checks the old example and the new probability, odds-ratio, and posterior-odds examples with rational arithmetic.
- History is restricted to the verified roles of Bayes, Berkson, and Cox. The origin of the ordinary word *odds* was not verified and is not claimed.
