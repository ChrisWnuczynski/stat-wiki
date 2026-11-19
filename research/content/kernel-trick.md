## Motivating example
A linear classifier using a scalar input cannot put the middle of a line in one class and both tails in another. The feature $x^2$ can separate them. A kernel evaluates inner products of expanded features directly, permitting an algorithm written in inner products to use such nonlinear information.{{cite:scholkopf_smola2003_intro}} (§6.2, pp. 54–56)

## Definition — Inner products without explicit coordinates
For a feature map $\phi$ into an inner-product space, define $K(x,x')=\langle\phi(x),\phi(x')\rangle$. In an algorithm depending on observations only through inner products, substitution of $K$ is the kernel trick. A linear function in feature space can correspond to a nonlinear function of the inputs. The representation avoids constructing every feature coordinate; it does not remove the cost of evaluating or storing all required kernel values.{{cite:rasmussen_williams2006}} (§2.1.2, pp. 11–12)

## Properties — Valid kernels and distances
For any sample and coefficients $c$, $c^\top Kc=\|\sum_i c_i\phi(x_i)\|^2\ge0$. Thus its Gram matrix is positive semidefinite. Conversely, a symmetric function whose every finite Gram matrix is positive semidefinite has an inner-product representation. Testing just one sample matrix does not prove the function works on every possible input set.{{cite:scholkopf_smola2003_intro}} (§7, pp. 57–60)

Feature-space distance can also be evaluated using kernels:
$$\|\phi(x)-\phi(x')\|^2=K(x,x)+K(x',x')-2K(x,x').$$
This makes a kernel's diagonal and scale relevant to geometric interpretation. A positive value of a similarity function alone says nothing about positive semidefiniteness.{{cite:rasmussen_williams2006}} (§4.1, pp. 79–80)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For necessity, expand $\|\sum_i c_i\phi(x_i)\|^2$ to obtain the Gram quadratic form. For sufficiency, start with formal finite linear combinations of symbols $e_x$ and set $\langle\sum_i a_ie_{x_i},\sum_j b_je_{z_j}\rangle=\sum_{i,j}a_ib_jK(x_i,z_j)$. Positive semidefiniteness makes every squared norm nonnegative. A vector with squared norm zero has inner product zero with every other vector, since the quadratic squared norm of its sum with any scalar multiple of that other vector cannot be negative. Quotienting out these zero-norm vectors gives an inner-product space. Its Hilbert completion contains the map $\phi(x)=[e_x]$, which satisfies $\langle\phi(x),\phi(x')\rangle=K(x,x')$.{{cite:scholkopf_smola2003_intro}} (§7, pp. 57–60)
:::
:::

## Worked example — Verifying the XOR solution
For the four points $(\pm1,\pm1)$, label equal-sign coordinates $-1$ and opposite-sign coordinates $+1$. The quadratic kernel $K(x,x')=(1+x^\top x')^2$ gives diagonal entries nine and every off-diagonal entry one. Its Gram matrix is $8I+\mathbf1\mathbf1^\top$, with eigenvalues $8,8,8,12$. With all hard-margin multipliers $1/8$, the balance constraint holds and every signed training score equals one. The resulting decision function is $f(x)=-x_1x_2$. It gives $0.25$ at $(0.5,-0.5)$ and $-4$ at $(2,2)$. The kernel obtains the relevant cross-product feature through the inner product.{{cite:scholkopf_smola2003_intro}} (§§4, 6.2, pp. 49–51, 54–56)

**Your turn.** For scalar inputs, verify the feature map $\phi(x)=(1,\sqrt2x,x^2)$ for the same quadratic kernel.

::: {.callout-tip collapse="true" title="Answer"}
The feature inner product is $1+2xx^{\prime}+x^2{x'}^2=(1+xx^{\prime})^2$. The square-root scaling supplies the coefficient two.
:::

## Connections — Covariance models use the same matrix condition
A Gaussian-process covariance function must also give positive semidefinite matrices on every finite input set. Its role is to specify joint uncertainty rather than a classification margin. The polynomial and squared-exponential functions can appear in both settings, while their fitted parameters and interpretation depend on the model.{{cite:rasmussen_williams2006}} (§4.1, pp. 79–80)
