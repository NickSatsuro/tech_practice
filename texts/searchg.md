## How to test a search input (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a search input

GIVEN THAT I am on a page with a search input

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to a search input I SEE focus is strongly visually indicated
   * THEN when I use the tab key to move focus to the search submit button I SEE the button is focused
   * THEN when I use the enter or spacebar key I SEE the search results are presented

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use the tab key to move focus to a search input
     * I HEAR its purpose is clear
     * I HEAR it identifies itself as a search input
     * I HEAR the form itself is discoverable with screenreader shortcuts as a search input
   * THEN when I use the tab key to move focus to the search submit button I HEAR the button is focused
   * THEN when I use the enter or spacebar key I HEAR the search results are presented

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND
   * I swipe to focus on a search input
     * I HEAR its purpose is clear
     * I HEAR it identifies itself as a search input
     * I HEAR the form itself is discoverable with screenreader

Full information: [https://www.magentaa11y.com/#/web-criteria/component/search](/web-criteria/component/search)