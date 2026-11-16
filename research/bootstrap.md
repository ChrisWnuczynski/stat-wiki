# Bootstrap — rank 104

Type: method/concept in generator. Frozen baseline 725 body words, zero figures. Source definition, inclusion-probability derivation, $.632$ error discussion, infobox and citations remain generated.

## Sources read

- **Checked:** Cosma R. Shalizi, *The Truth about Linear Regression* (author-hosted complete manuscript, 20 October 2025), https://www.stat.cmu.edu/~cshalizi/TALR/TALR.pdf, Ch. 24 §§24.2–24.7 printed pp. 390–401 and Ch. 25 §25.1 pp. 402–403. Read the simulation principle, nonparametric and model-based algorithms, case and residual resampling, Monte Carlo versus approximation error and pivoted intervals.
- **Checked:** Dodge, *The Concise Encyclopedia of Statistics* (2008), local authorized printed pp. 51–53, “Bootstrap,” for definition, algorithm and Efron's 1979 historical introduction. Its claim that 50–200 replicates suffice is dated and is not repeated.
- **Checked:** Project Euclid publisher page for Efron (1979), DOI 10.1214/aos/1176344552, confirms original title and journal metadata; full paper inaccessible there. Existing source citation retained, while new mathematical claims cite the full Shalizi text and Dodge instead.
- **Checked:** Simon and Aliferis, “Evaluation,” open-access Springer chapter (2024), §9.4, “The 0.632 and the 0.632+ bootstrap,” full publisher chapter at DOI 10.1007/978-3-031-39355-6_9. It explains the smaller effective training sets, pessimistic bootstrap error and the 0.368/0.632 weighted correction. This replaces unlocated inherited citations in the shared error-rates source chapter.
- **Checked by code:** `checks/bootstrap.py` enumerates all 27 and four resamples, verifies moments, inclusion probabilities and all printed inherited numerical values.
- **Assumed:** The case bootstrap example treats the observed cases as independent identically distributed units. Conditional calculations are exact for the empirical distribution, not unconditional guarantees about a population.
- **Disputed:** No 50–200 replicate sufficiency rule is universal. The $.632$ estimate in the source is a correction, not an identity.

## Proof and bank

One collapsed proof derives the exact bootstrap variance of the sample mean and expected distinct-case count. Answered bank questions: `ex-ur-bootstrap-unit`, `ex-sl-09-3`, `ex-sl-12-6`, each addressing a different practical inference issue.
