# 5.1 第二型曲线积分

[第5章目录](README.md) · [作业解读（5题）](homework1.md)

> 学习目标：从做功与两型关系理解方向，掌握参数法、选变量与对称性。

## 理解意义：变力沿有向曲线做功

![5.1 知识导图：做功、两型关系、直接计算与对称性](../assets/section51-map.svg)

本节按“理解做功 → 联系第一型 → 化为一元定积分 → 利用对称性”学习。正文先讲平面曲线，再补充空间形式。依据《微积分总结》PDF第6页、教材第172—179页。

### 从恒力做功到曲线上的微小功

恒力 $\mathbf F=(2,0)$ 沿位移 $(1,0)$ 做功为 $2$，沿 $(0,1)$ 为 $0$，沿 $(-1,0)$ 为 $-2$。点积保留的是力沿位移方向的分量。

![同一个力在三种位移方向上的做功](../assets/work_dot.svg)

曲线上每一小段的运动方向可能不同。设 $\mathbf F=(P,Q)$，微小位移为 $d\mathbf r=(dx,dy)$，则

<!-- study:concept|第二型曲线积分：有向微小功的累积 -->

$$
dW=\mathbf F\cdot d\mathbf r=Pdx+Qdy,\qquad
W=\int_LPdx+Qdy.
$$

$P,Q$ 是力在坐标轴上的分量，$dx,dy$ 是沿行进方向的坐标增量，可以为负。空间情形增加 $Rdz$，即 $\int_\Gamma(Pdx+Qdy+Rdz)$。

<!-- /study -->

### 定义、方向与基本性质

把有向曲线按行进顺序分成小段，取各段上的点 $(\xi_i,\eta_i)$，以该点的力近似整段的力，再将功相加。最大子弧长度趋于零时的极限就是积分。分段光滑曲线上，连续的 $P,Q$ 保证该积分存在。

<details class="study-extension" id="curve-definition">
<summary>扩展：从分割和式写出严格定义</summary>

设分点为 $M_i=(x_i,y_i)$，按起点至终点排列，$\Delta x_i=x_i-x_{i-1}$、$\Delta y_i=y_i-y_{i-1}$，$\lambda$ 是最大子弧长度。若极限存在且与分割、取点无关，定义

$$
\int_LPdx+Qdy
=\lim_{\lambda\to0}\sum_{i=1}^n
\left[P(\xi_i,\eta_i)\Delta x_i+Q(\xi_i,\eta_i)\Delta y_i\right].
$$

不能把 $\Delta x_i,\Delta y_i$ 换成它们的绝对值；那样会改变所累积的量。

</details>

|性质|具体含义|
|---|---|
|线性|对被积表达式的加法、常数倍可以分别积分|
|分段可加|$L=L_1+L_2$ 且方向衔接，则 $\int_L=\int_{L_1}+\int_{L_2}$|
|反向变号|$-L$ 与 $L$ 方向相反，则 $\int_{-L}Pdx+Qdy=-\int_LPdx+Qdy$|
|闭曲线记号|$\oint_L$ 表示沿闭曲线积分，不意味着积分值为零|

![同一条路径反向时，两型积分的区别](../assets/orientation.svg)

第一型的 $ds$ 是非负长度元；第二型的 $dx,dy,dz$ 保留坐标变化的符号。方向是题目数据的一部分。

## 两型曲线积分的关系

### 用单位切向量连接两型

沿行进方向的单位切向量为 $\mathbf T=(\cos\alpha,\cos\beta,\cos\gamma)$，其中角度分别是它与三个坐标轴正方向的夹角。

<!-- study:result|坐标微分是弧长元的有向投影 -->

$$
dx=\cos\alpha\,ds,\quad dy=\cos\beta\,ds,\quad dz=\cos\gamma\,ds,
$$

$$
\int_\Gamma Pdx+Qdy+Rdz
=\int_\Gamma(P\cos\alpha+Q\cos\beta+R\cos\gamma)ds
=\int_\Gamma\mathbf F\cdot\mathbf T\,ds.
$$

<!-- /study -->

