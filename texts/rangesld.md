## How to test a range slider input (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a range slider input

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus moves visibly to the input
   * Arrow-keys: Increase / decrease value one step

2. Test mobile screenreader gestures

   * Swipe: Focus moves to the input
   * Swipe up/down: Increase/decrease slider value one step on iOS
   * Volume: Increase/decrease slider value one step on Android

3. Listen to screenreader output on all devices

   * Name: Its purpose is clear
   * Role: It identifies itself as a range
   * Group: Its label is read with the input
   * State: Its current value

Full information: [https://www.magentaa11y.com/#/web-criteria/component/range-slider](/web-criteria/component/range-slider)