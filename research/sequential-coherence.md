# sequential-coherence

Rank 460; batch AA.

## Sources read

- `siegrist2022_bayes_estimators` (§ “The Bernoulli Distribution”): https://www.randomservices.org/random/point/Bayes.html
- `dodge2008` (p. 31, urn example): Private upload; printed pages 31, 199 and 200 checked against index.tsv; reference text outside repository.
- `durrett2019` (§4.1, Ex. 4.1.1, p. 216): https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf
- `siegrist2022_bayes_estimators` (§ “The Bernoulli Distribution”, beta posterior and moments): https://www.randomservices.org/random/point/Bayes.html

## Calculations

`checks/sequential-coherence.py` passed its independent numerical calculations and generated-article inspection. Final build5 passed (718 articles, 626 questions, 579 answers); all 15 AA checks, 45 exact custom-heading assertions, generated citation/hidden-answer/wording audits, offline verification of 665 bibliography entries and whitespace checks passed.

The full 72-test suite ran in 211.891 seconds with 71 passing, including all 517 completed-page numerical scripts. Its one failure was a root-owned Wold heading alias. Root corrected that and the analogous total-probability alias; the focused citation/structure method then passed in 1.136 seconds. The orchestrator will rerun the full suite after integrating the branches.

## Shared proposals

Exact source-input substitutions, bibliography additions where needed, and proof debts are staged in ignored `research/pending/sequential-coherence.json`. Root integrates shared inputs; only this page’s prose, log and check are committed by this batch.

Dodge supplies only the urn illustration. The continuous normalisation and dependent-batch arguments use the actually read integral Bayes formula in Durrett §4.1, Ex. 4.1.1, p. 216, alongside the beta posterior calculation in Siegrist.
