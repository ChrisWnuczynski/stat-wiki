"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='two-factor-analysis-of-variance'
body=(ROOT/"articles"/f'{SLUG}.qmd').read_text().split('## See also',1)[0]
def close(a,b,atol=1e-10):
    aa,bb,tt=np.broadcast_arrays(np.asarray(a),np.asarray(b),np.asarray(atol))
    for x,y,tol in zip(aa.flat,bb.flat,tt.flat):
        np.testing.assert_allclose(x,y,rtol=0,atol=float(tol))
def shown(*values):
    for value in values:
        assert value in body, (SLUG,value)
def finish():
    assert '**Your turn.**' in body
    assert '## Check yourself' in body
    assert body.count('data-cite-key=')>=5
    assert len(set(re.findall(r'data-cite-key="([^" ]+)"',body)))>=2
    assert not any(ord(c)<32 and c not in '\n\r\t' for c in body)
    print(SLUG+': numerical examples and article checks passed')
import ast
z=np.array([[[8,10],[12,14]],[[11,13],[19,21]]],float)
def balanced(z):
 a,b,r=z.shape;cell=z.mean(2);row=cell.mean(1);col=cell.mean(0);grand=cell.mean()
 interaction=cell-row[:,None]-col[None,:]+grand
 return np.array([b*r*np.sum((row-grand)**2),a*r*np.sum((col-grand)**2),r*np.sum(interaction**2),np.sum((z-cell[:,:,None])**2)]),interaction
ss,interaction=balanced(z);close(ss,[50,72,8,8]);close(interaction,[[1,-1],[-1,1]])
close(ss.sum(),np.sum((z-z.mean())**2));close(ss.sum(),138)
close(ss[:3]/(ss[3]/4),[25,36,4]);close(stats.f.sf([25,36,4],1,4),[.00749,.00388,.11612],.000005)
close(balanced(z+5)[0],ss);close((z+5).mean(),18.5)
# Recompute the full copied wheat dataset, including additive and one-region analyses.
m=re.search(r'yield <- c\((.*?)\)\nfertilizer',body,re.S);assert m
w=np.array([float(t) for t in m.group(1).replace('\n',' ').split(',')]).reshape(3,4,3)
sw,_=balanced(w);dfs=np.array([2,3,6,24]);fw=sw[:3]/dfs[:3]/(sw[3]/24)
close(sw[[1,0,2,3]],[29.340,8.560,.695,20.885],.0006)
close(fw[[1,0,2]],[11.2388,4.9182,.1332],.00006)
close(stats.f.sf(fw[[1,0,2]],[3,2,6],24),[8.451e-5,.01622,.99067],.000006)
add_mse=(sw[2]+sw[3])/30;close(add_mse,.719,.0005)
add_f=sw[:2]/dfs[:2]/add_mse;close(add_f[[1,0]],[13.6,5.95],.05)
close(stats.f.sf(add_f[[1,0]],[3,2],30),[9e-6,.007],[1e-6,.0005])
close(w.mean((0,2))[[0,3]],[8.70,10.96],.005)
close(w.mean((1,2)),[9.91,10.61,9.42],.005)
region=w[:,0,:];between=3*np.sum((region.mean(1)-region.mean())**2);within=np.sum((region-region.mean(1)[:,None])**2)
fr=(between/2)/(within/6);close(fr,1.87,.005);close(stats.f.sf(fr,2,6),.23,.005)
# Recover the crop raw data used for the preserved figure and refit its summaries.
fig=(ROOT/'sources/stat1301/figures/make_figures.py').read_text()
cm=re.search(r'c = np.array\(\[(.*?)\]\).reshape\(2, 3, 3\).mean\(2\)',fig,re.S);assert cm
crop=np.array(ast.literal_eval('['+cm.group(1)+']')).reshape(2,3,3)
close(crop.mean(2),[[3.20,2.87,5.70],[6.77,9.01,8.16]],.005)
sc,_=balanced(crop);fc=(sc[2]/2)/(sc[3]/12)
close(fc,574,.5);tt=stats.ttest_ind(crop[0].ravel(),crop[1].ravel(),equal_var=True)
close(tt.statistic,-7.30,.005);close(tt.pvalue,1.8e-6,.05e-6)
close(np.array([6.77,9.01,8.16])-np.array([3.20,2.87,5.70]),[3.57,6.14,2.46])
shown('138','0.00749','0.00388','0.11612','da-interaction.png','574','1.87')

# Zero-sum interaction effect is the B-difference contrast divided by 4.
close((8-4)/4,1); close(2*4*1**2,8)
finish()
