"""Rebuild the lidar plot from the numerical check's public measurement table."""
from pathlib import Path
import argparse,ast,io,os,tempfile
import numpy as np
os.environ.setdefault('MPLCONFIGDIR',str(Path(tempfile.gettempdir())/'statwiki-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2]);p.add_argument('--output',type=Path);a=p.parse_args()
tree=ast.parse((a.root/'checks/lidar-data.py').read_text())
data=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='DATA' for x in n.targets))
if a.output is None:a.output=a.root/'sources/book/figures/lidar.pdf'
xy=np.loadtxt(io.StringIO(data),skiprows=1);r,y=xy.T
assert len(r)==221 and r.min()==390 and r.max()==720
curves={h:np.array([y[np.abs(r-x)<=h].mean() for x in r]) for h in (5,25,100)}
for h,n,target in [(5,7,-.095964325),(25,34,-.098055052),(100,134,-.226669372)]:
 mask=np.abs(r-550)<=h;assert mask.sum()==n;assert abs(y[mask].mean()-target)<1e-9
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'statwiki-lidar-correct-units'})
fig,ax=plt.subplots(figsize=(8.18,5.2));ax.scatter(r,y,s=13,c='#777777',alpha=.6,zorder=2)
for h,c in [(5,'#D55E00'),(25,'#0072B2'),(100,'#009E73')]:ax.plot(r,curves[h],lw=1.6,color=c,label=f'{h} m half-window',zorder=3)
ax.set(xlabel='Range (metres)',ylabel='Log ratio of received signals',xlim=(374,736),ylim=(-1,.075))
ax.set_xticks([400,500,600,700]);ax.set_yticks([0,-.25,-.5,-.75]);ax.grid(color='#dddddd',lw=.6)
for spine in ax.spines.values():spine.set_color('#666666');spine.set_linewidth(.8)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.2),ncol=3,frameon=False,fontsize=10)
fig.subplots_adjust(left=.105,right=.98,top=.98,bottom=.24)
metadata={'Creator':'StatWiki'}
if a.output.suffix.lower()=='.pdf':metadata.update(CreationDate=None,ModDate=None)
fig.savefig(a.output,dpi=150,metadata=metadata);plt.close(fig)
print('Preserved221 observations and all3 inclusive-window curves; corrected physical labels.')
