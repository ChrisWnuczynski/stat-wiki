# Normal sample theorem

Type: theorem. Rank 297. Tier: lighter.

## Facts

- **Checked:** Siegrist §6.08, “Special Properties of Normal Samples”. For an iid normal sample, the sample mean is normal, it is independent of the sample variance, $(n-1)S^2/\sigma^2$ is chi-squared on $n-1$ degrees of freedom, and $(\overline X-\mu)/(S/\sqrt n)$ is Student $t$ on $n-1$ degrees of freedom.
- **Checked by code:** For $2,4,4,6$, the mean is $4$, $s^2=8/3$, and the $t$ ratio for $\mu=3$ is $\sqrt{3/2}\approx 1.225$. For $1,2,3,6$, the mean is $3$, $s^2=14/3$, and the ratio for $\mu=0$ is about $2.777$. The milk-carton ratio $(1.0512-1.10)/(0.0317/\sqrt{10})$ rounds to $-4.87$.
- **Assumed:** The exact chi-squared law and the exact independence need independent normal observations. The expectation $\E S^2=\sigma^2$ does not.
- **Disputed:** None. A new collapsed proof box was not added. The orthogonal argument is already written with the statement, and it is longer than a short box.

## Sources read

1. Kyle Siegrist, §6.08, Statistics LibreTexts, the sections “The Sample Mean”, “The Sample Variance”, and “The T Variable”.
