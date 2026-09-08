# Warme Flächen statt warmer Luft — Idee für Challenge C

Stand 8. Sep 2026.

**Teamentscheid:** Challenge **C – Robotaxi / Cabin Comfort**.

**Challenge A wurde bewusst verworfen**, weil die Aufgabe an ihrer eigenen
Prämisse scheitert: Sie fragt nach Komfort für den „driver" eines autonomen
Lastwagens — eine Person, die es 2035 voraussichtlich nicht mehr gibt.
Begründung im Abschnitt „Warum eher nicht im Lastwagen".

## Der Rahmen

**Use Case & Fahrzeugsegment** (von den Regeln ausdrücklich verlangt):
Level-4-BEV im C-/D-Segment, Europa/Schweiz, 2035, Kurzstrecke und städtisch —
in **zwei Betreibermodellen**:

- **Halterbetrieb:** Der Besitzer fährt ~2 h am Tag selbst und vermietet das
  Fahrzeug die restliche Zeit in eine Robotaxi-Flotte.
- **Flottenbetrieb:** Ein Betreiber lässt dasselbe Fahrzeug 16 h am Tag laufen.

Beide landen bei derselben Kabine, aber mit unterschiedlichem Druck. **Die Flotte
ist für einen Zulieferer der relevantere Kunde**, weil dort die Stückzahlen und
das Lastenheft entstehen. **Der Halter stellt die härtere Anforderung**, weil er
kein Depot hat.

**Der Aufhänger:** Die 2×2-Matrix des Dozenten (Private/Shared × Short/Long) hat für
genau diesen Fall **keine Zelle**. „Private" und „Shared" sind dort Alternativen –
ab 2035 sind sie zwei Betriebsmodi *desselben Fahrzeugs*. Das ist die Lücke, in die
wir stossen, und es ist eine Lücke in seiner eigenen Folie.

**Warum Boden und untere Seitenwände:**

1. **Sie sind die einzigen Flächen, die immer neben jedem sind.** Ohne Fahrer gibt
   es keine feste Sitzordnung mehr. Ein Lüftungsauslass im Armaturenbrett zielt
   2035 ins Leere; Boden und Seitenwand nicht.
2. **Wärme über die Fläche ist um Grössenordnungen billiger** als Wärme über die
   Luft — und im Robotaxi ist Energie bares Geld. Das ist der Kern der Idee.
3. **Niemand schaut mehr hin.** Ohne Fahrer gibt es keine soziale Kontrolle. Wer
   im Robotaxi etwas verschüttet, wird von niemandem gesehen und steigt aus.
4. **10× mehr Schuhe.** Ein Privatwagen sieht 2–4 Personen am Tag, ein geteiltes
   Fahrzeug in der Stadt eher 30–40. Der Boden ist die Fläche, die *jede* dieser
   Personen zwingend berührt.
5. **Reinigung kostet beide, auf verschiedene Weise.** Der Halter hat gar kein
   Depot — Garage, Handstaubsauger, fünf Minuten. Die Flotte hat ein Depot, aber
   jede Minute Reinigung ist eine Minute ohne Umsatz. Beide brauchen dieselbe
   Eigenschaft: die Fläche muss schnell wieder einsatzbereit sein.
6. **Es ist Autoneums Bauteil.** Innenraumboden und Seitenverkleidung sind
   Kernportfolio — wir erfinden nichts Fachfremdes.

---

## Die Idee: Heizung statt Klimaanlage

**Die Grundentscheidung, aus der alles folgt:** Im Robotaxi von 2035 heizt man
nicht mehr die Luft, sondern die Flächen, die der Fahrgast berührt und anschaut.
Boden und untere Seitenwände werden zu beheizten, abwischbaren,
**herausnehmbaren Paneelen**. Der Boden hört auf, ein Teppich zu sein.

### Warum Heizen im Robotaxi das teuerste Problem ist

**Die Tür geht ständig auf.** Ein Stadtrobotaxi macht 30–40 Halte am Tag. Jeder
Halt wirft das aufgeheizte Luftvolumen hinaus, und die Konvektionsheizung fängt
von vorn an. Eine warme Fläche kühlt in dreissig Sekunden offener Tür nicht aus.
Diesen Betriebsfall gibt es im Privatwagen nicht.

