## How to test tabs (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test tabs

1. Test keyboard only, then screen reader + keyboard actions

   * Tab key: Focus visibly moves to the active tab and then the open tab panel

   * Left/right-arrow-keys (automatic activation): Moves focus to the next or previous tab and activates the tab

   * Left/right-arrow-keys (manual activation): Moves focus to the next or previous tab

   * Spacebar or enter (manual activation): Activates the focused tab

2. Test mobile screenreader gestures

   * Swipe: Focus moves to the tabs and then the open tab panel

   * Doubletap: Activates the tab

3. Listen to screenreader output on all devices

   * Name: Its label and purpose is clear

   * Role: It identifies itself as a tab

   * State: It expresses its state (selected/pressed/checked)

Full information: [https://www.magentaa11y.com/#/web-criteria/component/tabs](/web-criteria/component/tabs)