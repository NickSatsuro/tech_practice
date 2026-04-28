## How to test a carousel/slideshow (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a carousel/slideshow

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus moves to carousel controls (forward, backward, pause/play, stop)
   * Spacebar: Activates the button
   * Enter: Activates the button

2. Test mobile screenreader gestures

   * Swipe: Focus moves within the carousel
   * Doubletap: This typically activates most elements

3. Listen to screenreader output on all devices

   * Name: Control name and purpose is clear
   * Role: Control identifies itself as a button
   * Group: The number of slides and current position in the carousel is indicated

4. Device OS settings
   * Reduced motion: Carousel does not auto-advance, motion transitions are disabled
   * Reflow/zoom: At a viewport width equivalent to 320 CSS pixels (for example, 1280 px wide at 400% zoom), content reflows without loss of information or functionality and does not require horizontal scrolling. Controls and slide content remain operable.
   * Horizontal scrolling content: At a height equivalent to 256 CSS pixels, content does not require vertical scrolling.
   * Exception: Two-dimensional scrolling is allowed only for parts of the content that require it for usage or meaning (e.g., complex data visualizations).

Full information: [https://www.magentaa11y.com/#/web-criteria/component/carousel-slideshow](/web-criteria/component/carousel-slideshow)