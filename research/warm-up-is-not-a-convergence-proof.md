# Warm-up is not a convergence proof — research notes (rank 208)

## Sources read

- Checked: Geyer (1992), *Practical Markov Chain Monte Carlo*, full original article from Duke University course archive, https://www2.stat.duke.edu/homeweb/scs/Courses/Stat376/Papers/GeyerStatSci1992.pdf, opened 2026-11-16. Sections 3.3–3.7, pp. 477–480: serial dependence, precision and effective sample size, spacing, burn-in; §4, p. 480 argues multiple starts alone do not suffice.
- Checked: Gelman and Rubin (1992), *Inference from Iterative Simulation Using Multiple Sequences*, full original article from Duke University course archive, https://www2.stat.duke.edu/homeweb/scs/Courses/Stat376/Papers/ConvergeDiagnostics/GelmanRubinStatSci1992.pdf, opened 2026-11-16. §§1.2–1.4, pp. 458–459 and §2.4, p. 462: slow chains, dispersed starts, and limitations of between-chain diagnostic.
- Checked: sources/book/chapters/bayes-04-mcmc.qmd and generated article. Keep the proposal-scale figure, examples, and linked questions.
- Checked by code: two-state switch probabilities in the worked and practice examples, and the exact formula for departure from the stationary distribution.
- Assumed: the two-state example is an exactly specified irreducible symmetric Markov chain; real MCMC transition probabilities and mode masses generally are unknown.
- Disputed: a preset warm-up length, a smooth trace, a high acceptance rate, and agreement of similarly initialized chains do not certify stationarity or efficient exploration.
- Dodge: index has no direct warm-up entry.

## Preservation

Baseline has 821 words and one figure. Keep both source examples and all four question links.
