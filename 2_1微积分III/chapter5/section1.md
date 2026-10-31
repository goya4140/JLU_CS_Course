# 5.1 第二型曲线积分

[第5章目录](README.md) · [作业解读（5题）](homework1.md)

> 学习目标：理解做功、路径方向及两型曲线积分之间的关系。

## 从质量累积走向做功

### 先理解向量与点积

$(2,0)$ 表示一个只沿 $+x$ 方向的力。如果位移为 $(1,0)$，功是 $2\times1+0\times0=2$；位移改成 $(0,1)$，功为0；位移改成 $(-1,0)$，功为 $-2$。这种“对应分量相乘再相加”的运算叫点积。

![同一个力在三种位移方向上的做功](../assets/work_dot.svg)

**从左向右读**：力始终朝右，位移分别朝右、朝上、朝左。功不仅取决于走了多远，还取决于相对于力的方向。对单位长度位移，三个结果是 $+2,0,-2$。箭头只用于显示方向和夹角，数值计算依照给定分量。

推广到很小的位移时，写成 $Pdx+Qdy+Rdz$；将每一小步的功相加，就进入第二型曲线积分。

<!-- study:concept|第二型曲线积分：做功与有向累积 -->

第一型积分累积标量函数乘长度。现在设质点沿曲线运动，力为 $\mathbf F=(P,Q,R)$，微小位移为 $d\mathbf r=(dx,dy,dz)$。微小功为

$$
dW=\mathbf F\cdot d\mathbf r=Pdx+Qdy+Rdz.
$$

点积只保留力沿位移方向的分量：顺着运动方向的力做正功，反向的力做负功，垂直于运动方向的力做功为零。把微小功沿有向曲线累加，得到第二型曲线积分。

$$
\int_L Pdx+Qdy+Rdz=\int_L\mathbf F\cdot d\mathbf r.
$$

<!-- /study -->

在分割和式中，$\Delta x_i,\Delta y_i,\Delta z_i$ 是按行进方向取的坐标增量。它们可以为负；这与非负弧长 $\Delta s_i$ 有本质区别。

![第一型与第二型的方向比较](../assets/orientation.svg)

图中把同一条线段画两次，左边从 $A$ 到 $B$，右边从 $B$ 到 $A$。第一型的长度元 $ds$ 总是正的；第二型的 $dx,dy$ 会随行进方向一起变号。因此同一份标量长度累积保持不变，同一个向量场的功改变符号。

如果不熟悉方向余弦，先把单位切向量理解为“当前前进方向的长度1箭头”：其三个分量是前进方向在三个坐标轴上的投影。下面两型关系就是先取力沿这个方向的分量，再乘实际小路程。

## 直接计算与两型关系

### 参数法保留导数的符号

<!-- study:result|有向曲线的参数计算公式 -->

设 $\mathbf r(t)=(x(t),y(t),z(t))$，随 $t$ 从 $a$ 到 $b$ 按题目方向行进，则

$$
\int_L Pdx+Qdy+Rdz
=\int_a^b\big(P(\mathbf r(t))x'(t)+Q(\mathbf r(t))y'(t)+R(\mathbf r(t))z'(t)\big)dt.
$$

<!-- /study -->

<!-- study:warning|导数的符号必须保留 -->

这里没有速度长度的根号，也没有导数的绝对值。反向取 $b$ 到 $a$ 时积分变号。如果同一坐标在曲线上先增后减，用参数统一处理比直接设上下限更稳妥。

<!-- /study -->

### 用有向单位切向量连接两型

<!-- study:result|两型曲线积分的关系 -->

设 $\mathbf T=(\cos\alpha,\cos\beta,\cos\gamma)$ 为沿行进方向的单位切向量，则 $d\mathbf r=\mathbf Tds$，因此

$$
\int_L Pdx+Qdy+Rdz
=\int_L(P\cos\alpha+Q\cos\beta+R\cos\gamma)ds.
$$

<!-- /study -->

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

反向后 $ds$ 不变，$\mathbf T$ 反向，所以第二型变号。

|比较|第一型曲线积分|第二型曲线积分|
|---|---|---|
|典型模型|线质量|变力做功|
|微元|$ds$|$dx,dy,dz$|
|参数公式的乘数|$\lVert\mathbf r'\rVert$|各坐标导数，有符号|
|反向|不变|变号|
|可先用对称性吗|常可直接奇偶配对|需连同切向方向、各项一起分析|

### 例1 同一条线段的两种积分

从 $A=(0,0)$ 到 $B=(1,1)$，取 $x=t,y=t,0\le t\le1$。

- $\int_L(x+y)ds=\int_0^1 2t\sqrt2dt=\sqrt2$。
- $\int_L ydx+xdy=\int_0^1(t+t)dt=1$。

反向走，第一式仍为 $\sqrt2$，第二式为 $-1$。不能只把第二式中的 $dx,dy$ 都换成 $ds$。

### 例2 分段路径：本地第5章作业第二次填空题1

从 $A=(1,1)$ 沿抛物线 $y=x^2$ 到 $B=(-1,1)$，再沿直线到 $C=(0,2)$，求 $\int_L y^2dx-xdy$。

第一段取 $x=t,y=t^2,t:1\to-1$，则

$$
I_{AB}=\int_1^{-1}(t^4-2t^2)dt=\frac{14}{15}.
$$

第二段取 $x=-1+t,y=1+t,0\le t\le1$，则

$$
I_{BC}=\int_0^1\big((1+t)^2-(-1+t)\big)dt
=\int_0^1(2+t+t^2)dt=\frac{17}{6}.
$$

总和为 $113/30$。第一段横坐标递减，保留 $1\to-1$ 是方向正确的关键。

---

[进入本节作业解读](homework1.md) · [本章导览](README.md) · [下一节：5.2](section2.md)
