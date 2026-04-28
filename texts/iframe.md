## How to test an iframe (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test an iframe

1. Test keyboard only, then screen reader + keyboard actions

   * Arrow keys: Content within the iframe is browsed
   * Tab: Interactive content in the iframe comes into view

2. Test mobile screenreader gestures

   * Swipe: Content within the iframe is browsed

3. Listen to screenreader output on all devices

   * Name: The title of the iframe is read if the iframe contains content
   * Group: If the iframe does not contain content, the iframe is ignored

Full information: [https://www.magentaa11y.com/#/web-criteria/component/iframe](/web-criteria/component/iframe)