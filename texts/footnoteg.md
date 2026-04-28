## How to test a footnote (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a footnote

GIVEN THAT I am on a page with a footnote

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to a footnote link I SEE focus is strongly visually indicated
   * THEN when I use the enter key to activate the link I SEE my focus moves directly to the targeted footnote

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use the tab key to move focus to a footnote link
     * I HEAR it describes its purpose
     * I HEAR it identifies itself as a link
   * THEN when I use the enter key to activate the link I HEAR my focus moves directly to the targeted footnote

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to focus on a footnote link
     * I HEAR it describes its purpose
     * I HEAR it identifies itself as a link
   * THEN when I doubletap with the link in focus I HEAR my focus moves directly to the targeted footnote

Full information: [https://www.magentaa11y.com/#/web-criteria/component/footnote](/web-criteria/component/footnote)