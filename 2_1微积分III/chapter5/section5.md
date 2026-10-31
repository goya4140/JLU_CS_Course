# 5.5 Stokes公式

[第5章目录](README.md) · [作业解读（2题）](homework5.md)

> 学习目标：理解旋度与右手定向，通过选择简单所张曲面计算空间闭路积分。

## 理解 Stokes 公式：空间闭曲线与所张曲面

![5.5 知识导图：右手方向、旋度、选面计算与公式整合](../assets/section55-map.svg)

本节按“理解边界关系 → 匹配右手方向 → 计算旋度 → 选择简单曲面”学习。依据《微积分总结》PDF第13页、教材第213—218页。

### 从 Green 走向空间

Green 联系平面闭曲线与平面区域；Stokes 联系空间闭曲线与以它为边界的有向曲面。右侧是**旋度场的第二型曲面积分**，所以复用5.3的投影与定向方法。

<!-- study:result|Stokes 公式及条件 -->

设 $\Sigma$ 是可定向、分片光滑曲面，分段光滑边界 $\Gamma=\partial\Sigma$ 与其法向满足右手规则，$\mathbf F=(P,Q,R)$ 在包含曲面的开邻域内一阶连续可微，则

$$
\oint_\Gamma Pdx+Qdy+Rdz
=\iint_\Sigma(R_y-Q_z)dydz+(P_z-R_x)dzdx+(Q_x-P_y)dxdy
=\iint_\Sigma\operatorname{curl}\mathbf F\cdot\mathbf n\,dS.
$$

曲面有多条边界时须全部计入，并由曲面方向统一诱导。Stokes 需要的是所张曲面附近的光滑性；与 Gauss 的“封闭面内部光滑”条件不同。

<!-- /study -->

### 右手规则：由曲线方向选曲面侧

![倾斜圆盘与边界的右手定向](../assets/stokes.svg)

右手四指顺着边界行进，拇指指向曲面法向。从法向指向的那一侧朝曲面看，边界呈逆时针。题目若说“从 $+z$ 侧看逆时针”，对可投到 $xy$ 面的平面片应选 $n_z>0$；顺时针则选 $n_z<0$。

不能只按三维图在屏幕上看起来的顺逆时针判断。若题目写“从某轴方向看”，先将观察位置和朝向翻译清楚，再选法向。

<details class="study-extension" id="stokes-green-proof">
<summary>扩展：为什么 Stokes 可以从 Green 得到？</summary>

设上侧曲面为 $z=g(x,y)$，其边界投影为平面正向闭曲线。先在曲线积分中代入 $z=g$ 和 $dz=g_xdx+g_ydy$，得到

$$
\oint_\Gamma\mathbf F\cdot d\mathbf r
=\oint_L(P+Rg_x)dx+(Q+Rg_y)dy.
$$

这里 $P,Q,R$ 均已复合 $z=g(x,y)$。按链式法则求平面 Green 的偏导差，可得

$$
\partial_x(Q+Rg_y)-\partial_y(P+Rg_x)
=(Q_x-P_y)+(Q_z-R_y)g_x+(R_x-P_z)g_y.
$$

它正是 $\operatorname{curl}\mathbf F\cdot(-g_x,-g_y,1)$，再利用5.3的向量面积元就得到 Stokes。该推导在足够光滑的图形曲面上直接成立；一般分片曲面可分块，公共边反向抵消。

当 $g=0$ 时只剩旋度第三分量 $Q_x-P_y$，Stokes 就退化为平面 Green 公式。

</details>

## 计算 Stokes：先展开旋度，再匹配面积元

### 旋度的分量计算

<!-- study:concept|旋度是向量，描述局部环流的轴向与强弱 -->

$$
\operatorname{curl}\mathbf F=\nabla\times\mathbf F
=(R_y-Q_z,\ P_z-R_x,\ Q_x-P_y).
$$

