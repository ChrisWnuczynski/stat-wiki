import numpy as np
from scipy import stats
# Oehlert (2010) Table 13.2, p.327: rows=period, cols=subject; A solution, B tablet, C capsule
L=[['A','C','B'],['C','B','A'],['B','A','C']]
Y=np.array([[1799,2075,1396],[1846,1156,868],[2147,1777,2291]],float)
g=3; G=Y.mean()
SSR=g*((Y.mean(1)-G)**2).sum(); SSC=g*((Y.mean(0)-G)**2).sum()
tm={t:np.mean([Y[i,j] for i in range(3) for j in range(3) if L[i][j]==t]) for t in 'ABC'}
SST_=g*sum((m-G)**2 for m in tm.values()); SSTot=((Y-G)**2).sum(); SSE=SSTot-SSR-SSC-SST_
dfe=(g-1)*(g-2); MSE=SSE/dfe; F=SST_/2/MSE
print('grand',G,'trt means',tm); print('SS rows(period)',SSR,'cols(subject)',SSC,'trt',SST_,'err',SSE,'dfe',dfe,'MSE',MSE)
print('F',F,'p',stats.f.sf(F,2,dfe),'F crit .05',stats.f.ppf(.95,2,dfe))
# what if analysed as RCB on subjects only (ignore period)
SSE_rcb=SSTot-SSC-SST_; dfr=4; F2=SST_/2/(SSE_rcb/dfr); print('ignore period: MSE',SSE_rcb/dfr,'F',F2,'p',stats.f.sf(F2,2,dfr))
# one-way CRD
SSE_crd=SSTot-SST_; F3=SST_/2/(SSE_crd/6); print('one-way: F',F3,'p',stats.f.sf(F3,2,6))
# Tukey HSD
q=stats.studentized_range.ppf(.95,3,dfe); print('q',q,'MSD',q*np.sqrt(MSE/3))
# counting: standard squares; 6x6 transformation sets per Fisher
import math; print('6! =',math.factorial(6))
