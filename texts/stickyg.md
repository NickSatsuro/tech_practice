## How to test a sticky element (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a sticky element

GIVEN THAT I am on a page with a sticky element

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to interactive elements inside the sticky element I SEE focus is visually indicated in a logical order in relation to the whole page

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND

   * I use the tab key to move focus to interactive elements inside the sticky element
     * I HEAR interactive elements are read in logical order in relation to the whole page

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND

   * I swipe to the sticky element
     * I HEAR Interactive elements are read in logical order in relation to the whole page

Full information: [https://www.magentaa11y.com/#/web-criteria/component/sticky-element](/web-criteria/component/sticky-element)

<!-- ## Developer Notes

### Name

- Typically doesn’t have a name or description since there must be only one instance per page. -->