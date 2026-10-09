"""Reproducible mathematical illustrations. pip install matplotlib numpy scipy sympy.
SVG glyphs are paths, so figures remain sharp and do not depend on client fonts.
All geometry is sampled from the displayed equations; arrows follow analytic vectors.
"""
from pathlib import Path
import os, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.collections import LineCollection
from matplotlib.ticker import MaxNLocator
from matplotlib.patches import Polygon, Rectangle, Circle, Arc
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.integrate import quad
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'assets'; PREVIEW=Path(os.environ.get('CALCULUS_PREVIEW','/tmp/calculus-figure-review'));PREVIEW.mkdir(exist_ok=True,parents=True)
font_candidates=[os.environ.get('CALCULUS_FONT',''),'/System/Library/Fonts/STHeiti Medium.ttc','/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc']
font=next((p for p in font_candidates if p and Path(p).exists()),None)
if not font:raise RuntimeError('Set CALCULUS_FONT to a Chinese font file')
fm.fontManager.addfont(font)
plt.rcParams.update({'font.family':[fm.FontProperties(fname=font).get_name(),'DejaVu Sans'],'font.size':15,'axes.titlesize':18,'axes.labelsize':15,'xtick.labelsize':12,'ytick.labelsize':12,'svg.fonttype':'path','svg.hashsalt':'jlu-calculus-visual-v2','axes.unicode_minus':False,'mathtext.fontset':'stix','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
TEAL='#087E8B';ORANGE='#DF762C';BLUE='#3D68B0';RED='#BD3653';GREY='#647785';PALE='#E4F2F3'
manifest=[]
def finish(fig,name,title,note):
 fig.suptitle(title,fontsize=23,fontweight='normal',y=.975,color='#1D3544')
 fig.text(.5,.025,note,ha='center',va='bottom',fontsize=14,color=GREY)
 for ax in fig.axes:
  if ax.name=='3d':
   for axis in (ax.xaxis,ax.yaxis,ax.zaxis):axis.set_major_locator(MaxNLocator(nbins=3))
 fig.subplots_adjust(left=.075,right=.95,bottom=.16,top=.82,wspace=.32)
 fig.savefig(OUT/(name+'.svg'),metadata={'Title':title,'Description':note,'Date':None},bbox_inches='tight')
 svg_path=OUT/(name+'.svg');svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text().splitlines())+'\n')
 fig.savefig(PREVIEW/(name+'.png'),dpi=170,bbox_inches='tight');plt.close(fig);manifest.append({'file':name+'.svg','title':title,'note':note})
def panels(n=2,three=False):
 fig=plt.figure(figsize=(13,6.5));axes=[fig.add_subplot(1,n,i+1,projection='3d' if three else None) for i in range(n)];return fig,axes
def xy(ax,xlim,ylim,equal=True):
 ax.set(xlim=xlim,ylim=ylim,xlabel='$x$',ylabel='$y$');ax.grid(alpha=.16)
 if equal:ax.set_aspect('equal',adjustable='box')
def arrow(ax,a,b,color=ORANGE,**kw):
 ax.annotate('',xy=b,xytext=a,zorder=8,arrowprops={'arrowstyle':'-|>','color':color,'lw':2.4,'mutation_scale':17,**kw})
def curvearrow(ax,x,y,i,color=TEAL):arrow(ax,(x[i],y[i]),(x[i+7],y[i+7]),color)
def three(ax,title):
 ax.set_title(title,pad=15);ax.set_xlabel('$x$',labelpad=8);ax.set_ylabel('$y$',labelpad=8);ax.set_zlabel('$z$',labelpad=8);ax.view_init(26,-56);ax.set_box_aspect((1,1,.85));ax.tick_params(labelsize=11)

# 1. Exact finite chord versus differential arc length.
f,axs=panels();x=np.linspace(0,1.15,400)
for ax in axs:ax.plot(x,x*x,color=TEAL,lw=3);xy(ax,(-.05,1.2),(-.06,1.42));ax.text(.03,1.24,'$y=x^2$',color=TEAL)
a=.7;b=.9
ax=axs[0];ax.plot([a,b],[a*a,b*b],color=ORANGE,lw=3);ax.plot([a,b,b],[a*a,a*a,b*b],'--',color=BLUE,lw=2);ax.scatter([a,b],[a*a,b*b],color=ORANGE,zorder=5);ax.text(.72,.43,'$\\Delta x=0.2$',fontsize=13);ax.text(.93,.62,'$\\Delta y=0.32$',fontsize=13);ax.set_title('有限小段：弦长近似弧长');length=quad(lambda u:np.sqrt(1+4*u*u),a,b)[0];ax.text(.03,.10,f'弦长 {np.hypot(.2,.32):.4f}\n实际弧长 {length:.4f}',fontsize=14)
ax=axs[1];point=np.array([.8,.64]);v=np.array([1,1.6])*.16;arrow(ax,point,point+v,ORANGE);ax.scatter(*point,color=ORANGE,zorder=5);ax.text(.08,.98,'斜率 $y\\prime(0.8)=1.6$\n$ds=\\sqrt{1+1.6^2}\\,dx$',fontsize=16);ax.text(.06,.17,'微分公式在极限中成立\n有限弦长与弧长不必相等',fontsize=14);ax.set_title('缩小到一点：切线给出微元')
finish(f,'elements','弧长 ds：先看一段真正的曲线','蓝色虚线为坐标增量；橙色弦段/切向箭头由 y=x² 的端点与导数计算。')

# 2. Riemann sums, quantitative convergence.
f,axs=panels();ax=axs[0];n=8;t=np.linspace(0,np.pi,n+1);tm=(t[:-1]+t[1:])/2
for i in range(n):
 ts=np.linspace(t[i],t[i+1],30);ax.plot(np.cos(ts),np.sin(ts),lw=10,color=plt.cm.YlOrRd((1+.6*np.cos(tm[i]))/1.6))
