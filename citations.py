"""Academic bibliography mappings and Wikipedia-style numbered reference rendering for StatWiki.

All bibliographic metadata live in ``bibliography.json`` and are verified
against Crossref, OpenAlex, OpenLibrary, and archival URLs by
``verify_citations.py``. This module maps chapters, concept articles,
reference sheets, ``overview.qmd``, interactive laboratories, and dataset-based
questions to their specific foundational works, modern textbooks, and dataset
sources, and renders clickable numbered superscript in-text citations ``[1]``,
``[2]``, ... paired with a numbered ``## References`` list and jump-back links.
"""

from __future__ import annotations

import html
import json
import re
import unicodedata
import urllib.parse
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BIB_PATH = ROOT / "bibliography.json"

OVERVIEW_REFS: tuple[str, ...] = ('bayes1763',
 'gauss1809',
 'pearson1900',
 'student1908',
 'fisher1922',
 'fisher1935_doe',
 'kolmogorov1933_slln',
 'neyman_pearson1933',
 'neyman1937',
 'rao1945',
 'cramer1946',
 'metropolis1953',
 'nelder_wedderburn1972',
 'efron1979',
 'liang_zeger1986',
 'hastie_tibshirani1990',
 'tibshirani1996',
 'breiman2001_rf',
 'gelman_bda2013',
 'wasserman2004',
 'hastings1970')

REFERENCE_REFS: dict[str, tuple[str, ...]] = {'distributions.qmd': ('bernoulli1713',
                       'demoivre1756',
                       'bayes1763',
                       'gauss1809',
                       'poisson1837',
                       'dirichlet1839',
                       'pearson1895',
                       'raiffa_schlaifer1961',
                       'feller1968',
                       'forbes2011',
                       'casella_berger2002'),
 'formulas.qmd': ('bayes1763',
                  'jeffreys1961',
                  'raiffa_schlaifer1961',
                  'box_tiao1973',
                  'diaconis_ylvisaker1979',
                  'metropolis1953',
                  'hastings1970',
                  'geman_geman1984',
                  'gelman_bda2013',
                  'casella_berger2002')}

LAB_REFS: dict[str, tuple[str, ...]] = {'beta-binomial.qmd': ('bernoulli1713',
                       'bayes1763',
                       'laplace1812',
                       'raiffa_schlaifer1961',
                       'diaconis_ylvisaker1979',
                       'gelman_bda2013'),
 'ci-coverage.qmd': ('student1908',
                     'wilson1927',
                     'clopper_pearson1934',
                     'neyman1937',
                     'brown_cai_dasgupta2001',
                     'casella_berger2002'),
 'index.qmd': ('bayes1763',
               'markov1906',
               'student1908',
               'wilson1927',
               'neyman1937',
               'rosenblatt1956',
               'parzen1962',
               'silverman1986'),
 'kernel-density.qmd': ('rosenblatt1956',
                        'parzen1962',
                        'epanechnikov1969',
                        'silverman1986',
                        'sheather_jones1991'),
 'markov-chain.qmd': ('markov1906',
                      'chapman1928',
                      'kolmogorov1931',
                      'feller1968',
                      'norris1997',
                      'grimmett_stirzaker2020')}

QUESTION_REFS: dict[str, tuple[str, ...]] = {'ex-cholesterol-gam': ('hastie_tibshirani1990',
                        'wood2011',
                        'wood2017',
                        'hosmer_lemeshow2000'),
 'ex-da-birth-weight': ('hosmer_lemeshow2000', 'venables_ripley2002'),
 'ex-fish-poisson': ('barbour_brown1974', 'nelder_wedderburn1972', 'wood2017'),
 'ex-inf-frizzle': ('landauer_dunn1930', 'pearson1900', 'fisher1925_smrw'),
 'ex-orthodont-lmm': ('potthoff_roy1964', 'laird_ware1982', 'bates_lme4_2015'),
 'ex-sl-06-5': ('akaike1974', 'schwarz1978', 'drton_plummer2017'),
 'ex-sl-08-7': ('fisher1936', 'anderson1936_iris'),
 'ex-sl-16-6': ('sejnowski_rosenberg1986',
                'sejnowski_rosenberg1987',
                'rumelhart_hinton_williams1986'),
 'ex-toenail-glmm': ('debacker1998_toenail',
                     'lesaffre_spiessens2001',
                     'breslow_clayton1993',
                     'bates_lme4_2015'),
 'ex-ur-exchangeable-bound': ('potthoff_roy1964', 'liang_zeger1986'),
 'ex-ur-held-out-label': ('fisher1936', 'anderson1936_iris', 'mclachlan_peel2000_book'),
 'ex-ur-mean-or-new-day': ('chambers1983_gmda', 'venables_ripley2002'),
 'ex-ur-two-fits': ('chambers1983_gmda', 'rubin1976_missing'),
 'ex-ur-what-a-row-is': ('chambers1983_gmda', 'rubin1976_missing'),
 'exr-full-bayes-and-interval-width': ('tarone1982',
                                       'dempster_selwyn_weeks1983',
                                       'gelman_bda2013'),
 'q-13': ('ruggles_brodie1947',
          'bayes1763',
          'pareto1909',
          'darmois1935',
          'pitman1936',
          'koopman1936'),
 'q-23': ('tarone1982', 'dempster_selwyn_weeks1983', 'gelman_bda2013'),
 'q-36': ('hastie_tibshirani1990', 'wood2011', 'wood2017'),
 'q-37': ('hastie_tibshirani1990', 'wood2011', 'wood2017'),
 'q-38': ('berkson1944', 'hastie_tibshirani1990', 'wood2017'),
 'q-39': ('debacker1998_toenail', 'breslow_clayton1993', 'bates_lme4_2015'),
 'q-40': ('debacker1998_toenail', 'breslow_clayton1993', 'bates_lme4_2015'),
 'q-41': ('debacker1998_toenail', 'lesaffre_spiessens2001', 'bates_lme4_2015')}

