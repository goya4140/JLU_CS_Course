/* Shared semantic reading layers for offline HTML and the Docsify course. */
(function () {
  const names = {
    concept: '核心知识点', result: '结论与公式',
    process: '推导与说明', warning: '易错提醒'
  };

  function card(kind, title) {
    const box = document.createElement('section');
    box.className = 'study-card study-' + kind;
    box.setAttribute('aria-label', title || names[kind]);
    const label = document.createElement('div');
    label.className = 'study-card-title';
    label.textContent = title || names[kind];
    box.append(label);
    return box;
  }

  function authorNotes(root) {
    // Author-selected ranges: no guess based on equation length or heading text.
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_COMMENT);
    const starts = [];
    while (walker.nextNode()) {
      if (/^study:(concept|result|process|warning)(?:\|.*)?$/.test(walker.currentNode.data.trim())) {
        starts.push(walker.currentNode);
      }
    }
    for (const start of starts) {
      const match = start.data.trim().match(/^study:(concept|result|process|warning)(?:\|(.*))?$/);
      let end = start.nextSibling;
      while (end && !(end.nodeType === Node.COMMENT_NODE && end.data.trim() === '/study')) end = end.nextSibling;
      if (!end) continue;
      const note = card(match[1], match[2]);
      start.before(note);
      while (start.nextSibling !== end) note.append(start.nextSibling);
      start.remove();
      end.remove();
    }
  }

  function homeworkLayers(root) {
    const roles = { '原题': 'question', '对应知识点': 'concept', '解题过程': 'process' };
    const fields = Array.from(root.children).filter(node => {
      const strong = node.tagName === 'P' && node.firstElementChild;
      return strong && strong.tagName === 'STRONG' && roles[strong.textContent.trim()];
    });
    for (const field of fields) {
      if (field.parentElement !== root) continue;
      const title = field.firstElementChild.textContent.trim();
      const followingText = field.firstElementChild.nextSibling;
      if (followingText && followingText.nodeType === Node.TEXT_NODE) {
        followingText.data = followingText.data.replace(/^[:：]\s*/, '');
      }
      const box = document.createElement('section');
      box.className = 'study-card study-' + roles[title];
      box.setAttribute('aria-label', title);
      field.before(box);
      let node = field;
      while (node) {
        const next = node.nextSibling;
        if (node !== field && (fields.includes(node) || /^H[12]$/.test(node.nodeName))) break;
        box.append(node);
        node = next;
      }
      field.classList.add('study-field-title');
    }
    // The author already identifies answers with \boxed or an explicit choice.
    for (const process of root.querySelectorAll('.study-process')) {
      for (const paragraph of Array.from(process.children)) {
        if (paragraph.tagName !== 'P' || paragraph.classList.contains('study-field-title')) continue;
        const boxed = Array.from(paragraph.querySelectorAll('annotation[encoding="application/x-tex"]'))
          .some(node => /\\boxed(?![A-Za-z])/.test(node.textContent));
        const answer = /(?:故选|选\s*[A-D]|答案为)/.test(paragraph.textContent);
        const choice = /(?:选|正确|答案)/.test(paragraph.textContent) &&
          Array.from(paragraph.querySelectorAll('strong')).some(node => /^[A-D]$/.test(node.textContent.trim()));
        if (!boxed && !answer && !choice) continue;
        const result = card('result', '结论');
        paragraph.before(result);
        result.append(paragraph);
      }
    }
  }

  window.applyCalculusEmphasis = function (root) {
    if (!root) return;
    authorNotes(root);
    homeworkLayers(root);
    if (!root.querySelector('.study-card') || root.querySelector('.study-legend')) return;
    const legend = document.createElement('div');
    legend.className = 'study-legend';
    legend.setAttribute('aria-label', '色块阅读提示');
    for (const [kind, title] of [['concept','知识点'], ['result','结论 / 公式'], ['process','推导 / 说明'], ['warning','易错提醒']]) {
      const item = document.createElement('span');
      item.className = 'study-chip study-' + kind;
      item.textContent = title;
      legend.append(item);
    }
    const heading = root.querySelector('h1');
    if (heading) heading.after(legend);
  };
})();
