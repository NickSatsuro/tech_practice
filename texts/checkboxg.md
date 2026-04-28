## How to test a checkbox (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a checkbox

GIVEN THAT I am on a page with a checkbox

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to a checkbox I SEE focus is strongly visually indicated
   * THEN when I use the spacebar to activate the checkbox I SEE the state is changed

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use the tab key to move focus to a checkbox
     * I HEAR its label and purpose is clear
     * I HEAR it identifies its role of checkbox
     * I HEAR hints or errors are read after the label and related inputs include a group name (ex: Account settings)
     * I HEAR it expresses its state (checked/unchecked, disabled)
   * THEN when I use the spacebar to activate the checkbox I HEAR the state is changed

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to focus on a checkbox input
     * I HEAR its label and purpose is clear
     * I HEAR it identifies its role of checkbox
     * I HEAR hints or errors are read after the label and related inputs include a group name (ex: Account settings)
     * I HEAR it expresses its state (checked/unchecked, disabled)
   * THEN when I doubletap with the checkbox in focus I HEAR the state is changed

Full information: [https://www.magentaa11y.com/#/web-criteria/component/checkbox](/web-criteria/component/checkbox)