CHAPTER_REFS: dict[str, tuple[str, ...]] = {'01-introduction-to-glms.qmd': ('fisher1925_est',
                                 'berkson1944',
                                 'hurn1945',
                                 'nelder_wedderburn1972',
                                 'mccullagh_nelder1989',
                                 'davison2003'),
 '02-inference-and-counts.qmd': ('greenwood_yule1920',
                                 'bliss1935',
                                 'conway_maxwell1962',
                                 'nelder_wedderburn1972',
                                 'mccullagh_nelder1989',
                                 'loader1999_locfit',
                                 'shmueli2005',
                                 'myers_glm2010',
                                 'huang2017_cmp',
                                 'davison2003'),
 '03-gamma-and-quasi.qmd': ('hurn1945',
                            'tweedie1957',
                            'wedderburn1974',
                            'mccullagh_nelder1989',
                            'cameron_johansson1997',
                            'huang_rathouz2017',
                            'huang2017_cmp',
                            'davison2003'),
 '04-categorical-responses.qmd': ('ashford1959',
                                  'cox1972',
                                  'mccullagh1980',
                                  'fahrmeir_tutz2001',
                                  'tutz2011',
                                  'yee2015',
                                  'agresti2002'),
 '05-comparisons-and-deviance.qmd': ('bradley_terry1952',
                                     'nelder_wedderburn1972',
                                     'akaike1974',
                                     'mccullagh_nelder1989',
                                     'fahrmeir_tutz2001',
                                     'myers_glm2010',
                                     'agresti2002',
                                     'davison2003'),
 '06-pit-residuals.qmd': ('rosenblatt1952_pit',
                          'dawid1984',
                          'dunn_smyth1996',
                          'davison2003'),
 '06-smooth-means.qmd': ('reinsch1967',
                         'wahba1990',
                         'hastie_tibshirani1990',
                         'green_silverman1994',
                         'holst1996_lidar',
                         'ruppert_wand_carroll2003',
                         'wood2003',
                         'wood2011',
                         'wood2017',
                         'deboor1978'),
 '07-additive-and-mixed.qmd': ('engle1986_plm',
                               'hastie_tibshirani1986',
                               'hastie_tibshirani1990',
                               'wood2011',
                               'wood2017'),
 '08-random-intercepts.qmd': ('fisher1925_smrw',
                              'patterson_thompson1971',
                              'henderson1975',
                              'laird_ware1982',
                              'davison2003'),
 '08-slopes-and-glmms.qmd': ('henderson1975',
                             'laird_ware1982',
                             'self_liang1987',
                             'breslow_clayton1993',
                             'steele_diamond1999',
                             'belenky2003',
                             'bates_lme4_2015'),
 '09-marginal-models.qmd': ('tippett1950_warp',
                            'huber1967',
                            'white1980',
                            'liang_zeger1986',
                            'zeger_liang_albert1988',
                            'song2007_burn'),
 '10-plants-and-series.qmd': ('liang_zeger1986', 'yee_mitchell1991', 'yee2015'),
 '11-forecasting.qmd': ('box_jenkins1970',
                        'akaike1974',
                        'dickey_fuller1979',
                        'engle1982',
                        'bollerslev1986',
                        'brockwell_davis1991',
                        'makridakis1998',
                        'hyndman_khandakar2008',
                        'granger_newbold1974',
                        'hyndman_athanasopoulos2021'),
 '12-time-series.qmd': ('yule1927',
                        'khinchin1934',
                        'slutsky1937',
                        'wold1938',
                        'matheron1963',
                        'box_jenkins1970',
                        'rasmussen_williams2006',
                        'brockwell_davis1991',
                        'hyndman_athanasopoulos2021'),
 'bayes-01-foundations.qmd': ('bayes1763',
                              'laplace1812',
                              'definetti1937',
                              'jeffreys1961',
                              'box_tiao1973',
                              'gelman_bda2013'),
 'bayes-02-beta-binomial.qmd': ('bernoulli1713',
                                'bayes1763',
                                'laplace1812',
                                'raiffa_schlaifer1961',
                                'diaconis_ylvisaker1979',
                                'diaconis_coin2007',
                                'gelman_bda2013'),
 'bayes-03-normal-models.qmd': ('gauss1809',
                                'laplace1812',
                                'jeffreys1961',
                                'raiffa_schlaifer1961',
                                'box_tiao1973',
                                'gelman_bda2013'),
 'bayes-04-mcmc.qmd': ('markov1906',
                       'ising1925',
                       'metropolis_ulam1949',
                       'metropolis1953',
                       'hastings1970',
                       'geman_geman1984',
                       'gelfand_smith1990',
                       'gelman_rubin1992',
                       'geyer1992',
                       'gubernatis2005',
                       'gelman_bda2013',
                       'robert_casella2004'),
 'bayes-05-categorical.qmd': ('dirichlet1839',
                              'raiffa_schlaifer1961',
                              'gelman_bda2013'),
 'bayes-06-testing.qmd': ('wald1950',
                          'jeffreys1961',
                          'kass_raftery1995',
                          'gelman_bda2013'),
 'bayes-07-exponential-families.qmd': ('fisher1922',
                                       'darmois1935',
                                       'pitman1936',
                                       'koopman1936',
                                       'halmos_savage1949',
                                       'lehmann_scheffe1950',
                                       'basu1955',
                                       'diaconis_ylvisaker1979',
                                       'lehmann_casella1998',
                                       'casella_berger2002'),
 'bayes-08-hierarchy.qmd': ('definetti1937',
                            'robbins1956',
                            'james_stein1961',
                            'lindley_smith1972',
                            'efron_morris1975',
                            'tarone1982',
                            'dempster_selwyn_weeks1983',
                            'lunn_winbugs2000',
                            'barendse2004_tg5',
                            'gelman2006',
                            'wood_mengersen2006_tg5',
                            'gelman_bda2013'),
 'bayes-09-linear-regression.qmd': ('legendre1805',
                                    'gauss1809',
                                    'jeffreys1961',
                                    'raiffa_schlaifer1961',
                                    'box_tiao1973',
                                    'zellner1986',
                                    'berger_bernardo_sun2009',
                                    'gelman_bda2013'),
 'da-01-studies-and-data.qmd': ('neyman1934',
                                'fisher1935_doe',
                                'hill1948_rct',
                                'simpson1951',
                                'cochran1977',
                                'casella_berger2002',
                                'wasserman2004'),
 'da-02-descriptive-statistics.qmd': ('pearson1895',
                                      'box_cox1964',
                                      'wilk_gnanadesikan1968',
                                      'tukey1977',
                                      'chicco_jurman2020',
                                      'wasserman2004'),
 'da-03-using-r.qmd': ('wilkinson_rogers1973',
                       'chambers1983_gmda',
                       'chambers_hastie1992',
                       'ihaka_gentleman1996'),
 'da-04-estimation-examples.qmd': ('student1908',
                                   'wilson1927',
                                   'wilcoxon1945',
                                   'satterthwaite1946',
                                   'welch1947',
                                   'mann_whitney1947',
                                   'casella_berger2002'),
 'da-05-testing-examples.qmd': ('student1908',
                                'neyman_pearson1933',
                                'welch1947',
                                'casella_berger2002',
                                'lehmann_romano2005'),
 'da-06-anova-examples.qmd': ('fisher1935_doe',
                              'bonferroni1936',
                              'tukey1949',
                              'dunn1961',
                              'casella_berger2002'),
 'da-07-regression-examples.qmd': ('legendre1805',
                                   'gauss1809',
                                   'wherry1931',
                                   'box_cox1964',
                                   'davison2003'),
 'da-08-linear-model-examples.qmd': ('gauss1809',
                                     'box_cox1964',
                                     'hosmer_lemeshow2000',
                                     'venables_ripley2002',
                                     'davison2003'),
 'da-09-chi-square-examples.qmd': ('pearson1900',
                                   'fisher1924_chisq',
                                   'landauer_dunn1930',
                                   'yates1934',
                                   'agresti2002'),
 'final-applied.qmd': ('potthoff_roy1964',
                       'nelder_wedderburn1972',
                       'barbour_brown1974',
                       'laird_ware1982',
                       'hastie_tibshirani1990',
                       'breslow_clayton1993',
                       'debacker1998_toenail',
                       'wood2017'),
 'final-bayesian.qmd': ('bayes1763',
                        'weibull1951',
                        'metropolis1953',
                        'hastings1970',
                        'jeffreys1961',
                        'geman_geman1984',
                        'kass_raftery1995',
                        'gelman_bda2013'),
 'final-preparation.qmd': ('bayes1763',
                           'nelder_wedderburn1972',
                           'laird_ware1982',
                           'hastie_tibshirani1990',
                           'gelman_bda2013'),
 'inf-01-statistical-inference.qmd': ('pearson1900',
                                      'student1908',
                                      'fisher1922',
                                      'fisher1925_smrw',
                                      'snedecor1934',
                                      'casella_berger2002',
                                      'wasserman2004'),
 'inf-02-estimation.qmd': ('gauss1809',
                           'pearson1895',
                           'pearson1896',
                           'student1908_corr',
                           'fisher1922',
                           'fisher1925_est',
                           'wald1949',
                           'wald1950',
                           'casella_berger2002',
                           'lehmann_casella1998'),
 'inf-03-confidence-intervals.qmd': ('student1908',
                                     'wilson1927',
                                     'clopper_pearson1934',
                                     'neyman1937',
                                     'wald1943',
                                     'brown_cai_dasgupta2001',
                                     'casella_berger2002'),
 'inf-04-hypothesis-tests.qmd': ('arbuthnot1710',
                                 'student1908',
                                 'fisher1925_smrw',
                                 'neyman_pearson1928',
                                 'neyman_pearson1933',
                                 'dixon_mood1946',
                                 'casella_berger2002',
                                 'lehmann_romano2005'),
 'inf-05-chi-square.qmd': ('pearson1900',
                           'fisher1922_chisq',
                           'fisher1924_chisq',
                           'landauer_dunn1930',
                           'agresti2002',
                           'casella_berger2002'),
 'inf-06-regression.qmd': ('legendre1805',
                           'gauss1809',
                           'galton1886',
                           'pearson1896',
                           'student1908_corr',
                           'fisher1922',
                           'casella_berger2002',
                           'davison2003'),
 'inf-07-anova.qmd': ('fisher1925_smrw',
                      'snedecor1934',
                      'fisher1935_doe',
                      'tukey1949',
                      'scheffe1959',
                      'casella_berger2002'),
 'inf-08-information-and-bounds.qmd': ('fisher1922',
                                       'fisher1925_est',
                                       'rao1945',
                                       'cramer1946',
                                       'casella_berger2002',
                                       'lehmann_casella1998'),
 'inf-09-rao-blackwell.qmd': ('rao1945',
                              'blackwell1947',
                              'halmos_savage1949',
                              'lehmann_scheffe1950',
                              'casella_berger2002',
                              'lehmann_casella1998'),
 'inf-10-large-sample-estimation.qmd': ('fisher1922',
                                        'fisher1925_est',
                                        'cramer1946',
                                        'wald1949',
                                        'huber1967',
                                        'white1980',
                                        'vandervaart1998',
                                        'casella_berger2002'),
 'inf-11-most-powerful-tests.qmd': ('neyman_pearson1928',
                                    'neyman_pearson1933',
                                    'lehmann_romano2005',
                                    'casella_berger2002'),
 'inf-12-generalised-likelihood-ratio.qmd': ('neyman_pearson1928',
                                             'wilks1938',
                                             'lehmann_romano2005',
                                             'vandervaart1998'),
 'inf-13-exact-tests.qmd': ('yates1934',
                            'fisher1935_doe',
                            'barnard1947',
                            'agresti2002',
                            'lehmann_romano2005'),
 'inf-14-linear-hypotheses.qmd': ('gauss1809',
                                  'fisher1925_smrw',
                                  'scheffe1959',
                                  'casella_berger2002',
                                  'davison2003'),
 'inf-15-two-factor-anova.qmd': ('fisher1925_smrw',
                                 'fisher1935_doe',
                                 'scheffe1959',
                                 'casella_berger2002'),
 'inf-16-predictive-values.qmd': ('bayes1763',
                                  'yerushalmy1947',
                                  'vecchio1966',
                                  'wasserman2004'),
 'prob-01-experiments.qmd': ('huygens1657',
                             'bernoulli1713',
                             'bayes1763',
                             'laplace1812',
                             'kolmogorov1933_slln',
                             'vonmises1939',
                             'selvin1975',
                             'feller1968',
                             'grimmett_stirzaker2020',
                             'ross2019'),
 'prob-02-random-variables.qmd': ('bernoulli1713',
                                  'demoivre1756',
                                  'gauss1809',
                                  'laplace1812',
                                  'poisson1837',
                                  'pearson1895',
                                  'kolmogorov1933_slln',
                                  'feller1968',
                                  'grimmett_stirzaker2020',
                                  'ross2019'),
 'prob-03-simulation.qmd': ('metropolis_ulam1949',
                            'lehmer1951',
                            'vonneumann1951',
                            'box_muller1958',
                            'hull_dobell1962',
                            'ross2019',
                            'robert_casella2004'),
 'prob-04-joint-distributions.qmd': ('gauss1809',
                                     'schwarz1885',
                                     'pearson1896',
                                     'kolmogorov1933_slln',
                                     'feller1968',
                                     'grimmett_stirzaker2020',
                                     'casella_berger2002'),
 'prob-05-transforms-and-limits.qmd': ('bernoulli1713',
                                       'demoivre1756',
                                       'gauss1809',
                                       'laplace1812',
                                       'chebyshev1867',
                                       'lindeberg1922',
                                       'kolmogorov1933_slln',
                                       'grimmett_stirzaker2020',
                                       'durrett2019'),
 'prob-06-markov-chains.qmd': ('markov1906',
                               'chapman1928',
                               'kolmogorov1931',
                               'feller1968',
                               'norris1997',
                               'grimmett_stirzaker2020',
                               'ross2019'),
 'prob-07-reliability.qmd': ('fubini1907',
                             'weibull1951',
                             'kaplan_meier1958',
                             'birnbaum1961',
                             'barlow_proschan1975',
                             'ross2019'),
 'sl-01-multivariate-normal.qmd': ('gauss1809',
                                   'pearson1896',
                                   'yule1907_pcorr',
                                   'fisher1936',
                                   'anderson1936_iris',
                                   'mahalanobis1936',
                                   'anderson2003_mva',
                                   'golub_vanloan2013'),
 'sl-02-normal-inference.qmd': ('wishart1928',
                                'hotelling1931',
                                'fisher1936',
                                'anderson1936_iris',
                                'welch1947',
                                'anderson2003_mva',
                                'golub_vanloan2013'),
 'sl-03-principal-components.qmd': ('pearson1901_pca',
                                    'spearman1904',
                                    'hotelling1933_pca',
                                    'fisher1936',
                                    'eckart_young1936',
                                    'cattell1966',
                                    'lee_seung1999',
                                    'anderson2003_mva',
                                    'hastie_esl2009'),
 'sl-04-kmeans.qmd': ('voronoi1908',
                      'fisher1936',
                      'macqueen1967',
                      'hartigan_wong1979',
                      'lloyd1982',
                      'hubert_arabie1985',
                      'tibshirani_gap2001',
                      'hastie_esl2009',
                      'james_islr2021'),
 'sl-05-mixtures-em.qmd': ('fisher1936',
                           'teicher1963',
                           'dempster_laird_rubin1977',
                           'wu1983',
                           'mclachlan_peel2000_book',
                           'peel_mclachlan2000_t',
                           'stephens2000',
                           'lange2013_opt',
                           'bishop2006'),
 'sl-06-model-selection.qmd': ('kullback_leibler1951',
                               'akaike1974',
                               'schwarz1978',
                               'kass_raftery1995',
                               'smyth2000',
                               'fraley_raftery2002',
                               'drton_plummer2017',
                               'cawley_talbot2010',
                               'hastie_esl2009'),
 'sl-07-linkage-and-density.qmd': ('sorensen1948',
                                   'rosenblatt1956',
                                   'sneath1957',
                                   'sokal_michener1958',
                                   'parzen1962',
                                   'ward1963',
                                   'epanechnikov1969',
                                   'silverman1986',
                                   'sheather_jones1991',
                                   'murtagh_legendre2014',
                                   'hastie_esl2009'),
 'sl-08-discriminant-analysis.qmd': ('fisher1936',
                                     'anderson1936_iris',
                                     'smith1947_qda',
                                     'wald1950',
                                     'hastie_tibshirani1996_mda',
                                     'hastie_esl2009',
                                     'fraley_raftery2002',
                                     'bishop2006'),
 'sl-09-error-rates.qmd': ('quenouille1949',
                           'quenouille1956',
                           'tukey1958_jackknife',
                           'stone1974',
                           'geisser1975',
                           'efron1979',
                           'efron1981',
                           'efron1983',
                           'cawley_talbot2010',
                           'davison_hinkley1997',
                           'hastie_esl2009'),
 'sl-10-logistic-regression.qmd': ('berkson1944',
                                   'brier1950',
                                   'cox1958_logistic',
                                   'nelder_wedderburn1972',
                                   'albert_anderson1984',
                                   'chicco_jurman2020',
                                   'mccullagh_nelder1989',
                                   'hastie_esl2009'),
 'sl-11-nearest-neighbours.qmd': ('cover_hart1967',
                                  'stone1977_knn',
                                  'olshen1977',
                                  'devroye1978',
                                  'fix_hodges1989',
                                  'hastie_esl2009'),
 'sl-12-classification-trees.qmd': ('gini1912',
                                    'shannon1948',
                                    'breiman_cart1984',
                                    'quinlan1993',
                                    'hastie_esl2009',
                                    'james_islr2021'),
 'sl-13-ensembles.qmd': ('schapire1990',
                         'freund_schapire1995',
                         'breiman1996_bagging',
                         'freund_schapire1997',
                         'ho1998_subspace',
                         'friedman_hastie_tibshirani2000',
                         'breiman2001_rf',
                         'friedman2001_gbm',
                         'strobl2007',
                         'krogh_vedelsby1995',
                         'hastie_esl2009'),
 'sl-14-neural-units.qmd': ('mcculloch_pitts1943',
                            'rosenblatt1958',
                            'widrow_hoff1960',
                            'minsky_papert1969',
                            'rumelhart_hinton_williams1986',
                            'cybenko1989',
                            'hornik1989',
                            'werbos1994',
                            'lecun1998',
                            'hinton_osindero_teh2006',
                            'williams1994_tsetse',
                            'ripley1996',
                            'bishop2006'),
 'sl-15-backpropagation.qmd': ('widrow_hoff1960',
                               'rumelhart_hinton_williams1986',
                               'werbos1994',
                               'hastie_esl2009',
                               'bishop2006',
                               'ripley1996'),
 'sl-16-networks-in-practice.qmd': ('robbins_monro1951',
                                    'hoerl_kennard1970',
                                    'sejnowski_rosenberg1986',
                                    'sejnowski_rosenberg1987',
                                    'pomerleau1989',
                                    'bridle1990',
                                    'krogh_hertz1992',
                                    'lecun1998',
                                    'hinton_osindero_teh2006',
                                    'glorot_bengio2010',
                                    'cawley_talbot2010',
                                    'bishop2006',
                                    'hastie_esl2009'),
 'sl-17-support-vectors.qmd': ('mercer1909',
                               'boser_guyon_vapnik1992',
                               'cortes_vapnik1995',
                               'vapnik1995',
                               'vapnik1998',
                               'platt1999_smo',
                               'burges1998',
                               'scholkopf_smola_muller1999',
                               'scholkopf_smola2002',
                               'hastie_esl2009'),
 'sl-18-high-dimensional.qmd': ('dempster1958',
                                'hoerl_kennard1970',
                                'donoho_johnstone1994',
                                'breiman1995_garrote',
                                'benjamini_hochberg1995',
                                'tibshirani1996',
                                'alon1999',
                                'benjamini_yekutieli2001',
                                'zou2006',
                                'friedman_glmnet2010',
                                'frank_friedman1993',
                                'hastie_esl2009',
                                'james_islr2021'),
 'sl-19-graphical-models.qmd': ('dempster1972_cov',
                                'besag1974',
                                'speed_kiiveri1986',
                                'clifford1990_hc',
                                'lauritzen1996',
                                'alon1999',
                                'meinshausen_buhlmann2006',
                                'friedman_glasso2008',
                                'foygel_drton2010'),
 'sp-01-stochastic-processes.qmd': ('chebyshev1867',
                                    'markov1906',
                                    'kolmogorov1933_slln',
                                    'doob1953',
                                    'grimmett_stirzaker2020',
                                    'durrett2019'),
 'sp-02-branching.qmd': ('watson_galton1875',
                         'feller1968',
                         'grimmett_stirzaker2020',
                         'ross2019'),
 'sp-03-random-walks.qmd': ('huygens1657',
                            'bernoulli1713',
                            'demoivre1756',
                            'feller1968',
                            'grimmett_stirzaker2020',
                            'ross2019'),
 'sp-04-discrete-markov.qmd': ('markov1906',
                               'chapman1928',
                               'birkhoff1946',
                               'feller1968',
                               'norris1997',
                               'grimmett_stirzaker2020'),
 'sp-05-classes-and-reversibility.qmd': ('markov1906',
                                         'kolmogorov1931',
                                         'kelly1979',
                                         'norris1997',
                                         'kolmogorov1936',
                                         'grimmett_stirzaker2020'),
 'sp-06-poisson-processes.qmd': ('erlang1909',
                                 'doob1953',
                                 'kingman1993',
                                 'ross2019',
                                 'grimmett_stirzaker2020'),
 'sp-07-continuous-markov.qmd': ('chapman1928',
                                 'kolmogorov1931',
                                 'jensen1953',
                                 'doob1953',
                                 'norris1997',
                                 'ross2019',
                                 'grimmett_stirzaker2020'),
 'sp-08-queues.qmd': ('erlang1909',
                      'erlang1917',
                      'kendall1953',
                      'little1961',
                      'kelly1979',
                      'wolff1982_pasta',
                      'ross2019'),
 'sp-09-probability-spaces.qmd': ('borel1909',
                                  'cantelli1917',
                                  'kolmogorov1933_slln',
                                  'billingsley1995',
                                  'durrett2019'),
 'sp-10-random-variables.qmd': ('lebesgue1902',
                                'kolmogorov1933_slln',
                                'doob1953',
                                'billingsley1995',
                                'durrett2019'),
 'sp-11-convergence.qmd': ('chebyshev1867',
                           'lebesgue1902',
                           'fatou1906',
                           'jensen1906',
                           'levy1925',
                           'kolmogorov1933_slln',
                           'doob1953',
                           'levy1937',
                           'billingsley1995',
                           'durrett2019'),
 'sp-12-extremes.qmd': ('frechet1927',
                        'fisher_tippett1928',
                        'gnedenko1943',
                        'weibull1951',
                        'gumbel1958',
                        'pareto1909',
                        'coles2001'),
 'ur-01-exploratory-data-analysis.qmd': ('bickel1975_ucb',
                                         'rubin1976_missing',
                                         'tukey1977',
                                         'chambers1983_gmda',
                                         'wickham2014_tidy',
                                         'wickham2016_ggplot2'),
 'ur-02-probability-and-simulation.qmd': ('kolmogorov1933_ks',
                                          'fisher1935_doe',
                                          'beall1942_sprays',
                                          'smirnov1948',
                                          'rosenblatt1956',
                                          'parzen1962',
                                          'phipson_smyth2010',
                                          'davison_hinkley1997'),
 'ur-03-bootstrap-and-numerical.qmd': ('brent1973',
                                       'efron1979',
                                       'chambers1983_gmda',
                                       'davison_hinkley1997'),
 'ur-04-mixtures-and-clustering.qmd': ('fisher1936',
                                       'anderson1936_iris',
                                       'dempster_laird_rubin1977',
                                       'hubert_arabie1985',
                                       'azzalini_bowman1990',
                                       'mclachlan_peel2000_book',
                                       'mclachlan_peel_bean2003',
                                       'baek_mclachlan_flack2010',
                                       'scrucca2016_mclust'),
 'ur-05-bayesian-computation.qmd': ('bayes1763',
                                    'cushny_peebles1905',
                                    'student1908',
                                    'metropolis1953',
                                    'hastings1970',
                                    'bickel1975_ucb',
                                    'geman_geman1984',
                                    'kass_raftery1995',
                                    'gelman_bda2013',
                                    'robert_casella2004'),
 'ur-06-model-objects.qmd': ('wilkinson_rogers1973',
                             'chambers1983_gmda',
                             'chambers_hastie1992',
                             'davison2003',
                             'venables_ripley2002'),
 'ur-07-glms-in-r.qmd': ('beall1942_sprays',
                         'nelder_wedderburn1972',
                         'wedderburn1974',
                         'bickel1975_ucb',
                         'madsen1976_housing',
                         'mccullagh1980',
                         'mccullagh_nelder1989',
                         'venables_ripley2002',
                         'davison2003'),
 'ur-08-additive-models.qmd': ('chambers1983_gmda',
                               'hastie_tibshirani1986',
                               'hastie_tibshirani1990',
                               'wood2011',
                               'wood2017'),
 'ur-09-repeated-measures.qmd': ('potthoff_roy1964',
                                 'patterson_thompson1971',
                                 'laird_ware1982',
                                 'liang_zeger1986',
                                 'hojsgaard2006_geepack',
                                 'bates_lme4_2015'),
 'ur-10-time-series.qmd': ('box_jenkins1970',
                           'ljung_box1978',
                           'hyndman_khandakar2008',
                           'hyndman_athanasopoulos2021'),
 'ur-11-checking-a-fit.qmd': ('potthoff_roy1964',
                              'bickel1975_ucb',
                              'tukey1977',
                              'chambers1983_gmda',
                              'gelman_bda2013')}

