## How to test a checkbox (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a checkbox

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus visibly moves to the checkbox
   * Spacebar: Toggles the checkbox between states

2. Test mobile screenreader gestures

   * Swipe: Focus moves to the element, expresses its state
   * Doubletap: Checkbox toggles between checked and unchecked states

3. Listen to screenreader output on all devices

   * Name: Its label and purpose is clear
   * Role: It identifies its role of checkbox
   * Group: Hints or errors are read after the label and related inputs include a group name (ex: Account settings)
   * State: It expresses its state (checked/unchecked, disabled)

Full information: [https://www.magentaa11y.com/#/web-criteria/component/checkbox](/web-criteria/component/checkbox)