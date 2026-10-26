# 5.2 作业解读

[返回本节教程](section2.md) · [本章目录](README.md)

保留作业批次、题型和原题号；原题按提供的作业文件转录，解答为本站推导。

## 第二次作业 · 选择题1

**原题**

设 $L$ 是椭圆 $4x^2+y^2=8x$ 的正向边界，则 $\oint_L e^{y^2}dx+xdy=(\quad)$。

(A) $2\pi$；(B) $\pi$；(C) $1$；(D) $0$。

**对应知识点**：Green公式；利用区域的对称性消去奇函数积分。

**解题过程**

椭圆为 $(x-1)^2+y^2/4=1$，内部区域 $D$ 的面积为 $2\pi$。取 $P=e^{y^2},Q=x$，由 Green 公式

$$
I=\iint_D(1-2ye^{y^2})dxdy.
$$

$D$ 关于 $y=0$ 对称，$2ye^{y^2}$ 关于 $y$ 为奇函数，故其积分为零，得到 $I=2\pi$，选 **A**。

## 第二次作业 · 选择题3

**原题**

当 $x>0,y>0$ 时，$\frac{(x+ay)dy-y\,dx}{(x+y)^2}$ 为某函数的全微分，则 $a=(\quad)$。

(A) $-1$；(B) $0$；(C) $2$；(D) $1$。

**对应知识点**：单连通区域内全微分的判别条件 $P_y=Q_x$。

**解题过程**

记 $P=-y/(x+y)^2,Q=(x+ay)/(x+y)^2$，计算得

$$
P_y=\frac{-x+y}{(x+y)^3},\qquad
Q_x=\frac{-x+(1-2a)y}{(x+y)^3}.
$$

二者相等要求 $1=1-2a$，即 $a=0$。此时原式确实等于 $d[y/(x+y)]$，故选 **B**。

## 第二次作业 · 选择题4

**原题**

设曲线积分 $\int_Lxy^2dx+y\varphi(x)dy$ 与路径无关，其中 $\varphi(x)$ 具有连续的导数，且 $\varphi(0)=0$，则 $\int_{(0,0)}^{(1,1)}xy^2dx+y\varphi(x)dy=(\quad)$。

(A) $1$；(B) $\frac34$；(C) $\frac12$；(D) $\frac38$。

**对应知识点**：路径无关的必要条件与势函数法。

**解题过程**

由 $P_y=Q_x$ 得 $2xy=y\varphi'(x)$，所以 $\varphi'(x)=2x$。结合 $\varphi(0)=0$ 得 $\varphi(x)=x^2$。

$$
xy^2dx+x^2y\,dy=d\left(\frac{x^2y^2}{2}\right).
$$

因此积分为 $\frac12-0=\frac12$，选 **C**。

## 第二次作业 · 填空题2

**原题**

设 $L$ 为 $x^2+(y-1)^2=4$ 正向一周，则 $\oint_L\frac{xdy-y\,dx}{x^2+(y-1)^2}=$ ______。

**对应知识点**：曲线方程可直接化简分母；闭曲线积分中的全微分项积分为零。

**解题过程**

曲线上分母恒为 $4$，故

$$
I=\frac14\oint_L(xdy-y\,dx)
=\frac14\cdot2\operatorname{Area}(D)
=\frac14\cdot2\cdot4\pi=\boxed{2\pi}.
$$

这里对多项式形式 $xdy-y\,dx$ 使用 Green 公式；没有把原来的有奇点向量场直接用于整个圆域。

## 第二次作业 · 填空题3

**原题**

设 $L$ 为封闭折线 $|x|+|x+y|=1$ 正向一周，则 $\oint_Lx^2y^2dx-\cos(x+y)dy=$ ______。

**对应知识点**：Green公式；线性换元后的中心对称性。

**解题过程**

由 Green 公式

$$
I=\iint_D[\sin(x+y)-2x^2y]dxdy.
$$

令 $u=x,v=x+y$，雅可比绝对值为 $1$，$D$ 化为 $|u|+|v|\le1$，被积函数化为 $\sin v-2u^2v+2u^3$。

该区域分别关于 $u=0,v=0$ 对称，三个项各自为某一变量的奇函数，积分均为零。故 $I=\boxed0$。

## 第二次作业 · 计算题1

**原题**

计算 $\int_\Gamma(x^2-yz)dx+(y^2-xz)dy+(z^2-xy)dz$，其中 $\Gamma$ 为从点 $A(1,0,0)$ 沿圆柱螺旋线 $x=\cos\theta,y=\sin\theta,z=\theta$ 到点 $B(1,0,2\pi)$ 的弧段。

**对应知识点**：空间势函数与路径无关；识别 $d(xyz)$ 可以避免螺旋线上的复杂计算。

**解题过程**

有

$$
(x^2-yz)dx+(y^2-xz)dy+(z^2-xy)dz
=d\left(\frac{x^3+y^3+z^3}{3}-xyz\right).
$$

