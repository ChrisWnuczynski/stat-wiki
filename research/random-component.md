# Rank 66: Random component

## Sources opened

- McCullagh and Nelder (1989), *Generalized Linear Models* (2nd ed.), Routledge/CRC publisher contents, “The Components of a Generalized Linear Model.”
- Penn State STAT 501, “Poisson and Nonlinear Regression,” official course page: response distribution (random term), linear predictor, and link.
- UCLA Biostat 200C GLM notes by Hua Zhou, introductory and exponential-family sections: normal, binomial, Poisson, gamma examples; mean and variance from $b'(\theta)$ and $a(\phi)b''(\theta)$.
- Dodge index directory absent from `~/statwiki-sources/dodge2008`.

## Fact audit

- **Checked:** The random component in a GLM specifies the conditional response distribution, typically an exponential-family law, and is distinct from the systematic predictor and link; McCullagh–Nelder contents, PSU, UCLA §§Introduction and Exponential family.
- **Checked:** For Poisson, $E(Y\mid x)=\mu$ and $\operatorname{Var}(Y\mid x)=\mu$; UCLA Poisson example and moments.
- **Checked:** Binomial or Bernoulli has variance determined by its mean and trial count, while Gaussian variance can have a free dispersion parameter; UCLA examples.
- **Assumed:** Conditional independence across observations is often used for a basic GLM likelihood but is a further sampling assumption, not the definition of a random component.
- **Disputed:** A random component is not a random effect; the latter adds latent variation in a mixed model.
- **Checked:** R's official `family` documentation (Usage, Arguments, Details, Value) distinguishes response-family variance functions from links and says quasi families have no likelihood-based AIC; opened directly.
- **Checked numerically:** At mean six, Poisson variance six and $P(Y=0)=e^{-6}=0.00247875$; Gamma with dispersion one half has shape two, rate one third, variance 18; $N(6,6)$ puts probability 0.00715294 below zero. At mean twelve, the same Gamma dispersion gives variance 72. Bernoulli $p=0.8$ has variance 0.16, while Poisson mean 0.8 puts 0.19120786 mass at two or more.
- **Disputed:** The UCLA notes call the second parameter of their shape-rate Gamma density a “scale”; this is an internal naming slip. The page uses the displayed density and independent NIST rate convention.

## Build audit

- Baseline 548 words and no figures; rebuilt 3,044 words and no figures.
- The copied GLM definition, original mean-six comparison, links, and existing citations remain present.
- One collapsed proof checks family variances and the Gamma comparison; no further theorem claim requires a proof log.
- `checks/random-component.py` passed; full build passed; 67 unit tests passed; offline bibliography verification passed for 457 entries; `git diff --check` passed.
