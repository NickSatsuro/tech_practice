## How to test an expander accordion (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test an expander accordion

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus visibly moves to the expander
   * Spacebar: Toggles the expander
   * Enter: Toggles the expander

2. Test mobile screenreader gestures

   * Swipe: Focus moves to the element, expresses its state (expanded/collapsed)
   * Doubletap: Toggles the expander

3. Listen to screenreader output on all devices

   * Name: Its purpose is clear
   * Role: It identifies its role of a button or details
   * State: It expresses its state (expanded/collapsed)

Full information: [https://www.magentaa11y.com/#/web-criteria/component/expander-accordion](/web-criteria/component/expander-accordion)