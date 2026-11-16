# Fisher information research notes

- **Checked:** Siegrist, *Probability, Mathematical Statistics, and Stochastic Processes*, §7.5 (official Statistics LibreTexts chapter), score mean zero, information as score second moment, negative expected Hessian under differentiability, iid additivity, Cramér–Rao argument, Bernoulli model. Opened full section at https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/07:_Point_Estimation/7.05:_Best_Unbiased_Estimators .
- **Checked:** Fisher (1922), original full article, §§2, 4, 7, pp. 311–316, 330–332, at https://www.stats.org.uk/statistical-inference/Fisher1922.pdf . It develops information in sufficiency and efficiency historically, not the contemporary score-variance identity; history is phrased accordingly.
- **Checked:** Nelder and Wedderburn (1972), original full article at https://www.maths.usyd.edu.au/u/jchan/GLM/Nelder1972GLM.pdf , §§1.1 and 2.1, pp. 371–374: score identity and expected second derivative; Fisher scoring and weighted least squares.
- **Checked:** Dodge (2008), *The Concise Encyclopedia of Statistics*, p. 35 under Bayesian Statistics, Bernoulli Fisher information $1/[p(1-p)]$ per observation. Local authorized source `/workspace/statwiki-sources/dodge2008/full.txt`.
- **Checked by code:** Bernoulli $n=20$, $S=14$ and $n=50$, $S=20$ arithmetic in `checks/fisher-information.py`.
- **Assumed:** Standard interior regularity conditions when using inverse information as a large-sample covariance approximation; the article states this qualification.
- **Disputed:** None.
