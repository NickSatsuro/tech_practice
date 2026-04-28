## How to test an autocomplete input with listbox (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test an autocomplete input with listbox

GIVEN THAT I am on a page with an autocomplete input with listbox

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to the text input I SEE focus is strongly visually indicated
   * THEN when I use the arrow keys to select an option I SEE the selected option is the new text input value
   * THEN when I use the enter key I SEE the selected option is changed and focus returns to the text input
   * THEN when I use the escape key when the select is open I SEE it collapses and focus moves to the text input

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND I use the tab key to move focus to the text input
     * I HEAR its purpose is clear
     * I HEAR it identifies itself as a select, popup, menu/submenu, listbox or combobox
     * I HEAR its label is read and selected options are read
     * I HEAR it indicates the value of the text input
   * THEN when I use the arrow keys to select an option I HEAR the selected option is the new text input value
   * THEN when I use the enter key I HEAR the selected option is changed and focus returns to the text input
   * THEN when I use the escape key when the select is open I HEAR it collapses and focus moves to the text input

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND I swipe to focus on a select
     * I HEAR its purpose is clear
     * I HEAR it identifies itself as a select, popup, menu/submenu, listbox or combobox
     * I HEAR its label is read and selected options are read
     * I HEAR it indicates the value of the text input
   * THEN when I doubletap with the select in focus I HEAR the selected option is changed

Full information: [https://www.magentaa11y.com/#/web-criteria/component/autocomplete](/web-criteria/component/autocomplete)