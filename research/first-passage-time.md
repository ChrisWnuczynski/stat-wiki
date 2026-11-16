# First-passage time

Type: concept. Rank 293. Tier: lighter.

## Facts

- **Checked:** Durrett, *Probability: Theory and Examples*, version 5 (11 January 2019), Theorem 4.8.9 and display (4.8.2), printed pp. 260–261. The hitting time is $T_z=\inf\{n:S_n=z\}$. For $p\neq 1/2$, $\varphi(y)=((1-p)/p)^y$ gives $\Pr_x(T_b<T_a)=(\varphi(x)-\varphi(a))/(\varphi(b)-\varphi(a))$. With $a=0$ and $b=d$ this is $(1-(q/p)^x)/(1-(q/p)^d)$.
- **Checked by code:** Fair values $h_2=2/5$, $e_2=6$, $h_4=2/3$, $e_4=8$, bank values $h_5=5/8$, $e_5=15$, and biased values $h_2=135/211$, $h_1=8/15$. The fair duration identity was expanded and matches $x(d-x)$.
- **Assumed:** Steps have size exactly one and both barriers absorb. The formulas are for that walk, not for an unbounded line.
- **Disputed:** Nothing in the cited formula. Dodge’s index has no first-passage entry; the article does not attribute the problem to a Dodge page.

## Sources read

1. Durrett (2019), Theorem 4.8.9, pp. 260–261, author PDF of the fifth edition.
2. Dodge (2008) index, searched for passage, gambler, and ruin; no matching entry.
