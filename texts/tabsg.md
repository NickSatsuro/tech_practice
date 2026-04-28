## How to test tabs (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test tabs

GIVEN THAT I am on a page with tabs

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to a tab I SEE focus is strongly visually indicated on the activated tab

   * IF TAB ACTIVATION IS MANUAL when I use the left/right arrow keys I SEE focus moves to other tabs and I use the spacebar or enter key to activate the tab

   * IF TAB ACTIVATION IS AUTOMATIC when I use the left/right arrow keys I SEE the tab is activated

   * THEN when I use the tab key I SEE focus moves to the activated tab panel

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND

   * I use the tab key to move focus to a tab
     * I HEAR its label and purpose is clear
     * I HEAR it identifies itself as a tab
     * I HEAR it expresses its state (selected/pressed/checked)

   * IF TAB ACTIVATION IS MANUAL when I use the left/right arrow keys I HEAR focus moves to other tabs and I use the spacebar or enter key to activate the tab

   * IF TAB ACTIVATION IS AUTOMATIC when I use the left/right arrow keys I HEAR the tab is activated

   * THEN when I use the tab key I HEAR focus moves to the activated tab panel

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND

   * I swipe to focus on a tab
     * I HEAR its label and purpose is clear
     * I HEAR it identifies itself as a tab
     * I HEAR it expresses its state (selected/pressed/checked)

   * THEN when I doubletap with the tab in focus I HEAR the state is changed

Full information: [https://www.magentaa11y.com/#/web-criteria/component/tabs](/web-criteria/component/tabs)