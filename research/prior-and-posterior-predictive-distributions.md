# Prior and posterior predictive distributions research notes

- **Checked:** Gelman et al. (2013), *Bayesian Data Analysis*, third edition, author-hosted full electronic edition https://sites.stat.columbia.edu/gelman/book/BDA3.pdf ; Ch. 1 §1.3 pp. 6–7 gives prior and posterior predictive mixtures and conditional independence, Ch. 2 §2.1 gives beta–binomial conjugacy, Ch. 3 §3.2 predictive variance and normal prediction, Ch. 6 §§6.3–6.5 pp. 143–160 gives predictive checks and hierarchical replication.
- **Checked:** Gelman, Meng and Stern (1996), original full paper author-hosted at https://stat.columbia.edu/~gelman/research/published/A6n41.pdf ; §§2.1 and 4.1 pp. 737–739, 754–756 give posterior predictive reference distributions, prior predictive comparison, improper-prior limitation, and replication choices.
- **Checked:** Dodge (2008) authorized local index and text do not have a dedicated predictive-distribution entry; used for orientation only, not cited.
- **Checked by code:** beta–binomial one- and two-step probabilities in `checks/prior-and-posterior-predictive-distributions.py`.
- **Assumed:** Conditional independence of future and observed Bernoulli outcomes given their shared $p$ in the worked example. The text states the dependence condition explicitly.
- **Disputed:** None.
