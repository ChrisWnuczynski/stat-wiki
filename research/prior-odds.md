# Prior odds — rank 105

Type: concept. Frozen baseline 486 body words, zero figures. The source definition, factorisation, infobox and supported citations remain generated.

## Sources read

- **Checked:** Gelman et al., *Bayesian Data Analysis*, 3rd ed., authorized author-hosted PDF https://sites.stat.columbia.edu/gelman/book/BDA3.pdf, Ch. 1 §1.3 pp. 7–8 and §1.4 pp. 8–10; Ch. 7 §7.4 pp. 182–184. Read odds Bayes identity, sequential conditioning, discrete-model Bayes factors and their dependence on proper marginal likelihoods.
- **Checked:** Dodge, *The Concise Encyclopedia of Statistics* (2008), printed pp. 30–32, Bayes entries for publication history and general orientation.
- **Checked by code:** `checks/prior-odds.py` evaluates new sensor examples, sensitivity counterexample and the three selected bank calculations, as well as odds identities.
- **Assumed:** Sensor rates describe the inspected population. Sequential product factors require independence conditional on each hypothesis.
- **Disputed:** Treating pairwise odds among several models as unconditional model probabilities is wrong; the prose states the conditioning. The source's Kass–Raftery citation remains, but was not newly used to support claims.

## Proof and bank

One collapsed proof derives the odds factorisation, sequential likelihood ratio and odds-to-probability conversion. Answered questions: `ex-sl-06-1`, `q-21`, `q-44`.
