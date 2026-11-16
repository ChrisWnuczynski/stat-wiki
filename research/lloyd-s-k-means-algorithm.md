# Lloyd's K-means algorithm

Type: concept. Rank 301. Tier: lighter.

## Facts

- **Checked by code:** Points $0,1,10$ with centres $0,10$ update to $0.5,10$ with sum of squares $0.5$. Points $0,8,10$ update to $0,9$ with sum of squares $2$. Stirling numbers $S(4,2)=7$ and $S(10,3)=9330$.
- **Checked:** The mean identity $\sum\|x_i-m\|^2=\sum\|x_i-\bar x\|^2+N\|\bar x-m\|^2$ is expanded in the proof box.
- **Checked and not cited:** James et al., ISLR corrected 7th printing, Algorithm 10.1, §10.3.1, pp. 387–388, alternates centroids and nearest-centre assignment. Lloyd (1982) was not opened.
- **Assumed:** Clusters stay nonempty, and ties keep the current label.
- **Disputed:** None.

## Sources read

1. James et al., ISLR, corrected 7th printing, §10.3.1.
