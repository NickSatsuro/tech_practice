## How to test a figure: maps, charts, and graphics (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a figure: maps, charts, and graphics

GIVEN THAT I am on a page with a figure: maps, charts, and graphics

1. Keyboard for mobile & desktop

   * WHEN I use the arrow key to browse to a figure I SEE the figure comes into view.
   * THEN when I use the tab key to move focus to figure controls (toggle, show/hide, etc) I SEE the control is in focus
   * THEN when I use the spacebar or enter key I SEE the intended action occurs

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND I use the arrow key to browse to a figure.
     * I HEAR Content is described by a heading, alt text or named on focus
     * I HEAR it identifies as a common HTML element (image, list, table)
     * I HEAR an alternative method of consumption or interaction is available
   * THEN when I use the tab key to move focus to figure controls (toggle, show/hide, etc) I HEAR the control is in focus
   * THEN when I use the spacebar or enter key I HEAR the intended action occurs

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND I swipe to browse to an image
     * I HEAR Content is described by a heading, alt text or named on focus
     * I HEAR it identifies as a common HTML element (image, list, table)
     * I HEAR an alternative method of consumption or interaction is available

Full information: [https://www.magentaa11y.com/#/web-criteria/component/figure](/web-criteria/component/figure)