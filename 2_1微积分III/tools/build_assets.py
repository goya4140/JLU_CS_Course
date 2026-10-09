from pathlib import Path
import html,math,urllib.request,concurrent.futures
R=Path(__file__).resolve().parents[1];A=R/'assets';(A/'vendor').mkdir(exist_ok=True)
def svg(name,title,sub,body,h=500):
 s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{h}" viewBox="0 0 1000 {h}" role="img"><title>{html.escape(title)}</title><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="#187c87"/></marker></defs><rect width="1000" height="{h}" rx="18" fill="#f5fafb"/><style>text{{font-family:"PingFang SC","Microsoft YaHei",sans-serif;fill:#213d49}}.line{{fill:none;stroke:#187c87;stroke-width:3}}.small{{font-size:19px}}.label{{font-size:22px}}</style><text x="38" y="47" font-size="28" font-weight="bold">{title}</text><text x="38" y="78" class="small">{sub}</text>{body}</svg>''';(A/(name+'.svg')).write_text(s)
def txt(x,y,s,cl='label'):return f'<text x="{x}" y="{y}" class="{cl}">{html.escape(s)}</text>'
def path(d,c='#187c87',w=3):return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}"/>'
def arrow(x,y,X,Y):return f'<path d="M{x},{y} L{X},{Y}" class="line" marker-end="url(#a)"/>'
def box(x,y,w,h,title,lines):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="white" stroke="#bcd4da"/>'+txt(x+18,y+34,title)+''.join(txt(x+18,y+68+28*i,l,'small') for i,l in enumerate(lines))
for name,title,branches in [
 ('map4','第4章 · 第一型积分知识地图',[('曲线积分',['密度 × 弧长 ds','参数化 → 一元定积分','圆弧 / 折线 / 空间曲线']),('曲面积分',['密度 × 面积 dS','投影 / 参数化 → 二重积分','图形面 / 球面 / 柱面']),('性质与技巧',['线性、分段、估值','对称性：域与函数一起看','面积、长度与平均值']),('物理应用',['质量 → 质心','距离平方 → 转动惯量','距离向量 → 引力'])]),
 ('map5','第5章 · 第二型积分知识地图',[('第二型曲线积分',['力 · 位移：Pdx + Qdy + Rdz','参数方向决定上下限','全微分 → 终点减起点']),('Green 与路径无关',['平面闭曲线 → 二重积分','补线、挖洞、面积','单连通域与偏导相等']),('第二型曲面积分',['通量：向量场 · 法向量','上侧 / 下侧 / 内侧 / 外侧','向量面积元保留符号']),('Gauss 与 Stokes',['封闭面 → 散度的体积分','空间闭曲线 → 旋度的通量','补面、右手方向、奇点'])])]:
 b=box(350,105,300,82,'积累的对象决定微元',['先认清几何对象，再选择方法'])
 for i in range(4):
  x=35+(i%2)*500;y=250+(i//2)*180
  if i<2:b+=arrow(500,187,x+215,y)
  else:b+=f'<path d="M500,187 L500,418 L{x+215},418 L{x+215},{y}" class="line" marker-end="url(#a)"/>'
 for i,(t,ls) in enumerate(branches):
  x=35+(i%2)*500;y=250+(i//2)*180;b+=box(x,y,430,155,t,ls)
 svg(name,title,'从几何意义出发，把概念、计算与题型连起来。',b,635)
svg('theorems','三个公式的关系：边界与内部','先辨认积分对象，再检查封闭性、方向和光滑条件。',
 box(40,145,290,220,'Green · 平面',['边界：平面闭曲线','内部：平面区域','微分：Qₓ - Pᵧ','结果：二重积分'])+box(355,145,290,220,'Gauss · 通量',['边界：封闭曲面','内部：三维立体','微分：散度 div F','结果：三重积分'])+box(670,145,290,220,'Stokes · 环流',['边界：空间闭曲线','内部：所张曲面','微分：旋度 curl F','结果：第二型曲面积分']),415)
urls={'marked.js':'https://cdn.jsdelivr.net/npm/marked@15.0.12/marked.min.js','katex.js':'https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.js','katex.css':'https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.css'}
def dl(item):
 n,u=item
 if not (A/'vendor'/n).exists():urllib.request.urlretrieve(u,A/'vendor'/n)
with concurrent.futures.ThreadPoolExecutor() as ex:list(ex.map(dl,urls.items()))
import re
css=(A/'vendor/katex.css').read_text();fonts=set(re.findall(r'url\((fonts/[^)]+)\)',css));(A/'vendor/fonts').mkdir(exist_ok=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:list(ex.map(lambda f:None if (A/'vendor'/f).exists() else urllib.request.urlretrieve('https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/'+f,A/'vendor'/f),fonts))
for pkg in ['katex@0.16.22','marked@15.0.12']:
 try:urllib.request.urlretrieve('https://cdn.jsdelivr.net/npm/'+pkg+('/LICENSE.md' if pkg.startswith('marked@') else '/LICENSE'),A/'vendor'/(pkg.split('@')[0]+'-LICENSE'))
 except Exception:pass
print('Created',len(list(A.glob('*.svg'))),'figures;',len(fonts),'font resources')
