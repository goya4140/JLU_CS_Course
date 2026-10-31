# 5.3 第二型曲面积分

[第5章目录](README.md) · [作业解读（7题）](homework3.md)

> 学习目标：从通量与两型关系理解有向面积元，掌握分项投影、对称性和合一投影。

## 理解通量：曲面的侧与法向

![5.3 知识导图：通量、两型关系、分项投影、对称性与合一投影](../assets/section53-map.svg)

本节按“指定侧 → 理解有向投影 → 分项计算 → 对称性 → 合一计算”学习。依据《微积分总结》PDF第9—10页、教材第194—204页。

### 从流体穿过小平面块理解通量

设 $\mathbf F=(P,Q,R)$ 是流速，曲面取定侧的单位法向量为 $\mathbf n$。穿过小块的有向体积流量是

<!-- study:concept|通量只保留场的法向分量 -->

$$
d\Phi=\mathbf F\cdot\mathbf n\,dS,\qquad
\Phi=\iint_\Sigma\mathbf F\cdot\mathbf n\,dS.
$$

$dS$ 是实际面积元；$\mathbf F\cdot\mathbf n$ 是法向分量。沿所选法向穿过为正，反向穿过为负，相切时为零。若 $\mathbf F$ 为速度，这给体积流量；质量流量应使用质量通量场 $\rho\mathbf F$，密度为1时二者数值相同。

<!-- /study -->

![竖直流穿过斜面以及换侧后的通量](../assets/flux.svg)

例如 $z=x+y$ 在单位方形上方的斜面，$\mathbf F=(0,0,1)$。上侧单位法向为 $(-1,-1,1)/\sqrt3$，实际面积为 $\sqrt3$，通量是 $(1/\sqrt3)\sqrt3=1$。换成下侧后为 $-1$。

### 上下侧、内外侧与基本性质

|指定侧|判断方式|
|---|---|
|上侧、下侧|分别看 $n_z>0$、$n_z<0$|
|朝正 x、正 y 方向的一侧|分别看 $n_x>0$、$n_y>0$|
|封闭曲面外侧、内侧|法向分别指向所围立体之外、之内|

法向是垂直于曲面的方向，上侧法向不一定竖直。圆柱侧面的外侧通常沿径向，不能统一称为上侧。

第二型曲面积分对被积场线性；曲面分片且侧相容时可相加；**换侧后积分整体变号**。

<details class="study-extension" id="surface-orientation">
<summary>扩展：什么叫可定向曲面？为什么要选单位法向？</summary>

可定向曲面能连续选取一致的单位法向；本节讨论分片光滑、可定向的曲面。莫比乌斯带无法连续选取全局一致的法向，不在本节全局通量公式的直接适用范围内。

单位法向只表示方向，长度为1。若使用未单位化法向 $\mathbf N$，应先除以 $\|\mathbf N\|$ 才能与实际面积元 $dS$ 配合。合一投影中使用的则是乘积 $\mathbf n\,dS$，它可以直接写成未单位化向量乘投影面积元，后面会推导。

</details>

## 有向投影面积元与两型曲面积分的关系

### 三个方向余弦对应三个投影

设 $\mathbf n=(\cos\alpha,\cos\beta,\cos\gamma)$，夹角分别相对坐标轴正方向。小曲面块的投影面积绝对值是实际面积乘夹角余弦的绝对值；有向投影的符号跟相应法向分量一致。

<!-- study:result|两型关系的三个基本等式 -->

$$
dy\,dz=\cos\alpha\,dS,\quad dz\,dx=\cos\beta\,dS,\quad dx\,dy=\cos\gamma\,dS,
$$

$$
\iint_\Sigma P\,dy\,dz+Q\,dz\,dx+R\,dx\,dy
=\iint_\Sigma(P\cos\alpha+Q\cos\beta+R\cos\gamma)dS.
$$

这里左侧的面积元带有方向；右侧 $dS$ 非负，方向已包含在余弦中。两边都表示 $\iint_\Sigma\mathbf F\cdot\mathbf n\,dS$。

<!-- /study -->

