## How to test a tidbit (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a tidbit

GIVEN THAT I am on a page with a tidbit

1. Keyboard for mobile & desktop

   * WHEN I use the arrow keys I SEE the Tidbit scrolls into view
   * WHEN when I use the tab key I SEE the focusable link (if present) receives keyboard focus - there is a highly visible focus ring

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use the arrow keys
     * I HEAR the screen reader announces the text alternative for the info icon, such as "Info", "Error", "Caution", or "Success"
     * I HEAR the screen reader announces the visual label for any nested controls and any additional context (e.g. "Learn more Cats are amazing creatures"). *Note:* Some screen readers require different navigational techniques to get the additional context to announce
     * I HEAR it identifies the info icon as an image and the Tidbit heading as a heading
     * I HEAR there is no grouping for the Tidbit
   * WHEN when I use the tab key I HEAR the focusable link (if present) receives keyboard focus - there is a highly visible focus ring

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to contents of the Tidbit are accessed in this order: Icon, heading, paragraph, link
     * I HEAR the screen reader announces the text alternative for the info icon, such as "Info", "Error", "Caution", or "Success"
     * I HEAR the screen reader announces the visual label for any nested controls and any additional context (e.g. "Learn more Cats are amazing creatures"). *Note:* Some screen readers require different navigational techniques to get the additional context to announce
     * I HEAR it identifies the info icon as an image and the Tidbit heading as a heading
     * I HEAR there is no grouping for the Tidbit

Full information: [https://www.magentaa11y.com/#/web-criteria/component/tidbit](/web-criteria/component/tidbit)