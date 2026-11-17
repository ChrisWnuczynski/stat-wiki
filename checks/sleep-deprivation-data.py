"""Recompute the numerical examples, exercises and answers for sleep-deprivation-data."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "sleep-deprivation-data.qmd").read_text(encoding="utf-8")
checks = 0
def near(a, b, tol=1e-9):
    global checks
    assert math.isclose(float(a), float(b), rel_tol=tol, abs_tol=tol), (a,b)
    checks += 1
def printed(value, decimals=3):
    global checks
    token = f"{value:.{decimals}f}"
    assert token in article, ("Printed value missing",token)
    checks += 1

# The data are embedded below from the redistributable lme4 sleepstudy dataset.
# https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/lme4/sleepstudy.csv
y=np.array([[249.56, 258.7047, 250.8006, 321.4398, 356.8519, 414.6901, 382.2038, 290.1486, 430.5853, 466.3535], [222.7339, 205.2658, 202.9778, 204.707, 207.7161, 215.9618, 213.6303, 217.7272, 224.2957, 237.3142], [199.0539, 194.3322, 234.32, 232.8416, 229.3074, 220.4579, 235.4208, 255.7511, 261.0125, 247.5153], [321.5426, 300.4002, 283.8565, 285.133, 285.7973, 297.5855, 280.2396, 318.2613, 305.3495, 354.0487], [287.6079, 285.0, 301.8206, 320.1153, 316.2773, 293.3187, 290.075, 334.8177, 293.7469, 371.5811], [234.8606, 242.8118, 272.9613, 309.7688, 317.4629, 309.9976, 454.1619, 346.8311, 330.3003, 253.8644], [283.8424, 289.555, 276.7693, 299.8097, 297.171, 338.1665, 332.0265, 348.8399, 333.36, 362.0428], [265.4731, 276.2012, 243.3647, 254.6723, 279.0244, 284.1912, 305.5248, 331.5229, 335.7469, 377.299], [241.6083, 273.9472, 254.4907, 270.8021, 251.4519, 254.6362, 245.4523, 235.311, 235.7541, 237.2466], [312.3666, 313.8058, 291.6112, 346.1222, 365.7324, 391.8385, 404.2601, 416.6923, 455.8643, 458.9167], [236.1032, 230.3167, 238.9256, 254.922, 250.7103, 269.7744, 281.5648, 308.102, 336.2806, 351.6451], [256.2968, 243.4543, 256.2046, 255.5271, 268.9165, 329.7247, 379.4445, 362.9184, 394.4872, 389.0527], [250.5265, 300.0576, 269.8939, 280.5891, 271.8274, 304.6336, 287.7466, 266.5955, 321.5418, 347.5655], [221.6771, 298.1939, 326.8785, 346.8555, 348.7402, 352.8287, 354.4266, 360.4326, 375.6406, 388.5417], [271.9235, 268.4369, 257.2424, 277.6566, 314.8222, 317.2135, 298.1353, 348.1229, 340.28, 366.5131], [225.264, 234.5235, 238.9008, 240.473, 267.5373, 344.1937, 281.1481, 347.5855, 365.163, 372.2288], [269.8804, 272.4428, 277.8989, 281.7895, 279.1705, 284.512, 259.2658, 304.6306, 350.7807, 369.4692], [269.4117, 273.474, 297.5968, 310.6316, 287.1726, 329.6076, 334.4818, 343.2199, 369.1417, 364.1236]], dtype=float)
# The balanced common design yields an analytic interior REML optimum.
x=np.column_stack([np.ones(10),np.arange(10)]);m,n=y.shape;p=x.shape[1]
C=np.linalg.inv(x.T@x);individual=np.linalg.lstsq(x,y.T,rcond=None)[0].T
beta=individual.mean(axis=0);within=y-individual@x.T
s2=float(np.sum(within**2)/(m*(n-p)))
coefficient_cov=np.cov(individual.T,ddof=1)
G=coefficient_cov-s2*C
Gml=(m-1)/m*coefficient_cov-s2*C
assert y.shape==(18,10);checks+=1
assert np.all(np.linalg.eigvalsh(G)>0);assert np.all(np.linalg.eigvalsh(Gml)>0);checks+=2
for v in beta:printed(v,6)
near(s2,654.9410270722988,tol=1e-11)
near(G[0,0],612.0899386625238,tol=1e-11);near(G[1,1],35.07166049831735,tol=1e-11);near(G[0,1],9.604333316744299,tol=1e-10)
for v in [G[0,0],G[1,1],G[0,1],s2]:printed(v,6)
# Evaluate the Gaussian (restricted) likelihood rather than using optimizer coordinates.
e=y-beta@x.T
from scipy.linalg import cho_factor,cho_solve
def nll(covariance,residual_variance,reml=False):
 V=x@covariance@x.T+residual_variance*np.eye(n);cf=cho_factor(V,lower=True)
 value=m*n*math.log(2*math.pi)+m*2*np.log(np.diag(cf[0])).sum()+np.sum(e*cho_solve(cf,e.T).T)
 if reml:value+=np.linalg.slogdet(m*x.T@cho_solve(cf,x))[1]-p*math.log(2*math.pi)
 return float(value/2)
near(nll(G,s2,True),871.8141359792454,tol=1e-12)
ml=nll(Gml,s2);near(ml,875.9696722315988,tol=1e-12)
# Intercept-only covariance: decompose residuals into within-subject means and orthogonal contrasts.
row_means=e.mean(axis=1);null_s2=float(np.sum((e-row_means[:,None])**2)/(m*(n-1)))
null_G=np.zeros((2,2));null_G[0,0]=float(np.mean(row_means**2)-null_s2/n)
assert null_G[0,0]>0;checks+=1
ml0=nll(null_G,null_s2);near(ml0,897.0393215026129,tol=1e-12)
lr=2*(ml0-ml);printed(-ml,6);printed(-ml0,6);printed(lr,6)
near(lr,42.1392985420282,tol=1e-11)
near(stats.chi2.sf(lr,2)/1e-10,7.072413,tol=1e-6)
printed(beta@[1,5],6);printed(5*beta[1],6)
# Covariance-derived examples use exactly the six-decimal fitted entries displayed in the text.
printed(round(G[0,0],6)+round(s2,6),6)
printed(round(G[0,0],6)+10*round(G[0,1],6)+25*round(G[1,1],6)+round(s2,6),6)
# Subject-level conditional predictions and rounded model output.
V=x@G@x.T+s2*np.eye(n)
blup=np.array([G@x.T@np.linalg.solve(V,ei) for ei in e])
for value in blup[[0,1,15]].ravel():printed(value,3)
printed(beta[1]+blup[1,1],3)
fixed_cov=(G+s2*C)/m
for v in np.sqrt(np.diag(fixed_cov)):printed(v,2)
printed(G[0,1]/math.sqrt(G[0,0]*G[1,1]),2)
for v in [math.sqrt(G[0,0]),math.sqrt(G[1,1]),math.sqrt(s2)]:printed(v,2)
print("sleep-deprivation-data:", checks, "numerical and rendered-value checks passed")
