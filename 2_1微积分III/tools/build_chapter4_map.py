"""Build the chapter 4 route from the actual ordered Markdown headings."""
from pathlib import Path
from html import escape
import re
import textwrap
ROOT=Path(__file__).resolve().parents[1]

def build(output):
    headings=re.findall(r'^## (\d+) (.+)$',(ROOT/'04_第一型积分_教程.md').read_text(),re.M)
    assert [int(n) for n,_ in headings]==list(range(1,11)), 'Chapter map expects sections 1–10 in order'
    titles={int(n):t for n,t in headings}
    groups=[('曲线：理解 → 定义 → 计算 → 简化',[1,2,3,4],'#168A88','#E9F5F3'),('曲面：面积元 → 完整例题',[5,6],'#4777B5','#EDF2FA'),('统一视角 → 物理应用',[7,8],'#8263A9','#F2EDF8'),('方法整理 → 自测',[9,10],'#BD784B','#FAF0E8')]
    notes=['从分段质量理解累加','先认清积分的对象','求 ds，再代入计算','域与函数一起检查','投影与参数两种工具','斜面、抛物面、球面、柱面','长度、面积、体积的共同思想','质量 → 质心 → 惯量 → 引力','按条件选择计算方法','先独立作答，再核对解答']
    parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="810" viewBox="0 0 1120 810" role="img" aria-labelledby="map-title map-desc">
<title id="map-title">第4章：按章节顺序展开的学习路线</title>
<desc id="map-desc">按正文十个小节顺序，从曲线积分到曲面积分，再到统一视角与物理应用，最后整理方法并自测。每行从左向右，各行自上而下。</desc>
<style>text{font-family:"PingFang SC","Microsoft YaHei","Noto Sans CJK SC",sans-serif;fill:#243747}.muted{fill:#657789}</style>
<rect width="1120" height="810" rx="20" fill="#FAFBFD"/>
<text x="40" y="43" font-size="13" letter-spacing="2" class="muted">CHAPTER 04 · 学习路线</text>
<text x="40" y="85" font-size="34" font-weight="600">第一型积分</text>
<text x="40" y="117" font-size="18" class="muted">按正文顺序读：每行从左到右，再进入下一行。</text>
<rect x="660" y="40" width="420" height="80" rx="14" fill="#203E50"/>
<text x="684" y="72" font-size="17" style="fill:#FFFFFF">共同思想：函数值 × 几何微元</text>
<text x="684" y="100" font-size="16" style="fill:#B8D6DF">曲线取 ds · 曲面取 dS · 分割后累加</text>
<path d="M64 180 V658" fill="none" stroke="#DDE6EC" stroke-width="3"/>
''']
    for row,(label,nums,color,tint) in enumerate(groups):
        y=148+row*148
        parts.append(f'<circle cx="64" cy="{y+26}" r="12" fill="{color}"/>')
        parts.append(f'<rect x="98" y="{y}" width="982" height="132" rx="16" fill="white" stroke="#E0E7EE"/>')
        parts.append(f'<text x="120" y="{y+28}" font-size="18" font-weight="600" style="fill:{color}">{escape(label)}</text>')
        parts.append(f'<text x="1058" y="{y+28}" text-anchor="end" font-size="14" class="muted">§{nums[0]}—§{nums[-1]}</text>')
        width=936/len(nums)
        for col,n in enumerate(nums):
            x=120+col*width
            parts.append(f'<rect x="{x}" y="{y+48}" width="30" height="24" rx="7" fill="{tint}"/>')
            parts.append(f'<text x="{x+15}" y="{y+66}" text-anchor="middle" font-size="13" font-weight="600" style="fill:{color}">{n:02d}</text>')
            wrap_width=(len(titles[n])+1)//2 if len(nums)==4 and len(titles[n])>9 else 24
            lines=textwrap.wrap(titles[n],width=wrap_width)
            for i,line in enumerate(lines):
                parts.append(f'<text x="{x+40}" y="{y+66+i*24}" font-size="18" font-weight="500">{escape(line)}</text>')
            parts.append(f'<text x="{x+40}" y="{y+115}" font-size="14" class="muted">{escape(notes[n-1])}</text>')
            if col<len(nums)-1:
                parts.append(f'<text x="{x+width-14}" y="{y+78}" text-anchor="middle" font-size="20" style="fill:{color}">→</text>')
    parts.append('''<path d="M40 754 H1080" stroke="#DFE6EE"/>
<text x="40" y="786" font-size="16" class="muted">01—10 与下文十个小节一一对应；§编号指本教程小节。</text>
<text x="1080" y="786" text-anchor="end" font-size="16" class="muted">每一步都承接上一步</text>
</svg>''')
    Path(output).write_text('\n'.join(parts),encoding='utf-8')

if __name__=='__main__':
    build(ROOT/'assets/map4.svg')
