## How to test a text input (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a text input

GIVEN THAT I am on a page with a text input

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to a text input I SEE focus is strongly visually indicated

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use the tab key to move focus to a text input
     * I HEAR its purpose is clear
     * I HEAR it identifies itself as a text input
     * I HEAR hints or errors are read after the label, related inputs include a group name (Ex: Enter your personal information)
     * I HEAR if applicable, it expresses its state (required, disabled / dimmed / unavailable)

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to focus on a text input
     * I HEAR its purpose is clear
     * I HEAR it identifies itself as a text input
     * I HEAR hints or errors are read after the label, related inputs include a group name (Ex: Enter your personal information)
     * I HEAR if applicable, it expresses its state (required, disabled / dimmed / unavailable)

Full information: [https://www.magentaa11y.com/#/web-criteria/component/text-input](/web-criteria/component/text-input)