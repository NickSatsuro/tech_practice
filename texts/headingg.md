## How to test a heading: h1, h2, h3, h4, h5, h6 (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a heading: h1, h2, h3, h4, h5, h6

GIVEN THAT I am on a page with a heading

1. Keyboard for mobile & desktop

   * WHEN I use the arrow key to browse to a heading I SEE the heading comes into view
   * WHEN I use the tab key I SEE nothing happens to the heading because headings must NOT be focusable

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use the arrow key to browse to a heading
     * I HEAR the heading's purpose and level must be clear
     * I HEAR it identifies itself as a heading and its level
     * I HEAR it is logically ordered, starting with a single h1, sections titled by h2, and subsections with h3
   * WHEN when I use the tab key I HEAR nothing happens to the heading because headings must NOT be focusable

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to browse to a heading
     * I HEAR the heading's purpose and level must be clear
     * I HEAR it identifies itself as a heading and its level
     * I HEAR it is logically ordered, starting with a single h1, sections titled by h2, and subsections with h3

Full information: [https://www.magentaa11y.com/#/web-criteria/component/heading](/web-criteria/component/heading)