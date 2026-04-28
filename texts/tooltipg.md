## How to test a tooltip (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a tooltip

GIVEN THAT I am on a page with a tooltip button

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to a tooltip button
     * I SEE focus is strongly visually indicated\
       AND I SEE a tooltip appears after a short delay
   * THEN when I use the spacebar and/or enter key to activate the button\
     I SEE the intended action occurs OR the tooltip remains visible without triggering an action

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver)\
     AND I use the tab key to move focus to a tooltip button
     * I HEAR the accessible name of the button
     * I HEAR the tooltip content (if implemented using `aria-describedby` or role="tooltip")
     * I HEAR whether the button is actionable or static
   * THEN when I use the spacebar and/or enter key to activate the tooltip button\
     I HEAR the intended action occurs (if applicable)

3. Mobile screenreader

   * WHEN I use a mobile screenreader (TalkBack, VoiceOver)\
     AND I swipe to focus on a tooltip button
     * I HEAR the accessible name of the button
     * I HEAR the tooltip content (if implemented using `aria-describedby` or role="tooltip")
     * I HEAR whether the button is actionable or static
   * THEN when I doubletap with the tooltip button in focus\
     I HEAR the intended action occurs (if applicable)

Full information: <https://www.magentaa11y.com/#/web-criteria/component/tooltip>