ARTICLE_GROUPS: list[tuple[tuple[str, ...], tuple[str, ...]]] = [(('axioms-of-probability',
   'probability-measure',
   'properties-of-a-probability',
   'sample-space',
   'event'),
  ('kolmogorov1933_slln', 'feller1968', 'grimmett_stirzaker2020')),
 (('equally-likely-outcomes', 'four-ways-of-counting-draws'),
  ('huygens1657', 'bernoulli1713', 'laplace1812', 'feller1968')),
 (('conditional-probability', 'product-rule', 'law-of-total-probability'),
  ('bayes1763', 'laplace1812', 'kolmogorov1933_slln', 'grimmett_stirzaker2020')),
 (('independent-events',), ('bernoulli1713', 'kolmogorov1933_slln', 'feller1968')),
 (('birthday-problem',), ('vonmises1939', 'feller1968')),
 (('monty-hall-problem',), ('selvin1975',)),
 (('random-variable', 'discrete-distribution'),
  ('kolmogorov1933_slln', 'feller1968', 'grimmett_stirzaker2020')),
 (('cumulative-distribution-function',),
  ('kolmogorov1933_slln', 'kolmogorov1933_ks', 'feller1968')),
 (('continuous-distribution',), ('laplace1812', 'kolmogorov1933_slln', 'feller1968')),
 (('expectation', 'expectation-of-a-function'),
  ('huygens1657', 'bernoulli1713', 'kolmogorov1933_slln', 'grimmett_stirzaker2020')),
 (('variance',),
  ('demoivre1756', 'gauss1809', 'fisher1925_smrw', 'casella_berger2002')),
 (('probability-generating-function', 'moment-generating-function'),
  ('demoivre1756', 'laplace1812', 'feller1968')),
 (('bernoulli-distribution', 'binomial-distribution'),
  ('bernoulli1713', 'demoivre1756', 'feller1968')),
 (('geometric-distribution',), ('bernoulli1713', 'feller1968')),
 (('poisson-distribution', 'poisson-limit-of-the-binomial'),
  ('poisson1837', 'feller1968')),
 (('hypergeometric-distribution',), ('bernoulli1713', 'feller1968', 'forbes2011')),
 (('uniform-distribution',), ('laplace1812', 'feller1968')),
 (('exponential-distribution', 'memoryless-property'),
  ('erlang1909', 'feller1968', 'ross2019')),
 (('normal-distribution',),
  ('demoivre1756',
   'gauss1809',
   'laplace1812',
   'feller1968',
   'forbes2011',
   'gelman_bda2013')),
 (('gamma-distribution',), ('laplace1812', 'pearson1895', 'feller1968', 'forbes2011')),
 (('multinomial-distribution',), ('bernoulli1713', 'pearson1900', 'feller1968')),
 (('linear-congruential-generator', 'random-seed'),
  ('lehmer1951', 'metropolis_ulam1949', 'hull_dobell1962', 'robert_casella2004')),
 (('inverse-transform-method', 'draws-from-the-usual-families'),
  ('vonneumann1951', 'box_muller1958')),
 (('acceptance-rejection-method',), ('vonneumann1951', 'metropolis_ulam1949')),
 (('box-muller-method',), ('box_muller1958', 'robert_casella2004')),
 (('cauchy-distribution',), ('feller1968', 'grimmett_stirzaker2020')),
 (('joint-probability-mass-function', 'independent-random-variables'),
  ('bernoulli1713', 'kolmogorov1933_slln', 'feller1968')),
 (('joint-probability-density', 'conditional-distribution'),
  ('laplace1812', 'kolmogorov1933_slln', 'feller1968')),
 (('covariance', 'expectation-vector-and-covariance-matrix'),
  ('galton1886', 'pearson1896', 'anderson2003_mva')),
 (('cauchy-schwarz-inequality',), ('schwarz1885', 'grimmett_stirzaker2020')),
 (('conditional-expectation', 'tower-property'),
  ('kolmogorov1933_slln', 'doob1953', 'grimmett_stirzaker2020', 'durrett2019')),
 (('transformation-rule',
   'jacobian',
   'distribution-of-a-function-or-a-sum',
   'convolution'),
  ('laplace1812', 'feller1968', 'cramer1946', 'casella_berger2002')),
 (('multivariate-normal-distribution', 'affine-images-of-normal-vectors'),
  ('gauss1809', 'pearson1896', 'anderson2003_mva')),
 (('normal-linear-model',), ('legendre1805', 'gauss1809', 'fisher1925_smrw')),
 (('law-of-large-numbers',),
  ('bernoulli1713',
   'chebyshev1867',
   'kolmogorov1933_slln',
   'grimmett_stirzaker2020',
   'durrett2019')),
 (('central-limit-theorem', 'limit-theorems'),
  ('demoivre1756',
   'laplace1812',
   'lindeberg1922',
   'feller1968',
   'grimmett_stirzaker2020',
   'durrett2019')),
 (('markov-property', 'finite-state-markov-chain', 'limiting-distribution'),
  ('markov1906', 'feller1968', 'norris1997')),
 (('chapman-kolmogorov-equations',),
  ('chapman1928', 'kolmogorov1931', 'norris1997', 'grimmett_stirzaker2020')),
 (('structure-function', 'reliability-function'),
  ('birnbaum1961', 'barlow_proschan1975')),
 (('survival-function', 'hazard-rate'),
  ('weibull1951', 'kaplan_meier1958', 'cox1972', 'barlow_proschan1975')),
 (('weibull-distribution',), ('frechet1927', 'weibull1951', 'forbes2011', 'ross2019')),
 (('fubini-s-theorem',), ('fubini1907', 'lebesgue1902', 'billingsley1995')),
 (('stochastic-process', 'state-space', 'stationary-and-independent-increments'),
  ('kolmogorov1931',
   'kolmogorov1933_slln',
   'doob1953',
   'durrett2019',
   'grimmett_stirzaker2020')),
 (('chebyshev-s-inequality', 'markov-s-inequality'),
  ('chebyshev1867', 'grimmett_stirzaker2020', 'durrett2019')),
 (('galton-watson-process',
   'offspring-probability-generating-function',
   'extinction-criterion',
   'extinction-probability'),
  ('watson_galton1875', 'feller1968', 'grimmett_stirzaker2020', 'ross2019')),
 (('gambler-s-ruin',
   'expected-duration-of-a-random-walk',
   'drift-and-scale-of-a-random-walk',
   'first-passage-time'),
  ('huygens1657',
   'bernoulli1713',
   'demoivre1756',
   'feller1968',
   'grimmett_stirzaker2020',
   'ross2019')),
 (('discrete-time-markov-chain',
   'transition-matrix',
   'stationary-distribution',
   'hitting-probabilities'),
  ('markov1906', 'feller1968', 'norris1997')),
 (('doubly-stochastic-matrix',), ('birkhoff1946', 'feller1968')),
 (('communicating-classes',
   'irreducible-markov-chain',
   'aperiodic-markov-chain',
   'recurrence-and-period',
   'transient-and-recurrent-states',
   'finite-irreducible-chains'),
  ('markov1906', 'kolmogorov1931', 'feller1968', 'norris1997')),
 (('detailed-balance', 'global-balance-and-detailed-balance'),
  ('kolmogorov1931', 'kelly1979', 'norris1997', 'kolmogorov1936')),
 (('homogeneous-poisson-process',
   'forward-equations-of-the-poisson-process',
   'interarrival-time',
   'nonhomogeneous-poisson-process',
   'intensity-function',
   'superposition-and-thinning',
   'spatial-poisson-process'),
  ('erlang1909', 'doob1953', 'kingman1993', 'ross2019')),
 (('generator',
   'holding-time',
   'jump-chain',
   'kolmogorov-forward-and-backward-equations',
   'two-state-continuous-time-chain'),
  ('chapman1928', 'kolmogorov1931', 'doob1953', 'norris1997', 'ross2019')),
 (('uniformisation',), ('jensen1953', 'norris1997')),
 (('birth-death-balance',
   'local-balance',
   'm-m-1-queue',
   'm-m-queue',
   'multi-server-and-finite-capacity-queues',
   'blocking-probability',
   'machine-repair-model'),
  ('erlang1909',
   'erlang1917',
   'kendall1953',
   'kelly1979',
   'wolff1982_pasta',
   'ross2019')),
 (('throughput',),
  ('erlang1909',
   'erlang1917',
   'kendall1953',
   'little1961',
   'kelly1979',
   'wolff1982_pasta',
   'ross2019')),
 (('little-s-law',), ('little1961', 'ross2019')),
 (('probability-space',
   'sigma-algebra',
   'generated-and-borel-sigma-algebras',
   'countable-additivity',
   'limits-of-sequences-of-events'),
  ('borel1909',
   'lebesgue1902',
   'kolmogorov1933_slln',
   'billingsley1995',
   'durrett2019')),
 (('borel-cantelli-lemmas',),
  ('borel1909',
   'cantelli1917',
   'kolmogorov1933_slln',
   'billingsley1995',
   'durrett2019')),
 (('measurable-random-variable',
   'simple-variables-and-expectation',
   'atom-of-a-distribution',
   'lebesgue-decomposition'),
  ('lebesgue1902',
   'kolmogorov1933_slln',
   'doob1953',
   'billingsley1995',
   'durrett2019')),
 (('kolmogorov-extension-theorem',),
  ('kolmogorov1933_slln', 'doob1953', 'billingsley1995', 'durrett2019')),
 (('monotone-convergence-fatou-and-dominated-convergence',),
  ('lebesgue1902', 'fatou1906', 'billingsley1995', 'durrett2019')),
 (('jensen-s-inequality',), ('jensen1906', 'billingsley1995', 'casella_berger2002')),
 (('characteristic-functions', 'levy-s-continuity-theorem'),
  ('levy1925', 'feller1968', 'levy1937', 'durrett2019')),
 (('modes-of-convergence', 'uniform-integrability'),
  ('kolmogorov1933_slln', 'doob1953', 'billingsley1995', 'durrett2019')),
 (('strong-law',),
  ('borel1909',
   'cantelli1917',
   'kolmogorov1933_slln',
   'billingsley1995',
   'durrett2019')),
 (('extreme-value-classification', 'exponential-tails-and-the-gumbel-law'),
  ('fisher_tippett1928', 'gnedenko1943', 'gumbel1958', 'coles2001')),
 (('power-law-tails-and-the-frechet-law',),
  ('frechet1927', 'fisher_tippett1928', 'gnedenko1943', 'coles2001')),
 (('a-finite-endpoint-and-a-weibull-extreme-value-law',),
  ('fisher_tippett1928', 'gnedenko1943', 'weibull1951', 'coles2001')),
 (('pareto-distribution',), ('pareto1909', 'gnedenko1943', 'coles2001', 'forbes2011')),
 (('random-sample',
   'statistic',
   'moments-of-the-sample-mean-and-variance',
   'milk-carton-example'),
  ('student1908', 'fisher1922', 'fisher1925_smrw', 'casella_berger2002')),
 (('chi-squared-distribution', 'degrees-of-freedom'),
  ('pearson1900',
   'fisher1922_chisq',
   'fisher1924_chisq',
   'casella_berger2002',
   'forbes2011')),
 (('student-t-distribution', 'normal-sample-theorem'),
  ('student1908', 'fisher1925_smrw', 'casella_berger2002')),
 (('f-distribution',), ('fisher1925_smrw', 'snedecor1934', 'casella_berger2002')),
 (('estimator', 'bias-of-an-estimator', 'unbiased-estimator', 'mean-squared-error'),
  ('gauss1809',
   'fisher1922',
   'cramer1946',
   'casella_berger2002',
   'lehmann_casella1998')),
 (('method-of-moments',), ('pearson1895', 'fisher1922', 'casella_berger2002')),
 (('sample-correlation-coefficient',),
  ('galton1886', 'pearson1896', 'student1908_corr')),
 (('likelihood-function',
   'maximum-likelihood',
   'maximum-likelihood-for-a-binomial-proportion',
   'maximum-likelihood-for-a-normal-sample',
   'nuisance-parameters'),
  ('fisher1922', 'fisher1925_est', 'casella_berger2002', 'davison2003')),
 (('invariance-of-maximum-likelihood',),
  ('fisher1922', 'fisher1925_est', 'anderson2003_mva')),
 (('consistent-estimator',),
  ('fisher1922', 'wald1949', 'casella_berger2002', 'vandervaart1998')),
 (('loss-and-risk',), ('wald1950', 'lehmann_casella1998', 'casella_berger2002')),
 (('median-unbiased-estimators',), ('fisher1925_est', 'cramer1946')),
 (('cramer-rao-lower-bound',),
  ('fisher1922', 'rao1945', 'cramer1946', 'lehmann_casella1998', 'casella_berger2002')),
 (('rao-blackwell-theorem', 'uniformly-minimum-variance-unbiased-estimator'),
  ('rao1945',
   'blackwell1947',
   'lehmann_scheffe1950',
   'lehmann_casella1998',
   'casella_berger2002')),
 (('asymptotic-normality-of-maximum-likelihood', 'asymptotic-relative-efficiency'),
  ('fisher1922',
   'fisher1925_est',
   'cramer1946',
   'wald1949',
   'vandervaart1998',
   'lehmann_casella1998')),
 (('delta-method',), ('cramer1946', 'vandervaart1998', 'casella_berger2002')),
 (('maximum-likelihood-under-the-wrong-model',),
  ('huber1967', 'white1980', 'vandervaart1998', 'davison2003')),
 (('confidence-interval',
   'coverage',
   'pivot',
   'standard-error',
   'sample-size-for-a-confidence-interval'),
  ('neyman1937', 'casella_berger2002')),
 (('one-sample-t-pivot',
   'two-sample-t-pivot',
   'pooled-variance',
   'interval-for-a-difference-of-means'),
  ('student1908', 'fisher1925_smrw', 'neyman1937', 'casella_berger2002')),
 (('interval-for-a-normal-variance',),
  ('pearson1900', 'fisher1925_smrw', 'neyman1937')),
 (('variance-ratio-f-pivot', 'interval-for-a-ratio-of-variances'),
  ('fisher1925_smrw', 'snedecor1934', 'neyman1937')),
 (('wald-interval', 'interval-for-a-proportion'),
  ('wilson1927', 'clopper_pearson1934', 'wald1943', 'brown_cai_dasgupta2001')),
 (('null-and-alternative-hypotheses',
   'critical-region',
   'type-i-and-type-ii-errors',
   'neyman-pearson-approach',
   'power-function',
   'significance-level',
   'ingredients-of-a-hypothesis-test',
   'tests-and-confidence-intervals'),
  ('neyman_pearson1928',
   'neyman_pearson1933',
   'neyman1937',
   'lehmann_romano2005',
   'casella_berger2002')),
 (('p-value',),
  ('pearson1900', 'fisher1925_smrw', 'casella_berger2002', 'lehmann_romano2005')),
 (('one-sample-t-test', 'two-sample-t-test', 'paired-samples'),
  ('cushny_peebles1905', 'student1908', 'fisher1925_smrw')),
 (('chi-squared-test-for-a-variance',), ('pearson1900', 'fisher1925_smrw')),
 (('f-test-for-equal-variances',),
  ('fisher1925_smrw', 'snedecor1934', 'box1953', 'casella_berger2002')),
 (('binomial-test', 'test-for-one-proportion', 'two-proportion-z-test'),
  ('clopper_pearson1934', 'wald1943', 'agresti2002', 'casella_berger2002')),
 (('sign-test',), ('arbuthnot1710', 'dixon_mood1946')),
 (('neyman-pearson-lemma', 'uniformly-most-powerful-test'),
  ('neyman_pearson1933', 'lehmann_romano2005', 'casella_berger2002')),
 (('uniformly-most-powerful-unbiased-test',),
  ('neyman_pearson1933', 'lehmann_romano2005')),
 (('generalised-likelihood-ratio-test', 'wilks-theorem'),
  ('neyman_pearson1928', 'wilks1938', 'lehmann_romano2005', 'vandervaart1998')),
 (('pearson-statistic',
   'pearson-chi-squared-approximation',
   'chi-squared-test-with-known-cell-probabilities',
   'observed-and-expected-counts'),
  ('pearson1900', 'fisher1922_chisq', 'agresti2002')),
 (('pearson-test-with-estimated-parameters',
   'chi-squared-test-with-estimated-parameters',
   'contingency-tables',
   'chi-squared-test-of-independence'),
  ('pearson1900', 'fisher1922_chisq', 'fisher1924_chisq', 'agresti2002')),
 (('fisher-s-exact-test', 'homogeneity-and-independence'),
  ('yates1934', 'fisher1935_doe', 'barnard1947', 'agresti2002', 'lehmann_romano2005')),
 (('regression-effect',), ('galton1886', 'pearson1896')),
 (('least-squares',
   'least-squares-line',
   'least-squares-estimators-are-unbiased',
   'simple-linear-regression',
   'regression-slope',
   'explanatory-variable',
   'response-variable'),
  ('legendre1805', 'gauss1809', 'galton1886', 'fisher1925_smrw', 'davison2003')),
 (('sampling-distribution-of-the-regression-estimators',
   'slope-t-pivot',
   'prediction-interval',
   'coefficient-of-determination'),
  ('gauss1809', 'fisher1922', 'fisher1925_smrw', 'davison2003', 'casella_berger2002')),
 (('one-way-analysis-of-variance',
   'one-factor-analysis-of-variance',
   'anova-sum-of-squares-decomposition',
   'anova-f-distribution'),
  ('fisher1925_smrw', 'snedecor1934', 'scheffe1959', 'casella_berger2002')),
 (('contrast', 'multiple-comparisons', 'tukey-intervals'),
  ('tukey1949', 'scheffe1959')),
 (('randomised-block-design', 'blocks-in-analysis-of-variance'),
  ('fisher1925_smrw', 'fisher1935_doe')),
 (('general-linear-hypothesis',), ('gauss1809', 'fisher1925_smrw', 'scheffe1959')),
 (('two-factor-analysis-of-variance', 'sum-to-zero-and-contrast-constraints'),
  ('fisher1925_smrw', 'fisher1935_doe', 'scheffe1959')),
 (('positive-predictive-value',
   'negative-predictive-value',
   'fallacy-of-the-transposed-conditional'),
  ('bayes1763', 'yerushalmy1947', 'vecchio1966')),
 (('observational-study', 'confounding-variable', 'sampling-bias'),
  ('neyman1934', 'simpson1951', 'cochran1977')),
 (('designed-experiment', 'treatment'), ('fisher1935_doe', 'box_hunter_hunter2005')),
 (('randomised-controlled-trial', 'blinding-and-placebo'),
  ('fisher1935_doe', 'hill1948_rct')),
 (('simple-random-sample', 'stratified-and-cluster-sampling'),
  ('neyman1934', 'cochran1977')),
 (('measurement-error',), ('gauss1809', 'laplace1812', 'fuller1987')),
 (('summary-statistics',
   'median',
   'sample-quantile',
   'interquartile-range',
   'range',
   'sample-variance-and-standard-deviation',
   'outlier'),
  ('student1908', 'fisher1925_smrw', 'tukey1977')),
 (('five-number-summary-and-boxplot', 'exploratory-data-analysis'),
  ('tukey1977', 'chambers1983_gmda')),
 (('histogram', 'skewness'), ('pearson1895', 'tukey1977')),
 (('scatterplot',), ('galton1886', 'chambers1983_gmda')),
 (('normal-quantile-plot',), ('wilk_gnanadesikan1968', 'chambers1983_gmda')),
 (('transformations-of-data',), ('beall1942_sprays', 'box_cox1964', 'tukey1977')),
 (('heart-failure-data',), ('chicco_jurman2020',)),
 (('large-sample-intervals', 'margin-of-error'),
  ('wilson1927', 'neyman1937', 'casella_berger2002', 'vandervaart1998')),
 (('welch-interval',), ('satterthwaite1946', 'welch1947')),
 (('wilcoxon-rank-sum-test',), ('wilcoxon1945', 'mann_whitney1947')),
 (('bonferroni-correction',), ('bonferroni1936', 'dunn1961')),
 (('interaction', 'main-effect'), ('fisher1935_doe', 'scheffe1959')),
 (('multiple-linear-regression',),
  ('legendre1805', 'gauss1809', 'fisher1922', 'davison2003')),
 (('adjusted-r-squared',), ('wherry1931', 'davison2003')),
 (('dummy-variable-coding',), ('wilkinson_rogers1973', 'venables_ripley2002')),
 (('birth-weight-data',), ('hosmer_lemeshow2000', 'venables_ripley2002')),
 (('d-p-q-and-r-functions', 'r-s-distribution-interface'),
  ('chambers_hastie1992', 'ihaka_gentleman1996')),
 (('a-permutation-test',), ('fisher1935_doe', 'phipson_smyth2010')),
 (('nonparametric-bootstrap',), ('efron1979', 'efron1981', 'davison_hinkley1997')),
 (('pearson-dispersion-ratio',), ('wedderburn1974', 'mccullagh_nelder1989')),
 (('exchangeable-correlation',), ('potthoff_roy1964', 'liang_zeger1986')),
 (('bayes-rule',), ('bayes1763', 'laplace1812', 'jeffreys1961', 'gelman_bda2013')),
 (('bayesian-credible-interval',),
  ('laplace1812', 'jeffreys1961', 'box_tiao1973', 'gelman_bda2013')),
 (('credible-region-constructions',),
  ('laplace1812',
   'jeffreys1961',
   'box_tiao1973',
   'gelman_bda2013',
   'darmois1935',
   'pitman1936',
   'koopman1936')),
 (('proper-prior-and-proper-posterior',
   'improper-prior',
   'flat-prior',
   'a-proper-approximation-to-the-flat-prior'),
  ('laplace1812', 'jeffreys1961', 'box_tiao1973', 'berger_bernardo_sun2009')),
 (('uniformity-depends-on-a-domain',),
  ('laplace1812', 'jeffreys1961', 'box_tiao1973', 'berger_bernardo_sun2009', 'gelman_bda2013')),
 (('posterior-point-summaries',
   'posterior-mean',
   'posterior-median',
   'maximum-a-posteriori-estimate'),
  ('laplace1812', 'wald1950', 'raiffa_schlaifer1961', 'lehmann_casella1998', 'gelman_bda2013')),
 (('posterior-summaries-from-draws', 'grid-monte-carlo-approximation'),
  ('metropolis_ulam1949', 'geyer1992', 'gelman_bda2013')),
 (('prior-and-posterior-predictive-distributions', 'predictive-variance-decomposition'),
  ('raiffa_schlaifer1961', 'box_tiao1973', 'gelman_bda2013')),
 (('kernel-of-a-density',), ('raiffa_schlaifer1961', 'gelman_bda2013')),
 (('beta-distribution',
   'beta-binomial-conjugacy',
   'beta-binomial-posterior-prediction'),
  ('bayes1763', 'laplace1812', 'raiffa_schlaifer1961', 'gelman_bda2013', 'forbes2011')),
 (('pseudo-counts-and-sequential-updating',
   'two-pseudo-count-conventions',
   'sequential-coherence',
   'prior-sensitivity'),
  ('bayes1763', 'raiffa_schlaifer1961', 'diaconis_ylvisaker1979', 'diaconis_coin2007')),
 (('conjugacy-is-optional', 'nonconjugate-priors'),
  ('raiffa_schlaifer1961', 'diaconis_ylvisaker1979', 'gelman_bda2013')),
 (('normal-normal-model',
   'normal-normal-conjugacy',
   'precision',
   'precision-weighting'),
  ('gauss1809',
   'laplace1812',
   'raiffa_schlaifer1961',
   'box_tiao1973',
   'gelman_bda2013')),
 (('inverse-gamma-distribution',
   'normal-inverse-gamma-variance-update',
   'full-conditionals-under-independent-priors'),
  ('raiffa_schlaifer1961', 'box_tiao1973', 'gelfand_smith1990', 'gelman_bda2013')),
 (('monte-carlo-method',),
  ('metropolis_ulam1949', 'metropolis1953', 'robert_casella2004', 'gelman_bda2013')),
 (('markov-chain',
   'stationarity-and-detailed-balance',
   'detailed-balance-implies-stationarity',
   'four-state-random-walk'),
  ('markov1906', 'metropolis1953', 'hastings1970', 'norris1997')),
 (('ising-model',), ('ising1925', 'metropolis1953', 'geman_geman1984')),
 (('metropolis-algorithm',),
  ('metropolis1953', 'gubernatis2005', 'hastings1970', 'gelman_bda2013')),
 (('metropolis-hastings-algorithm',
   'metropolis-hastings-update',
   'metropolis-hastings-invariance',
   'hastings-correction',
   'random-walk-and-independent-proposals'),
  ('metropolis1953', 'hastings1970', 'gelman_bda2013', 'robert_casella2004')),
 (('gibbs-sampling', 'systematic-scan-gibbs-sampler', 'full-conditional-distribution'),
  ('geman_geman1984', 'gelfand_smith1990', 'gelman_bda2013', 'robert_casella2004')),
 (('burn-in',
   'warm-up-is-not-a-convergence-proof',
   'effective-sample-size',
   'thinning-a-markov-chain',
   'trace-plot'),
  ('gelman_rubin1992', 'geyer1992', 'gelman_bda2013')),
 (('dirichlet-distribution',
   'dirichlet-moments',
   'interior-dirichlet-mode',
   'the-beta-distribution-is-the-two-category-dirichlet',
   'dirichlet-multinomial-conjugacy',
   'categorical-and-multinomial-models'),
  ('dirichlet1839', 'raiffa_schlaifer1961', 'gelman_bda2013')),
 (('multinomial-central-limit-theorem',),
  ('demoivre1756', 'pearson1900', 'cramer1946')),
 (('marginal-likelihood-and-bayes-factor',
   'bayes-factors-and-posterior-odds',
   'posterior-odds-factorisation',
   'prior-odds',
   'posterior-hypothesis-probability',
   'a-hypothesis-region-is-not-a-separate-model'),
  ('jeffreys1961', 'kass_raftery1995', 'gelman_bda2013')),
 (('bayes-action-for-two-hypotheses',),
  ('wald1950', 'raiffa_schlaifer1961', 'jeffreys1961')),
 (('sufficient-statistic', 'fisher-neyman-factorisation', 'statistic-and-estimator'),
  ('fisher1922',
   'neyman1937',
   'halmos_savage1949',
   'lehmann_casella1998',
   'casella_berger2002')),
 (('minimal-sufficiency', 'complete-statistic'),
  ('lehmann_scheffe1950', 'lehmann_casella1998', 'casella_berger2002')),
 (('lehmann-scheffe-theorem',),
  ('lehmann_scheffe1950', 'rao1945', 'blackwell1947', 'lehmann_casella1998')),
 (('ancillary-statistic', 'basu-s-theorem'),
  ('fisher1925_est', 'basu1955', 'lehmann_casella1998', 'casella_berger2002')),
 (('natural-exponential-family',
   'pitman-koopman-darmois-informal-form',
   'log-partition-moment-identities',
   'translation-to-another-common-notation'),
  ('darmois1935',
   'pitman1936',
   'koopman1936',
   'diaconis_ylvisaker1979',
   'mccullagh_nelder1989',
   'lehmann_casella1998')),
 (('generic-exponential-family-conjugate-update',),
  ('raiffa_schlaifer1961', 'diaconis_ylvisaker1979')),
 (('hierarchical-bayesian-model',
   'hyperparameter',
   'complete-pooling-no-pooling-and-partial-pooling',
   'normal-hierarchical-shrinkage',
   'marginal-hyperposterior',
   'study-rate-full-conditional'),
  ('lindley_smith1972', 'efron_morris1975', 'gelman2006', 'gelman_bda2013')),
 (('exchangeability',), ('definetti1937', 'lindley_smith1972', 'gelman_bda2013')),
 (('empirical-bayes',), ('robbins1956', 'james_stein1961', 'efron_morris1975')),
 (('rat-tumour-data',), ('tarone1982', 'dempster_selwyn_weeks1983', 'gelman_bda2013')),
 (('tg5-cattle-studies',),
  ('lunn_winbugs2000', 'barendse2004_tg5', 'wood_mengersen2006_tg5')),
 (('gaussian-linear-model',
   'ordinary-least-squares',
   'error-and-residual',
   'least-squares-decomposition',
   'sampling-distribution-of-the-ols-estimator',
   'studentised-coefficient-pivot'),
  ('legendre1805', 'gauss1809', 'fisher1925_smrw', 'box_tiao1973')),
 (('likelihood-and-reference-prior',
   'conditional-coefficient-posterior',
   'marginal-variance-posterior',
   'marginal-student-posterior',
   'direct-posterior-simulation',
   'posterior-predictive-target',
   'posterior-prediction-under-the-reference-prior',
   'three-easy-confusions'),
  ('jeffreys1961', 'box_tiao1973', 'berger_bernardo_sun2009', 'gelman_bda2013')),
 (('normal-inverse-gamma-prior', 'normal-inverse-gamma-conjugacy'),
  ('raiffa_schlaifer1961', 'zellner1986', 'gelman_bda2013')),
 (('generalised-linear-model',
   'three-components-of-a-glm',
   'random-component',
   'linear-predictor',
   'link-function',
   'canonical-link',
   'identity-link'),
  ('nelder_wedderburn1972', 'mccullagh_nelder1989', 'davison2003')),
 (('exponential-family',
   'natural-parameter',
   'mean-and-variance-of-an-exponential-family',
   'dispersion-parameter'),
  ('darmois1935',
   'pitman1936',
   'koopman1936',
   'nelder_wedderburn1972',
   'mccullagh_nelder1989')),
 (('fisher-scoring',
   'maximum-likelihood-in-a-glm',
   'fisher-information',
   'score-function'),
  ('fisher1925_est', 'nelder_wedderburn1972', 'mccullagh_nelder1989')),
 (('binary-responses-in-a-glm',
   'logit-link',
   'interpreting-a-logistic-regression',
   'odds',
   'odds-ratio'),
  ('berkson1944',
   'cox1958_logistic',
   'nelder_wedderburn1972',
   'mccullagh_nelder1989',
   'agresti2002')),
 (('probit-link', 'logit-probit-and-complementary-log-log-links'),
  ('bliss1935', 'berkson1944', 'mccullagh_nelder1989')),
 (('complementary-log-log-link',), ('fisher1922', 'cox1972', 'mccullagh_nelder1989')),
 (('clotting-time-data',), ('hurn1945', 'mccullagh_nelder1989', 'huang_rathouz2017')),
 (('cholesterol-and-heart-disease',),
  ('cox1958_logistic', 'mccullagh_nelder1989', 'hosmer_lemeshow2000')),
 (('poisson-regression',
   'count-responses',
   'reading-a-log-linear-coefficient',
   'log-link'),
  ('poisson1837', 'nelder_wedderburn1972', 'mccullagh_nelder1989', 'myers_glm2010')),
 (('quasi-poisson', 'overdispersion'), ('wedderburn1974', 'mccullagh_nelder1989')),
 (('negative-binomial-distribution', 'count-models-beyond-the-poisson'),
  ('greenwood_yule1920',
   'mccullagh_nelder1989',
   'venables_ripley2002',
   'conway_maxwell1962',
   'shmueli2005')),
 (('conway-maxwell-poisson-distribution', 'underdispersion'),
  ('conway_maxwell1962', 'shmueli2005', 'huang2017_cmp')),
 (('mine-injury-data',), ('loader1999_locfit', 'myers_glm2010')),
 (('bids-for-a-bankrupt-firm',), ('cameron_johansson1997', 'huang2017_cmp')),
 (('gamma-regression', 'positive-continuous-responses', 'inverse-link'),
  ('nelder_wedderburn1972', 'mccullagh_nelder1989', 'huang_rathouz2017')),
 (('inverse-gaussian-distribution',),
  ('tweedie1957', 'mccullagh_nelder1989', 'huang_rathouz2017')),
 (('lognormal-distribution',),
  ('mccullagh_nelder1989', 'mcalister1879', 'huang_rathouz2017', 'forbes2011')),
 (('quasi-likelihood', 'quasi-score-and-quasi-likelihood', 'variance-function'),
  ('wedderburn1974', 'mccullagh_nelder1989')),
 (('leaf-blotch-data',), ('wedderburn1974', 'mccullagh_nelder1989')),
 (('ordinal-responses', 'proportional-odds-model'),
  ('ashford1959', 'mccullagh1980', 'yee2015', 'agresti2002')),
 (('proportional-hazards-model',), ('cox1972', 'mccullagh1980')),
 (('nominal-responses', 'baseline-category-logit-model'),
  ('mccullagh_nelder1989', 'tutz2011', 'yee2015', 'agresti2002')),
 (('addiction-data',), ('fahrmeir_tutz2001', 'tutz2011')),
 (('bradley-terry-model', 'paired-comparison'),
  ('bradley_terry1952', 'mccullagh_nelder1989')),
 (('deviance',
   'null-deviance',
   'residual-deviance',
   'scaled-deviance',
   'saturated-model',
   'analysis-of-deviance'),
  ('nelder_wedderburn1972', 'mccullagh_nelder1989', 'myers_glm2010')),
 (('residuals-in-a-glm', 'deviance-residual', 'pearson-residual'),
  ('nelder_wedderburn1972', 'mccullagh_nelder1989', 'dunn_smyth1996')),
 (('roughness-penalty', 'cubic-smoothing-spline', 'spline', 'knot'),
  ('reinsch1967',
   'wahba1990',
   'green_silverman1994',
   'wood2003',
   'wood2017',
   'deboor1978')),
 (('lidar-data',), ('holst1996_lidar', 'ruppert_wand_carroll2003')),
 (('kyphosis-data',), ('breiman_cart1984', 'hastie_tibshirani1990')),
 (('sums-of-smooth-functions', 'effective-degrees-of-freedom'),
  ('hastie_tibshirani1986', 'hastie_tibshirani1990', 'wood2011', 'wood2017')),
 (('partially-linear-model',),
  ('engle1986_plm', 'ruppert_wand_carroll2003', 'wood2017')),
 (('random-intercept-model',
   'linear-mixed-model',
   'fixed-and-random-effects',
   'repeated-measures'),
  ('henderson1975', 'laird_ware1982', 'bates_lme4_2015')),
 (('intraclass-correlation',), ('fisher1925_smrw', 'laird_ware1982')),
 (('restricted-maximum-likelihood',),
  ('patterson_thompson1971', 'laird_ware1982', 'wood2011')),
 (('random-slopes',), ('laird_ware1982', 'self_liang1987', 'bates_lme4_2015')),
 (('sleep-deprivation-data',), ('belenky2003', 'bates_lme4_2015')),
 (('generalised-linear-mixed-model',),
  ('breslow_clayton1993', 'steele_diamond1999', 'bates_lme4_2015')),
 (('marginal-model',
   'generalised-estimating-equations',
   'working-correlation',
   'marginal-and-conditional-effects'),
  ('liang_zeger1986', 'zeger_liang_albert1988')),
 (('sandwich-estimator',), ('huber1967', 'white1980', 'liang_zeger1986')),
 (('warp-breaks-data',), ('tippett1950_warp', 'liang_zeger1986')),
 (('two-responses-one-person',), ('liang_zeger1986', 'song2007_burn')),
 (('vector-response-regression',), ('yee_mitchell1991', 'yee2015')),
 (('time-series',
   'autoregression-and-moving-averages',
   'white-noise',
   'random-walk-with-drift'),
  ('yule1927', 'slutsky1937', 'wold1938', 'box_jenkins1970')),
 (('stationarity-of-a-time-series',
   'weak-stationarity',
   'strict-stationarity',
   'autocorrelation-function'),
  ('khinchin1934', 'wold1938', 'box_jenkins1970', 'brockwell_davis1991')),
 (('variogram',), ('matheron1963', 'brockwell_davis1991')),
 (('gaussian-process',), ('kolmogorov1933_slln', 'doob1953', 'rasmussen_williams2006')),
 (('wold-decomposition',), ('wold1938', 'brockwell_davis1991')),
 (('arima-model',
   'seasonality',
   'trend',
   'cycle',
   'partial-autocorrelation',
   'point-forecast'),
  ('box_jenkins1970',
   'brockwell_davis1991',
   'hyndman_khandakar2008',
   'hyndman_athanasopoulos2021')),
 (('accidental-deaths-data',),
  ('box_jenkins1970', 'brockwell_davis1991', 'makridakis1998')),
 (('unit-root',),
  ('dickey_fuller1979',
   'box_jenkins1970',
   'granger_newbold1974',
   'hyndman_athanasopoulos2021')),
 (('arch-and-garch-models',), ('engle1982', 'bollerslev1986', 'brockwell_davis1991')),
 (('mean-vector-and-covariance-matrix',),
  ('gauss1809', 'galton1886', 'pearson1896', 'anderson2003_mva')),
 (('joint-distribution-and-density',
   'multivariate-normal-distribution-sl-01-multivariate-normal',
   'linear-images-of-a-normal-vector',
   'conditional-distribution-of-a-multivariate-normal'),
  ('gauss1809', 'pearson1896', 'anderson2003_mva')),
 (('correlation',), ('galton1886', 'pearson1896', 'anderson2003_mva')),
 (('partial-correlation',), ('pearson1896', 'yule1907_pcorr', 'anderson2003_mva')),
 (('positive-definite-matrix', 'sylvester-s-criterion'),
  ('golub_vanloan2013', 'anderson2003_mva')),
 (('squared-mahalanobis-distance',), ('mahalanobis1936', 'anderson2003_mva')),
 (('iris-data',), ('anderson1936_iris', 'fisher1936')),
 (('maximum-likelihood-for-a-normal-mean-vector',
   'maximum-likelihood-for-a-covariance-matrix',
   'invariance-of-the-maximum-likelihood-estimator',
   'sampling-law-of-the-normal-mean-and-scatter',
   'pooled-covariance'),
  ('fisher1922', 'wishart1928', 'anderson2003_mva')),
 (('wishart-distribution',), ('wishart1928', 'anderson2003_mva')),
 (('multivariate-central-limit-theorem',),
  ('lindeberg1922', 'cramer1946', 'anderson2003_mva')),
 (('hotelling-s-t2-test',
   'null-distribution-of-hotelling-s',
   'the-limit-of-hotelling-s-statistic',
   'two-sample-hotelling-t2-test',
   'two-sample-hotelling-test',
   'univariate-t-test-as-a-template-for-t2',
   'confidence-region-for-a-normal-mean-vector',
   'simultaneous-confidence-statements'),
  ('hotelling1931', 'anderson2003_mva')),
 (('likelihood-ratio-test',), ('neyman_pearson1928', 'wilks1938', 'hotelling1931')),
 (('behrens-fisher-problem',), ('fisher1935_doe', 'welch1947', 'anderson2003_mva')),
 (('cholesky-decomposition',), ('golub_vanloan2013',)),
 (('principal-component-directions',
   'principal-component-directions-and-scores',
   'loadings',
   'scaling',
   'choosing-the-number-of-principal-components'),
  ('pearson1901_pca', 'hotelling1933_pca', 'anderson2003_mva')),
 (('eigenvalues-and-eigenvectors', 'singular-value-decomposition'),
  ('eckart_young1936', 'golub_vanloan2013')),
 (('scree-plot',), ('cattell1966', 'hotelling1933_pca')),
 (('factor-analysis',), ('spearman1904', 'hotelling1933_pca', 'anderson2003_mva')),
 (('non-negative-matrix-factorisation',), ('lee_seung1999', 'hastie_esl2009')),
 (('k-means-criterion',
   'within-cluster-scatter',
   'lloyd-s-k-means-algorithm',
   'descent-of-lloyd-s-algorithm'),
  ('macqueen1967', 'lloyd1982', 'hastie_esl2009', 'james_islr2021')),
 (('hartigan-wong-algorithm',), ('hartigan_wong1979', 'hastie_esl2009')),
 (('choosing-k-the-gap-statistic', 'why-the-raw-sum-of-squares-cannot-choose'),
  ('tibshirani_gap2001',)),
 (('adjusted-rand-index',), ('hubert_arabie1985',)),
 (('voronoi-tessellation',), ('voronoi1908', 'lloyd1982')),
 (('finite-mixture-model', 'posterior-membership', 'k-means-as-a-limiting-case'),
  ('pearson1895',
   'dempster_laird_rubin1977',
   'mclachlan_peel2000_book',
   'peel_mclachlan2000_t')),
 (('complete-data-likelihood',
   'e-step',
   'm-step',
   'em-algorithm',
   'em-for-a-normal-mixture',
   'monotonicity-of-em'),
  ('dempster_laird_rubin1977',
   'wu1983',
   'mclachlan_peel2000_book',
   'lange2013_opt',
   'kullback_leibler1951')),
 (('gibbs-inequality',),
  ('shannon1948', 'kullback_leibler1951', 'dempster_laird_rubin1977')),
 (('identifiability',), ('teicher1963', 'mclachlan_peel2000_book')),
 (('label-switching',), ('stephens2000', 'mclachlan_peel2000_book')),
 (('missing-data',), ('rubin1976_missing', 'dempster_laird_rubin1977')),
 (('bayesian-information-criterion', 'laplace-approximation'),
  ('laplace1812',
   'schwarz1978',
   'kass_raftery1995',
   'fraley_raftery2002',
   'drton_plummer2017')),
 (('akaike-information-criterion', 'kullback-leibler-divergence'),
  ('kullback_leibler1951', 'akaike1974', 'drton_plummer2017', 'davison2003')),
 (('cross-validation-of-the-likelihood',),
  ('stone1974', 'smyth2000', 'cawley_talbot2010')),
 (('hierarchical-clustering',
   'agglomerative-and-divisive-clustering',
   'dendrogram',
   'single-complete-and-average-linkage',
   'single-linkage',
   'complete-linkage',
   'average-linkage'),
  ('sorensen1948', 'sneath1957', 'sokal_michener1958', 'hastie_esl2009')),
 (('ward-s-method',), ('ward1963', 'murtagh_legendre2014', 'hastie_esl2009')),
 (('kernel-density-estimator', 'gaussian-kernel', 'choosing-the-bandwidth'),
  ('rosenblatt1956', 'parzen1962', 'silverman1986', 'sheather_jones1991')),
 (('epanechnikov-kernel',), ('epanechnikov1969', 'silverman1986')),
 (('training-data-and-classifier',
   'posterior-class-probability',
   'zero-one-loss-and-risk',
   'bayes-classifier',
   'bayes-optimal-rule',
   'classification-with-unequal-costs'),
  ('wald1950', 'hastie_esl2009')),
 (('linear-discriminant-analysis',
   'fisher-s-linear-discriminant-analysis',
   'fisher-s-direction'),
  ('fisher1936', 'anderson2003_mva', 'hastie_esl2009')),
 (('quadratic-discriminant-analysis',), ('smith1947_qda', 'hastie_esl2009')),
 (('mixture-discriminant-analysis',),
  ('hastie_tibshirani1996_mda',
   'mclachlan_peel2000_book',
   'fraley_raftery2002',
   'hastie_esl2009')),
 (('kernel-density-discriminant-analysis',),
  ('parzen1962', 'silverman1986', 'fix_hodges1989')),
 (('fixed-rule-error',
   'apparent-error',
   'a-held-out-test-set',
   'training-set',
   'classification-accuracy'),
  ('stone1974', 'efron1983', 'hastie_esl2009')),
 (('confusion-matrix', 'sensitivity-and-specificity'),
  ('yerushalmy1947', 'hastie_esl2009')),
 (('cross-validation', 'leave-one-out-cross-validation', 'fold-cross-validation'),
  ('stone1974', 'geisser1975', 'cawley_talbot2010', 'hastie_esl2009')),
 (('nested-cross-validation', 'validation-set'), ('stone1974', 'cawley_talbot2010')),
 (('bootstrap', 'bootstrap-error-and-the-correction'),
  ('efron1979', 'efron1981', 'efron1983', 'davison_hinkley1997')),
 (('jackknife', 'jackknife-bias-and-standard-error'),
  ('quenouille1949',
   'quenouille1956',
   'tukey1958_jackknife',
   'efron1981',
   'davison_hinkley1997')),
 (('binary-logistic-regression',
   'interpretation-and-the-decision-boundary',
   'a-finite-stationary-point-is-a-global-maximiser'),
  ('berkson1944',
   'cox1958_logistic',
   'mccullagh_nelder1989',
   'albert_anderson1984',
   'agresti2002')),
 (('iteratively-reweighted-least-squares', 'newton-raphson-method'),
  ('fisher1925_est', 'nelder_wedderburn1972', 'mccullagh_nelder1989')),
 (('multinomial-logistic-regression',),
  ('cox1958_logistic', 'mccullagh_nelder1989', 'hastie_esl2009')),
 (('complete-separation',), ('albert_anderson1984',)),
 (('brier-score',), ('brier1950', 'hastie_esl2009')),
 (('wald-test',), ('wald1943', 'mccullagh_nelder1989', 'casella_berger2002')),
 (('nearest-neighbours', 'cover-hart-bound', 'bayes-consistency-of-nearest-neighbours'),
  ('cover_hart1967', 'stone1977_knn', 'fix_hodges1989', 'hastie_esl2009')),
 (('rank-distance',), ('olshen1977', 'devroye1978')),
 (('decision-tree',
   'regression-tree',
   'node-impurity',
   'tree-size-and-pruning',
   'cost-complexity-pruning',
   'surrogate-split'),
  ('breiman_cart1984', 'hastie_esl2009', 'james_islr2021')),
 (('gini-index',), ('gini1912', 'breiman_cart1984')),
 (('cross-entropy',), ('shannon1948', 'kullback_leibler1951', 'breiman_cart1984')),
 (('ensemble-method', 'squared-error-of-an-average', 'bagging'),
  ('breiman1996_bagging', 'breiman2001_rf', 'krogh_vedelsby1995', 'hastie_esl2009')),
 (('random-forest', 'out-of-bag-estimation-and-variable-importance'),
  ('ho1998_subspace', 'breiman2001_rf', 'hastie_esl2009')),
 (('variable-importance',),
  ('ho1998_subspace', 'breiman2001_rf', 'strobl2007', 'hastie_esl2009')),
 (('boosting',),
  ('schapire1990',
   'freund_schapire1995',
   'freund_schapire1997',
   'friedman_hastie_tibshirani2000',
   'hastie_esl2009')),
 (('adaboost', 'decision-stump', 'the-reweighted-error-is-one-half'),
  ('schapire1990', 'freund_schapire1995', 'freund_schapire1997', 'hastie_esl2009')),
 (('exponential-loss', 'gradient-boosting'),
  ('friedman_hastie_tibshirani2000', 'friedman2001_gbm')),
 (('artificial-neuron', 'neural-unit'),
  ('mcculloch_pitts1943', 'rosenblatt1958', 'bishop2006')),
 (('perceptron', 'perceptron-learning-rule', 'linear-separability'),
  ('rosenblatt1958', 'widrow_hoff1960', 'minsky_papert1969', 'bishop2006')),
 (('xor-problem', 'a-single-threshold-unit-cannot-compute-xor'),
  ('minsky_papert1969', 'rumelhart_hinton_williams1986', 'bishop2006')),
 (('hidden-layer',),
  ('minsky_papert1969',
   'rumelhart_hinton_williams1986',
   'williams1994_tsetse',
   'ripley1996',
   'bishop2006')),
 (('activation-function',
   'sigmoid-function',
   'universal-approximation',
   'one-hidden-layer-approximates-continuous-functions'),
  ('cybenko1989', 'hornik1989', 'bishop2006', 'ripley1996')),
 (('gradient-descent',
   'basic-gradient-descent-learning',
   'learning-rate',
   'delta-rule'),
  ('robbins_monro1951',
   'widrow_hoff1960',
   'rumelhart_hinton_williams1986',
   'bishop2006')),
 (('backpropagation-batch-form',
   'local-minima-plateaus-and-symmetry',
   'squared-error-is-not-the-logistic-likelihood'),
  ('rumelhart_hinton_williams1986', 'werbos1994', 'bridle1990', 'bishop2006')),
 (('weight-initialisation',),
  ('rumelhart_hinton_williams1986', 'lecun1998', 'glorot_bengio2010')),
 (('batch-and-online-learning', 'stochastic-gradient-descent', 'mini-batch', 'epoch'),
  ('robbins_monro1951', 'widrow_hoff1960', 'lecun1998')),
 (('output-coding-softmax-and-cross-entropy',
   'softmax-is-multinomial-logistic-regression',
   'one-hot-encoding'),
  ('shannon1948', 'bridle1990', 'hastie_esl2009')),
 (('regularisation-and-weight-decay',), ('hoerl_kennard1970', 'krogh_hertz1992')),
 (('early-stopping', 'overfitting', 'underfitting'),
  ('krogh_hertz1992', 'hastie_esl2009', 'cawley_talbot2010')),
 (('nettalk',),
  ('sejnowski_rosenberg1986', 'sejnowski_rosenberg1987', 'krogh_hertz1992')),
 (('linear-separators-and-the-margin',
   'distance-to-a-hyperplane',
   'signed-distance',
   'hard-margin-primal',
   'hard-margin-dual',
   'hard-margin-support-vector-machine',
   'support-vectors-and-their-multipliers',
   'dual-problem'),
  ('boser_guyon_vapnik1992',
   'cortes_vapnik1995',
   'vapnik1998',
   'burges1998',
   'hastie_esl2009')),
 (('vapnik-s-radius-margin-bound',), ('vapnik1995', 'vapnik1998', 'burges1998')),
 (('soft-margin-primal', 'soft-margin-slack-variables', 'hinge-loss'),
  ('cortes_vapnik1995', 'vapnik1998', 'hastie_esl2009', 'bishop2006')),
 (('kernel-trick',
   'kernel',
   'which-functions-are-kernels',
   'gram-matrix',
   'polynomial-kernel',
   'radial-basis-function-kernel',
   'kernel-support-vector-machine'),
  ('mercer1909',
   'boser_guyon_vapnik1992',
   'cortes_vapnik1995',
   'platt1999_smo',
   'burges1998',
   'scholkopf_smola2002')),
 (('high-dimensional-data', 'rank-bound', 'regression-when-p-n', 'multicollinearity'),
  ('dempster1958',
   'hoerl_kennard1970',
   'tibshirani1996',
   'alon1999',
   'hastie_esl2009')),
 (('multiple-testing',
   'family-wise-error-rate',
   'family-wise-control-implies-false-discovery-control'),
  ('bonferroni1936', 'benjamini_hochberg1995')),
 (('false-discovery-rate',
   'benjamini-hochberg',
   'benjamini-hochberg-controls-the-false-discovery-rate'),
  ('benjamini_hochberg1995', 'benjamini_yekutieli2001')),
 (('ridge-regression',),
  ('hoerl_kennard1970',
   'tibshirani1996',
   'donoho_johnstone1994',
   'breiman1995_garrote',
   'hastie_esl2009')),
 (('regularisation',),
  ('hoerl_kennard1970', 'tibshirani1996', 'hastie_esl2009', 'james_islr2021')),
 (('lasso',
   'subset-selection-and-shrinkage',
   'sparsity',
   'soft-thresholding-for-orthonormal-predictors'),
  ('donoho_johnstone1994',
   'breiman1995_garrote',
   'tibshirani1996',
   'zou2006',
   'hoerl_kennard1970',
   'frank_friedman1993',
   'hastie_esl2009')),
 (('logistic-lasso',), ('tibshirani1996', 'friedman_glmnet2010')),
 (('alon-colon-cancer-data',), ('alon1999',)),
 (('undirected-graph',
   'clique',
   'separating-set',
   'conditional-independence',
   'markov-graphs',
   'markov-random-field'),
  ('besag1974', 'lauritzen1996')),
 (('markov-properties-and-factorisation', 'hammersley-clifford'),
  ('besag1974', 'clifford1990_hc', 'lauritzen1996')),
 (('gaussian-graphical-models',
   'precision-matrix',
   'a-zero-precision-entry-is-conditional-independence',
   'maximum-likelihood-for-a-known-graph'),
  ('dempster1972_cov', 'speed_kiiveri1986', 'lauritzen1996')),
 (('graphical-lasso',),
  ('meinshausen_buhlmann2006',
   'friedman_glasso2008',
   'foygel_drton2010',
   'hastie_esl2009')),
 (('extended-information-criterion',), ('foygel_drton2010',))]

