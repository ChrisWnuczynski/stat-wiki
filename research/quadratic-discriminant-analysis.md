# Quadratic discriminant analysis

Rank 355. Type: concept. Tier: lighter.

## Checked
- Hastie, Tibshirani and Friedman, 12th printing (2017), §4.3, equations (4.8)–(4.12), pp. 108–110. Equation (4.12) is the quadratic score. The shared-covariance cancellation is equation (4.9) on pp. 108–109.
- The one-dimensional tie points 1.418 and −3.418, and the scores at 0, −4 and 3, were solved from the score equation and checked in checks/quadratic-discriminant-analysis.py.
- Parameter counts 4 and 5 for G=2, p=1 match Gp+p(p+1)/2+(G−1) and the version with a separate covariance per class.

## Assumed
- Equal misclassification costs and class-conditional normality, as in the derivation of (4.12).

## Disputed
- None in the algebra. Smith (1946/1947) is cited on the source page; that paper was not opened, so the new prose cites Hastie, Tibshirani and Friedman.

## Sources read
- Trevor Hastie, Robert Tibshirani and Jerome Friedman, *The Elements of Statistical Learning*, 2nd ed., 12th printing, author-hosted PDF, §4.3, pp. 108–112.
