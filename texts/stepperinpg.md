## How to test a stepper input (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a stepper input

GIVEN THAT I am on a page with a stepper input

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to the first interactive item I SEE focus is strongly visually indicated
   * THEN when I use the arrow keys to select an option I SEE the selected option is changed
   * THEN when I use the escape key when the select is open I SEE it collapses and focus moves to the select
   * WHEN when I use the enter key is pressed on buttons I SEE the value is incremented or decremented

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND I use the tab key to move focus to the first interactive item AND
     * I HEAR button labels are clear and include contextThe select field's visual label is announced
     * I HEAR for the select field it identifies itself as a select, popup button, menu/submenu or listboxFor the buttons they are identified as button
     * I HEAR its label is read with the input
     * I HEAR it indicates when the select is expanded/collapsed, indicates which option is selected
   * THEN when I use the arrow keys to select an option, I HEAR the selected option is changed
   * THEN when I use the escape key when the select is open, I HEAR it collapses and focus moves to the select
   * WHEN when I use the enter key is pressed on buttons I HEAR the value is incremented or decremented

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to focus on the form fields
     * I HEAR button labels are clear and include contextThe select field's visual label is announced
     * I HEAR for the select field it identifies itself as a select, popup button, menu/submenu or listboxFor the buttons they are identified as button
     * I HEAR its label is read with the input
     * I HEAR it indicates when the select is expanded/collapsed, indicates which option is selected
   * THEN when I doubletap with the select in focus I HEAR the picker/spinner opens
   * THEN when I doubletap with the button in focus I HEAR the value is incremented or decremented

Full information: [https://www.magentaa11y.com/#/web-criteria/component/stepper-input](/web-criteria/component/stepper-input)