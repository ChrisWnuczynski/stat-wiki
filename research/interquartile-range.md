# Interquartile range

Type: Definition. Rank 256. Tier: full.

## Material checked

- **Checked:** Dodge p. 266 defines the interquartile range as $Q_3-Q_1$. NIST §1.3.5.6, the measures-of-scale page, contrasts it with the variance and the range and recommends it for long tails. Quartiles use the position $1+(n-1)p$.
- **Checked by code:** sample 1…9, 100 gives quartiles 3.25 and 7.75, IQR 4.5, fence 14.5, standard deviation 30.152 against 2.739 without the 100. Normal quartile factor $2\Phi^{-1}(0.75)=1.349$.
- **Assumed:** The position rule is the one used for every printed quartile. Another interpolation rule would move the non-integer positions.

## Sources opened

1. Dodge (2008), p. 266, local `pdf-0268.txt`. Key `dodge2008`.
2. NIST/SEMATECH §1.3.5.6. Key `nist_handbook2002`.