**Heizen ist im BEV der grösste Kältefresser.** Widerstandsheizung zieht
**3–5 kW dauerhaft**; im Winter verlieren Elektrofahrzeuge **20–40 % Reichweite**,
im städtischen Stop-and-go bei −18 °C bis zu **50 %**. Für ein Robotaxi ist
Reichweite nicht Komfort, sondern das Geschäftsmodell.

**Strahlungsheizung kostet einen Bruchteil.** Flächen-/Infrarotheizung liefert
Komfort bei **rund 200 W** gegenüber **etwa 4,5 kW** konvektiv. Lokale Heizung
senkte in einer Messung die Batterieleistung bei 0 °C von **2,3 kW auf etwa
0,9 kW**; Studien nennen **45–50 %** Einsparung an HVAC-Energie.

**Und der Mensch merkt es nicht.** Mit *einer* Strahlungsquelle empfinden Insassen
die Kabine schon bei **rund 3 °C unter** Solltemperatur als neutral, mit **zwei**
Quellen bei etwa **6 °C darunter**. Boden *und* Seitenwand sind zwei Quellen.

**Ohne Fahrer stimmt die HVAC-Geometrie nicht mehr.** Klimatisierung ist heute um
Armaturenbrett und Fahrerposition gebaut. In einer Lounge- oder
Gegenüber-Bestuhlung gibt es keine definierte Blickrichtung mehr — Boden und
Seitenwände sind aber **immer** neben jedem, egal wie die Sitze stehen. Die
Flächenheizung ist das layoutunabhängige Heizprinzip.

### Dieselbe Fläche muss abwischbar sein — ohne die Akustik zu töten

Eine beheizte Fläche im geteilten Fahrzeug, die man nicht putzen kann, ist
wertlos — deshalb hängt an der Heizidee zwingend ein zweiter Zielkonflikt.

Ein akustisch wirksamer Boden muss **offen und porös** sein, damit Schall
eindringen und absorbiert werden kann. Ein leicht reinigbarer Boden will
**geschlossen und dicht** sein, damit nichts eindringt. Heute muss man wählen:
schöner absorbierender Teppich, der Flecken zieht — oder Gummimatte, die laut ist.
Im BEV-Robotaxi fällt das doppelt auf, weil ohne Motorgeräusch Roll- und
Windgeräusche dominieren.

**Autoneum hat den Konflikt bereits dreimal angefasst — nur nie am Pkw-Boden.**

*Erstens, dasselbe Bauteil im falschen Fahrzeug:* **Washable surface flooring**
steht auf Folie 7 als erster Punkt unter *Interior floor* beim **Nutzfahrzeug**.
Beim Pkw gibt es das nicht. Das Produkt kam mit **Borgers Automotive** ins Haus
(1. April 2023, EUR 117 Mio.) und ist seither im Lkw-Portfolio geblieben.
Autoneums Nutzfahrzeug-Seite führt **„outstanding cleanability"** als erstes
Argument — bei den Pkw-Böden steht es nicht an dieser Stelle.

*Zweitens, der bereits gelöste Zielkonflikt:* **Alpha-Liner**, der textile
Radhaus-Aussenliner, trägt eine **dünne Beschichtung**, bei der „the porosity of
the textile material is **tuned to maximize the sound absorption**" — und
zugleich ist „the plasticized surface **also easier to clean**". Beschichtet,
akustisch abgestimmt und reinigbar in einem Bauteil. Die Beschichtung wird nur
dort aufgetragen, wo sie wirkt, damit der Verschnitt recycelbar bleibt.

*Drittens, dasselbe Prinzip in Metall:* Die **RIMIC**-Hitzeschilde sind
geschlossene Aluminiumbleche, die trotzdem absorbieren — eine gezielte
**Mikroperforation** wandelt Luftschall in Wärme um, gesteuert über die Anzahl
Öffnungen. Kombinierbar mit **Theta-Cell** für 2–6 kHz.

### Der Aufbau

| Schicht | Funktion | Herkunft im Haus |
|---|---|---|
| Abwischbare Deckschicht, hydrophob, Monomaterial-PET, mit abgestimmter Mikroperforation | Flüssigkeit perlt ab und wird weggewischt, Schall geht hindurch | Alpha-Liner, RIMIC, Washable surface flooring |
| Absorber | die eigentliche Akustik | Hybrid-Acoustics PET |
| Heizebene | Strahlungswärme statt Luftheizung | „(Heated) Floor mats", Nutzfahrzeug |
| Drainage | Reinigungswasser läuft ab statt im Absorber zu stehen | neu |
| Magnethalterung mit kontaktloser Speisung | herausnehmbar, kein sichtbares Kabel | Unterhaltungselektronik |