ARTICLE_REFS: dict[str, tuple[str, ...]] = {
    slug: refs for slugs, refs in ARTICLE_GROUPS for slug in slugs
}

# Keyword fallbacks used only when a brand-new article is introduced on main
# before an explicit entry is added to ARTICLE_GROUPS, so builds never crash.
KEYWORD_FALLBACKS: tuple[tuple[str, tuple[str, ...]], ...] = (('conway-maxwell', ('conway_maxwell1962', 'shmueli2005', 'huang2017_cmp')),
 ('bradley-terry', ('bradley_terry1952', 'mccullagh_nelder1989')),
 ('benjamini-hochberg', ('benjamini_hochberg1995', 'benjamini_yekutieli2001')),
 ('false-discovery', ('benjamini_hochberg1995', 'benjamini_yekutieli2001')),
 ('graphical-lasso', ('meinshausen_buhlmann2006', 'friedman_glasso2008')),
 ('lasso', ('tibshirani1996', 'zou2006')),
 ('ridge', ('hoerl_kennard1970',)),
 ('support-vector', ('boser_guyon_vapnik1992', 'cortes_vapnik1995', 'vapnik1998')),
 ('adaboost',
  ('schapire1990', 'freund_schapire1997', 'friedman_hastie_tibshirani2000')),
 ('random-forest', ('ho1998_subspace', 'breiman2001_rf')),
 ('bagging', ('breiman1996_bagging',)),
 ('backpropagation', ('rumelhart_hinton_williams1986', 'werbos1994')),
 ('perceptron', ('rosenblatt1958', 'minsky_papert1969')),
 ('metropolis', ('metropolis1953', 'hastings1970')),
 ('gibbs', ('geman_geman1984', 'gelfand_smith1990')),
 ('bootstrap', ('efron1979', 'efron1983')),
 ('jackknife', ('quenouille1949', 'quenouille1956', 'tukey1958_jackknife')),
 ('cross-validation', ('stone1974', 'geisser1975', 'cawley_talbot2010')),
 ('em-algorithm', ('dempster_laird_rubin1977', 'wu1983')),
 ('mixture', ('dempster_laird_rubin1977', 'mclachlan_peel2000_book')),
 ('k-means', ('macqueen1967', 'hartigan_wong1979', 'lloyd1982')),
 ('kernel-density', ('rosenblatt1956', 'parzen1962', 'silverman1986')),
 ('principal-component', ('pearson1901_pca', 'hotelling1933_pca')),
 ('hotelling', ('hotelling1931', 'anderson2003_mva')),
 ('wishart', ('wishart1928', 'anderson2003_mva')),
 ('mahalanobis', ('mahalanobis1936', 'anderson2003_mva')),
 ('discriminant', ('fisher1936', 'smith1947_qda')),
 ('nearest-neighbour', ('cover_hart1967', 'fix_hodges1989')),
 ('spline', ('reinsch1967', 'wahba1990', 'green_silverman1994', 'wood2017')),
 ('smooth', ('hastie_tibshirani1990', 'wood2011', 'wood2017')),
 ('quasi-likelihood', ('wedderburn1974', 'mccullagh_nelder1989')),
 ('estimating-equation', ('liang_zeger1986', 'zeger_liang_albert1988')),
 ('mixed-model', ('laird_ware1982', 'breslow_clayton1993', 'bates_lme4_2015')),
 ('wold', ('wold1938',)),
 ('arima', ('box_jenkins1970', 'hyndman_khandakar2008')),
 ('rao-blackwell', ('rao1945', 'blackwell1947', 'lehmann_scheffe1950')),
 ('cramer-rao', ('fisher1922', 'rao1945', 'cramer1946')),
 ('neyman-pearson', ('neyman_pearson1933', 'lehmann_romano2005')),
 ('wilks', ('wilks1938',)),
 ('welch', ('satterthwaite1946', 'welch1947')),
 ('tukey', ('tukey1949', 'tukey1977')),
 ('poisson-process', ('erlang1909', 'kingman1993', 'ross2019')),
 ('queue', ('erlang1909', 'kendall1953', 'little1961')),
 ('branching', ('watson_galton1875', 'feller1968')),
 ('markov', ('markov1906', 'feller1968', 'norris1997')),
 ('bayes', ('bayes1763', 'jeffreys1961', 'gelman_bda2013')))

