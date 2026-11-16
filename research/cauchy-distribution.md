# Cauchy distribution

Type: Distribution. Rank 271. Tier: lighter.

## Material checked

- **Checked:** Baseline 832 words, 2 figures. Dodge printed p. 60: density, symmetry about the location, quartiles at α±θ, mean and variance undefined, and agreement with Student’s t on one degree of freedom when α=0 and θ=1. The catalogue already proves that the absolute mean is infinite; that proof box is left in place.
- **Checked by code:** P(|X|>5)=1−2 arctan(5)/π ≈ 0.1257 for the standard law. Quartiles at location 2 and scale 3 are −1 and 5. `checks/cauchy-distribution.py`.
- **Assumed:** Failure of the strong law is the usual consequence of an undefined mean. A separate proof of that implication is logged rather than added beside the catalogue proof.
- **Not opened:** Casella and Berger, Forbes et al. The catalogue already cites them.

## Sources opened

1. Dodge, printed p. 60. Key `dodge2008`.