### Die Befestigung: MagSafe und Switch 2

Das Paneel muss heraus — zum gründlichen Reinigen, zum Tauschen bei Verschleiss,
zum Warten der Heizung. Zwei Vorbilder aus einer anderen Branche, was die Regeln
ausdrücklich einladen:

- **Nintendo Switch 2** für die Mechanik: Magnete halten *und* zentrieren, ein
  Entriegelungsknopf verhindert versehentliches Lösen, und dieselbe Bewegung
  stellt die mechanische *und* die elektrische Verbindung her.
- **MagSafe** für die Energie: Leistung geht **kontaktlos durch eine geschlossene
  Oberfläche**.

**Das ist keine Spielerei, sondern der technische Kern.** Man kann keinen
waschbaren Boden und offenliegende Steckkontakte gleichzeitig haben — Streusalz
und Schneematsch fressen jeden Stecker. **Kontaktlose Energieübertragung ist das,
was „beheizt" und „abwaschbar" überhaupt erst vereinbar macht.** Sie erfüllt
nebenbei wörtlich die Bedingung „there should be no visible cable" aus einer
Challenge, die wir gar nicht bearbeiten.

### Eine Halterung, zwei Geschäftsmodelle

Dieselbe Magnethalterung beantwortet zwei völlig verschiedene Probleme — und das
ist der Grund, warum sich das Bauteil an beide Kundengruppen verkaufen lässt.

**Halterbetrieb — zwei Häute, ein Handgriff.** Der Konflikt des Halters ist
psychologisch: Er will, dass sich sein Auto wie *seins* anfühlt, obwohl Fremde
darin sitzen. Im Privatmodus klipst eine hochwertige Di-Light- oder
Relive-1-Einlage auf; im Taximodus kommt sie ab und darunter liegt die beheizte,
abwischbare Fläche.

**Flottenbetrieb — tauschen statt schrubben.** Der Konflikt der Flotte ist
arithmetisch: Reinigung ist Stillstand, und Stillstand ist entgangener Umsatz. Im
Depot wird das ganze Paneel gezogen, ein sauberes eingesetzt, das Fahrzeug fährt
weiter. Geputzt wird abseits der Einsatzzeit. Genau dafür ist eine kontaktlose,
werkzeuglose Halterung gebaut.

Und weil die Deckhaut einzeln tauschbar ist, wird bei Verschleiss nicht der ganze
Boden entsorgt — die Kreislaufantwort auf Autoneums eigenen Sustainability-Trend.

### Warum eher nicht im Lastwagen

Challenge A fragt nach der beheizten Matte für den „driver" — in
Anführungszeichen, was der Fragesteller selbst schon andeutet. Fährt der Lkw 2035
autonom, sitzt dort niemand mehr, dessen Füsse warm werden müssen.

**Und es geht um viel mehr als die Matte.** Verschwindet der Fahrer, verschwindet
der Grund für die *ganze bewohnte Kabine*. Autoneums Lkw-Innenraumportfolio —
Headliners, Side and rear panels, Upper storage, **Bunk bed support**, Floor mats,
Carpet systems — existiert ausschliesslich, weil dort ein Mensch sitzt, isst und
schläft. Ein fahrerloser Lkw braucht keine Schlafkabine, sondern ein
Sensorgehäuse. Das ist zugleich die ehrlichste Antwort auf Challenge B's
„trends that kill the need for Autoneum products".

*Der Einwand, der kommen wird, und die Antwort darauf:* „Schlafkabinen und
begleitete Fahrten gibt es doch noch." Stimmt — Europa ist beim fahrerlosen Lkw
deutlich langsamer als die USA. Nur ist das ein **schrumpfender** Markt mit
sinkendem Innovationsbedarf, während die Robotaxi-Kabine ein wachsender ist. Wer
als Zulieferer Entwicklungsbudget verteilt, steckt es nicht in das Segment, dem
der Nutzer abhandenkommt.

### Die Pointe für die Story

Autoneum besitzt **jede einzelne Zutat**: den waschbaren Boden (Lkw), die
akustisch abgestimmte Beschichtung (Alpha-Liner), die Heizebene (Lkw), die
Absorber, und die Messtechnik. **Keine davon wurde je mit einer anderen
kombiniert, und keine ist je im Pkw gelandet.** Das ist keine Erfindung, sondern
eine Zusammenführung — und genau das macht sie für einen Zulieferer glaubwürdig
umsetzbar.

