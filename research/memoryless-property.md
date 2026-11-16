# Memoryless property

Type: Theorem. Rank 218. Tier: full.

## Material checked

- **Checked:** Baseline 599 words and no figures. The source theorem states the conditional survival identity, the exponential cancellation, and the geometric substitution $(1-p)^{s+t}$. The generator keeps that statement. The added proof derives the same cancellation, the rational-power extension to $S(t)=e^{-\lambda t}$, and the geometric masses $(1-q)q^{n-1}$.
- **Checked:** Grinstead and Snell, printed pp. 68, 164, 186 and 206–207. Page 68 states that an exponential residual lifetime has the original law and that the exponential density is the only continuous density with the property. Page 164 states the bus comparison: exponential mean gap 30 minutes gives mean residual wait 30, while a regular timetable gives mean wait 15. Page 186 derives $\Pr(T>k)=q^k$ and $\Pr(T>r+s\mid T>r)=q^s$. Pages 206–207 compute $e^{-\lambda(r+s)}/e^{-\lambda r}=e^{-\lambda s}$.
- **Checked:** Dodge printed p. 194: density $\theta e^{-\theta x}$ for $x\ge 0$, distribution function $1-e^{-\theta x}$, mean $1/\theta$, variance $1/\theta^2$. The entry does not name the memoryless identity. Dodge printed p. 226: number of failures before the first success has masses $p q^k$ and mean $q/p$.
- **Checked by code:** $e^{-1/2}=0.60653066$ (printed $0.6065$), $e^{-3/8}=0.68728928$ (printed $0.6873$), $e^{-1}=0.36787944$ (printed $0.3679$), $e^{-3}=0.04978707$ (printed $0.0498$), $(3/4)^4=81/256=0.31640625$, $(3/4)^6=729/4096=0.177978515625$, and $q/p=3$ when $p=1/4$.
- **Assumed:** The survival function in the converse is continuous on $[0,\infty)$. Without continuity, a pathological solution of Cauchy's equation could exist; that case is outside the continuous-density claim on p. 68.
- **Disputed:** Nothing in the opened pages contradicts the exponential or geometric identities. Dodge's geometric mean $q/p$ and the trials-until-success mean $1/p$ differ by one because the counts differ by the successful trial. Both are reported, with the indexing named.

## Sources opened and used

1. Charles M. Grinstead and J. Laurie Snell, *Introduction to Probability*, 2nd revised edition, American Mathematical Society, 1997. PDF from `https://math.dartmouth.edu/~prob/prob/prob.pdf`, pp. 68, 164, 186, 206–207. Existing key `grinstead_snell1997`.
2. Yadolah Dodge, *The Concise Encyclopedia of Statistics*, Springer, 2008, printed pp. 194 and 226. Local extract `~/statwiki-sources/dodge2008/pages/pdf-0198.txt` and `pdf-0229.txt`. Existing key `dodge2008`.

## Skipped

The functional equation's proof is written out in the proof box. Grinstead states uniqueness on p. 68; the rational-extension steps are the argument in that box, not a quotation. No separate proofs-todo row. The theorem template has no Check yourself slot, so the three questions sit in the worked example with hidden answers.
