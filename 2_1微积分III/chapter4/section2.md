# 4.2 第一型曲面积分

[第4章目录](README.md) · [作业解读（6题）](homework2.md)

> 学习目标：分清实际曲面与投影区域，掌握面积元、投影法和参数法。

## 第一型曲面积分与面积元

曲线部分已经走完，现在把“一小段长度”换成“一小块面积”。本节依次介绍曲面积分、投影面积元与参数面积元，为下一节的例题准备工具。

<!-- study:concept|第一型曲面积分：定义与性质 -->

曲面分成小块，实际面积为 $\Delta S_i$，则

$$
\iint_\Sigma f\,dS=\lim_{\max\operatorname{diam}\Delta\Sigma_i\to0}\sum_i f(M_i)\Delta S_i.
$$

取 $f=1$ 得曲面面积，取面密度得薄壳质量。第一型曲面积分也具有线性、分片相加、估值和方向无关等性质。

<!-- /study -->

### 图形曲面的投影公式

<!-- study:result|投影法：面积元与计算公式 -->

若 $\Sigma:z=g(x,y)$，投影域为 $D$，且曲面可单值表示，则

$$
dS=\sqrt{1+g_x^2+g_y^2}\,dxdy,
$$

$$
\iint_\Sigma f(x,y,z)dS=\iint_D f(x,y,g(x,y))\sqrt{1+g_x^2+g_y^2}\,dxdy.
$$

<!-- /study -->

可类比斜面的实际面积与水平投影面积：坡度越大，修正因子越大。换成 $x=h(y,z)$ 或 $y=k(z,x)$ 时，公式相应换字母。

![曲面投影和面积修正](../assets/projection.svg)

<!-- study:process|面积元的几何推导 -->

**用一个可精确测量的小斜面推公式**

图中曲面是 $z=x+y$，投影是单位正方形。橙色小块的投影边长都是0.4，投影面积为0.16。在曲面上，两条边对应向量 $(0.4,0,0.4)$ 与 $(0,0.4,0.4)$。

**向量**是带方向的量，可用分量写成 $(a,b,c)$；两个向量的**叉积**垂直于它们所在平面，其长度等于这两条边构成的平行四边形面积。本例叉积为 $(-0.16,-0.16,0.16)$，长度为 $0.16\sqrt3\approx0.2771$，所以实际小块比投影大。

将0.4改为微小的 $dx,dy$，对一般曲面 $z=g(x,y)$，两条切向边成为 $(1,0,g_x)dx$ 与 $(0,1,g_y)dy$。叉积为 $(-g_x,-g_y,1)dxdy$，取长度就得到面积修正因子 $\sqrt{1+g_x^2+g_y^2}$。这里 $g_x,g_y$ 是固定另一坐标时曲面的两种坡度。

**数值检查**：整个单位方形上的平面 $z=x+y$，投影面积为1，真实面积为 $\sqrt3$。如果计算出1，说明漏了斜面的伸缩。

<!-- /study -->

<!-- study:warning|投影范围与分片 -->

投影域由**全部限制条件**确定。例如 $z=x^2+y^2,0\le z\le2$ 投影为圆盘 $x^2+y^2\le2$。对整球面投影时，上下半球对应同一圆盘，需要分片或改用球面参数。

<!-- /study -->

### 参数曲面的面积元

<!-- study:result|参数曲面的面积元 -->

设 $\mathbf r(u,v)$ 覆盖曲面一次，则

$$
dS=\lVert\mathbf r_u\times\mathbf r_v\rVert\,dudv.
$$

<!-- /study -->

<details class="study-extension" id="parametric-extension">
<summary>扩展说明：参数偏导的含义，以及表中四种曲面的参数式与面积元推导</summary>

#### 先读懂参数式和偏导向量

参数式 $\mathbf r(u,v)=(x(u,v),y(u,v),z(u,v))$ 表示：给定两个参数 $u,v$，就确定曲面上的一个点。两个参数可以是角度、高度或平面坐标，不一定就是 $x,y$。

$\mathbf r_u,\mathbf r_v$ 是分别对两个参数求偏导得到的向量；每个坐标分量都要分别求导：

$$
\mathbf r_u=\frac{\partial\mathbf r}{\partial u}
=\left(\frac{\partial x}{\partial u},\frac{\partial y}{\partial u},\frac{\partial z}{\partial u}\right),
$$

