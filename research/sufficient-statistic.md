# Sufficient statistic

Type: Concept/definition. Rank 62.

## Material checked

- **Checked:** Frozen baseline 1,019 body words, no figures. The inherited definition, normal-mean factorization, Fisher–Neyman, Basu and Pitman–Koopman–Darmois properties, three examples, infobox and six question links are preserved. The definition's unread Lehmann–Casella and Casella–Berger citations were replaced with Fisher and opened Geyer §8.1. The factorization and Basu statements now cite opened Geyer and Berkeley treatments.
- **Checked:** Fisher's 1922 original, pp. 309–316, was read and logged in `research/statistic.md` for the history and data-reduction claim. Geyer's University of Minnesota exponential-family notes §§8.1–8.3 and 9.1 were opened for the conditional definition, factorization, natural statistic and model-relative warning. Berkeley's §3 states and proves Basu's theorem. Geyer's §9.4 supports the qualified Pitman–Koopman–Darmois statement.
- **Checked by code:** the five-toss example has ten orderings with three successes, conditional sequence probability 1/10, Beta(5,4) posterior and mean 5/9. Practice has six orderings, probability 1/6, Beta(4,4) posterior and mean 1/2. The Poisson bank question's 405/1024 and plug-in value are recalculated in `checks/sufficient-statistic.py`.
- **Assumed:** The Bernoulli example uses independent tosses with one constant $0<p<1$. The normal-mean sufficiency claim assumes known variance. Basu's proof uses sufficiency, completeness and ancillarity under the same model family.
- **Disputed:** Sufficiency is not usefulness for every scientific purpose; raw order and residuals remain useful for model checks. It does not imply minimality or completeness. A full dominated-space converse of factorization and the formal Pitman–Koopman–Darmois converse exceed the one collapsed proof and are logged in `research/proofs-todo-overrides.json` for the generated proofs todo.

## Sources opened and used

1. R. A. Fisher, [*On the Mathematical Foundations of Theoretical Statistics*](https://doi.org/10.1098/rsta.1922.0009), *Philosophical Transactions A* **222** (1922), pp. 309–316; previously read and logged in `research/statistic.md`, key `fisher1922`.
2. Charles J. Geyer, [*Exponential Families*](https://www.stat.umn.edu/geyer/f22/5421/notes/expfam.html), §§8.1–8.3, 9.1 and 9.4 (2022), key `geyer2022_exp_family`.
3. University of California, Berkeley, [*Completeness, Ancillarity, and Basu's Theorem*](https://stat210a.berkeley.edu/fall-2024/reader/completeness.html), §§1 and 3 (2024), new key `berkeley_basu2024`.
4. The [University of Washington historical list](https://sites.stat.washington.edu/peter/582/basu.html) was opened to check the 1955 Basu title and pages; the technical theorem is cited to Berkeley's proof.

Dodge index directory was absent from `~/statwiki-sources/dodge2008`.

## Changes and checks

The page adds a narrative explanation, one proof box covering discrete factorization and Basu's theorem, numeric Bernoulli worked and practice examples with hidden answer, and two answered bank questions. Source-chapter corrections also affect Fisher–Neyman and Basu pages, whose generated results are checked after the build. Full Quarto HTML rendering is unavailable because Quarto is not installed; the generator uses the system Pandoc shim.

- **Checked:** DasGupta (2007), pp. 945–946, restates Basu’s 1955 theorem and the role of completeness; its Purdue-hosted publisher PDF is the cited accessible source. The Berkeley reader was also consulted for the conditional-probability proof pattern.
