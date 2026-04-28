## How to test a scrolling container (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a scrolling container

GIVEN THAT I am on a page with a scrolling container

1. Keyboard for mobile & desktop
   * WHEN I use the tab key to move focus to the container I SEE focus is strongly visually indicated
   * THEN when I use the up/down arrow keys I SEE the content is browsed up/down

2. Desktop screenreader
   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND I use the tab key to move focus to the container
     * I HEAR its purpose is clear
     * I HEAR it identifies its role as region
   * THEN when I use the up/down arrow keys I HEAR the content is browsed up/down

3. Mobile screenreader
   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND I swipe move browse to the container
     * I HEAR its purpose is clear
     * I HEAR it identifies its role as region
   * THEN when I swipe move browse to the content I HEAR the content is read

Full information: [https://www.magentaa11y.com/#/web-criteria/scrolling](/web-criteria/scrolling)