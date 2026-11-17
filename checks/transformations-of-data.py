"""Recompute numerical examples and exercise answers for transformations-of-data."""
import math
import numpy as np
from scipy import stats, special, linalg, integrate

x=np.array([10,20,40,80]);assert np.allclose(np.diff(np.log(x)),math.log(2))
assert np.median([1,9])==5 and math.isclose(np.median(np.log([1,9])),math.log(3))
assert round(math.e,4)==2.7183 and round(math.exp(1.125),4)==3.0802
assert round(math.exp(.2),4)==1.2214 and round(100*(math.exp(.2)-1),2)==22.14
assert round(math.exp(1.2-.98),4)==1.2461 and round(math.exp(1.2+.98),4)==8.8463
assert math.isclose(math.exp(2*math.log(1.5)),2.25)
assert math.isclose(np.median(np.log([1,4,16])),math.log(np.median([1,4,16])))
from pathlib import Path
import csv
heart=next(p for p in Path('sources/stat1301/data').glob('*.csv') if 'heart' in p.name)
rows=list(csv.DictReader(heart.open()));creat=np.array([float(r['serum_creatinine']) for r in rows])
print('creatinine moment skewness',stats.skew(creat),stats.skew(np.log(creat)),stats.skew(1/creat))
assert len(creat)==299 and round(stats.skew(creat),1)==4.4 and round(stats.skew(np.log(creat)),1)==1.6
assert abs(stats.skew(1/creat))<.15
assert math.exp(2+.5)>math.exp(2) and 1/2>1/3
print("transformations-of-data: numerical checks passed")
