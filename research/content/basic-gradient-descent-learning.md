## Motivating example
A negative derivative indicates which local direction lowers an error function, but it does not specify how far to move. For example, derivative $-4$ gives update $+0.4$ at learning rate $0.1$ and $+8$ at learning rate $2$. The latter can pass far beyond the region where the local linear approximation is useful.{{cite:zhang_d2l2023}} (§12.3.1, gradient descent in one dimension)

## Interpretation — A local derivative and a finite step
For a differentiable objective $E(w)$, a full-gradient step is $w^+=w-\eta\nabla E(w)$. The directional derivative along $-\nabla E(w)$ is $-\|\nabla E(w)\|^2$. Thus a sufficiently short positive step decreases the objective when the gradient is nonzero. A finite step also encounters curvature. If $E$ is twice continuously differentiable and its Hessian is bounded above by $LI$ along the step, Taylor's bound gives
$$
E(w-\eta g)\le E(w)-\eta(1-L\eta/2)\|g\|^2,\qquad g=\nabla E(w).
$$
The integral remainder is $\eta^2\int_0^1(1-s)g^\top\nabla^2E(w-s\eta g)g\,ds$. Bounding the quadratic form by $L\|g\|^2$ and integrating $1-s$ gives the displayed inequality. The bound ensures descent for $0<\eta<2/L$ under that curvature condition. It supplies no global minimum guarantee for an arbitrary neural-network loss.{{cite:boyd_vandenberghe2004}} (§9.3.1, pp. 467–469)

Backpropagation is one way to calculate $\nabla E$ in a network. Batch learning evaluates it using the entire training objective. Mini-batch and observation-by-observation updates use fewer contributions at each step. Changing from a summed to an averaged loss changes the gradient scale and therefore the effective learning rate.{{cite:zhang_d2l2023}} (§§12.3.2 and 5.3)

## Assumptions and limits — Initialisation and stopping
Random initial weights, such as independent uniforms on $[-0.5,0.5]$, can distinguish otherwise identical hidden units. That numerical interval is not a guarantee against saturation: the input scale and the number of summed inputs also determine a sigmoid's weighted input. Hidden-unit permutations can give different parameter vectors with the same network function. For a sigmoid unit, $g(-u)=1-g(u)$. Negating its incoming weights and its outgoing weight $w$, then changing the next-layer bias from $b$ to $b+w$, leaves $-w(1-h)+(b+w)=wh+b$. A sign change therefore needs this accompanying bias adjustment. Random restarts explore different optimisation trajectories; selecting by training loss alone supplies no independent estimate of predictive performance.{{cite:goodfellow_bengio_courville2016}} (§6.5, p. 200; §5.2, pp. 107–115)

Small changes in weights can arise from a small learning rate as well as proximity to a stationary point. A small gradient, a small objective change and satisfactory prediction on separate validation data answer different questions. In a convex problem, a first-order stopping criterion can have a stronger interpretation when a curvature bound relates gradient size to suboptimality.{{cite:boyd_vandenberghe2004}} (§9.3.1, pp. 467–469)

## Worked example — Contraction, oscillation and divergence
Let $E(w)=\tfrac12(w-3)^2$, with $w_0=0$. Its gradient is $w-3$, so $w_{k+1}-3=(1-\eta)(w_k-3)$. At $\eta=0.5$, the iterates are $0,1.5,2.25,2.625$ and the losses are $4.5,1.125,0.28125,0.0703125$. Each step halves the parameter error and quarters the loss. Convergence holds exactly when $|1-\eta|<1$, or $0<\eta<2$. At $\eta=2$ the iterates alternate between $0$ and $6$; at $\eta=2.5$ their distance from $3$ grows by a factor $1.5$.{{cite:zhang_d2l2023}} (§12.3.1)

For $E(w)=\tfrac12(w_1^2+10w_2^2)$, the two error multipliers are $1-\eta$ and $1-10\eta$. At $\eta=0.1$ they are $0.9$ and $0$, while at $\eta=0.25$ they are $0.75$ and $-1.5$. One coordinate can contract as the other diverges. This illustrates why scale and conditioning matter when choosing one learning rate for many weights.{{cite:boyd_vandenberghe2004}} (§9.3.2, pp. 469–470)

**Your turn.** For the scalar example, what happens at learning rate $1$?

::: {.callout-tip collapse="true" title="Answer"}
The multiplier $1-\eta$ is zero. From any starting value one step reaches $w=3$, the minimum of this particular quadratic.
:::
