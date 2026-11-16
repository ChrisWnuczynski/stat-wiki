# Sigmoid function

Type: Concept. Rank 54.

## Material checked

- Frozen baseline: 489 body words, zero figures. Read the inherited definition, threshold and logistic formulas, derivative at zero and two, one-layer interpretation, infobox, nine question links and both relevant question answers. Keep all of them.
- **Checked:** Bishop (2006), Ch. 4 §4.3.2 Eqs. 4.57–4.61, 4.88 gives logistic and inverse-logit, derivative and Bernoulli gradient; Ch. 5 §§5.1–5.2 describes network activations and losses. The author-hosted full PDF is linked from the Microsoft Research publication page.
- **Checked:** McCulloch and Pitts (1943) publisher abstract describes all-or-none neural events. Rumelhart, Hinton and Williams (1986), pp. 533–534, author-hosted original paper describes differentiable units and error backpropagation.
- **Checked by code:** sigmoid, derivatives, odds ratio, loss gradients and rounded values for the worked, practice and inherited saturation examples are recalculated in `checks/sigmoid-function.py`.
- **Assumed:** In the worked classification interpretation, targets are Bernoulli with log odds equal to the score. The mathematical sigmoid properties themselves need no distributional assumption.
- **Disputed:** a bounded sigmoid output alone does not guarantee probability calibration; the article explicitly conditions that interpretation on the fitted binary model. The 1943 threshold and 1986 backpropagation papers do not establish priority for invention of the logistic curve.

## Sources opened and used

1. Christopher M. Bishop, [*Pattern Recognition and Machine Learning*](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf) (2006), Ch. 4 §4.3.2 and Ch. 5 §§5.1–5.2. Microsoft Research hosts the full official PDF. Existing key `bishop2006` updated to this URL.
2. McCulloch and Pitts, [*A logical calculus of the ideas immanent in nervous activity*](https://link.springer.com/article/10.1007/BF02478259) (1943), publisher abstract. Existing key `mcculloch_pitts1943`.
3. Rumelhart, Hinton and Williams, [*Learning representations by back-propagating errors*](https://www.cs.toronto.edu/~hinton/absps/naturebp.pdf), *Nature* 323 (1986), pp. 533–536. Read the author-hosted original PDF, especially pp. 533–534. Existing key `rumelhart_hinton_williams1986`.

Dodge index directory was absent from `~/statwiki-sources/dodge2008`.

## Changes and checks

- Add context, motivation, worked and practice arithmetic, one collapsed proof, concrete failure cases and two answered bank questions while preserving inherited text and values.
- The source chapter receives only pinpoint citation locations. Because that text is shared, the build dependency report and chapter output must be checked.
- The generated body has 2,917 words and zero figures. Its inherited formulas, interpretation, infobox and nine question links remain, and the shared neural-units chapter shows the new pinpoint citations after build.
- Verification: `checks/sigmoid-function.py` passes the displayed calculations; the generator builds 718 articles and 557 questions; all 67 Python tests pass; offline verification covers 441 bibliography entries; and `git diff --check` passes. Full Quarto HTML rendering is unavailable because Quarto is not installed; the generator used the system Pandoc shim.
