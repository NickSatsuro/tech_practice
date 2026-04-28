## How to test an informative image (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test an informative image

GIVEN THAT I am on a page with an informative image

1. Keyboard for mobile & desktop

   * WHEN I use the arrow keys to browse to an image I SEE the image comes into view

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND I use the arrow keys to browse to an image
   * * I HEAR the content of the image alt text is clear
     * I HEAR it identifies its role as an image or graphic

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND I swipe to browse to an image
   * * I HEAR the content of the image alt text is clear
     * I HEAR it identifies its role as an image or graphic

Full information: [https://www.magentaa11y.com/#/web-criteria/component/informative-image](/web-criteria/component/informative-image)