# 5.2 Green公式及其应用

[第5章目录](README.md) · [作业解读（10题）](homework2.md)

> 学习目标：理解 Green 的条件和方向，掌握补线、挖洞、投影、路径无关与全微分。

## 理解 Green 公式：平面边界与区域的联系

![5.2 知识导图：公式、补线挖洞、计算应用与路径无关](../assets/section52-map.svg)

本节按“理解公式 → 构造完整边界 → 简化计算 → 路径无关与全微分”学习。依据《微积分总结》PDF第7—8页、教材第182—192页。

### 区域、完整边界与正方向

单连通域可直观理解为没有孔洞，域内闭路可以在域内缩成一点；环域、穿孔平面有孔洞。**Green 可以用于有孔区域，但必须计入全部边界**。

![Green 公式与内外边界的正方向](../assets/green.svg)

沿正向边界走，区域始终在左手边。因此外边界逆时针，孔洞边界顺时针。

<!-- study:result|Green 公式及使用条件 -->

设有界平面区域 $D$ 的边界分段光滑，$P,Q$ 在包含 $\overline D$ 的开邻域内具有连续一阶偏导数，则

$$
\oint_{\partial D^+}Pdx+Qdy
=\iint_D(Q_x-P_y)dxdy.
$$

使用前检查：**边界完整、方向正向、区域及边界附近无未处理奇点**。反向边界的积分需整体取负。

<!-- /study -->

### 为什么局部贡献最后只留下边界？

把区域分成许多小块，沿各块边界正向积分。相邻两块的公共边走向相反，积分抵消，只留下外边界及孔洞边界；$Q_x-P_y$ 对应局部环流密度。

单位圆上取 $\mathbf F=(-y,x)$。逆时针参数 $(\cos t,\sin t)$ 给 $\oint_L(-y\,dx+x\,dy)=2\pi$；圆盘内 $Q_x-P_y=2$，二重积分也为 $2\pi$。

<details class="study-extension" id="green-proof">
<summary>扩展推导：从一元微积分基本定理到 Green 公式</summary>

先设 $D=\{a\le x\le b,\varphi_1(x)\le y\le\varphi_2(x)\}$。按正向边界，下边界从左向右，上边界从右向左，竖直边上 $dx=0$，因此

$$
\oint_{\partial D^+}Pdx
=\int_a^b[P(x,\varphi_1(x))-P(x,\varphi_2(x))]dx
=-\int_a^b\int_{\varphi_1(x)}^{\varphi_2(x)}P_y\,dy\,dx.
$$

类似地，对可写成 $y$ 型的区域，用水平截线有

$$
\oint_{\partial D^+}Qdy=\iint_DQ_x\,dxdy.
$$

两式相加得到 Green。一般区域分成可处理的小块，公共边反向抵消；有孔区域也用同样办法保留内边界。

</details>

## 构造 Green 公式：补线法与挖洞法

### 补线法：开曲线先闭合，补线积分要算回来

![补线方向与积分账本](../assets/closing.svg)

对 $L:A\to B$，补 $C:B\to A$。若 $L+C$ 为正向边界，则

$$
\int_LPdx+Qdy=\iint_D(Q_x-P_y)dxdy-\int_CPdx+Qdy.
$$

### 例1 补线积分不为零：总结中的上半圆题

$L$ 为半径 $a>0$ 的上半圆，从 $(a,0)$ 逆时针走到 $(-a,0)$，求 $\int_Lx^2dx+(y-x)dy$。

**本例知识点**：补直径形成正向闭路；补线通量不能凭几何形状假定为零。

补线 $C:y=0,x:-a\to a$。$Q_x-P_y=-1$，所以闭路积分为 $-\pi a^2/2$。在 $C$ 上 $dy=0$，但 $x^2dx$ 仍保留：

$$
\int_Cx^2dx+(y-x)dy=\int_{-a}^ax^2dx=\frac{2a^3}{3}.
$$

