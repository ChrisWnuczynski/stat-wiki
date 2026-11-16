# Five-number summary and boxplot

Type: concept. Rank 294. Tier: lighter.

## Facts

- **Checked:** Dodge (2008), printed p. 55: a box plot shows the median, the first and third quartiles, and the minimum and maximum; the central rectangle is the interquartile range. Printed p. 266: interquartile range equals Q3 minus Q1. Printed p. 440: the $j$th quartile uses position $j(n+1)/4$, with linear interpolation between adjacent order statistics.
- **Checked:** NIST/SEMATECH e-Handbook §1.3.3.7, “Box plots with fences”: inner fences at the quartiles plus or minus 1.5 times the interquartile range, whiskers to the most extreme observation inside those fences, and an outer fence at 3 times the interquartile range.
- **Checked by code:** For $4,7,8,9,12,15,40$ the $(n+1)/4$ quartiles are 7, 9, 15 and the upper fence is 27. For $2,5,6,8,9,11,30$ they are 5, 8, 11 and the upper fence is 20. The ten carton hinges are 1.035, 1.046, 1.077.
- **Assumed:** The serum creatinine quartiles 0.90 and 1.40 are the software summary already printed with the figure. They were not recomputed with Dodge’s formula.
- **Disputed:** Dodge dates the box plot to Tukey in 1972. Tukey’s 1977 book was not opened, so that date is reported only as Dodge’s statement and is not repeated as a page of Tukey.

## Sources read

1. Dodge (2008), pp. 55, 266, 440.
2. NIST/SEMATECH e-Handbook §1.3.3.7, https://www.itl.nist.gov/div898/handbook/eda/section3/boxplot.htm
