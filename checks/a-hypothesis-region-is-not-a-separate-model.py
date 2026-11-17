"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='a-hypothesis-region-is-not-a-separate-model'
NEEDLES=['0.88671875', '7.827586', '0.563140']

from scipy.integrate import quad
post=stats.beta.sf(.5,8,4)
assert np.isclose(post,227/256) and np.isclose(1-post,29/256)
assert np.isclose(post/(1-post),227/29)
m0=stats.binom.pmf(7,10,.5);m1=quad(lambda theta:stats.binom.pmf(7,10,theta),0,1)[0]
assert np.isclose(m1,1/11) and np.isclose(m0/m1,165/128)
assert np.isclose((m0/m1)/(1+m0/m1),165/293)
assert np.isclose(stats.gamma.cdf(10,a=189,scale=1/21),.9329838080545596)
assert 177+12==189 and 20+1==21 and 189/21==9 and 177/20==8.85
assert stats.gamma.ppf(.975,a=189,scale=1/21)>10
assert stats.gamma.ppf(.025,a=189,scale=1/21)<10

# Integrate the two conditional uniform priors independently of the Beta CDF.
a=quad(lambda t:2*stats.binom.pmf(7,10,t),.5,1)[0];b=quad(lambda t:2*stats.binom.pmf(7,10,t),0,.5)[0]
assert np.isclose(a/b,227/29)
assert (2*3-1)==5 and (2-1)+(3-1)==3

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
