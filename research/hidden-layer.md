# Hidden layer

Type: Concept. Rank 57.

## Material checked

- Frozen baseline: 870 body words, zero figures. Read the network notation, both XOR threshold constructions and their tables, the 24-hidden-neuron tsetse assertion, infobox and eight question links. Retain the worked XOR arithmetic and connections.
- **Checked:** Bishop, *Pattern Recognition and Machine Learning*, Ch. 5 §§5.1–5.3, officially hosted by Microsoft Research and read for the sigmoid pass, describes feed-forward hidden representations, nonlinear activations, training and symmetry. Rumelhart, Hinton and Williams (1986), pp. 533–535, read from Hinton's author-hosted original, explains internal units and backpropagating error derivatives.
- **Checked by code:** both inherited XOR constructions, the affine-collapse parameter count, the smooth two-hidden-unit worked/practice values, and the answered initial-weights bank question are recomputed in `checks/hidden-layer.py`.
- **Checked correction:** The initial-weights bank question used a fixed input squared norm of $25$ but the answer used fan-in $26$ to calculate variance $6.5$. With 25 standardised inputs and a bias, the answer is coherent when the *augmented* input has squared norm $26$. Corrected the question and answer source chapters accordingly; the printed standard deviation and tail probability remain valid.
- **Assumed:** The smooth worked example treats sigmoid output as a deterministic score, without a fitted Bernoulli model or probability calibration claim.
- **Disputed/unverified:** The inherited Williams et al. (1994) tsetse example cites an Open Library author page, not the original chapter; web searches found bibliographic mentions but not primary text verifying exactly 24 hidden neurons. The example is preserved as inherited and flagged here, rather than making new claims from it. No new citation to Ripley is added because only the author-hosted book description and preface, not Ch. 5, were available to read.

## Sources opened and used

1. Christopher M. Bishop, [*Pattern Recognition and Machine Learning*](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf) (2006), Ch. 5 §§5.1–5.3. The full PDF is linked by its official Microsoft Research publication page. Existing key `bishop2006`.
2. Rumelhart, Hinton and Williams, [*Learning representations by back-propagating errors*](https://www.cs.toronto.edu/~hinton/absps/naturebp.pdf), *Nature* 323 (1986), pp. 533–536. Read the author-hosted original, especially pp. 533–535. Existing key `rumelhart_hinton_williams1986`.
3. B. D. Ripley, [author's *Pattern Recognition and Neural Networks* page](https://www.stats.ox.ac.uk/~ripley/PRbook/) and preface. Checked that Ch. 5 covers feed-forward neural networks, but did not cite technical content not available in the excerpt.

Dodge index directory was absent from `~/statwiki-sources/dodge2008`.

## Changes and checks

- Add motivation, architecture and interpretation, proof of affine collapse and XOR separation, smooth worked and practice example, distinct failures and two answered bank questions. Preserve both inherited XOR tables and the infobox.
- The generated body has 3,380 words and zero figures. The inherited two XOR tables, tsetse paragraph and eight question links remain. The corrected augmented-input wording appears in the generated bank question and in this article's embedded answer; the related source chapter remains intact.
- Rank-57 checkpoint comparison: rank 48 has 2,330 words, 13 top-level sections, a worked example, hidden Your turn answer and 25 inline citations. Rank 57 has 3,380 words, 12 top-level sections, a worked example, hidden Your turn answer and 37 inline citations. Rank 48's distribution-specific Examples section is represented here by a worked-example subsection. The concept page has no missing relevant section.
- Verification: `checks/hidden-layer.py` passes both XOR circuits, the smooth and rectified examples, corrected initial-weights arithmetic and page structure; the generator builds 718 articles and 557 questions; all 67 Python tests pass; offline verification covers 442 bibliography entries; and `git diff --check` passes. Full Quarto HTML rendering is unavailable because Quarto is not installed; the generator used the system Pandoc shim.
