# Moment generating function

Rank 190. Type: Concept/definition. Frozen baseline: 562 body words, zero figures. The definition, Poisson derivative example, exponential-moment exercise and all original links are retained.

## Checked

- **Checked in full source:** Dodge (2008), printed p. 358, “Moment”, defines raw and central moments and traces the statistical term to the mechanical moment of a force. The complete extracted page `/workspace/statwiki-sources/dodge2008/pages/pdf-0358.txt` was read. It supports the historical account, not the transform uniqueness assertion.
- **Checked in the repository source chapter:** `sources/stat2003/chapters/prob-02-random-variables.qmd`, lines 108–118 and its exponential/normal/Gamma distribution discussions. The source states the MGF definition, open-interval condition, derivative relation and independent-sum product. The exercise and solution at `prob-solutions.qmd:257` provide the inherited exponential-moment example.
- **Checked by derivation:** The collapsed proof gives dominated differentiation, the independent product rule and cumulant derivatives. The lognormal counterexample follows by integrating $e^{t e^z}$ against a normal density: its positive-tail exponent dominates the quadratic normal decay. The transform uniqueness theorem is logged for a full proof.
- **Checked by code:** `checks/moment-generating-function.py` verifies the Bernoulli sum, Poisson derivatives, exponential-domain bank answer and every added printed numeric result.
- **Assumed:** Independent trials in the worked sum; finite exponential moments in an open interval for differentiation and uniqueness. The characteristic function statement requires real-valued $X$.
- **Disputed:** All finite integer moments do not imply an MGF near zero; the lognormal is a counterexample. The rational formula for an exponential MGF cannot be extrapolated beyond its integral domain.

## Sources used

- Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), p. 358, “Moment”; existing `dodge2008` key.
- The repository probability course chapter and its worked solution were read for the mathematical baseline. Its inherited Laplace, Feller and Grimmett–Stirzaker citations remain in the original definition; new claims are proved or accompanied by the opened Dodge source.

## Changes

Added motivation, domain and loss of existence, independent-sum interpretation, one collapsed proof, lognormal and dependence counterexamples, a fully checked numerical example with hidden answer, misconceptions, connections and history. Two answered bank questions and the uniqueness proof debt are pending shared integration. No original figure was present.
