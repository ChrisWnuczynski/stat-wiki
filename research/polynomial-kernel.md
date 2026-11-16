# Polynomial kernel

Rank 367. Type: concept. Tier: lighter.

## Checked
- Hastie, Tibshirani and Friedman, §12.3.1, pp. 423–424, equations (12.21)–(12.24). The degree-d polynomial kernel is (1+⟨x,x'⟩)^d. Equation (12.23) expands the degree-2 map in two inputs and names the six coordinates, including the √2 scalings.
- K((1,2),(3,0))=16 matches the feature inner product. K((1,0),(0,1))=1 while the pure square of the inner product is 0. The dimensions binom(4,2)=6 and binom(5,2)=10 were checked.

## Assumed
- The kernel is used as an inner product in a real feature space, so the Gram matrix on any finite set is positive semi-definite. That property is used as stated by Hastie, Tibshirani and Friedman; it is not re-proved for a general polynomial.

## Disputed
- None in the degree-2 expansion.

## Sources read
- Trevor Hastie, Robert Tibshirani and Jerome Friedman, *The Elements of Statistical Learning*, 2nd ed., §12.3.1, pp. 423–424.
