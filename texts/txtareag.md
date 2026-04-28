## How to test a textarea multiline input (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a textarea multiline input

GIVEN THAT I am on a page with a textarea multiline input

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to a textarea I SEE focus is strongly visually indicated

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND I use the tab key to move focus to a textarea
     * I HEAR Its purpose is clear
     * I HEAR It identifies itself as a textarea
     * I HEAR Hints or errors (ex: chars remaining) are read after the label, related inputs include a group name (ex: Contact us)
     * I HEAR If applicable, it expresses its state (required, disabled / dimmed / unavailable)
     * I HEAR Character counter updates dynamically after keypress and a short delay

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND I swipe to focusable elements on a textarea
     * I HEAR Its purpose is clear
     * I HEAR It identifies itself as a textarea
     * I HEAR Hints or errors (ex: chars remaining) are read after the label, related inputs include a group name (ex: Contact us)
     * I HEAR If applicable, it expresses its state (required, disabled / dimmed / unavailable)
     * I HEAR Character counter updates dynamically after keypress and a short delay

Full information: [https://www.magentaa11y.com/#/web-criteria/component/textarea-multiline-input](/web-criteria/component/textarea-multiline-input)