教材也写为 $\operatorname{rot}\mathbf F$。分量顺序与叉积一致，中间分量应是 $P_z-R_x$。

<!-- /study -->

<details class="study-extension" id="curl-expansion">
<summary>扩展：旋度行列式如何逐项展开？</summary>

形式记号为

$$
\nabla\times\mathbf F=
\begin{vmatrix}
\mathbf i&\mathbf j&\mathbf k\\
\partial_x&\partial_y&\partial_z\\
P&Q&R
\end{vmatrix}
=\mathbf i(R_y-Q_z)-\mathbf j(R_x-P_z)+\mathbf k(Q_x-P_y).
$$

第二项有代数余子式的负号，因此最终第二分量为 $P_z-R_x$。这里第二行是求导算子，要作用于第三行对应函数。

例如本地第三次作业填空题4的 $\mathbf A=(xz,y^4,z^2)$：第一分量 $0-0=0$，第二分量 $x-0=x$，第三分量 $0-0=0$，故旋度为 $(0,x,0)$。

</details>

### 标准计算步骤

**识别闭曲线及方向 → 求旋度 → 选所张曲面 → 匹配法向 → 用5.3算曲面积分 → 复核符号**。

两种等价写法任选一种，不能混用：

|所用面积|配套公式|
|---|---|
|实际曲面面积元 $dS$|$\operatorname{curl}\mathbf F\cdot\mathbf n\,dS$，其中 $\mathbf n$ 必须单位化|
|投影面积元 $dxdy$|上侧用 $\operatorname{curl}\mathbf F\cdot(-g_x,-g_y,1)dxdy$，下侧取负|

### 例1 水平圆：联系 Green 并核对方向

$L:x^2+y^2=a^2,z=h$，从 $+z$ 侧看逆时针，求 $\oint_L(-y\,dx+x\,dy)$。

**本例知识点**：水平圆选水平圆盘，上侧法向与逆时针边界匹配。

$\mathbf F=(-y,x,0)$，旋度为 $(0,0,2)$。选圆盘法向 $(0,0,1)$，得到 $I=2\pi a^2$。若方向顺时针，结果为 $-2\pi a^2$。

### 例2 倾斜大圆：区分实际面积与投影面积

$L$ 为单位球面与 $x+y+z=0$ 的交线，从 $+z$ 侧看逆时针，求 $\oint_L(y\,dz-z\,dy)$。

**本例知识点**：旋度为常向量、所张面为平面时，可用单位法向乘实际面积；也可用向量面积元投影计算。

$\mathbf F=(0,-z,y)$，旋度为 $(2,0,0)$。选平面内单位圆盘，法向 $\mathbf n=(1,1,1)/\sqrt3$，其 $z$ 分量为正，实际面积为 $\pi$，故

$$
I=(2,0,0)\cdot\frac{(1,1,1)}{\sqrt3}\,\pi=\frac{2\pi}{\sqrt3}.
$$

若改投 $xy$ 面，$z=-x-y$，上侧向量面积元 $(1,1,1)dxdy$；投影椭圆 $x^2+y^2+(x+y)^2\le1$ 的面积是 $\pi/\sqrt3$，所以 $I=2\cdot\pi/\sqrt3$。不能将单位法向直接乘投影面积，否则少了面积修正。

## 选简单曲面：边界固定，曲面可以改变

### 换面的条件

在保持同一有向边界的前提下，可选更容易计算的曲面，但新曲面必须可定向、方向匹配，且场在新曲面附近一阶连续可微。不能选穿过场奇点的曲面。

<!-- study:warning|选面自由来自适用条件，并非任何曲面都能替换 -->

两张曲面若都满足 Stokes 条件，旋度通量都等于同一个边界积分。所选面不必是题目给出的球面或抛物面的一部分；平面圆盘往往更简单。

<!-- /study -->

### 例3 两个曲面的交线，改选圆盘：教材例5.2

