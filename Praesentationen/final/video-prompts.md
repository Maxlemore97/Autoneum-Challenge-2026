# Videos für die Schlusspräsentation

Regel zuerst: **höchstens zwei Videos** in einem Zehn-Minuten-Pitch, je 3–5 Sekunden,
Kamera statisch, Schleife, das Standbild bleibt als Poster auf der Folie. Ein Video, das
auf dem Hörsaalrechner nicht startet, ist schlimmer als keines.

Reihenfolge nach Nutzen. Jeweils das vorhandene Bild als **Startframe** ins
Image-to-Video-Modell, der Prompt beschreibt nur die Bewegung.

## 1 — Folie 7, das Wärmebild *(das Video, das erklärt)*

Startbild: `assets/07-thermal-camera-view-warm-floor-cabin.jpg`
Speichern als: `assets/07-thermal-warmup.mp4` · dann in `deck.yaml` bei der Folie mit
`id: thermal` die Zeile `video: assets/07-thermal-warmup.mp4` ergänzen.

Das ist die einzige Animation, die etwas zeigt, was ein Standbild nicht kann: **die
Wärme entsteht in der Fläche und bleibt dort — die Luft bleibt kalt.**

```
Start with the whole cabin cold: floor, door panels, seats and air all in the same deep
blue and violet. Over about three seconds the floor and the lower door panels warm up
smoothly from blue through purple and red to bright orange and yellow, the glow
spreading evenly across the whole floor surface at once, not from a single point. The
seat cushions and the passenger's legs pick up a soft red warmth from below. The air,
the glass roof and the ceiling stay cold blue throughout. Then hold the final state.
Locked off camera, no camera movement, no zoom, no cuts, single continuous shot,
false-colour thermal look unchanged, no text, no numbers.
```

Negativ: `no camera movement, no zoom, no cuts, no people entering, no text, no scale
bar, no flicker, the air must not turn warm`

## 2 — Folie 2, die Fahrt *(das Video, das die Stimmung setzt)*

Startbild: `assets/02-premium-driverless-car-winter-lake-road.jpg`
Speichern als: `assets/02-journey.mp4` · `video: assets/02-journey.mp4` bei `id: journey`.

Läuft stumm, während der Kaltstart erzählt wird. Wenig Bewegung, viel Atmosphäre.

```
The car drives slowly along the lakeside road from the left of the frame toward the
right, its warm cabin light steady, headlights on the snow. The lake stays still, a
few snowflakes drift, the dusk light stays constant. The camera is locked off on the
landscape and does not follow the car. Single continuous shot, 4 to 5 seconds, no
cuts, no zoom, no text.
```

Negativ: `no camera movement, no drone orbit, no cuts, no other vehicles, no people,
no headlight flare, no text`

## 3 — Folie 12, die Matte *(nur wenn neu generiert)*

Auf Folie 12 läuft bisher das **alte** Video mit der einfachen Matte im normalen
Fussraum — das passt nicht mehr zum Luxus-Standbild darüber. Zwei Wege:

- **Neu generieren** aus `assets/12-luxury-floor-mat-lifted-from-premium.jpg`,
  speichern als `assets/12-lux-swap.mp4`, und in `deck.yaml` bei `id: lux-swap` die
  `video:`-Zeile darauf umstellen. Prompt:

```
The hand lifts the cream lambswool mat further, peeling it up and away in one smooth
motion until it clears the top of the frame, the mat staying roughly parallel as it
rises, revealing the dark dock plate with its four circular magnet pads and the
central ring. Everything else in the cabin stays perfectly still. Locked off camera,
no camera movement, no zoom, no cuts, single continuous shot, lighting unchanged.
```

- **Oder das Video weglassen** und das Standbild allein stehen lassen — die Dock ist in
  dieser Präsentation Nebensache, das Bild reicht. Dann in `deck.yaml` die
  `video:`-Zeile bei `id: lux-swap` entfernen.

## 4 — Folie 13, die Ankunft *(optional, als Klammer zu Folie 2)*

Startbild: `assets/13-premium-car-arrival-night-lakefront-warm.jpg`
Speichern als: `assets/13-arrival.mp4` · `video: assets/13-arrival.mp4` bei `id: arrival`.

```
The rear door swings open slowly and the warm cream light from the cabin spills out
onto the snow, growing brighter as the door opens. Snow falls gently. The city lights
on the water shimmer slightly. Nothing else moves. Locked off camera, no zoom, no
cuts, single continuous shot, 3 to 4 seconds, no text.
```

## Nicht animieren

- **Folie 1** — das Standbild ist stärker; ein pulsierendes Glühen wirkt billig.
- **Folie 3, 6, 10** — Diagramm, Porträt, Explosionsgrafik: Bewegung lenkt ab, und
  Schichten, die sich zusammensetzen, werden von Videomodellen fast immer verzerrt.

## Empfehlung

**Folie 7 und Folie 2.** Eins erklärt, eins stimmt ein. Folie 12 nur, wenn ihr das Video
ohnehin neu macht; sonst weg damit. Folie 13 ist Kür.
