# 5.5 作业解读

[返回本节教程](section5.md) · [本章目录](README.md)

保留作业批次、题型和原题号；原题按提供的作业文件转录，解答为本站推导。

## 第三次作业 · 填空题4

**原题**

已知向量场 $\mathbf A(M)=(xz,y^4,z^2)$，则 $\operatorname{rot}\mathbf A(M)=$ ______。

**对应知识点**：旋度的三个分量由交叉偏导组成；中间分量为 $P_z-R_x$。

**解题过程**

设 $\mathbf A=(P,Q,R)$，则

$$
\operatorname{rot}\mathbf A=(R_y-Q_z,\ P_z-R_x,\ Q_x-P_y)
=(0-0,\ x-0,\ 0-0)=\boxed{(0,x,0)}.
$$

## 第三次作业 · 计算题5

**原题**

利用 Stokes 公式计算 $\oint_\Gamma(y^2-z^2)dx+(2z^2-x^2)dy+(3x^2-y^2)dz$，其中 $\Gamma$ 是平面 $x+y+z=2$ 与柱面 $|x|+|y|=1$ 的交线，从 $z$ 轴正向看 $\Gamma$ 为逆时针方向。

**对应知识点**：Stokes公式与右手定向；选择交线所围的平面片作为跨接曲面。

**解题过程**

取平面片 $S:z=2-x-y$，投影域为 $D=\lbrace |x|+|y|\le1\rbrace $。从 $+z$ 方向看边界为逆时针，故取上侧，面积向量为 $(1,1,1)dxdy$。

记原向量场为 $\mathbf F$，则

$$
\nabla\times\mathbf F=(-2y-4z,\ -2z-6x,\ -2x-2y).
$$

由 Stokes 公式

$$
I=\iint_D(-8x-4y-6z)dxdy
=\iint_D(-12-2x+2y)dxdy.
$$

$D$ 关于两坐标轴对称，面积为 $2$，故两个奇函数项积分为零，得到

$$
I=-12\cdot2=\boxed{-24}.
$$