![小曲面块与三个坐标面的有向投影](../assets/surface_projection.svg)

<details class="study-extension" id="surface-relation-proof">
<summary>扩展推导：为什么投影面积等于法向分量乘实际面积？</summary>

用切平面上的两条小边向量 $\mathbf a,\mathbf b$ 近似曲面小块。叉积 $\mathbf a\times\mathbf b$ 垂直于小块，其长度是平行四边形面积，方向按所选侧调整。其三个分量为

$$
(a_yb_z-a_zb_y,\ a_zb_x-a_xb_z,\ a_xb_y-a_yb_x).
$$

第三分量就是两条边投到 $xy$ 面后组成的有向平行四边形面积；另一方面，该分量也等于 $\|\mathbf a\times\mathbf b\|\cos\gamma$。极限下得到 $dx\,dy=\cos\gamma\,dS$。另外两项同理。

再将三个等式代入 $Pdy\,dz+Qdz\,dx+Rdx\,dy$，合并并沿曲面积分，就得到两型关系。

</details>

|比较|第一型曲面积分|第二型曲面积分|
|---|---|---|
|累积对象|标量函数乘实际面积|向量场的法向分量乘实际面积|
|面积元|$dS$|有向 $dy\,dz,dz\,dx,dx\,dy$，或 $\mathbf n\,dS$|
|换侧|固定标量函数时不变|变号|
|方向信息|不需要选侧|必须保留在法向或有向面积元中|

## 分项投影法：各项投到对应坐标面

### 三种投影与符号

教材称“分面投影法”，即三类积分项分别投到对应坐标面；遇到多值曲面时还需分片。

|积分项|曲面表示与投影域|变成普通二重积分|
|---|---|---|
|$Pdy\,dz$|$x=h(y,z),D_{yz}$|$\pm\iint_{D_{yz}}P(h(y,z),y,z)dy\,dz$，符号看 $n_x$|
|$Qdz\,dx$|$y=k(z,x),D_{zx}$|$\pm\iint_{D_{zx}}Q(x,k(z,x),z)dz\,dx$，符号看 $n_y$|
|$Rdx\,dy$|$z=g(x,y),D_{xy}$|$\pm\iint_{D_{xy}}R(x,y,g(x,y))dx\,dy$，符号看 $n_z$|

右侧已经是普通的无向面积积分，符号在前面单独处理。步骤是：**看积分项 → 选对应投影 → 判断侧 → 消元 → 写投影域 → 积分**。

### 例1 平面下侧的单项积分：本地第三次作业选择题2

$\Sigma:x+y+z=1$ 在第一卦限取下侧，求 $\iint_\Sigma zdxdy$。

**本例知识点**：$dxdy$ 项投到 $xy$ 面；下侧的有向投影取负。

投影 $D:x,y\ge0,x+y\le1$，代入 $z=1-x-y$，有

$$
I=-\int_0^1\int_0^{1-x}(1-x-y)dy\,dx=-\frac16.
$$

### 坐标恒定与零贡献

若 $n_z=0$，则 $Rdxdy=Rn_zdS=0$；例如竖直柱面侧面上该项为零。同理，$n_x=0$ 时 $Pdy\,dz$ 为零，$n_y=0$ 时 $Qdz\,dx$ 为零。判断依据是该项对应的法向分量。

### 例2 六个面的贡献：教材例3.1

$\Sigma$ 是单位立方体 $[0,1]^3$ 的全部外表面，求 $\iint_\Sigma xyz\,dy\,dz$。

**本例知识点**：单项积分只保留对应法向分量非零的面；两个平行面的符号由外法向决定。

$y=0,1$ 与 $z=0,1$ 四个面上 $n_x=0$，贡献为零。面 $x=1$ 的 $n_x=1$，积分为 $\int_0^1\int_0^1yz\,dy\,dz=1/4$；面 $x=0$ 的 $n_x=-1$，但代入后 $xyz=0$，贡献为零。总和为 $1/4$。

### 例3 球面投影为什么要分上下两片？

单位球面 $\Sigma$ 取外侧，求 $\iint_\Sigma zdxdy$。