取势函数 $u=(x^3+y^3+z^3)/3-xyz$，则

$$
I=u(B)-u(A)=\frac{1+8\pi^3}{3}-\frac13
=\boxed{\frac{8\pi^3}{3}}.
$$

## 第二次作业 · 计算题2

**原题**

计算 $\int_L(y+\frac{e^y}{x})dx+e^y\ln x\,dy$，其中 $L$ 是半圆周 $x=1+\sqrt{2y-y^2}$ 上从点 $(1,0)$ 到点 $(2,1)$ 的一段弧。

**对应知识点**：将积分拆为全微分和简单曲线积分；圆弧参数化保留行进方向。

**解题过程**

由于

$$
\frac{e^y}{x}dx+e^y\ln x\,dy=d(e^y\ln x),
$$

原积分等于 $\int_Ly\,dx+e\ln2$。圆弧满足 $(x-1)^2+(y-1)^2=1$，可取

$$
x=1+\cos t,\quad y=1+\sin t,\quad-\frac\pi2\le t\le0.
$$

于是

$$
\int_Ly\,dx=-\int_{-\pi/2}^0(\sin t+\sin^2t)dt=1-\frac\pi4.
$$

故 $I=\boxed{1-\frac\pi4+e\ln2}$。

## 第二次作业 · 计算题3

**原题**

证明 $(2xy^3-y^2\cos x)dx+(1-2y\sin x+3x^2y^2)dy$ 是某二元函数 $u(x,y)$ 的全微分，求一个 $u(x,y)$，并计算 $\int_{(0,0)}^{(\pi/2,1)}(2xy^3-y^2\cos x)dx+(1-2y\sin x+3x^2y^2)dy$。

**对应知识点**：全微分判别；对一个变量积分后需要补上另一个变量的函数。

**解题过程**

记两系数为 $P,Q$，则

$$
P_y=6xy^2-2y\cos x=Q_x.
$$

系数在整个平面上一阶连续可微，且平面单连通，故为全微分。由 $u_x=P$ 积分得

$$
u=x^2y^3-y^2\sin x+C(y).
$$

令 $u_y=Q$，得 $C'(y)=1$，可取 $C(y)=y$。因此一个势函数为 $u=x^2y^3-y^2\sin x+y$，且

$$
I=u(\pi/2,1)-u(0,0)=\frac{\pi^2}{4}-1+1
=\boxed{\frac{\pi^2}{4}}.
$$

## 第二次作业 · 计算题4

**原题**

计算 $I=\int_L[\varphi(y)\cos x-\pi y]dx+[\varphi'(y)\sin x-\pi]dy$，其中 $L$ 为连接点 $A(\pi,2)$ 与 $B(3\pi,4)$ 的线段之下的任意曲线，从 $A$ 到 $B$ 方向，且该段曲线与 $AB$ 所围成的面积为 $2$，$\varphi(y)$ 具有连续的导数。

**对应知识点**：拆出全微分；用曲线和弦所围区域的面积求剩余积分。

**解题过程**

原式可写成

$$
I=[\varphi(y)\sin x]_A^B-\pi\int_Ly\,dx-\pi(4-2).
$$

端点的正弦均为零，第一项为零。$L$ 从 $A$ 到 $B$，再沿线段 $BA$ 返回，围成正向边界，故

$$
\int_Ly\,dx-\int_{AB}y\,dx=-2.
$$

在线段 $AB$ 上，$y$ 的平均值为 $3$，$x$ 的增量为 $2\pi$，所以 $\int_{AB}y\,dx=6\pi$，从而 $\int_Ly\,dx=6\pi-2$。

$$
I=-\pi(6\pi-2)-2\pi=\boxed{-6\pi^2}.
$$

## 第二次作业 · 计算题5

**原题**

计算 $\oint_L\frac{xdy-y\,dx}{x^2+2y^2}$，其中 $L$ 为 $(x-1)^2+y^2=4$ 的正向边界。

**对应知识点**：有奇点时挖去小区域再使用Green公式；积分由围绕原点的绕行决定。

**解题过程**

令 $P=-y/(x^2+2y^2),Q=x/(x^2+2y^2)$。在原点之外，$Q_x-P_y=0$；原点位于 $L$ 内部，不能直接在整个圆域套用 Green 公式。

取充分小的椭圆 $C_\varepsilon:x^2+2y^2=\varepsilon^2$，正向绕行。对两曲线之间的无奇点区域使用 Green 公式，得 $\oint_L=\oint_{C_\varepsilon}$。

令 $x=\varepsilon\cos t,y=\varepsilon\sin t/\sqrt2$，$0\le t\le2\pi$，则

$$
xdy-y\,dx=\frac{\varepsilon^2}{\sqrt2}dt,
\qquad x^2+2y^2=\varepsilon^2.
$$

所以 $I=\int_0^{2\pi}\frac1{\sqrt2}dt=\boxed{\sqrt2\pi}$。
