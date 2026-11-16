# Proportional-odds model

Type: concept. Rank 305. Tier: lighter.

## Facts

- **Checked by code:** With intercepts $-1,-2$ and slope $0.5$, the probabilities at $x=2$ are $1/2$ and $1/(1+e)\approx 0.268941$, so the middle category is about $0.231059$. The odds factor is $e^{0.5}\approx 1.649$. At $x=0$ the cumulative probabilities are about $0.268941$ and $0.119203$.
- **Checked:** Yee (2010), *Journal of Statistical Software* 32(10), p. 7, identifies `cumulative(parallel = TRUE)` and `propodds()` as the proportional-odds fit. The article derives the common odds factor directly, so that paper is not given a new bibliography key.
- **Assumed:** The upper-tail form $\Pr(Y\ge k)$ is the convention used here. The intercepts decrease in $k$.
- **Disputed:** None. McCullagh (1980) was not opened.

## Sources read

1. Thomas W. Yee, The VGAM Package for Categorical Data Analysis, JSS 32(10), 2010, p. 7.
