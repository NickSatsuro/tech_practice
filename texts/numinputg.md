## How to test a number input (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a number input

GIVEN THAT I am on a page with a number input field

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to a number input I SEE focus is strongly visually indicated
   * THEN when I use the number keys I SEE numbers are entered
   * THEN when I use non-number keys I SEE nothing is entered

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver)
     * AND I use the tab key to move focus to a number input
     * I HEAR its purpose is clear
     * I HEAR it identifies itself as an editable input
     * I HEAR hints or errors are read after the label, related inputs include a group name (Ex: Enter your personal information)
     * I HEAR if applicable, it expresses its state (required, disabled / dimmed / unavailable)
   * THEN when I use the number keys I HEAR numbers are entered
   * THEN when I use non-number keys I HEAR nothing is entered

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver)
     * AND I swipe to focus on a number input
     * I HEAR its purpose is clear
     * I HEAR it identifies itself as an editable input
     * I HEAR hints or errors are read after the label, related inputs include a group name (Ex: Enter your personal information)
     * I HEAR if applicable, it expresses its state (required, disabled / dimmed / unavailable)
   * THEN when I enter a number I HEAR the numeric keypad is revealed

Full information: [https://www.magentaa11y.com/#/web-criteria/component/number-input](/web-criteria/component/number-input)