因此 $I=-\pi a^2/2-2a^3/3$。图中的曲线、补线均应画箭头，再写减去补线的等式。

### 挖洞法：先排除奇点，再使用定理

<!-- study:warning|偏导差为零不能掩盖函数未定义的点 -->

$$
P=-\frac y{x^2+y^2},\qquad Q=\frac x{x^2+y^2}
$$

在原点外满足 $Q_x-P_y=0$，但在原点未定义。若闭曲线围住原点，不能直接对整块内部区域使用 Green。

<!-- /study -->

![奇点、挖洞以及内外边界方向](../assets/singularity.svg)

### 例2 围住原点与没有围住原点：教材例2.4

对正向简单闭曲线 $L$，计算 $\oint_L(xdy-ydx)/(x^2+y^2)$，假定 $L$ 不经过原点。

**本例知识点**：适用条件要检查整个区域；挖去小圆后，环域正向包含外圈逆时针、内圈顺时针。

若原点在外部，场在 $L$ 围成的闭区域附近光滑，Green 给积分为 $0$。若原点在内部，挖去原点附近小圆，记其逆时针边界为 $C_\varepsilon$，则

$$
\oint_L\omega-\oint_{C_\varepsilon}\omega=\iint_{D\setminus B_\varepsilon}0\,dxdy=0.
$$

取 $x=\varepsilon\cos t,y=\varepsilon\sin t,t:0\to2\pi$，得到小圆积分 $\int_0^{2\pi}dt=2\pi$，所以原积分为 $2\pi$。

<details class="study-extension" id="green-ellipse-hole">
<summary>进阶例题：变形分母时，如何选择便于计算的小孔？</summary>

本地第5章第二次作业计算题5：$L:(x-1)^2+y^2=4$ 取正向，求

$$
I=\oint_L\frac{xdy-ydx}{x^2+2y^2}.
$$

在原点外，令 $P=-y/(x^2+2y^2),Q=x/(x^2+2y^2)$，可算出 $Q_x-P_y=0$。原点在 $L$ 内部，挖去小椭圆 $x^2+2y^2=\varepsilon^2$。用 $x=\varepsilon\cos t,y=\varepsilon\sin t/\sqrt2$ 计算其逆时针积分，得

$$
I=\int_0^{2\pi}\frac{\varepsilon^2/\sqrt2}{\varepsilon^2}dt=\sqrt2\pi.
$$

这里外圈等于小圈逆时针积分，是将环域内边界的负号移项后的结果。

</details>

## 计算应用：二重积分、面积与空间曲线投影

### 闭曲线积分化为二重积分

先算 $Q_x-P_y$，再决定使用常数、对称性、极坐标或普通二重积分。偏导差不一定是常数。

### 例3 椭圆上的闭积分：本地第二次作业选择题1

$L:4x^2+y^2=8x$ 为正向边界，求 $\oint_Le^{y^2}dx+xdy$。

**本例知识点**：先求偏导，再利用区域对称性；被积函数复杂不等于转换后的积分复杂。

$Q_x-P_y=1-2ye^{y^2}$，椭圆写成 $4(x-1)^2+y^2=4$。区域关于 $x$ 轴对称，第二项关于 $y$ 为奇函数，积分为零。剩余项为椭圆面积，故 $I=\pi\cdot1\cdot2=2\pi$。

### 面积公式：反过来用边界计算面积

选 $P=-y/2,Q=x/2$，使 $Q_x-P_y=1$，得到

<!-- study:result|正向边界对应正面积 -->

$$
\operatorname{Area}(D)=\frac12\oint_{\partial D^+}(xdy-ydx)
=\oint_{\partial D^+}xdy=-\oint_{\partial D^+}ydx.
$$

有孔区域需使用全部正向边界；反向时右侧为负的有向面积。

<!-- /study -->

