## How to test a video/audio player (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test a video/audio player

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Focus visibly moves to each control
   * Spacebar: Activates the control button
   * Enter: Activates the control button
   * Arrow-keys: Fast forward/reverse media

2. Test mobile screenreader gestures

   * Swipe: Focus visibly moves to each control
   * Doubletap: Activates the control

3. Listen to screenreader output on all devices

   * Name: The video control purpose is clear (play, pause, stop)
   * Role: Video controls identify as button, switch etc.
   * Group: Audio content never autoplays
   * State: It expresses it state if applicable (pressed, expanded, disabled)

Full information: [https://www.magentaa11y.com/#/web-criteria/component/video-audio-player](/web-criteria/component/video-audio-player)