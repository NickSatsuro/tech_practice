## How to test a carousel/slideshow (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a carousel/slideshow

GIVEN THAT I am on a page with a carousel/slideshow

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to carousel controls (forward, backward, pause/play, stop) I SEE focus is strongly visually indicated
     * THEN when I use the spacebar or enter key I SEE the intended action occurs

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND I use the tab key to move focus to carousel controls (forward, backward, pause/play, stop)
     * I HEAR Control name and purpose is clear
     * I HEAR Control identifies itself as a button
     * I HEAR The number of slides and current position in the carousel is indicated
     * THEN when I use the spacebar or enter key I HEAR the intended action occurs

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND I swipe to move focus to carousel controls (forward, backward, pause/play, stop)
     * I HEAR Control name and purpose is clear
     * I HEAR Control identifies itself as a button
     * I HEAR The number of slides and current position in the carousel is indicated
     * THEN when I doubletap I HEAR the intended action occurs

4. Device OS settings

   * WHEN I use reduced motion THEN I see Carousel does not auto-advance, motion transitions are disabled
   * WHEN I zoom to 400% (or set the viewport to a width equivalent to 320 CSS pixels) THEN I SEE the carousel content and controls reflow without loss of information or functionality and I do not need to scroll in two dimensions
   * AND WHEN content scrolls horizontally, THEN at a height equivalent to 256 CSS pixels I do not need to scroll vertically
   * EXCEPT FOR parts of the content that require two-dimensional layout for usage or meaning

Full information: [https://www.magentaa11y.com/#/web-criteria/component/carousel-slideshow](/web-criteria/component/carousel-slideshow)