_AMERICAN_TO_BRITISH = (
    ("generalized", "generalised"),
    ("regularization", "regularisation"),
    ("factorization", "factorisation"),
    ("optimization", "optimisation"),
    ("parameterization", "parameterisation"),
    ("randomized", "randomised"),
    ("neighbors", "neighbours"),
    ("neighbor", "neighbour"),
)

_STATIC_REF_RE = re.compile(r"\n*## References(?:\s*\{#references\})?\n.*\Z", re.S)
_EXISTING_CITE_SUP_RE = re.compile(r'<sup\b[^>]*\bclass="cite-ref"[^>]*>.*?</sup>', re.S)
_CITE_SUP_KEY_RE = re.compile(
    r'<sup\b[^>]*\bdata-cite-key="([a-z0-9_]+)"[^>]*>.*?</sup>',
    re.S,
)
_EXPLICIT_CITE_RE = re.compile(r"\{\{cite:([a-z0-9_,\s]+)\}\}")
_AFTER_CITE_PUNCT_RE = re.compile(r"^[.,;:!?]+")

_PROTECT_PROSE_RE = re.compile(
    r"^\A---\n.*?\n---\n+"  # YAML frontmatter
    r"|```.*?```"  # fenced code or raw html blocks
    r"|`[^`\n]*`"  # inline code
    r"|\$\$.*?\$\$|\$(?:\\.|[^$\\\n])+\$"  # display and inline math
    r"|\\begin\{(?P<env>[a-z*]+)\}.*?\\end\{(?P=env)\}"  # LaTeX math environments
    r"|!?\[(?:[^\[\]\n]|\[[^\]\n]*\])*\]\([^)\n]*\)(?:\{[^}\n]*\})?"  # links & images
    r"|\[[^\]\n]*\]\{[^}\n]*\}"  # bracketed spans
    r"|^#{1,6}\s+[^\n]*$"  # headings
    r"|^:{3,}[^\n]*$"  # Quarto div fences
    r"|\{[#.][^}\n]*\}"  # Quarto attributes
    r"|<[^>\n]+>"  # HTML tags
    r"|https?://\S+"  # bare URLs
    r"|\[\^[^\]\n]+\]",  # footnote markers
    re.S | re.M,
)

