## How to test a button (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a button

GIVEN THAT I am on a page with a button

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to a button I SEE focus is strongly visually indicated
   * THEN when I use the spacebar and/or enter key to activate the button I SEE the intended action occurs

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND I use the tab key to move focus to a button
     * I HEAR Its purpose is clear
     * I HEAR It identifies its role of button
     * I HEAR It indicates if it has popup for listbox or menus
     * I HEAR It expresses its state if applicable (pressed, expanded, disabled/dimmed/unavailable)
   * THEN when I use the spacebar and/or enter key to activate the button I HEAR the intended action occurs

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND I swipe to focus on a button
     * I HEAR Its purpose is clear
     * I HEAR It identifies its role of button
     * I HEAR It indicates if it has popup for listbox or menus
     * I HEAR It expresses its state if applicable (pressed, expanded, disabled/dimmed/unavailable)
   * THEN when I doubletap with the button in focus I HEAR the intended action occurs

Full information: [https://www.magentaa11y.com/#/web-criteria/component/button](/web-criteria/component/button)