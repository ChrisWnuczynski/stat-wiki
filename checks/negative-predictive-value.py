"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='negative-predictive-value'
NEEDLES=['0.986301', '0.888889', '0.013699']

npv=lambda pi,se,sp:sp*(1-pi)/(sp*(1-pi)+(1-se)*pi)
assert np.isclose(npv(.1,.9,.8),72/73)
assert np.isclose(npv(.5,.9,.8),8/9)
assert np.isclose(10/730,1/73)
assert 90/(90+180)==1/3 and np.isclose(.1/.8,1/8)
assert np.isclose(npv(.005,.95,.95),.9997355896351138)
assert np.isclose(npv(.02,.98,.9),.9995466908431551)
assert np.isclose(.98*.02/(.98*.02+.1*.98),1/6)
pi,se,sp=s.symbols('pi se sp',positive=True)
f=sp*(1-pi)/(sp*(1-pi)+(1-se)*pi)
assert s.simplify(s.diff(f,pi)+sp*(1-se)/(sp*(1-pi)+(1-se)*pi)**2)==0

if '--math-only' not in sys.argv:
 source=(ROOT/'research/content'/f'{SLUG}.md').read_text()
 article=(ROOT/"articles"/f'{SLUG}.qmd').read_text().split('## See also',1)[0]
 for needle in NEEDLES:assert needle in article,(SLUG,needle)
 assert len(re.findall(r'\{\{cite:[^}]+\}\}',source))>=5
 assert len(set(re.findall(r'\{\{cite:([^}]+)\}\}',source)))>=2
 assert 'Your turn' in article and 'collapse="true" title="Answer"' in article
 assert '## Check yourself {#check-yourself}' in article
 section=article.split('## Check yourself {#check-yourself}',1)[1].split('\n## ',1)[0]
 ids=re.findall(r'(?m)^### .*\{#self-check-([^}]+)\}',section)
 assert len(ids) in (2,3) and section.count('collapse="true" title="Answer"')==len(ids),(SLUG,ids)
 for qid in ids:assert (ROOT/'questions'/f'{qid}.qmd').exists()
 for ans in re.findall(r'::: \{[^\n]*title="Answer"[^\n]*\}\n(.*?)\n:::',article,re.S):assert 'cite-ref' not in ans
print(SLUG+': independent calculations and article checks passed')
