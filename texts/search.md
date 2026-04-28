## How to test a search input (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a search input

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus moves visibly to the search text input and search button
   * Space: Search button is activated
   * Enter: Search is activated

2. Test mobile screenreader gestures
   * Swipe: Focus moves to the search text input and search button
   * Doubletap: Search button is activated

3. Listen to screenreader output on all devices

   * Name: Its purpose is clear
   * Role: It identifies itself as a search input
   * Group: The form itself is discoverable with screenreader shortcuts as a search input

Full information: [https://www.magentaa11y.com/#/web-criteria/component/search](/web-criteria/component/search)