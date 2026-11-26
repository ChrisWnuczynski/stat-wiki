## Motivating example
At one feature value, three classes have conditional probabilities $(0.20,0.55,0.25)$. A rule must return one label. Under zero–one loss, class $2$ has error probability $0.45$, compared with $0.80$ and $0.75$ for classes $1$ and $3$. The optimal label follows from conditional expected loss, rather than from geometric distance alone.{{cite:rasmussen_williams2006}} (§3.1.1, p. 36)

## Intuition — Minimise before averaging over features
Let $\tau_g(x)=P(Y=g\mid X=x)$ and $\delta(x)$ be a measurable class prediction. Under zero–one loss,
$$
R(\delta\mid x)=\sum_g\mathbf1\{\delta(x)\ne g\}\tau_g(x)
=1-\tau_{\delta(x)}(x).
$$
The smallest conditional risk is $1-\max_g\tau_g(x)$. If posteriors are $(0.40,0.40,0.20)$, predicting either of the first two classes gives risk $0.60$. A fixed tie-breaking convention makes the rule unambiguous. Randomisation over tied maximisers gives the same risk; assigning positive probability to a strictly inferior class increases it.{{cite:pishro_nik2014}} (§9.1.8, MAP hypothesis test)

## Proof
For every $x$, $\tau_{\delta(x)}(x)\le\max_g\tau_g(x)$. Taking expectations of the resulting conditional-risk inequality yields
$$
R(\delta)=\E[1-\tau_{\delta(X)}(X)]\ge
\E[1-\max_g\tau_g(X)]=R^*.
$$
Equality holds exactly when the nonnegative difference $\max_g\tau_g(X)-\tau_{\delta(X)}(X)$ is zero almost surely. Thus a rule is Bayes-optimal when it selects a true maximiser except on a feature set of probability zero. This argument assumes a finite class set and measurable conditional probabilities and decisions.{{cite:rasmussen_williams2006}} (§3.1.1, p. 36)

## Key results — Probability estimation and decision accuracy differ
A plug-in classifier replaces $\tau$ by an estimate $\widehat\tau$. It attains Bayes risk if its chosen labels are true maximisers almost surely; its estimated probability vector need not equal the true vector. Conversely, reporting a confident probability does not establish a low classification risk. Under a general loss matrix $L(a,g)$, the relevant comparison is $\sum_gL(a,g)\tau_g(x)$, so largest-posterior classification is specific to equal error costs.{{cite:rasmussen_williams2006}} (§3.1.1, p. 36)

Bayes risk describes irreducible error relative to the observed features, data-generating law and loss. Additional information can improve the attainable rule, while a finite training procedure must estimate unknown distributions. The oracle comparison does not mean that a fitted method knows the true conditional probabilities.{{cite:goodfellow_bengio_courville2016}} (§5.2, pp. 113–115)

## Worked example

### Integrating local mistakes
Suppose $P(X=A)=0.6$ and $P(X=B)=0.4$, with class probabilities $(0.20,0.55,0.25)$ at $A$ and $(0.40,0.40,0.20)$ at $B$. Predict class $2$ at $A$ and either class $1$ or $2$ at $B$. Then
$$
R^*=0.6(0.45)+0.4(0.60)=0.51.
$$
A rule predicting class $1$ at $A$ and class $3$ at $B$ has risk $0.6(0.80)+0.4(0.80)=0.80$. Its excess risk is $0.29$, exactly the weighted loss from failing to choose a largest posterior at the two feature values.{{cite:pishro_nik2014}} (§9.1.8)

**Your turn.** A third rule predicts class $2$ at $A$ and class $1$ at $B$, but reports probability vectors $(0.1,0.8,0.1)$ and $(0.5,0.3,0.2)$. What is its classification risk?

::: {.callout-tip collapse="true" title="Answer"}
It chooses a true posterior maximiser at both feature values and therefore has risk $0.51$. Its reported probabilities are inaccurate, but those errors do not change these zero–one decisions.
:::