$$
\mathbf r_v=\frac{\partial\mathbf r}{\partial v}
=\left(\frac{\partial x}{\partial v},\frac{\partial y}{\partial v},\frac{\partial z}{\partial v}\right).
$$

固定 $v$，让 $u$ 增加很小的 $du$，曲面上的位移近似为 $\mathbf r_u\,du$；固定 $u$，另一方向的位移近似为 $\mathbf r_v\,dv$。因此小曲面块可以用这两条切向边构成的平行四边形近似，其面积为

$$
\left\|(\mathbf r_u\,du)\times(\mathbf r_v\,dv)\right\|
=\|\mathbf r_u\times\mathbf r_v\|\,du\,dv.
$$

这里把 $du\,dv$ 理解为参数平面上的正面积元。曲面光滑且参数化正则时，这个局部近似给出面积元 $dS$。叉积通常不能直接改成两个向量长度相乘，因为两条切向边未必垂直。

#### 叉积具体怎么算？先展开三个分量

这里的 $\times$ 表示两个向量的**叉积**；公式中参与运算的是 $\mathbf r_u$ 和 $\mathbf r_v$ 这两个偏导向量。

对 $\mathbf A=(A_1,A_2,A_3)$、$\mathbf B=(B_1,B_2,B_3)$，按下列顺序计算。其中 $\mathbf i=(1,0,0),\mathbf j=(0,1,0),\mathbf k=(0,0,1)$ 是三个坐标轴方向的单位向量。

$$
\mathbf A\times\mathbf B
=\begin{vmatrix}
\mathbf i&\mathbf j&\mathbf k\\
A_1&A_2&A_3\\
B_1&B_2&B_3
\end{vmatrix}.
$$

沿第一行展开时，三个位置的符号依次为“正、负、正”：

$$
\begin{aligned}
\mathbf A\times\mathbf B
={}&(A_2B_3-A_3B_2)\mathbf i\\
&-(A_1B_3-A_3B_1)\mathbf j\\
&+(A_1B_2-A_2B_1)\mathbf k.
\end{aligned}
$$

将中间的负号乘进去，得到三个坐标分量：

$$
\boxed{\mathbf A\times\mathbf B
=(A_2B_3-A_3B_2,\ A_3B_1-A_1B_3,\ A_1B_2-A_2B_1)}.
$$

特别注意：**第二个分量是 $A_3B_1-A_1B_3$**。例如上一段斜面的两条切向量为 $(1,0,1)$ 和 $(0,1,1)$，逐项代入得到

$$
\begin{aligned}
C_x&=0\cdot1-1\cdot1=-1,\\
C_y&=1\cdot0-1\cdot1=-1,\\
C_z&=1\cdot1-0\cdot0=1.
\end{aligned}
$$

所以叉积是 $(-1,-1,1)$，再取长度 $\sqrt{(-1)^2+(-1)^2+1^2}=\sqrt3$，才得到面积修正因子。**先求叉积向量，再求向量长度，是两步运算。** 下面每种曲面也都按这三个分量展开。

#### 1. 球面：先用角度确定点的位置

半径为 $a>0$ 的球面，取 $\phi$ 为从 $+z$ 轴量起的极角，$\theta$ 为水平投影从 $+x$ 轴量起的方位角。

点的高度为 $z=a\cos\phi$，到 $z$ 轴的水平距离为 $\rho=a\sin\phi$。再把水平距离分解到两条坐标轴：

$$
x=\rho\cos\theta=a\sin\phi\cos\theta,\quad
y=\rho\sin\theta=a\sin\phi\sin\theta,\quad
z=a\cos\phi.
$$

所以球面参数式为 $\mathbf r(\phi,\theta)=(a\sin\phi\cos\theta,a\sin\phi\sin\theta,a\cos\phi)$。分别求偏导：

$$
\mathbf r_\phi=(a\cos\phi\cos\theta,a\cos\phi\sin\theta,-a\sin\phi),
$$

$$
\mathbf r_\theta=(-a\sin\phi\sin\theta,a\sin\phi\cos\theta,0).
$$

记 $\mathbf r_\phi\times\mathbf r_\theta=(C_x,C_y,C_z)$，将两条偏导向量逐项代入通用公式：