### Nachweis und offene Punkte

**Nachweisbar:** Heizleistung, Aufheizzeit und Flächentemperatur über eine
Thermografie-Aufnahme — das ist der Nachweis, der auf die Bühne gehört.
Dazu Absorption über Impedanzrohr oder Alpha-Kabine und Reinigbarkeit über
Autoneums Carpet Cleanability Analyzer. Alles drei in einer Blockwoche
demonstrierbar, und keines davon ist ein Bastelmodell.

**Offen und ehrlich zu benennen:**

- **Wirkungsgrad der kontaktlosen Übertragung.** Induktiv gehen typisch 10–20 %
  verloren. Bei 200 W verschmerzbar, aber es gehört gerechnet — sonst frisst die
  Kopplung den Vorteil an.
- **Sicherheit.** Heisse Fläche plus barfüssige oder schlafende Fahrgäste plus
  Kinder: Temperaturbegrenzung und Fehlerabschaltung sind Pflicht.
- **Magnete** gegen Medizintechnik und gegen die Batterie-Elektromagnetik-
  abschirmung, die Autoneum selbst herstellt.
- **Gewicht.** Heizebene plus Magnete gegen den Leichtbauanspruch aufwiegen.
- **Drainage im Fahrzeug.** Wohin das Wasser läuft, ist im Pkw ungelöst — im Lkw
  gibt es dafür Vorbilder.

**Quellen zu den Zahlen:** DOE und AAA zur Winterreichweite; ScienceDirect,
*Design and development of electric radiant heaters for local heating inside the
cabin of electric vehicles* (2024); ScienceDirect, *Optimizing thermal comfort in
highly automated vehicles: an AI-based HVAC management approach with radiant
panels for winter conditions* (2026); ThermoAnalytics zu Strahlungsheizung und
Reichweite; Autoneum Produktbroschüre 2021 zu Alpha-Liner, RIMIC und dem
Carpet Cleanability Analyzer.

---

## Ausblick, klein am Rande: Reinigbarkeit als spezifizierbare Kenngrösse

*Nicht Teil des Pitches, aber der naheliegende nächste Schritt, falls jemand
nachfragt, wie man die Reinigbarkeit eigentlich beweist.*

Autoneum hat die Messung bereits: Der **Carpet Cleanability Analyzer** steht in
der Produktbroschüre unter *Measurement Systems*, wird mit standardisierten
Schmutzpartikeln ausgeliefert und gibt einen **Cleanability Index** und einen
**Dirt Repellency Index** aus — heute intern in der Vorentwicklung.

Denkbar wäre, den Index zu einer veröffentlichten, vom OEM spezifizierbaren
Klasse zu machen (Clean Class A–D) und den Schmutzkatalog von Sand und Wollfasern
auf die geteilte Nutzung umzustellen: Kaffee, Streusalz-Schneematsch, Kosmetik,
Take-away-Fett, Tierhaare. Wer die Messmethode definiert, definiert den
Wettbewerb — und Autoneum verkauft Messsysteme ohnehin schon als Produkt.

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
Fertigungslogik wie Autoneums Mikroperforation. Damit sind die Deckschicht des
Paneels und der Bionik-Teil nicht zwei nebeneinanderliegende Kapitel, sondern
dieselbe Aussage von zwei Seiten.

**Life's Principles** dann als KPI, nach der Regel aus eurem eigenen Modul:
*leiten, nicht dekorieren; nur relevante wählen; testbar machen.* Kandidaten hier:
„be resource efficient" (Monomaterial, ein Bauteil statt Teppich + Gummimatte),
„use life-friendly chemistry" (Hygiene über Geometrie statt Biozid, ABC statt Latex),
„be locally attuned and responsive" (Privatmodus/Taximodus).

## Nächster Schritt

Eine Idee, ein Bauteil: **Heizung statt Klimaanlage, in einer Fläche, die man
herausnehmen und abwischen kann.** In dieser Reihenfolge präsentieren — erst was
Heizen im Robotaxi kostet, dann die warme Fläche, dann warum sie zwingend
abwischbar und herausnehmbar sein muss.

Die Zwischenpräsentation ist Mittwoch 09:00 und wird zu 50 % auf die Idee und zu
30 % auf die Recherche bewertet. Beides ist damit belegt.
