"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
caf=np.array([17,22,21,16,6,-2,27,15,16,20],dtype=float)
dec=np.array([4,10,7,-9,5,4,5,7,6,12],dtype=float)
a=stats.ttest_ind(caf,dec,equal_var=False,alternative='greater')
b=stats.ttest_ind(caf,dec,equal_var=True,alternative='greater')
assert f'{a.statistic:.4f}'=='3.3752'
assert f'{a.df:.2f}'=='15.74'
assert f'{a.pvalue:.6f}'=='0.001966'
assert f'{b.pvalue:.6f}'=='0.001686'
assert np.isclose(caf.mean()-dec.mean(),10.7)
se=math.sqrt(caf.var(ddof=1)/10+dec.var(ddof=1)/10)
ci=10.7+np.array([-1,1])*stats.t.ppf(.975,a.df)*se
assert [round(v,1) for v in ci]==[4.0,17.4]
se2=math.sqrt(Fraction(202,105));assert f'{3/se2:.6f}'=='2.162919'
assert f'{2/se2:.6f}'=='1.441946'
assert f'{2.5/se2:.6f}'=='1.802432'
assert f'{2*stats.t.sf(2.5/se2, 14):.6f}'=='0.093041'
assert (5-1)/2==2
sew=math.sqrt(4/6+9/10)
vw=(4/6+9/10)**2/((4/6)**2/5+(9/10)**2/9)
assert f'{sew:.6f}'=='1.251666'
assert f'{vw:.6f}'=='13.720497'
assert f'{3/sew:.6f}'=='2.396806'
assert f'{2*stats.t.sf(3/sew, vw):.6f}'=='0.031380'
sep=math.sqrt(((9*4+9*16)/18)*(1/10+1/10))
dfw=(4/10+16/10)**2/((4/10)**2/9+(16/10)**2/9)
assert f'{sep:.6f}'=='1.414214'
assert f'{dfw:.6f}'=='13.235294'
assert f'{stats.t.sf(2/sep, 18):.6f}'=='0.087182'
assert f'{stats.t.sf(2/sep, dfw):.6f}'=='0.090195'
assert f'{stats.t.ppf(.975, 14)*se2:.6f}'=='2.974850'

text = (ROOT / "articles" / "two-sample-t-test.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert "1.802432" in text
assert "0.093041" in text
assert text.count('class="cite-ref"') >= 5
print("two-sample-t-test: all recomputed claims and generated-text checks passed")
