"""Generate accessible, self-contained SVG knowledge maps and lesson figures."""
from pathlib import Path
from html import escape
import math

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
INK = '#244052'
COLORS = ['#177f7a', '#b27b1c', '#59739c', '#ae645b', '#697b4b']

def text(x,y,value,size=19,color=INK,weight=400,anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>'

def rect(x,y,w,h,fill='#f2f7f8',stroke='#cad9df',r=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"/>'

def line(x1,y1,x2,y2,color='#9aadb7',arrow=False,dash=False):
    return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{color}" stroke-width="2"'+(' marker-end="url(#arrow)"' if arrow else '')+(' stroke-dasharray="6 5"' if dash else '')+'/>'

def svg(name,title,desc,body,w=1080,h=500):
    header=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#526b7c"/></marker></defs><rect width="100%" height="100%" rx="18" fill="#fbfdfd"/><g font-family="PingFang SC,Microsoft YaHei,sans-serif">'''
    body = body.replace('n𝓏', 'n<tspan baseline-shift="sub" font-size="14">z</tspan>')
    (ASSETS/name).write_text(header+body+'</g></svg>')

def mindmap(name,title,root,branches,footer):
    h=120+len(branches)*100
    body=text(28,38,title,25,weight=650)
    cy=70+len(branches)*50
    body+=rect(24,cy-46,200,92,'#254957','#254957')
    for i,t in enumerate(root):body+=text(124,cy-5+i*29,t,22,'white',600,'middle')
    for i,(heading,detail) in enumerate(branches):
        y=70+i*100;c=COLORS[i%len(COLORS)]
        body+=f'<path d="M224,{cy} C260,{cy} 250,{y+36} 286,{y+36}" stroke="{c}" stroke-width="2.5" fill="none"/>'
        body+=rect(286,y,766,76,'#f5f9f9',c)+text(306,y+30,heading,22,c,600)+text(306,y+58,detail,18)
    body+=text(28,h-17,footer,16,'#657985')
    svg(name,title,'；'.join(a+'：'+b for a,b in branches),body,h=h)

maps=[
('chapter5-map.svg','第5章 · 第二型积分知识导图',['方向与','有向累积'],[
('5.1 曲线积分：做功','切向位移 → 两型关系 → 参数 / 直角坐标 → 对称性'),
('5.2 Green：平面闭路 ↔ 平面区域','条件与方向 → 补线 / 挖洞 → 面积 / 投影 → 全微分与路径无关'),
('5.3 曲面积分：通量','法向与有向面积元 → 分项投影 → 对称性 → 合一投影'),
('5.4 Gauss：封闭面 ↔ 体积','散度 → 直接三重积分 → 补面 → 挖洞'),
('5.5 Stokes：空间闭路 ↔ 所张面','右手定向 → 旋度 → 选简单面 → 复用曲面积分方法')],
'学习顺序：5.1 → 5.2；5.3 → 5.4；5.5 联系曲线、曲面与 Green。'),
('section51-map.svg','5.1 · 第二型曲线积分',['沿有向曲线','累积做功'],[
('理解意义','力与位移点积 → 定义 → 线性 / 分段可加 / 反向变号'),
('两型关系','弧长参数 → 单位切向量 → 方向余弦 → 切向分量乘弧长'),
('直接计算','选参数 / 选 x 或 y → 同步替换微分 → 起终点决定上下限'),
('对称性与选择','同时看函数、微分、方向；变量不单值时分段')],
'正文按分支顺序学习；证明可展开，例题紧跟方法。'),
('section52-map.svg','5.2 · Green 公式及其应用',['平面边界','联系区域'],[
('理解公式','完整边界 + 正方向 + 场光滑；公共边反向抵消'),
('构造公式','未闭合 → 补线再减；内部有奇点 → 挖洞并计入内边界'),
('计算应用','求偏导差 → 二重积分 / 面积；空间曲线先消元与投影'),
('路径无关与全微分','检查定义域 → 换路径 / 求参数 / 求原函数 → 端点差')],
'注意：Green 可用于有孔区域；偏导相等推出路径无关需核对定义域。'),
('section53-map.svg','5.3 · 第二型曲面积分',['沿指定侧','累积通量'],[
('理解意义','场的法向分量 × 实际面积；换侧变号'),
('两型关系','三个有向投影面积元 = 对应法向分量 × 实际面积元'),
('分项投影','各项投到对应坐标面 → 定符号 → 消元 → 写投影域'),
('对称性','函数与法向同时配对；先投影后二重积分判断更稳妥'),
('合一投影','三项统一到同一平面；单位法向分母与面积根号抵消')],
'参数法与叉积计算放在扩展；封闭面及补面方法接续 5.4。'),
('section54-map.svg','5.4 · Gauss 公式及其应用',['封闭面通量','联系体积分'],[
('理解公式与散度','完整外边界 + 内部光滑；散度表示局部净流出'),
('直接计算','求散度 → 写立体范围 → 选直角 / 柱 / 球坐标'),
('补面法','开放曲面 → 补成封闭外边界 → 总通量减去补面'),
('挖洞法','排除奇点 → 内边界朝孔洞 → 用易算的小球联系原曲面')],
'使用前依次核对：是否封闭？哪一侧？内部是否有未处理奇点？'),
('section55-map.svg','5.5 · Stokes 公式',['空间闭路','联系所张面'],[
('理解边界与定向','边界环流 = 旋度通量；右手规则匹配曲线与曲面'),
('计算旋度','先写三个分量 → 逐项求偏导 → 核对中间分量符号'),
('选面与计算','确定边界 → 选圆盘 / 平面片 → 用单位法向或向量面积元'),
('联系与整合','平面情形退化为 Green；区分梯度、散度、旋度')],
'换面前检查：同一有向边界，且场在新曲面附近光滑。')]
for args in maps:mindmap(*args)

# Space curve and its exact xy projection: a=1, x=cos(t)/sqrt(2), y=sin(t), z=1-x.
def path(points,closed=True):
    return 'M'+' L'.join(f'{x:.2f},{y:.2f}' for x,y in points)+(' Z' if closed else '')
def proj(x,y,z):return (285+145*x-85*y,330+35*x+48*y-110*z)
pts=[];shadow=[]
for k in range(121):
 t=2*math.pi*k/120;x=math.cos(t)/math.sqrt(2);y=math.sin(t)
 pts.append(proj(x,y,1-x));shadow.append(proj(x,y,0))
b=text(25,36,'空间曲线先消元，再投影到平面',25,weight=650)
for endpoint,label in [(proj(1.7,0,0),'x'),(proj(0,1.7,0),'y'),(proj(0,0,1.9),'z')]:
 b+=line(285,330,*endpoint,arrow=True)+text(endpoint[0]+6,endpoint[1],label,18)
b+=f'<path d="{path(shadow)}" fill="#d9e8ee" stroke="#69889b" stroke-width="2"/>'
for i in [0,30,60,90]:b+=line(*pts[i],*shadow[i],dash=True)
b+=f'<path d="{path(pts)}" fill="#e2f0e9" fill-opacity=".65" stroke="#177f7a" stroke-width="3"/>'
b+=line(*pts[15],*pts[20],arrow=True)+line(*shadow[15],*shadow[20],arrow=True)
b+=text(45,440,'原曲线：z = 1 − x',20)+text(45,474,'投影：2x² + y² = 1',20)
b+=rect(590,80,455,330)+text(615,120,'同一组 x、y 坐标',23,'#177f7a',600)
for i,t in enumerate(['① 用平面约束 z = 1 − x 消元','② 同步替换 dz = −dx','③ 代入球面得到投影椭圆','④ 核对投影方向，再用 Green']):b+=text(615,177+i*52,t,20)
svg('green_projection.svg','空间交线与平面投影','a=1，倾斜空间交线竖直投影到椭圆，箭头保持参数行进方向。',b)

# A tangent parallelogram and its three signed coordinate projections.
b=text(25,36,'实际小曲面块与三个有向投影',25,weight=650)
for i,(axis,lab,formula) in enumerate([(0,'yz 面','dy dz = nₓ dS'),(1,'zx 面','dz dx = nᵧ dS'),(2,'xy 面','dx dy = n𝓏 dS')]):
 ox=180+i*355;oy=295
 def p(v):x,y,z=v;return (ox+65*x-42*y,oy+20*x+30*y-75*z)
 a=(.5,.4,1);v=(1,0,.6);w=(0,1,.4)
 quad=[a,tuple(a[j]+v[j] for j in range(3)),tuple(a[j]+v[j]+w[j] for j in range(3)),tuple(a[j]+w[j] for j in range(3))]
 flat=[tuple(0 if j==axis else q[j] for j in range(3)) for q in quad]
 for e,l in [((2.1,0,0),'x'),((0,2.1,0),'y'),((0,0,2.1),'z')]:b+=line(*p((0,0,0)),*p(e),arrow=True)+text(p(e)[0]+4,p(e)[1],l,16)
 b+=f'<path d="{path([p(q) for q in flat])}" fill="#f5d99c" fill-opacity=".65" stroke="#b27b1c" stroke-width="2"/>'
 for q,f in zip(quad,flat):b+=line(*p(q),*p(f),dash=True)
 b+=f'<path d="{path([p(q) for q in quad])}" fill="#c4e3dc" stroke="#177f7a" stroke-width="2"/>'
 center=tuple(a[j]+.5*v[j]+.5*w[j] for j in range(3));tip=tuple(center[j]+[-.6,-.4,1][j]*.6 for j in range(3))
 b+=line(*p(center),*p(tip),arrow=True)+text(p(tip)[0]-13,p(tip)[1]-8,'n',18)
 b+=text(ox,390,lab,23,'#177f7a',600,'middle')+text(ox,430,formula,22,anchor='middle')
b+=text(32,465,'投影的绝对值由面积缩放决定；正负号跟随对应法向分量。图示选择向上法向。',18)
svg('surface_projection.svg','小曲面块的三个有向投影','同一小平行四边形分别投到yz、zx、xy面，相应面积等于实际面积乘法向分量。',b)

# Normal parity on paired hemispheres.
b=text(25,36,'上下对称时，函数与法向要一起配对',25,weight=650)
for ox,title,Rup,Rdn,result,c in [(270,'R = 1：偶函数','+1','+1','贡献相消 → 总积分为 0','#59739c'),(790,'R = z：奇函数','+|z|','−|z|','贡献同号 → 上半球积分加倍','#177f7a')]:
 b+=f'<circle cx="{ox}" cy="220" r="110" fill="#eef5f7" stroke="#7694a3" stroke-width="2"/>'
 b+=line(ox-145,220,ox+145,220,dash=True)
 b+=line(ox,145,ox,83,arrow=True)+line(ox,295,ox,357,arrow=True)
 b+=text(ox+13,115,'n_z > 0',18)+text(ox+13,343,'n_z < 0',18)
 b+=text(ox,180,'R = '+Rup,20,anchor='middle')+text(ox,275,'R = '+Rdn,20,anchor='middle')
 b+=text(ox,395,title,22,c,600,'middle')+text(ox,435,result,21,c,anchor='middle')
b+=text(30,480,'以球面外侧为例：比较的是 R n_z dS，而不是只比较 R。',17)
svg('surface_symmetry.svg','球面外侧的上下对称性','外法向的z分量在上下反号，R为偶时相消，为奇时同号。',b)

# Two paraboloids with shared circle: use radial section, then chosen disk.
b=text(25,36,'边界固定，改选更简单的所张圆盘',25,weight=650)
# exact r-z section: z=2r² and z=3-r², intersection at r=1,z=2
for ox,mode in [(280,'curves'),(800,'disk')]:
 def p2(r,z):return (ox+145*r,365-85*z)
 b+=line(*p2(-1.45,0),*p2(1.45,0),arrow=True)+text(ox+217,373,'x',18)
 b+=line(*p2(0,0),*p2(0,3.5),arrow=True)+text(ox+10,64,'z',18)
 if mode=='curves':
  for f,col in [(lambda r:2*r*r,'#177f7a'),(lambda r:3-r*r,'#59739c')]:
   points=[p2(-1.18+2.36*k/100,f(-1.18+2.36*k/100)) for k in range(101)]
   b+=f'<path d="{path(points,False)}" stroke="{col}" stroke-width="3" fill="none"/>'
  b+=text(35,430,'联立：r² = 1，z = 2',22)+text(35,465,'左图为轴截面；两交点绕 z 轴旋转形成交线。',17)
 else:
  b+=f'<ellipse cx="{ox}" cy="195" rx="145" ry="37" fill="#d5eae3" stroke="#177f7a" stroke-width="3"/>'
  b+=line(ox,195,ox,110,arrow=True)+text(ox+12,125,'n = (0, 0, 1)',18)
  b+=text(590,430,'选圆盘：z = 2，x² + y² ≤ 1',22)+text(590,465,'从 +z 侧看，边界逆时针对应上侧法向。',17)
 b+=text(ox+12,195,'2',17)
 if mode=='curves':
  for r in [-1,1]:x,y=p2(r,2);b+=f'<circle cx="{x}" cy="{y}" r="5" fill="#b27b1c"/>'
b+=line(488,230,567,230,arrow=True)
svg('stokes_disk.svg','两个抛物面的交线及替换圆盘','轴截面显示两曲面交于x=±1,z=2，右图选水平单位圆盘并取上侧。',b)
print('Built 6 knowledge maps and 4 lesson figures')