右边是以力的切向分量为被积函数的第一型曲线积分。反向时 $ds$ 不变，但 $\mathbf T$ 反向，所以功仍然变号。方向余弦一般随位置变化，不能直接提出积分号。

<details class="study-extension" id="curve-integral-relation">
<summary>扩展推导：从弧长参数、单位切向量到两型曲线积分的关系</summary>

#### 1. 用沿行进方向累计的弧长作参数

设曲线从 $A$ 指向 $B$，全长为 $\ell$。用从 $A$ 出发累计走过的弧长 $s$ 表示曲线上的位置：

$$
\mathbf r(s)=(x(s),y(s),z(s)),\qquad0\le s\le\ell.
$$

这里 $s$ 是已经走过的长度，$ds$ 是微小弧长；$dx,dy,dz$ 是这段运动在三个坐标轴方向上的有符号变化量。走了一小段正的长度，某个坐标仍然可能减小。

#### 2. 为什么对弧长求导得到单位切向量？

先在一段光滑正则曲线上取一般参数 $t$，并使 $t$ 增大时从 $A$ 向 $B$ 行进。其速度长度为

$$
\frac{ds}{dt}=\|\mathbf r'(t)\|
=\sqrt{x'(t)^2+y'(t)^2+z'(t)^2}>0.
$$

由链式法则，

$$
\frac{d\mathbf r}{ds}
=\frac{d\mathbf r/dt}{ds/dt}
=\frac{\mathbf r'(t)}{\|\mathbf r'(t)\|}.
$$

右侧把切向量除以它的长度，方向仍沿行进方向，长度则变成 $1$，所以它就是有向单位切向量：

$$
\mathbf T=\frac{d\mathbf r}{ds}
=\left(\frac{dx}{ds},\frac{dy}{ds},\frac{dz}{ds}\right),
\qquad
\left(\frac{dx}{ds}\right)^2+
\left(\frac{dy}{ds}\right)^2+
\left(\frac{dz}{ds}\right)^2=1.
$$

分段光滑曲线可以在每一段上这样推导，再把积分相加；有限个折点不影响积分。

#### 3. 方向余弦为什么等于这三个导数？

设 $\alpha,\beta,\gamma$ 分别为 $\mathbf T$ 与三个坐标轴正方向的夹角。以 $x$ 轴单位向量 $\mathbf e_x=(1,0,0)$ 为例，按点积公式，

$$
\mathbf T\cdot\mathbf e_x
=\|\mathbf T\|\,\|\mathbf e_x\|\cos\alpha
=\cos\alpha.
$$

另一方面，按分量计算同一个点积，

$$
\mathbf T\cdot\mathbf e_x
=\frac{dx}{ds}\cdot1+\frac{dy}{ds}\cdot0+\frac{dz}{ds}\cdot0
=\frac{dx}{ds}.
$$

因此 $dx/ds=\cos\alpha$；另外两条坐标轴同理，得到

$$
\frac{dx}{ds}=\cos\alpha,\qquad
\frac{dy}{ds}=\cos\beta,\qquad
\frac{dz}{ds}=\cos\gamma.
$$

也就是

$$
\boxed{dx=\cos\alpha\,ds,\quad dy=\cos\beta\,ds,\quad dz=\cos\gamma\,ds}.
$$

这三个式子表示微小位移在各坐标轴上的有向投影。例如沿途 $x$ 减小时，$dx/ds<0$，相应的 $\cos\alpha<0$，于是 $dx$ 为负，符号没有丢失。

#### 4. 将三个微分逐项代入积分

先看被积表达式：

$$
\begin{aligned}
Pdx+Qdy+Rdz
&=P\cos\alpha\,ds+Q\cos\beta\,ds+R\cos\gamma\,ds\\
&=(P\cos\alpha+Q\cos\beta+R\cos\gamma)ds.
\end{aligned}
$$

再沿整条曲线累加，就得到

$$
\boxed{\int_\Gamma Pdx+Qdy+Rdz
=\int_\Gamma(P\cos\alpha+Q\cos\beta+R\cos\gamma)ds}.
$$

如果记 $\mathbf F=(P,Q,R)$，括号里的标量正是 $\mathbf F\cdot\mathbf T$。因此这一步把第二型曲线积分化为以 $\mathbf F\cdot\mathbf T$ 为被积函数的第一型曲线积分。方向余弦随曲线上点的位置变化，一般不能当作常数提出积分号。

#### 5. 为什么右边用的是第一型积分，仍然保留方向？

第一型积分对同一个标量函数沿同一条曲线积分，与行进方向无关。但这里的标量函数包含了有向单位切向量 $\mathbf T$：反向行进时，$ds$ 不变，而 $\mathbf T$ 变为 $-\mathbf T$，所以 $\mathbf F\cdot\mathbf T$ 整体变号。

例如线段从 $(0,0,0)$ 指向 $(1,1,0)$，有 $\mathbf T=(1,1,0)/\sqrt2$，所以

$$
Pdx+Qdy=\frac{P+Q}{\sqrt2}\,ds.
$$

反向时单位切向量变成 $(-1,-1,0)/\sqrt2$，相同向量场对应的表达式变成 $-(P+Q)ds/\sqrt2$。因此第二型积分反向变号，与上面的关系式完全一致。

</details>

### 小例：同一条线段的两种累积

$L$ 从 $(0,0)$ 到 $(1,1)$，取 $x=y=t,0\le t\le1$。第一型积分为

$$
\int_L(x+y)ds=\int_0^12t\sqrt2\,dt=\sqrt2;
$$

第二型积分为

$$
\int_Ly\,dx+x\,dy=\int_0^1(t+t)dt=1.
$$

反向后两者分别为 $\sqrt2$ 和 $-1$。两种积分累积的对象不同，不能直接将 $dx,dy$ 换成 $ds$。

## 计算本质：化为一元定积分

### 一般参数法

<!-- study:result|替换坐标时，同步替换微分 -->

若 $x=x(t),y=y(t)$，起终点分别对应 $t=a,b$，则

$$
\int_LPdx+Qdy
=\int_a^b\left[P(x(t),y(t))x'(t)+Q(x(t),y(t))y'(t)\right]dt.
$$

空间曲线增加 $R(\mathbf r(t))z'(t)$。公式中没有弧长根号，也不对坐标导数取绝对值。

<!-- /study -->

统一步骤是：**选变量 → 写曲线方程 → 换算微分 → 按起终点定上下限 → 积分**。

### 例1 圆弧参数法：教材例1.1

计算 $\int_Lxdy-ydx$，$L$ 为圆 $x^2+(y-1)^2=1$ 上从 $O=(0,0)$ 到 $B=(1,1)$ 的右下方四分之一圆弧。

**本例知识点**：用圆的参数表达式同时代入坐标和微分；参数范围必须对应指定的弧与方向。

取 $x=\cos t,y=1+\sin t,t:-\pi/2\to0$，则 $dx=-\sin tdt,dy=\cos tdt$。因此

$$
I=\int_{-\pi/2}^0\left[\cos^2t+(1+\sin t)\sin t\right]dt
=\int_{-\pi/2}^0(1+\sin t)dt=\frac\pi2-1.
$$

若改走折线 $O\to(0,1)\to B$，竖段 $x=0,dx=0$，贡献为零；横段 $y=1,dy=0$，贡献为 $-\int_0^1dx=-1$。同一对端点的不同路径，积分一般不同。

### 以 x 或 y 为变量

|曲线表示|微分替换|一元积分|
|---|---|---|
|$y=\varphi(x),x:a\to b$|$dy=\varphi'(x)dx$|$\int_a^b[P(x,\varphi(x))+Q(x,\varphi(x))\varphi'(x)]dx$|
|$x=\psi(y),y:c\to d$|$dx=\psi'(y)dy$|$\int_c^d[P(\psi(y),y)\psi'(y)+Q(\psi(y),y)]dy$|

