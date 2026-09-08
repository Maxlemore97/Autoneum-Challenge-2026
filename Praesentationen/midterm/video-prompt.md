# Folie 7 als Video: der Wechsel

**Das Problem mit einem einzigen Clip:** Eine Matte, die herunterklappt und
einrastet, zeigt *Befestigung*. Die Folie behauptet aber *Wechsel* — dreckige
raus, saubere rein. Dafür braucht es zwingend **zwei Matten**, und die kann ein
Image-to-Video-Modell aus einem Standbild nicht erfinden.

Die Lösung sind **zwei kurze Clips, hintereinandergeschnitten**. Der Schnittpunkt
ist der nackte Boden mit seinen Magnetaufnahmen — das ist das Bild, das „Wechsel"
beweist, weil es die leere Schnittstelle zeigt.

```
Clip 1: dreckige Matte raus  →  [nackter Boden mit Pads]  →  Clip 2: saubere rein
```

## Was du dafür brauchst

| | |
|---|---|
| **Standbild A** | dasselbe Bild, aber die Matte **sichtbar verschmutzt** |
| **Standbild B** | das vorhandene saubere Bild, `assets/07-clip-in-floor-mat-lifted-out.png` |

Standbild A **nicht neu aus Text erzeugen** — sonst stimmen Innenraum, Winkel und
Licht nicht mit B überein und der Schnitt fällt auseinander. Stattdessen das
vorhandene Bild als **Image-to-Image**-Vorlage nehmen, mit niedriger Stärke
(ca. 0.3–0.4), damit die Komposition erhalten bleibt:

```
Same shot, same camera, same lighting, same hand position. Only the mat surface is
changed: the mat is visibly dirty, grey road salt residue, fine sand, a dried
brown coffee stain near the centre, flattened worn fibres. The magnet pads stay
clean and metallic. The floor underneath stays as it is.
```

## Clip 1 — die dreckige Matte kommt raus *(der wichtigere)*

Startbild A. Dieser Clip allein trägt die Aussage schon zur Hälfte, weil er auf
dem nackten Boden endet und damit die Schnittstelle zeigt.

```
The hand lifts the dirty mat further, peeling it up and away in one smooth motion
until it clears the top of the frame, leaving the bare vehicle floor with its
circular magnet pads exposed and empty. The mat stays roughly parallel as it
rises. Everything else in the interior stays perfectly still. Locked off camera,
no camera movement, no zoom, no cuts, single continuous shot, lighting unchanged.
```

**Letzter Frame: leerer Boden mit Pads.** Auf diesem Bild wird geschnitten.

## Clip 2 — die saubere Matte kommt rein

Startbild B, das vorhandene Bild.

```
The hand lowers the clean mat into place. The folded flap rotates down about its
diagonal crease, slowly and evenly, until the three magnet pads on its underside
are about one centimetre above the matching pads on the floor. Then it is pulled
down that last centimetre abruptly, much faster than it was moving before, and
stops instantly flat against the floor with no bounce and no wobble. The hand
opens and moves up out of frame. Everything else stays perfectly still. Locked off
camera, no camera movement, no zoom, no cuts, single continuous shot.
```

Die drei Stellen, auf denen der Magnet-Eindruck ruht:

- **„slowly and evenly … then abruptly, much faster than it was moving before"** —
  der Beschleunigungssprung. Videomodelle bewegen von sich aus gleichförmig, und
  eine gleichmässig absinkende Matte sieht aus wie hingelegt.
- **„stops instantly … no bounce and no wobble"** — ein Magnet federt nicht nach.
- **„rotates down about its diagonal crease"** — eine einzige Drehachse. Weiche
  Matten frei verformen zu lassen geht fast immer schief.

## Wenn nur Zeit für einen Clip ist

Dann **Clip 1**, nicht Clip 2. Er endet auf dem leeren Boden mit den
Magnetaufnahmen, und das liest sich als „hier kommt gleich eine andere rein".
Einrasten allein zeigt nur, dass etwas hält.

## Schnitt

- je Clip **2–3 s**, zusammen **4–6 s**
- **harter Schnitt** auf dem leeren Boden, keine Blende
- danach **Standbild von Clip 2 stehen lassen** oder die ganze Sache loopen
- kein Ton, keine Titel im Video — die Folie hat schon einen

## Negativliste

```
no camera movement, no zoom, no orbit, no cuts, no scene change, no extra hands,
no people entering, no text, no logos, no lens flare, no slow motion,
no bouncing, no wobble, no deformation of the mat
```

## In die Präsentation

Ein Video, das auf dem Hörsaalrechner nicht startet, ist schlimmer als keines:

- **MP4 / H.264**, in PowerPoint **eingebettet**, nicht verlinkt
- unter ~20 MB, **Schleife**, **automatisch starten**
- Seitenverhältnis **16:9 wie die Standbilder** — die Folie beschneidet auf fast
  quadratisch
- das **Standbild als Rückfallebene** auf der Folie behalten
- vorher **auf dem Präsentationsrechner** testen

Sag Bescheid, wenn das Video fertig ist — dann baue ich `add_movie` in die Skill
ein und setze es mit dem Standbild als Poster auf Folie 7.
