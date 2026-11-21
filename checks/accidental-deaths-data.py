from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
import numpy as np
Y=np.array([9007,8106,8928,9137,10017,10826,11317,10744,9713,9938,9161,8927,7750,6981,8038,8422,8714,9512,10120,9823,8743,9129,8710,8680,8162,7306,8124,7870,9387,9556,10093,9620,8285,8466,8160,8034,7717,7461,7767,7925,8623,8945,10078,9179,8037,8488,7874,8647,7792,6957,7726,8106,8890,9299,10625,9302,8314,8850,8265,8796,7836,6892,7791,8192,9115,9434,10484,9827,9110,9070,8633,9240])
assert len(Y)==72 and Y[:12].sum()==115821
W=Y[12:]-Y[:-12]
assert W[0]==-1257 and W[1]==-1125 and np.diff(W)[0]==132
assert Y[1]-Y[0]==-901 and 1978-1973+1==6
assert 6*12==72 and len(W)==60 and len(np.diff(W))==59
# Polynomial differencing, checked without fitting a trend to the data.
t=np.arange(30);linear=3*t+5;quad=t*t
assert np.all(linear[12:]-linear[:-12]==36)
assert np.all(np.diff(quad[12:]-quad[:-12])==24)
printed=['-1257','-1125','115821','-901']

# Verify the forecast numbers using the fitted model in base R; the exact auto.arima
# order selection was also reproduced separately with forecast 8.20 during research.
import os,shutil,subprocess
rhome=os.environ.get('STATWIKI_R_HOME')
if rhome:
 cmd=[str(Path(rhome)/'bin/exec/R'),'--vanilla','--slave','-e']
elif shutil.which('Rscript'):
 cmd=[shutil.which('Rscript'),'--vanilla','-e']
elif shutil.which('R'):
 cmd=[shutil.which('R'),'--vanilla','--slave','-e']
else:
 raise RuntimeError('The accidental-deaths forecast check requires R; install R or set STATWIKI_R_HOME.')
expr='fit<-arima(USAccDeaths,order=c(0,1,1),seasonal=list(order=c(0,1,1),period=12));p<-predict(fit,n.ahead=12);cat(p$pred[1],sum(p$pred),p$pred[1]-qnorm(.975)*p$se[1],p$pred[1]+qnorm(.975)*p$se[1])'
out=subprocess.run(cmd+[expr],text=True,capture_output=True,check=True)
a,b,lower,upper=map(float,out.stdout.split())
assert abs(a-8336.061)<.02 and abs(b-109952.8)<.2
assert lower<7798<upper and 7798<a
assert round(b)==109953 and 109953-105000==4953
printed += ['109{,}953','4{,}953','8300']

# Deepened research calculations.
assert 115821/12 == 9651.75
assert 7750-9007 == -1257
# Y_t = 100 + 2t + t^2, lag-12 difference, then ordinary difference.
def W(t):
    Y = lambda s: 100 + 2*s + s*s
    return Y(t) - Y(t-12)
assert W(20) - W(19) == 24
def W3(t):
    return 3*t*t - 3*(t-12)**2
assert W3(20) - W3(19) == 72
assert W3(20) == 72*20 - 432

article=(ROOT/"articles"/"accidental-deaths-data.qmd").read_text()
for token in printed:
    assert token in article,("accidental-deaths-data",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["accidental-deaths-data"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("accidental-deaths-data: numerical examples, self-checks and generated text verified")