下限对应起点，上限对应终点，不必从小到大。若曲线不能在整段上写成所选变量的单值函数，应分段或更换变量。

### 例2 同一道抛物线题，比较选 x 与选 y

计算 $\int_Lxy\,dx$，$L:x=y^2$ 从 $A=(1,-1)$ 经原点到 $B=(1,1)$。此题来自总结第6页。

**本例知识点**：以 $y$ 为变量可以覆盖整条曲线；以 $x$ 为变量则必须区分上下两支。

以 $y$ 为变量，$x=y^2,dx=2y\,dy$，所以

$$
I=\int_{-1}^1y^2\cdot y\cdot2y\,dy=\int_{-1}^12y^4dy=\frac45.
$$

以 $x$ 为变量：下支 $y=-\sqrt x,x:1\to0$；上支 $y=\sqrt x,x:0\to1$。于是

$$
I=\int_1^0-x\sqrt x\,dx+\int_0^1x\sqrt x\,dx=\frac45.
$$

两段的 $x$ 变化方向不同；如果都写成 $0\to1$，就会错误相消。

### 例3 分段空间曲线：教材例1.3

计算 $\int_\Gamma ydx+zdy+xdz$，路径为 $A=(2,0,0)\to B=(3,4,5)\to C=(3,4,0)$ 的折线。

