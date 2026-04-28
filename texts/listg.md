## How to test a list (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a list

GIVEN THAT I am on a page with a list

1. Keyboard for mobile & desktop

   * WHEN I use the arrow key to browse to a list I SEE the list comes into view
   * WHEN I use the tab key I SEE nothing happens to the list itself because lists must NOT be focusable

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use the arrow key to browse to a list
     * I HEAR it identifies itself as a list
     * I HEAR it declares the number of items in the list
   * WHEN I use the tab key I HEAR nothing happens to the list itself because lists must NOT be focusable

3. Mobile screenreader

   * WHEN I have mobile screenreader verbosity settings enabled to Speak text formatting and list position AND
   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to browse a list
     * I HEAR it identifies itself as a list
     * I HEAR it declares the number of items in the list

Full information: [https://www.magentaa11y.com/#/web-criteria/component/list](/web-criteria/component/list)