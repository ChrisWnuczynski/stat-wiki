"""Recompute numerical examples and exercise answers for summary-statistics."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'summary-statistics'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

x=np.array([1,2,3,4,10]);y=5+10*x
assert x.mean()==4 and np.median(x)==3 and np.ptp(x)==9
assert list(np.quantile(x,[0,.25,.5,.75,1]))==[1,2,3,4,10]
assert x.var(ddof=1)==12.5 and round(x.std(ddof=1),3)==3.536
assert y.mean()==45 and np.median(y)==35 and y.var(ddof=1)==1250 and np.ptp(y)==90
assert np.diff(np.quantile(y,[.25,.75]))[0]==20 and round(y.std(ddof=1),3)==35.355
z=np.array([2,2,5,7]);assert z.mean()==4 and np.median(z)==3.5 and np.ptp(z)==5 and z.var(ddof=1)==6
assert round(19/11.89,3)==1.598
assert round(2*stats.norm.ppf(.75),3)==1.349
import csv
files=list(Path('sources/stat1301/data').glob('*'))
heart=next(p for p in files if 'heart' in p.name and p.suffix=='.csv')
rows=list(csv.DictReader(heart.open()));age=np.array([float(r['age']) for r in rows])
assert len(age)==299 and round(age.mean(),2)==60.83 and np.median(age)==60
assert np.allclose(np.quantile(age,[0,.25,.75,1]),[40,51,70,95]) and round(age.std(ddof=1),2)==11.89
assert 12-5==7 and 40-10==30 and 19-14==5

assert round(19/11.9,1)==1.6

# Match computed worked-example and practice results to their generated text.
assert f"sample variance ${x.var(ddof=1):g}$ and standard deviation ${x.std(ddof=1):.3f}$" in worked
assert f"standard deviation approximately ${y.std(ddof=1):.3f}$" in worked
assert f"sample variance is ${y.var(ddof=1):g}$" in worked
assert f"sample variance $18/3={z.var(ddof=1):g}$" in answer and f"range is ${np.ptp(z):g}$" in answer
print("summary-statistics: numerical checks passed")
