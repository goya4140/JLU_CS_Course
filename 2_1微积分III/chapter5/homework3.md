# 5.3 作业解读

[返回本节教程](section3.md) · [本章目录](README.md)

保留作业批次、题型和原题号；原题按提供的作业文件转录，解答为本站推导。

## 第三次作业 · 选择题1

**原题**

设 $\Sigma$ 是 $Oxy$ 面上的圆域 $x^2+y^2\le1$，取上侧，则 $\iint_\Sigma(x^2+y^2+z^2)dzdx=(\quad)$。

(A) $\frac{2\pi}{3}$；(B) $\frac\pi2$；(C) $0$；(D) $-\frac\pi2$。

**对应知识点**：第二型曲面积分的投影与法向分量；$dzdx$ 对应法向量的 $y$ 分量。

**解题过程**

$Oxy$ 平面的上侧单位法向量为 $\mathbf n=(0,0,1)$，故 $dzdx=n_y\,dS=0$。因此积分为 $0$，选 **C**。

## 第三次作业 · 选择题2

**原题**

设曲面 $\Sigma$ 为 $x+y+z=1$ 在第一卦限部分的下侧，则 $\iint_\Sigma zdxdy=(\quad)$。

(A) $-\frac16$；(B) $\frac16$；(C) $-\frac13$；(D) $\frac13$。

**对应知识点**：取下侧时 $dxdy$ 带负号；先将曲面投影到 $Oxy$ 平面。

**解题过程**

写成 $z=1-x-y$，投影域为 $D=\lbrace x\ge0,y\ge0,x+y\le1\rbrace $。下侧给出

$$
I=-\int_0^1\int_0^{1-x}(1-x-y)dy\,dx
=-\frac12\int_0^1(1-x)^2dx=-\frac16.
$$

故选 **A**。

## 第三次作业 · 选择题4

**原题**

设 $\Sigma$ 为球面 $x^2+y^2+z^2=R^2$ 上半部分的上侧，则下列结论不正确的是 $(\quad)$。

(A) $\iint_\Sigma x^2dydz=0$；(B) $\iint_\Sigma x\,dydz=0$；(C) $\iint_\Sigma y^2dydz=0$；(D) $\iint_\Sigma y\,dydz=0$。

**对应知识点**：把第二型曲面积分化为第一型后再判断奇偶性，不能只看原被积函数。

**解题过程**

上半球上侧为外侧，故 $dydz=(x/R)dS$。A、C、D 分别对应 $x^3/R,xy^2/R,xy/R$ 的第一型积分，均由对称性为零。

B 实际为

$$
\iint_\Sigma x\,dydz=\frac1R\iint_\Sigma x^2dS
=\frac1R\cdot\frac{2\pi R^4}{3}=\frac{2\pi R^3}{3}>0.
$$

故不正确的是 **B**。

## 第三次作业 · 填空题1

**原题**

设 $\Sigma$ 是平面 $3x+2y+2\sqrt3z=6$ 在第一卦限部分的上侧，则 $I=\iint_\Sigma P\,dydz+Q\,dzdx+R\,dxdy$ 化为第一型曲面积分为 ______。

**对应知识点**：两型曲面积分的关系为 $\mathbf F\cdot\mathbf n\,dS$，上侧要求法向量的 $z$ 分量为正。

**解题过程**

法向量可取 $(3,2,2\sqrt3)$，其模长为 $\sqrt{9+4+12}=5$，且 $z$ 分量为正。因此

$$
\boxed{I=\iint_\Sigma\frac{3P+2Q+2\sqrt3R}{5}\,dS}.
$$

## 第三次作业 · 填空题2

**原题**

设 $\Sigma$ 是锥面 $z=\sqrt{x^2+y^2}\ (0\le z\le1)$ 的下侧，则 $\iint_\Sigma x\,dydz+y\,dzdx+(z-1)dxdy=$ ______。

**对应知识点**：曲面合一投影法；锥面下侧需要取向下的面积向量。

**解题过程**

令 $r=\sqrt{x^2+y^2}$，除顶点外 $z_x=x/r,z_y=y/r$。向下的面积向量为 $(z_x,z_y,-1)dxdy$，所以

$$
I=\iint_{x^2+y^2\le1}\left(\frac{x^2+y^2}{r}-(r-1)\right)dxdy
=\iint_{x^2+y^2\le1}1\,dxdy=\boxed\pi.
$$

顶点为单个点，不影响该积分。

## 第三次作业 · 计算题1

**原题**

计算 $I=\iint_\Sigma y\,dzdx+(z^2+1)dxdy$，其中 $\Sigma$ 是圆柱面 $x^2+y^2=4$ 被平面 $x+z=2$ 和 $z=0$ 所截出部分的外侧。

**对应知识点**：圆柱侧面的外法向参数法；$dxdy$ 项在竖直圆柱侧面上为零。

**解题过程**

取

$$
\mathbf r(\theta,z)=(2\cos\theta,2\sin\theta,z),\quad
0\le\theta\le2\pi,\quad0\le z\le2-2\cos\theta.
$$

有向面积向量为 $\mathbf r_\theta\times\mathbf r_z=(2\cos\theta,2\sin\theta,0)$，指向外侧。向量场为 $(0,y,z^2+1)$，故

$$
I=\int_0^{2\pi}\int_0^{2-2\cos\theta}4\sin^2\theta\,dz d\theta
=8\int_0^{2\pi}(\sin^2\theta-\sin^2\theta\cos\theta)d\theta
=\boxed{8\pi}.
$$

## 第三次作业 · 计算题3

**原题**

计算 $I=\oiint_\Sigma\frac{2\,dydz}{x\cos^2x}+\frac{dzdx}{\cos^2y}-\frac{dxdy}{z\cos^2z}$，其中 $\Sigma$ 是球面 $x^2+y^2+z^2=1$ 的外侧。

**对应知识点**：球面外法向可抵消分母中的坐标因子；先检查通量的可积性，再使用对称性。

**解题过程**

球面外单位法向量为 $(x,y,z)$。在 $xz\ne0$ 处，原式化为

$$
I=\oiint_\Sigma\left(\frac2{\cos^2x}+\frac y{\cos^2y}-\frac1{\cos^2z}\right)dS.
$$

右侧被积函数在整个球面连续，因此原积分可按去掉 $x=0,z=0$ 附近小带后取极限来理解。不能对原向量场直接在整个球内使用 Gauss 公式。

中间项关于 $y$ 为奇函数，积分为零；由球面的轮换对称性，$\oiint\sec^2x\,dS=\oiint\sec^2z\,dS$。故

$$
I=\oiint_\Sigma\sec^2z\,dS
=2\pi\int_{-1}^{1}\sec^2t\,dt
=\boxed{4\pi\tan1}.
$$

这里用到单位球上高度带的面积元 $dS=d\theta\,dz$；$1$ 以弧度计。
