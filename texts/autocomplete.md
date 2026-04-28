## How to test an autocomplete input with listbox (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test an autocomplete input with listbox

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus moves visibly to the text input
   * Arrow-keys: Focus moves to and selects the next option. If the textbox is empty and the listbox is not displayed, opens the listbox and moves visual focus to the next option. In both cases DOM focus remains on the textbox.
   * Enter: The textbox value is set to the content of the selected option. The listbox closes.
   * Escape: Clears the textbox. If the listbox is displayed, closes it.

2. Test mobile screenreader gestures

   * Swipe: Focus moves to the input, traverses list
   * Doubletap: Opens select, chooses option

3. Listen to screenreader output on all devices

   * Name: Its purpose is clear
   * Role: It identifies itself as a select, popup, menu/submenu, listbox or combobox
   * Group: Its label is read and selected options are read
   * State: It indicates the value of the text input

Full information: [https://www.magentaa11y.com/#/web-criteria/component/autocomplete](/web-criteria/component/autocomplete)