xy(ax,(-1.3,1.3),(-.15,1.45));ax.set_title('半圆弧：按小段分割并取中点');ax.text(-1.22,1.24,r'$\rho(\theta)=1+0.6\cos\theta$',fontsize=16);ax.text(-1.22,-.10,'颜色越深，线密度越大',fontsize=13);ax.scatter(np.cos(tm),np.sin(tm),s=22,color='#273B46',zorder=5)
ns=np.array([2,4,8,16,32]);mass=[]
for n in ns:
 dt=np.pi/n;mid=(np.arange(n)+.5)*dt;mass.append(np.sum((1+.6*np.cos(mid))*2*np.sin(dt/2)))
ax=axs[1];ax.plot(ns,mass,'o-',lw=2.8,color=TEAL,label='密度 × 弦长的中点近似');ax.axhline(np.pi,color=ORANGE,ls='--',label='精确值 π');ax.set(xlabel='小段数量 n',ylabel='质量近似',ylim=(2.7,3.22));ax.grid(alpha=.2);ax.legend(fontsize=12,loc='lower right');ax.set_title('分割越细，近似趋于积分');ax.text(6,2.78,'半径取 1，线密度按图中函数给定\n精确质量 ∫₀^π ρ(θ)dθ = π',fontsize=13)
finish(f,'density_sum','第一型积分：把“每段的质量”加起来','本图用弦长近似小弧长，因此有限 n 时有误差；右图数值由真实分割计算。')

# 3. Same dx, different ds; reparametrization.
f,axs=panels();ax=axs[0];xx=np.linspace(0,1,300);ax.plot(xx,xx,color=BLUE,lw=3,label='$y=x$');ax.plot(xx,3*xx,color=TEAL,lw=3,label='$y=3x$');xy(ax,(-.05,1.1),(-.05,3.25),False);ax.legend(fontsize=14);ax.set_title('同样的横向增量，弧长不同');ax.text(.05,2.8,'斜率 1：$ds=\\sqrt{2}\\,dx$\n斜率 3：$ds=\\sqrt{10}\\,dx$',fontsize=15)
ax=axs[1];u=np.linspace(0,1,300);ax.plot(u,u,color=BLUE,lw=3,label='参数 t：x=t，y=t');ax.plot(u,u*u,color=TEAL,lw=3,label='参数 u：x=u²，y=u²');ax.set(xlabel='参数（不是横坐标 x）',ylabel='横坐标 x',xlim=(0,1),ylim=(0,1));ax.grid(alpha=.2);ax.legend(fontsize=12,loc='upper left');ax.set_title('走过同一线段，速度可以不同');ax.text(.35,.10,'两种参数覆盖相同几何线段\n∫ ds 都等于 √2',fontsize=13)
finish(f,'param_speed','参数只描述“怎样走”，微元负责记录实际长度','第二幅横轴是参数：t 与 u² 对应同一个点，但到达该点的参数值不同。')

# 4. Helix and projection.
f,axs=panels(2,True);t=np.linspace(0,np.pi,300);ax=axs[0];ax.plot(np.cos(t),np.sin(t),t,color=TEAL,lw=3);ax.plot(np.cos(t),np.sin(t),np.zeros_like(t),'--',color=GREY,lw=2);ax.plot([0,1],[0,0],[0,0],color=ORANGE);ax.scatter([1,-1],[0,0],[0,np.pi],color=ORANGE,s=40);three(ax,'空间半圈：x=cos t，y=sin t，z=t');ax.set(zlim=(0,3.5));ax.text(1,0,0,'A',fontsize=16);ax.text(-1,0,np.pi,'B',fontsize=16)
ax=axs[1];tt=.9;pt=np.array([np.cos(tt),np.sin(tt),tt]);v=np.array([-np.sin(tt),np.cos(tt),1]);ax.plot(np.cos(t),np.sin(t),t,color=TEAL,lw=2,alpha=.6);ax.quiver(*pt,*v,length=.65,color=ORANGE,normalize=False);ax.quiver(*pt,*np.array([-np.sin(tt),np.cos(tt),0]),length=.65,color=BLUE);three(ax,'速度：水平分量长度 1，竖直分量 1');ax.text2D(.02,.86,r'$|\mathbf{r}\prime(t)|=\sqrt{1+1}=\sqrt{2}$',transform=ax.transAxes,fontsize=18);ax.text2D(.02,-.11,'橙色：完整速度；蓝色：水平速度',transform=ax.transAxes,fontsize=13)
finish(f,'helix','空间曲线：投影的长度不能替代真实弧长','参数范围 0≤t≤π；速度箭头统一乘 0.65 作显示，分量比例保持不变。')

