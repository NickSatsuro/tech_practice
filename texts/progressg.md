## How to test a progress indicator (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a progress indicator

GIVEN THAT I am on a page with a progress indicator

1. Keyboard for mobile & desktop

   * WHEN I use the arrow key to browse to a progress bar I SEE the progress bar comes into view

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use the arrow key to browse to a progress bar
     * I HEAR the progress indicator purpose is clear
     * I HEAR it identifies itself as some kind of progress indicator
     * I HEAR it expresses its current value if it dynamically changes

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to browse to a progress bar
     * I HEAR the progress indicator purpose is clear
     * I HEAR it identifies itself as some kind of progress indicator
     * I HEAR it expresses its current value if it dynamically changes

Full information: [https://www.magentaa11y.com/#/web-criteria/component/progress-indicator](/web-criteria/component/progress-indicator)