# Inline Author (Year) and parenthetical (Author, Year) scanner
_PARTICLE = r"(?:van\s+der|van\s+den|van|von|de\s+la|de|del|della|di|le|la|du|der|den|ten|ter)"
_SURNAME = (
    rf"(?:{_PARTICLE}\s+)?[A-ZÀ-ÖØ-Þ][A-Za-zÀ-ÖØ-öø-ÿ'’\-]*"
    r"(?:-[A-ZÀ-ÖØ-Þ][A-Za-zÀ-ÖØ-öø-ÿ'’\-]*)*"
)
_AUTHOR_SEQ = (
    rf"{_SURNAME}"
    rf"(?:(?:\s*,\s*{_SURNAME})*(?:\s*,?\s*(?:&|and)\s*{_SURNAME})|\s+et\s+al\.)?"
)
_YEAR_TOKEN = r"(?:1[6-9]|20)\d{2}[a-z]?"
_YEAR_LIST = rf"{_YEAR_TOKEN}(?:\s*,\s*{_YEAR_TOKEN})*"

_NARRATIVE_CITE_RE = re.compile(
    rf"(?<![A-Za-zÀ-ÖØ-öø-ÿ])(?P<authors>{_AUTHOR_SEQ})\s*\((?P<years>{_YEAR_LIST})(?P<extra>(?:\s*,\s*(?:Section|Chapter|Theorem|Lemma|Proposition|p\.|pp\.)[^()\n]*)?)\)"
)
_PAREN_BLOCK_RE = re.compile(r"\(([^()\n]{3,200})\)")
_PAREN_CLAUSE_RE = re.compile(
    rf"^\s*(?:see\s+|e\.g\.?\s*,?\s*|cf\.?\s*,?\s*)?(?P<authors>{_AUTHOR_SEQ})\s*,\s*(?P<years>{_YEAR_LIST})(?:\s*,\s*(?:Section|Chapter|Theorem|Lemma|Proposition|p\.|pp\.)[^;()\n]*)?\s*$"
)
_YEAR_FIND_RE = re.compile(_YEAR_TOKEN)

