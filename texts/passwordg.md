## How to test a password input (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a password input

GIVEN THAT I am on a page with a password input

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to the password input I SEE focus is strongly visually indicated
   * THEN when I use the tab key to move focus to the show/hide password feature I SEE its name, role and state
   * THEN when I use the show/hide password feature I SEE the state of the password visibility (with or without characters entered)

2. Desktop screenreader
   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND I use the tab key to move focus to the password input
     * I HEAR its purpose is clear
     * I HEAR it identifies itself as a text input
     * I HEAR hints or errors are read after the label (Ex: Password formatting)
     * I HEAR it expresses if the password is being shown and if applicable: required, disabled / dimmed / unavailable
   * THEN when I use the tab key to move focus to the show/hide password feature I HEAR its name, role and state
   * THEN when I use the show/hide password feature I HEAR the state of the password visibility (with or without characters entered)

3. Mobile screenreader
   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND I swipe to focus on a password input
     * I HEAR its purpose is clear
     * I HEAR it identifies itself as a text input
     * I HEAR hints or errors are read after the label (Ex: Password formatting)
     * I HEAR it expresses if the password is being shown and if applicable: required, disabled / dimmed / unavailable

Full information: [https://www.magentaa11y.com/#/web-criteria/component/password-input](/web-criteria/component/password-input)