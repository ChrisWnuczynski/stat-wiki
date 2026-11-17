from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
import numpy as np
x=np.array([0.,2.,8.,10.]);mu=np.array([0.,8.])
z=((x[:,None]-mu)**2).argmin(axis=1)
J=lambda z,m:sum((x[i]-m[z[i]])**2 for i in range(len(x)))
assert J(z,mu)==8
new=np.array([x[z==k].mean() for k in range(2)])
assert np.array_equal(new,[1.,9.]) and J(z,new)==4
assert np.array_equal(((x[:,None]-new)**2).argmin(axis=1),z)
assert 2*(1-0)**2+2*(9-8)**2==4
assert (0-3)**2+(2-3)**2==10 and (0-1)**2+(2-1)**2==2
printed=['8','4','10','2']

# Check the rectangular counterexample to global optimality in the intuition.
x=np.array([[0.,0.],[0.,1.],[10.,0.],[10.,1.]])
m0=np.array([[0.,0.],[0.,1.]])
z=np.argmin(((x[:,None,:]-m0[None,:,:])**2).sum(axis=2),axis=1)
loss=lambda m:((x-m[z])**2).sum()
assert loss(m0)==200
m1=np.array([x[z==j].mean(axis=0) for j in range(2)])
assert np.array_equal(m1,[[5.,0.],[5.,1.]]) and loss(m1)==100
assert np.array_equal(np.argmin(((x[:,None,:]-m1[None,:,:])**2).sum(axis=2),axis=1),z)
assert abs(np.sqrt(26)-5.10)<.005
mv=np.array([[0.,.5],[10.,.5]])
assert ((x-mv[[0,0,1,1]])**2).sum()==1

# Deepened research calculations.
assert (0+0+3)/3 == 1
assert (0-1)**2 + (0-1)**2 + (3-1)**2 == 6
assert (1+1+4)/3 == 2
assert (1-2)**2 + (1-2)**2 + (4-2)**2 == 6

article=(ROOT/"articles"/"descent-of-lloyd-s-algorithm.qmd").read_text()
for token in printed:
    assert token in article,("descent-of-lloyd-s-algorithm",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["descent-of-lloyd-s-algorithm"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("descent-of-lloyd-s-algorithm: numerical examples, self-checks and generated text verified")
