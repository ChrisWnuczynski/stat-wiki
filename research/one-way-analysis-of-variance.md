# One-way analysis of variance — rank 137 research

## Sources read

- **Checked:** NIST/SEMATECH e-Handbook, “One-Way ANOVA,” §3.2.3.1, full official page `https://www.itl.nist.gov/div898/handbook/ppc/section2/ppc231.htm`. It presents the one-factor model, ANOVA table, equal-variance normal assumptions, test logic and a five-machine example.
- **Checked:** R Foundation documentation for `stats::oneway.test`, `https://stat.ethz.ch/R-manual/R-devel/library/stats/html/oneway.test.html`, Description and Arguments. It states that `var.equal = TRUE` uses the standard F test and the default unequal-variance option uses a Welch approximation.
- **Checked:** Fisher's original 1925 *Statistical Methods for Research Workers*, Chapter VII, §38, printed pp. 177–178, and Chapter VIII, publicly transcribed by York University's Classics in the History of Psychology `https://psychclassics.yorku.ca/Fisher/Methods/chap7.htm`. Chapter VII explicitly introduces separating variance attributable to different groups of causes; Chapter VIII applies the approach to experiments. The inherited `fisher1925_smrw` bibliography entry is retained.
- **Checked:** Dodge, *The Concise Encyclopedia of Statistics*, authorized local PDF extraction, printed pp. 399–400, “One-Way Analysis of Variance.” It gives the model, decomposition, degrees of freedom and F comparison as orientation. **Disputed:** Its statement that failure to reject permits considering samples from the same population is too strong; the page correctly distinguishes absence of evidence from proven equality. Its treatment-causation wording also needs randomized assignment, which the page states.
- **Assumed:** NIST's web page does not display a publication date; the pending bibliography uses 2002, consistent with the existing NIST e-Handbook bibliography convention.

## Baseline and numbers

- **Checked:** The baseline page is already substantial, with corn and cold-sore tables, a heart-rate example, contrast and multiple-comparison discussions, and six figures. The rewrite preserves generator content and adds a focused worked example, conceptual transitions, conditions and a collapsed proof.
- **Checked:** New worked scores $A=(7,8,9)$, $B=(8,9,10)$, $C=(11,12,13)$ give group means 8, 9, 12, grand mean $29/3$, $\mathrm{SS}_{\mathrm{treatment}}=26$, $\mathrm{SS}_{\mathrm{error}}=6$, total 32, degrees of freedom 2 and 6, mean squares 13 and 1, $F=13$, and $P(F_{2,6}\ge13)=27/4096\approx0.006592$.
- **Checked:** Your-turn groups $(4,5,6)$ and $(6,7,8)$ give treatment SS 6, error SS 4, F 6 and pooled $t=-\sqrt6\approx-2.449490$.
- **Checked:** The inherited corn data and cold-sore data are verified in `checks/one-way-analysis-of-variance.py`; the existing question pages `ex-inf-anova-two-groups`, `ex-da-sickle-anova`, and `ex-da-bonferroni` all have worked answers relevant to the test and follow-up.
- **Disputed:** The existing alt text for `inf-corn-groups.png` says “four varieties,” whereas the actual image and table visibly have five. The page-local pending record asks integration to fix the shared `figure_alts.py` text; the figure and data remain intact.

## Proof scope

The new collapsed proof covers the sums-of-squares identity, orthogonal-normal chi-squared F law, and two-group $F=t^2$ relation. Full simultaneous Tukey coverage and a complete planned-contrast F derivation are logged for follow-up.
