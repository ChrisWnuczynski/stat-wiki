# Uniform distribution — rank 96

Type: distribution. Baseline 710 words, two figures. Preserve the PDF/CDF plots, infobox, mean/variance proof, inverse-transform property, convolution example, half-interval example, question links and citations. The existing proofs-todo.json entry logs the unproved inverse-transform method; the page adds no second proof box.

## Sources opened

- **Checked:** Siegrist, *Probability, Mathematical Statistics, and Stochastic Processes*, §5.21, full online chapter on standard and interval uniform laws, densities, CDFs, quantiles, moments and inverse-CDF related distributions.
- **Checked:** authorized Dodge (2008), printed pp. 553–554, “Uniform Distribution”: rectangular terminology, density, CDF, mean, variance, beta relation and rounding-error example.
- **Checked:** von Neumann (1951), full original article in an official Los Alamos National Laboratory hosted reprint, pp. 36–38: generation of random digits, uniform reals and non-uniform target laws.
- **Checked:** answered bank items `ex-prob-generate-uniform`, `ex-prob-min-and-mean`, `ex-prob-name-the-laws`; none repeats the source convolution or half-interval examples.
- **Assumed:** the model of rounding error is flat over its stated interval; this is a modeling assumption, not a universal measurement fact.
- **Disputed:** the generated lead has two sentences because `lead_context` supplies a second substantive sentence. Move its claim to statistical_use, keeping a citation-only context. Also, “equal likelihood” for a continuous law means equal-length sets have equal probability, not a positive point mass at each value.

## Mathematical checks

For U[2,8], width 6, density 1/6, P(3<X<6)=3/6=0.5, mean 5, variance 36/12=3, Q(.9)=7.4. For U[-2,4], P(0<Y<3)=0.5, mean1, variance3, Q(.75)=2.5. The source half-interval U[2,6] gives P(3<X<5)=1/2. Its two-uniform convolution integrates to one and rises/falls on [0,2]. Checked with SciPy and direct integration.