# 5. Exact surface / projected area.
f,axs=panels(2,True);u,v=np.meshgrid(np.linspace(0,1,9),np.linspace(0,1,9));ax=axs[0];ax.plot_surface(u,v,u+v,color=TEAL,alpha=.22,edgecolor='#39919A',linewidth=.6);ax.plot_surface(u,v,np.zeros_like(u),color=GREY,alpha=.13);patch=np.array([[.25,.25,.5],[.65,.25,.9],[.65,.65,1.3],[.25,.65,.9]]);ax.add_collection3d(Poly3DCollection([patch],facecolors=ORANGE,alpha=.65,edgecolor=ORANGE));bottom=patch.copy();bottom[:,2]=0;ax.add_collection3d(Poly3DCollection([bottom],facecolors=BLUE,alpha=.35));
for a,b in zip(patch,bottom):ax.plot(*np.array([a,b]).T,'--',color=GREY,lw=1)
three(ax,'真实斜面 z=x+y 与水平投影');ax.set(zlim=(0,2.2))
ax=axs[1];origin=np.array([.25,.25,.5]);au=np.array([.4,0,.4]);av=np.array([0,.4,.4]);normal=np.cross(au,av);ax.add_collection3d(Poly3DCollection([patch],facecolors=TEAL,alpha=.25));ax.quiver(*origin,*au,color=ORANGE,length=1);ax.quiver(*origin,*av,color=BLUE,length=1);ax.quiver(*patch.mean(axis=0),*normal,length=3,color=RED);three(ax,'两条切向边的叉积给出面积');ax.set(xlim=(-.15,.8),ylim=(-.15,.8),zlim=(.3,1.6));ax.text2D(.00,.91,'投影小方块面积：0.4² = 0.16\n曲面小块面积：0.16√3 ≈ 0.2771',transform=ax.transAxes,fontsize=14);ax.text2D(.00,-.11,r'$dS=\sqrt{1+1^2+1^2}\,dxdy$',transform=ax.transAxes,fontsize=18)
finish(f,'projection','面积元 dS：同一个小块，斜面面积更大','平面小块的数值面积是精确值；红色叉积箭头放大 3 倍，仅显示方向。')

# 6. Paraboloid and its domain.
f=plt.figure(figsize=(13,6.5));ax=f.add_subplot(121,projection='3d');rr,tt=np.meshgrid(np.linspace(0,np.sqrt(2),25),np.linspace(0,2*np.pi,55));xx=rr*np.cos(tt);yy=rr*np.sin(tt);zz=rr*rr;ax.plot_surface(xx,yy,zz,cmap='YlGnBu',alpha=.65,linewidth=0);rim=np.linspace(0,2*np.pi,250);ax.plot(np.sqrt(2)*np.cos(rim),np.sqrt(2)*np.sin(rim),2,color=ORANGE,lw=3);three(ax,'曲面 z=x²+y²，截在 z=2');ax.set(zlim=(0,2.4))
ax=f.add_subplot(122);ax.add_patch(Circle((0,0),np.sqrt(2),facecolor=PALE,edgecolor=TEAL,lw=2.5));xy(ax,(-1.7,1.7),(-1.7,1.7));arrow(ax,(0,0),(np.sqrt(2),0));ax.text(.4,.13,'半径 √2',fontsize=15);ax.set_title('投影域 D：x²+y²≤2');ax.text(-1.35,-1.5,'曲面高度限制\n0≤x²+y²≤2',fontsize=14)
finish(f,'paraboloid_domain','确定积分范围：把高度限制投回坐标平面','橙色边界在曲面上是高度 2 的圆；投影后成为半径 √2 的圆。')

# 7. spherical surface parameters.
f=plt.figure(figsize=(13,6.5));ax=f.add_subplot(121,projection='3d');pp,tt=np.meshgrid(np.linspace(0,np.pi/2,20),np.linspace(0,2*np.pi,45));ax.plot_surface(np.sin(pp)*np.cos(tt),np.sin(pp)*np.sin(tt),np.cos(pp),color=TEAL,alpha=.20,linewidth=0);p0,p1=.65,.85;t0,t1=-1.1,-.75;p,t=np.meshgrid(np.linspace(p0,p1,9),np.linspace(t0,t1,9));ax.plot_surface(np.sin(p)*np.cos(t),np.sin(p)*np.sin(t),np.cos(p),color=ORANGE,alpha=.85);three(ax,'单位上半球上的参数小块');ax.text2D(.03,.91,r'$0\leq\phi\leq\pi/2$',transform=ax.transAxes,fontsize=17)
ax=f.add_subplot(122);phis=np.linspace(.02,np.pi-.02,300);ax.plot(phis,np.sin(phis),color=TEAL,lw=3);ax.axvline(np.pi/2,color=ORANGE,ls='--');ax.set(xlim=(0,np.pi),ylim=(0,1.15),xlabel='极角 φ（从 +z 轴量起）',ylabel='面积因子 sin φ');ax.set_xticks([0,np.pi/2,np.pi],['0','π/2','π']);ax.grid(alpha=.18);ax.set_title('相同 dφ、dθ：赤道附近小块更大');ax.text(.13,.82,'$dS=\\sin\\phi\\,d\\phi d\\theta$\n半径 a 时再乘 a²',fontsize=16)
finish(f,'sphere_patch','球面面积元：经线会在极点汇合','橙色小块由给定 φ、θ 区间精确采样；右图说明 sin φ 因子的几何含义。')

# 8. cylinder unrolled to rectangle.
f=plt.figure(figsize=(13,6.5));ax=f.add_subplot(121,projection='3d');t,z=np.meshgrid(np.linspace(0,2*np.pi,48),np.linspace(0,2,17));ax.plot_surface(np.cos(t),np.sin(t),z,color=TEAL,alpha=.22);tp,zp=np.meshgrid(np.linspace(-1.1,-.65,10),np.linspace(.6,1.1,10));ax.plot_surface(np.cos(tp),np.sin(tp),zp,color=ORANGE,alpha=.85);three(ax,'圆柱侧面：半径 1，高度 2');ax.set(zlim=(0,2.2))
ax=f.add_subplot(122);ax.add_patch(Rectangle((0,0),2*np.pi,2,fc=PALE,ec=TEAL,lw=2.5));ax.add_patch(Rectangle((2*np.pi-1.1,.6),.45,.5,fc=ORANGE,alpha=.65));ax.set(xlim=(-.1,6.7),ylim=(-.1,2.4),xlabel='展开后的水平弧长 s=θ',ylabel='高度 z');ax.set_xticks([0,np.pi,2*np.pi],['0','π','2π']);ax.set_title('展开后：面积就是长 × 宽');ax.text(1.2,1.2,'$dS=d\\theta dz$\n半径 a 时：$dS=a\\,d\\theta dz$',fontsize=17);ax.grid(alpha=.15)
finish(f,'cylinder_patch','圆柱面积元：把弯曲薄壳展开看','本图只画侧面；上下底盘没有包含在侧面积中。')

