# Bayesian credible interval

Type: Definition/concept. Rank 52.

## Material checked

- Frozen baseline: 956 body words and one figure. Read the generated definition, the posterior-draw property, both preserved interval-comparison worked questions, the source figure and the twelve question links. The existing figure compares two 95% intervals for a $\operatorname{Beta}(3,9)$ posterior.
- **Checked:** Gelman et al., *Bayesian Data Analysis*, 3rd ed., Ch. 2 §2.3 pp. 32–34 defines central posterior intervals, highest-density regions, their difference for skewed or multimodal posteriors, and direct or simulation-based calculation. Ch. 4 §4.4 pp. 90–92 discusses large-sample repeated-sampling correspondence without equating the posterior and coverage probability statements. The author-hosted electronic edition explicitly permits noncommercial use; no unauthorized copy was used.
- **Checked by code:** $\operatorname{Beta}(3,9)$ equal-tailed 95% endpoints 0.0602177 and 0.5177559, width 0.4575381; HPD endpoints 0.0405552 and 0.4837237, width 0.4431685 and equal endpoint density. These use SciPy's Beta CDF, quantile and root finding. The practice $\operatorname{Beta}(4,8)$ interval endpoints and tail probability are checked in `checks/bayesian-credible-interval.py`.
- **Checked history:** BDA3 Ch. 2 §2.10 p. 56 traces inverse probability to Bayes's 1763 essay and identifies Box and Tiao's 1973 discussion of highest-density regions. The history statement is limited to what that bibliographic note supports.
- **Assumed:** the worked binomial trials are independent conditional on a fixed success probability, with a proper uniform Beta prior.
- **Disputed:** a 95% posterior interval does not automatically have 95% repeated-sampling coverage at each fixed parameter. The source chapter's comparison is kept with located BDA citations; the new page states the different conditioning explicitly.

## Sources opened and used

1. Gelman, Carlin, Stern, Dunson, Vehtari and Rubin, [*Bayesian Data Analysis*, 3rd ed.](https://sites.stat.columbia.edu/gelman/book/BDA3.pdf), Ch. 2 §§2.3, 2.10 (pp. 32–34, 56) and Ch. 4 §4.4 (pp. 90–92). Opened the author-hosted PDF and read the indicated sections. Existing key `gelman_bda2013`.
2. The source chapter `sources/book/chapters/bayes-01-foundations.qmd` and its existing figure were checked for continuity. Existing posterior-draw property cites Geyer (1992) and Wang (2025), both documented as opened in the earlier Posterior mean research note; their citations are preserved.

## Changes and checks

- Retained the original definition, figure, posterior-draw property, both long worked question answers, infobox values and all twelve question links. Replaced only the definition's unlocated Box–Tiao and Jeffreys citations with located BDA passages actually read. Added a numerical Beta worked example, a hidden practice answer, a collapsed proof of interval content and the HPD endpoint condition, and two relevant answered bank questions (q-08 and ex-applied-iq). The asymptotic coverage correspondence is logged in `proofs-todo.json`.
- The generated article grows from 956 to 2,857 body words and retains its one figure. The dependent Credible-region constructions, Posterior point summaries and Posterior summaries from draws articles remain above their frozen word and figure baselines. One collapsed proof covers posterior content, monotone transformations, the interior HPD endpoint condition, Beta updating and the improper-posterior counterexample. The asymptotic coverage claim has a durable property-level entry in `research/proofs-todo-overrides.json`, which regenerates `proofs-todo.json`.
- Verification: `checks/bayesian-credible-interval.py` recalculates all new Beta interval endpoints, posterior contents, the inherited draw indices and IQ question values; the generator builds 718 articles and 557 questions; all 67 Python tests pass; offline verification covers 441 bibliography entries; and `git diff --check` passes. Full Quarto HTML rendering is unavailable because Quarto is not installed; the generator used the system Pandoc shim.
