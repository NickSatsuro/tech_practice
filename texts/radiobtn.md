## How to test a radio button (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a radio button

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus visibly moves to the checked radio button in the group. If a radio button is not checked, focus moves to the first radio button in the group.

   * Spacebar: If the radio button with focus is not checked, changes the state to checked.  Otherwise, does nothing.

   * Arrow-keys: Moves focus to and checks the previous or next radio button in the group

2. Test mobile screenreader gestures

   * Swipe: Focus moves to the element, expresses its state

   * Doubletap: If the radio button with focus is not checked, changes the state to checked. Otherwise, does nothing.

3. Listen to screenreader output on all devices

   * Name: Its label and purpose is clear

   * Role: It identifies itself as a radio option

   * Group: Hints or errors are read after the label and related inputs include a group name (ex: Shipping options)

   * State: It expresses its state (selected, checked, disabled)

Full information: [https://www.magentaa11y.com/#/web-criteria/form/radio-button](/web-criteria/form/radio-button)