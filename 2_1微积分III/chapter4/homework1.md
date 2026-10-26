# 4.1 作业解读

[返回本节教程](section1.md) · [本章目录](README.md)

保留作业批次、题型和原题号；原题按提供的作业文件转录，解答为本站推导。

## 第一次作业 · 选择题1

**原题**

设 $L$ 是圆周 $x^2+y^2=a^2$，则 $\oint_L(x+y)^2ds=(\quad)$。

(A) $2\pi a^2$；(B) $2\pi a^3$；(C) $\pi a^4$；(D) $2\pi a^4$。

**对应知识点**：第一型曲线积分的参数法；整圆上的奇偶对称性。

**解题过程**

圆的半径为 $a>0$。令 $x=a\cos t,y=a\sin t$，$0\le t\le2\pi$，则 $ds=a\,dt$。

$$
I=a^3\int_0^{2\pi}(\cos t+\sin t)^2dt
=a^3\int_0^{2\pi}(1+\sin2t)dt=2\pi a^3.
$$

故选 **B**。

## 第一次作业 · 选择题2

**原题**

设 $\Gamma$ 为螺旋线 $x=\cos t,y=\sin t,z=t$ 在 $0\le t\le\pi$ 上的一段，则 $\int_\Gamma(x^2+y^2+z)ds=(\quad)$。

(A) $\sqrt2(\pi+\pi^2)$；(B) $\pi+\pi^2$；(C) $\pi+\frac{\pi^2}{2}$；(D) $\sqrt2(\pi+\frac{\pi^2}{2})$。

**对应知识点**：空间曲线的弧长元为参数导数向量的长度乘参数微元。

**解题过程**

$$
ds=\sqrt{(-\sin t)^2+(\cos t)^2+1}\,dt=\sqrt2\,dt,
\qquad x^2+y^2+z=1+t.
$$

因此

$$
I=\sqrt2\int_0^\pi(1+t)dt
=\sqrt2\left(\pi+\frac{\pi^2}{2}\right).
$$

故选 **D**。

## 第一次作业 · 选择题4

**原题**

设 $\Gamma$ 为球面 $x^2+y^2+z^2=R^2\ (R>0)$ 与平面 $x+y+z=0$ 的交线，则 $\oint_\Gamma3xy\,ds=(\quad)$。

(A) $-\pi R^3$；(B) $-2\pi R^3$；(C) $\pi R^3$；(D) $2\pi R^3$。

**对应知识点**：空间大圆上的轮换对称性；用约束关系化简积分。

**解题过程**

平面过球心，故 $\Gamma$ 为半径 $R$ 的大圆，长度为 $2\pi R$。由轮换对称性，$\oint xy\,ds=\oint yz\,ds=\oint zx\,ds$。

在曲线上，$(x+y+z)^2=0$，故

$$
xy+yz+zx=-\frac{x^2+y^2+z^2}{2}=-\frac{R^2}{2}.
$$

因此

$$
\oint_\Gamma3xy\,ds
=\oint_\Gamma(xy+yz+zx)ds
=-\frac{R^2}{2}\cdot2\pi R=-\pi R^3.
$$

故选 **A**。

## 第一次作业 · 填空题1

**原题**

设 $L$ 为以 $(0,0),(1,0),(0,1)$ 为顶点的三角形的周界，则 $\oint_L(x+y)ds=$ ______。

**对应知识点**：第一型曲线积分对分段曲线可逐段相加。

**解题过程**

两条直角边分别取 $(x,y)=(t,0)$ 与 $(0,t)$，$0\le t\le1$，积分各为 $\int_0^1t\,dt=1/2$。

斜边上 $x+y=1$，长度为 $\sqrt2$，故其积分为 $\sqrt2$。

$$
I=\frac12+\frac12+\sqrt2=\boxed{1+\sqrt2}.
$$

## 第一次作业 · 计算题1

**原题**

计算 $\oint_\Gamma(\sqrt{2y^2+z^2}+y^2)ds$，其中闭曲线 $\Gamma$ 为球面 $x^2+y^2+z^2=9$ 与平面 $y=x$ 的交线。

**对应知识点**：空间圆的参数化；利用曲线约束先化简被积函数。

**解题过程**

曲线上 $x=y$，故 $2y^2+z^2=9$，根式恒为 $3$。交线为半径 $3$ 的大圆，可取

$$
x=y=\frac3{\sqrt2}\cos t,\qquad z=3\sin t,\qquad0\le t\le2\pi.
$$

此时 $ds=3dt$，从而

$$
I=3\int_0^{2\pi}\left(3+\frac92\cos^2t\right)dt
=18\pi+\frac{27\pi}{2}=\boxed{\frac{63\pi}{2}}.
$$