_STOP_SURNAMES = {
    "january", "february", "march", "april", "may", "june", "july", "august",
    "september", "october", "november", "december",
    "in", "from", "between", "since", "after", "before", "around", "until",
    "during", "by", "at", "on", "for", "with", "under", "over", "about",
    "table", "figure", "section", "chapter", "part", "model", "type", "rule",
    "step", "case", "act", "year", "years", "seed", "version", "edition",
    "class", "group", "study", "trial", "sample", "batch", "stage",
}

_SURNAME_ALIASES = {
    "kolmogorov": "kolmogoroff",
    "chebyshev": "tchebichef",
    "boor": "de boor",
    "vaart": "van der vaart",
    "backer": "de backer",
    "moivre": "de moivre",
    "finetti": "de finetti",
}


@lru_cache(maxsize=1)
def load_works(bib_path: Path = BIB_PATH) -> dict[str, dict]:
    data = json.loads(bib_path.read_text(encoding="utf-8"))
    return data["works"]


def _fold_alpha(text: str) -> str:
    clean = "".join(
        c for c in unicodedata.normalize("NFKD", text or "") if not unicodedata.combining(c)
    )
    return re.sub(r"[^a-z]+", " ", clean.lower()).strip()


def normalize_surname(raw: str) -> str:
    folded = _fold_alpha(raw)
    if folded in _SURNAME_ALIASES:
        return _SURNAME_ALIASES[folded]
    parts = folded.split()
    if parts and parts[-1] in _SURNAME_ALIASES and len(parts) == 1:
        return _SURNAME_ALIASES[parts[-1]]
    return folded


def work_surnames(work: dict) -> list[str]:
    out: list[str] = []
    for author in work.get("authors") or []:
        head = author.split(",", 1)[0].split("[", 1)[0].strip()
        norm = normalize_surname(head)
        if norm:
            out.append(norm)
    return out


def parse_inline_authors(author_str: str) -> tuple[list[str], bool]:
    """Return ``(normalized_surnames, is_et_al)`` from an inline author string."""
    s = author_str.strip()
    is_et_al = False
    if re.search(r"\bet\s+al\.?$", s):
        is_et_al = True
        s = re.sub(r"\s+et\s+al\.?$", "", s).strip()
    parts = re.split(r"\s*,\s*(?:&|and)\s*|\s+(?:&|and)\s+|\s*,\s*", s)
    surnames: list[str] = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        norm = normalize_surname(p)
        if norm:
            surnames.append(norm)
    return surnames, is_et_al


def match_work_key(
    surnames: list[str],
    is_et_al: bool,
    year: int,
    candidate_keys: tuple[str, ...] | list[str],
    works: dict[str, dict] | None = None,
) -> str | None:
    """Resolve an inline ``(surnames, year)`` mention to a bibliography key."""
    if not surnames:
        return None
    catalog = works if works is not None else load_works()

    def score_pool(pool: list[str]) -> list[tuple[int, str]]:
        scored: list[tuple[int, str]] = []
        for k in pool:
            w = catalog.get(k)
            if not w or int(w["year"]) != year:
                continue
            w_surnames = work_surnames(w)
            if not w_surnames:
                continue
            # Check primary surname match (allowing last-token match for multi-word names)
            s0 = surnames[0]
            w0 = w_surnames[0]
            if s0 != w0 and s0.split()[-1] != w0.split()[-1]:
                continue
            if is_et_al and len(w_surnames) < 2:
                continue
            if not is_et_al and len(surnames) > 1:
                w_last_tokens = {ws.split()[-1] for ws in w_surnames}
                if not all(sn in w_surnames or sn.split()[-1] in w_last_tokens for sn in surnames):
                    continue
            exact_count = 2 if (not is_et_al and len(surnames) == len(w_surnames)) else 1
            scored.append((exact_count, k))
        return scored

    cand_list = list(dict.fromkeys(candidate_keys))
    hits = score_pool(cand_list)
    if not hits:
        hits = score_pool(list(catalog.keys()))
    if not hits:
        return None
    hits.sort(key=lambda pair: (-pair[0], cand_list.index(pair[1]) if pair[1] in cand_list else 9999, pair[1]))
    return hits[0][1]


def scan_inline_author_years(text: str) -> list[dict]:
    """Scan prose (outside math, code, links, headings, HTML, and References) for inline author-year citations."""
    base = _STATIC_REF_RE.sub("", text)
    base = _EXISTING_CITE_SUP_RE.sub("", base)
    base = _EXPLICIT_CITE_RE.sub("", base)
    spans = [(m.start(), m.end()) for m in _PROTECT_PROSE_RE.finditer(base)]
    spans.sort()
    merged: list[list[int]] = []
    for s, e in spans:
        if merged and s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])

    results: list[dict] = []
    last = 0
    segments: list[tuple[int, str]] = []
    for s, e in merged:
        if s > last:
            segments.append((last, base[last:s]))
        last = e
    if last < len(base):
        segments.append((last, base[last:]))

    for offset, seg in segments:
        used_ranges: list[tuple[int, int]] = []
        for m in _NARRATIVE_CITE_RE.finditer(seg):
            surnames, is_et_al = parse_inline_authors(m.group("authors"))
            if not surnames or surnames[0].split()[-1] in _STOP_SURNAMES:
                continue
            years = [int(ym.group(0)[:4]) for ym in _YEAR_FIND_RE.finditer(m.group("years"))]
            used_ranges.append((m.start(), m.end()))
            for y in years:
                results.append(
                    {
                        "authors": m.group("authors").strip(),
                        "surnames": surnames,
                        "is_et_al": is_et_al,
                        "year": y,
                        "raw": m.group(0),
                        "start": offset + m.start(),
                        "end": offset + m.end(),
                    }
                )
        for pb in _PAREN_BLOCK_RE.finditer(seg):
            if any(not (pb.end() <= us or pb.start() >= ue) for us, ue in used_ranges):
                continue
            inner = pb.group(1)
            clauses = inner.split(";")
            pos = pb.start() + 1
            for clause in clauses:
                cm = _PAREN_CLAUSE_RE.match(clause)
                if cm:
                    surnames, is_et_al = parse_inline_authors(cm.group("authors"))
                    if surnames and surnames[0].split()[-1] not in _STOP_SURNAMES:
                        years = [int(ym.group(0)[:4]) for ym in _YEAR_FIND_RE.finditer(cm.group("years"))]
                        for y in years:
                            results.append(
                                {
                                    "authors": cm.group("authors").strip(),
                                    "surnames": surnames,
                                    "is_et_al": is_et_al,
                                    "year": y,
                                    "raw": f"({inner})",
                                    "start": offset + pos,
                                    "end": offset + pos + len(clause),
                                }
                            )
                pos += len(clause) + 1
    return results


