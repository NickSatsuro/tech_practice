## How to test a heading: h1, h2, h3, h4, h5, h6 (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a heading: h1, h2, h3, h4, h5, h6

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Nothing, headings must not be focusable
   * Arrow-keys: Browses headings (when using screen reader)

2. Test mobile screenreader gestures

   * Swipe: The screenreader reads the heading and its level

3. Listen to screenreader output on all devices

   * Name: The heading's purpose and level must be clear
   * Role: It identifies itself as a heading and its level
   * Group: It is logically ordered, starting with a single h1, sections titled by h2, and subsections with h3

Full information: [https://www.magentaa11y.com/#/web-criteria/component/heading](/web-criteria/component/heading)