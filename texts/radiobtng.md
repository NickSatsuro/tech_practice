## How to test a radio button (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a radio button

GIVEN THAT I am on a page with a radio button

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to a radio group I SEE focus is strongly visually indicated on the first unselected option or the selected option

   * THEN when I use the spacebar to activate the radio button I SEE the radio button with focus change state to selected.

   * THEN when I use the arrow keys to focus radio button I SEE the state is changed

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND

   * I use the tab key to move focus to a radio group
     * I HEAR its label and purpose is clear
     * I HEAR it identifies itself as a radio option
     * I HEAR hints or errors are read after the label and related inputs include a group name (ex: Shipping options)
     * I HEAR it expresses its state (selected, checked, disabled)

   * THEN when I use the spacebar to activate the radio button I HEAR the radio button with focus change state to selected.

   * THEN when I use the arrow keys to focus radio button I HEAR the state is changed

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND

   * I swipe to focus on a radio button
     * I HEAR its label and purpose is clear
     * I HEAR it identifies itself as a radio option
     * I HEAR hints or errors are read after the label and related inputs include a group name (ex: Shipping options)
     * I HEAR it expresses its state (selected, checked, disabled)

   * THEN when I doubletap with the radio in focus I HEAR the state is changed

Full information: [https://www.magentaa11y.com/#/web-criteria/form/radio-button](/web-criteria/form/radio-button)