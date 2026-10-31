# 5.4 Gauss公式及其应用

[第5章目录](README.md) · [作业解读（4题）](homework4.md)

> 学习目标：理解散度与封闭面通量，掌握直接体积分、补面和挖洞。

## 理解 Gauss 公式：封闭曲面与所围体积

![5.4 知识导图：散度、直接计算、补面与挖洞](../assets/section54-map.svg)

本节按“理解净流出 → 核对封闭外侧 → 直接化体积分 → 补面或挖洞”学习。依据《微积分总结》PDF第11—12页、教材第206—212页。

### 从第二型曲面积分到三重积分

<!-- study:result|Gauss 公式：完整封闭边界，取外侧 -->

设空间有界区域 $\Omega$ 的边界分片光滑并取外侧，$\mathbf F=(P,Q,R)$ 在包含 $\overline\Omega$ 的开邻域内一阶连续可微，则

$$
\iint_{\partial\Omega}Pdy\,dz+Qdz\,dx+Rdx\,dy
=\iiint_\Omega(P_x+Q_y+R_z)dV.
$$

$\partial\Omega$ 必须是全部边界；整体取内侧时，右侧加负号。有空腔时，内边界相对材料区域的外法向指向空腔。

<!-- /study -->

### 散度是什么？

<!-- study:concept|散度描述单位体积的局部净流出 -->

$$
\operatorname{div}\mathbf F=\nabla\cdot\mathbf F=P_x+Q_y+R_z.
$$

正值对应局部净流出，负值对应净流入，零表示流入流出平衡，不表示场本身为零。Gauss 把内部各点的净流出累加，等于外表面的总通量。

<!-- /study -->

![三个具体向量场的散度比较](../assets/divergence.svg)

图中只画 $z=0$ 的截面，散度仍按三维场计算。$(x,y,z)$ 的散度为3，$(x,-y,0)$ 的散度为0，$(-x,-y,-z)$ 的散度为 $-3$。

<details class="study-extension" id="gauss-proof">
<summary>扩展推导：为什么公共面抵消？如何从一个分量得到 Gauss？</summary>

若 $\Omega$ 可表示为 $z_1(x,y)\le z\le z_2(x,y)$，底面投影为 $D$，则

$$
\iiint_\Omega R_zdV
=\iint_D[R(x,y,z_2)-R(x,y,z_1)]dxdy.
$$

外侧上表面的 $Rdxdy$ 为正向投影，下表面为负向投影，侧面在这一项中的贡献为零，所以右侧等于 $\iint_{\partial\Omega}Rdxdy$。另外两项同理，相加得到公式。

一般立体可以分块处理；相邻小块公共面的外法向相反，内部通量成对抵消，只留下完整外边界。

</details>

## 直接计算：求散度后选择体积分坐标

### 计算流程

**确认全部封闭面 → 调整为外侧 → 求散度 → 写出立体 → 选坐标 → 积分**。散度为常数时可直接乘体积；散度不是常数时仍需积分。

### 例1 球面外侧与内侧

半径 $a$ 的球面，场 $\mathbf F=(x,y,z)$，求通量。

**本例知识点**：散度为常数时，将曲面通量转成常数乘体积；内侧整体变号。

散度为3，外侧通量为 $3\cdot4\pi a^3/3=4\pi a^3$；内侧为 $-4\pi a^3$。在球面上也有 $\mathbf F\cdot\mathbf n=a$，直接乘球面积可复核外侧结果。

### 例2 半球体的全部外表面：教材例4.1

$\Sigma$ 是上半球体 $x^2+y^2+z^2\le a^2,z\ge0$ 的全部外表面，求

$$
I=\iint_\Sigma xz^2dy\,dz+(x^2y-z^3)dz\,dx+(2xy+y^2z)dx\,dy.
$$

**本例知识点**：先识别全部边界，求散度后用球坐标；体积元含雅可比因子。

$P_x=z^2,Q_y=x^2,R_z=y^2$，故散度为 $x^2+y^2+z^2=r^2$。取球坐标

$$
x=r\sin\varphi\cos\theta,\quad y=r\sin\varphi\sin\theta,\quad z=r\cos\varphi,
$$

范围 $0\le r\le a,0\le\varphi\le\pi/2,0\le\theta\le2\pi$，$dV=r^2\sin\varphi\,drd\varphi d\theta$，所以

$$
I=\int_0^{2\pi}\int_0^{\pi/2}\int_0^ar^4\sin\varphi\,drd\varphi d\theta=\frac{2\pi a^5}{5}.
$$

如果题目只指上半球曲面，就要另外检查底盘贡献；本题底盘上 $R=2xy$，朝下通量为 $-\iint_D2xy\,dxdy=0$，因此两种表述在本题中恰好同值，理由应写出。

### 常用体积元

|立体特征|坐标与体积元|常见范围|
|---|---|---|
|直角边界|$dV=dxdydz$|按截面确定|
|绕 z 轴对称|柱坐标 $dV=r\,drd\theta dz$|$r,\theta$ 由投影决定，$z$ 由上下曲面决定|
|球或球壳|球坐标 $dV=r^2\sin\varphi\,drd\varphi d\theta$|$\varphi$ 是与正 z 轴的夹角|

