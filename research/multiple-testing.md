# Multiple testing

Rank 366. Type: concept. Tier: lighter.

## Checked
- Hastie, Tibshirani and Friedman, §18.7, pp. 686–688: family-wise error of m independent level-α tests is 1−(1−α)^m; Bonferroni rejects at α/m and has family-wise error at most α by the union bound; Algorithm 18.2 is the Benjamini–Hochberg step-up rule. Their displayed inequality is strict. The 1995 paper uses a non-strict inequality. The worked example uses ≤, as in Benjamini and Hochberg, and the chosen p-values are not on the boundary, so the strict and non-strict rules agree.
- Benjamini and Hochberg (1995), pp. 291–293: FDR is the expected proportion of false rejections among rejections; it is at most the family-wise error rate, with equality when all nulls are true. Section 3.1 and Theorem 1 state the ordered procedure and control under independence of the true-null statistics.
- 1−0.95^20=0.6415, 1−0.95^5=0.22622, and the four-test rejection count k=3 were recomputed.

## Assumed
- The five-test family-wise calculation treats the true nulls as independent.

## Disputed
- Hastie, Tibshirani and Friedman write a strict inequality in Algorithm 18.2. Benjamini and Hochberg state the largest i such that the ordered p-value does not exceed i q*/m. The worked p-values satisfy both versions.

## Sources read
- Yoav Benjamini and Yosef Hochberg, *Journal of the Royal Statistical Society B* 57 (1995), pp. 289–300, sections 2 and 3. Read from the author-university PDF.
- Trevor Hastie, Robert Tibshirani and Jerome Friedman, *The Elements of Statistical Learning*, 2nd ed., §18.7, pp. 686–688.
