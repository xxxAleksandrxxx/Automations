(() => {
  async function loadKeywords() {
    const url = chrome.runtime.getURL('jql_keywords.json');
    const resp = await fetch(url);
    const data = await resp.json();
    return Array.isArray(data.keywords) ? data.keywords : [];
  }

  function encodeJQL(query) {
    return encodeURIComponent(query);
  }

  function filterKeywords(keywords, prefix) {
    const p = prefix.toLowerCase();
    return keywords.filter(k => k.toLowerCase().startsWith(p));
  }

  // Expose for popup.js
  window.Utils = { loadKeywords, encodeJQL, filterKeywords };

  // Also expose for Node-based tests (if you have Node installed)
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { loadKeywords, encodeJQL, filterKeywords };
  }
})();