# 9. symmetry with signed weight.
f,axs=panels();t=np.linspace(0,2*np.pi,600);x=np.cos(t);y=np.sin(t)
for ax in axs:xy(ax,(-1.3,1.3),(-1.35,1.35));ax.axvline(0,color=GREY,lw=1)
for i,fun in enumerate([x,x*x]):
 pts=np.column_stack([x,y]);segments=np.stack([pts[:-1],pts[1:]],axis=1);lc=LineCollection(segments,cmap='coolwarm' if i==0 else 'YlOrRd',linewidth=5);lc.set_array(fun[:-1]);lc.set_clim(-1 if i==0 else 0,1);axs[i].add_collection(lc);f.colorbar(lc,ax=axs[i],shrink=.60,pad=.03,label='权重 f')
 a=.8;b=.6;axs[i].scatter([a,-a],[b,b],color=ORANGE,s=65,zorder=5);axs[i].plot([-a,a],[b,b],'--',color=GREY);axs[i].set_title('$f=x$：镜像点的贡献抵消' if i==0 else '$f=x^2$：镜像点的贡献相加');axs[i].text(-1.2,-1.2,'∮ x ds = 0' if i==0 else '∮ x² ds = π',fontsize=18)
finish(f,'symmetry','对称性：在同一圆周上比较 x 与 x²','取单位圆；两点 (0.8,0.6) 与 (-0.8,0.6) 的弧长权重相同，函数值不同。')

# 10. centroid mass weighting.
f,axs=panels();ax=axs[0];points=np.array([0,2]);ax.scatter(points,[0,0],s=[350,1050],color=[BLUE,ORANGE]);ax.plot([-.4,2.4],[0,0],color=GREY);ax.axvline(1.5,color=RED,ls='--');ax.text(-.25,.30,'质量 1',fontsize=16);ax.text(1.65,.30,'质量 3',fontsize=16);ax.text(.95,-.30,'质心 x̄=1.5',color=RED,fontsize=16);ax.set(xlim=(-.5,2.6),ylim=(-.6,.65),yticks=[],xlabel='位置 x');ax.set_title('先看两个质点：较重的一侧拉近质心');ax.text(.1,-.52,r'$\bar x=(0\times1+2\times3)/4=1.5$',fontsize=15)
ax=axs[1];x=np.linspace(0,1,250);ax.fill_between(x,0,1+x,color=PALE);ax.plot(x,1+x,color=TEAL,lw=3);ax.axvline(5/9,color=RED,ls='--');ax.axvline(.5,color=GREY,ls=':');ax.set(xlabel='细杆位置 x',ylabel='线密度 ρ(x)',ylim=(0,2.3));ax.set_title('再看连续细杆：ρ(x)=1+x');ax.text(.05,1.9,'右端更密 → 质心略偏右',fontsize=15);ax.text(.06,.4,'总质量 m=3/2\n一阶矩 ∫xρdx=5/6\n质心 x̄=5/9≈0.556',fontsize=15)
finish(f,'centroid','质心：从离散的加权平均到连续积分','左图圆点面积与质量成比例；右图红线是质心，灰线是几何中点。')

# 11. inertia distance.
f,axs=panels();t=np.linspace(0,2*np.pi,400);x=np.cos(t);y=np.sin(t)
for ax in axs:ax.plot(x,y,color=TEAL,lw=3);xy(ax,(-1.5,1.5),(-1.4,1.4))
ax=axs[0];ax.scatter(0,0,marker='x',s=100,color=RED);arrow(ax,(0,0),(.6,.8));ax.scatter(.6,.8,color=ORANGE,s=50);ax.text(.07,.35,'r=1',fontsize=16);ax.set_title('绕 z 轴：每个点距离都是 1');ax.text(-1.3,-1.25,'$I_z=m$（单位圆环）',fontsize=18)
ax=axs[1];ax.axhline(0,color=RED,lw=3);ax.plot([.6,.6],[0,.8],color=ORANGE,lw=3);ax.scatter(.6,.8,color=ORANGE,s=50);ax.text(.73,.4,'r=|y|',fontsize=16);ax.set_title('绕 x 轴：距离随圆周位置变化');ax.text(-1.3,-1.25,'$I_x=\\int y^2dm=m/2$',fontsize=18)
finish(f,'inertia','转动惯量：先找旋转轴，再量垂直距离','圆环位于 xy 平面；左图 z 轴垂直屏幕，右图 x 轴是红色水平线。')

# 12. ring gravity side cut + analytic curve.
f,axs=panels();ax=axs[0];xy(ax,(-1.4,1.4),(-.3,2.4),False);ax.set_ylabel('z');ax.scatter([-1,1],[0,0],color=TEAL,s=100);ax.scatter(0,1.3,color=RED,s=80);arrow(ax,(0,1.3),(-.55,.585),TEAL);arrow(ax,(0,1.3),(.55,.585),TEAL);arrow(ax,(0,1.3),(0,.36),ORANGE);ax.text(.10,1.55,'观察点 (0,0,h)',fontsize=14);ax.text(-1.3,-.15,'截面中的两个相对源点',fontsize=14);ax.set_title('水平分量抵消，竖直分量相加');ax.axvline(0,color=GREY,ls=':',lw=1)
ax=axs[1];h=np.linspace(0,4,400);value=-h/(1+h*h)**1.5;ax.plot(h,value,color=TEAL,lw=3);ax.axhline(0,color=GREY,lw=1);ax.scatter([1/np.sqrt(2)],[-2/(3*np.sqrt(3))],color=ORANGE,s=65);ax.set(xlabel='轴上高度 h / a',ylabel='Fz / (GMm₀/a²)',ylim=(-.43,.05));ax.grid(alpha=.2);ax.set_title('圆环轴向引力：先增大，再减小');ax.text(1.6,-.12,r'$F_z\propto-\frac{h}{(1+h^2)^{3/2}}$',fontsize=18)
finish(f,'gravity_ring','引力：对称性决定方向，距离决定大小','右图采用 a=1 的无量纲形式；左图箭头为方向分解，显示长度统一缩放。')

