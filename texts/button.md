## How to test a button (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a button

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus visibly moves to the button.
   * Spacebar: Activates the button.
   * Enter: Activates the button.

2. Test mobile screenreader gestures

   * Swipe: Focus moves to the element, expresses its state
   * Doubletap: Activates the button

3. Listen to screenreader output on all devices
   * Name: Its purpose is clear
   * Role: It identifies its role of button
   * Group: It indicates if it has popup for listbox or menus
   * State: It expresses its state if applicable (pressed, expanded, disabled/dimmed/unavailable)

Full information: [https://www.magentaa11y.com/#/web-criteria/component/button](/web-criteria/component/button)