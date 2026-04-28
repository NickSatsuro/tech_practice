## How to test a textarea multiline input (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a textarea multiline input

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus moves visibly to the textarea unless it's disabled

2. Test mobile screenreader gestures

   * Swipe: Focus moves to the textarea
   * Keyboard: Keyboard appears

3. Listen to screenreader output on all devices

   * Name: Its purpose is clear
   * Role: It identifies itself as a textarea
   * Group: Hints or errors (ex: chars remaining) are read after the label, related inputs include a group name (ex: Contact us)
   * State: If applicable, it expresses its state (required, disabled / dimmed / unavailable)
   * Status: Character counter updates dynamically after keypress and a short delay

Full information: [https://www.magentaa11y.com/#/web-criteria/component/textarea-multiline-input](/web-criteria/component/textarea-multiline-input)