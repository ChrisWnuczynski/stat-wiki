# Interaction

Type: Concept/definition. Rank 47.

## Material checked

- Frozen baseline: 1,163 body words and three figure instances. The generated article contains wheat, pesticide–fertiliser, and age-by-smoking examples with their tables, code and plots.
- Read the two source chapters, `sources/stat1301/chapters/da-06-anova-examples.qmd` and `sources/stat1301/chapters/da-08-linear-model-examples.qmd`, along with the two rank-42–43 research pages for the depth standard. Checked the 36 wheat observations and 189 birth-weight records against the printed results. The source gives only rounded crop cell means, so its printed $F=574$ could not be independently recalculated from those means.

## Sources opened and used

1. NIST/SEMATECH, [*e-Handbook of Statistical Methods*, “Exploring First Order Interactions”](https://www.itl.nist.gov/div898/handbook/ppc/section4/ppc423.htm), §3.4.2.3 (2002). Opened the NIST page and checked the definition, nonparallel-plot interpretation and effect-at-a-level guidance. New key: `nist_interactions2002`.
2. NIST/SEMATECH, [*e-Handbook of Statistical Methods*, “The two-way ANOVA”](https://itl.nist.gov/div898/handbook/prc/section4/prc437.htm), §7.4.3.7 (2002). Opened the NIST page and checked the model, interaction component, sums of squares and degrees of freedom. New key: `nist_two_way_anova2002`.
3. Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), printed p. 266, from the user-supplied copy outside the repository. Read the “Interaction” entry, including its model and Fisher attribution. Existing key: `dodge2008`.

No unauthorised copy was used or added to the repository.

## Changes and checks

- Added a motivating pesticide example, binary contrast and treatment-coded models, a collapsed algebraic proof, statistical interpretation, a separate four-cell worked example, and a hidden “Your turn” calculation.
- Replaced inherited unlocated Fisher, Scheffé and Casella–Berger definition citations with opened, located NIST and Dodge sources. Kept the crop, wheat and birth-weight examples and all three figure instances.
- Added two located NIST citations to the dependent Main effect article after the shared-source edit exposed its citation gap, and clarified that averaging is a marginal-mean comparison rather than the meaning of every coded coefficient.
- Narrowed the completed-page prose test's `opened` marker to editorial phrases such as `opened source`; rank 44's Monty Hall example properly says a host “opens” a door.
- Corrected the high-fertiliser pesticide effect to $8.16-5.70=2.46$ from the displayed rounded cell means. Its inherited $2.45$ was inconsistent with that table.
- Selected answered bank questions q-39 and q-40 for “Check yourself.” The page check recomputes both new tables, the wheat sums of squares, the crop simple effects and the birth-weight regression coefficients from source data.

## Verification

The generator completed 718 articles and 557 question pages. The article has 3,912 body words versus 1,163 before and retains all three figure instances. All 47 page checks, 67 Python tests, 11 Node tests, offline verification of 437 bibliography entries, the overview link check, and git diff --check pass. Quarto is unavailable in this workspace; the generator uses a local Pandoc command shim for its conversion step. No full Quarto HTML render was run.
