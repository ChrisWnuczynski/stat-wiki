## Motivating example
Suppose a straight-line calibration experiment is repeated many times at the same input settings. A fitted slope varies between repetitions because the responses contain noise. Unbiasedness asks whether the average of those fitted slopes equals the slope in the response-generating model. It is a property of an estimator over repeated samples, not a statement that one observed slope equals the truth.{{cite:goodfellow_bengio_courville2016}} (§5.4.2, eq. 5.20, pp. 122–124)

The relevant assumption is the mean of the error conditional on the design. Knowing only that errors average to zero across an uncontrolled mixture of inputs is insufficient if their mean varies with those inputs. The design matrix and the conditional expectation must refer to the same regression experiment.{{cite:dodge2008}} (pp. 364–365)

## Statement
Let $Y=X\beta+\varepsilon$, where the $n\times p$ matrix $X$ has rank $p$, the vector $\beta$ is fixed, and $E(\varepsilon\mid X)=0$. Assume the required first moments exist. Then the least-squares estimator $\widehat\beta=(X^\top X)^{-1}X^\top Y$ satisfies $E(\widehat\beta\mid X)=\beta$. With a fixed design, this is ordinary unbiasedness. With a random design, unconditional unbiasedness follows by the tower property when the estimator is integrable. No Gaussian assumption is required for this expectation identity.{{cite:dodge2008}} (p. 365){{cite:goodfellow_bengio_courville2016}} (§5.4.2, definition of unbiasedness)

Conditional unbiasedness and the existence of an unconditional mean are distinct when the random design can be nearly singular. The conditional equality alone is not a license to ignore integrability. In routine finite fixed-design calculations, every coefficient estimate is a fixed linear combination of integrable responses, so the requirement is transparent.

## Proof
Put $A=(X^\top X)^{-1}X^\top$. Conditional on $X$, this matrix is fixed and $AX=I_p$. Therefore
$$\widehat\beta=A(X\beta+\varepsilon)=\beta+A\varepsilon,$$
so $E(\widehat\beta\mid X)=\beta+AE(\varepsilon\mid X)=\beta$. The formula is the entire unbiasedness argument. It separates the algebraic identity $AX=I_p$ from the probabilistic premise about the errors. Neither assumption can replace the other.{{cite:dodge2008}} (p. 365)

If instead $E(\varepsilon\mid X)=m(X)$, the same calculation gives conditional bias $Am(X)$. A nonzero error mean need not bias every coefficient: a component orthogonal to the column space of $X$ is annihilated by $A$. The required condition for unbiasedness at that design is $X^\top m(X)=0$; the zero conditional mean is a useful sufficient assumption that does not depend on such a cancellation.

## Key results — Variance and fitted means are separate questions
If $\operatorname{Cov}(\varepsilon\mid X)=\Omega$, then the same linearity gives
$$\operatorname{Cov}(\widehat\beta\mid X)=A\Omega A^\top.$$
For $\Omega=\sigma^2I_n$, this reduces to $\sigma^2(X^\top X)^{-1}$. Heteroscedasticity changes the covariance formula but does not undo unbiasedness when the conditional mean assumption remains true. A Gaussian sampling model adds exact distributional results; it is stronger than the assumptions used in the expectation proof.{{cite:dodge2008}} (p. 365)

For a fixed new design row $x_*^\top$, the fitted mean $x_*^\top\widehat\beta$ is unbiased for $x_*^\top\beta$ by linearity. A new response also contains a new error term. Unbiased estimation of its mean does not make its prediction error vanish, nor does it establish a reliable confidence level without a variance calculation.{{cite:goodfellow_bengio_courville2016}} (§§5.4.2–5.4.3)

## Worked example
### Enumerate every possible error vector
Use the three-row design $X=((1,0),(1,1),(1,2))^\top$ and coefficient vector $(1,2)^\top$. Let each error independently equal $-1$ or $1$ with probability $1/2$. There are eight equally likely error vectors. The matrix mapping errors into coefficient errors is
$$A=\begin{pmatrix}5/6&1/3&-1/6\\-1/2&0&1/2\end{pmatrix}.$$
Averaging the eight least-squares fits gives intercept one and slope two exactly. The error distribution is discrete, illustrating that normality is unnecessary. The conditional covariance of the fitted coefficients is
$$AA^\top=\begin{pmatrix}5/6&-1/2\\-1/2&1/2\end{pmatrix}.$$
These quantities follow from the expectation and covariance calculations above.{{cite:dodge2008}} (p. 365)

If instead the error mean is $m=(0,1,2)^\top$, it equals the slope column of $X$. The conditional bias is then $Am=(0,1)^\top$: the fitted intercept stays unbiased and the fitted slope has bias one. This failure has a systematic direction, rather than arising merely from one unfavorable sample.

**Your turn.** Keep the same design but give every error mean the value $0.5$. What are the intercept and slope biases?

::: {.callout-tip collapse="true" title="Answer"}
The mean error vector is half the intercept column. Multiplication by $A$ gives $(0.5,0)^\top$. The intercept bias is $0.5$ and the slope bias is zero.
:::

## Common misconceptions — Zero bias is only one performance criterion
A small sample can produce a very inaccurate unbiased estimate. Its spread, the size of its errors under a chosen loss and its sensitivity to unusual observations are further properties. An estimator with some bias may have smaller mean squared error if its variance is sufficiently reduced. The identity $E[(\widehat\theta-\theta)^2]=\operatorname{Var}(\widehat\theta)+\operatorname{Bias}(\widehat\theta)^2$ makes that tradeoff explicit.{{cite:goodfellow_bengio_courville2016}} (§5.4.4, bias–variance tradeoff)

Fitting additional columns does not automatically repair a nonzero conditional error mean. The scientific interpretation of the regression still depends on what variables were measured, how observations were selected and whether the modeled conditional mean is appropriate. The proof gives a precise implication under assumptions; checking those assumptions is a separate part of statistical analysis.
