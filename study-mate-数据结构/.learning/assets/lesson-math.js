/* StudyMate · 课件公式排版（离线 KaTeX，MIT，见 katex/LICENSE）
 *
 * 渲染器把 `$…$` 与 `$$…$$` 写成：
 *   <span class="math-inline">TeX 原文</span>   /   <div class="math-block">TeX 原文</div>
 * 元素里**先放 TeX 原文**——没有 JS、或 KaTeX 没加载成功时，学生读到的还是公式源码（降级可读，
 * 不会白屏）。这个脚本加载后把它们替换成排版结果。
 *
 * 只处理这两个类名，不做全文扫描：代码块里的 `$` 不该被当成公式，扫描式方案（auto-render）
 * 分不清代码与正文，所以这里由渲染器明确标出位置。
 */
(function () {
  'use strict';

  /* 排 `root` 里所有还没排过的公式；返回排了几条。
     题面/选项/解析是 quiz.js 建块时**动态**插进来的（本脚本在它之前跑完），
     所以那个文件会拿着自己的块再调一次 LessonMath.render(block)。
     排过的节点打标记跳过——重复排会把上一次的产物当成 TeX 再排一遍。 */
  function renderWithin(root) {
    if (typeof katex === 'undefined') return 0;
    var scope = root || document;
    var nodes = scope.querySelectorAll('.math-inline, .math-block');
    var done = 0;
    for (var index = 0; index < nodes.length; index += 1) {
      var node = nodes[index];
      if (node.getAttribute('data-math-done') === '1') continue;
      var tex = node.textContent;
      try {
        katex.render(tex, node, {
          displayMode: node.classList.contains('math-block'),
          throwOnError: false,      // TeX 写错时显示成红色原文，不炸整页
          strict: 'ignore'
        });
      } catch (error) {
        node.textContent = tex;     // 兜底：留着原文
      }
      node.setAttribute('data-math-done', '1');
      done += 1;
    }
    return done;
  }

  window.LessonMath = { render: renderWithin };
  renderWithin(document);
})();
