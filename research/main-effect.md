# Main effect

Type: Concept/definition. Rank 177.

## Material checked

- **Checked:** Frozen baseline: 455 body words, no figures, factorial model, reference-coding explanation and the variety-by-water reversal example. All original numbers and cited definitions remain.
- **Checked:** NIST/SEMATECH e-Handbook §7.4.3.7, complete official page, specifies the two-way fixed-factor model, balanced sums of squares and ANOVA degrees of freedom. §3.4.2.3, complete official page, defines first-order interaction as unequal simple differences and says main effects must be read conditionally then.
- **Checked:** Dodge (2008), printed p. 203 Fisher entry, lists Fisher's experimental-design work and 1935 book. The article does not claim an unverified first use of the term.
- **Checked by code:** The original reversal table and the two new two-by-two tables are recomputed in `checks/main-effect.py`.
- **Assumed:** Equal weighting of B levels in the displayed marginal contrasts; replicated independent observations would be needed for the usual full ANOVA error mean square.
- **Disputed:** The old lead said a main effect is a model contribution *before* interactions. In an interaction model a main-effect coefficient is often a baseline conditional contrast, while a marginal main effect averages over specified levels. Pending lead correction states the latter and its dependence on weights.

## Sources opened and used

1. Heckert et al., NIST/SEMATECH e-Handbook §7.4.3.7, “The Two-Way ANOVA,” `https://www.itl.nist.gov/div898/handbook/prc/section4/prc437.htm`; existing key `nist_two_way_anova2002`.
2. Heckert et al., NIST/SEMATECH e-Handbook §3.4.2.3, “Exploring First Order Interactions,” `https://www.itl.nist.gov/div898/handbook/ppc/section4/ppc423.htm`; existing key `nist_interactions2002`.
3. Dodge, *The Concise Encyclopedia of Statistics* (2008), p. 203, Fisher entry; existing key `dodge2008`.

## Changes and checks

One collapsed proof shows the simple, marginal and reference-cell coefficient relationships. Two existing answered bank questions are requested as hidden self-checks. Full gate results recorded in commit run.
