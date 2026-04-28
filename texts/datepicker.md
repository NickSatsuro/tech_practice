## How to test a date picker dialog (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a date picker dialog

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus visibly moves to the date grid table and calendar navigation buttons
   * Escape: The dialog closes and focus returns to the launch button
   * Arrow keys: Date selection visibly moves through next/previous days
   * Page up/down: Changes the grid of dates to the previous/next month
   * Shift + page up/down: Changes the grid of dates to the previous/next year
   * Home/end: Moves focus to the first/last day of the current week
   * Spacebar or enter: Activates the date picker buttons and calendar navigation buttons

2. Test mobile screenreader gestures

   * Swipe: Focus moves through elements, expresses its state
   * Doubletap: Activates the element in focus

3. Listen to screenreader output on all devices

   * Name: The purpose of each control is clear
   * Role: Buttons identify as buttons, dialog identifies itself dialog or modal, date grid table may identify itself as table or grid
   * Group: The launch button indicates it has a popup, menu or dialog; days are announced with month and year
   * State: Date options express state (pressed, selected, disabled/dimmed)

Full information: [https://www.magentaa11y.com/#/web-criteria/web/date-picker](/web-criteria/web/date-picker)