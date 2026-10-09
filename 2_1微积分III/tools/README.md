# 图文教程维护

正文保存在课程根目录的 Markdown 文件中，HTML 由相同内容生成。

1. 安装绘图依赖：`python3 -m pip install matplotlib==3.11.2 sympy==1.14.0 numpy scipy`。
2. 运行 `python3 tools/build_assets.py` 生成三张结构图并检查本地阅读资源。
3. 运行 `python3 tools/build_math_figures.py` 生成26张数学 SVG；需要中文字体，可设置 `CALCULUS_FONT` 为字体文件的路径。预览 PNG 默认输出到 `/tmp/calculus-figure-review`，可通过 `CALCULUS_PREVIEW` 修改。
4. 运行 `python3 tools/check_examples.py` 复核原版中10个代表性数值结果。
5. 运行 `python3 tools/build_reading.py` 更新图文阅读页。

`assets/math-figures.json` 记录图名、图注、使用的版本以及数学核验值。图形不得通过缩放或平移变成与正文公式不符的对象。向量箭头如缩放展示，应在图注中说明。
