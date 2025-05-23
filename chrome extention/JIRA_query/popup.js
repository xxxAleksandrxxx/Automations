(() => {
  const BASE_URL = 'https://lab14-analysis.atlassian.net/issues/?jql=';

  let keywords = [];
  let suggestions = [];
  let selectedIndex = -1;

  const inputEl = document.getElementById('jql-input');
  const listEl = document.getElementById('autocomplete-list');
  const okBtn = document.getElementById('ok-btn');
  const cancelBtn = document.getElementById('cancel-btn');

  // Insert suggestions into the UL
  function renderSuggestions() {
    listEl.innerHTML = '';
    if (!suggestions.length) {
      listEl.style.display = 'none';
      return;
    }
    suggestions.forEach((kw, idx) => {
      const li = document.createElement('li');
      li.textContent = kw;
      li.dataset.index = idx;
      if (idx === selectedIndex) li.classList.add('selected');
      li.addEventListener('mousedown', e => {
        // apply on click
        applySuggestion(idx);
        e.preventDefault();
      });
      listEl.appendChild(li);
    });
    listEl.style.display = 'block';
  }

  // Replace the last token with the chosen suggestion + trailing space
  function applySuggestion(idx) {
    const kw = suggestions[idx];
    const val = inputEl.value;
    // split on whitespace, preserve everything before last token
    const parts = val.split(/\s+/);
    parts.pop();
    parts.push(kw);
    const newVal = parts.join(' ') + ' ';
    inputEl.value = newVal;
    inputEl.focus();
    // reset suggestions
    suggestions = [];
    selectedIndex = -1;
    renderSuggestions();
  }

  // On every input, update suggestions
  async function onInput() {
    const val = inputEl.value;
    const tokens = val.split(/\s+/);
    const prefix = tokens[tokens.length - 1];
    if (!prefix) {
      suggestions = [];
    } else {
      suggestions = Utils.filterKeywords(keywords, prefix);
    }
    selectedIndex = suggestions.length ? 0 : -1;
    renderSuggestions();
  }

  // Handle key navigation and selection
  function onKeyDown(e) {
    if (suggestions.length) {
      switch (e.key) {
        case 'ArrowDown':
          e.preventDefault();
          selectedIndex = Math.min(selectedIndex + 1, suggestions.length - 1);
          renderSuggestions();
          return;
        case 'ArrowUp':
          e.preventDefault();
          selectedIndex = Math.max(selectedIndex - 1, 0);
          renderSuggestions();
          return;
        case 'Tab':   // tab bar to use suggestion
        // case ' ':  // space bar to use suggestion - don't use it
          // apply suggestion on Tab or Space
          e.preventDefault();
          applySuggestion(selectedIndex);
          return;
      }
    }

    if (e.key === 'Enter') {
      e.preventDefault();
      runQuery();
    } else if (e.key === 'Escape') {
      e.preventDefault();
      window.close();
    }
  }

  // Open the Jira URL with the encoded query
  function runQuery() {
    const query = inputEl.value.trim();
    if (!query) return;
    const url = BASE_URL + Utils.encodeJQL(query);
    window.open(url, '_blank');
    window.close();
  }

  // Initialize
  document.addEventListener('DOMContentLoaded', async () => {
    keywords = await Utils.loadKeywords();
    inputEl.addEventListener('input', onInput);
    inputEl.addEventListener('keydown', onKeyDown);
    okBtn.addEventListener('click', runQuery);
    cancelBtn.addEventListener('click', () => window.close());
  });
})();
