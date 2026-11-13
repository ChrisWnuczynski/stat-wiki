"""Accessible statistical descriptions for every figure in ``figures/``.

Every PNG generated from the chapters, practice examples, or TikZ diagrams
maps here to a concise, self-contained plain-text description of its axes,
curves, distributions, geometric projections, network diagrams, or comparison
takeaways so readers using screen readers or text-only browsers get the same
information as visual readers.
"""

from __future__ import annotations

import re

FIGURE_ALTS: dict[str, str] = {
    "06-smooth-means-roughness-penalty.png": (
        "Three smoothing spline curves overlaid on noisy scatter points as the roughness penalty lambda varies: "
        "lambda near zero interpolates every wiggle, intermediate lambda tracks the underlying smooth trend, "
        "and large lambda flattens onto the least-squares straight line."
    ),
    "08-random-intercepts-shared-intercept.png": (
        "Schematic plot of response against covariate x showing a dashed population regression line beta_0 + beta_1 x "
        "and parallel solid lines for separate blocks, each shifted vertically by its own random intercept alpha_j "
        "with observations clustered around their block line."
    ),
    "ar-paths.png": (
        "Three time-series traces generated from the same innovation sequence over time: a stationary AR(1) series "
        "fluctuating around its mean, a unit-root random walk drifting away without returning, and a jagged MA(1) "
        "series with one-step memory."
    ),
    "beetles.png": (
        "Scatterplot of the sample proportion of flour beetles killed (0 to 1) against log10 carbon disulphide dose "
        "with vertical binomial standard-error bars, rising steeply along an S-shaped dose-response trajectory."
    ),
    "burn-ellipse.png": (
        "Two-dimensional parameter plot comparing the two burn-severity slopes: a dashed axis-aligned rectangle "
        "for the pair of marginal 95% confidence intervals and an inscribed joint 95% confidence ellipse showing "
        "corners inside the rectangle that fall outside the joint region."
    ),
    "cholesterol-band.png": (
        "Binary heart-disease indicator (jittered near 0 and 1) plotted against serum cholesterol from 4.5 to 7.0, "
        "comparing a solid S-shaped logistic curve and dashed slope-interval curves bounded in (0, 1) against a "
        "straight least-squares line that exits the probability bounds."
    ),
    "cholesterol-links-2025.png": (
        "Fitted probability of heart disease (0.0 to 1.0) against cholesterol (4.5 to 7.0) with sex markers f and m "
        "at 0 and 1, comparing nearly overlapping solid logit and dotted probit S-shaped curves rising from about "
        "0.2 to 0.9."
    ),
    "cholesterol-links.png": (
        "Fitted probability of heart disease against serum cholesterol under three binary GLM links: logit and probit "
        "curves nearly coincide symmetrically, while the complementary log-log curve sits slightly lower at moderate "
        "cholesterol and climbs more steeply near 1 at high cholesterol."
    ),
    "cholesterol-smooth-2025.png": (
        "Component smooth plot s(cholesterol, 2.01) on the link scale (-2 to 4) against cholesterol (4.5 to 7.0) with "
        "rug marks along the bottom: a solid curve flat below 5.0 then rising steeply above 5.0, flanked by dashed "
        "95% confidence bands that widen sharply above 6.5 where observations are sparse."
    ),
    "clotting.png": (
        "Plot of blood clotting time in seconds (0 to 150) against plasma percentage concentration (0 to 100) for "
        "thromboplastin Lot 1 and Lot 2: hyperbolic decay curves where Lot 1 stays consistently above Lot 2, comparing "
        "solid Gamma inverse-link fits with dotted inverse-Gaussian inverse-quadratic fits."
    ),
    "contraception.png": (
        "Fitted probability of contraceptive use against centred age for women with living children in a typical "
        "district: two concave downward parabolic curves on the probability scale, with the urban curve parallel above "
        "the rural curve and peaking near mean age."
    ),
    "da-01-studies-and-data-assignment.png": (
        "Two-panel causal diagram comparing study designs. Left (observational study): confounding variables diet and "
        "income have arrows into both maternal smoking and son's height. Right (designed experiment): random assignment "
        "determines drug treatment independently of age, diet, and fitness before measuring blood pressure."
    ),
    "da-alice-strip.png": (
        "Horizontal strip plot of heart-rate change in beats per minute for twenty participants assigned to caffeinated "
        "or decaffeinated diet cola, with group means marked: caffeinated changes cluster higher (mean 15.8 bpm) than "
        "decaffeinated changes (mean 5.1 bpm)."
    ),
    "da-anaemia-death.png": (
        "Two-panel bar chart of follow-up mortality by anaemia status in 299 heart-failure patients: raw patient counts "
        "on the left (unequal group totals) versus proportion who died on the right (about 0.36 with anaemia vs 0.29 "
        "without anaemia)."
    ),
    "da-birthwt-interaction.png": (
        "Scatterplot of infant birth weight in grams against mother's age in years with separate least-squares lines "
        "for non-smokers and smokers: the non-smoker line slopes upward (+27.7 g/year) while the smoker line slopes "
        "downward (-18.8 g/year), crossing to show an age-by-smoking interaction."
    ),
    "da-birthwt-residuals.png": (
        "Two-panel diagnostic plot for the birth-weight linear model. Left: residuals in grams against fitted birth "
        "weights forming an even horizontal band around zero. Right: normal quantile-quantile plot of residuals "
        "tracking closely along the straight diagonal reference line."
    ),
    "da-chisq-simulation.png": (
        "Histogram of Pearson chi-squared statistics T from 10,000 simulated multinomial throws of 100 balls into 10 "
        "equally likely boxes, closely matching the overlaid continuous chi-squared density with 9 degrees of freedom."
    ),
    "da-coldsore.png": (
        "Strip plot of cold-sore healing times in days across five treatment groups (six patients per group) with "
        "group means marked: placebo has the longest mean healing time (7.5 days) and treatment 3 the shortest "
        "(about 4.3 days)."
    ),
    "da-creatinine-by-death.png": (
        "Side-by-side comparison of serum creatinine on a logarithmic scale grouped by survival status in heart-failure "
        "patients, showing an upward-shifted distribution and higher median among patients who died despite substantial "
        "overlap."
    ),
    "da-creatinine-qq.png": (
        "Two-panel normal quantile-quantile plot for serum creatinine in 299 patients. Left: raw creatinine values "
        "curve steeply upward in the right tail. Right: reciprocal creatinine values lie close to the straight normal "
        "reference line with slight rounding steps."
    ),
    "da-creatinine-shape.png": (
        "Three-panel summary of serum creatinine (mg/dL) for 299 heart-failure patients: a boxplot on the left with 29 "
        "high outliers above the upper whisker, a strongly right-skewed histogram with kernel density curve in the "
        "middle, and a much more symmetric histogram on a log10 scale on the right."
    ),
    "da-interaction.png": (
        "Two-panel interaction plot of group means. Left: mean wheat yield across regions with nearly parallel lines "
        "for each fertiliser (no interaction). Right: mean crop yield across fertiliser levels where lines for two "
        "pesticide settings cross sharply (strong interaction)."
    ),
    "da-pairs.png": (
        "Three-by-three scatterplot matrix for 299 heart-failure patients showing all pairwise scatterplots of age, "
        "log serum creatinine, and serum sodium, with diffuse point clouds indicating weak pairwise linear associations."
    ),
    "da-power-by-n.png": (
        "Line plot of statistical power (0 to 1) against sample size n for a one-sided level-0.05 one-sample t test "
        "at an effect size of 0.5 standard deviations, rising monotonically and crossing 0.80 power near n = 27."
    ),
    "da-sodium-jitter.png": (
        "Two-panel scatterplot of serum sodium (mEq/L) against ejection fraction (%). Left: exact recorded integer "
        "pairs with heavy overplotting on grid points. Right: jittered points revealing dense clusters around 35-40% "
        "ejection fraction and 135-140 mEq/L sodium."
    ),
    "da-two-sample-heights.png": (
        "Overlapping histograms of simulated adult heights (cm) from two normal populations: 60 sons of mothers who "
        "smoked (mean 170 cm, variance 200) and 140 sons of non-smokers (mean 175 cm, variance 100), illustrating "
        "wide individual overlap despite a 5 cm mean difference."
    ),
    "deaths-corr.png": (
        "Four-panel autocorrelation (ACF) and partial autocorrelation (PACF) correlogram of monthly US accidental "
        "deaths by lag in months. Top row (raw series): slow decay with strong peaks at lags 12 and 24. Bottom row "
        "(after seasonal and first differencing): isolated significant spikes at lag 1 and lag 12."
    ),
    "deaths-forecast.png": (
        "Time-series plot of monthly US accidental deaths through December 1978 followed by seasonal forecasts from "
        "January 1979 with shaded 80% and 95% prediction bands, marking the observed January 1979 count of 7,798 "
        "below the point forecast but inside the 95% interval."
    ),
    "deaths-series.png": (
        "Line plot of monthly accidental deaths in the United States from 1973 to 1978 (72 months), displaying a "
        "pronounced annual summer peak every 12 months alongside a dip in overall level around 1974-1975."
    ),
    "fish-latitude-smooth-2024.png": (
        "GAM smooth plot s(latitude, 8.88) against latitude (0 to 75 degrees) with rug marks and dashed 95% confidence "
        "bands: an oscillating nonlinear curve dipping near latitude 22, peaking near 38, and widening substantially "
        "above latitude 65 where data are sparse."
    ),
    "fish-scatterplots-2024.png": (
        "Two-panel scatterplot with number of fish species (0 to 250) on the vertical axis against latitude (left) and "
        "log lake area (right): species counts cluster into two latitude bands without a linear trend on the left, "
        "whereas counts rise with increasing spread as log lake area grows on the right."
    ),
    "hunua.png": (
        "Fitted probability of plant species presence (0 to 1) against altitude in metres from three marginal logit "
        "curves: Beilschmiedia tawa rises from rare at sea level to peak at mid-altitude, Cyathea dealbata stays nearly "
        "flat, and Knightia excelsa follows an intermediate curve."
    ),
    "inf-04-hypothesis-tests-errors.png": (
        "Two-panel normal density diagram for a size-0.05 two-sided z test with cutoffs at plus and minus 1.960. Left: "
        "standard normal null N(0, 1) shading the two critical tails and marking observed z = 2.30 (p = 0.021). Right: "
        "shifted N(2, 1) alternative shading type II error between cutoffs and power beyond them."
    ),
    "inf-07-anova-sums-of-squares.png": (
        "Geometric diagram of one-way ANOVA across three factor levels showing individual observations Y_ij, level "
        "means Y-bar_.j, and the grand mean Y-bar: vertical brackets separate within-group residuals going into "
        "SS_error from level-mean deviations going into SS_treatment."
    ),
    "inf-corn-groups.png": (
        "Dot plot of corn yields across four varieties (three plots per variety) with red horizontal bars at variety "
        "means and a dashed grand mean line, showing small within-variety scatter compared with Variety 3 standing "
        "well above the others."
    ),
    "inf-coverage.png": (
        "Horizontal interval plot of forty simulated 95% Student t confidence intervals from N(10, 1) samples of size "
        "10 against a vertical line at the true mean mu = 10: thirty-eight intervals cross the truth and two intervals "
        "highlighted in red miss it."
    ),
    "inf-hardness-blocks.png": (
        "Two-panel plot of metal hardness readings across four indenter tips. Left: unblocked points per tip where "
        "between-coupon spread obscures tip differences. Right: points connected by lines within each metal coupon "
        "running nearly parallel, revealing consistent differences between tips."
    ),
    "inf-heart-oxygen.png": (
        "Scatterplot of oxygen intake against heart rate (bpm) with the fitted least-squares line, a narrow inner 95% "
        "confidence band for the mean response, and a wider outer 95% prediction band for a new observation, both "
        "flaring outward away from mean heart rate 107 and into a shaded extrapolation zone."
    ),
    "inf-houses-poisson.png": (
        "Grouped bar chart comparing observed numbers of land plots having 0, 1, 2, 3, or 4+ houses against fitted "
        "Poisson expected counts: close agreement at 0 and 2 houses, but fewer observed plots at 1 house and more at "
        "4 or more than the Poisson fit predicts."
    ),
    "inf-np-region.png": (
        "Overlapping normal densities of the standardised sample mean under H_0 (centred at 0) and under a right-sided "
        "alternative (centred at 1.8), divided by the Neyman-Pearson cutoff at 1.645 into shaded size alpha = 0.05 "
        "under H_0 and larger shaded power under the alternative."
    ),
    "inf-p-value.png": (
        "Two-panel Student t_39 null density for the one-sided caffeine test: full bell curve on the left and enlarged "
        "upper tail on the right showing the 1% critical cutoff at t = 2.43 and the observed statistic t = 2.575 "
        "with shaded tail area p = 0.007."
    ),
    "inf-power-curve.png": (
        "Plot of test power (0 to 1) against true first-serve probability p (from 0.6 to 1.0) for n = 15 binomial "
        "trials comparing two rejection rules: rejecting at 12 or more serves gives higher power everywhere than "
        "rejecting at 13 or more, at the cost of raising null size at p = 0.6 from 0.027 to 0.091."
    ),
    "inf-ppv-prevalence.png": (
        "Curves of positive predictive value (0 to 1) against disease prevalence (0 to 1) for two diagnostic tests "
        "(95% and 99% sensitivity and specificity), rising steeply from near zero at rare prevalence (PPV around 0.09 "
        "at prevalence 0.005) toward 1 as prevalence increases."
    ),
    "inf-regression-effect.png": (
        "Scatterplot of 1,078 simulated father-son height pairs in inches (correlation 0.5) comparing the shallower "
        "solid least-squares regression line (slope near 0.5) against the steeper dashed equal-standing line y = x + 1, "
        "with shaded vertical strips at 63 and 71 inches showing regression toward the mean."
    ),
    "inf-t-densities.png": (
        "Overlaid symmetric bell curves comparing Student t densities on 1, 3, and 10 degrees of freedom against the "
        "standard normal density: lower degrees of freedom have lower peaks and heavier tails, nearly matching the "
        "normal curve by 10 degrees of freedom."
    ),
    "inf-two-factor-means.png": (
        "Two-factor interaction plot of mean plant yield against water level (dry vs wet) with separate lines for low "
        "and high fertiliser: both lines rise with water, but the high-fertiliser line rises much more steeply "
        "(gap of 8 vs gap of 3), showing non-parallel slopes."
    ),
    "kyphosis-additive.png": (
        "Three-panel partial-effect plot for an additive logistic GAM of postoperative kyphosis on the centred log-odds "
        "scale: a rising then flattening curve for age, a nearly linear upward trend for number of vertebrae, and a "
        "curve for starting vertebra that stays flat then drops sharply."
    ),
    "kyphosis.png": (
        "Two-panel plot of postoperative kyphosis against child age in months. Top: centred GAM smooth on the log-odds "
        "scale with 95% confidence band and dashed zero line. Bottom: concave fitted probability curve rising to a "
        "mid-childhood peak then falling, contrasted with a monotonic dashed linear-logit curve."
    ),
    "leaf-residuals.png": (
        "Two-panel plot of Pearson residuals against the linear predictor with dashed reference lines at plus and minus "
        "2 for barley leaf-blotch proportions. Left: quasi-binomial variance compresses residuals near small fitted "
        "values. Right: Wedderburn's mu^2(1 - mu)^2 variance equalises vertical spread across the range."
    ),
    "lidar.png": (
        "Scatterplot of LIDAR log-ratio signal against range comparing three moving-window smoothers: a narrow window "
        "tracking high-frequency noise, a 25-foot window capturing the sharp sigmoidal drop cleanly, and a 100-foot "
        "window oversmoothing the transition while residual scatter widens at larger ranges."
    ),
    "links.png": (
        "Comparison of three inverse link curves mapping a linear predictor onto probabilities in (0, 1), matched to "
        "slope one at probability 0.5: symmetric logistic and probit S-curves versus an asymmetric complementary "
        "log-log curve that approaches 1 much more abruptly than 0."
    ),
    "marginal-schematic.png": (
        "Schematic plot of complication risk against maternal age illustrating Simpson's paradox between conditional "
        "and marginal slopes: individual mothers' trajectories in red each slope gently downward with age, whereas "
        "the population-averaged blue curve across all births slopes upward."
    ),
    "orthodont-trajectories-2025.png": (
        "Twenty-seven small-multiple line panels (16 boys M01-M16 and 11 girls F01-F11) plotting orthodontic craniofacial "
        "distance (roughly 15 to 35 mm) across childhood ages: trajectories generally trend upward with substantial "
        "between-child differences in baseline intercept and occasional sharp jumps."
    ),
    "part1-fig-01-credible-regions.png": (
        "Comparison of two 95% Bayesian credible intervals on the same right-skewed Beta(3, 9) posterior density: "
        "an equal-tailed interval leaving 2.5% area in each tail versus a shorter highest-posterior-density (HPD) "
        "interval shifted leftward with equal density heights at both endpoints."
    ),
    "part1-fig-02-prior-sensitivity.png": (
        "Three-column panel comparing Beta(5, 5), Beta(1, 1), and U-shaped Beta(0.6, 0.6) priors (left) and their "
        "posteriors after 3/10 heads (middle) and 30/100 heads (right) with a dashed line at 0.3: distinct posteriors "
        "at n = 10 converge tightly around 0.3 by n = 100."
    ),
    "part1-fig-04-gibbs-staircase.png": (
        "Two-dimensional contour plot of a bivariate normal target with correlation 0.95 overlaid with an axis-aligned "
        "Gibbs-sampler trajectory: alternating horizontal X_1 | X_2 and vertical X_2 | X_1 updates take small "
        "staircase steps along the narrow diagonal ridge."
    ),
    "part1-fig-04-proposal-scale.png": (
        "Three trace plots of random-walk Metropolis chains targeting N(0, 1) with small, moderate, and huge proposal "
        "scales s_q: tiny proposals accept almost always but drift slowly, huge proposals stick flat during long "
        "rejection runs, and moderate proposals mix rapidly across the support."
    ),
    "part1-fig-05-dirichlet-simplex.png": (
        "Three ternary simplex triangles showing simulated probability vectors from symmetric Dirichlet(alpha, alpha, alpha) "
        "laws: alpha = 1 scatters uniformly across the triangle, alpha = 5 concentrates around the centroid (1/3, 1/3, 1/3), "
        "and alpha = 0.1 pushes draws into the corners and edges."
    ),
    "part1-fig-06-fruit-posterior.png": (
        "Gamma(189, 21) posterior density curve for mean fruit rate theta showing the region theta <= 10 shaded (93.3% "
        "posterior probability) alongside the two-sided 95% equal-tailed interval whose upper endpoint extends slightly "
        "above 10."
    ),
    "part1-fig-08-hyperposterior-grid.png": (
        "Contour plot of the rat-tumour log-hyperposterior density in transformed coordinates (z_1, z_2) including the "
        "Jacobian: a dashed inner box truncates substantial upper-right contour mass, whereas an expanded domain encloses "
        "the full posterior mode marked in gold."
    ),
    "part1-fig-08-shrinkage.png": (
        "Shrinkage plot for the rat-tumour studies comparing raw binomial tumour rates against hierarchical posterior "
        "medians, with line segments pulling extreme small-sample estimates toward the common population rate and "
        "point sizes proportional to study sample size n_j."
    ),
    "part1-fig-09-regression-bands.png": (
        "Bayesian linear regression plot of eight observations with the posterior mean line, an inner 95% credible band "
        "for the mean response, and a wider outer 95% posterior predictive band for a new observation, with vertical "
        "rules at x = 4.5 (interpolation) and x = 10 (extrapolation where bands flare wide)."
    ),
    "part1-inline-simplex.png": (
        "Equilateral triangle representing the three-category probability simplex with vertices labelled (1, 0, 0), "
        "(0, 1, 0), and (0, 0, 1), and an interior point marked at barycentric coordinates (0.2, 0.3, 0.5)."
    ),
    "pit.png": (
        "Two-panel uniform quantile-quantile plot of ordered probability-integral-transform (PIT) residuals against "
        "the 45-degree diagonal. Left: systematic upward bow from a misspecified mean. Right: gamma clotting-time fit "
        "tracking closely along the uniform diagonal."
    ),
    "pneumonia.png": (
        "Plot of cumulative probabilities of pneumoconiosis severity in coal miners against exposure time: observed "
        "proportions and two fitted proportional-odds logistic curves (mild-or-severe above severe) sharing a common "
        "log-odds slope."
    ),
    "prob-01-experiments-total-probability.png": (
        "Two-panel area diagram for the three-factory defective-chip example. Left: partition of production width into "
        "shares B_1, B_2, B_3 with defective heights giving joint areas 0.0015, 0.0175, and 0.0100 summing to 0.029. "
        "Right: renormalised Bayes posterior shares 0.052, 0.603, and 0.345."
    ),
    "prob-02-random-variables-distribution-function.png": (
        "Four-panel comparison of discrete and continuous distributions. Left column: uniform six-sided die mass bars "
        "and its right-continuous staircase CDF with jumps of 1/6. Right column: Exp(1) density shading P(0.5 < X <= 1.6) "
        "as area beneath the curve, matched to the vertical rise F(1.6) - F(0.5) on the smooth CDF."
    ),
    "prob-04-joint-distributions-conditional-slice.png": (
        "Geometric support diagram on the unit square showing the shaded triangle 0 <= y <= x <= 1 below the diagonal "
        "y = x, with a vertical slice highlighted at x = 0.72 illustrating the uniform conditional distribution of "
        "Y given X = 0.72 on (0, 0.72)."
    ),
    "prob-06-markov-chains-reflected-walk.png": (
        "Two-panel diagram of a random walk reflected at state 0. Top: state-transition graph on states 0, 1, 2, 3, ... "
        "with upward step probabilities p and downward probabilities q. Bottom: geometric stationary bar weights "
        "pi_j = (1/2)^(j+1) when p/q = 1/2."
    ),
    "prob-acceptance-rejection.png": (
        "Scatterplot illustrating acceptance-rejection sampling on [0, 1] for target density f(x) = 6x(1 - x) beneath "
        "horizontal envelope c = 1.5: dark accepted points fill the region under the parabola (about two-thirds of "
        "600 uniform proposals) while light points above the curve are rejected."
    ),
    "prob-binomial-normal.png": (
        "Step-function CDF of Bin(20, 1/2) overlaid with the smooth N(10, 5) normal approximation CDF, showing the "
        "smooth curve bisecting each vertical step so evaluating at k + 0.5 provides the continuity correction."
    ),
    "prob-birthday.png": (
        "S-shaped curve of the probability that at least two people share a birthday against group size n (1 to 70), "
        "crossing probability 0.5 at n = 23 people and exceeding 0.99 by n = 57."
    ),
    "prob-clt.png": (
        "Two-row by three-column grid of histograms of standardised sums of n = 1, 2, and 10 independent draws from "
        "Uniform(0, 1) (top row) and Exp(1) (bottom row) with the N(0, 1) bell curve overlaid: uniform sums look "
        "normal by n = 10 while exponential sums retain slight right skew."
    ),
    "prob-coin-averages.png": (
        "Spaghetti line plot of running head proportions across n = 1 to 100 tosses for twenty simulated fair-coin "
        "sequences, swinging widely between 0 and 1 at small n before funnelling toward the horizontal line at 0.5."
    ),
    "prob-continuous-densities.png": (
        "Two-panel density comparison: three decaying exponential densities with rates 0.5, 1, and 2 on [0, infinity) "
        "(left), and three symmetric zero-mean normal bell curves with standard deviations 0.5, 1, and 2 showing taller "
        "peaks for smaller spreads (right)."
    ),
    "prob-correlation.png": (
        "Four scatterplots of 200 standard bivariate normal draws with correlations rho = 0, 0.4, 0.7, and -0.9, "
        "progressing from a circular cloud at rho = 0 to tilted elliptical clouds tightening sharply along a negative "
        "diagonal at rho = -0.9."
    ),
    "prob-discrete-pmfs.png": (
        "Three side-by-side probability mass bar charts: left-skewed Bin(10, 0.7) on 0..10, geometrically decaying "
        "Geom(0.3) on 1, 2, ..., and roughly bell-shaped Poisson(10) centred near 10."
    ),
    "prob-inverse-transform.png": (
        "Diagram of inverse-transform simulation on a smooth S-shaped CDF F(x): horizontal arrows map uniform draws U "
        "on the vertical [0, 1] axis to the curve and vertically down to X = F^(-1)(U), concentrating draws where F "
        "rises steeply."
    ),
    "prob-random-walk.png": (
        "Trajectory of a symmetric simple random walk X_n on the integers (p = q = 1/2) over 500 steps, making long "
        "excursions away from zero and returning without settling toward any stationary distribution."
    ),
    "prob-stepping-stones.png": (
        "Two-panel Markov-chain plot for the six-stepping-stones frog walk starting at stone 1. Left: discrete state "
        "trajectory over the first 60 hops. Right: exact n-step state probabilities converging onto horizontal dashed "
        "stationary probabilities within 20 steps."
    ),
    "prob-system-survival.png": (
        "Survival probability curves P(T > t) against time t for systems of independent Exp(1) components: parallel "
        "(2 components) stays highest, series (2 components) drops fastest, and 2-out-of-3 starts above a single "
        "component before crossing below it at t = log 2 = 0.69."
    ),
    "prob-systems.png": (
        "Reliability block network diagrams connecting left input to right output: two components in series (top left), "
        "two components in parallel (bottom left), and a five-component Wheatstone bridge with a vertical cross-link "
        "component 3 (right)."
    ),
    "prob-weibull-hazards.png": (
        "Line plot of Weibull hazard functions h(t) against time t at unit rate for three shape values: decreasing "
        "infant-mortality curve for beta < 1, flat constant exponential line for beta = 1, and rising wear-out curve "
        "for beta > 1."
    ),
    "q3-marginals.png": (
        "Three side-by-side bar histograms of discrete marginal distributions: x on 0..10 peaking near 4-5, y on 0..20 "
        "symmetric around 12, and fine-grained z on [0, 1] forming a smooth bell shape centred at 0.50."
    ),
    "sleep.png": (
        "Spaghetti plot of reaction time in milliseconds against days of sleep deprivation (0 to 9) for eighteen "
        "drivers with the black population mixed-model line (251 + 10.5 ms/day) and highlighted individual trajectories "
        "for subjects 308 (steep rise), 309 (flat), and 370."
    ),
    "variance.png": (
        "Two-panel comparison of GLM variance functions V(mu) against the mean mu. Left (counts and positive responses "
        "for mu from 0 to 4): linear mu (Poisson), quadratic mu^2 (Gamma), and steep cubic mu^3 (inverse Gaussian). "
        "Right (proportions on [0, 1]): symmetric arches mu(1 - mu) peaking at 0.25 and mu^2(1 - mu)^2 peaking at 0.0625."
    ),
    "www-forecast.png": (
        "Time-series plot of 100 minutes of server traffic followed by a 20-minute ARIMA forecast: a nearly flat "
        "horizontal point forecast surrounded by shaded prediction intervals that fan wider with lead time."
    ),
    "www-series.png": (
        "Three-panel diagnostic of per-minute server hits: wandering time-series trace over 100 minutes, sample ACF "
        "decaying slowly and crossing negative, and sample PACF dominated by a single large spike at lag 1."
    ),
}


def alt_for(filename: str) -> str:
    """Return the verified accessible alt text for ``filename`` (e.g. ``'pit.png'``)."""
    name = filename.rsplit("/", 1)[-1]
    if name in FIGURE_ALTS:
        return FIGURE_ALTS[name]
    # Multi-page PDF figures (stem-1.png, stem-2.png, ...) fall back to stem.png if needed.
    base = re.sub(r"-\d+\.png$", ".png", name)
    if base in FIGURE_ALTS:
        return FIGURE_ALTS[base]
    raise KeyError(f"Missing accessible alt text in figure_alts.FIGURE_ALTS for {name!r}")
