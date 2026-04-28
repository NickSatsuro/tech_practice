## How to test a star rating input (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a star rating input

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus visibly moves to the checked radio button in the group. If a radio button is not checked, focus moves to the first radio button in the group.
   * Spacebar: If the radio button with focus is not checked, changes the state to checked.  Otherwise, does nothing.
   * Arrow-keys: Moves focus to and checks the previous or next radio button in the group

2. Test mobile screenreader gestures

   * Swipe: Focus moves to the element, expresses its state
   * Doubletap: If the radio button with focus is not checked, changes the state to checked. Otherwise, does nothing.

3. Listen to screenreader output on all devices

   * Name: Its label and purpose is clear
   * Role: It identifies itself as a radio option
   * Group: Each option has an associated label and the radio group name
   * State: It expresses its state (selected, checked, disabled)

Full information: [https://www.magentaa11y.com/#/web-criteria/component/star-rating](/web-criteria/component/star-rating)