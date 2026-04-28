## How to test a tooltip (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a tooltip

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus visibly moves to the tooltip button, and the tooltip appears.
   * Spacebar: Activates the button (if applicable) or retains the tooltip visibility.
   * Enter: Activates the button (if applicable) or retains the tooltip visibility.

2. Test mobile screenreader gestures

   * Swipe: Focus moves to the tooltip button, tooltip content is announced.
   * Doubletap: Activates the button (if applicable).

3. Listen to screenreader output on all devices

   * Name: The accessible name of the tooltip button is clear.
   * Role: It identifies as a button.
   * Tooltip: The tooltip content is read aloud (via `aria-describedby` or role="tooltip").
   * Action: It is clear whether the button performs an action or is static.

Full information: <https://www.magentaa11y.com/#/web-criteria/component/tooltip>