**本例知识点**：分段可加；某坐标恒定时，相应微分为零。

在 $AB$ 上取 $(x,y,z)=(2+t,4t,5t),t:0\to1$，得到

$$
I_{AB}=\int_0^1[4t+20t+5(2+t)]dt=\frac{49}{2}.
$$

在 $BC$ 上 $x=3,y=4,z:5\to0$，$dx=dy=0$，所以 $I_{BC}=\int_5^03dz=-15$。总和为 $I=19/2$。

## 计算技巧：对称性与方法选择

### 先检查函数、微分和行进方向

第二型积分的对称性要分别分析 $Pdx$、$Qdy$。函数在对称点处同号或反号之外，还需检查对应小段的坐标增量是否同号。

<!-- study:warning|几何对称并不足以直接套奇偶口诀 -->

对称性结论依赖有向路径的配对方式。开口曲线与闭曲线不能只凭同一幅对称形状套用相同口诀。稳妥方法是先参数化或投到一元积分，再判断奇偶性。

<!-- /study -->

例如关于 $y$ 轴对称的抛物线 $y=x^2$，从 $(1,1)$ 经原点走到 $(-1,1)$ 时，左右对应小段的 $dx$ 同号、$dy$ 反号。相应地，$P$ 关于 $x$ 偶时 $Pdx$ 加倍，奇时相消；$Q$ 关于 $x$ 偶时 $Qdy$ 相消，奇时加倍。这些结论针对这里的有向路径。

<details class="study-extension" id="curve-symmetry">
<summary>扩展：用同一个参数逐项验证“相消或加倍”</summary>

令 $x=t^2,y=t,t:-1\to1$。则

$$
\int_LPdx+Qdy=\int_{-1}^1[2tP(t^2,t)+Q(t^2,t)]dt.
$$

这里曲线关于 $x$ 轴对称，比较的是 $t$ 与 $-t$：若 $P(x,-y)=P(x,y)$，则 $2tP(t^2,t)$ 为奇函数，$Pdx$ 项为零；若 $Q(x,-y)=Q(x,y)$，则 $Qdy$ 项为偶函数，可取半段加倍。可见不同微分对应的结论不同。

这与正文关于 $y$ 轴对称的路径是两种情形，应根据实际图形与方向判断。

</details>

### 做题前的选择

|路径或表达式特征|优先尝试|
|---|---|
|已给参数、圆弧、空间曲线|一般参数法|
|能写成单值 $y(x)$ 或 $x(y)$|选能减少分支与计算量的变量|
|折线、不同方程拼接|分段计算，分别标明方向|
|对称路径|先检查有向配对，再利用奇偶性|
|平面闭路、疑似全微分|继续学习5.2中的 Green 与路径无关方法|

本节自检：能否解释 $dx$ 为什么可负？能否同时替换 $x,y,dx,dy$？能否从起终点确定参数上下限？

---

[进入本节作业解读](homework1.md) · [本章导览](README.md) · [下一节：5.2](section2.md)
