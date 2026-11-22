import numpy as np, itertools
from scipy import stats
wp=[(360,{'C2':73,'C3':83,'C1':67,'C4':89}),(370,{'C1':65,'C3':87,'C4':86,'C2':91}),
    (380,{'C3':147,'C1':155,'C2':127,'C4':212}),(380,{'C4':153,'C3':90,'C2':100,'C1':108}),
    (370,{'C4':150,'C1':140,'C3':121,'C2':142}),(360,{'C1':33,'C4':54,'C2':8,'C3':46})]
C=['C1','C2','C3','C4']; T=[360,370,380]
Y=np.array([[d[c] for c in C] for _,d in wp],float); temp=np.array([t for t,_ in wp])
a,b,n=3,4,2; N=24; g=Y.mean()
wpm=Y.mean(1); tm={t:Y[temp==t].mean() for t in T}; cm=Y.mean(0)
cell={(t,j):Y[temp==t,j].mean() for t in T for j in range(4)}
SST=((Y-g)**2).sum()
SSA=b*n*sum((tm[t]-g)**2 for t in T)
SSWP=b*((wpm-g)**2).sum(); SSWPE=SSWP-SSA
SSB=a*n*((cm-g)**2).sum()
SSAB=n*sum((cell[t,j]-tm[t]-cm[j]+g)**2 for t in T for j in range(4))
SSSPE=SST-SSWP-SSB-SSAB
df=dict(A=2,WPE=3,B=3,AB=6,SPE=9)
MS=dict(A=SSA/2,WPE=SSWPE/3,B=SSB/3,AB=SSAB/6,SPE=SSSPE/9)
print('means temp',tm,'coat',dict(zip(C,cm)),'grand',g)
for k,v in MS.items(): print(k,round(v*df[k],3),df[k],round(v,3))
FA=MS['A']/MS['WPE'];FB=MS['B']/MS['SPE'];FAB=MS['AB']/MS['SPE']
print('split-plot F/p: A',FA,stats.f.sf(FA,2,3),' B',FB,stats.f.sf(FB,3,9),' AB',FAB,stats.f.sf(FAB,6,9))
# naive CRD two-way with replication: error = WPE+SPE pooled, 12 df
MSE=(SSWPE+SSSPE)/12
for nm,ss,d in [('A',SSA,2),('B',SSB,3),('AB',SSAB,6)]:
    F=ss/d/MSE; print('naive',nm,F,stats.f.sf(F,d,12))
print('SST',SST)
