## How to test a hint, help, or error (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a hint, help, or error

GIVEN THAT I am on a page with a hint, help, or error

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to an input I SEE hint, help, or error text meets size and contrast requirements

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use the tab key to move focus to an input
     * I HEAR after the input name, the role and state is read, THEN the hint, help, or error is read
     * I HEAR when it appears dynamically, an error is read automatically

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to focus on an input
     * I HEAR after the input name, the role and state is read, THEN the hint, help, or error is read
     * I HEAR when it appears dynamically, an error is read automatically

Full information: [https://www.magentaa11y.com/#/web-criteria/component/help-hint-error](/web-criteria/component/help-hint-error)