![椭圆区域与位置向量扫过的小面积](../assets/area_ellipse.svg)

例如 $x=a\cos t,y=b\sin t,t:0\to2\pi$，$xdy-ydx=abdt$，故椭圆面积为 $\pi ab$。

### 空间曲线先消元，再对投影曲线用 Green

若曲线约束可写为 $z=g(x,y)$，代入时必须同时写 $dz=g_xdx+g_ydy$，先把空间积分重写为投影曲线上的 $\widetilde Pdx+\widetilde Qdy$。需核对投影的行进方向与覆盖次数；本节例题中投影是一次覆盖的简单闭曲线。

### 例4 球面与平面的交线：总结中的投影题

$\Gamma$ 为 $x^2+y^2+z^2=2az$ 与 $x+z=a$ 的交线，$a>0$，从 $+z$ 侧看逆时针，求 $\oint_\Gamma ydx+zdy+xdz$。

**本例知识点**：先用约束替换坐标和微分，再将平面闭路积分化为二重积分。

由 $z=a-x$ 得 $dz=-dx$；代入球面得投影椭圆 $L:2x^2+y^2=a^2$，方向为逆时针。因此

$$
I=\oint_L(y-x)dx+(a-x)dy
=\iint_D[-1-1]dxdy
=-2\pi\frac a{\sqrt2}a=-\sqrt2\pi a^2.
$$

![空间倾斜曲线、平面投影及方向](../assets/green_projection.svg)

图中投影保留 $x,y$ 坐标；同时替换 $dz$ 才能保证新表达式等于原积分。

## 路径无关：从两条路径到闭路

### 判定条件与等价关系

![同一对端点的不同路径以及场的对照](../assets/paths.svg)

路径无关表示：在指定定义域内，固定起终点后，所有允许路径的积分相同。只检查两条路径恰好相等，并不能证明路径无关。

<!-- study:concept|路径无关、闭路为零、全微分与梯度 -->

在连通开域内，对连续场，“任意闭路积分为零”“积分与路径无关”“存在单值 $u$ 使 $du=Pdx+Qdy$”相互等价；最后一项也可写为 $\nabla u=(P,Q)$。

若域进一步单连通且 $P,Q$ 一阶连续可微，则上述条件又等价于 $P_y=Q_x$。

<!-- /study -->

在穿孔域中，偏导相等未必推出路径无关；例2就是反例。单连通是常用的充分条件框架，不是所有势函数存在的必要条件；若已直接构造出单值势函数，就可以使用端点公式。

<details class="study-extension" id="path-independence-proof">
<summary>扩展：为什么“任意闭路为零”能推出“两条路径积分相等”？</summary>

设 $L_1,L_2$ 都从 $A$ 到 $B$。把 $L_1$ 与反向的 $L_2$ 拼成闭路，有

$$
0=\oint_{L_1+(-L_2)}\omega=\int_{L_1}\omega-\int_{L_2}\omega.
$$

所以两条路径积分相等。反过来，若路径无关，一条从 $A$ 出发又回到 $A$ 的闭路可与常值路径比较，积分为零。

固定基点 $A$，定义 $u(x,y)=\int_A^{(x,y)}\omega$。路径无关保证该函数单值；比较一个短水平段或短竖直段的积分，可得 $u_x=P,u_y=Q$。

</details>

### 例5 换成简单路径：教材例2.5

$L$ 为 $(x-2)^2+y^2=4$ 的上半圆，顺时针从 $(0,0)$ 到 $(4,0)$，求

$$
\int_L(1+xe^{2y})dx+(x^2e^{2y}-y)dy.
$$

**本例知识点**：先确认整个定义域满足判定条件，再用同起终点的简单路径替换。

$P_y=2xe^{2y}=Q_x$，场在全平面一阶连续可微，故路径无关。改走 $y=0,x:0\to4$，$dy=0$，于是 $I=\int_0^4(1+x)dx=12$。

