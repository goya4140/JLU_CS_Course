# 来源与构建

本目录的 HTML 页面和 `.learning/assets/` 由 StudyMate 的静态生成器生成。原项目：[Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate)，MIT License。本次使用 commit `e8be34293d3f064f5ee40cd3043a31939c5255df`。课程内容文件、`curriculum.yaml` 和 `subject.yaml` 为本站编写。

构建时使用的 StudyMate commit 由下方记录；要重新生成，请检出该版本，然后在 StudyMate 仓库根目录运行：

```sh
python3 scripts/render_lesson.py /path/to/JLU_CS_Course/study-mate-数据结构/.learning/subjects/data-structures list.link
python3 scripts/render_lesson.py /path/to/JLU_CS_Course/study-mate-数据结构/.learning/subjects/data-structures graph.dijkstra
python3 scripts/render_lesson.py /path/to/JLU_CS_Course/study-mate-数据结构/.learning/subjects/data-structures sort.quick
python3 scripts/gen_home.py /path/to/JLU_CS_Course/study-mate-数据结构
```

## 对照范围

| 样例课件 | 本站原有笔记 | 课程讲义 |
| --- | --- | --- |
| 单链表与哨位结点 | 第 2 章线性表、栈与队列 | Lecture 3 线性表的链接存储 |
| Dijkstra 最短路径 | 第 5 章图 | Lecture 17 图的最短路径 |
| 快速排序与分划 | 第 6 章排序 | Lecture 21 快速排序 |

样例只覆盖三个知识点，现有完整课程仍是全部章节的入口。页面内答题交互在访问者浏览器中运行，不向仓库写回进度。
