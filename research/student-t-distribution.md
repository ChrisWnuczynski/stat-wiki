# Student t distribution

Type: Distribution. Rank 275. Tier: lighter.

## Material checked

- **Checked:** Baseline 1215 words, 3 figures. Student, “The probable error of a mean”, *Biometrika* 6 (1908), pp. 1–2 of the York typeset copy, which carries the original page numbers: a small sample is the only guide to variability. Dodge printed p. 526: the density, the representation T=Z/√(X/ν), and the one-sample statistic on n−1 degrees of freedom. Dodge p. 60 identifies one degree of freedom with the standard Cauchy law and states that the Cauchy mean does not exist.
- **Checked by code:** Variance 5/3≈1.6667, P(|T_5|>2)≈0.1019, normal tail ≈0.0455, t_8 variance 4/3≈1.3333, t_8 0.975 quantile 2.30600, normal 0.975 quantile 1.95996. `checks/student-t-distribution.py`.
- **Assumed:** The catalogue proof that ν=1 is Cauchy is left in place. Independence of Z and X is part of Dodge’s representation and is not re-proved.
- **Not opened:** Casella and Berger; Fisher 1925, which Dodge mentions and which was not read.

## Sources opened

1. Student, *Biometrika* 6 (1908), pp. 1–2. Key `student1908`. York history-of-statistics typeset copy with the journal page numbers.
2. Dodge, printed pp. 60 and 526. Key `dodge2008`.
