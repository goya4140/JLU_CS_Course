# 5.4 作业解读

[返回本节教程](section4.md) · [本章目录](README.md)

保留作业批次、题型和原题号；原题按提供的作业文件转录，解答为本站推导。

## 第三次作业 · 选择题3

**原题**

设 $\Sigma$ 是球面 $x^2+y^2+z^2=a^2$ 的外侧，则 $\oiint_\Sigma\frac{x\,dydz+y\,dzdx+z\,dxdy}{(x^2+y^2+z^2)^{3/2}}=(\quad)$。

(A) $0$；(B) $1$；(C) $2\pi$；(D) $4\pi$。

**对应知识点**：径向场的通量；原点的奇点使得不能在整个球体内直接套用Gauss公式。

**解题过程**

在半径 $a>0$ 的球面上，外单位法向量为 $(x,y,z)/a$，故

$$
\frac{(x,y,z)}{a^3}\cdot\mathbf n
=\frac{x^2+y^2+z^2}{a^4}=\frac1{a^2}.
$$

所以 $I=\frac1{a^2}\cdot4\pi a^2=4\pi$，选 **D**。该场在原点无定义，其球面外通量不能由“散度为零”推出为零。

## 第三次作业 · 填空题3

**原题**

已知三元函数 $u=u(x,y,z)=x^2+y^2+z^2$，则 $\operatorname{div}(\operatorname{grad}u)=$ ______。

**对应知识点**：梯度将标量函数变为向量场，散度再将向量场变为标量函数；二者复合为拉普拉斯算子。

**解题过程**

$$
\operatorname{grad}u=(2x,2y,2z),\qquad
\operatorname{div}(\operatorname{grad}u)=2+2+2=\boxed6.
$$

## 第三次作业 · 计算题2

**原题**

已知 $\Sigma$ 为空间曲面 $x^2+y^2+z^4=1\ (z\ge0)$ 的上侧，$f$ 连续，计算

$$
I=\iint_\Sigma[x^2+yzf(x^2-y^2)]dydz
+[y^2+xzf(x^2-y^2)]dzdx
+[z^2+xyf(x^2-y^2)]dxdy.
$$

**对应知识点**：先用对称性消去含未知连续函数的项，再对光滑多项式场使用Gauss公式；连续性本身不保证可以求散度。

**解题过程**

把向量场拆为 $\mathbf F_0=(x^2,y^2,z^2)$ 与 $\mathbf F_1=f(x^2-y^2)(yz,xz,xy)$。

在 $z>0$ 的曲面部分有 $z_x=-x/(2z^3),z_y=-y/(2z^3)$。$\mathbf F_1$ 向上通量的投影后的被积函数为

$$
-yzf\,z_x-xzf\,z_y+xyf
=xyf(x^2-y^2)\left(\frac1{z^2}+1\right).
$$

该式关于 $x$ 为奇函数，而投影圆盘关于 $x=0$ 对称，所以此部分积分为零。可先在半径小于 $1$ 的同心圆盘上积分再取极限；$z^{-2}=(1-r^2)^{-1/2}$ 在边界可积。

对 $\mathbf F_0$ 补上 $z=0$ 的底盘，其通量为零。$\Sigma$ 的上侧正是封闭体的外侧，由 Gauss 公式

$$
I=\iiint_\Omega2(x+y+z)dV
=2\iiint_\Omega z\,dV.
$$

在高度 $z$，截面面积为 $\pi(1-z^4)$，故

$$
I=2\pi\int_0^1z(1-z^4)dz
=2\pi\left(\frac12-\frac16\right)=\boxed{\frac{2\pi}{3}}.
$$

## 第三次作业 · 计算题4

**原题**

利用 Gauss 公式计算 $\iint_\Sigma(8y+1)x\,dydz+2(1-y^2)dzdx-4yz\,dxdy$，其中 $\Sigma$ 是由曲线 $z=\sqrt{y-1},x=0\ (1\le y\le3)$ 绕 $y$ 轴旋转一周所成的曲面，它的法向量与 $y$ 轴正向的夹角恒大于 $\pi/2$。

**对应知识点**：开放曲面补面；根据法向量的符号判断给定侧是否为封闭体外侧。

**解题过程**

旋转面为 $y=1+x^2+z^2$，$1\le y\le3$。补上 $y=3$ 的圆盘，形成区域

$$
\Omega=\lbrace 1\le y\le3,\ x^2+z^2\le y-1\rbrace .
$$

该体侧面的外法向量的 $y$ 分量为负，符合题意。对 $\mathbf F=((8y+1)x,2(1-y^2),-4yz)$，

$$
\operatorname{div}\mathbf F=(8y+1)-4y-4y=1.
$$

故封闭面总通量为 $\operatorname{Vol}(\Omega)=\pi\int_1^3(y-1)dy=2\pi$。

顶盘外法向为 $+y$，面积为 $2\pi$，通量为 $2(1-9)\cdot2\pi=-32\pi$。因此原侧面通量为

$$
I=2\pi-(-32\pi)=\boxed{34\pi}.
$$
