# Jira JQL Autocomplete Chrome Extension

A Chrome extension that provides a multiline input window for constructing Jira JQL queries with autocomplete for fields and operators, customizable styling, and hotkey support for quick access.

## Features

* **Autocomplete**: Suggests JQL fields and operators from a customizable JSON list.
* **Multiline Input**: 5-line textarea for long queries with word wrapping.
* **Keyboard Navigation**: Navigate suggestions with Arrow keys and select with Tab, Space, or mouse.
* **OK/Cancel**: Submit your JQL to open in Jira or cancel to close the popup.
* **Customizable Theme**: Dark mode with configurable colors in `popup.css`.
* **Hotkey Support**: Bind a keyboard shortcut (e.g., Ctrl+Shift+J) to open the popup.
* **Easy Development**: Modular code with `utils.js`, `popup.js`, JSON keywords, and tests.

## Getting Started

### Prerequisites

* Chrome (v88+ recommended)
* Node.js (optional, for running tests)
* Git

### Installation

1. **Save project folder as zip file**
   
2. **Unzip archive**
   
3. **Add extention to Chrome**
   * Open `chrome://extensions` in Chrome.
   * Enable **Developer mode**.
   * Click **Load unpacked** and select the project folder.

## Usage

1. Click the extension icon or press your configured hotkey (e.g., `Alt+j`).
2. Enter a JQL query in the 5-line textarea.
3. Use autocomplete suggestions:

   * Type a prefix (e.g., `pro`) to see suggestions.
   * Navigate with ↑ / ↓ and select with `Tab` or mouse.
4. Press **Enter** or click **OK** to open the query in Jira.
5. Press **Escape** or click **Cancel** to close the popup.

## Configuration

* **Keywords**: Edit `jql_keywords.json` to add or remove JQL fields/operators.
* **Styling**: Modify `popup.css` for custom colors, rounding, etc.
* **Hotkey**: Adjust the `commands` section in `manifest.json` or via `chrome://extensions/shortcuts`.

## Development

The extension is structured as follows:

```bash
jira-jql-autocomplete-extension/
├── manifest.json       # Extension manifest (v3)
├── popup.html          # HTML for the popup UI
├── popup.css           # Stylesheet with customizable theme
├── popup.js            # Main logic: autocomplete & query handling
├── utils.js            # Helper functions for loading keywords and encoding
├── jql_keywords.json   # JSON list of JQL keywords for autocomplete
├── icons/              # Extension icons
└── tests/
    ├── utils.test.js   # Unit tests for util functions
    └── popup.test.js   # (Future) tests for popup logic
```

To run tests (if Node.js is available):

```bash
npm test
# or
node tests/utils.test.js
```

