# Regularisation and weight decay — research notes (rank 212)

## Sources read

- Checked: Krogh and Hertz (1992), *A Simple Weight Decay Can Improve Generalization*, full original paper from NeurIPS proceedings, https://proceedings.neurips.cc/paper/1991/file/8eefcfdf5990e441f0fb6f3fad709e21-Paper.pdf, opened 2026-11-16. §1, p. 951 gives penalized objective and gradient shrinkage; §§4–6, pp. 953–956 discuss noise, linear-network analysis, limitations and NetTalk experiment. Proceedings year/catalogue may be 1991 while printed volume is 1992; bibliography uses 1992.
- Checked: Loshchilov and Hutter (2019), *Decoupled Weight Decay Regularization*, full author paper at https://arxiv.org/pdf/1711.05101, opened 2026-11-16. §2 and Appendix A distinguish ordinary SGD equivalence from adaptive-preconditioner nonequivalence, including Propositions 1–2.
- Checked: Goodfellow, Bengio and Courville (2016), *Deep Learning*, full publisher-hosted Chapter 7 at https://www.deeplearningbook.org/contents/regularization, opened 2026-11-16. §7.1.1, pp. 226–230 gives squared-weight penalty, update and local quadratic/ridge interpretations. Use only if added to pending bibliography.
- Checked: sources/stat3006/chapters/sl-16-networks-in-practice.qmd and generated topic, including its numerical network example. Keep source facts and links.
- Checked by code: one-step gradient and decay factors, ridge normal equations and rescaling example.
- Assumed: differentiable loss for gradient example; positive penalty strength and a fixed learning rate for the simple equivalence.
- Disputed: an L2 penalty and an independently applied decay step are not generally the same under Adam; shrinkage alone does not guarantee better test error, and input rescaling changes penalty effect.
- Dodge: no direct weight-decay entry found in index.

## Preservation

Baseline has 376 words and zero figures. Preserve original network experiment and linked questions.
