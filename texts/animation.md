## How to test an animation (Magenta a11y, condensed)

### #a11y - Web Accessibility Acceptance Criteria

How to test an animation

1. Test keyboard only, then screen reader + keyboard actions

   * Tab: Where applicable, focus moves directly to pause/play/hide controls
   * Spacebar: Activates the control
   * Enter: Activates the control
   * Reduced motion settings: Animation is disabled or reduced

2. Test mobile screenreader gestures

   * Swipe: Focus moves to the control
   * Doubletap: Activates the button

3. Listen to screenreader output on all devices

   * Name: The control's purpose (pause/play/hide) is clear
   * Role: It identifies its role of button
   * State: The control expresses its state if applicable (pressed, expanded)

4. Device OS Settings
   * Reduced motion: Large motion, animations or effects are reduced or eliminated

Full information: [https://www.magentaa11y.com/#/web-criteria/component/animation](/web-criteria/component/animation)