# Apparent error — rank 169

Type: concept. Baseline 680 words, zero figures. Preserve displayed apparent-error and bias formulas, one-nearest-neighbour zero-error example, tree discussion, fixed-rule target, and all existing topic/question links.

## Sources opened

- James, Witten, Hastie and Tibshirani (2013), full authorized first-edition *An Introduction to Statistical Learning* hosted by its authors, Ch. 2 §2.2.3 pp. 33–43 (training versus test error and one-nearest-neighbour), Ch. 5 §5.1 pp. 176–185 (validation, LOOCV and $K$-fold CV), §5.2 (bootstrap).
- Efron (1983), publisher DOI page and Stanford Statistics technical-report catalogue inspected for history and bibliography only; full publisher article and Stanford report could not be accessed. No claim about its contents is cited to it in new prose.
- Dodge (2008) index checked for apparent/resubstitution error; no dedicated entry.

## Fact ledger

- **Checked:** Training error reuses fitted observations while test error concerns new observations; one-nearest-neighbour training error is zero for unique predictors but test error can be high (ISLR Ch. 2 §2.2.3 pp. 38–43).
- **Checked:** Held-out validation, LOOCV and cross-validation score points that did not build the corresponding prediction rule (ISLR Ch. 5 §5.1 pp. 176–185). The numerical nearest-neighbour example is checked in `checks/apparent-error.py`.
- **Checked:** The conditional future-error target $\mathrm{Err}(D)$ and the expected optimism expression follow the definitions; a single observed training/test pair need not respect the average ordering.
- **Assumed:** Future and training pairs come from the same distribution for the predictive interpretation; distinct feature values and the stated no-tie geometry for the one-neighbour proof.
- **Disputed:** Apparent error is *often*, not universally, optimistic. A prediction rule selected independently of the sample can have unbiased resubstitution error, and a perverse rule could be pessimistic. Efron's original article is unverified at full-text level here; the original page's citation remains in the generated source, and the pending change requests a precise accessible supporting source.
