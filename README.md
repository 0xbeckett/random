# random

A deliberately incoherent, zero-build static site. One `index.html`, no dependencies, no build step.

Every load is different: randomized fonts/colors/sizes/positions, generated nonsense + zalgo text,
drifting/jittering/reshuffling elements, spawning emoji & multi-script glyphs, glitch noise overlay,
and structured + feral sound on interaction. A fever dream, not a usable page.

Live: https://random.0xbeckett.me

## Epilepsy warning gate

The page contains rapid flashing, strobing and high-contrast motion and plays loud, unpredictable
sound. It is a genuine photosensitive-seizure hazard, so it is gated behind a **static, calm,
high-contrast interstitial** — the only honest, motionless element on the page. Nothing runs until
you accept:

- The entire engine lives behind a single `start()`. On load only the gate's static markup is
  painted — the QRNG refill loop, audio unlock, drone, noise canvas, spawners and animation loop
  do **not** run until the visitor clicks *"I understand — enter"*.
- A way out that isn't closing the tab: *"No thanks — take me out"* links away.
- The choice is stored in `localStorage` (`random-accepted`) so returning visitors are not re-gated.
  Re-show it with the corner **⚠ warning** link or by adding `?warn` to the URL.

## Randomness axes

Entropy comes from the ANU quantum RNG (`QRNG`, buffered async refill, graceful fallback to
`Math.random`, live `src:` label). Layered on the original glyph/colour/size/audio dials, this
version adds six new **independent** axes of variation:

1. **Layout regime** — the field periodically swaps between scatter / grid / ring / spiral / orbit /
   columns / stack / diagonal placement systems (not just randomized blobs).
2. **Time regime** — variable global tick rate with freeze-frames, slow-motion, fast-forward and
   stutter (dropped frames); the spawn cadence, sequencer pulse and noise refresh all ride it.
3. **Typography** — random writing systems (kana, CJK, Cyrillic, Greek, Hebrew, runic, braille,
   math, box-drawing, ogham) beyond the Arabic soup, random font *stacks*, random text direction
   (rtl/ltr) and vertical writing modes.
4. **Page-level regime** — randomized favicon (generated emoji), cursor (incl. emoji cursors),
   accent/caret colour and document-background regimes (solid / hue / radial / flicker / strobe /
   gradient), plus the existing title flicker.
5. **Audio structure** — random musical scales, root, tempo and waveform driving a rhythmic
   sequencer with subdivision/augmentation, scale-quantized beeps and biquad filter sweeps, instead
   of pure random beeps.
6. **Rare high-impact events** — low-probability set pieces (full invert, supernova, black-hole
   pull, mega-glyph, mirror flip, mono-scream, text rain, quake) so the page occasionally does
   something a visitor has never seen.

Still a single self-contained `index.html`: vanilla JS, no build step, no dependencies.
