"""Build offline HTML with course → chapter → Section → homework navigation."""
from pathlib import Path
import json
import posixpath
import re
from html import escape
from build_sections import build, STRUCTURE

ROOT = Path(__file__).resolve().parents[1]


def relative(target, current):
    return posixpath.relpath(target, posixpath.dirname(current) or '.')


def generate():
    build()
    pages = [
        ('index.html', 'README.md', '课程导览'),
        ('chapter4.html', '04_第一型积分_教程.md', '第4章 · 整章连续阅读'),
        ('chapter5.html', '05_第二型积分_教程.md', '第5章 · 整章连续阅读'),
        ('review.html', '06_期末题型与复习路线.md', '真题与复习'),
        ('sources.html', '资料依据与覆盖对照.md', '资料依据'),
    ]
    for chapter in STRUCTURE['chapters']:
        ch = chapter['number']
        base = f'chapter{ch}'
        pages.append((f'{base}/index.html', f'{base}/README.md', f'第{ch}章 · {chapter["title"]}'))
        for section in chapter['sections']:
            n = section['number']
            title = f'{ch}.{n} {section["title"]}'
            pages.append((f'{base}/section{n}.html', f'{base}/section{n}.md', title))
            pages.append((f'{base}/homework{n}.html', f'{base}/homework{n}.md', f'{ch}.{n} 作业解读'))
        pages.append((f'{base}/summary.html', f'{base}/summary.md', f'第{ch}章 · 总结与自测'))
    # Reading order traverses lessons, not every homework answer page.
    order = ['index.html']
    for chapter in STRUCTURE['chapters']:
        ch = chapter['number']
        order += [f'chapter{ch}/index.html']
        order += [f'chapter{ch}/section{s["number"]}.html' for s in chapter['sections']]
        order += [f'chapter{ch}/summary.html']
    order += ['review.html', 'sources.html']
    titles = {html: title for html, md, title in pages}
    mapping = {md: html for html, md, title in pages}
    for html, md, title in pages:
        prefix = relative('assets', html)
        linkmap = {relative(source, md): relative(target, html) for source, target in mapping.items()}
        for original_link in re.findall(r'\]\(([^\s)]+\.md)\)', (ROOT/md).read_text()):
            normalized = posixpath.normpath(posixpath.join(posixpath.dirname(md), original_link))
            if normalized in mapping:
                linkmap[original_link] = relative(mapping[normalized], html)
        linkmap['https://goya4140.github.io/JLU_CS_Course/2_1%E5%BE%AE%E7%A7%AF%E5%88%86III/index.html'] = relative('index.html', html)
        current_ch = next((c for c in STRUCTURE['chapters'] if html.startswith(f'chapter{c["number"]}/') or html == f'chapter{c["number"]}.html'), None)
        def anchor(target, label, css=''):
            active = 'active' if html == target else ''
            selected = ' aria-current="page"' if active else ''
            return f'<a class="{css} {active}" href="{relative(target, html)}"{selected}>{escape(label)}</a>'
        nav = anchor('index.html', '课程导览')
        for chapter in STRUCTURE['chapters']:
            ch = chapter['number']
            opened = ' open' if current_ch == chapter else ''
            nav += f'<details class="chapter-nav"{opened}><summary>第{ch}章 · {chapter["title"]}</summary>'
            nav += anchor(f'chapter{ch}/index.html', '本章导览')
            for section in chapter['sections']:
                n = section['number']
                nav += '<div class="section-nav">'
                nav += anchor(f'chapter{ch}/section{n}.html', f'{ch}.{n} {section["title"]}')
                nav += anchor(f'chapter{ch}/homework{n}.html', '作业解读', 'homework-link') + '</div>'
            nav += anchor(f'chapter{ch}/summary.html', '章末总结与自测') + '</details>'
        nav += anchor('review.html', '真题与复习') + anchor('sources.html', '资料依据')
        crumb = anchor('index.html', '微积分 III')
        tabs = ''
        if current_ch:
            ch = current_ch['number']
            chapter_index = f'chapter{ch}/index.html'
            crumb += ' / ' + anchor(chapter_index, f'第{ch}章 {current_ch["title"]}')
            section = next((s for s in current_ch['sections'] if md in (f'chapter{ch}/section{s["number"]}.md', f'chapter{ch}/homework{s["number"]}.md')), None)
            if section:
                n = section['number']
                crumb += f' / {ch}.{n}'
                tabs = '<nav class="lesson-tabs" aria-label="本节内容">' + anchor(f'chapter{ch}/section{n}.html', '本节教程') + anchor(f'chapter{ch}/homework{n}.html', '作业解读') + anchor(chapter_index, '本章目录') + '</nav>'
        if html in order:
            i = order.index(html)
            previous = anchor(order[i-1], '← ' + titles[order[i-1]]) if i else '<span></span>'
            following = anchor(order[i+1], titles[order[i+1]] + ' →') if i+1 < len(order) else '<span></span>'
        else:
            previous = anchor(f'chapter{current_ch["number"]}/index.html', '← 本章目录')
            following = anchor(md.replace('homework','section').replace('.md','.html'), '返回本节教程 →') if 'homework' in md else '<span></span>'
        data = json.dumps({'markdown': (ROOT/md).read_text(), 'links': linkmap}, ensure_ascii=False).replace('<', '\\u003c')
        site_home = relative('../index.html', html) + '#/'
        doc = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} | 微积分 III</title><link rel="stylesheet" href="{prefix}/vendor/katex.css"><link rel="stylesheet" href="{prefix}/reading.css"><link rel="stylesheet" href="{prefix}/emphasis.css?v=20261030-1"></head>
<body><header class="top"><a href="{site_home}" style="color:#cfdee3;text-decoration:none;font-size:14px">JLU CS Course / 大二上</a><br><strong>微积分 III · 第4、5章</strong><p>按章节与 Section 学习 · 图文教程与平时作业</p></header>
<div class="layout"><aside class="nav" aria-label="课程导航"><details id="course-menu" open><summary>课程目录</summary>{nav}</details><div class="label">本页目录</div><nav id="toc" aria-label="本页目录"></nav></aside>
<main><div class="breadcrumb">{crumb}</div>{tabs}<article id="content"></article><div class="foot">{previous}{following}</div><noscript>本阅读页需要启用 JavaScript；也可在 GitHub 仓库直接阅读对应 Markdown 文件。</noscript></main></div>
<footer>JLU CS Course · 教材 Section 导航 · 本地公式与图片资源</footer>
<script type="application/json" id="data">{data}</script><script src="{prefix}/vendor/marked.js"></script><script src="{prefix}/vendor/katex.js"></script><script src="{prefix}/emphasis.js?v=20261026-1"></script><script src="{prefix}/reading.js?v=20261026-1"></script></body></html>'''
        (ROOT/html).write_text(doc)
    print(f'Built {len(pages)} offline reading pages')


if __name__ == '__main__':
    generate()
