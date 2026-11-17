## Lead context
A unit is the thing being studied. A variable is the characteristic that is written down about it: a number, a count, or a category. {{cite:abs_glossary2023}} (Glossary, “Variable (data item)”) {{cite:dodge2008}} (p. 440)

## Motivating example
In a ward, each patient is a unit. Age, sex, and creatinine are three variables. Age and creatinine are numerical. Sex is a category. The analysis that is legal for creatinine, a mean or a regression on dose, is not legal for sex merely because someone stored sex as 0 and 1. {{cite:dodge2008}} (p. 439) {{cite:dodge2008}} (p. 440) {{cite:abs_glossary2023}} (Glossary, “Numeric variable”)

## Intuition
A variable is a question asked of every unit. "How tall?" and "which ward?" are different questions. The column is the list of answers. The name of the column is the variable. {{cite:abs_glossary2023}} (Glossary, “Data item (or variable)”) {{cite:abs_glossary2023}} (Glossary, “Categorical variable”)

## Definition
A variable is any characteristic, number, or quantity that can be measured or counted. {{cite:abs_glossary2023}} (Glossary, “Variable (data item)”) A quantitative variable has numerical values, such as weight, age, or a count of children. Discrete quantitative variables take distinct whole values. Continuous ones can fall anywhere in an interval, as a length can. {{cite:dodge2008}} (p. 440) {{cite:abs_glossary2023}} (Glossary, “Discrete variable”) {{cite:abs_glossary2023}} (Glossary, “Continuous variable”)

A qualitative, or categorical, variable has categories. Those categories may be unordered, a nominal scale, or ordered, an ordinal scale. {{cite:dodge2008}} (p. 439) {{cite:abs_glossary2023}} (Glossary, “Nominal variable”) {{cite:abs_glossary2023}} (Glossary, “Ordinal variable”)

In a regression the response, or dependent variable, is the one treated as varying with the others, which are the explanatory variables. {{cite:dodge2008}} (p. 161)

## Properties
The level of measurement is a property of the variable, not of the software column. A code is still nominal if the categories have no order. An ordered rating is still ordinal if the gaps between ratings are not lengths. {{cite:dodge2008}} (p. 439) {{cite:abs_glossary2023}} (Glossary, “Qualitative data”) {{cite:abs_glossary2023}} (Glossary, “Quantitative data”)

Data are called quantitative, qualitative, discrete, or continuous according to the variable they record. {{cite:dodge2008}} (p. 150)

## Statistical use
The variable decides the summary. A nominal variable is described by frequencies. A quantitative variable can also be described by a mean. A model then says how one variable changes with others. The parameters of that model are not variables of the units; they are features of the population description. {{cite:dodge2008}} (p. 353) {{cite:abs_glossary2023}} (Glossary, “Frequency”) {{cite:dodge2008}} (p. 412)

## Worked example
Six animals have species codes cat, dog, cat, cat, dog, rabbit, and masses in kilograms 4, 12, 5, 4, 9, 2. Species is categorical. Its frequencies are cat 3, dog 2, rabbit 1. Mass is quantitative. Its mean is (4+12+5+4+9+2)/6 = 36/6 = 6. {{cite:dodge2008}} (p. 208) {{cite:dodge2008}} (p. 440) {{cite:abs_glossary2023}} (Glossary, “Mean”)

**Your turn.** The rabbit's mass was recorded in grams as 2 by mistake and is corrected to 2 kg, which it already is, and a seventh animal is a 3 kg cat. What are the frequency of cat and the mean mass?

::: {.callout-tip collapse="true" title="Answer"}
Cats now number 4 out of 7. The masses are 4, 12, 5, 4, 9, 2, and 3. Their total is 39, so the mean is 39/7.
:::

## Common misconceptions
A variable is not a unit and not a parameter. The column of masses varies from animal to animal. The population mean of mass is a single unknown number, a parameter, even though it is estimated by a variable's sample mean. {{cite:dodge2008}} (p. 412) {{cite:abs_glossary2023}} (Glossary, “Statistic”)

Storing a category as a number does not create a quantitative variable. {{cite:dodge2008}} (p. 439) {{cite:abs_glossary2023}} (Glossary, “Nominal variable”)

## Assumptions and limits
Calling a variable continuous is a modelling choice. A recorded length is discrete at the resolution of the instrument. The continuous description is useful when that rounding is fine relative to the variation under study. {{cite:dodge2008}} (p. 440) {{cite:abs_glossary2023}} (Glossary, “Continuous variable”)

## Connections
[Levels of measurement](levels-of-measurement.qmd) name the scale. An [explanatory variable](explanatory-variable.qmd) and a [response variable](response-variable.qmd) are roles in a model, not scales. A [random variable](random-variable.qmd) is the probability-language version of a variable whose value is not fixed in advance. {{cite:dodge2008}} (p. 353) {{cite:abs_glossary2023}} (Glossary, “Variable (data item)”)

## History
Once records were organised by characteristics of units, it became possible to ask how one characteristic moves with another. That question is the start of regression and of the models that followed it. {{cite:dodge2008}} (p. 353) {{cite:dodge2008}} (p. 518)