$\Gamma$ 为 $z=2(x^2+y^2)$ 与 $z=3-x^2-y^2$ 的交线，从 $+z$ 侧看逆时针，求

$$
I=\oint_\Gamma z^3dx+x^3dy+y^3dz.
$$

**本例知识点**：先联立曲面确定边界，再选最简单的所张曲面；旋度的许多分量可能因法向而不贡献。

联立得 $x^2+y^2=1,z=2$。选圆盘 $\Sigma:z=2,x^2+y^2\le1$，取上侧。场 $\mathbf F=(z^3,x^3,y^3)$ 的旋度为 $(3y^2,3z^2,3x^2)$，点积只保留第三分量，因此

$$
I=\iint_D3x^2dxdy
=3\int_0^{2\pi}\int_0^1r^3\cos^2\theta\,drd\theta=\frac{3\pi}{4}.
$$

![两张曲面的交线及可替换的水平圆盘](../assets/stokes_disk.svg)

图中上下两张曲面只用来确定交线。选圆盘后，不必分别计算两张曲面的面积元。

<details class="study-extension" id="stokes-constant-curl">
<summary>扩展：旋度为常向量时，平面面积法怎样简化？</summary>

若 $\operatorname{curl}\mathbf F=\mathbf c$ 为常向量，所选面为面积 $A$ 的平面片、单位法向为 $\mathbf n$，则 $I=(\mathbf c\cdot\mathbf n)A$。

但旋度不是常向量时，不能直接把点积当成常数提出积分。可以先利用平面方程化简，若所得函数在该面上确为常数，才使用“常数乘面积”。

</details>

## 梯度、散度、旋度与三大公式的联系

### 三种运算的输入与输出

![标量等高线的梯度与旋转场的旋度](../assets/gradient_curl.svg)

左图 $u=x^2+y^2$ 是标量函数，梯度 $(2x,2y)$ 垂直等高线并指向函数增加方向；右图 $\mathbf F=(-y,x,0)$ 是向量场，旋度为 $(0,0,2)$，表示局部环流的轴向为正 $z$ 方向。

|运算|输入|输出|用途|
|---|---|---|---|
|梯度 $\nabla u=(u_x,u_y,u_z)$|标量函数|向量场|找势函数，使用端点差|
|散度 $\nabla\cdot\mathbf F$|向量场|标量函数|Gauss 转三重积分|
|旋度 $\nabla\times\mathbf F$|向量场|向量场|Stokes 转第二型曲面积分|

### 三个公式，分别连接什么？

![Green、Gauss、Stokes 的对象关系](../assets/theorems.svg)

|公式|边界上的量|内部或所张面上的量|方向|
|---|---|---|---|
|Green|平面闭曲线环流|区域内 $Q_x-P_y$ 的二重积分|区域在左侧|
|Gauss|完整封闭面的通量|立体内散度的三重积分|所围立体外侧|
|Stokes|空间闭曲线环流|所张面上旋度的通量|边界与法向符合右手规则|

<details class="study-extension" id="vector-identities">
<summary>扩展：两个零恒等式，以及不能误记为零的拉普拉斯算子</summary>

若相应函数二阶连续可微，混合偏导相等给出

$$
\operatorname{curl}(\nabla u)=\mathbf0,\qquad
\operatorname{div}(\operatorname{curl}\mathbf F)=0.
$$

例如第一式的第一分量为 $u_{zy}-u_{yz}=0$，其他分量同理；第二式逐项展开后，六个混合偏导成对抵消。

但 $\operatorname{div}(\nabla u)=u_{xx}+u_{yy}+u_{zz}=\Delta u$ 一般不为零，例如 $u=x^2+y^2+z^2$ 时为6。

</details>

本节自检：旋度中间分量的符号是否正确？边界方向与法向是否匹配？实际面积和投影面积是否配套？所选曲面是否经过奇点？

---

[进入本节作业解读](homework5.md) · [上一节：5.4](section4.md) · [章末总结与自测](summary.md)
