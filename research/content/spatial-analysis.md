## Lead context

A pollutant, a house price, or a disease count is not only a number. It is a number at a place, and places near each other tend to look alike. Spatial analysis is the statistical treatment of that fact. The observations carry coordinates, or they are areas that share borders, and the methods ask whether the pattern on the map is more than a random assignment of the same values. Geology, epidemiology, ecology, and official small-area statistics all hand the subject this kind of data.

## Definition — Scope

Spatial analysis, or spatial statistics, is the analysis of observations distributed in space, with explicit attention to their locations and to dependence between neighbours. Two observations close together are expected to resemble each other more than two that are far apart. The data may come from geology, earth science, image analysis, epidemiology, agriculture, ecology, astronomy, or forestry. Sometimes the locations themselves are random, as in a point pattern; sometimes they are fixed areas or fixed sample sites. The subject includes exploring that dependence and testing it, not only drawing the map.{{cite:dodge2008}} (p. 501)

Geostatistics is the branch aimed at geology and hydrology, and more generally at variables measured at known coordinates. The modelling slogan recorded for it is local models, assembled into a global analysis, used to describe and forecast how a variable is distributed in space and, when needed, in time. The word was used by Hart in 1954 in a geographical context. Areal data, the other large class, are values on regions. Spatial autocorrelation is the dependence among those values. Positive autocorrelation means similar values cluster. Negative autocorrelation means dissimilar values sit next to each other.{{cite:dodge2008}} (p. 229){{cite:moraga2023}} (Ch. 8)

## Statistical use

Ordinary summaries still apply. Histograms, means, and correlations describe the values while ignoring the map, and that is often the wrong last step. For several variables at once, scatterplots and correlation remain available, but they do not use the coordinates. Tools that do use them include the [variogram](variogram.qmd), which describes how variation grows with separation, a [spatial Poisson process](spatial-poisson-process.qmd) for event locations, and indices of areal association. [Moran's I](morans-i.qmd) and Geary's $C$ summarise whether neighbouring areas are more alike than a random reassignment of the same numbers would suggest. Weights $w_{ij}$ encode who is a neighbour. The index is then a weighted product of deviations from the mean, scaled by the total variation. A map of local indices shows where the clustering sits, which a single global number cannot.{{cite:moraga2023}} (Ch. 8){{cite:rey_gds2020}} (Ch. 8, §8.3.3){{cite:dodge2008}} (p. 501)

Tobler's statement that near things are more related than distant things is the qualitative form of the same idea. It is not a theorem. It is the reason a model that treats areas as independent is often incredible for these data.{{cite:moraga2023}} (Ch. 8)

## History

Edmond Halley, in 1686, overlaid wind directions and the monsoon on a map and tried to explain them. The statistical models came later. Fisher's work at Rothamsted in the 1920s and 1930s set out randomisation, blocking, and replication for field experiments, which are spatial designs even though their aim is agricultural comparison rather than a map of dependence. Geostatistics as a named application grew up around spatial interpolation for natural resources. Areal indices of autocorrelation, among them Moran's $I$, gave a test for the pattern on a choropleth map.{{cite:dodge2008}} (pp. 229, 501){{cite:moraga2023}} (Ch. 8)

## Connections

Spatial analysis neighbours [time series](time-series.qmd), which is dependence along one ordered index, and [official statistics](official-statistics.qmd), which publishes many of the areal counts. Epidemiology uses the map when an exposure is a place, as in a water supply. A pretty choropleth can show a pattern that is only the pattern of the population. Rates, not raw counts, are the values that belong in an autocorrelation index when the scientific question is risk. Dependence also means that a standard error computed as if the areas were a simple random sample is usually too small.{{cite:dodge2008}} (p. 501){{cite:moraga2023}} (Ch. 8)
