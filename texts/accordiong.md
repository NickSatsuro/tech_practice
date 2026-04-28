## How to test an expander accordion (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test an expander accordion

GIVEN THAT I am on a page with an expander accordion

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to an expander I SEE focus is strongly visually indicated
   * THEN when I use the spacebar and/or enter key to activate the expander I SEE the hidden content is revealed

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use the tab key to move focus to an expander
     * I HEAR its purpose is clear
     * I HEAR it identifies its role of a button or details
     * I HEAR it expresses its state (expanded/collapsed)
   * THEN when I use the spacebar and/or enter key to activate the expander I HEAR the hidden content is revealed

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to focus on a button
     * I HEAR its purpose is clear
     * I HEAR it identifies its role of a button or details
     * I HEAR it expresses its state (expanded/collapsed)
   * THEN when I doubletap with the button in focus I HEAR the intended action occurs

Full information: [https://www.magentaa11y.com/#/web-criteria/component/expander-accordion](/web-criteria/component/expander-accordion)