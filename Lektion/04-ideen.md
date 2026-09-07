# Zwei Ideen für Challenge C – Stand 7. Sep 2026

Gewählte Challenge: **C – Robotaxi / Cabin Comfort**, fokussiert auf den
**reinigbaren Boden**.

## Der gemeinsame Rahmen

**Use Case & Fahrzeugsegment** (von den Regeln ausdrücklich verlangt):
Privat gekauftes Level-4/5-Fahrzeug, C-/D-Segment, Europa/Schweiz, 2035.
Der Halter fährt es ~2 h am Tag selbst und vermietet es die restliche Zeit in eine
Robotaxi-Flotte. Kurzstrecke, städtisch.

**Der Aufhänger:** Die 2×2-Matrix des Dozenten (Private/Shared × Short/Long) hat für
genau diesen Fall **keine Zelle**. „Private" und „Shared" sind dort Alternativen –
ab 2035 sind sie zwei Betriebsmodi *desselben Fahrzeugs*. Das ist die Lücke, in die
wir stossen, und es ist eine Lücke in seiner eigenen Folie.

**Warum ausgerechnet der Boden:**

1. **Niemand schaut mehr hin.** Ohne Fahrer gibt es keine soziale Kontrolle. Wer im
   Robotaxi etwas verschüttet, wird von niemandem gesehen und steigt einfach aus.
2. **10× mehr Schuhe.** Ein Privatwagen sieht 2–4 Personen am Tag, ein geteiltes
   Fahrzeug in der Stadt eher 30–40. Der Boden ist die einzige Fläche, die *jede*
   dieser Personen zwingend berührt.
3. **Der Halter putzt selbst.** Kein Flottendepot, keine Industriewaschanlage –
   die Garage zuhause, ein Handstaubsauger, fünf Minuten. Das ist ein völlig anderes
   Lastenheft als bei einer OEM-eigenen Robotaxi-Flotte.
4. **Dreck kostet den Halter direkt Geld.** Schlechte Bewertung → weniger Fahrten.
   Reinigbarkeit wird damit erstmals zu einer Kenngrösse, für die ein *Privatkunde*
   zu zahlen bereit ist.
5. **Es ist Autoneums Bauteil.** Der Innenraumboden ist Kernportfolio (Relive-1,
   Di-Light, Hybrid-Acoustics PET) – wir erfinden nichts Fachfremdes.

---

## Idee 1 – „Clean Class": Reinigbarkeit als spezifizierbare Kenngrösse

