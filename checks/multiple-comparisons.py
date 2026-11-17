"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

close(1-.95**10,.4012630608);close(.05/10,.005);close(.05/4,.0125);close(4*.009,.036)
assert math.comb(5,2)==10 and math.comb(6,2)==15
corn=np.array([[46.2,51.9,48.7],[49.2,58.6,57.4],[60.3,58.7,60.4],[48.9,51.4,44.6],[52.5,54,49.3]])
means=corn.mean(1);mse=((corn-means[:,None])**2).sum()/10
close(means,[48.9333333333,55.0666666667,59.8,48.3,51.9333333333]);close(mse,10.568)
q=stats.studentized_range.ppf(.95,5,10);close(q,4.6542929979)
h=q*math.sqrt(10.57/3);close(h,8.7363612903)
# Exact source-data MSE is 10.568; rounded 10.57 gives the same hundredth endpoints.
h2=q*math.sqrt(mse/3)
expected=[[-14.87,2.60],[-19.60,-2.13],[-8.10,9.37],[-11.74,5.74],[-13.47,4.00],[-1.97,15.50],[-5.60,11.87],[2.76,20.24],[-.87,16.60],[-12.37,5.10]]
from itertools import combinations
calculated=[];significant=[]
for i,j in combinations(range(5),2):
 lo,hi=means[i]-means[j]+np.array([-h2,h2]);calculated.append([lo,hi])
 if lo>0 or hi<0:significant.append((i+1,j+1))
close(np.round(calculated,2),expected,tol=1e-9)
assert significant==[(1,3),(3,4)]
print("multiple-comparisons: numerical checks passed")
