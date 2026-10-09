"""Build the chapter 4 concept map as a readable, editable SVG."""
from pathlib import Path
from html import escape

def build(output):
    parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="730" viewBox="0 0 1120 730" role="img" aria-labelledby="map-title map-desc">
<title id="map-title">第4章：第一型积分学习地图</title>
<desc id="map-desc">中央是函数值乘几何微元的累加思想，四个分支为曲线积分、曲面积分、性质与技巧、物理应用。下方给出从模型到计算的阅读顺序。</desc>
<style>text{font-family:"PingFang SC","Microsoft YaHei","Noto Sans CJK SC",sans-serif;fill:#243747}.muted{fill:#657789}.heading{font-size:25px;font-weight:600}.body{font-size:19px}.section{font-size:15px}</style>
<rect width="1120" height="730" rx="20" fill="#FAFBFD"/>
<text x="40" y="43" font-size="13" letter-spacing="2" class="muted">CHAPTER 04 · 学习地图</text>
<text x="40" y="85" font-size="34" font-weight="600">第一型积分</text>
<text x="40" y="117" font-size="18" class="muted">先理解累加的对象，再选择微元与计算方法。</text>
''']
    branches=[
        (40,160,'01','曲线积分','#168A88','#E9F5F3', ['沿一条线，累加每一小段','函数值 × 弧长 ds','参数化 → 一元定积分'],'§1—§4 · 圆弧 / 折线 / 空间曲线'),
        (750,160,'02','曲面积分','#4777B5','#EDF2FA', ['沿一片面，累加每一小块','函数值 × 面积 dS','投影 / 参数化 → 二重积分'],'§5—§7 · 斜面 / 球面 / 柱面'),
        (40,425,'03','性质与技巧','#8263A9','#F2EDF8', ['线性、分段、估值','先检查积分域，再使用对称性','用积分求长度、面积与平均值'],'贯穿全章 · §4、§7 重点讲解'),
        (750,425,'04','物理应用','#BD784B','#FAF0E8', ['质量 → 坐标加权 → 质心','到轴的距离平方 → 转动惯量','距离与方向 → 引力'],'§8 · 先写质量元 dm，再加权'),
    ]
    # Connect each branch directly to the central concept; no shared crossing bus.
    for x,y,n,title,color,tint,lines,section in branches:
        left=x<500
        start=(410,335 if y<400 else 405) if left else (710,335 if y<400 else 405)
        end=(370,y+100) if left else (750,y+100)
        a,b=start;c,d=end
        parts.append(f'<path d="M{a} {b} C{(a+c)/2} {b} {(a+c)/2} {d} {c} {d}" fill="none" stroke="{color}" stroke-opacity=".55" stroke-width="2.5"/>')
        parts.append(f'<circle cx="{c}" cy="{d}" r="4" fill="{color}"/>')
    parts.append('''<rect x="410" y="285" width="300" height="175" rx="22" fill="#203E50"/>
<text x="560" y="318" text-anchor="middle" font-size="13" letter-spacing="2" style="fill:#B8D6DF">全章的共同思想</text>
<text x="560" y="358" text-anchor="middle" font-size="26" font-weight="600" style="fill:#FFFFFF">函数值 × 几何微元</text>
<path d="M452 377 H668" stroke="#5B7887" stroke-width="1"/>
<text x="560" y="407" text-anchor="middle" font-size="19" style="fill:#DFEDF1">沿曲线 / 曲面累加</text>
<text x="560" y="436" text-anchor="middle" font-size="15" style="fill:#B8D6DF">曲线取 ds · 曲面取 dS</text>''')
    for x,y,n,title,color,tint,lines,section in branches:
        parts.append(f'<rect x="{x}" y="{y}" width="330" height="205" rx="16" fill="white" stroke="#E0E7EE"/>')
        parts.append(f'<rect x="{x+20}" y="{y+20}" width="35" height="30" rx="9" fill="{tint}"/>')
        parts.append(f'<text x="{x+37.5}" y="{y+41}" text-anchor="middle" font-size="14" font-weight="600" style="fill:{color}">{n}</text>')
        parts.append(f'<text x="{x+67}" y="{y+44}" class="heading">{escape(title)}</text>')
        for i,line in enumerate(lines):
            parts.append(f'<text x="{x+22}" y="{y+83+i*30}" class="body">{escape(line)}</text>')
        parts.append(f'<path d="M{x+22} {y+162} H{x+308}" stroke="#EDF0F4"/>')
        parts.append(f'<text x="{x+22}" y="{y+186}" class="section" style="fill:{color}">{escape(section)}</text>')
    parts.append('''<path d="M40 666 H1080" stroke="#DFE6EE"/>
<text x="40" y="702" font-size="16" class="muted">建议阅读顺序</text>
<text x="220" y="702" font-size="18">具体模型</text><text x="330" y="702" font-size="18" class="muted">→</text>
<text x="374" y="702" font-size="18">选微元</text><text x="465" y="702" font-size="18" class="muted">→</text>
<text x="509" y="702" font-size="18">建立积分式</text><text x="641" y="702" font-size="18" class="muted">→</text>
<text x="685" y="702" font-size="18">完成计算</text><text x="794" y="702" font-size="18" class="muted">→</text>
<text x="838" y="702" font-size="18">检查结果</text>
</svg>''')
    Path(output).write_text('\n'.join(parts),encoding='utf-8')

if __name__=='__main__':
    build(Path(__file__).resolve().parents[1]/'assets/map4.svg')
