## How to test a separator / horizontal rule (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a separator / horizontal rule

GIVEN THAT I am on a page with a separator / horizontal rule

1. Keyboard for mobile & desktop

   * WHEN I use arrow keys to browse to the separator I SEE the element is skipped entirely. It is completely inert.

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use arrow keys to browse to the separator
     * I HEAR the element is skipped entirely. It is completely inert.

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to the separator
     * I HEAR the element is skipped entirely. It is completely inert.

Full information: [https://www.magentaa11y.com/#/web-criteria/component/separator-horizontal-rule](/web-criteria/component/separator-horizontal-rule)