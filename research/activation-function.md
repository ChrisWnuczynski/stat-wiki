# Activation function research notes

Type: concept. Baseline: 264 words, zero figures. Preserve the original step and sigmoid definitions, links to artificial neurons and XOR, infobox values, and all inherited citations. The new page contrasts representational power, derivative flow and probability interpretation rather than treating activation names as a list.

## Sources opened

- Goodfellow, Bengio and Courville (2016), *Deep Learning*, full author-hosted Ch. 6 at https://www.deeplearningbook.org/contents/mlp.html. Read §6.1, §6.2, §6.3.1–6.3.2 and §6.5 (pp. 166–191 and backpropagation section). Checked affine-plus-activation construction, why identity hidden layers collapse, sigmoid saturation, ReLU corner and inactive gradient, and output versus hidden roles. Its pending bibliography key `goodfellow_deep_learning2016_ch6` was introduced with rank 148.
- Glorot, Bordes and Bengio (2011), “Deep Sparse Rectifier Neural Networks,” *Proceedings of Machine Learning Research* 15:315–323, full official proceedings PDF at https://proceedings.mlr.press/v15/glorot11a/glorot11a.pdf. Read §1, §3.1 and §4: rectifier shape, active-set piecewise linearity, sparsity, training experiments and limits. New key `glorot_bordes_bengio2011` requested in pending.
- McCulloch and Pitts (1943), original publisher DOI page at https://doi.org/10.1007/BF02478259 and paper metadata, inspected for orientation. Full article was not accessed for this pass; its existing citation is preserved from the baseline. The new history sentence cites Mehlig's full account.
- Mehlig (2022), *Machine Learning with Neural Networks*, Cambridge University Press authorized full Introduction excerpt, https://assets.cambridge.org/97811084/94939/excerpt/9781108494939_excerpt.pdf. Read §1.2, pp. 7–8: McCulloch–Pitts binary threshold units and the distinction between their original model and later general weighted formulations.
- Rumelhart, Hinton and Williams (1986), full four-page *Nature* paper read for rank 148 via Hinton's University of Toronto author-hosted PDF; pp. 533–536 support the hidden-representation/backpropagation account. Existing citation retained.
- Dodge index at `/workspace/statwiki-sources/dodge2008/index.tsv` consulted; it has no direct activation-function or neural-unit entry, so no Dodge claim is added.

## Fact ledger

- **Checked:** Logistic derivative $g(1-g)$, maximum $1/4$, and ReLU's zero/one one-sided derivatives. Algebra in proof and numerical checks in `checks/activation-function.py`.
- **Checked:** $g(2)=0.8807971$, $g'(2)=0.1049936$, $g(1)=0.7310586$, $g(-1)=0.2689414$, $g'(-1)=0.1966119$, $g(-2)=0.1192029$, $g'(-2)=0.1049936$, $g'(20)=2.0611536\times10^{-9}$.
- **Checked:** Identity activations leave an affine composition; a ReLU network is piecewise affine with input-dependent active sets. Full textbook §6.1 and §6.3; Glorot et al. §3.1.
- **Assumed:** The switch classification example has exact binary inputs and labels; the numerical unit weights are hypothetical and do not imply a fitted model.
- **Disputed:** “Best” activation is task- and optimisation-dependent; the original rectifier experiments do not establish universal superiority.

## Bank selection

Answered `ex-sl-14-6` asks why identity hidden activations collapse a network into an affine score. Answered `ex-sl-15-7` derives the sigmoid-derivative chain in a backpropagation update. Both directly test distinct roles of an activation function and differ from the embedded numeric example.
