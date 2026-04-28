## How to test an alert notification (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test an alert notification

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus does not automatically move to the alert, but can move to interactive elements within the alert (example: Dismiss button)
   * Arrow: Browses to the alert like any other content

2. Test mobile screenreader gestures

   * Swipe: Focus does not move to the alert when it appears, but it can be browsed by the screenreader

3. Listen to screenreader output on all devices

   * Name: The alert is read when it appears (BUT focus DOES NOT transfer automatically when the alert appears)
   * Role: It identifies itself as an alert

Full information: [https://www.magentaa11y.com/#/web-criteria/component/alert-notification](/web-criteria/component/alert-notification)