**本例知识点**：同一圆盘投影对应上下两片曲面；两片法向符号与函数符号都要保留。

在 $D:x^2+y^2\le1$ 上，上半球 $z=\sqrt{1-x^2-y^2}$，下半球 $z=-\sqrt{1-x^2-y^2}$，所以

$$
I=\iint_D\sqrt{1-x^2-y^2}dxdy
-\iint_D(-\sqrt{1-x^2-y^2})dxdy
=2\cdot2\pi\int_0^1r\sqrt{1-r^2}dr=\frac{4\pi}{3}.
$$

不能只在圆盘上代入一个 $z$ 分支，也不能因 $z$ 关于上下半球反号就认定相消。

## 对称性：同时检查函数与法向

### 从上下半球看“偶零奇倍”的来源

设曲面关于 $xy$ 面对称，且所选侧在反射下相容，例如关于该面对称的封闭曲面取外侧。上下对应点的 $n_z$ 反号，而 $dS$ 相同。对单项 $Rdxdy=Rn_zdS$：

<!-- study:result|有向面积元也参与对称性配对 -->

- 若 $R(x,y,-z)=R(x,y,z)$，上下贡献相消。
- 若 $R(x,y,-z)=-R(x,y,z)$，上下贡献相同，可用上半片积分的两倍。

上述结论要求法向在反射下按所述方式配对；只看曲面形状和函数奇偶性不够。

<!-- /study -->

![对称球面上，场与法向符号如何共同决定相消或加倍](../assets/surface_symmetry.svg)

例3中 $R=z$ 为奇函数，且 $n_z$ 也反号，乘积同号，因此加倍。若改成 $R=1$，函数同号而法向反号，总积分为零。其他坐标面可用同样方法分析对应的积分项。

更稳妥的计算策略是先投影，写成带正确正负号的普通二重积分，再利用投影区域的奇偶性和轮换对称性。

## 合一投影法：三项统一到一个坐标面

### 从单位法向与实际面积元得到公式

对 $z=g(x,y)$ 的上侧，法向与实际面积元分别为

$$
\mathbf n=\frac{(-g_x,-g_y,1)}{\sqrt{1+g_x^2+g_y^2}},\qquad
dS=\sqrt{1+g_x^2+g_y^2}dxdy.
$$

<!-- study:result|合一投影：根号抵消，三个分量统一计算 -->

$$
\mathbf n\,dS=(-g_x,-g_y,1)dxdy,
$$

$$
I=\iint_D\left[-P(x,y,g)g_x-Q(x,y,g)g_y+R(x,y,g)\right]dxdy.
$$

下侧将整个表达式取负。所有 $z$ 均需用 $g(x,y)$ 替换，不再额外乘面积根号。

<!-- /study -->

![单位法向、实际面积元及根号抵消的过程](../assets/normal_area.svg)

<details class="study-extension" id="unified-projection-proof">
<summary>扩展推导：法向怎么求？为什么可以把三项放到同一平面？</summary>

把曲面写成 $H(x,y,z)=z-g(x,y)=0$，梯度 $\nabla H=(-g_x,-g_y,1)$ 垂直于曲面，第三分量为正，所以指向上侧。除以它的长度即得到单位法向。

把两型关系逐项写成 $Pn_xdS+Qn_ydS+Rn_zdS$，再代入单位法向和 $dS$。每一项的分母都与面积根号相消，分别成为 $-Pg_xdxdy,-Qg_ydxdy,Rdxdy$，三项自然落在同一投影域中。

若投到其他坐标面，$x=h(y,z)$ 朝正 $x$ 一侧用 $\mathbf n\,dS=(1,-h_y,-h_z)dydz$；$y=k(z,x)$ 朝正 $y$ 一侧用 $\mathbf n\,dS=(-k_x,1,-k_z)dzdx$。投影为多值时需分片，不能用一个分支覆盖整面。

</details>

### 例4 同一锥面：分项投影与合一投影比较（教材例3.3）

