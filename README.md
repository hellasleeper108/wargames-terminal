```
.------..------..------..------..------..------..------..------.
|W.--. ||A.--. ||R.--. ||G.--. ||A.--. ||M.--. ||E.--. ||S.--. |
| :/\: || (\/) || :(): || :/\: || (\/) || (\/) || (\/) || :/\: |
| :\/: || :\/: || ()() || :\/: || :\/: || :\/: || :\/: || :\/: |
| '--'W|| '--'A|| '--'R|| '--'G|| '--'A|| '--'M|| '--'E|| '--'S|
`------'`------'`------'`------'`------'`------'`------'`------'
```



A faithful terminal simulation of the WOPR computer from
the 1983 film **WarGames** — rendered in your browser with
full CRT aesthetics, variable-speed typewriter text, and
zero dependencies.

────────────────────────────────────────────────────────

   ╔══════════════════════════════════════════╗
   ║   GREETINGS.  PROFESSOR FALKEN.         ║
   ║                                          ║
   ║   "SHALL WE PLAY A GAME?"               ║
   ╚══════════════════════════════════════════╝

────────────────────────────────────────────────────────


THE EXPERIENCE
──────────────

  Phase 1  SYSTEM BOOT
           POST, memory test (640K), disk check, peripheral init

  Phase 2  MODEM DIAL-UP
           ATDT 415-555-2368 — Carrier at 1200 baud
           XMODEM-CRC protocol — Backdoor detection

  Phase 3  LOGIN / FALKEN BACKDOOR
           "LOGON: PLEASE ENTER YOUR PASSWORD"
           Search algorithm auto-types FALKEN
           "GREETINGS. PROFESSOR FALKEN."

  Phase 4  GAME SELECTION
           Full game list from the film
           ▸ Pick any game for a short scene
           ▸ GLOBAL THERMONUCLEAR WAR for the main event

  Phase 5  GLOBAL THERMONUCLEAR WAR
           Satellite infrared detection
           NORAD radar tracking (Thule, Clear, Fylingdales)
           ICBM/SLBM launches — Counterforce protocol
           City-level casualty reports
           1,858,490,000 total casualties

  Phase 6  THE LESSON
           Tic-tac-toe demonstration
           "A STRANGE GAME."
           "THE ONLY WAY TO WIN IS TO NOT PLAY."

  Phase 7  SYSTEM SHUTDOWN
           Countdown — Signal lost — Restart available


CRT AESTHETIC
─────────────

  ∙ Scanlines           repeating 2px gradient overlay
  ∙ Phosphor glow       #33ff33 with multi-layered text-shadow bloom
  ∙ Screen curvature    radial gradient vignette on CRT bezel
  ∙ Subtle flicker      random opacity oscillation at 8s interval
  ∙ Noise overlay       SVG fractal turbulence at 1.5% opacity
  ∙ VT323 font          authentic 1980s terminal typography (Google Fonts)
  ∙ Typewriter text     variable-speed character-by-character output
  ∙ Blinking cursor     800ms step-end CSS animation
  ∙ Power LED           pulsing green indicator on monitor frame


CONTROLS
────────

  Password prompt:    Type anything — any input grants access
  Game selection:     Type the name of a game at the menu
  Main path:          Choose GLOBAL THERMONUCLEAR WAR
  Continue prompts:   Press ENTER when asked
  Restart:            Press ENTER after signal loss

  The menu accepts LIST or ? to re-display available games.
  All other games play a short scene and return you to the menu.


LAUNCH
──────

  Open index.html directly in any modern browser:

      $ open index.html

  Or serve locally:

      $ python3 -m http.server 8080
      └─ http://localhost:8080

  Or use the included server script:

      $ python3 serve.py
      $ ./start.sh


FILES
─────

  index.html     Self-contained simulation (877 lines, single file)
  serve.py       Python HTTP server with retro terminal banner
  start.sh       Convenience launcher (opens browser + starts server)
  README.md      This file


TIPS
────

  · Set your browser to fullscreen (F11) for maximum immersion
  · Dim the lights. Sit close to the screen.
  · Use an old CRT monitor or a portrait-orientation display
    for that tall terminal look
  · Try it with a green-on-black terminal theme for bonus points


CREDITS
───────

  Inspired by the 1983 MGM film "WarGames"
  Directed by John Badham · Written by Lawrence Lasker & Walter F. Parkes

  Built with love for the command line generation.

  "Shall we play a game?"
