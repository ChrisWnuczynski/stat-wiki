import numpy as np
from scipy import stats
print('--- Latin square your turn (4x4 cyclic, rows=day, cols=operator)')
L=[list('ABCD'),list('BCDA'),list('CDAB'),list('DABC')]
row=[2,0,-1,-1]; col=[1,-1,0,0]; trt=dict(A=3,B=-1,C=0,D=-2)
e=np.array([[1,-1,0,0],[0,1,-1,0],[-1,0,1,0],[0,0,0,0]])
Y=np.array([[50+row[i]+col[j]+trt[L[i][j]]+e[i,j] for j in range(4)] for i in range(4)])
print(Y); G=Y.mean()
tm={t:np.mean([Y[i,j] for i in range(4) for j in range(4) if L[i][j]==t]) for t in 'ABCD'}
SSR=4*((Y.mean(1)-G)**2).sum(); SSC=4*((Y.mean(0)-G)**2).sum(); SST=4*sum((v-G)**2 for v in tm.values()); SSTot=((Y-G)**2).sum(); SSE=SSTot-SSR-SSC-SST
print('grand',G,'trt means',tm,'SSrow',SSR,'SScol',SSC,'SStrt',SST,'SSE',SSE,'MSE',SSE/6,'F',SST/3/(SSE/6),'p',stats.f.sf(SST/3/(SSE/6),3,6))
print('--- Crossover your turn')
AB=np.array([[50,62],[48,58],[55,65],[47,59]]);BA=np.array([[52,61],[45,56],[50,59],[53,64]])
DX=AB[:,0]-AB[:,1];DY=BA[:,0]-BA[:,1];print('DX',DX,DX.mean(),'DY',DY,DY.mean())
print('tau_hat (A-B)',(DX.mean()-DY.mean())/2,'period1-period2',(DX.mean()+DY.mean())/2)
naive=np.concatenate([AB[:,0]-AB[:,1], BA[:,1]-BA[:,0]]); print('naive A-B mean',naive.mean(), stats.ttest_1samp(naive,0))
print(stats.ttest_ind(DX,DY))
print('--- crossover efficiency: N_par/N_cross = 2(1+sb2/se2); sb2/se2=2 ->',2*(1+2))
print('--- Split-plot your turn (4 fields, irrigation I1 fields 1-2, I2 fields 3-4; F1,F2 per field)')
Y=np.array([[10,14],[12,18],[15,19],[19,25]],float); irr=np.array([1,1,2,2])
tot=Y.sum(1); diff=Y[:,1]-Y[:,0]; print('totals',tot,'diffs',diff)
G=Y.mean(); SSTot=((Y-G)**2).sum()
SSWP=2*((Y.mean(1)-G)**2).sum(); im={k:Y[irr==k].mean() for k in (1,2)}; SSI=4*sum((v-G)**2 for v in im.values()); SSWPE=SSWP-SSI
fm=Y.mean(0); SSF=4*((fm-G)**2).sum(); cell={(k,j):Y[irr==k,j].mean() for k in (1,2) for j in (0,1)}
SSIF=2*sum((cell[k,j]-im[k]-fm[j]+G)**2 for k in (1,2) for j in (0,1)); SSSPE=SSTot-SSWP-SSF-SSIF
print('irr means',im,'fert means',fm,'SSI',SSI,'SSWPE',SSWPE,'(df 2) MS',SSWPE/2,'F_I',SSI/(SSWPE/2),'p',stats.f.sf(SSI/(SSWPE/2),1,2))
print('SSF',SSF,'SSIF',SSIF,'SSSPE',SSSPE,'(df 2) MS',SSSPE/2,'F_F',SSF/(SSSPE/2),'p',stats.f.sf(SSF/(SSSPE/2),1,2),'F_IF',SSIF/(SSSPE/2))
print('t on diffs by irrigation', stats.ttest_ind(diff[irr==1],diff[irr==2]), 'mean diff',diff.mean(), stats.ttest_1samp(diff,0))
print('t on totals', stats.ttest_ind(tot[irr==1],tot[irr==2]))
print('--- 2^3 your turn (standard order)')
y=np.array([20,30,22,32,21,39,23,41],float)
X=np.array([[(-1)**(1-((r>>f)&1)) for f in range(3)] for r in range(8)]); A,B,C=X.T
for nm,c in [('A',A),('B',B),('AB',A*B),('C',C),('AC',A*C),('BC',B*C),('ABC',A*B*C)]: print(nm,'total effect (high-low)',c@y/4)
print('A effect at C low', (30+32-20-22)/2,'at C high',(39+41-21-23)/2)
