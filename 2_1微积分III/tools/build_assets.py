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
svg('elements','微元：ds 与 dS 从哪里来','换元既要替换函数，也要替换曲线长度或曲面面积。',
 path('M70,340 Q210,90 430,310')+path('M245,203 L300,214','#de8a36',9)+arrow(245,203,300,203)+arrow(300,203,300,214)+txt(246,185,'dx')+txt(313,218,'dy')+txt(205,263,'ds² = dx² + dy²')+txt(80,398,'曲线：ds = |r′(t)| dt')+
 '<path d="M590,330 L810,370 L920,190 L700,150 Z" fill="#d4eaf0" stroke="#187c87" stroke-width="3"/>'+arrow(700,150,810,170)+arrow(700,150,650,230)+txt(800,144,'rᵤ du')+txt(563,231,'rᵥ dv')+txt(575,414,'曲面：dS = |rᵤ × rᵥ| du dv'),470)
svg('projection','曲面与投影：面积修正因子','曲面倾斜时，真实面积通常大于它在坐标面上的投影面积。',
 '<path d="M150,215 L410,145 L600,280 L340,350 Z" fill="#c7e5e9" stroke="#187c87" stroke-width="3"/><path d="M150,390 L410,320 L600,390 L340,460 Z" fill="#e9eef1" stroke="#7899a5" stroke-width="2"/>'+''.join(path(f'M{x},{y} L{x},{Y}','#9caeb5',1) for x,y,Y in [(150,215,390),(410,145,320),(600,280,390),(340,350,460)])+txt(250,232,'曲面 z = g(x,y)')+txt(220,398,'投影域 D')+box(655,150,310,160,'上侧法向量',['方向向量：(-gₓ,-gᵧ,1)','第一型：取它的长度','第二型：保留整个向量']),510)
svg('symmetry','对称性要同时检查积分域与函数','第一型微元在镜像变换下保持不变；第二型还需要检查方向。',
 '<circle cx="240" cy="270" r="130" fill="#e2f1f2" stroke="#187c87" stroke-width="3"/>'+path('M75,270 L415,270','#8ca8b2',1)+path('M240,115 L240,430','#8ca8b2',1)+'<circle cx="330" cy="230" r="7" fill="#187c87"/><circle cx="150" cy="230" r="7" fill="#de8a36"/>'+txt(312,205,'(x,y)')+txt(94,205,'(-x,y)')+box(490,140,440,220,'镜像配对',['f(-x,y) = -f(x,y) → 两点贡献抵消','f(-x,y) =  f(x,y) → 两点贡献相等','域不对称时，以上结论不能直接使用','球面上 ∫x²dS = ∫y²dS = ∫z²dS']),470)
svg('centroid','质心与转动惯量：给质量加权','质心用坐标加权；转动惯量用到旋转轴的垂直距离平方加权。',
 '<path d="M100,320 Q200,80 410,220" class="line"/>'+path('M500,130 L500,410','#de8a36',4)+'<circle cx="305" cy="188" r="10" fill="#187c87"/>'+arrow(305,188,500,188)+txt(318,168,'到轴的距离 r')+txt(230,234,'微小质量 dm')+box(600,135,340,225,'同一个 dm，不同权重',['总质量：∫ dm','质心横坐标：∫ x dm / m','绕指定轴：∫ r² dm','r 由轴的位置决定']),475)
svg('orientation','第一型与第二型：方向的差别','沿同一段路径反向行进，长度不变；位移向量反向。',
 arrow(100,200,380,200)+arrow(380,290,100,290)+txt(95,160,'A')+txt(375,160,'B')+txt(100,340,'ds 始终表示非负长度')+txt(100,380,'dx、dy、dz 保留变化的符号')+box(520,150,420,235,'反向后的结果',['第一型：∫ f ds 不变','第二型：∫ F · dr 变号','用参数时：顺着题目方向选区间','第一型反向时需保持正弧长元']),460)
