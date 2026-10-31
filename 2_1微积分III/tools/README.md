# 图文教程维护

正文保存在课程根目录的 Markdown 文件中，HTML 由相同内容生成。

1. 安装绘图依赖：`python3 -m pip install matplotlib==3.11.2 sympy==1.14.0 numpy scipy`。
2. 运行 `python3 tools/build_assets.py` 生成三张结构图并检查本地阅读资源；第4章学习地图的布局由 `build_chapter4_map.py` 维护。
3. 运行 `python3 tools/build_math_figures.py` 生成26张数学 SVG；需要中文字体，可设置 `CALCULUS_FONT` 为字体文件的路径。预览 PNG 默认输出到 `/tmp/calculus-figure-review`，可通过 `CALCULUS_PREVIEW` 修改。
4. 运行 `python3 tools/check_examples.py` 复核原版中10个代表性数值结果。
5. 运行 `python3 tools/build_reading.py` 更新图文阅读页。

`assets/math-figures.json` 记录图名、图注、使用的版本以及数学核验值。图形不得通过缩放或平移变成与正文公式不符的对象。向量箭头如缩放展示，应在图注中说明。

讲解顺序以章节和正文小节为主线，导图、目录与正文应保持同一顺序。第4章路线图直接读取正文十个二级标题；修改正文标题后应重新生成图。新增概念、图示和例题放入对应的小节，并用简短开场承接上一节，避免按知识类别来回跳转。

## Section与作业内容维护

- `course_structure.json`保存第4章3节、第5章5节与原教程讲解单元的对应关系。
- 两份根目录教程Markdown是讲解内容源；`chapter4/homework*.md`和`chapter5/homework*.md`是作业内容源。每题保留批次、题型、原题号，正文仅包含原题、对应知识点（1—2句话）、解题过程。
- 运行`python3 2_1微积分III/tools/build_reading.py`（仓库根目录）生成Section教程、章节导览、章末总结及全部25个HTML页面。`build_sections.py`检查原讲解单元无遗漏、无重复归类，并检查作业三字段完整。
- `chapter*/section*.md`、`chapter*/README.md`和`chapter*/summary.md`是生成文件，应修改原教程后重新构建。原`chapter4.html`、`chapter5.html`保留整章连续阅读与旧锚点；新章节入口为`chapter4/index.html`和`chapter5/index.html`。
- 运行`python3 tools/generate_sidebar.py --course 2_1微积分III`仅更新课程导航，保留其他课程已有的人工整理。
- 数学与链接检查：`python3 tools/check_math_fragments.py 2_1微积分III`、`python3 2_1微积分III/tools/check_examples.py`、`python3 2_1微积分III/tools/check_homework.py`及`node 2_1微积分III/tools/check_reading.cjs`。

## 阅读色块

讲解原文使用成对的HTML注释标出经过人工选择的重点范围，例如`<!-- study:result|参数计算公式 -->`与`<!-- /study -->`。可用类型为`concept`（核心知识点）、`result`（结论与公式）、`process`（推导说明）、`warning`（易错提醒）；不要跨标题或嵌套标记，定理条件应和公式放在同一范围内。

`assets/emphasis.js`与`assets/emphasis.css`为图文阅读版和Docsify主站共用的渲染与样式。作业的原题、对应知识点、解题过程按现有字段分层；作者用LaTeX的`boxed`命令或明确选项标出的最终答案加结论色块。颜色配合文字标签和边框，保持推导文字的正常对比度。

## 第5章导图与示意图

运行 `python3 tools/build_chapter5_maps.py` 生成6张知识导图和4张教学示意图；再运行 `python3 tools/build_reading.py` 同步 Section Markdown 与离线 HTML。第5章正文仍以 `05_第二型积分_教程.md` 为唯一编辑源，分组见 `course_structure.json`。
