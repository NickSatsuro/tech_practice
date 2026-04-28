## How to test a video/audio player (Magenta a11y, gherkin)

### #a11y - Web Accessibility Acceptance Criteria

How to test a video/audio player

GIVEN THAT I am on a page with a video/audio player

1. Keyboard for mobile & desktop

   * WHEN I use the tab key to move focus to a control I SEE focus is strongly visually indicated
   * THEN when I use the spacebar and/or enter key to activate the button I SEE the intended action occurs
   * THEN when I use the arrow keys (left/right) I SEE the media fast forwards/reverses

2. Desktop screenreader

   * WHEN I use a desktop screenreader (NVDA, JAWS, VoiceOver) AND
   * I use the tab key to move focus to a control
     * I HEAR the video control purpose is clear (play, pause, stop)
     * I HEAR video controls identify as button, switch etc.
     * I HEAR audio content never autoplays
     * I HEAR it expresses it state if applicable (pressed, expanded, disabled)
   * THEN when I use the spacebar and/or enter key to activate the button I HEAR the intended action occurs
   * THEN when I use the arrow keys (left/right) I HEAR the media fast forwards/reverses

3. Mobile screenreader

   * WHEN I use a mobile screenreader (Talkback, VoiceOver) AND

     * I swipe to focusable to a video control

     * I HEAR the video control purpose is clear (play, pause, stop)

     * I HEAR video controls identify as button, switch etc.

     * I HEAR audio content never autoplays

     * I HEAR it expresses it state if applicable (pressed, expanded, disabled)
   * Then when I doubletap with the video control in focus I HEAR the intended action occurs

Full information: [https://www.magentaa11y.com/#/web-criteria/component/video-audio-player](/web-criteria/component/video-audio-player)