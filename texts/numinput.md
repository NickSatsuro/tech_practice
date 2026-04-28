## How to test a number input (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a number input

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus moves visibly to the input
   * Number keys: Numbers are entered
   * Non-number keys: Nothing is entered

2. Test mobile screenreader gestures

   * Swipe: Focus moves to the input, numeric keypad is revealed

3. Listen to screenreader output on all devices

   * Name: Its purpose is clear
   * Role: It identifies itself as an editable input
   * Group: Hints or errors are read after the label, related inputs include a group name (Ex: Enter your personal information)
   * State: If applicable, it expresses its state (required, disabled / dimmed / unavailable)

Full information: [https://www.magentaa11y.com/#/web-criteria/component/number-input](/web-criteria/component/number-input)