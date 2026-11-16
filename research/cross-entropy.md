# Cross-entropy — rank 162

Type: concept. Baseline 381 words, no figures. Preserve the tree impurity formula with Gini/misclassification comparison, the network output excerpt, its links, infobox and five question backlinks.

## Sources opened

- Goodfellow, Bengio and Courville (2016), *Deep Learning*, complete authorized online MIT Press book, Ch. 3 §3.13 pp. 71–73 and Ch. 5 §5.5 p. 130. Read Shannon entropy, KL divergence, cross-entropy `H(P,Q)`, the `0 log 0` convention, and empirical cross-entropy/negative log-likelihood relation.
- Raphael John Lamarre Townshend, Stanford CS229, *Decision Trees* (Fall 2018), complete university-hosted PDF, §3 pp. 4–6. Read tree-node entropy impurity, change-of-base bits, and split reduction. It calls `H(p,p)` “cross-entropy” in this tree-specific setting; the article explains the naming distinction.
- Original Shannon publisher DOI/PDF page was opened, but it exposed only bibliographic metadata rather than the full argument. The original is not cited in new prose; history uses the complete Goodfellow book. Dodge index has no Cross-entropy/Entropy entry.

## Fact ledger

- **Checked:** `H(P,Q)=−Σ p_k log q_k=H(P)+D_KL(P||Q)` for discrete distributions; `H(P,Q)≥H(P)` with equality at `Q=P` (Goodfellow Ch. 3 §3.13). Complete proof from log inequality supplied.
- **Checked:** A one-hot observed class has log loss `−log q_y`; the empirical mean is negative conditional log-likelihood per observation (Goodfellow Ch. 5 §5.5). Softmax gradient `s_j−y_j` derived in the single proof box.
- **Checked:** A tree node's impurity `−Σ p log p` is entropy `H(p)=H(p,p)`, while genuine cross-entropy compares separate distributions (Stanford CS229 §3; Goodfellow Ch. 3). Naming qualified.
- **Checked:** All numerical examples for `p=(.8,.2)`, `q=(.6,.4)` and Your-turn `p=(.5,.5)`, `q=(.9,.1)` computed with Python and checked in focused script.
- **Assumed:** Finite categorical support and natural logarithms for printed numbers. A zero `q_k` where `p_k>0` makes the loss infinite.
- **Disputed:** The inherited Shannon 1948 citation attached to the negative softmax log-likelihood claim does not specifically support that later machine-learning formulation; it should be replaced in shared source with opened Goodfellow Ch. 5. Its use for node entropy can likewise be replaced with opened book/Stanford notes unless the original paper is read in full.
