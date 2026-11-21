## Lead context
Boosting builds a strong classifier by fitting each new weak rule to the training cases the rules so far still get wrong.

## Motivating example
Four cases start with weights $1/4$. A stump that misses one of them has weighted error $1/4$ and vote $\tfrac12\log 3$. After the update the mistaken case has weight $1/2$ and each correct case has weight $1/6$.

## Intuition — Aim the next rule at the remaining mistakes
A single decision stump looks at one coordinate and one threshold. On a hard classification problem that stump may be only a little better than a coin toss. Boosting does not average many such stumps fitted to the same problem. It changes the problem. Cases the latest stump missed receive more weight, cases it got right receive less, and the next stump is fitted to the reweighted sample. The final prediction is the sign of a weighted vote, and a stump that was only slightly better than chance receives only a small vote.{{cite:hastie_esl2009}} (p. 339, Algorithm 10.1){{cite:schapire1990}} (pp. 197–198)

## Definition — The half-log vote and the weight update
Label the classes $y_i\in\{-1,+1\}$. At round $t$ a classifier $f_t$ has weighted error $\varepsilon_t\in(0,1)$. The symmetric update uses

$$
\alpha_t=\frac12\log\frac{1-\varepsilon_t}{\varepsilon_t}
$$

and replaces the weight $w_{t,i}$ by a multiple of $w_{t,i}\exp(-\alpha_t y_i f_t(x_i))$, then divides by the sum of those multiples so that the new weights sum to $1$. The ensemble is the sign of $\sum_t\alpha_t f_t(x)$.{{cite:freund_schapire1997}} (p. 12)

Hastie, Tibshirani and Friedman write the same round with vote weight $\log((1-\varepsilon_t)/\varepsilon_t)$, twice $\alpha_t$, and multiply only the misclassified weights by the exponential of that larger coefficient. A misclassified weight then grows relative to a correctly classified weight by $(1-\varepsilon_t)/\varepsilon_t$ in both writings, so the normalised weight distribution is the same, and the sign of the vote is the same.{{cite:hastie_esl2009}} (p. 339, Algorithm 10.1)

## Properties — The rule just fitted becomes a coin toss
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Assume the current weights sum to $1$, and write $\alpha=\frac12\log((1-\varepsilon)/\varepsilon)$ with $0<\varepsilon<1$. Then $e^{\alpha}=\sqrt{(1-\varepsilon)/\varepsilon}$ and $e^{-\alpha}=\sqrt{\varepsilon/(1-\varepsilon)}$. The un-normalised weight of the misclassified cases is $\varepsilon e^{\alpha}=\sqrt{\varepsilon(1-\varepsilon)}$, and the un-normalised weight of the correctly classified cases is $(1-\varepsilon)e^{-\alpha}=\sqrt{\varepsilon(1-\varepsilon)}$. The two groups therefore carry the same total weight. After normalisation each group has total weight $1/2$, so the weighted error of this same rule on the new weights is $1/2$.{{cite:freund_schapire1997}} (p. 12)
:::
:::

## Worked example — One mistake among four equally weighted cases
Four labelled cases start with weights $1/4,1/4,1/4,1/4$. A stump classifies three of them correctly and one incorrectly, so $\varepsilon=1/4$ and

$$
\alpha=\frac12\log 3\approx 0.5493.
$$

The normaliser is $2\sqrt{(1/4)(3/4)}=\sqrt3/2$. Each correct case then has new weight $1/6$, and the incorrect case has new weight $1/2$. The three correct weights sum to $1/2$, and the one incorrect weight is $1/2$, which is the coin-toss error proved above. The ratio of the incorrect multiplier to the correct multiplier is $3=(1-\varepsilon)/\varepsilon$.

**Your turn.** A later round has weighted error $1/5$. Find $\alpha$ as a logarithm, and find the factor by which an incorrect weight grows relative to a correct weight.

::: {.callout-tip collapse="true" title="Answer"}
$\alpha=\frac12\log 4=\log 2$. The relative factor is $(1-1/5)/(1/5)=4$. The logarithm is positive because $1/5<1/2$, so this round still receives a positive vote.
:::

## Connections — What boosting is not averaging
[Bagging](bagging.qmd) and a [random forest](random-forest.qmd) draw diversity from different samples. Boosting manufactures diversity by reweighting. The base rule is often a [decision stump](decision-stump.qmd), and the particular half-log update above is [AdaBoost](adaboost.qmd). A round with error above $1/2$ gets a negative vote, which is a vote for the opposite label.{{cite:freund_schapire1997}} (p. 12){{cite:schapire1990}} (pp. 197–198)
