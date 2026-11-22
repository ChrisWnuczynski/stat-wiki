import numpy as np
from scipy import stats
# Wellek & Blettner (2012) Box 2, p.279: formoterol (A) vs salbutamol (B), PEF
X1=np.array([310,310,370,410,250,380,330]);X2=np.array([270,260,300,390,210,350,365])  # AB group, periods 1,2
Y1=np.array([370,310,380,290,260,90]);Y2=np.array([385,400,410,320,340,220])           # BA group
DX,DY,CX,CY=X1-X2,Y1-Y2,X1+X2,Y1+Y2
print('mean DX',DX.mean(),'mean DY',DY.mean())
print('treatment test (D):',stats.ttest_ind(DX,DY))
print('carryover pre-test (C):',stats.ttest_ind(CX,CY))
m,n=7,6; tau=(DX.mean()-DY.mean())/2; per=(DX.mean()+DY.mean())/2
sp2=((m-1)*DX.var(ddof=1)+(n-1)*DY.var(ddof=1))/(m+n-2); se=0.5*np.sqrt(sp2*(1/m+1/n)); q=stats.t.ppf(.975,m+n-2)
print('tau_hat A-B',tau,'se',se,'95% CI',tau-q*se,tau+q*se,'period1-period2',per)