# 13. signed work from exact vectors.
f,axs=panels(3)
for ax,ang,label in zip(axs,[0,np.pi/2,np.pi],['顺着力：做正功','与力垂直：功为零','逆着力：做负功']):
 xy(ax,(-1.9,2.5),(-.7,2.0));arrow(ax,(0,0),(2,0),TEAL);arrow(ax,(0,0),(1.5*np.cos(ang),1.5*np.sin(ang)),ORANGE);ax.text(1,.12,'力',color=TEAL,fontsize=14);ax.text(-.25,1.75,'力 F=(2,0)',color=TEAL,fontsize=15);ax.set_title(label,fontsize=17);ax.text(.10,-.48,f'夹角 {int(np.degrees(ang))}°\n每单位路程的功 = {2*np.cos(ang):.0f}',fontsize=15)
finish(f,'work_dot','做功：力的方向与位移方向一起决定结果','青色代表力的固定方向，橙色代表三种位移方向；箭头长度仅作展示，功按 F=(2,0) 计算。')
# correction: labels above arrows and colors explicit in final note.

# 14. forward/reverse, genuine path and signed dx.
f,axs=panels();t=np.linspace(0,1,200)
for i,ax in enumerate(axs):
 ax.plot(t,t,color=TEAL,lw=3);xy(ax,(-.2,1.3),(-.2,1.3));ax.scatter([0,1],[0,1],color=ORANGE,s=60);ax.text(-.12,-.12,'A');ax.text(1.05,1.02,'B');arrow(ax,(.35,.35),(.62,.62),ORANGE) if i==0 else arrow(ax,(.62,.62),(.35,.35),ORANGE);ax.set_title('A → B：x 与 y 一起增加' if i==0 else 'B → A：x 与 y 一起减少');ax.text(-.12,1.20,'∫(x+y)ds = √2',fontsize=16);ax.text(-.12,1.06,'∫(y dx+x dy) = 1' if i==0 else '∫(y dx+x dy) = −1',fontsize=16)
finish(f,'orientation','反向实验：几何路径相同，功的符号改变','单位线段 A=(0,0)、B=(1,1)；两幅图保持相同坐标比例。')

# 15. Conservative field vs rotational field on two paths.
f,axs=panels();X,Y=np.meshgrid(np.linspace(.05,.95,7),np.linspace(.05,.95,7));t=np.linspace(0,1,200)
for i,ax in enumerate(axs):
 U,V=(2*X,2*Y) if i==0 else (-Y,X);ax.quiver(X,Y,U,V,color='#9DB4C3',angles='xy',scale_units='xy',scale=10,width=.006);ax.plot(t,t,color=TEAL,lw=3,label='路径①：直线');ax.plot([0,1,1],[0,0,1],color=ORANGE,lw=3,label='路径②：先横后竖');xy(ax,(-.15,1.15),(-.15,1.15));curvearrow(ax,t,t,100);arrow(ax,(.45,0),(.65,0),ORANGE);arrow(ax,(1,.45),(1,.65),ORANGE);ax.legend(fontsize=12,loc='upper left');ax.text(-.12,-.12,'A=(0,0)');ax.text(.55,1.02,'B=(1,1)');ax.set_title('梯度场 F=(2x,2y)' if i==0 else '旋转场 F=(-y,x)');ax.text(.10,.70,'①=2；②=2\n势函数 u=x²+y²' if i==0 else '①=0；②=1\n路径改变，功也改变',fontsize=15,bbox={'facecolor':'white','alpha':.9,'edgecolor':'none'})
finish(f,'paths','路径无关需要条件：同一对端点，比较两条路线','背景箭头按相同系数缩放；路线①与②覆盖不同路径，端点相同。')

# 16. Green example with true vector field and internal cancellation.
f,axs=panels();ax=axs[0];X,Y=np.meshgrid(np.linspace(-.9,.9,9),np.linspace(-.9,.9,9));mask=X*X+Y*Y<.95;ax.quiver(X[mask],Y[mask],-Y[mask],X[mask],color=BLUE,angles='xy',scale_units='xy',scale=5);t=np.linspace(0,2*np.pi,300);x=np.cos(t);y=np.sin(t);ax.plot(x,y,color=TEAL,lw=3);curvearrow(ax,x,y,20);xy(ax,(-1.35,1.35),(-1.4,1.4));ax.set_title('旋转场 F=(-y,x)，边界逆时针');ax.text(-1.24,-1.24,'$Q_x-P_y=2$，总环流 $2\\pi$',fontsize=15)
ax=axs[1];xy(ax,(-.2,2.2),(-.25,1.55));
for x0 in [0,1]:
 ax.add_patch(Rectangle((x0,0),1,1,fc=PALE,ec=TEAL,lw=2));arrow(ax,(x0+.2,0),(x0+.7,0),TEAL);arrow(ax,(x0+1,.2),(x0+1,.7),TEAL);arrow(ax,(x0+.7,1),(x0+.2,1),TEAL);arrow(ax,(x0,.7),(x0,.2),TEAL)
