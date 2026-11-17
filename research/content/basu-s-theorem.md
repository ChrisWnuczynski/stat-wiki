## Lead context
Completeness turns a parameter-free conditional expectation into a constant, yielding independence between two statistics calculated from the same sample.

## Statement
In a model admitting the usual parameter-free conditional distribution given a sufficient statistic $T$, suppose $T$ is boundedly complete and $A$ is ancillary. Then $T$ and $A$ are independent under each parameter value. Full completeness implies the bounded completeness needed for this argument. Ancillarity and completeness must both refer to the same parameter family.{{cite:dasgupta2007_basu}} (§1, pp. 945–946)

## Motivating example
A statistic used to estimate a location parameter and a residual pattern are both computed from the same observations. Their shared data do not by themselves settle whether they are dependent. A complete sufficient statistic captures the parameter information in a precise sense, and an ancillary statistic has the same marginal law for every parameter value. Basu's theorem provides an independence conclusion when these properties hold together.{{cite:siegrist2022_sufficient_complete}} (§7.6, Ancillary Statistics and Basu's theorem)

## Intuition — Three conditions with different roles
Sufficiency gives a conditional law of the sample given $T$ that does not involve the parameter. Ancillarity gives a marginal law of $A$ that does not involve it. Bounded completeness says that if a bounded function $h(T)$ has mean zero for every parameter value, then it is zero almost surely under every member of the model. Each condition addresses a different part of the proof. Neither a small correlation nor a plausible verbal claim of “no information” replaces them.{{cite:dasgupta2007_basu}} (§1, p. 945){{cite:siegrist2022_sufficient_complete}} (§7.6, Complete Statistics)

## Proof
Fix a measurable set $B$ in the range of $A$. Sufficiency lets us write $g_B(T)=\Pr(A\in B\mid T)$ with the same function $g_B$ for every parameter. Ancillarity makes $c_B=\Pr(A\in B)$ independent of the parameter. Therefore
$$
\mathbb E_\theta\{g_B(T)-c_B\}=0\quad\text{for every }\theta.
$$
The function is bounded, so bounded completeness implies $g_B(T)=c_B$ almost surely. For any measurable set $C$ in the range of $T$,
$$
\Pr_\theta(A\in B,T\in C)
=\mathbb E_\theta[\mathbf1_{\{T\in C\}}g_B(T)]
=c_B\Pr_\theta(T\in C).
$$
This is the required factorisation of the joint probabilities. Taking indicators avoids any requirement that $A$ have a density.{{cite:siegrist2022_sufficient_complete}} (§7.6, proof of Basu's theorem){{cite:dasgupta2007_basu}} (§2, pp. 946–947, conditional-distribution formulation)

## Key results — Why sufficiency alone cannot do the job
If an ancillary statistic is a nonconstant function of a sufficient statistic, it cannot be independent of that statistic. For any event determined by that function, independence from itself would force its probability to equal its square, hence to be zero or one. Such examples reveal the missing completeness hypothesis. In a location-uniform sample, the range is ancillary and is a function of the pair of extreme order statistics, illustrating the obstruction.{{cite:siegrist2022_sufficient_complete}} (§7.6, sufficiency, completeness and ancillary statistics)

## Worked example
Let $X_1,X_2$ be independent exponentials with rate $\lambda>0$. Set $S=X_1+X_2$ and $R=X_1/S$. For $s>0$ and $0<r<1$, the transformation $x_1=rs$, $x_2=(1-r)s$ has Jacobian magnitude $s$. The joint density is
$$
f_{S,R}(s,r)=\lambda^2s e^{-\lambda s}\,\mathbf1_{\{s>0\}}\mathbf1_{\{0<r<1\}}.
$$
The first factor integrates to one in $s$, and the second is the uniform density in $r$. This directly proves independence and shows why the ratio contains no rate information. The factorisation also identifies $S$ as sufficient; the complete exponential-family structure permits the same independence conclusion through Basu's theorem.{{cite:dasgupta2011_exponential_family}} (§18.4, Thm. 18.8–18.9, pp. 511–512)

At rate one, $\Pr(S>2)=3e^{-2}=0.406006$. Independence gives
$$
\Pr(R\le1/4,S>2)=\frac14(3e^{-2})=0.101501.
$$
For observed values $X_1=0.4$, $X_2=1.6$, the realised total is two and the ratio is $0.2$; independence describes their repeated-sampling law while the realised total and ratio remain algebraic functions of the observations.

**Your turn.** Still at rate one, calculate $\Pr(R\le1/2\mid S>2)$.

::: {.callout-tip collapse="true" title="Answer"}
It is $1/2$. The event involving $S$ does not change the uniform distribution of $R$, since the two variables are independent.
:::
