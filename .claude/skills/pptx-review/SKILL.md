---
name: pptx-review
description: Review a PowerPoint deck against the TAF / Autoneum Challenge criteria — Autoneum's rules of the game as hard gates, then the marked criteria (midterm: Idee 50, Recherche 30, Foliendesign 20; final: Story 50, Foliendesign 30, Auftritt 20) — and return a weighted grade with a fix list ranked by how much it moves the mark. Runs a mechanical audit first (word budget, typefaces, colours, type size, picture coverage, title consistency, notes, timing, sources) and renders the slides so the design is actually looked at. Use when the user asks to check, review, grade, audit or sanity-check a deck or presentation, asks whether it is ready to present, what is missing, what grade it would get, or how to improve it ("prüfe die Präsentation", "ist das abgabebereit", "welche Note", "review my slides", "was fehlt noch").
---

# Deck review — gates, grade, fix list

Three passes, in this order. Do not skip the second: a deck reviewed from its
text alone is a deck nobody looked at, and *Foliendesign* is 30 % of the final.

## Which rubric

Ask, or infer from the date and the deck. Midterm and final are marked on
**different criteria** — see `references/rubric.md`. Getting this wrong makes
the whole review misleading.

```bash
python3 .claude/skills/pptx-review/scripts/audit_pptx.py deck.pptx \
        --mode final --limit-seconds 600
```

`--mode midterm|final`, `--limit-seconds` from the slot, `--json` for the raw
record. The script checks only what a machine can check honestly; the
judgement stays with you.

## Pass 1 — the gates

From the script's `rules` block. Each of Autoneum's rules of the game is
pass/fail: English, use case *and* vehicle segment named, 2035 framing, sources
listed, supplier rather than carmaker perspective.

A failed gate is not a deducted point, it is off-brief. Report these first and
separately, before any score.

The regex checks are indicators, not proof. When the script says a gate passed,
confirm it actually holds in context — "OEM" appearing once does not mean the
deck argues from a supplier's position.

## Pass 2 — look at the slides

```bash
python3 ~/.claude/skills/pptx-deck/scripts/preview.py deck.pptx --contact
```

Then **read `preview/contact-sheet.png`**. Judge what no script can: whether the
slides look like one deck, whether anything is ugly, cramped or unbalanced,
whether the pictures earn their place or are decorative stock, whether a chart
makes its claim or merely displays data.

If the renderer reports overflow, that is real — text is leaving its box.

## Pass 3 — the story

The script prints **the titles in order**. Read only that list. If it does not
tell the argument on its own, *Story* cannot score well no matter what the
slides look like, and this is the single highest-value finding you can return
for the final presentation.

Then check the notes against the slides: if a note repeats its slide, the
presenter will read aloud from the screen — the failure mode the lecture names
explicitly.

Also judge, per rubric:

- **Idee** (midterm, 50 %) — is it next-step innovation, or either obvious or
  science fiction? Is it a *supplier's* idea?
- **Recherche** (midterm, 30 %) — are the claims sourced, are the numbers real,
  is the portfolio understood?
- **Auftritt** (final, 20 %) — cannot be seen in a file. Judge its
  preconditions: notes good enough to speak from, timing that fits the slot,
  speakers assigned, and whether anything exists beyond the slides.

## Output

1. **Gates** — pass/fail, failures first
2. **Score** — each criterion 1–6 in tenths with one sentence of justification,
   then the weighted total
3. **Fix list** — ranked by grade impact, each with the slide number and what
   specifically to change. Not "improve the story": "slides 4–6 are three
   parallel facts with no turn between them; make 5 the objection and 6 the
   answer"
4. **What is already good** — briefly, and only what genuinely is

Be the external examiner. An inflated score is a failure of this skill: it tells
the user they are ready when they are not, two days before a presentation worth
70 % of the module.

## Fixing

If the deck was built by the `pptx-deck` skill, fix the **spec**, not the
.pptx — rebuilding overwrites the file. If it came from PowerPoint, hand back
findings; do not rewrite someone else's deck without being asked.