$$
\begin{aligned}
C_x&=(a\cos\phi\sin\theta)\cdot0
-(-a\sin\phi)(a\sin\phi\cos\theta)\\
&=a^2\sin^2\phi\cos\theta,\\[4pt]
C_y&=(-a\sin\phi)(-a\sin\phi\sin\theta)
-(a\cos\phi\cos\theta)\cdot0\\
&=a^2\sin^2\phi\sin\theta,\\[4pt]
C_z&=(a\cos\phi\cos\theta)(a\sin\phi\cos\theta)\\
&\quad-(a\cos\phi\sin\theta)(-a\sin\phi\sin\theta)\\
&=a^2\sin\phi\cos\phi(\cos^2\theta+\sin^2\theta)\\
&=a^2\sin\phi\cos\phi.
\end{aligned}
$$

把三个分量组成向量，并提出公因子：

$$
\mathbf r_\phi\times\mathbf r_\theta
=a^2\sin\phi\,(\sin\phi\cos\theta,\sin\phi\sin\theta,\cos\phi).
$$

括号内向量的长度为 $\sqrt{\sin^2\phi(\cos^2\theta+\sin^2\theta)+\cos^2\phi}=1$。当 $0\le\phi\le\pi$ 时，$\sin\phi\ge0$，于是

$$
\boxed{dS=a^2\sin\phi\,d\phi\,d\theta}.
$$

整球取 $0\le\phi\le\pi,0\le\theta\le2\pi$；上半球取 $0\le\phi\le\pi/2$。极角从 $+z$ 轴量起，所以北极为 $\phi=0$、赤道为 $\phi=\pi/2$。极点及参数区间接缝的重复表示不影响曲面积分。

#### 2. 圆柱侧面：一个参数控制角度，一个参数控制高度

圆柱 $x^2+y^2=a^2$ 的水平截面是半径为 $a$ 的圆，故令 $x=a\cos\theta,y=a\sin\theta$；高度独立变化，直接令 $z=v$：

$$
\mathbf r(\theta,v)=(a\cos\theta,a\sin\theta,v).
$$

分别求偏导并叉乘：

$$
\mathbf r_\theta=(-a\sin\theta,a\cos\theta,0),\qquad
\mathbf r_v=(0,0,1),
$$

记 $\mathbf r_\theta\times\mathbf r_v=(C_x,C_y,C_z)$，则

$$
\begin{aligned}
C_x&=(a\cos\theta)\cdot1-0\cdot0=a\cos\theta,\\
C_y&=0\cdot0-(-a\sin\theta)\cdot1=a\sin\theta,\\
C_z&=(-a\sin\theta)\cdot0-(a\cos\theta)\cdot0=0.
\end{aligned}
$$

所以叉积向量与其长度分别为

$$
\mathbf r_\theta\times\mathbf r_v=(a\cos\theta,a\sin\theta,0),
$$

$$
\|\mathbf r_\theta\times\mathbf r_v\|
=\sqrt{a^2\cos^2\theta+a^2\sin^2\theta}=a.
$$

所以

$$
\boxed{dS=a\,d\theta\,dv}.
$$

几何上，这是“周向小弧长 $a\,d\theta$ × 竖直小高度 $dv$”。整周取 $0\le\theta\le2\pi$；若侧面高度为 $0\le z\le h$，则 $0\le v\le h$。这里只参数化侧面，不包含上下底盘。

#### 3. 圆锥：水平半径与高度由锥面方程联系

为避免把位置向量 $\mathbf r$ 和标量半径混淆，这里把表中的半径参数 $r$ 改写成 $\rho=\sqrt{x^2+y^2}\ge0$。锥面 $z=k\rho$ 中，$k$ 为常数，故可取

$$
\mathbf r(\rho,\theta)=(\rho\cos\theta,\rho\sin\theta,k\rho).
$$

其中 $\rho$ 控制沿母线走到哪里，$\theta$ 控制绕轴转到哪个方向。分别求偏导：

$$
\mathbf r_\rho=(\cos\theta,\sin\theta,k),\qquad
\mathbf r_\theta=(-\rho\sin\theta,\rho\cos\theta,0).
$$

记 $\mathbf r_\rho\times\mathbf r_\theta=(C_x,C_y,C_z)$，逐项计算：

