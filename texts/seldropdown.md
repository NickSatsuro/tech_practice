## How to test a select dropdown (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a select dropdown

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus moves visibly to the input

   * Arrow-keys: Moves focus to and chooses the next option.

   * Escape: If the select options are displayed, collapses the select and moves focus to the select.

2. Test mobile screenreader gestures

   * Swipe: Focus moves to the input, traverses list

   * Double-tap: Opens select, chooses option

3. Listen to screenreader output on all devices

   * Name: Its purpose is clear

   * Role: It identifies itself as a select, popup, menu/submenu, listbox or combobox

   * Group: Hints or errors are read after the label and related inputs include a group name (ex: Account settings)

   * State: It indicates which option is selected and if disabled/dimmed/unavailable

Full information: [https://www.magentaa11y.com/#/web-criteria/component/select-dropdown](/web-criteria/component/select-dropdown)