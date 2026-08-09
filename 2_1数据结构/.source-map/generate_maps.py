#!/usr/bin/env python3
"""Build auditable per-slide maps from the verified PowerPoint-export inventory."""

from __future__ import annotations

import json
import sys
from pathlib import Path


TARGETS = {
    3: "02_线性表栈与队列/02_1_线性表.md",
    4: "02_线性表栈与队列/02_4_链表双指针技巧.md",
    5: "02_线性表栈与队列/02_2_栈.md",
    6: "02_线性表栈与队列/02_3_队列.md",
    7: "03_数组矩阵与字符串/03_2_特殊矩阵的压缩存储.md",
    8: "03_数组矩阵与字符串/03_3_字符串与模式匹配.md",
    9: "04_树与二叉树/04_1_树的基本概念.md",
    10: "04_树与二叉树/04_2_二叉树.md",
    11: "04_树与二叉树/04_3_线索二叉树.md",
    12: "04_树与二叉树/04_4_树与森林.md",
    13: "04_树与二叉树/04_7_哈夫曼树与哈夫曼编码.md",
    14: "05_图/05_1_图的基本概念与存储.md",
    15: "05_图/05_2_图的遍历.md",
    16: "05_图/05_3_拓扑排序与关键路径.md",
    17: "05_图/05_4_最短路径.md",
    18: "05_图/05_5_最小生成树.md",
    19: "06_排序/06_2_插入类排序.md",
    20: "06_排序/06_3_选择类排序.md",
    21: "06_排序/06_4_交换类排序.md",
    22: "06_排序/06_5_归并排序.md",
    23: "06_排序/06_6_分布类排序.md",
    24: "07_查找/07_2_线性结构查找.md",
    25: "07_查找/07_3_二叉查找树.md",
    26: "07_查找/07_4_平衡查找树.md",
    27: "07_查找/07_5_哈希表.md",
    28: "07_查找/07_6_堆与优先级队列.md",
}

EXCLUDED_MARKERS = (
    "练习", "思考", "oj", "leetcode", "面试题",
    "考研题", "期末", "计入成绩", "作业", "慕课自学内容",
)


def lecture_number(path: Path) -> int:
    return int(path.name.split("-", 1)[0].split()[1])


def target_for(lecture: int, slide: int) -> str:
    if lecture == 7:
        if slide <= 10:
            return "03_数组矩阵与字符串/03_1_数组与多维数组.md"
        if slide <= 41:
            return "03_数组矩阵与字符串/03_2_特殊矩阵的压缩存储.md"
        return "03_数组矩阵与字符串/03_4_数组上的动态规划与子集生成.md"
    if lecture == 13 and slide >= 65:
        return "04_树与二叉树/04_8_表达式树与并查集.md"
    if lecture == 25 and slide >= 46:
        return "04_树与二叉树/04_6_平衡二叉树.md"
    return TARGETS[lecture]


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: generate_maps.py INVENTORY_DIRECTORY")
    inventory_dir = Path(sys.argv[1])
    output_dir = Path(__file__).resolve().parent

    for inventory_path in sorted(inventory_dir.glob("Lecture*.json"), key=lecture_number):
        lecture = lecture_number(inventory_path)
        if lecture not in TARGETS:
            continue
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
        slides = []
        for item in inventory["slides"]:
            number = item["slide"]
            normalized = "".join(item.get("text", "").lower().split())
            if number == 2:
                entry = {"slide": number, "disposition": "omitted", "reason": "课程引语或装饰页"}
            elif any(marker in normalized for marker in EXCLUDED_MARKERS):
                entry = {"slide": number, "disposition": "omitted", "reason": "非讲解型课堂任务或课程管理信息"}
            else:
                entry = {
                    "slide": number,
                    "disposition": "used" if number == 1 else "merged",
                    "target": target_for(lecture, number),
                }
            slides.append(entry)

        result = {
            "source_file": Path(inventory["source_path"]).name,
            "source_format": inventory["source_format"],
            "powerpoint_provenance_verified": inventory["powerpoint_provenance_verified"],
            "total_slides": inventory["total_slides"],
            "mapping_note": "连续动画帧合并为概念过程；引语、课程管理信息和非讲解型任务页不进入学习正文。",
            "slides": slides,
        }
        output_path = output_dir / f"lecture-{lecture:02d}.json"
        output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(output_path.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
