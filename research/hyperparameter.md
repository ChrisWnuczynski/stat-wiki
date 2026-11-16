# Hyperparameter

Type: Concept/definition. Rank 49.

## Material checked

- Frozen baseline: 1,244 body words, no figures. Read the generated page, its two embedded rat-study examples, the marginal-hyperposterior property, and `sources/book/chapters/bayes-08-hierarchy.qmd`.
- **Checked:** Gelman et al., *Bayesian Data Analysis*, Ch. 2 §2.4, pp. 34–35, calls Beta prior parameters hyperparameters; Ch. 5 §§5.1–5.3, pp. 101–110, distinguishes fixed estimated values from full posterior uncertainty and derives the hierarchy. The authors' Columbia site explicitly permits non-commercial access to its electronic edition.
- **Checked:** The rat-study data (4/14 current, 70 historical groups), Beta update, and example of failure of exchangeability between laboratories are in Gelman et al., Ch. 5 §5.1, pp. 102–104. The book's historical note, §5.8, p. 132, gives the cited lineage of hierarchical Bayesian modelling.
- **Checked by exact arithmetic:** new two-group and practice Beta updates; inherited q-23's 6/20 and 42/110 means, its shrinkage weights, and the current-study update. See `checks/hyperparameter.py`.
- **Assumed:** the worked counts are conditionally independent within their groups and the Beta prior with specified hyperparameters is appropriate. A full hyperprior is required before treating hyperparameters as uncertain in the Bayesian model.
- **Disputed:** none. The Dodge directory is absent, so no unsupported claim about the word's origin is made.

## Sources opened and used

1. Andrew Gelman et al., [*Bayesian Data Analysis*, third edition](https://sites.stat.columbia.edu/gelman/book/BDA3.pdf), Ch. 2 §2.4, pp. 34–35, and Ch. 5 §§5.1–5.3, 5.8, pp. 101–110, 132. Read the author-hosted electronic edition through the web reader. Existing bibliography key: `gelman_bda2013`.
2. Read the [bookseller’s detailed contents listing](https://www.betterworldbooks.com/product/detail/applied-statistical-decision-theory-9780471383499/new) for Raiffa and Schlaifer's *Applied Statistical Decision Theory*. Its Chapter 7 explicitly lists “Beta-Binomial and Beta-Pascal Functions” on pp. 232–241. The source text retains its citation only for that narrow statement about the book's scope; Gelman et al. support the hierarchical product formula. Existing key: `raiffa_schlaifer1961`.
3. Read the repository's source chapter named above for notation and preservation of its rat-study example and q-23 answer. The Lindley–Smith publisher record was consulted for bibliographic context, but its full article was not available from the publisher and is not used for a mathematical or historical claim.

## Changes and checks

- Added a plain-language rationale, hierarchical notation, conditional and marginal distinction, a collapsed proof, statistical use, an independent numerical worked example and a hidden practice answer. Kept the rat-study example, q-23 and the hyperposterior property.
- Selected answered bank questions `q-02` and `c-02` for the generated self-check section; neither duplicates embedded q-23.
- Replaced unlocated source-definition and rat-study citations with the read, page-located Gelman treatment. A preservation test exposed the shared marginal-hyperposterior property's Raiffa–Schlaifer citation, so it remains for the book's listed beta-binomial treatment with a location. No new bibliography entry was needed.

## Verification

The generator completed 718 articles and 557 question pages with a temporary Pandoc shim. Quarto itself is unavailable here, so no full HTML render was run. The article has 3,942 body words versus 1,244 before and no figures in either version. The definition, rat example and marginal-hyperposterior excerpt now have located citations; all generated article citations before “See also” pass the location scan. The shared rat excerpt also appears in Exchangeability, Rat-tumour data and Hierarchical Bayesian model; all three remain above their frozen word and figure baselines. The page arithmetic check, 67 Python tests, offline verification of 437 bibliography entries and `git diff --check` pass.