arrow(ax,(.94,.25),(.94,.7),ORANGE);arrow(ax,(1.06,.7),(1.06,.25),RED);ax.text(.22,1.25,'公共边：相反方向 → 抵消',fontsize=16);ax.text(-.06,-.21,'每块小区域都取正向边界',fontsize=15);ax.set_title('分成两块后，只留下外围边界')
finish(f,'green','Green：把小区域的环流相加，内部边会消去','左图积分由单位圆与旋转场精确计算；右图说明相邻块的共同边为何消失。')

# 17. ellipse area swept parameter.
f,axs=panels();t=np.linspace(0,2*np.pi,400);x=2*np.cos(t);y=np.sin(t);ax=axs[0];ax.fill(x,y,color=PALE);ax.plot(x,y,color=TEAL,lw=3);curvearrow(ax,x,y,40);xy(ax,(-2.5,2.5),(-1.6,1.6));ax.set_title('椭圆：a=2，b=1');ax.text(-1.95,-1.38,'面积 = πab = 2π',fontsize=18)
ax=axs[1];t0=.5;t1=.9;p=np.array([2*np.cos(t0),np.sin(t0)]);q=np.array([2*np.cos(t1),np.sin(t1)]);ax.plot(x,y,color=TEAL,lw=2);ax.add_patch(Polygon([(0,0),p,q],fc=ORANGE,alpha=.45));ax.plot([0,p[0]],[0,p[1]],color=ORANGE);ax.plot([0,q[0]],[0,q[1]],color=ORANGE);xy(ax,(-2.5,2.5),(-1.6,1.6));ax.set_title('微小扇形：面积来自位置与位移');ax.text(-2.1,-1.4,'$dA=\\frac{1}{2}(x\\,dy-y\\,dx)=d\\theta$',fontsize=17)
finish(f,'area_ellipse','用曲线积分计算面积：位置向量扫过的微小面积','橙色三角形近似有限扇形；dA 公式是增量趋于零后的精确微分关系。')

# 18. correctly oriented closing semicircle.
f,axs=panels();t=np.linspace(0,np.pi,300);x=np.cos(t);y=np.sin(t)
for ax in axs:ax.fill_between(x,y,0,color=PALE);ax.plot(x,y,color=TEAL,lw=3);curvearrow(ax,x,y,60);xy(ax,(-1.35,1.35),(-.35,1.4));ax.text(1.03,-.06,'A');ax.text(-1.16,-.06,'B')
ax=axs[0];arrow(ax,(-.8,0),(.75,0),ORANGE);ax.set_title('原弧 L：A→B；补线 C：B→A');ax.text(-1.2,1.19,'闭合方向：区域始终在左侧',fontsize=14)
ax=axs[1];ax.plot([-1,1],[0,0],color=ORANGE,lw=3);ax.set_title('分别记录两个积分，最后相减');ax.text(-1.23,.62,'F=(-y,x)，旋度为 2\n闭合积分：2 × (π/2) = π\n补线：y=0、dy=0 → 0\n原曲线：π − 0 = π',fontsize=15,bbox={'facecolor':'white','alpha':.85,'edgecolor':'none'})
finish(f,'closing','补线：让开放的半圆弧变成正向闭边界','所有箭头由参数方向产生；原弧从右端向左端走，补线沿直径向右。')

# 19. singularity, two loops with explicit circulation.
f,axs=panels();X,Y=np.meshgrid(np.linspace(-1.4,1.4,11),np.linspace(-1.4,1.4,11));r2=X*X+Y*Y;mask=(r2>.12)&(r2<2);t=np.linspace(0,2*np.pi,400)
for ax in axs:ax.quiver(X[mask],Y[mask],-Y[mask]/r2[mask],X[mask]/r2[mask],angles='xy',scale_units='xy',scale=8,color=BLUE);xy(ax,(-1.6,1.6),(-1.6,1.6));ax.scatter(0,0,color=RED,marker='x',s=100);ax.plot(np.cos(t),np.sin(t),color=TEAL,lw=3);curvearrow(ax,np.cos(t),np.sin(t),30)
ax=axs[0];ax.set_title('原点以外：局部旋度等于零');ax.text(-1.4,-1.45,'原点未定义，不能跨过它用 Green',fontsize=14)
ax=axs[1];ax.add_patch(Circle((0,0),.35,fc='white',ec=ORANGE,lw=3,zorder=4));x=.35*np.cos(t[::-1]);y=.35*np.sin(t[::-1]);curvearrow(ax,x,y,70,ORANGE);ax.set_title('挖去小圆：内边界要顺时针');ax.text(-1.4,-1.45,'外圈 + 内圈 = 2π − 2π = 0',fontsize=15)
finish(f,'singularity','奇点：局部旋度为零，绕洞的环流仍可非零','场 F=(-y,x)/(x²+y²)；任一绕原点一次的正向圆积分均为 2π。')

# 20. flux through tilted plane with signs.
f,axs=panels(2,True);u,v=np.meshgrid(np.linspace(0,1,10),np.linspace(0,1,10));center=np.array([.5,.5,1.]);normal=np.array([-1,-1,1])/np.sqrt(3)
for i,ax in enumerate(axs):
 ax.plot_surface(u,v,u+v,color=TEAL,alpha=.30);n=normal if i==0 else -normal;ax.quiver(*center,*n,length=.65,color=ORANGE);ax.quiver(*center,0,0,1,length=.85,color=BLUE);three(ax,'选上侧：F·n 为正' if i==0 else '选下侧：同一个 F·n 为负');ax.text2D(.01,.91,'F=(0,0,1)',transform=ax.transAxes,fontsize=17);ax.text2D(.01,-.11,'单位方形上的总通量 = +1' if i==0 else '单位方形上的总通量 = −1',transform=ax.transAxes,fontsize=15);ax.set(xlim=(-.2,1.2),ylim=(-.2,1.2),zlim=(0,2.2))
