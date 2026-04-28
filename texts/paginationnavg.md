## How to test a pagination nav (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a pagination nav

GIVEN THAT I am on a page with a pagination nav

1. Keyboard for mobile & desktop

   * WHEN I use the arrow keys to browse to a pagination navigation I SEE the nav comes into view
   * THEN when I use the tab key to move focus to a link in the nav and use the enter key I SEE my browser goes to the intended location

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use the arrow keys to browse to a pagination navigation
     * I HEAR The pagination nav has a logical name ("pagination")
     * I HEAR The nav landmark is discoverable with screenreader shortcuts
   * THEN when I use the tab key to move focus to a link in the nav and use the enter key I HEAR my browser goes to the intended location

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to elements in the nav
     * I HEAR The pagination nav has a logical name ("pagination")
     * I HEAR The nav landmark is discoverable with screenreader shortcuts
   * THEN when I doubletap with the link in focus I HEAR my browser goes to the intended location

Full information: [https://www.magentaa11y.com/#/web-criteria/component/pagination-nav](/web-criteria/component/pagination-nav)