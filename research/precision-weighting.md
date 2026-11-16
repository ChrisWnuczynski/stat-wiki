# Precision weighting

Rank 346. Lighter tier. Concept page.

## Facts checked

- Hoff, *Bayes estimators* notes, 10 October 2013, p. 13: if \(\bar X\mid\theta\sim N(\theta,1/n)\) and \(\theta\sim N(0,\tau^2)\), then \(\theta\mid\bar x\sim N(a\bar x, a/n)\) with \(a=n/(n+1/\tau^2)\). Under squared error this posterior mean minimises posterior risk.
- \(n=4\), \(\bar x=10\), \(\tau^2=1\): \(a=0.8\), mean \(8\), variance \(0.2\).
- \(n=5\), \(\bar x=20\), \(\sigma^2=\sigma_0^2=4\), \(\mu_0=16\): \(\kappa_0=1\), mean \(116/6=58/3\).
- \(n=9\), \(\bar x=3\): mean \(2.7\), variance \(0.1\).
- Check: \(\kappa_0=4\), equal weights \(1/2\). Posterior precision \(4+1=5\), variance \(1/5=0.2\).

## Assumed

- The general \(\kappa_0\) formula is the same completion of the square, with a nonzero prior mean and a common observation variance. Hoff's page states the zero-mean unit-variance case.

## Disputed

- None. The extracted fraction on p. 13 is \(a=n/(n+1/\tau^2)\); the numerator sits on the line above the denominator in the notes.

## Not opened

- Gelman et al. and Raiffa and Schlaifer, already cited on the page, were not reopened. No new citation to them is added.