svg('green','Green 公式：正向边界让区域在左手边','外边界逆时针，孔洞内边界顺时针。',
 '<circle cx="270" cy="280" r="155" fill="#dceff1" stroke="#187c87" stroke-width="3"/><circle cx="270" cy="280" r="58" fill="#f5fafb" stroke="#de8a36" stroke-width="3"/>'+arrow(270,125,210,136)+arrow(270,222,305,232)+txt(94,465,'外圈：逆时针')+txt(297,283,'孔洞')+box(540,160,410,220,'边界累积 ↔ 区域累积',['∮ Pdx + Qdy','         ↓ Green','∬ (Qₓ - Pᵧ) dxdy','场在整个积分区域内应足够光滑']),515)
svg('closing','补线：把开曲线变成闭曲线','先明确新增路径的行进方向，再从闭合积分中减去补线积分。',
 path('M130,350 Q280,110 450,230')+arrow(277,187,313,190)+arrow(450,230,130,350)+txt(94,376,'A')+txt(457,225,'B')+txt(270,150,'原曲线 L：A → B')+txt(257,337,'补线 C：B → A')+box(560,160,390,210,'公式账本',['L + C 是正向闭曲线时','∫L + ∫C = ∬D (Qₓ - Pᵧ)','所以 ∫L = ∬D (…) - ∫C','如果闭合方向为负，整体加负号']),480)
svg('singularity','奇点与挖洞：光滑条件不能跳过','偏导相等是局部信息；绕孔洞的积分仍可能不为零。',
 '<circle cx="255" cy="270" r="145" fill="#dceff1" stroke="#187c87" stroke-width="3"/><circle cx="255" cy="270" r="48" fill="#fff" stroke="#de8a36" stroke-width="3"/>'+txt(225,278,'奇点')+arrow(255,125,195,139)+arrow(255,222,285,231)+box(495,140,465,230,'在挖去奇点的环域应用 Green',['外圈逆时针，内圈顺时针','旋度为零 ⇒ 两条正向边界积分和为零','外圈积分 = 内圈逆时针积分','“偏导相等”不能忽略定义域的洞']),480)
svg('flux','通量：向量场穿过曲面的分量','切向分量不穿过曲面；法向分量决定通量的正负。',
 '<ellipse cx="290" cy="305" rx="195" ry="70" fill="#dceff1" stroke="#187c87" stroke-width="3"/>'+arrow(290,305,290,145)+arrow(290,305,410,185)+arrow(290,305,410,305)+txt(238,123,'单位法向量 n')+txt(417,181,'向量场 F')+txt(403,343,'切向分量')+box(580,150,360,215,'向量面积元',['n dS：法向量 × 面积','F · n &gt; 0：沿选定法向穿出'.replace('&gt;','>'),'换侧：n → -n，积分变号','上侧时 n 的 z 分量为正']),470)
svg('gauss','Gauss：封闭面的总通量来自内部散度','开放曲面可补面封闭；所有面应按同一立体的外侧定向。',
 '<path d="M130,325 Q285,50 440,325" fill="#dceff1" stroke="#187c87" stroke-width="3"/><ellipse cx="285" cy="325" rx="155" ry="40" fill="#e9eef1" stroke="#de8a36" stroke-width="3"/>'+arrow(285,140,285,100)+arrow(150,220,108,200)+arrow(420,220,465,200)+arrow(285,325,285,402)+txt(115,453,'补底面：外法向朝下')+box(555,150,400,235,'补面计算',['曲面 Σ + 底面 B = 封闭面','∫Σ F·n dS + ∫B F·n dS','               = ∭Ω div F dV','求原曲面：体积分减去补面通量']),505)
svg('stokes','Stokes：边界方向与法向量配对','从法向量指向的那一侧看，正向边界呈逆时针。',
 '<ellipse cx="280" cy="315" rx="175" ry="75" fill="#dceff1" stroke="#187c87" stroke-width="3"/>'+arrow(280,315,280,120)+arrow(280,240,215,246)+txt(295,139,'法向量 n')+txt(108,432,'右手四指沿边界，拇指沿法向')+box(560,145,390,230,'替换曲面的条件',['边界曲线保持相同','法向量与边界方向匹配','向量场在使用的曲面附近光滑','常选平面圆盘降低计算量']),490)
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
 try:urllib.request.urlretrieve('https://cdn.jsdelivr.net/npm/'+pkg+'/LICENSE',A/'vendor'/(pkg.split('@')[0]+'-LICENSE'))
 except Exception:pass
print('Created',len(list(A.glob('*.svg'))),'figures;',len(fonts),'font resources')
