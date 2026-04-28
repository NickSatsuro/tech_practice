## How to test a stepper input (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a stepper input

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus moves to either the select field or buttons.
   * Enter or spacebar:
     * If select is focused, expands the select and places focus on the currently selected option in the list.
     * If focus is in the options, collapses the select and keeps the currently selected option.
     * If focus is on one of the buttons, it will either increment or decrement the value.
   * Arrow-keys: If select is focused, moves focus to and selects the next option.
   * Escape: If the select is displayed, collapses the select and moves focus to the button.
   * Home: If the select is displayed, moves focus to and selects the first option.
   * End: If the select is displayed, moves focus to and selects the last option.

2. Test mobile screenreader gestures

   * Swipe: Moves focus to each form control in the pattern.
   * Double-tap: If select is focused, opens select, selects option. Note: If a button is focused, it will either increment or decrement the value.

3. Listen to screenreader output on all devices

   * Name: Button labels are clear and include context. The select field's visual label is announced.
   * Role: For the select field it identifies itself as a select, popup button, menu/submenu or listbox. For the buttons they are identified as button.
   * Group: Its label is read with the input.
   * State: It indicates when the select is expanded/collapsed, indicates which option is selected.

Full information: [https://www.magentaa11y.com/#/web-criteria/component/stepper-input](/web-criteria/component/stepper-input)