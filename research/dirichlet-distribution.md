# Dirichlet distribution — rank 135 research

## Sources read

- **Checked:** Gelman et al., *Bayesian Data Analysis*, third edition, author-hosted electronic edition `https://sites.stat.columbia.edu/gelman/book/BDA3.pdf`, Chapter 3 §3.4, printed pp. 69–70. The authors' site explicitly offers this PDF for non-commercial use. The chapter gives the multinomial likelihood, Dirichlet prior and posterior, and a three-category election-poll example. The beta marginal in Tokdar p. 1 and direct algebra support the moment formulas; the author-hosted PDF text available to the research browser did not include Appendix A.
- **Checked:** Surya T. Tokdar, *The Dirichlet Distributions*, full two-page handout at `https://www2.stat.duke.edu/~st118/sta941/dirichlet.pdf`, p. 1. It states the simplex density and normalizer, gamma normalization, beta marginals and grouped components, and multinomial conjugacy. The handout is on the author's Duke course site, whose STA 941 page identifies him and the Fall 2018 course.
- **Checked:** Dodge, *The Concise Encyclopedia of Statistics*, the authorized local PDF extraction at `/workspace/statwiki-sources/dodge2008/`, printed p. 363, “Multinomial Distribution.” It gives the count likelihood context but has no direct Dirichlet entry in its index. The page does not cite Dodge for a Dirichlet-specific claim.
- **Assumed:** The Tokdar PDF itself prints no year; 2018 is the course-page year. Historical attribution of the normalizing integral to Dirichlet follows Tokdar p. 1. The inherited original `dirichlet1839` entry is preserved but is not used to assert details of that nineteenth-century paper.

## Baseline and numbers

- **Checked:** Preserve the infobox plot for $\alpha=(2,3,4)$ and the two body simplex figures; the inherited density, mean, variance, interior mode, beta marginal, gamma-normalization proof, three-category update, six-cell advertising example and four question backlinks remain generator content.
- **Checked:** Existing update $\operatorname{Dirichlet}(2,3,5)+(4,1,0)=\operatorname{Dirichlet}(6,4,5)$; first-coordinate means are $2/10=0.2$ and $6/15=0.4$. The six-cell advertising counts total 501 and posterior parameters $(54,58,148,94,39,114)$ total 507. The mean $54/507\approx0.1065$ and joint MAP $53/501\approx0.1058$.
- **Checked:** New worked example prior $(1,1,1)$ plus counts $(2,3,1)$ yields posterior $(3,4,2)$, total 9, posterior mean $(1/3,4/9,2/9)$, predictive category-two probability $4/9\approx0.444444$, beta marginal $P_2\sim\operatorname{Beta}(4,5)$, variance $2/81\approx0.024691$, and covariance $\operatorname{Cov}(P_1,P_2)=-2/135\approx-0.014815$.
- **Checked:** Your-turn prior $(1,2,1)$ plus counts $(3,0,1)$ yields $(4,2,2)$, total 8, mean $(0.5,0.25,0.25)$, combined predictive probability $0.75$, beta marginal $P_1\sim\operatorname{Beta}(4,4)$, variance $1/36\approx0.027778$.
- **Checked:** `q-22` and `ex-applied-restaurant` both have substantive worked answers for Dirichlet updates and summaries.

## Proof scope and integration

The generated property section already contains one collapsed gamma-ratio proof of the beta marginal. This page adds interpretation and applications without a duplicate proof box. The multinomial conjugacy derivation is stated directly in the statistical-inference prose. A pending change relocates substantive `lead_context` text into body content while leaving its citation marker for the distribution-template test.

The build logs the other linked results in `proofs-todo.json`: Dirichlet moments, interior mode, Dirichlet–multinomial conjugacy and the two-category Beta identity. Their page prose gives derivations or references but no separate collapsed proof, so those proof obligations remain explicitly visible.

At the eight-article checkpoint, rank 135 renders about 3,635 body words, three figures, one collapsed proof, a worked example and a hidden practice answer, compared with rank 128's about 2,153 body words, zero figures and the same proof/practice components. Its substantive section coverage has not thinned. Both pages' bank-question IDs are pending shared integration.

- **Checked by code:** New bank questions use a Dirichlet(1,2,3) beta marginal with variance 5/252 and covariance -1/126, and posterior Dirichlet(3,1,2) predictive share 1/6; see the focused check.