$$
\begin{aligned}
C_x&=\sin\theta\cdot0-k\cdot(\rho\cos\theta)
=-k\rho\cos\theta,\\
C_y&=k\cdot(-\rho\sin\theta)-\cos\theta\cdot0
=-k\rho\sin\theta,\\
C_z&=\cos\theta\cdot(\rho\cos\theta)
-\sin\theta\cdot(-\rho\sin\theta)\\
&=\rho(\cos^2\theta+\sin^2\theta)=\rho.
\end{aligned}
$$

因此，叉积向量为

$$
\mathbf r_\rho\times\mathbf r_\theta
=(-k\rho\cos\theta,-k\rho\sin\theta,\rho).
$$

再对三个分量平方、相加、开根号，得到长度：

$$
\|\mathbf r_\rho\times\mathbf r_\theta\|
=\sqrt{k^2\rho^2(\cos^2\theta+\sin^2\theta)+\rho^2}
=\rho\sqrt{1+k^2}.
$$

因此

$$
\boxed{dS=\rho\sqrt{1+k^2}\,d\rho\,d\theta}.
$$

也可以看成“母线小长度 $\sqrt{1+k^2}\,d\rho$ × 周向小弧长 $\rho\,d\theta$”。例如 $z=\sqrt{x^2+y^2}$ 且 $0\le z\le2$ 时，$k=1$，范围为 $0\le\rho\le2,0\le\theta\le2\pi$。锥顶是一个点，不影响面积积分。

#### 4. 图形面：直接把两个平面坐标作为参数

对 $z=g(x,y)$，直接用 $x,y$ 控制曲面上的点，即

$$
\mathbf r(x,y)=(x,y,g(x,y)).
$$

分别求偏导并叉乘：

$$
\mathbf r_x=(1,0,g_x),\qquad\mathbf r_y=(0,1,g_y),
$$

将这两个向量放入行列式：

$$
\mathbf r_x\times\mathbf r_y
=\begin{vmatrix}
\mathbf i&\mathbf j&\mathbf k\\
1&0&g_x\\
0&1&g_y
\end{vmatrix}.
$$

逐项展开，三个分量为

$$
\begin{aligned}
C_x&=0\cdot g_y-g_x\cdot1=-g_x,\\
C_y&=g_x\cdot0-1\cdot g_y=-g_y,\\
C_z&=1\cdot1-0\cdot0=1.
\end{aligned}
$$

所以

$$
\mathbf r_x\times\mathbf r_y=(-g_x,-g_y,1),
\qquad
\|\mathbf r_x\times\mathbf r_y\|
=\sqrt{(-g_x)^2+(-g_y)^2+1^2}.
$$

所以

$$
\boxed{dS=\sqrt{1+g_x^2+g_y^2}\,dx\,dy}.
$$

这里的参数域就是曲面在 $Oxy$ 平面上的投影域。可见投影公式是参数曲面公式的一种特殊情形。

</details>

叉积的长度是两条微小切向边所形成平行四边形的面积。交换 $u,v$ 会使叉积反向，但长度不变，这也说明第一型面积积分与定向无关。

|曲面|参数与范围|面积元|
|---|---|---|
|球面半径 $a$|$x=a\sin\phi\cos\theta,y=a\sin\phi\sin\theta,z=a\cos\phi$|$a^2\sin\phi\,d\phi d\theta$；整球 $0\le\phi\le\pi,0\le\theta\le2\pi$|
|圆柱侧面|$x=a\cos\theta,y=a\sin\theta,z=v$|$a\,d\theta dv$|
|圆锥 $z=kr$|$x=r\cos\theta,y=r\sin\theta,z=kr$|$r\sqrt{1+k^2}\,drd\theta$|
|图形面 $z=g(x,y)$|$\mathbf r(x,y)=(x,y,g(x,y))$|$\sqrt{1+g_x^2+g_y^2}\,dxdy$|

球面公式里的 $\phi$ 是从 $+z$ 轴量起的极角，上半球取 $0\le\phi\le\pi/2$。不要混用纬度参数与极角参数。

![球面参数小块与极角面积因子](../assets/sphere_patch.svg)

**球面读图**：相同的极角宽度 $d\phi$ 与方位角宽度 $d\theta$，在赤道附近形成较宽的小块，在北极附近形成很窄的小块。沿经线的小边约为 $a\,d\phi$；沿纬线的小边约为 $a\sin\phi\,d\theta$。两边互相垂直，相乘得到 $a^2\sin\phi\,d\phi d\theta$。右图画出了面积因子 $\sin\phi$，从极点的0增至赤道的1。

