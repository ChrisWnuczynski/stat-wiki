## Motivating example
A regression may contain hundreds of plausible predictors but only a modest number of observations. Selecting a small subset reduces the number of coefficients to estimate; shrinkage limits their magnitudes. These approaches answer related but different questions: which variables to use, and how strongly to fit them.{{cite:boyd_vandenberghe2004}} (§6.3.2, Ex. 6.4, p. 310)

## Interpretation — Searching models or penalising coefficients
Best subset selection compares fits over sparsity patterns. At a fixed subset size $k$, there are $\binom pk$ possible subsets, and across every size there are $2^p$. For $p=20$ this is $1,048,576$ models; for $p=30$ it exceeds one billion. A forward path that adds one predictor at each stage evaluates $1+p+(p-1)+\cdots+1=1+p(p+1)/2$ candidate fits, or $211$ at $p=20$, counting an intercept-only starting fit once. This reduction is achieved by restricting the search, so it can miss the best subset at a given size. Exhaustive search is a combinatorial optimisation problem.{{cite:boyd_vandenberghe2004}} (§6.3.2, Ex. 6.4, p. 310)

The penalty $\|\beta\|_0$ counts nonzero coordinates; it is not a norm, since multiplying a nonzero vector by two leaves the count unchanged. The $L_1$ penalty is convex and promotes exact zeros, while an $L_2$ squared penalty gives a smooth quadratic tradeoff. A sparse penalised fit need not equal the least-squares fit on the selected variables: shrinkage still affects its nonzero coefficients. Refitting on the selected subset removes that penalty but changes the procedure and its uncertainty.{{cite:boyd_vandenberghe2004}} (§6.3.2, pp. 308–310)

## Worked example — Selection and estimation separate
With orthonormal columns and least-squares coefficients $b=(2.4,-0.9,0.5,-0.1)$, minimise raw residual sum of squares plus a penalty with $\lambda=2$. An $L_0$ penalty compares $b_j^2$ with two and selects only the first coordinate, fitted at $2.4$. Lasso compares $|b_j|$ with one and also selects only the first coordinate, fitted at $1.4$. Ridge gives $(0.8,-0.3,1/6,-1/30)$ and selects no coordinates out by exact zero. Identical selected supports can therefore hide materially different predictions.{{cite:parikh_boyd2014_proximal}} (§6.5.2, eq. 6.9){{cite:boyd_vandenberghe2004}} (§6.3.2, eq. 6.10)

**Your turn.** For an orthonormal design with $b=(1,0.5)$ and raw $L_0$ penalty one, describe every minimiser.

::: {.callout-tip collapse="true" title="Answer"}
The second coordinate must be zero because $0.5^2<1$. In the first coordinate, zero and one have equal objective value. Thus the two minimisers are $(0,0)$ and $(1,0)$.
:::

## Statistical use — Evaluate the selection procedure
Prediction error and recovery of a scientifically meaningful support are different targets. Correlated predictors can substitute for one another in prediction, while finite samples can make the selected set unstable. A method's predictive success alone cannot establish that every selected coefficient corresponds to a necessary causal variable.{{cite:cawley_talbot2010}} (§1, pp. 2079–2081)

Validation must repeat every data-dependent selection step. Ranking genes with all response labels before splitting into cross-validation folds allows validation labels to influence the predictors presented to the training algorithm. Feature selection and penalty tuning belong inside the training portion of each assessment split; a final test set assesses the resulting selection procedure. Searching many noisy validation scores can itself overfit the criterion.{{cite:cawley_talbot2010}} (§2, pp. 2081–2084)
