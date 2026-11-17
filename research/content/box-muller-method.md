## Lead context
An exponential squared radius and an independent uniform angle together generate the joint density of two independent normal variables.

## Motivating example
A simulation may need normal measurement errors while its random-number generator supplies uniforms. Computing an inverse normal distribution function is one solution; the Box–Muller transformation produces two independent standard normal draws from two independent uniforms using elementary functions. Both outputs can be used in a simulation.{{cite:grinstead_snell1997}} (§5.2, pp. 213–214)

## Definition — Radius and angle from uniforms
Let $U,V$ be independent uniforms on $(0,1)$. Define
$$
R=\sqrt{-2\log U},\qquad\Theta=2\pi V,
\qquad Z_1=R\cos\Theta,\quad Z_2=R\sin\Theta.
$$
Then $Z_1$ and $Z_2$ are independent standard normal variables. The inputs must be independent: giving the two transformations correlated inputs need not produce the desired joint distribution. The logarithm also requires a positive value of $U$.{{cite:grinstead_snell1997}} (§5.2, p. 213)

The squared radius $R^2=-2\log U$ has survival probability $P(R^2>s)=e^{-s/2}$ for $s\geq0$. Its mean is two. Independently, the angle is uniform on a full circle. The circular geometry is the reason a single radius can participate in both outputs without making the resulting normal coordinates dependent.{{cite:siegrist2022_normal_distribution}} (§5.6, Distribution Functions, polar-coordinate normalisation)

## Properties — Factorisation proves independence
The radius has density $re^{-r^2/2}$ on $r>0$, and the independent angle has density $1/(2\pi)$ on $[0,2\pi)$. The polar-to-Cartesian Jacobian has absolute determinant $r$. Dividing their joint density by that factor gives
$$
f_{Z_1,Z_2}(z_1,z_2)=\frac1{2\pi}
\exp\left(-\frac{z_1^2+z_2^2}{2}\right)
=\phi(z_1)\phi(z_2).
$$
The factorisation establishes independence as well as both marginal normal distributions. The exceptional origin and angle boundary have probability zero and do not change the joint law.{{cite:siegrist2022_normal_distribution}} (§5.6, polar-coordinate density calculation);{{cite:grinstead_snell1997}} (§5.2, p. 213)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For $r>0$, $P(R\leq r)=P(U\geq e^{-r^2/2})=1-e^{-r^2/2}$, so differentiating gives the radial density. Independence of $U$ and $V$ gives independence of $R$ and $\Theta$. The Jacobian matrix of $(r\cos\theta,r\sin\theta)$ has determinant $r(\cos^2\theta+\sin^2\theta)=r$. Applying the density transformation gives the product of two standard normal densities displayed above.
:::
:::

## Worked example
Take $U=e^{-2}$ and $V=1/6$. Then $R=2$ and $\Theta=\pi/3$, giving
$$
Z_1=2(1/2)=1,\qquad Z_2=2(\sqrt3/2)=\sqrt3.
$$
The identity $Z_1^2+Z_2^2=-2\log U$ checks the arithmetic: both sides equal four. These are the outputs for this input pair; independence is a property of the random transformation over all possible inputs, not of two fixed numerical values.{{cite:grinstead_snell1997}} (§5.2, p. 213)

To generate a normal draw with mean $\mu$ and standard deviation $\sigma>0$, use $\mu+\sigma Z_1$. For example $3+3Z_1$ has mean three and variance nine. The multiplier is the standard deviation, rather than the variance.{{cite:grinstead_snell1997}} (§5.2, pp. 213–214);{{cite:siegrist2022_normal_distribution}} (§5.6, location-scale family)

**Your turn.** Keep $U=e^{-2}$ but replace $V$ by $5/6$. Find both outputs.

::: {.callout-tip collapse="true" title="Answer"}
The angle becomes $5\pi/3$, where cosine is $1/2$ and sine is $-\sqrt3/2$. The outputs are $(1,-\sqrt3)$, and their squared radius is again four.
:::

## Assumptions and limits — Finite random-number grids
The continuous construction assumes exact independent uniform inputs. In an implementation, a generator that can return zero requires a rule that excludes zero before taking the logarithm. Floating-point uniforms also have a smallest positive representable value in the generator's actual support, which bounds the largest radius the transformation can return. These are properties of the implemented random source; they do not alter the continuous density calculation.{{cite:grinstead_snell1997}} (§§1.1, 5.2, uniform simulation and normal transformation)

