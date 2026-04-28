## How to test a password input (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a password input

1. Test keyboard only, then screen reader + keyboard actions
   * Tab: Focus moves visibly to the input or show password checkbox
   * Spacebar: Toggles the show password checkbox

2. Test mobile screenreader gestures
   * Swipe: Focus moves to the input
   * Keyboard: Keyboard appears

3. Listen to screenreader output on all devices
   * Name: Its purpose is clear
   * Role: It identifies itself as a text input
   * Group: Hints or errors are read after the label (Ex: Password formatting)
   * State: It expresses if the password is being shown and if applicable: required, disabled / dimmed / unavailable

Full information: [https://www.magentaa11y.com/#/web-criteria/component/password-input](/web-criteria/component/password-input)