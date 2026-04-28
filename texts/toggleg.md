## How to test a toggle switch (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a toggle switch

GIVEN THAT I am on a page with a toggle switch

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to a switch I SEE focus is strongly visually indicated
   * THEN when I use the spacebar to activate the switch I SEE the state is changed

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use the tab key to move focus to a switch
     * I HEAR its label and purpose is clear
     * I HEAR it identifies its role of switch, toggle button or checkbox
     * I HEAR hints or errors are read after the label and related inputs include a group name (Ex: Account settings)
     * I HEAR it expresses its state (on/off, checked/unchecked, disabled/dimmed)
   * THEN when I use the spacebar to activate the switch I HEAR the state is changed

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to focus on a switch input
     * I HEAR its label and purpose is clear
     * I HEAR it identifies its role of switch, toggle button or checkbox
     * I HEAR Hints or errors are read after the label and related inputs include a group name (Ex: Account settings)
     * I HEAR it expresses its state (on/off, checked/unchecked, disabled/dimmed)
   * THEN when I doubletap with the switch in focus I HEAR the state is changed

Full information: [https://www.magentaa11y.com/#/web-criteria/component/toggle-switch](/web-criteria/component/toggle-switch)