$\Sigma:z=\sqrt{x^2+y^2},0\le z\le h$，取相对锥内立体的外侧，即下侧，计算 $\iint_\Sigma xdydz+ydzdx+zdxdy$。

**本例知识点**：合一投影避免三项分别求曲面分支；外侧在本题中对应下侧。锥顶一个点不影响积分，计算可在去掉锥顶的光滑部分进行。

分项投影时，$xdy\,dz$ 项在前后两片上贡献同号，得到

$$
I_x=2\int_0^h\int_{-z}^z\sqrt{z^2-y^2}\,dy\,dz=\frac{\pi h^3}{3}.
$$

同理 $I_y=\pi h^3/3$。第三项下侧取负，$I_z=-2\pi\int_0^hr^2dr=-2\pi h^3/3$，所以 $I=0$。

合一投影时，记 $r=\sqrt{x^2+y^2}$，下侧向量面积元为 $(x/r,y/r,-1)dxdy$，点积为

$$
x\frac xr+y\frac yr-z=\frac{x^2+y^2}{r}-r=0.
$$

于是立即得到 $I=0$。几何上，场 $(x,y,z)$ 沿锥面母线，与侧面相切，通量为零。

### 例5 抛物面下侧：教材例3.4

$\Sigma:z=(x^2+y^2)/2,0\le z\le2$ 取下侧，求 $\iint_\Sigma(z^2+x)dydz-zdxdy$。

**本例知识点**：下侧整体变号，代入曲面方程后再使用投影域对称性与极坐标。

$D:x^2+y^2\le4$，下侧向量面积元为 $(x,y,-1)dxdy$，所以

$$
I=\iint_D[x(z^2+x)+z]dxdy
=\iint_D\left[\frac{x(x^2+y^2)^2}{4}+x^2+\frac{x^2+y^2}{2}\right]dxdy.
$$

第一项关于 $x$ 为奇函数，积分为零；圆盘内 $\iint_Dx^2dxdy=\frac12\iint_D(x^2+y^2)dxdy$。故

$$
I=\iint_D(x^2+y^2)dxdy=2\pi\int_0^2r^3dr=8\pi.
$$

<details class="study-extension" id="flux-parametric">
<summary>扩展：参数曲面法，以及叉积逐分量的计算</summary>

对 $\mathbf r(u,v)$，若 $\mathbf r_u\times\mathbf r_v$ 指向指定侧，则

$$
I=\iint_E\mathbf F(\mathbf r(u,v))\cdot(\mathbf r_u\times\mathbf r_v)dudv.
$$

方向相反则整体取负；叉积不取长度。第一型面积元才使用 $\|\mathbf r_u\times\mathbf r_v\|dudv$。

例如圆柱侧面 $x^2+y^2=a^2,0\le z\le h$ 取外侧，$\mathbf F=(x,y,z)$。令 $\mathbf r(\theta,v)=(a\cos\theta,a\sin\theta,v)$，则

$$
\mathbf r_\theta=(-a\sin\theta,a\cos\theta,0),\quad\mathbf r_v=(0,0,1).
$$

按 $(a_2b_3-a_3b_2,a_3b_1-a_1b_3,a_1b_2-a_2b_1)$ 展开：

$$
\mathbf r_\theta\times\mathbf r_v
=(a\cos\theta\cdot1-0,\ 0-(-a\sin\theta)\cdot1,\ 0-0)
=(a\cos\theta,a\sin\theta,0).
$$

它沿径向向外，方向正确。点积为 $a^2$，故 $I=\int_0^h\int_0^{2\pi}a^2d\theta dv=2\pi a^2h$。场的 $z$ 分量在侧面上没有法向贡献。

</details>

### 方法选择与自检

单项优先考虑对应平面的分项投影；多项且曲面能方便写成单值图形时比较合一投影；柱面等参数简单时可用参数法。若曲面封闭或易补成封闭面，继续学习5.4的 Gauss 方法。

每题复核：侧是否明确？是否漏分支？曲面变量是否全部替换？是否多乘了面积根号？

---

[进入本节作业解读](homework3.md) · [上一节：5.2](section2.md) · [下一节：5.4](section4.md)
