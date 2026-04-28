## How to test a link (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a link

GIVEN THAT I am on a page with a link

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to a link I SEE focus is strongly visually indicated
   * THEN when I use the enter key to activate the link I SEE my browser goes somewhere

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use the tab key to move focus to a link
     * I HEAR its purpose is clear
     * I HEAR it identifies itself as a link
   * THEN when I use the enter key to activate the link I HEAR my browser goes somewhere

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to focus on a link
     * I HEAR its purpose is clear
     * I HEAR it identifies itself as a link
   * THEN when I doubletap with the link in focus I HEAR my browser goes somewhere

Full information: [https://www.magentaa11y.com/#/web-criteria/component/link](/web-criteria/component/link)