![圆柱侧面与展开后的参数小块](../assets/cylinder_patch.svg)

**圆柱读图**：把半径1、高度2的侧面沿一条母线剪开并展开，得到宽 $2\pi$、高2的长方形。橙色块在圆柱与展开图中是同一块：宽度等于弧长 $d\theta$，高度为 $dz$。半径换为 $a$ 后，宽度变成 $a\,d\theta$，所以侧面面积元是 $a\,d\theta dz$。

球面的参数网格会向极点收拢，圆柱的参数网格不会。两个公式的差异可从这两幅图直接看出。

## 曲面积分完整例题

上一节得到面积元，本节按“写曲面与范围 → 选投影或参数 → 替换函数和面积元 → 计算”的同一顺序，练习斜平面、抛物面、球面与圆柱侧面。

### 例5 斜平面上的密度：本地第4章作业填空题3

$\Sigma:x/2+y+z=1$ 在第一卦限的部分，求 $\iint_\Sigma(x+2y+2z+4)dS$。

曲面写成 $z=1-x/2-y$，故 $g_x=-1/2,g_y=-1$，$dS=3dxdy/2$。投影域为 $x\ge0,y\ge0,x/2+y\le1$，三角形面积是 $1$。又在曲面上 $x+2y+2z+4=6$，于是 $I=6\cdot(3/2)\cdot1=9$。

这里先用曲面方程化简被积函数，可避免不必要的逐项积分。

### 例6 抛物面：补充例题

本题为抛物面补充练习；原始作业计算题2为锥面 $z=\sqrt{x^2+y^2}$，见 [4.2 作业解读](../chapter4/homework2.md)。

$\Sigma:z=x^2+y^2,0\le z\le2$，求 $\iint_\Sigma(x^2+y^2)dS$。

投影域是半径 $\sqrt2$ 的圆盘，$dS=\sqrt{1+4x^2+4y^2}\,dxdy$。在投影平面改用极坐标：

![被平面截下的抛物面与投影圆盘](../assets/paraboloid_domain.svg)

左图的橙色边界满足 $z=2$。将它代入 $z=x^2+y^2$，得到 $x^2+y^2=2$。右图是从上往下投影后得到的圆盘：半径 $\sqrt2$，包括边界内部的所有点。因此极坐标范围是 $0\le r\le\sqrt2,0\le\theta\le2\pi$；不是仅沿边界圆做曲线积分。

沿曲面从中心向外走，坡度越来越大，因此同样的投影面积在外圈对应更大的真实曲面面积。式中的 $\sqrt{1+4r^2}$ 正在记录这种变化。

$$
I=\int_0^{2\pi}\int_0^{\sqrt2}r^3\sqrt{1+4r^2}\,drd\theta.
$$

令 $u=1+4r^2$，$r^3dr=(u-1)du/32$，则

$$
I=\frac\pi{16}\int_1^9(u^{3/2}-u^{1/2})du
=\frac\pi{16}\left[\frac25u^{5/2}-\frac23u^{3/2}\right]_1^9
=\frac{149\pi}{30}.
$$

两个因子承担不同工作：$\sqrt{1+4r^2}$ 把投影面积还原为曲面面积，$r$ 把直角坐标面积换成极坐标面积；两者都要保留。

### 例7 球面的平方积分

在整球面 $x^2+y^2+z^2=a^2$ 上，计算 $\iint_\Sigma x^2dS$。

三个平方积分相等，总和为 $a^2\cdot4\pi a^2$，因此 $\iint_\Sigma x^2dS=4\pi a^4/3$。整球上 $\iint_\Sigma xdS=0$，但上半球上 $\iint_\Sigma zdS=\pi a^3$，后者可由球面参数直接验证。

### 例8 圆柱侧面：本地第4章作业填空题5

$\Sigma:x^2+y^2=a^2,0\le z\le h$，求 $\iint_\Sigma x^2dS$。

取 $x=a\cos\theta,y=a\sin\theta,z=v$，$dS=a\,d\theta dv$。结果为

$$
I=a^3\int_0^h dv\int_0^{2\pi}\cos^2\theta\,d\theta=\pi a^3h.
$$

题目只给圆柱侧面，不应添加上下底面。

---

[进入本节作业解读](homework2.md) · [上一节：4.1](section1.md) · [下一节：4.3](section3.md)