## 全微分的题型：求参数、求原函数与方程

### 求参数：利用偏导相等建立恒等式

例如总结中的表达式

$$
\omega=\frac{(x+ky)dx+y\,dy}{(x+y)^2},\quad x+y\ne0.
$$

若它是全微分，则 $P_y=Q_x$。计算

$$
P_y=\frac{(k-2)x-ky}{(x+y)^3},\qquad Q_x=-\frac{2y}{(x+y)^3}.
$$

比较系数得 $k=2$。定义域的两个半平面分别单连通，可验证该值充分；也可直接取 $u=\ln|x+y|-y/(x+y)$，求导得所需的 $P,Q$。

### 求原函数：三种写法解决同一个问题

|方法|操作|注意|
|---|---|---|
|先积分再补函数|由 $u_x=P$ 积分得 $u=\int Pdx+g(y)$，再用 $u_y=Q$ 确定 $g$|积分“常数”可以依赖 $y$|
|沿折线积分|从基点先水平再竖直，累加两段积分|基点及整条折线必须位于定义域内|
|观察凑全微分|识别乘积、复合函数的微分|求导核验，防止漏项|

<!-- study:result|原函数与端点计算公式 -->

$$
du=Pdx+Qdy\quad\Longrightarrow\quad\int_A^BPdx+Qdy=u(B)-u(A).
$$

若折线 $(x_0,y_0)\to(x,y_0)\to(x,y)$ 全在路径无关的定义域内，则可取

$$
u(x,y)=\int_{x_0}^xP(\xi,y_0)d\xi+\int_{y_0}^yQ(x,\eta)d\eta+C.
$$

<!-- /study -->

### 例6 求原函数：教材例2.6

证明 $(2x+\sin y)dx+x\cos y\,dy$ 为全微分并求原函数。

**本例知识点**：判定全微分后，用另一个偏导补全积分产生的未知函数。

$P_y=\cos y=Q_x$，定义域为全平面。由 $u_x=2x+\sin y$ 得 $u=x^2+x\sin y+g(y)$。再由 $u_y=x\cos y+g'(y)=Q$ 得 $g'=0$，所以 $u=x^2+x\sin y+C$。直接求微分可以复核两项。

### 全微分方程：从求原函数到求解

若方程 $Pdx+Qdy=0$ 的左侧恰为 $du$，则解曲线满足 $u(x,y)=C$。例如总结中的

$$
ye^{y^2}dx+(xe^{y^2}+2xy^2e^{y^2})dy=0
$$

左侧等于 $d(xye^{y^2})$，所以隐式解为 $xye^{y^2}=C$。

<details class="study-extension" id="potential-practice">
<summary>作业衔接：更复杂的原函数与空间中的全微分</summary>

本地第二次作业计算题3中，$P=2xy^3-y^2\cos x$，$Q=1-2y\sin x+3x^2y^2$。先积分再补函数可得

$$
u=x^2y^3-y^2\sin x+y.
$$

从 $(0,0)$ 到 $(\pi/2,1)$ 的积分为 $\pi^2/4$。

空间中同理：若 $du=Pdx+Qdy+Rdz$，则积分为 $u(B)-u(A)$。本地计算题1中

$$
(x^2-yz)dx+(y^2-xz)dy+(z^2-xy)dz
=d\left(\frac{x^3+y^3+z^3}{3}-xyz\right).
$$

沿螺线从 $(1,0,0)$ 到 $(1,0,2\pi)$，积分为 $8\pi^3/3$。这里用直接构造原函数完成验证。

</details>

### 方法选择

闭路且场光滑时比较 Green 与直接计算；开路可比较补线与路径无关；有奇点先检查定义域。换路径不需要减去“新增路径”，补线闭合则必须减去补线积分：两种操作的依据不同。

---

[进入本节作业解读](homework2.md) · [上一节：5.1](section1.md) · [下一节：5.3](section3.md)