坐标选择取决于散度和立体的共同形状，不取决于原来的曲面方程看起来是否复杂。

## 补面法：开放曲面先补成完整外边界

### 补面的方向与积分等式

![补上底盘形成封闭外表面](../assets/gauss.svg)

若 $\Sigma+B=\partial\Omega$，且两部分均按 $\Omega$ 的外侧取向，则

<!-- study:result|原曲面等于封闭面减去补面 -->

$$
\iint_\Sigma\mathbf F\cdot\mathbf n\,dS
=\iiint_\Omega\operatorname{div}\mathbf FdV
-\iint_B\mathbf F\cdot\mathbf n\,dS.
$$

先写这个等式再代入数值。上方立体的底盘，外法向朝下；补面通量可能为正、为负或为零。

<!-- /study -->

### 例3 抛物面补底盘：教材例4.2

$\Sigma:z=1-x^2-y^2\ge0$ 取上侧，求

$$
I=\iint_\Sigma(y^2-x)dydz+(z^2-y)dzdx+(x^2-z)dxdy.
$$

**本例知识点**：原曲面不是封闭面；补面外法向和“减去补面”是两次独立的符号判断。

补 $B:z=0,x^2+y^2\le1$，取下侧，与原面围成 $0\le z\le1-r^2$。散度为 $-3$，体积为 $2\pi\int_0^1(1-r^2)rdr=\pi/2$，所以封闭面通量为 $-3\pi/2$。

补面上 $dxdy$ 取负，$R=x^2$，故

$$
I_B=-\iint_Dx^2dxdy
=-\int_0^{2\pi}\int_0^1r^3\cos^2\theta\,drd\theta=-\frac\pi4.
$$

于是 $I=-3\pi/2-(-\pi/4)=-5\pi/4$。补面的负号不能在移项时丢失。

<details class="study-extension" id="gauss-hemisphere">
<summary>补充例题：半球面补盘，补面通量为什么不是零？</summary>

上半球 $x^2+y^2+z^2=a^2,z\ge0$ 取外侧，$\mathbf F=(x,y,z+1)$。散度为3，半球体内积分为 $2\pi a^3$。底盘法向为 $(0,0,-1)$，场的竖直分量为1，故补面通量 $-\pi a^2$。

因此原半球面通量为 $2\pi a^3+\pi a^2$。不能因为补面位于 $z=0$ 就认定其通量为零，应代入完整的 $R$。

</details>

## 挖洞法：排除内部奇点

### 散度为零仍可能有非零通量

<!-- study:warning|使用 Gauss 要检查立体内部，不只检查表面 -->

$$
\mathbf F=\frac{(x,y,z)}{(x^2+y^2+z^2)^{3/2}}
$$

在原点外散度为零，在原点未定义。若封闭面包围原点，不能直接对整块内部使用 Gauss。

<!-- /study -->

![球面积与法向场强相互抵消，球面通量保持不变](../assets/gauss_singularity.svg)

### 例4 椭球外侧的径向通量：教材例4.3

$\Sigma:x^2/a^2+y^2/b^2+z^2/c^2=1$ 取外侧，$a,b,c>0$，求上述场的通量。

**本例知识点**：挖去小球后，在光滑的剩余区域用 Gauss；小球是空腔，其法向相对剩余区域指向球心。

记 $r=\sqrt{x^2+y^2+z^2}$，在 $r>0$ 处有

$$
P_x=r^{-3}-3x^2r^{-5},\quad Q_y=r^{-3}-3y^2r^{-5},\quad R_z=r^{-3}-3z^2r^{-5},
$$

所以散度为 $3r^{-3}-3r^2r^{-5}=0$。在椭球内部挖去小球 $r\le\varepsilon$，记小球向外法向为 $\mathbf n_+$。剩余区域内边界法向为 $-\mathbf n_+$，Gauss 给

$$
\iint_\Sigma\mathbf F\cdot\mathbf n\,dS
-\iint_{S_\varepsilon}\mathbf F\cdot\mathbf n_+\,dS=0.
$$

小球上 $\mathbf F\cdot\mathbf n_+=1/\varepsilon^2$，面积 $4\pi\varepsilon^2$，因此原积分为 $4\pi$。椭球形状的复杂度没有进入最后计算。

### 方法选择与自检

|情形|操作|
|---|---|
|完整封闭面、内部光滑|直接用 Gauss，外侧为正，内侧取负|
|有开口、容易补简单面|补面后用 Gauss，再减去补面|
|内部有孤立奇点|先挖洞，在剩余光滑区域用 Gauss|
|直接投影更短|仍可用5.3，不必为用定理而补复杂面|

自检：题目给的是曲面还是立体的全部边界？法向是相对哪个立体的外侧？补面、孔洞的积分是否完整计入？

---

[进入本节作业解读](homework4.md) · [上一节：5.3](section3.md) · [下一节：5.5](section5.md)
