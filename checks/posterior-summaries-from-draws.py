"""Check all numeric claims in the new draw-summary examples."""
import math
import statistics
from pathlib import Path

first=[1,2,2,3,7]
assert len(first)==5 and sum(first)==15
assert statistics.mean(first)==3
assert sum((x-3)**2 for x in first)==22
assert statistics.variance(first)==5.5
assert sum(x>2 for x in first)==2
assert sum(x>2 for x in first)/5==.4
assert statistics.median(first)==2
assert math.isclose(math.sqrt(5.5/5),1.04881,abs_tol=5e-6)
assert math.isclose(math.sqrt(5.5),2.34521,abs_tol=5e-6)
second=[0,1,2,2,5]
assert len(second)==5 and sum(second)==10
assert statistics.mean(second)==2
assert sum((x-2)**2 for x in second)==14
assert statistics.variance(second)==3.5
assert statistics.median(second)==2
assert sum(x>1 for x in second)==3
assert sum(x>1 for x in second)/5==.6
assert math.isclose(math.sqrt(3.5/5),.83666,abs_tol=5e-6)
root=Path(__file__).resolve().parents[1]
source=(root/'research/content/posterior-summaries-from-draws.md').read_text()
for number in ('1.04881','2.34521','0.83666','5.5','3.5','0.4','0.6'):
    assert number in source
page=root/'articles/posterior-summaries-from-draws.qmd'
if page.exists():
    rendered=page.read_text()
    for preserved in ('example-q-25','example-c-11','q-42.qmd','ex-norm-both.qmd','title="Proof"'):
        assert preserved in rendered
