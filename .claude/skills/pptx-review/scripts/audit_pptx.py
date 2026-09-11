#!/usr/bin/env python3
"""Mechanical audit of a .pptx against the TAF / Autoneum Challenge criteria.

Checks only what a machine can check honestly. Story quality, idea strength and
research depth are judgements and stay with the reviewer — this script hands
them the evidence.

Usage:
  audit_pptx.py deck.pptx [--mode midterm|final] [--limit-seconds 600] [--json]
"""
from __future__ import annotations
import argparse, json, re, statistics as st, sys
from collections import Counter
from pathlib import Path

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

EN = set("the a an of and or for in on to with is are be this that we our you "
         "how what why not from as at by it its their there".split())
DE = set("der die das und oder für in auf zu mit ist sind sein diese dieser wir "
         "unser sie wie was warum nicht von als bei durch es ihre dort".split())

GATES = {
    "english":  (r"\b(the|and|of|we|is|are)\b", "Presentations must be in English"),
    "use_case": (r"\buse[- ]?case\b|\bapplication\b|\bszenario\b",
                 "State clearly the use case"),
    "segment":  (r"\bsegment\b|\bB-segment\b|\bC-segment\b|\bD-segment\b|"
                 r"\blight vehicle\b|\bcommercial vehicle\b|\brobotaxi\b|\btruck\b|"
                 r"\bvan\b|\bSUV\b", "State clearly the vehicle segment"),
    "year2035": (r"\b203[0-9]\b", "Put yourself in 2035"),
    "sources":  (r"\bsources?\b|\bquellen?\b|https?://|\b(19|20)\d{2}\b",
                 "List your sources when available"),
    "supplier": (r"\bsupplier\b|\btier[- ]?1\b|\bOEM\b|\bAutoneum\b",
                 "Put yourselves in the shoes of a supplier"),
}


def shape_text(sh):
    if sh.has_text_frame:
        return sh.text_frame.text or ""
    if sh.has_table:
        return " ".join(c.text for r in sh.table.rows for c in r.cells)
    return ""


def collect(prs):
    slides = []
    for i, s in enumerate(prs.slides, 1):
        texts, fonts, sizes, colors = [], set(), [], set()
        pics, pic_area, bullets = 0, 0, 0
        title, title_box = None, None
        cands = []
        has_source = False
        foot_y = prs.slide_height - 685800          # bottom 0.75"
        for sh in s.shapes:
            if sh.shape_type in (MSO_SHAPE_TYPE.PICTURE, MSO_SHAPE_TYPE.MEDIA):
                pics += 1                   # a video with its poster is a visual too
                pic_area += (sh.width or 0) * (sh.height or 0)
                continue
            t = shape_text(sh)
            if not t.strip():
                continue
            if (sh.name or "").lower() == "source" or t.strip().startswith("Source:"):
                has_source = True
                continue                    # a footnote is not slide content
            if (sh.name or "").lower() == "footer" or \
               (sh.top is not None and sh.top >= foot_y):
                continue                    # page numbers are not content
            texts.append(t)
            if sh.has_text_frame:
                paras = [p for p in sh.text_frame.paragraphs if p.text.strip()]
                bullets += max(0, len(paras) - 1) if len(paras) > 1 else 0
                for p in paras:
                    for r in p.runs:
                        if r.font.name:
                            fonts.add(r.font.name)
                        if r.font.size:
                            sizes.append(r.font.size.pt)
                        try:
                            if r.font.color and r.font.color.type == 1:
                                colors.add(str(r.font.color.rgb))
                        except Exception:
                            pass
                big = max((r.font.size.pt for p in paras for r in p.runs
                           if r.font.size), default=0)
                real = [p for p in paras if len(p.text.strip()) >= 3]
                lead = max(real, key=lambda p: max(
                    (r.font.size.pt for r in p.runs if r.font.size), default=0),
                    default=None)
                cands.append({"text": (lead.text if lead else
                                       paras[0].text).strip(), "size": big,
                              "named": (sh.name or "").lower() == "title",
                              "band": sh.top is not None and sh.top < 2011680,
                              "left": sh.left, "top": sh.top})
        pool = ([c for c in cands if c["named"]]
                or [c for c in cands if c["band"]] or cands)
        best = max(pool, key=lambda c: c["size"], default=None)
        if best:
            title = (best["text"], best["size"])
            title_box = (best["left"], best["top"])
        body = " ".join(texts)
        notes = ""
        if s.has_notes_slide:
            notes = s.notes_slide.notes_text_frame.text or ""
        slides.append({
            "n": i, "text": body, "words": len(re.findall(r"\S+", body)),
            "title": title[0] if title else "", "title_size": title[1] if title else 0,
            "title_left": title_box[0] if title_box else None,
            "title_top": title_box[1] if title_box else None,
            "pictures": pics,
            "pic_cover": round(pic_area / (prs.slide_width * prs.slide_height), 3),
            "bullets": bullets, "fonts": sorted(fonts), "colors": sorted(colors),
            "min_size": min(sizes) if sizes else None,
            "notes": notes, "note_words": len(re.findall(r"\S+", notes)),
            "has_source": has_source,
        })
    return slides


