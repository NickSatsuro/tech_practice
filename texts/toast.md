## How to test a toast snackbar (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a toast snackbar

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus visibly moves in logical order to buttons or links inside the toast
   * Space: Any buttons inside are activated
   * Enter: Any links or buttons inside are activated

2. Test mobile screenreader gestures

   * Swipe: Focus moves in logical order to the toast
   * Doubletap: This typically activates most elements in the toast

3. Listen to screenreader output on all devices

   * Name: The toast is read when it appears (BUT focus DOES NOT transfer automatically when the toast appears)
   * Role: It identifies itself as an alert or status when it appears
   * Group: If it is possible to close the toast, focus then returns to a logical place in the page
   * State: It remains open until closed by user

Full information: [https://www.magentaa11y.com/#/web-criteria/component/toast-snackbar](/web-criteria/component/toast-snackbar)