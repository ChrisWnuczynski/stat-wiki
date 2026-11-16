# Hastings correction

Rank 358. Type: concept. Tier: lighter.

## Checked
- Gelman and others, *Bayesian Data Analysis*, 3rd ed., author-hosted electronic edition, §11.2, pp. 278–280. Equation (11.1) is the symmetric Metropolis ratio. Equation (11.2) is the Hastings ratio of ratios. The text states that a symmetric jump reduces (11.2) to (11.1), and that the target remains stationary by the same detailed-balance comparison.
- The numerical ratios 0.625, 2.5 and 10 were recomputed from those two target values and the stated proposal densities.
- §11.4 identifies a Gibbs update as a Metropolis–Hastings jump with acceptance probability 1.

## Assumed
- The target values p(1) and p(3) are the only two points needed for the ratio; they are not a normalised distribution on a larger space.

## Disputed
- None. The full irreducibility argument for a unique stationary distribution is Gelman's, and it is logged rather than copied.

## Sources read
- Andrew Gelman, John B. Carlin, Hal S. Stern, David B. Dunson, Aki Vehtari and Donald B. Rubin, *Bayesian Data Analysis*, 3rd ed., §11.2 and §11.4, https://sites.stat.columbia.edu/gelman/book/BDA3.pdf