def _norm_slug(slug: str) -> str:
    s = "".join(c for c in unicodedata.normalize("NFKD", slug) if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    for src, dst in _AMERICAN_TO_BRITISH:
        s = s.replace(src, dst)
    return s


def _candidate_slugs(slug: str, aliases: list[str] | None = None, chapter_stem: str = "") -> list[str]:
    out: list[str] = []

    def add(val: str) -> None:
        for cand in (val, _norm_slug(val)):
            if cand and cand not in out:
                out.append(cand)
            for trimmed in (
                re.sub(r"ies$", "y", cand),
                re.sub(r"es$", "", cand),
                re.sub(r"s$", "", cand),
            ):
                if trimmed and trimmed not in out:
                    out.append(trimmed)

    add(slug)
    if chapter_stem and slug.endswith("-" + chapter_stem):
        add(slug[: -(len(chapter_stem) + 1)])
    for alias in aliases or []:
        add(alias.removesuffix(".html").removesuffix(".qmd"))
    return out


def citations_for_article(article: dict) -> tuple[str, ...]:
    """Return verified citation keys for an article, handling slug aliases and retirements gracefully."""
    slug = article.get("slug") or ""
    box = article.get("box") or {}
    chapter_path = box.get("chapter")
    chapter_name = Path(chapter_path).name if chapter_path else ""
    chapter_stem = Path(chapter_path).stem if chapter_path else ""

    for cand in _candidate_slugs(slug, article.get("aliases"), chapter_stem):
        if cand in ARTICLE_REFS:
            return ARTICLE_REFS[cand]

    hay = f"{slug} {_norm_slug(article.get('term') or '')}"
    for needle, refs in KEYWORD_FALLBACKS:
        if needle in hay:
            return refs

    if chapter_name and chapter_name in CHAPTER_REFS:
        return CHAPTER_REFS[chapter_name][:3]
    return REFERENCE_REFS["distributions.qmd"][:3]


def citations_for_chapter(filename: str) -> tuple[str, ...]:
    return CHAPTER_REFS.get(filename, ())


def citations_for_question(question_id: str) -> tuple[str, ...]:
    return QUESTION_REFS.get(question_id, ())


def _sort_key(work_key: str, works: dict[str, dict]) -> tuple[str, int, str]:
    w = works[work_key]
    first_author = w["authors"][0] if w.get("authors") else ""
    folded = "".join(c for c in unicodedata.normalize("NFKD", first_author) if not unicodedata.combining(c)).lower()
    return (folded, int(w["year"]), w["title"].lower())


def format_authors(authors: list[str]) -> str:
    if len(authors) == 1:
        return authors[0]
    if len(authors) == 2:
        return f"{authors[0]} & {authors[1]}"
    return ", ".join(authors[:-1]) + f" & {authors[-1]}"


def short_author_year(work: dict) -> str:
    authors = work.get("authors") or []
    surnames = [a.split(",", 1)[0].split("[", 1)[0].strip() for a in authors]
    yr = work["year"]
    if not surnames:
        return f"({yr})"
    if len(surnames) == 1:
        return f"{surnames[0]} ({yr})"
    if len(surnames) == 2:
        return f"{surnames[0]} & {surnames[1]} ({yr})"
    return f"{surnames[0]} et al. ({yr})"


def work_tooltip(work: dict) -> str:
    title = work["title"].rstrip(".")
    return f"{short_author_year(work)} — {title}"


def doi_href(doi: str) -> str:
    encoded = urllib.parse.quote(doi.strip(), safe="/:.-_;")
    return f"https://doi.org/{encoded}"


def format_work_md(work: dict) -> str:
    authors = format_authors(work["authors"])
    year = work["year"]
    title = work["title"].rstrip(".")
    kind = work["kind"]
    edition = work.get("edition")
    ed_str = f" ({edition})" if edition else ""

    if kind == "book":
        pub = work["publisher"].rstrip(".")
        core = f"{authors} ({year}). *{title}*{ed_str}. {pub}."
    elif kind == "incollection":
        venue = work.get("venue")
        pub = work.get("publisher")
        vol = work.get("volume")
        pages = work.get("pages")
        parts = []
        if venue:
            v_str = f"In *{venue}*"
            if vol:
                v_str += f", Vol. {vol}"
            if pages:
                v_str += f" (pp. {pages})"
            parts.append(v_str)
        if pub and (not venue or pub not in venue):
            parts.append(pub.rstrip("."))
        tail = ". ".join(parts)
        core = f"{authors} ({year}). {title}. {tail}."
    else:
        venue = work["venue"].rstrip(".")
        vol = work.get("volume")
        issue = work.get("issue")
        pages = work.get("pages")
        loc = f"*{venue}*"
        if vol:
            loc += f", {vol}"
            if issue and issue != vol:
                loc += f"({issue})"
        if pages:
            loc += f", {pages}"
        core = f"{authors} ({year}). {title}. {loc}."

    if work.get("doi"):
        disp = f"https://doi.org/{work['doi']}".replace("<", "&lt;").replace(">", "&gt;")
        link = f"[{disp}]({doi_href(work['doi'])})"
    else:
        url = work["url"]
        disp = url.replace("<", "&lt;").replace(">", "&gt;")
        safe_url = url.replace("(", "%28").replace(")", "%29")
        link = f"[{disp}]({safe_url})"
    return f"{core} {link}"


def format_work_html(work: dict) -> str:
    authors = html.escape(format_authors(work["authors"]))
    year = work["year"]
    title = html.escape(work["title"].rstrip("."))
    kind = work["kind"]
    edition = html.escape(work["edition"]) if work.get("edition") else ""
    ed_str = f" ({edition})" if edition else ""

    if kind == "book":
        pub = html.escape(work["publisher"].rstrip("."))
        core = f"{authors} ({year}). <em>{title}</em>{ed_str}. {pub}."
    elif kind == "incollection":
        venue = html.escape(work["venue"]) if work.get("venue") else ""
        pub = html.escape(work["publisher"].rstrip(".")) if work.get("publisher") else ""
        vol = html.escape(str(work["volume"])) if work.get("volume") else ""
        pages = html.escape(str(work["pages"])) if work.get("pages") else ""
        parts = []
        if venue:
            v_str = f"In <em>{venue}</em>"
            if vol:
                v_str += f", Vol. {vol}"
            if pages:
                v_str += f" (pp. {pages})"
            parts.append(v_str)
        if pub and (not venue or pub not in venue):
            parts.append(pub)
        core = f"{authors} ({year}). {title}. {'. '.join(parts)}."
    else:
        venue = html.escape(work["venue"].rstrip("."))
        vol = html.escape(str(work["volume"])) if work.get("volume") else ""
        issue = html.escape(str(work["issue"])) if work.get("issue") else ""
        pages = html.escape(str(work["pages"])) if work.get("pages") else ""
        loc = f"<em>{venue}</em>"
        if vol:
            loc += f", {vol}"
            if issue and issue != vol:
                loc += f"({issue})"
        if pages:
            loc += f", {pages}"
        core = f"{authors} ({year}). {title}. {loc}."

    if work.get("doi"):
        disp = html.escape(f"https://doi.org/{work['doi']}")
        href = html.escape(doi_href(work["doi"]), quote=True)
    else:
        disp = html.escape(work["url"])
        href = html.escape(work["url"], quote=True)
    return f'{core} <a href="{href}" target="_blank" rel="noopener">{disp}</a>'


def _alpha_label(idx: int) -> str:
    """Convert 0-indexed counter to Wikipedia-style backlink label: a, b, ..., z, aa, ab, ..."""
    out = ""
    n = idx
    while True:
        out = chr(ord("a") + (n % 26)) + out
        n = n // 26 - 1
        if n < 0:
            break
    return out


class PageCitationLinker:
    """Stateful per-page linker that numbers inline citations [1], [2], ... in order of first appearance."""

    def __init__(self, page_keys: tuple[str, ...] | list[str], works: dict[str, dict] | None = None) -> None:
        self.works = works if works is not None else load_works()
        self.page_keys = [k for k in dict.fromkeys(page_keys) if k in self.works]
        self.number_for_key: dict[str, int] = {}
        self.ordered_cited_keys: list[str] = []
        self.ref_ids_by_key: dict[str, list[str]] = {}

    def cite_sup(self, key: str) -> str:
        if key not in self.works:
            raise KeyError(f"Unknown citation key {key!r} in {{cite:...}} marker")
        if key not in self.number_for_key:
            num = len(self.ordered_cited_keys) + 1
            self.number_for_key[key] = num
            self.ordered_cited_keys.append(key)
        else:
            num = self.number_for_key[key]
        occ = len(self.ref_ids_by_key.get(key, ())) + 1
        ref_id = f"cite_ref-{num}" if occ == 1 else f"cite_ref-{num}-{occ}"
        self.ref_ids_by_key.setdefault(key, []).append(ref_id)
        if key not in self.page_keys:
            self.page_keys.append(key)
        tip = html.escape(work_tooltip(self.works[key]), quote=True)
        return (
            f'<sup id="{ref_id}" class="cite-ref" data-cite-key="{key}">'
            f'<a href="#cite_note-{num}" title="{tip}">[{num}]</a></sup>'
        )

    def cite_sups(self, keys: list[str]) -> str:
        seen: list[str] = []
        for k in keys:
            if k not in seen:
                seen.append(k)
        return "".join(self.cite_sup(k) for k in seen)

    def _transform_prose_segment(self, seg: str) -> str:
        """Attach superscripts to explicit {{cite:...}} markers and matched inline Author (Year) mentions."""
        # Tokenize explicit {{cite:...}} markers first so we process left-to-right in reading order!
        events: list[tuple[int, int, str, list[str]]] = []

        for m in _EXPLICIT_CITE_RE.finditer(seg):
            raw_keys = [k.strip() for k in m.group(1).split(",") if k.strip()]
            events.append((m.start(), m.end(), "explicit", raw_keys))

        def overlaps(a: int, b: int) -> bool:
            return any(not (b <= s or a >= e) for s, e, _, _ in events)

        # Narrative Author (Year) or Author (Year1, Year2)
        for m in _NARRATIVE_CITE_RE.finditer(seg):
            if overlaps(m.start(), m.end()):
                continue
            # If immediately followed by an explicit {{cite:...}}, let the explicit marker handle it cleanly
            after = seg[m.end() :]
            if after.startswith("{{cite:"):
                continue
            surnames, is_et_al = parse_inline_authors(m.group("authors"))
            if not surnames or surnames[0].split()[-1] in _STOP_SURNAMES:
                continue
            years = [int(ym.group(0)[:4]) for ym in _YEAR_FIND_RE.finditer(m.group("years"))]
            matched_keys: list[str] = []
            for y in years:
                mk = match_work_key(surnames, is_et_al, y, self.page_keys, self.works)
                if mk:
                    matched_keys.append(mk)
            if matched_keys:
                events.append((m.start(), m.end(), "append", matched_keys))

        # Parenthetical (Author, Year; Author, Year)
        for pb in _PAREN_BLOCK_RE.finditer(seg):
            if overlaps(pb.start(), pb.end()):
                continue
            after = seg[pb.end() :]
            if after.startswith("{{cite:"):
                continue
            inner = pb.group(1)
            clauses = inner.split(";")
            matched_keys = []
            all_clauses_valid = True
            for clause in clauses:
                cm = _PAREN_CLAUSE_RE.match(clause)
                if not cm:
                    all_clauses_valid = False
                    break
                surnames, is_et_al = parse_inline_authors(cm.group("authors"))
                if not surnames or surnames[0].split()[-1] in _STOP_SURNAMES:
                    all_clauses_valid = False
                    break
                years = [int(ym.group(0)[:4]) for ym in _YEAR_FIND_RE.finditer(cm.group("years"))]
                for y in years:
                    mk = match_work_key(surnames, is_et_al, y, self.page_keys, self.works)
                    if mk:
                        matched_keys.append(mk)
            if all_clauses_valid and matched_keys:
                events.append((pb.start(), pb.end(), "append", matched_keys))

        if not events:
            return seg

        events.sort(key=lambda item: item[0])
        out: list[str] = []
        pos = 0
        for start, end, mode, keys in events:
            if start < pos:
                continue
            out.append(seg[pos:start])
            sups = self.cite_sups(keys)
            if mode == "explicit":
                # "...usefulness{{cite:key}}." renders as usefulness.[n]. A marker restored
                # from a named attribution, "Bliss (1935){{cite:key}}.", keeps the number
                # before the punctuation: Bliss (1935)[n].
                punct = _AFTER_CITE_PUNCT_RE.match(seg[end:])
                preceded_by_paren = start > 0 and seg[start - 1] == ")"
                if punct and not preceded_by_paren:
                    out.append(punct.group(0) + sups)
                    end += punct.end()
                else:
                    out.append(sups)
            else:
                out.append(seg[start:end] + sups)
            pos = end
        out.append(seg[pos:])
        return "".join(out)

    def process_text(self, text: str) -> str:
        """Process a block of Markdown/Quarto prose, strictly skipping protected regions."""
        # Leave fenced code untouched, including any sample of this markup.
        fences: list[str] = []

        def _hold_fence(match: re.Match) -> str:
            fences.append(match.group(0))
            return f"\ue000CITEFENCE{len(fences) - 1}\ue000"

        shielded = re.sub(r"```.*?```", _hold_fence, text, flags=re.S)
        # A previous pass stored the key on the superscript. Restore it, then drop any
        # leftover superscript that has no key, so numbering can be rebuilt.
        clean = _CITE_SUP_KEY_RE.sub(lambda match: "{{cite:" + match.group(1) + "}}", shielded)
        clean = _EXISTING_CITE_SUP_RE.sub("", clean)
        spans = [(m.start(), m.end()) for m in _PROTECT_PROSE_RE.finditer(clean)]
        spans.sort()
        merged: list[list[int]] = []
        for s, e in spans:
            if merged and s <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], e)
            else:
                merged.append([s, e])

        parts: list[str] = []
        last = 0
        for s, e in merged:
            if s > last:
                parts.append(self._transform_prose_segment(clean[last:s]))
            parts.append(clean[s:e])
            last = e
        if last < len(clean):
            parts.append(self._transform_prose_segment(clean[last:]))
        joined = "".join(parts)
        if fences:
            joined = re.sub(
                r"\ue000CITEFENCE(\d+)\ue000",
                lambda match: fences[int(match.group(1))],
                joined,
            )
        return joined

    def final_ordered_keys(self) -> list[str]:
        remaining = [k for k in self.page_keys if k not in self.number_for_key]
        remaining_sorted = sorted(remaining, key=lambda k: _sort_key(k, self.works))
        return self.ordered_cited_keys + remaining_sorted

    def render_references_section(self) -> str:
        ordered = self.final_ordered_keys()
        if not ordered:
            return ""
        li_lines: list[str] = []
        for idx, k in enumerate(ordered, 1):
            ref_ids = self.ref_ids_by_key.get(k, [])
            backlink_html = ""
            if len(ref_ids) == 1:
                backlink_html = (
                    f'<span class="cite-backlink">'
                    f'<a href="#{ref_ids[0]}" aria-label="Jump up" title="Jump up">^</a>'
                    f"</span> "
                )
            elif len(ref_ids) > 1:
                sublinks = " ".join(
                    f'<a href="#{rid}" aria-label="Jump up to {_alpha_label(i)}"><sup>{_alpha_label(i)}</sup></a>'
                    for i, rid in enumerate(ref_ids)
                )
                backlink_html = f'<span class="cite-backlink">^ {sublinks}</span> '
            li_lines.append(f'  <li id="cite_note-{idx}">{backlink_html}{format_work_html(self.works[k])}</li>')
        items = "\n".join(li_lines)
        return (
            "\n\n## References {#references}\n\n"
            "```{=html}\n"
            '<div class="wiki-refs">\n'
            "<ol>\n"
            f"{items}\n"
            "</ol>\n"
            "</div>\n"
            "```\n"
        )


def strip_cite_markers(text: str) -> str:
    """Remove raw ``{{cite:...}}`` markers and rendered ``<sup class="cite-ref">...</sup>`` tags cleanly."""
    text = _EXPLICIT_CITE_RE.sub("", text)
    return _EXISTING_CITE_SUP_RE.sub("", text)


def render_references_md(keys: tuple[str, ...] | list[str], *, works: dict[str, dict] | None = None) -> str:
    linker = PageCitationLinker(keys, works=works)
    return linker.render_references_section()


def render_references_html_fenced(keys: tuple[str, ...] | list[str], *, works: dict[str, dict] | None = None) -> str:
    linker = PageCitationLinker(keys, works=works)
    return linker.render_references_section()


def attach_page_references(pages: list[dict], article_by_path: dict[Path, dict]) -> None:
    """Link inline citations with numbered superscripts and append ``## References`` to generated pages."""
    works = load_works()
    non_prose_labels = {"infobox", "what-links-here", "see-also", "questions", "figures-head", "figure", "references"}
    for page in pages:
        kind = page["kind"]
        path: Path = page["path"]
        keys: tuple[str, ...] = ()
        if kind in {"chapter", "final"}:
            keys = citations_for_chapter(path.name)
        elif kind == "reference":
            keys = REFERENCE_REFS.get(path.name, ())
        elif kind == "article":
            article = article_by_path.get(path)
            if article is not None:
                keys = citations_for_article(article)
        elif kind == "question":
            keys = citations_for_question(path.stem)

        # Even if a question is not in QUESTION_REFS, strip or link any inline citations if present
        linker = PageCitationLinker(keys, works=works)
        new_blocks = []
        for is_content, label, text in page["blocks"]:
            if label not in non_prose_labels:
                text = linker.process_text(text)
            new_blocks.append((is_content, label, text))
        page["blocks"] = new_blocks

        section = linker.render_references_section()
        if section:
            page["blocks"].append((False, "references", section))


def _upsert_static_page_references(path: Path, keys: tuple[str, ...], *, works: dict[str, dict]) -> None:
    if not path.is_file():
        return
    raw = path.read_text(encoding="utf-8")
    body = _STATIC_REF_RE.sub("", raw).rstrip()
    linker = PageCitationLinker(keys, works=works)
    linked_body = linker.process_text(body)
    section = linker.render_references_section()
    updated = linked_body + section
    if updated != raw:
        path.write_text(updated, encoding="utf-8")


def write_sheet_and_static_references(wiki_root: Path = ROOT) -> None:
    """Link inline citations and attach numbered ``## References`` to distributions.qmd, overview.qmd, and labs/*.qmd."""
    works = load_works()
    dist_path = wiki_root / "reference" / "distributions.qmd"
    _upsert_static_page_references(dist_path, REFERENCE_REFS["distributions.qmd"], works=works)

    overview_path = wiki_root / "overview.qmd"
    _upsert_static_page_references(overview_path, OVERVIEW_REFS, works=works)

    labs_dir = wiki_root / "labs"
    for lab_name, keys in LAB_REFS.items():
        _upsert_static_page_references(labs_dir / lab_name, keys, works=works)