finish(f,'flux','通量：穿过斜面的分量 × 实际面积','蓝色为 F，橙色为所选单位法向；两图曲面相同、法向相反。')

# 21. tangent and normal for upward/downward graph, cancellation factor.
f,axs=panels();ax=axs[0];ax.add_patch(Polygon([(-1,-1),(1,1),(1,-.2),(-1,-2.2)],fc=PALE));ax.plot([-1,1],[-1,1],color=TEAL,lw=3);xy(ax,(-1.5,1.6),(-1.5,1.7));ax.set_ylabel('z');arrow(ax,(0,0),(-.65,.65),ORANGE);arrow(ax,(0,0),(0,1),BLUE);ax.text(.18,.90,'F=(0,0,1)',color=BLUE,fontsize=14);ax.text(-1.4,1.26,'剖面 z=x；上法向朝左上',fontsize=14);ax.set_title('二维剖面：区分法向与竖直方向')
ax=axs[1];ax.axis('off');lines=[('单位法向',r'$\mathbf{n}=(-1,-1,1)/\sqrt{3}$'),('实际面积元',r'$dS=\sqrt{3}\,dxdy$'),('相乘后，根号抵消',r'$\mathbf{n}\,dS=(-1,-1,1)\,dxdy$'),('竖直场 F=(0,0,1)',r'$\mathbf{F}\cdot\mathbf{n}\,dS=dxdy$')]
for i,(a,b) in enumerate(lines):ax.text(.02,.88-i*.23,a,fontsize=16,color=TEAL);ax.text(.02,.77-i*.23,b,fontsize=19)
ax.set_title('合一投影公式的每一步')
finish(f,'normal_area','第二型面积元：长度因子为何不再出现','左图只画 y=0 的剖面；右侧公式适用于完整的三维平面 z=x+y。')

# 22. divergence fields source zero sink; 2d slices, full3d defined explicit.
f,axs=panels(3);X,Y=np.meshgrid(np.linspace(-1,1,7),np.linspace(-1,1,7))
for ax,U,V,title,value in zip(axs,[X,X,-X],[Y,-Y,-Y],['源：F=(x,y,z)','拉伸与压缩：F=(x,-y,0)','汇：F=(-x,-y,-z)'],[3,0,-3]):
 ax.quiver(X,Y,U,V,color=TEAL,angles='xy',scale_units='xy',scale=4);xy(ax,(-1.45,1.45),(-1.45,1.45));ax.add_patch(Rectangle((-.65,-.65),1.3,1.3,fill=False,ec=ORANGE,lw=2));ax.set_title(title,fontsize=15);ax.text(-1.25,-1.32,f'三维散度 div F = {value}',fontsize=15)
finish(f,'divergence','散度：同样的小区域，可以流出、抵消或流入','箭头画 z=0 的截面；散度按标题中的完整三维场计算，不能只看图中的两分量。')

# 23. half sphere vs cap, genuine outward normals.
f,axs=panels(2,True);p,t=np.meshgrid(np.linspace(0,np.pi/2,18),np.linspace(0,2*np.pi,42));x=np.sin(p)*np.cos(t);y=np.sin(p)*np.sin(t);z=np.cos(p)
ax=axs[0];ax.plot_surface(x,y,z,color=TEAL,alpha=.3);three(ax,'原曲面：单位上半球外侧');pt=np.array([.6,0,.8]);ax.quiver(*pt,*pt,length=.45,color=ORANGE);ax.quiver(0,0,1,0,0,1,length=.4,color=ORANGE);ax.set(zlim=(-.5,1.5))
ax=axs[1];ax.plot_surface(x,y,z,color=TEAL,alpha=.15);r,tt=np.meshgrid(np.linspace(0,1,12),np.linspace(0,2*np.pi,42));ax.plot_surface(r*np.cos(tt),r*np.sin(tt),np.zeros_like(r),color=ORANGE,alpha=.55);ax.quiver(0,0,0,0,0,-1,length=.5,color=RED);three(ax,'补底盘：同一立体外侧必须朝下');ax.set(zlim=(-.6,1.5));ax.text2D(.01,-.11,'底盘通量 −π；半球通量 3π',transform=ax.transAxes,fontsize=15)
finish(f,'gauss','Gauss 补面：看清底盘的外法向','使用 F=(x,y,z+1)、单位上半球：体积分 2π，减去底盘通量 −π，得到 3π。')

# 24. Gauss singularity scaling.
f,axs=panels();ax=axs[0];rs=np.array([.6,1,1.5]);theta=np.linspace(0,2*np.pi,400)
for r,c in zip(rs,[ORANGE,TEAL,BLUE]):ax.plot(r*np.cos(theta),r*np.sin(theta),color=c,lw=2.5,label=f'球半径 {r:g} 的截面')
xy(ax,(-1.9,1.9),(-1.9,1.9));ax.scatter(0,0,marker='x',s=100,color=RED);ax.legend(fontsize=11,loc='upper right');ax.set_title('径向场 r/|r|³：原点有奇点')
ax=axs[1];r=np.linspace(.4,2,300);ax.plot(r,1/(r*r),color=TEAL,lw=3,label='法向场强 1/a²');ax.plot(r,r*r,color=ORANGE,lw=3,label='球面积 /4π = a²');ax.axhline(1,color=BLUE,ls='--',label='总通量 /4π = 1');ax.set(xlabel='球半径 a',ylabel='归一化值',ylim=(0,6.5));ax.legend(fontsize=12);ax.grid(alpha=.15);ax.set_title('场强减弱与面积增大恰好抵消')
finish(f,'gauss_singularity','为什么散度为零，球面通量却是 4π？','左图是球面的赤道截面；场在原点不定义，直接使用 Gauss 的条件不成立。')