**Kern:** Autoneum besitzt bereits den **Carpet Cleanability Analyzer** – ein
robotergeführter Saugarm mit definiertem Anpressdruck reinigt pro Zyklus drei
verschmutzte Teppichproben; bewertet wird über Rückstand auf der Oberfläche und
Gewichtsdifferenz. Heute ist das ein internes Laborgerät und in der Broschüre ein
Adjektiv („easy to clean").

Der Vorschlag: daraus die **Branchennorm** machen. Ein veröffentlichtes Prüfprotokoll,
eine Klassierung (Clean Class A–D) und eine zweite Kennzahl **„time to reset"** –
wie lange braucht ein Laie, bis die Fläche wieder vermietbar ist.

**Was neu ist:** Der Schmutzkatalog. Der Analyzer prüft heute stark haftende Partikel
wie Sandkörner und Wollfasern. Für geteilte Fahrzeuge braucht es den realen Katalog:
Kaffee, Streusalz-Schneematsch, Sand, Kosmetik, Fettiges aus Take-away, Tierhaare,
Haare. Das ist wenig Aufwand und ergibt eine Datenbasis, die sonst niemand hat.

**Warum das ein Vorsprung ist:** Wer die Messmethode definiert, definiert den
Wettbewerb. Sobald ein OEM „Clean Class A" ins Lastenheft schreibt, ist Autoneum der
Einzige, der zertifizieren kann. Der Prüfstand steht bereits – Konkurrenten bräuchten
Jahre, um eine vergleichbare Datenbasis aufzubauen. Zusätzlich entsteht ein
Erlösstrom neben dem Bauteilgeschäft (Zertifizierung, Lizenz).

**Warum es in eine Blockwoche passt:** Wir können den Prüfstand im Kleinen
nachbauen – Saugdüse an einer Schiene, definierter Anpressdruck, Waage,
Foto-Auswertung vorher/nachher – und auf der Bühne **drei bis vier Bodenproben
live ranken**. Damit erfüllen wir „don't limit yourselves to just Powerpoint
presentations" mit einem Messergebnis statt mit einem Bastelmodell.

**Schwäche, die wir selbst ansprechen sollten:** Eine Norm ohne Produkt ist eine
Folie. Idee 1 trägt nur zusammen mit Idee 2 – sie ist der Massstab, Idee 2 ist das,
was daran gemessen wird.

---

## Idee 2 – „Wipe-Through Floor": den Zielkonflikt Akustik ↔ Reinigbarkeit auflösen

**Der Zielkonflikt:** Ein akustisch wirksamer Boden muss **offen und porös** sein,
damit Schall eindringen und absorbiert werden kann. Ein leicht reinigbarer Boden will
**geschlossen und dicht** sein, damit nichts eindringt. Heute muss man sich
entscheiden: schöner absorbierender Teppich, der Flecken zieht – oder Gummimatte,
die laut ist. In einem BEV-Robotaxi ohne Motorgeräusch fällt das doppelt auf, weil
Roll- und Windgeräusche dann dominieren.

**Die Lösung liegt bei Autoneum schon im Haus – nur aussen am Auto.**
Die **RIMIC**-Hitzeschilde sind geschlossene Aluminiumbleche, die trotzdem
absorbieren: Eine gezielte **Mikroperforation** wandelt Luftschall in Wärme um, und
die Akustikleistung wird schlicht über die Anzahl Öffnungen pro Schild gesteuert.
Kombinierbar mit **Theta-Cell** für 2–6 kHz.

**Übertragung nach innen:** eine geschlossene, hydrophobe, abwischbare Deckschicht
aus Monomaterial-PET mit abgestimmter Mikroperforation, darunter der eigentliche
Absorber aus **Hybrid-Acoustics PET**, darunter eine Drainageebene, damit
Reinigungswasser abläuft statt im Absorber zu stehen. Flüssigkeit perlt ab und wird
weggewischt; Schall geht durch die Perforation hindurch nach unten.

**Der Dual-Use-Griff:** Derselbe Grundboden, zwei Persönlichkeiten. Im *Privatmodus*
klipst der Halter eine hochwertige Di-Light- oder Relive-1-Einlage ein und hat sein
Auto. Im *Taximodus* nimmt er sie heraus, darunter liegt die abwischbare Fläche.
Das löst den eigentlichen psychologischen Konflikt: Der Halter will, dass sich sein
Auto wie *seins* anfühlt, obwohl Fremde darin sitzen.

**Regelkonformität:** „Get inspired by other industries and markets" – wir holen die
Inspiration aus Autoneums eigener Exterieur-Produktlinie in den Innenraum. Das ist
belastbarer als eine fremde Branche, weil Fertigungsverfahren und Kompetenz schon da
sind. Monomaterial-PET bleibt vollständig recycelbar, damit bleibt die Idee auf der
Nachhaltigkeitslinie des ganzen Autoneum-Portfolios.

**Nachweis:** Reinigbarkeit über den Prüfstand aus Idee 1, Absorption über Impedanzrohr
oder Alpha-Kabine. Die beiden Ideen greifen ineinander – das ist ihre Stärke, und man
kann sie auch als *eine* Idee mit zwei Hälften präsentieren, falls das Team das lieber
möchte.

---

## Wenn das Problem steht: Biomimicry andocken

Sobald wir uns auf das Problem geeinigt haben, ist der Bionik-Teil aus der Blockwoche
Bionics direkt anschlussfähig – Selbstreinigung ist eine der am besten belegten
Bionik-Domänen überhaupt.

Sinnvolle Vorbilder, mit ehrlicher Bewertung:

| Vorbild | Prinzip | Taugt es für einen Boden? |
|---|---|---|
| **Lotus** (*Nelumbo*) | superhydrophob, Schmutz wird von abrollenden Tropfen mitgenommen | **Nur bedingt** – der Effekt sitzt auf feinen Wachsstrukturen und geht unter Abrieb kaputt. Auf einer Fläche, auf die man tritt, ist das ehrlich gesagt das falsche Vorbild. Genau deshalb lohnt es sich, es zu erwähnen und zu verwerfen. |
| **Springschwanz** (*Collembola*) | omniphobe Kutikula, weist auch Öle ab; Effekt kommt aus **hinterschnittener Geometrie**, nicht aus einer Beschichtung | **Das passende Vorbild.** Geometrie überlebt Abrieb, eine Wachsschicht nicht. Und Geometrie ist genau das, was Autoneum mit Mikroperforation ohnehin fertigt. |
| **Kannenpflanze** (*Nepenthes*) | flüssigkeitsinfundierte, rutschige Oberfläche (SLIPS), selbstheilend | Interessant für Fett und Öl, aber eine infundierte Flüssigkeit in einem Fahrzeugboden ist regulatorisch heikel. Als Variante prüfen. |
| **Haifischhaut** | Bewuchs wird durch Topografie verhindert, ohne Biozid | Hygiene-Argument ohne Chemie – passt zu „use life-friendly chemistry". |
| **Laubfrosch-Haftscheiben** | Kanäle leiten Wasser weg und erhalten dadurch Grip im Nassen | Direkt relevant: Fahrgäste steigen mit nassen Schuhen ein, Rutschsicherheit ist eine harte Anforderung. Ihr habt dazu schon `Example tree frog.pdf` im Kursmaterial. |

**Die Konvergenz, auf die es ankommt:** Springschwanz und Laubfrosch führen beide auf
*Mikrogeometrie* statt auf *Beschichtung* – abriebfest, chemiefrei, und in derselben
Fertigungslogik wie Autoneums Mikroperforation. Damit sind Idee 2 und der Bionik-Teil
nicht zwei nebeneinanderliegende Kapitel, sondern dieselbe Aussage von zwei Seiten.

**Life's Principles** dann als KPI, nach der Regel aus eurem eigenen Modul:
*leiten, nicht dekorieren; nur relevante wählen; testbar machen.* Kandidaten hier:
„be resource efficient" (Monomaterial, ein Bauteil statt Teppich + Gummimatte),
„use life-friendly chemistry" (Hygiene über Geometrie statt Biozid, ABC statt Latex),
„be locally attuned and responsive" (Privatmodus/Taximodus).

## Nächster Schritt

Beide Ideen morgen ins Team, dann eine wählen oder – empfohlen – als eine Idee mit
Norm-Hälfte und Produkt-Hälfte zusammenziehen. Der Coaching-Slot am Dienstag
13:00–15:00 wäre der richtige Ort, das gegenzuprüfen.
