"""Independent calculations and generated-output checks for this article."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
import numpy as np
from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import pdist
x=np.array([0,2,3,10])[:,None]
for name,heights in {'single':[1,2,7],'complete':[1,3,10],'average':[1,2.5,25/3]}.items():
 Z=linkage(pdist(x),method=name)
 assert np.allclose(Z[:,2],heights)
 assert len(Z)==len(x)-1
assert np.mean([10-2,10-3])==7.5
x=np.array([1,2,6,8,15])[:,None]
for name,heights in {'single':[1,2,4,7],'complete':[1,2,7,14],'average':[1,2,5.5,10.75]}.items():
 assert np.allclose(linkage(pdist(x),method=name)[:,2],heights)

source=(ROOT/"research/content/agglomerative-and-divisive-clustering.md").read_text()
article=(ROOT/"articles/agglomerative-and-divisive-clustering.qmd").read_text().split("## See also",1)[0]
for needle in ['25/3', '7.5', '2.5']:
    assert needle in source and needle in article, needle
assert len(re.findall(r"\{\{cite:[^}]+\}\}", source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)\}\}",source)))>=2
assert "Your turn" in article and 'collapse="true" title="Answer"' in article
assert "## Check yourself {#check-yourself}" in article
print("agglomerative-and-divisive-clustering: calculations and article checks passed")
