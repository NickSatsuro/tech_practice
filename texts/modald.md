## How to test a modal dialog (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a modal dialog

1. Test keyboard only, then screen reader + keyboard actions

   * Launch button: Focus visibly moves to the open dialog itself.
   * Arrow keys: Content within the dialog is browsed in logical order.
   * Tab: Focus visibly moves to interactive controls in the dialog, starting with the first interactive control (typically close button).
   * Escape: The dialog closes and returns focus to the button that launched it.
   * Space: Any buttons are activated.
   * Enter: Any buttons or links are activated.

2. Test mobile screenreader gestures

   * Swipe: Focus moves within the dialog and doesn't enter the rest of the page.
   * Doubletap: This typically activates most elements.

3. Listen to screenreader output on all devices

   * Name: The dialog describes its purpose or title on launch.
   * Role: It identifies itself as a modal or dialog.
   * Group: When closed, focus returns to the launch button.
   * State: When open, content behind the modal remains inert.

Full information: [https://www.magentaa11y.com/#/web-criteria/component/modal-dialog](/web-criteria/component/modal-dialog)