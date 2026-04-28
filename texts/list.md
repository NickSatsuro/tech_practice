## How to test a list (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a list

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Nothing, list items must not be focusable
   * Arrow-keys: Browses list items (when using screen reader)

2. Test mobile screenreader gestures

Mobile Screen Reader Setup:

* Android: Settings > Accessibility > TalkBack > Settings > Verbosity > Speak text formatting (enable)
* iOS: Settings > VoiceOver > Verbosity > List Position > Speak (enable)

Test:

* Swipe: The screenreader reads the list content

3. Listen to screenreader output on all devices

   * Role: It identifies itself as a list
   * Group: It declares the number of items in the list

Full information: [https://www.magentaa11y.com/#/web-criteria/component/list](/web-criteria/component/list)