def check(name, ok, detail, weight="", severity="FAIL"):
    return {"check": name, "status": "PASS" if ok else severity,
            "detail": detail, "area": weight}


def audit(path, mode, limit):
    prs = Presentation(str(path))
    S = collect(prs)
    n = len(S)
    alltext = " ".join(s["text"] + " " + s["notes"] for s in S)
    low = alltext.lower()
    # the rules of the game are about what the audience SEES, so the gates look
    # at slide text only - a year that lives in the notes was never presented
    visible = " ".join(s["text"] for s in S).lower()
    body = [s for s in S if s["n"] not in (1, n)]      # skip title/closing
    out = []

    # ---- hard gates from Autoneum's "Rules of the game"
    toks = re.findall(r"[a-zA-ZäöüßÄÖÜ]+", visible)
    en = sum(t in EN for t in toks)
    de = sum(t in DE for t in toks)
    out.append(check("Language is English", en >= de,
                     f"English markers {en}, German markers {de}", "rules"))
    for key, (pat, label) in GATES.items():
        if key == "english":
            continue
        hit = re.search(pat, visible, re.I)
        out.append(check(label, bool(hit),
                         f"matched '{hit.group(0)}'" if hit else "no match found",
                         "rules"))

    # ---- Foliendesign
    words = [s["words"] for s in body] or [0]
    worst = max(S, key=lambda s: s["words"])
    out.append(check("Word budget per slide (max 40)", max(words) <= 40,
                     f"max {max(words)} on slide {worst['n']}, mean "
                     f"{round(st.mean(words),1)}", "design",
                     "WARN" if max(words) <= 55 else "FAIL"))
    fonts = sorted({f for s in S for f in s["fonts"]})
    out.append(check("At most 2 typefaces", len(fonts) <= 2,
                     f"{len(fonts)}: {', '.join(fonts) or 'theme default'}",
                     "design", "WARN"))
    colors = sorted({c for s in S for c in s["colors"]})
    out.append(check("At most 4 text colours", len(colors) <= 4,
                     f"{len(colors)}: {', '.join(colors)}", "design", "WARN"))
    mins = [s["min_size"] for s in S if s["min_size"]]
    floor = min(mins) if mins else None
    tiny = [s["n"] for s in S if s["min_size"] and s["min_size"] < 12]
    out.append(check("Smallest text at least 12 pt", not tiny,
                     f"smallest is {floor} pt"
                     + (f"; under 12 pt on slides {tiny}" if tiny else ""),
                     "design"))
    smallish = [s["n"] for s in S if s["min_size"] and 12 <= s["min_size"] < 14]
    if smallish:
        out.append(check("Body text comfortably readable (14 pt+)", False,
                         f"12–13 pt on slides {smallish} — fine for captions, "
                         f"too small for body copy", "design", "WARN"))
    visual = [s for s in body if s["pictures"] > 0]
    ratio = len(visual) / max(len(body), 1)
    out.append(check("Bild vor Text — ≥50 % of content slides carry a visual",
                     ratio >= 0.5, f"{len(visual)}/{len(body)} "
                     f"({round(ratio*100)} %)", "design", "WARN"))
    fat = [s["n"] for s in S if s["bullets"] > 6]
    out.append(check("No slide over 6 bullets", not fat,
                     f"slides {fat}" if fat else "ok", "design", "WARN"))
    tops = [s["title_top"] for s in body if s["title_top"] is not None]
    if len(tops) > 2:
        modal = Counter(round(v / 45720) for v in tops).most_common(1)[0][0]
        off = [s["n"] for s in body if s["title_top"] is not None
               and abs(round(s["title_top"] / 45720) - modal) > 3]
        out.append(check("Titles sit in the same place",
                         len(off) <= max(1, 0.3 * len(tops)),
                         f"{len(tops)-len(off)}/{len(tops)} on the common "
                         f"baseline" + (f"; off: slides {off}" if off else ""),
                         "design", "WARN"))

    # ---- Story
    absent = [s["n"] for s in S if s["note_words"] == 0]
    thin = [s["n"] for s in S if 0 < s["note_words"] < 12]
    out.append(check("Every slide has speaker notes", not absent,
                     f"absent on slides {absent}" if absent else "ok", "story"))
    out.append(check("Notes carry enough to speak from", not thin,
                     f"under 12 words on slides {thin}" if thin else "ok",
                     "story", "WARN"))
    labels = [s["n"] for s in body
              if s["title"] and len(s["title"].split()) < 4]
    out.append(check("Action titles, not labels", not labels,
                     f"short titles on slides {labels}" if labels else "ok",
                     "story", "WARN"))
    spoken = sum(s["note_words"] for s in S)
    secs = round(spoken / 130 * 60)
    ok_t = (abs(secs - limit) <= limit * 0.2) if limit else True
    out.append(check("Speaking time fits the slot",
                     ok_t, f"~{secs//60}:{secs%60:02d} from {spoken} words of "
                     f"notes" + (f" (limit {limit//60} min)" if limit else ""),
                     "story", "WARN"))

    # ---- Recherche
    nums = len(re.findall(
        r"\d[\d'’.,]*\s?(?:%|°C|kW|W\b|kWh|kg|km|m\b|mm|CHF|EUR|dB|"
        r"s\b|min\b|h\b|watts?\b|percent\b)", alltext, re.I))
    out.append(check("Quantified evidence present", nums >= 5,
                     f"{nums} figures with units", "research", "WARN"))
    urls = len(re.findall(r"https?://", alltext))
    out.append(check("Sources cited on the slides", urls >= 1 or
                     bool(re.search(r"\bsources?\b|\bquellen?\b", low)),
                     f"{urls} URL(s), source list "
                     f"{'present' if re.search(r'sources?|quellen?', low) else 'absent'}",
                     "research", "WARN"))

    num_slides = [s["n"] for s in S
                  if re.search(r"\d[\d'’.,]*\s?(%|°C|kW|W\b|min\b|USD|CHF|EUR|km|m\b)", s["text"])]
    unsourced = [n for n in num_slides if not S[n-1]["has_source"] and n not in (1, len(S))]
    out.append(check("Every slide with a figure names its source", not unsourced,
                     f"figures without a source line on slides {unsourced}" if unsourced
                     else f"{sum(1 for s in S if s['has_source'])} slides carry a source line",
                     "research", "WARN"))

    weights = ({"idea": 50, "research": 30, "design": 20} if mode == "midterm"
               else {"story": 50, "design": 30, "delivery": 20})
    return {"file": str(path), "mode": mode, "slides": n,
            "aspect_16_9": abs(prs.slide_width / prs.slide_height - 16/9) < .02,
            "weights": weights, "checks": out, "per_slide": S}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx")
    ap.add_argument("--mode", choices=["midterm", "final"], default="final")
    ap.add_argument("--limit-seconds", type=int, default=0)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    r = audit(Path(a.pptx).resolve(), a.mode, a.limit_seconds)
    if a.json:
        print(json.dumps(r, indent=2, default=str))
        return 0
    print(f"# Mechanical audit — {Path(r['file']).name}")
    print(f"{r['slides']} slides · {'16:9' if r['aspect_16_9'] else 'NOT 16:9'} "
          f"· mode: {r['mode']} · weights: "
          + ", ".join(f"{k} {v}%" for k, v in r["weights"].items()) + "\n")
    for area in ("rules", "design", "story", "research"):
        rows = [c for c in r["checks"] if c["area"] == area]
        if not rows:
            continue
        print(f"## {area}")
        for c in rows:
            mark = {"PASS": "✓", "WARN": "!", "FAIL": "✗"}[c["status"]]
            print(f"  {mark} {c['check']} — {c['detail']}")
        print()
    bad = [c for c in r["checks"] if c["status"] != "PASS"]
    print(f"{len(bad)} of {len(r['checks'])} checks not passing.")
    print("\n## Titles in order (read as a story)")
    for s in r["per_slide"]:
        print(f"  {s['n']:>2}. {s['title'] or '(no title)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