# 25. Stokes real tilted plane and normal; top view matches orientation.
f=plt.figure(figsize=(13,6.5));ax=f.add_subplot(121,projection='3d');e1=np.array([1,-1,0])/np.sqrt(2);normal=np.ones(3)/np.sqrt(3);e2=np.cross(normal,e1);r,t=np.meshgrid(np.linspace(0,1,14),np.linspace(0,2*np.pi,55));pts=r[...,None]*(np.cos(t)[...,None]*e1+np.sin(t)[...,None]*e2);ax.plot_surface(pts[:,:,0],pts[:,:,1],pts[:,:,2],color=TEAL,alpha=.32);ts=np.linspace(0,2*np.pi,400);bd=np.cos(ts)[:,None]*e1+np.sin(ts)[:,None]*e2;ax.plot(*bd.T,color=TEAL,lw=3);ax.quiver(0,0,0,*normal,length=.85,color=ORANGE);i=50;tangent=-np.sin(ts[i])*e1+np.cos(ts[i])*e2;ax.quiver(*bd[i],*tangent,length=.28,color=RED);three(ax,'圆盘在平面 x+y+z=0 中');ax.set_box_aspect((1,1,1));ax.text2D(.0,.92,r'$\mathbf{n}=(1,1,1)/\sqrt{3}$',transform=ax.transAxes,fontsize=17)
ax=f.add_subplot(122);ax.fill(np.cos(ts),np.sin(ts),color=PALE);ax.plot(np.cos(ts),np.sin(ts),color=TEAL,lw=3);curvearrow(ax,np.cos(ts),np.sin(ts),50,RED);xy(ax,(-1.35,1.35),(-1.4,1.4));ax.set_xlabel('平面内坐标 ξ');ax.set_ylabel('平面内坐标 η');ax.set_title('从法向一侧看：正向边界为逆时针');ax.scatter(0,0,marker='$\\odot$',s=180,color=ORANGE);ax.text(-1.2,-1.22,'⊙ 表示法向朝向观察者',fontsize=14)
finish(f,'stokes','Stokes：先把边界箭头与曲面法向配成一对','左图从方程生成真实倾斜圆盘；右图是在同一圆盘自身坐标中的正视图。')

# 26. vector derivatives with concrete contour geometry.
f,axs=panels();ax=axs[0];X,Y=np.meshgrid(np.linspace(-1.4,1.4,100),np.linspace(-1.4,1.4,100));cs=ax.contour(X,Y,X*X+Y*Y,levels=[.25,.5,1,1.5,2],colors=BLUE);ax.clabel(cs,inline=True,fontsize=11);x,y=np.meshgrid(np.linspace(-1.1,1.1,6),np.linspace(-1.1,1.1,6));ax.quiver(x,y,2*x,2*y,color=TEAL,angles='xy',scale_units='xy',scale=10);xy(ax,(-1.5,1.5),(-1.5,1.5));ax.set_title('u=x²+y²：梯度垂直等高线');ax.text(-1.35,-1.36,'梯度 ∇u=(2x,2y)',fontsize=16)
ax=axs[1];ax.quiver(x,y,-y,x,color=TEAL,angles='xy',scale_units='xy',scale=5);ax.add_patch(Circle((0,0),1,fc='none',ec=ORANGE,lw=2));xy(ax,(-1.5,1.5),(-1.5,1.5));ax.set_title('F=(-y,x,0)：旋度朝 +z');ax.scatter(0,0,marker='$\\odot$',s=200,color=ORANGE);ax.text(-1.35,-1.36,'curl F=(0,0,2)',fontsize=16)
finish(f,'gradient_curl','梯度与旋度：用两幅具体场区分输入和输出','左图输入是标量高度 u，右图输入是旋转向量场 F；箭头统一缩放显示。')

# Quantitative checks tied to the diagrams, not merely file existence.
x,y,z,t=sp.symbols('x y z t',real=True)
checks={}
checks['plane_area_factor']=str(sp.sqrt(1+sp.diff(x+y,x)**2+sp.diff(x+y,y)**2))
checks['helix_speed_squared']=str(sp.simplify(sp.diff(sp.cos(t),t)**2+sp.diff(sp.sin(t),t)**2+1))
checks['rod_mass']=str(sp.integrate(1+x,(x,0,1)));checks['rod_centroid']=str(sp.integrate(x*(1+x),(x,0,1))/sp.integrate(1+x,(x,0,1)))
P=-y/(x*x+y*y);Q=x/(x*x+y*y);checks['punctured_plane_curl']=str(sp.simplify(sp.diff(Q,x)-sp.diff(P,y)))
checks['tilted_circle_on_plane']=float(np.max(np.abs(bd.sum(axis=1))));checks['tilted_circle_radius_error']=float(np.max(np.abs(np.linalg.norm(bd,axis=1)-1)))
assert checks['plane_area_factor']=='sqrt(3)' and checks['helix_speed_squared']=='2'
assert checks['rod_centroid']=='5/9' and checks['punctured_plane_curl']=='0'
assert checks['tilted_circle_on_plane']<1e-12 and checks['tilted_circle_radius_error']<1e-12
assert np.all(np.diff(mass)>0) and abs(mass[-1]-np.pi)<.002
for a in [.6,1,1.5]:assert abs((1/a**2)*(4*np.pi*a*a)-4*np.pi)<1e-12
(OUT/'math-figures.json').write_text(json.dumps({'figures':manifest,'checks':checks,'density_sum':{'n':ns.tolist(),'mass':mass,'exact':float(np.pi)},'tools':{'matplotlib':matplotlib.__version__,'sympy':sp.__version__},'font_note':'SVG characters and formulas exported as vector paths'},ensure_ascii=False,indent=2))
print('Generated',len(manifest),'mathematical SVGs; geometry and symbolic checks passed')
