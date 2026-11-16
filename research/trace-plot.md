# Trace plot

Type: Concept. Rank 268. Tier: full.

## Material checked

- **Checked:** Baseline 452 words, 0 figures. Gelman and Rubin, *Statistical Science* 7 (1992), printed pp. 457–461: several sequences, the difficulty of judging one sequence, equation (3) for σ̂² = ((n-1)/n)W + B/n, and the statement that B cannot be calculated from one sequence. The scale-reduction factor is described as declining toward 1 when sequences mix and not when they remain in separate modes. The author PDF is image-only; these pages were read from rendered page images.
- **Checked by code:** Sequences 0,1,0,1 and 5,6,5,6 give W=1/3, B/n=12.5, σ̂²=12.75, √(σ̂²/W)≈6.185. Agreeing sequences 1,2,1,2 give B=0 and σ̂²=0.25. `checks/trace-plot.py`.
- **Assumed:** The algebraic identity σ̂² − W = (B−W)/n follows from equation (3) alone. The degrees-of-freedom multiplier in the published √R̂ is not recomputed, because the printed formula on p. 461 is a compound expression and the worked example uses equation (3) directly.
- **Disputed:** None. The paper does not use the phrase “trace plot” on the pages read. The article uses that phrase for the iteration plot whose separation equation (3) measures.

## Sources opened

1. Andrew Gelman and Donald B. Rubin, “Inference from iterative simulation using multiple sequences”, *Statistical Science* 7 (1992), pp. 457–461. Key `gelman_rubin1992`. Author-hosted PDF, read as page images.
