# Type I and type II errors — rank 166

Type: concept. Baseline 344 words, two figures. Preserve the two normal/binomial diagrams, their numerical examples, topic links and existing bibliography where supported.

## Sources opened

- Siegrist (2022), *Probability, Mathematical Statistics, and Stochastic Processes*, full authorized §9.1, Basic Theory: Hypotheses, Errors, Power, P-value. Definitions, size as supremum under composite null, alternative-specific beta, power tradeoff and the distinction between nonrejection and acceptance.
- Dodge (2008), *The Concise Encyclopedia of Statistics*, authorized printed pp. 550–552, Type I Error/Type II Error. Definitions and 1928 Neyman–Pearson historical pointer.
- Existing first-serve and most-powerful-test answered problem pages were read for numerical cross-checks.

## Fact ledger

- **Checked:** A type I error is rejection under a true null, a type II error is nonrejection under an alternative, and power is the latter's complementary probability (Siegrist §9.1, Errors/Power).
- **Checked:** For a composite null, level bounds the supremum of false rejection probabilities; beta changes with the particular alternative (Siegrist §9.1, Errors). Discrete tests need not reach their nominal bound.
- **Checked:** First-serve binomial probabilities and normal-test areas in both figures and examples were calculated with SciPy in the focused check.
- **Checked:** Dodge p. 551 credits Neyman and Pearson's 1928 work with articulating both error types.
- **Assumed:** Independent Bernoulli serves for the binomial illustration and standardized normal sampling for the normal illustration.
- **Disputed:** Dodge p. 552 has an apparent sign error in one displayed beta definition, contradicting its correct initial definition. The page uses the initial definition, also confirmed by Siegrist. The existing wording “accept H0” is logically stronger than the standard decision “fail to reject”; the page explains the distinction.
