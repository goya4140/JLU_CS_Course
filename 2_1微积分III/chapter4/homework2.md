# 4.2 作业解读

[返回本节教程](section2.md) · [本章目录](README.md)

保留作业批次、题型和原题号；原题按提供的作业文件转录，解答为本站推导。

## 第一次作业 · 选择题3

**原题**

设 $\Sigma:x^2+y^2+z^2=a^2\ (z\ge0)$，$\Sigma_1$ 为 $\Sigma$ 在第一卦限中的部分，则有 $(\quad)$。

(A) $\iint_\Sigma x\,dS=4\iint_{\Sigma_1}x\,dS$；

(B) $\iint_\Sigma y\,dS=4\iint_{\Sigma_1}y\,dS$；

(C) $\iint_\Sigma z\,dS=4\iint_{\Sigma_1}z\,dS$；

(D) $\iint_\Sigma xyz\,dS=4\iint_{\Sigma_1}xyz\,dS$。

**对应知识点**：第一型曲面积分的对称性；扩大积分区域时要同时检查被积函数是否同号对称。

**解题过程**

$\Sigma$ 关于 $x=0$ 和 $y=0$ 对称，故 $\iint_\Sigma x\,dS=\iint_\Sigma y\,dS=\iint_\Sigma xyz\,dS=0$；对应的第一卦限积分均大于零，所以 A、B、D 不成立。

将上半球分成四个全等部分。反射改变 $x,y$ 的符号，却不改变 $z$ 和 $dS$，所以四部分的 $z$ 积分相等：

$$
\iint_\Sigma z\,dS=4\iint_{\Sigma_1}z\,dS.
$$

故选 **C**。

## 第一次作业 · 填空题2

**原题**

设 $\Sigma$ 为 $Oyz$ 平面上的圆域 $y^2+z^2\le1$，则 $\iint_\Sigma[x+(y^2+z^2)^2]dS=$ ______。

**对应知识点**：平面上的第一型曲面积分；在投影平面中使用极坐标。

**解题过程**

在 $Oyz$ 平面上 $x=0,dS=dy\,dz$。令 $y=r\cos\theta,z=r\sin\theta$，则

$$
I=\int_0^{2\pi}\int_0^1r^4\,r\,drd\theta
=2\pi\cdot\frac16=\boxed{\frac\pi3}.
$$

## 第一次作业 · 填空题3

**原题**

设 $\Sigma$ 为平面 $\frac{x}{2}+y+z=1$ 在第一卦限中的部分，则 $\iint_\Sigma(x+2y+2z+4)dS=$ ______。

**对应知识点**：图形曲面的面积元；先用曲面方程化简被积函数。

**解题过程**

写成 $z=1-x/2-y$，则

$$
dS=\sqrt{1+(-1/2)^2+(-1)^2}\,dxdy=\frac32dxdy.
$$

投影域为 $D=\lbrace x\ge0,y\ge0,x/2+y\le1\rbrace $，面积为 $\frac12\cdot2\cdot1=1$。在曲面上 $x+2y+2z+4=6$，故

$$
I=6\cdot\frac32\cdot1=\boxed9.
$$

## 第一次作业 · 填空题4

**原题**

圆柱面 $x^2+y^2=R^2$ 介于 $Oxy$ 平面及柱面 $z=R+\frac{x^2}{R}$ 之间的面积为 ______。

**对应知识点**：参数曲面的面积元；圆柱侧面的高度可以随周向变化。

**解题过程**

取 $\mathbf r(\theta,z)=(R\cos\theta,R\sin\theta,z)$，则 $dS=R\,d\theta dz$，上边界为 $z=R(1+\cos^2\theta)$。

$$
S=\int_0^{2\pi}\int_0^{R(1+\cos^2\theta)}R\,dz d\theta
=R^2(2\pi+\pi)=\boxed{3\pi R^2}.
$$

## 第一次作业 · 填空题5

**原题**

设 $\Sigma$ 为柱面 $x^2+y^2=a^2\ (a>0)$ 在 $0\le z\le h$ 之间的部分，则 $\iint_\Sigma x^2dS=$ ______。

**对应知识点**：圆柱侧面的参数法；面积元中需要保留半径因子。

**解题过程**

令 $x=a\cos\theta,y=a\sin\theta$，则 $dS=a\,d\theta dz$，所以

$$
I=\int_0^h\int_0^{2\pi}a^2\cos^2\theta\cdot a\,d\theta dz
=\boxed{\pi a^3h}.
$$

## 第一次作业 · 计算题2

**原题**

设 $\Sigma$ 是锥面 $z=\sqrt{x^2+y^2}$ 介于 $z=0$ 与 $z=2$ 之间的部分，计算 $\iint_\Sigma(x^2+y^2)dS$。

**对应知识点**：锥面的参数法与面积元；高度范围决定投影圆盘半径。

**解题过程**

令 $\mathbf r(r,\theta)=(r\cos\theta,r\sin\theta,r)$，$0\le r\le2,0\le\theta\le2\pi$。

$$
\left|\mathbf r_r\times\mathbf r_\theta\right|=\sqrt2\,r,
\qquad x^2+y^2=r^2.
$$

故

$$
I=\int_0^{2\pi}\int_0^2r^2\sqrt2\,r\,drd\theta
=2\pi\sqrt2\left[\frac{r^4}{4}\right]_0^2
=\boxed{8\sqrt2\pi}.
$$
