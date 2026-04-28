## How to test a toggle switch (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a toggle switch

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus visibly moves to the switch
   * Spacebar: Toggles the switch between states

2. Test mobile screenreader gestures

   * Swipe: Focus moves to the element, expresses its state
   * Doubletap: Element toggles between states

3. Listen to screenreader output on all devices

   * Name: Its label and purpose is clear
   * Role: It identifies its role of switch, toggle button or checkbox
   * Group: Hints or errors are read after the label and related inputs include a group name (Ex: Account settings)
   * State: It expresses its state (on/off, checked/unchecked, disabled/dimmed)

Full information: [https://www.magentaa11y.com/#/web-criteria/component/toggle-switch](/web-criteria/component/toggle-switch)