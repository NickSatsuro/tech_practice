## How to test a tidbit (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a tidbit

1. Test keyboard only, then screen reader + keyboard actions

   * Arrow-keys: The Tidbit scrolls into view.
   * Tab-key: The focusable link (if present) receives keyboard focus - there is a highly visible focus ring.

2. Test mobile screenreader gestures

   * Swipe: The individual contents of the Tidbit are accessed in this order: Icon, heading, paragraph, link.

3. Listen to screenreader output on all devices

   * Name: The screen reader announces the text alternative for the info icon. Such as "Info", "Error", "Caution", or "Success".
   * Description: The screen reader announces the visual label for any nested controls and any additional context (e.g. "Learn more Cats are amazing creatures"). *Note:* Some screen readers require different navigational techniques to get the additional context to announce.
   * Role: It identifies the info icon as an image and the Tidbit heading as a heading.
   * Group: There is no grouping for the Tidbit.

Full information: [https://www.magentaa11y.com/#/web-criteria/component/tidbit](/web-criteria/component/tidbit)