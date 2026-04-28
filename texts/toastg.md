## How to test a toast snackbar (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a toast snackbar

GIVEN THAT I am on a page with a toast snackbar

1. Keyboard for mobile & desktop

   * WHEN I use features that trigger the toast I SEE the toast (BUT focus DOES NOT transfer automatically when the alert appears)

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use features that trigger the toast
     * I HEAR the toast is read when it appears (BUT focus DOES NOT transfer automatically when the toast appears)
     * I HEAR it identifies itself as an alert or status when it appears
     * I HEAR if it is possible to close the toast, focus then returns to a logical place in the page
     * I HEAR it remains open until closed by user

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I use features that trigger the toast snackbar
     * I HEAR the toast is read when it appears (BUT focus DOES NOT transfer automatically when the toast appears)
     * I HEAR it identifies itself as an alert or status when it appears
     * I HEAR if it is possible to close the toast, focus then returns to a logical place in the page
     * I HEAR it remains open until closed by user

Full information: [https://www.magentaa11y.com/#/web-criteria/component/toast-snackbar](/web-criteria/component/toast-snackbar)