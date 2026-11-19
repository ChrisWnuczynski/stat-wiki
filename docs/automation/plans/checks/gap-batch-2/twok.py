import numpy as np
from scipy import stats
labels=['(1)','a','b','ab','c','ac','bc','abc']
y=np.array([4.388,2.831,4.360,3.107,4.330,3.268,4.336,2.471])  # Oehlert Table 10.4 p.240
def yates(v):
    cols=[v.copy()]
    for _ in range(int(np.log2(len(v)))):
        p=cols[-1]; cols.append(np.concatenate([p[0::2]+p[1::2], p[1::2]-p[0::2]]))
    return cols
cols=yates(y); print('col3',np.round(cols[-1],3)); eff=cols[-1]/8; print('effects (Oehlert scale, /2^k)',np.round(eff,3))
names=['Mean','A','B','AB','C','AC','BC','ABC']
# total effect convention (high minus low mean) = col/2^(k-1)
print('total effects (/4)',dict(zip(names[1:],np.round(cols[-1][1:]/4,4))))
# Lenth on Oehlert-scale effects
e=np.abs(eff[1:]); s0=1.5*np.median(e); keep=e[e<=2.5*s0]; pse=1.5*np.median(keep)
print('median|e|',np.median(e),'s0',s0,'cut',2.5*s0,'median kept',np.median(keep),'PSE',pse)
t=eff[1]/pse; d=7/3; print('t_A',t,'p two-sided',2*stats.t.sf(abs(t),d))
# Oehlert rounds: median .068, cutoff 2.5*.068 = .17 -> note Oehlert uses 2.5*median? check
print('2.5*median',2.5*np.median(e))
# half-normal scores
from scipy.stats import norm
m=7; i=np.arange(1,8); hn=norm.ppf(0.5+0.5*(i-0.5)/m); order=np.argsort(e); print('half-normal order',[names[1:][k] for k in order], np.round(hn,3))
# contrast matrix check
X=np.array([[(-1)**(1-((r>>f)&1)) for f in range(3)] for r in range(8)])
A,B,C=X.T; M=np.column_stack([A,B,A*B,C,A*C,B*C,A*B*C]); print('orthogonal:',np.allclose(M.T@M,8*np.eye(7)))
print('direct contrast/8 matches yates',np.allclose(M.T@y/8,eff[1:]))
