# Pooling across groups — research notes (rank 205)

## Sources read

- Checked: Gelman et al. (2013), *Bayesian Data Analysis*, author-hosted complete third-edition PDF, https://sites.stat.columbia.edu/gelman/book/BDA3.pdf, opened 2026-11-16. Chapter 5 §5.4, pp. 113–117, explicitly compares unpooled, pooled and weighted estimates and derives the normal hierarchical conditional posterior, equation 5.17. The PDF permits non-commercial reading.
- Checked: Lindley and Smith (1972), full original journal article hosted on Imperial College faculty site, https://www.ma.imperial.ac.uk/~das01/MyWeb/SCBI/Papers/LindleySmith.pdf, opened 2026-11-16. Pages 1–3 motivate exchangeable normal means and give shrinkage estimate equation 1.
- Checked: Efron and Morris (1975), full original article hosted by McGill biostatistics, https://www.medicine.mcgill.ca/epidemiology/hanley/bios602/MultilevelData/EfronMorrisJASA1975.pdf, opened 2026-11-16. Pages 311–312 introduce multivariate normal shrinkage and examples. It concerns Stein/empirical Bayes estimates, not the exact conditional model used in the page's example.
- Checked: original hierarchy chapter, complete/no/partial pooling table and normal-hierarchical shrinkage derivation, for preservation of its existing explanation and question links.
- Checked: numeric examples and limiting weights with Python; parameters explicitly held fixed for the conditional posterior calculation.
- Assumed: the tutorial classes are reasonably exchangeable after relevant predictors; Gaussian sampling and known within-group variance for the exact worked formula.
- Disputed: partial pooling does not guarantee improved estimates for an isolated, systematically different group; and it does not automatically model causal class effects.
- Dodge: present; index has no pooling or hierarchy entry.

## Preservation

Baseline has 203 words, no figures, and four linked questions. The original comparison table and question links remain.
