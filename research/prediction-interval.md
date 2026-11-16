# Prediction interval

Rank 354. Type: concept/definition. Tier: lighter.

## Checked
- Hyndman and Athanasopoulos §5.5 define a prediction interval as a range for a future observation, with the normal form ŷ ± c σ̂_h, and give the Google price illustration 758.88 ± 1.96×11.19. That product is 21.9324, and the endpoints round to 736.9 and 780.8. Their printed 80% lower end 744.5 does not match 758.88−1.28×11.19=744.56, so that 80% pair is not repeated here.
- NIST/SEMATECH §4.5.1.2 writes σ̂_p = √(σ̂²+σ̂_f²) and the interval ŷ ± t σ̂_p.
- The straight-line variance identity and the numbers 1.62439, 3.67462, 1.410 and 3.54412 were recomputed from SciPy's t_9 quantile.

## Assumed
- The worked regression uses fixed predictors, independent normal errors, and the usual residual mean square on n−2 degrees of freedom.

## Disputed
- Hyndman and Athanasopoulos print an 80% lower endpoint 744.5. The multiplier and residual standard deviation they state give 744.56. The 95% endpoints they print do match.

## Sources read
- Rob J. Hyndman and George Athanasopoulos, *Forecasting: Principles and Practice*, 3rd ed., §5.5, https://otexts.com/fpp3/toolbox.html
- NIST/SEMATECH e-Handbook, §4.5.1.2, https://www.itl.nist.gov/div898/handbook/pmd/section5/pmd512.htm
