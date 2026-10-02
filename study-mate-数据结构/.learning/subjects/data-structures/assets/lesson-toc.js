/* ═══════════════════════════════════════════════════════════════
   StudyMate · 课件侧边目录（照搬 sayo-ui 文档页的侧边栏）
   ═══════════════════════════════════════════════════════════════
   用法：课件页底部引一次（占位符壳 templates/lesson.html 由渲染器填好后已经带好）：

     <script src="../assets/lesson-toc.js" defer></script>

   目录内容不用手写：本脚本取 <article class="lesson"> 里的全部 <h2>（小节；h3 是节内步骤，
   不进目录），给没有 id 的小节补 sec-N，然后按 sayo-ui 文档页那套结构建出侧边栏：

     <div class="doc-grid">
       <div class="sidebar-backdrop"></div>          ← 移动端遮罩
       <aside class="doc-sidebar" data-syo-scrollspy="100">
         <button class="sidebar-toggle">…</button>   ← 折叠成 44px rail
         <p class="doc-sidebar-title">…本节目录</p>   ← 图标 + 标题
         <a href="#sec-1">…</a> …                     ← 每个 h2 一条
         <nav class="lesson-nav">…</nav>             ← 正文里的上/下节课指针，搬到这里
       </aside>
       <article class="lesson">…</article>
     </div>

    上/下节课指针不在这里生成——它是**课件里的真实链接**（`<nav class="lesson-nav">`，由
    `scripts/render_lesson.py` 按 `curriculum.yaml` 的 nodes 顺序渲染进正文），本脚本只负责把那一块
    搬到目录下面。取值来自 `curriculum.yaml`（节点 id 与顺序），所以交给渲染器算；照原样留在正文里，
    没有 javascript 时也还能点。

   行为也照搬：桌面折叠状态记在 localStorage、≤1024px 自动收成 rail、≤768px 变抽屉
   （顶栏里的汉堡拉开、点遮罩或点链接关掉）；当前小节高亮由 Sayo 的 data-syo-scrollspy 负责
   （本脚本是 defer，先于 DOMContentLoaded 跑完，所以 Sayo 的自动扫描扫得到这些链接）。

   少于两节、或页面上没有 .lesson 时不生成——一两节的目录只是噪音。
   ═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var COLLAPSE_KEY = 'studymate-lesson-toc-collapsed';
  var TOGGLE_SVG = '<svg viewBox="0 0 20 20" fill="none"><path d="M7 4l-1.5 1.5L10.5 10l-5 4.5L7 16l6-6-6-6z" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  var TITLE_SVG = '<svg width="13" height="13" viewBox="0 0 20 20" fill="none"><path d="M5 3h8l4 4v10a1.5 1.5 0 01-1.5 1.5h-9A1.5 1.5 0 014 17V4.5A1.5 1.5 0 015.5 3z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M13 3v4h4M7 9h6M7 12.5h4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>';
  var HAMBURGER_SVG = '<svg width="18" height="18" viewBox="0 0 20 20" fill="none"><path d="M3 5h14M3 10h14M3 15h14" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>';

  /* localStorage 在 file:// 下不一定可用（各浏览器策略不同），失败了就当没记住 */
  function readCollapsed() {
    try {
      var value = window.localStorage.getItem(COLLAPSE_KEY);
      return value === '1' ? true : value === '0' ? false : null;
    } catch (e) { return null; }
  }
  function writeCollapsed(value) {
    try { window.localStorage.setItem(COLLAPSE_KEY, value ? '1' : '0'); } catch (e) { /* 忽略 */ }
  }
  function svg(html) {
    var holder = document.createElement('span');
    holder.innerHTML = html;
    return holder.firstChild;
  }

  function build() {
    var lesson = document.querySelector('article.lesson');
    if (!lesson || document.querySelector('.doc-sidebar')) return;

    var headings = [];
    Array.prototype.forEach.call(lesson.querySelectorAll('h2'), function (h2) {
      var text = (h2.textContent || '').trim();
      if (!text) return;
      if (!h2.id) h2.id = 'sec-' + (headings.length + 1);
      headings.push({ id: h2.id, text: text });
    });
    if (headings.length < 2) return;

    // ① 两列网格外壳（照搬 .doc-grid）：article 搬进去当第二列
    var grid = document.createElement('div');
    grid.className = 'doc-grid';
    lesson.parentNode.insertBefore(grid, lesson);
    grid.appendChild(lesson);

    // ② 移动端遮罩
    var backdrop = document.createElement('div');
    backdrop.className = 'sidebar-backdrop';
    grid.insertBefore(backdrop, lesson);

    // ③ 侧边栏本体
    var aside = document.createElement('aside');
    aside.className = 'doc-sidebar';
    aside.setAttribute('data-syo-scrollspy', '100');

    var toggle = document.createElement('button');
    toggle.type = 'button';
    toggle.className = 'sidebar-toggle';
    toggle.title = '折叠侧边栏';
    toggle.setAttribute('aria-label', '折叠侧边栏');
    toggle.appendChild(svg(TOGGLE_SVG));
    aside.appendChild(toggle);

    var title = document.createElement('p');
    title.className = 'doc-sidebar-title';
    title.appendChild(svg(TITLE_SVG));
    var titleText = document.createElement('span');
    titleText.textContent = '本节目录';
    title.appendChild(titleText);
    aside.appendChild(title);

    headings.forEach(function (item) {
      var link = document.createElement('a');
      link.href = '#' + item.id;
      link.textContent = item.text;
      aside.appendChild(link);
    });

    // ③b 上/下节课指针：把正文里的 .lesson-nav 搬到目录下面（appendChild 自带"从原位移走"）。
    //     页面里没有这一块（第一课没写、或旧课件）就跳过。
    var nav = lesson.querySelector('.lesson-nav');
    if (nav) aside.appendChild(nav);

    grid.insertBefore(aside, lesson);

    // ④ 顶栏里的汉堡（只有 ≤768px 显示，CSS 管可见性）
    var bar = document.querySelector('.lesson-bar');
    var hamburger = null;
    if (bar) {
      hamburger = document.createElement('button');
      hamburger.type = 'button';
      hamburger.className = 'nav-hamburger';
      hamburger.title = '菜单';
      hamburger.setAttribute('aria-label', '菜单');
      hamburger.appendChild(svg(HAMBURGER_SVG));
      bar.insertBefore(hamburger, bar.firstChild);
    }

    // ⑤ 行为（照搬 sayo-ui 文档页那段脚本）
    function isMobile() { return window.innerWidth <= 768; }
    function openMobile() {
      aside.classList.add('mobile-open');
      backdrop.classList.add('show');
      document.body.style.overflow = 'hidden';
    }
    function closeMobile() {
      aside.classList.remove('mobile-open');
      backdrop.classList.remove('show');
      document.body.style.overflow = '';
    }

    var collapsed = readCollapsed();
    function syncCollapsed() {
      aside.classList.toggle('collapsed', collapsed === null ? window.innerWidth <= 1024 : collapsed);
    }
    if (!isMobile()) syncCollapsed();

    toggle.addEventListener('click', function () {
      if (isMobile()) {
        if (aside.classList.contains('mobile-open')) closeMobile(); else openMobile();
        return;
      }
      collapsed = aside.classList.toggle('collapsed');
      writeCollapsed(collapsed);
    });

    if (hamburger) {
      hamburger.addEventListener('click', function () {
        if (aside.classList.contains('mobile-open')) closeMobile(); else openMobile();
      });
    }

    backdrop.addEventListener('click', closeMobile);

    window.addEventListener('resize', function () {
      if (!isMobile() && aside.classList.contains('mobile-open')) closeMobile();
      if (!isMobile()) syncCollapsed();
    });

    Array.prototype.forEach.call(aside.querySelectorAll('a'), function (link) {
      link.addEventListener('click', function () { if (isMobile()) closeMobile(); });
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', build);
  else build();
})();
