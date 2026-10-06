"""Drawn frames: the title card, a table or a numbered list taken from lesson.md, a Command
Prompt showing real output, and the grey placeholder for a still nobody has made yet.

Each function returns (image, meta). meta["parts"] names rectangles a storyboard can mark
with ("part", name):
    table   "head", "r1".."rN" (rows), "r1c1".. (cells; column 1 is the left one)
    list    "item1".."itemN"
    prompt  "run1:cmd", "run1:prompt" (the path and the > before it), "end:prompt" (the last,
            waiting line), "run1:<word>" for an output line that is one word (run1:clean),
            "run1:last" for the run's last line; meta["text"] lets ("lines"/"text") work too
            (on the ROWS as drawn); ("span", run, "words") and ("out", run, n) follow a wrap
    page    "sheet", "find1".."findN"
    search  "word", "summary", "file1".., "hit1".. (every hit, in order), "f1h1".. (by file)
"""
import os
import re

from PIL import Image, ImageDraw, ImageFont

import config as c


def font(path, px):
    return ImageFont.truetype(path, px)


def _canvas(color=None):
    img = Image.new("RGB", (c.W, c.H), color or c.PAPER)
    return img, ImageDraw.Draw(img)


# ------------------------------------------------------------- lesson.md -----
def _section(lesson_text, heading):
    """The lines under a '## heading' (or ###), up to the next heading of the same depth."""
    lines = lesson_text.replace("\r\n", "\n").split("\n")
    for i, ln in enumerate(lines):
        m = re.match(r"^(#+)\s+(.*?)\s*$", ln)
        if m and m.group(2) == heading:
            depth, out = len(m.group(1)), []
            for nxt in lines[i + 1:]:
                m2 = re.match(r"^(#+)\s", nxt)
                if m2 and len(m2.group(1)) <= depth:
                    break
                out.append(nxt)
            return out
    raise ValueError(f"lesson.md has no heading {heading!r}")


def table_of(lesson_text, heading, nth=1):
    """The nth table under a heading (1 is the first)."""
    tables, rows = [], []
    for ln in _section(lesson_text, heading):
        if ln.startswith("|"):
            cells = [x.strip() for x in ln.strip().strip("|").split("|")]
            if all(re.match(r"^:?-+:?$", x) for x in cells):
                continue
            rows.append(cells)
        elif rows:
            tables.append(rows)
            rows = []
    if rows:
        tables.append(rows)
    if len(tables) < nth:
        raise ValueError(f"no table {nth} under {heading!r}")
    return tables[nth - 1][0], tables[nth - 1][1:]


def list_of(lesson_text, heading):
    items, cur = [], None
    for ln in _section(lesson_text, heading):
        m = re.match(r"^\d+\.\s+(.*)$", ln)
        if m:
            cur = [m.group(1)]
            items.append(cur)
        elif cur is not None and ln.startswith("   ") and ln.strip():
            cur.append(ln.strip())
        elif cur is not None and not ln.strip():
            cur = None
    if not items:
        raise ValueError(f"no numbered list under {heading!r}")
    return [" ".join(x) for x in items]


# ------------------------------------------------------------- rich text -----
def _runs(text):
    """Markdown-ish text -> [(words, style)], style in 'text', 'bold', 'code'."""
    out = []
    for part in re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text):
        if not part:
            continue
        if part.startswith("**"):
            out.append((part[2:-2], "bold"))
        elif part.startswith("`"):
            out.append((part[1:-1], "code"))
        else:
            out.append((part, "text"))
    return out


def _fonts(px):
    return {"text": font(c.FONT_TEXT, px), "bold": font(c.FONT_BOLD, px),
            "code": font(c.FONT_MONO, int(px * 0.95))}


def _layout(draw, text, px, width):
    """Wrap rich text to width. -> [[(word, style, x)]] one list per line."""
    fonts = _fonts(px)
    space = draw.textlength(" ", font=fonts["text"])
    lines, cur, x = [], [], 0.0
    for words, style in _runs(text):
        pieces = [words] if style == "code" else re.findall(r"\S+", words)
        if style == "code" and draw.textlength(words, font=fonts[style]) > width:
            pieces = re.findall(r"\S+", words)         # code too long for its column wraps at its spaces
        for w in pieces:
            wlen = draw.textlength(w, font=fonts[style])
            glue = space if cur and not re.match(r"^[.,;:!?)]", w) and not cur[-1][0].endswith("(") else 0
            if cur and x + glue + wlen > width:
                lines.append(cur)
                cur, x, glue = [], 0.0, 0
            cur.append((w, style, x + glue))
            x += glue + wlen
    if cur:
        lines.append(cur)
    return lines


def _paint(draw, lines, px, x, y, ink, line_gap=1.4):
    fonts = _fonts(px)
    for ln in lines:
        for w, style, dx in ln:
            fill = c.ACCENT if style == "code" else ink
            if style == "code":
                fill = (190, 205, 225)
            draw.text((x + dx, y + (px * 0.06 if style == "code" else 0)), w, font=fonts[style], fill=fill)
        y += int(px * line_gap)
    return y


def _height(lines, px, line_gap=1.4):
    return int(px * line_gap) * len(lines)


def _kicker(draw, text, x, y):
    draw.text((x, y), text.upper(), font=font(c.FONT_BOLD, 26), fill=c.ACCENT)


# ----------------------------------------------------------------- cards -----
def title(kicker, title_text, sub=""):
    img, d = _canvas()
    x = 200
    size = 104
    f = font(c.FONT_LIGHT, size)
    while d.textlength(title_text, font=f) > c.W - 2 * x and size > 40:
        size -= 4
        f = font(c.FONT_LIGHT, size)
    y = c.H // 2 - size
    _kicker(d, kicker, x + 4, y - 64)
    d.text((x, y), title_text, font=f, fill=c.INK)
    d.rectangle((x + 4, y + size + 44, x + 124, y + size + 49), fill=c.ACCENT)
    if sub:
        d.text((x + 4, y + size + 76), sub, font=font(c.FONT_TEXT, 40), fill=c.INK_SOFT)
    return img, {"kind": "card", "parts": {}}


def table(kicker, header, rows):
    """A table. The text shrinks, and the margins with it, until every row is on the card."""
    img, d = _canvas()
    ncol = len(header)
    px = 38
    while True:
        pad_x, pad_y = int(px * 0.9), int(px * 0.68)
        left, right = (160, c.W - 160) if px >= 34 else (90, c.W - 90)
        # the first column holds labels and is narrow (never more than a third); the others share what is left
        def natural(cell):                             # how wide the cell is when nothing makes it wrap
            text = cell if "`" in cell else "**%s**" % cell
            return max(w[2] + d.textlength(w[0], font=_fonts(px)[w[1]]) for w in _layout(d, text, px, 10 ** 6)[0])
        first = max(natural(r[0]) for r in [header] + rows) + 2 * pad_x + 20
        first = min(first, (right - left) * 0.42)
        other = (right - left - first) / (ncol - 1)
        xs = [left, left + first] + [left + first + other * i for i in range(1, ncol)]
        laid = [[_layout(d, ("**%s**" % cell) if ((ri == 0 or ci == 0) and "`" not in cell) else cell, px, xs[ci + 1] - xs[ci] - 2 * pad_x)
                 for ci, cell in enumerate(r)] for ri, r in enumerate([header] + rows)]
        heights = [max(_height(cell, px) for cell in r) + 2 * pad_y for r in laid]
        if sum(heights) <= c.H - 220 or px <= 22:
            break
        px -= 2
    top = (c.H - sum(heights)) // 2 + 30
    _kicker(d, kicker, left, top - 70)
    parts, y = {}, top
    for ri, r in enumerate(laid):
        if ri == 0:
            d.rectangle((left, y, right, y + heights[0]), fill=c.PANEL)
        for ci, cell in enumerate(r):
            _paint(d, cell, px, xs[ci] + pad_x, y + pad_y, c.INK_SOFT if ri == 0 else c.INK)
            if ri:
                parts[f"r{ri}c{ci + 1}"] = [int(xs[ci]) + 6, y + 6, int(xs[ci + 1]) - 6, y + heights[ri] - 6]
        parts["head" if ri == 0 else f"r{ri}"] = [left + 6, y + 6, right - 6, y + heights[ri] - 6]
        y += heights[ri]
        d.line((left, y, right, y), fill=c.RULE, width=2)
    return img, {"kind": "card", "parts": parts}


def numbered(kicker, items):
    img, d = _canvas()
    px, left, right, gap = 36, 220, c.W - 220, 34
    laid = [_layout(d, it, px, right - left - 90) for it in items]
    total = sum(_height(x, px) for x in laid) + gap * (len(items) - 1)
    while total > c.H - 260 and px > 24:
        px -= 2
        laid = [_layout(d, it, px, right - left - 90) for it in items]
        total = sum(_height(x, px) for x in laid) + gap * (len(items) - 1)
    y = (c.H - total) // 2 + 30
    _kicker(d, kicker, left, y - 76)
    parts = {}
    for i, lines in enumerate(laid, 1):
        d.text((left, y - 4), str(i), font=font(c.FONT_LIGHT, int(px * 1.25)), fill=c.ACCENT)
        end = _paint(d, lines, px, left + 90, y, c.INK)
        parts[f"item{i}"] = [left - 26, y - 16, right + 26, end + 4]
        y = end + gap
    return img, {"kind": "card", "parts": parts}


def placeholder(name, note=""):
    img, d = _canvas((52, 52, 56))
    for i in range(-c.H, c.W, 80):
        d.line((i, c.H, i + c.H, 0), fill=(60, 60, 64), width=3)
    d.text((120, 420), "NOT MADE YET", font=font(c.FONT_BOLD, 40), fill=(255, 120, 90))
    d.text((120, 480), name, font=font(c.FONT_LIGHT, 96), fill=(235, 235, 235))
    if note:
        d.text((124, 610), note, font=font(c.FONT_TEXT, 40), fill=(190, 190, 190))
    return img, {"kind": "placeholder", "parts": {}}




def points(kicker, items):
    """A numbered list whose words come from the storyboard (the script's own), not lesson.md."""
    return numbered(kicker, items)


def page(kicker, paragraphs, find=(), strike=(), notes=(), caption=""):
    """A sheet of paper with prose on it: a manuscript, or a word processor's page.
    find    substrings to name as parts "find1", "find2", ... (each occurrence, in order)
    strike  substrings an editor has struck through (drawn in the accent)
    notes   [(substring, words)]: words written in the margin, level with that substring
    """
    img, d = _canvas()
    paper, ink = (226, 223, 214), (38, 36, 34)
    x0, x1 = 330, c.W - 330
    px = 46
    serif = font(os.path.join(c.FONTS, "georgia.ttf"), px)
    hand = font(os.path.join(c.FONTS, "segoepr.ttf"), 34)
    width = x1 - x0 - 2 * 110
    # lay the words out, remembering where every character lands
    lines = []                                   # [(text, start offset in its paragraph, paragraph number)]
    for pn, para in enumerate(paragraphs):
        at, cur = 0, ""
        for w in re.findall(r"\S+\s*", para):
            if cur and d.textlength((cur + w).rstrip(), font=serif) > width:
                lines.append((cur, at, pn))
                at += len(cur)
                cur = ""
            cur += w
        lines.append((cur, at, pn))
    lh = int(px * 1.7)
    para_gap = int(px * 0.9)
    total = lh * len(lines) + para_gap * (len(paragraphs) - 1)
    sheet_h = max(total + 220, 560)
    y0 = (c.H - sheet_h) // 2 + 20
    _kicker(d, kicker, x0, y0 - 56)
    d.rectangle((x0 + 10, y0 + 10, x1 + 10, y0 + sheet_h + 10), fill=(12, 13, 16))
    d.rectangle((x0, y0, x1, y0 + sheet_h), fill=paper)
    tx, ty = x0 + 110, y0 + 110
    place = []                                   # (line text, start, paragraph, y)
    y, last_p = ty, 0
    for text, at, pn in lines:
        if pn != last_p:
            y += para_gap
            last_p = pn
        d.text((tx, y), text, font=serif, fill=ink)
        place.append((text, at, pn, y))
        y += lh

    def boxes(sub, nth=1):
        """Rectangles covering the nth occurrence of sub, counted over the whole page."""
        seen = 0
        for pn, para in enumerate(paragraphs):
            i = para.find(sub)
            while i >= 0:
                seen += 1
                if seen == nth:
                    out = []
                    for text, at, p2, yy in place:
                        a, b = max(i, at), min(i + len(sub), at + len(text))
                        if p2 == pn and a < b:
                            xa = tx + d.textlength(text[:a - at], font=serif)
                            xb = tx + d.textlength(text[:b - at], font=serif)
                            out.append([int(xa), yy, int(xb), yy + int(px * 1.25)])
                    return out
                i = para.find(sub, i + 1)
        raise ValueError(f"the page has no {sub!r} (occurrence {nth})")

    for sub in strike:
        for r in boxes(sub):
            mid = (r[1] + r[3]) // 2 + 4
            d.line((r[0] - 4, mid, r[2] + 4, mid - 6), fill=(196, 96, 0), width=5)
    for sub, words in notes:
        r = boxes(sub)[0]
        d.text((x1 - 100 - d.textlength(words, font=hand) + 86, r[1] - 52), words, font=hand, fill=(196, 96, 0))
        d.line((r[2] + 6, r[1] + 4, r[2] + 30, r[1] - 16), fill=(196, 96, 0), width=4)
    if caption:
        d.text((x0, y0 + sheet_h + 34), caption, font=font(c.FONT_TEXT, 30), fill=c.INK_SOFT)
    parts = {"sheet": [x0, y0, x1, y0 + sheet_h]}
    counts = {}
    for n, sub in enumerate(find, 1):
        counts[sub] = counts.get(sub, 0) + 1
        r = boxes(sub, counts[sub])[0]
        parts[f"find{n}"] = [r[0] - 8, r[1] - 4, r[2] + 8, r[3] + 6]
    return img, {"kind": "card", "parts": parts}


# -------------------------------------------------------- Command Prompt -----
def prompt(runs, prompt_text=None, cols=None, title="Command Prompt", last_prompt=None, banner=None, tail=None,
           px_max=38, head=None):
    """A Command Prompt window. runs = [(command, output text)]. The output is what the
    real command printed; only the window round it is drawn. A line longer than the window
    is wide carries on from the left edge of the next row, as it does in a real one.

    meta["flow"] keeps each printed line whole, with the row it starts on, so a storyboard
    can mark words that a wrap has split: ("span", run, "words") and ("out", run, n)."""
    prompt_text = prompt_text or c.PROMPT
    cols = cols or c.TERM_COLS
    rows, marks, flow = [], [], []          # marks: (name, row index, col_from, col_to)

    def put(text, run, kind):
        flow.append({"run": run, "kind": kind, "row": len(rows), "text": text})
        for i in range(0, max(len(text), 1), cols):
            rows.append(text[i:i + cols])

    for ln in (banner or ()):                # what a new window says before its first prompt
        put(ln, 0, "banner")
    if banner:
        put("", 0, "gap")
    base_prompt = prompt_text
    for k, run in enumerate(runs, 1):
        command, output = run[0], run[1]
        # a run may carry its own prompt (a session that has changed folder): (command, output, prompt)
        prompt_text = run[2] if len(run) > 2 and run[2] else base_prompt
        at = len(rows)
        put(prompt_text + command, k, "cmd")
        marks.append((f"run{k}:cmd", at, len(prompt_text), min(cols, len(prompt_text + command))))
        marks.append((f"run{k}:prompt", at, 0, min(cols, len(prompt_text))))
        out = [ln.rstrip() for ln in output.replace("\r\n", "\n").replace("\t", "    ").split("\n")]
        while out and not out[-1]:
            out.pop()
        last = None
        for ln in out:
            at = len(rows)
            put(ln, k, "out")
            s = ln.strip()
            if s:
                last = (at, len(ln))
            if re.match(r"^[A-Za-z]+$", s):
                marks.append((f"run{k}:{s}", at, len(ln) - len(ln.lstrip()), len(ln)))
        if last is not None and last[1] <= cols:
            marks.append((f"run{k}:last", last[0], 0, last[1]))
        put("", k, "gap")
    if last_prompt is not False:             # False: the command is still running, and no prompt has come back
        put(last_prompt or prompt_text, 0, "cmd")
        marks.append(("end:prompt", len(rows) - 1, 0, min(cols, len(rows[-1]))))
    else:
        put("", 0, "gap")
    if head and len(rows) > head:            # scrolled back to the top of a long answer
        rows = rows[:head]
        marks = [m for m in marks if m[1] < head]
        flow = [f for f in flow if f["row"] < head]
    if tail and len(rows) > tail:            # a long report has scrolled: the window shows its last rows
        cut = len(rows) - tail
        rows = rows[cut:]
        marks = [(n, r - cut, a, b) for n, r, a, b in marks if r >= cut]
        flow = [dict(f, row=f["row"] - cut) for f in flow if f["row"] >= cut]
    longest = max(len(r) for r in rows)
    px = px_max
    bar, pad = 46, 26
    win_w, win_h = 1680, 940
    while px > 14:
        f = font(c.FONT_MONO, px)
        cw = f.getlength("M")
        lh = int(px * 1.32)
        if longest * cw <= win_w - 2 * pad and len(rows) * lh <= win_h - bar - 2 * pad:
            break
        px -= 1
    img, d = _canvas()
    x0, y0 = (c.W - win_w) // 2, (c.H - win_h) // 2
    d.rectangle((x0 - 1, y0 - 1, x0 + win_w, y0 + win_h), outline=(70, 70, 70))
    d.rectangle((x0, y0, x0 + win_w - 1, y0 + bar), fill=(32, 32, 32))
    d.text((x0 + 18, y0 + 10), title, font=font(c.FONT_TEXT, 22), fill=(220, 220, 220))
    for i, glyph in enumerate(("\u2500", "\u25a1", "\u2715")):
        d.text((x0 + win_w - 150 + i * 50, y0 + 10), glyph, font=font(r"C:\Windows\Fonts\seguisym.ttf", 20),
               fill=(200, 200, 200))
    d.rectangle((x0, y0 + bar, x0 + win_w - 1, y0 + win_h - 1), fill=c.TERM_BG)
    tx, ty = x0 + pad, y0 + bar + pad
    for i, r in enumerate(rows):
        d.text((tx, ty + i * lh), r, font=f, fill=c.TERM_INK)
    # the cursor, after the last prompt
    cy = ty + (len(rows) - 1) * lh
    d.rectangle((tx + len(rows[-1]) * cw, cy + lh - 8, tx + (len(rows[-1]) + 1) * cw, cy + lh - 4), fill=c.TERM_INK)
    parts = {}
    for name, row, a, b in marks:
        parts.setdefault(name, [int(tx + a * cw) - 8, ty + row * lh - 4, int(tx + b * cw) + 8, ty + (row + 1) * lh])
    meta = {"kind": "terminal", "parts": parts, "flow": flow, "cols": cols,
            "text": {"lines": rows, "y_line1": ty - 2, "line_h": lh, "x0": tx, "char_w": cw,
                     "visible": [1, len(rows)], "clip": [x0, y0 + bar, x0 + win_w, y0 + win_h]}}
    return img, meta


def flow_rects(meta, run, a_text=None, nth=1, line=None, kind="out"):
    """Rectangles (one a row) for words in a drawn Command Prompt, wraps and all.
    a_text: the nth occurrence of those words in the run's output; or line: the whole of the
    run's nth line of output that is not blank."""
    t = meta["text"]
    cols, cw, lh = meta["cols"], t["char_w"], t["line_h"]
    outs = [f for f in meta["flow"] if f["run"] == run and f["kind"] == kind and f["text"].strip()]
    hit = None
    if line is not None:
        if not 1 <= line <= len(outs):
            raise ValueError(f"run {run} printed {len(outs)} lines, and line {line} is marked")
        f = outs[line - 1]
        lead = len(f["text"]) - len(f["text"].lstrip())
        hit = (f, lead, len(f["text"]))
    else:
        seen = 0
        for f in outs:
            i = f["text"].find(a_text)
            while i >= 0:
                seen += 1
                if seen == nth:
                    hit = (f, i, i + len(a_text))
                    break
                i = f["text"].find(a_text, i + 1)
            if hit:
                break
        if not hit:
            raise ValueError(f"run {run} did not print {a_text!r} (occurrence {nth})")
    f, a, b = hit
    rects = []
    for k in range(a // cols, (b - 1) // cols + 1):
        ca, cb = max(a, k * cols) - k * cols, min(b, (k + 1) * cols) - k * cols
        y = t["y_line1"] + (f["row"] + k) * lh
        rects.append([t["x0"] + ca * cw - 6, y - 2, t["x0"] + cb * cw + 6, y + lh + 2])
    return rects


# ------------------------------------------------------------------ search -----
def find_whole(files, word):
    """Where a word is in a folder's text files, as an editor's search counts with Match
    Case and Match Whole Word both on. -> [(file, [(line number, column, line text)])]"""
    pat = re.compile(r"(?<![A-Za-z0-9_])" + re.escape(word) + r"(?![A-Za-z0-9_])")
    out = []
    for name in sorted(files):
        hits = []
        for n, ln in enumerate(files[name].split("\n"), 1):
            for m in pat.finditer(ln):
                hits.append((n, m.start(), ln))
        if hits:
            out.append((name, hits))
    return out


def search(word, found, kicker="Search the folder"):
    """What a search of the folder finds, drawn plainly (it is not a picture of the editor):
    the word, the count, and every hit with its file and line number. found = find_whole().
    Parts: "word", "summary", "file1".., "hit1".. (all hits in order), and "f1h1".. by file."""
    img, d = _canvas()
    left, right = 150, c.W - 150
    total = sum(len(h) for _, h in found)
    rows = total + len(found)
    px = 30
    while px > 18 and 250 + rows * int(px * 1.5) + len(found) * 16 > c.H - 60:
        px -= 1
    mono, monob = font(c.FONT_MONO, px), font(c.FONT_MONO_BOLD, px)
    lh = int(px * 1.5)
    cw = mono.getlength("M")
    block = 150 + rows * lh + len(found) * 16
    y = max(50, (c.H - block) // 2)
    _kicker(d, kicker, left, y)
    y += 50
    big = font(c.FONT_MONO, 44)
    w = d.textlength(word, font=big)
    d.rounded_rectangle((left, y, left + w + 48, y + 70), radius=6, fill=c.PANEL, outline=c.RULE, width=2)
    d.text((left + 24, y + 10), word, font=big, fill=c.INK)
    parts = {"word": [left - 4, y - 4, int(left + w + 52), y + 74]}
    note = "match case, whole word"
    d.text((left + w + 80, y + 20), note, font=font(c.FONT_TEXT, 28), fill=c.INK_SOFT)
    if total:
        summary = f"{total} result{'s' if total != 1 else ''} in {len(found)} file{'s' if len(found) != 1 else ''}"
    else:
        summary = "No results"
    sf = font(c.FONT_BOLD, 34)
    sx = right - d.textlength(summary, font=sf)
    d.text((sx, y + 14), summary, font=sf, fill=c.INK)
    parts["summary"] = [int(sx) - 14, y + 6, right + 14, y + 66]
    y += 100
    d.line((left, y, right, y), fill=c.RULE, width=2)
    y += 22
    room = int((right - left - 110) / cw)
    n_all = 0
    for fi, (name, hits) in enumerate(found, 1):
        d.text((left, y), name, font=font(c.FONT_BOLD, px), fill=c.INK)
        d.text((left + d.textlength(name, font=font(c.FONT_BOLD, px)) + 18, y), str(len(hits)),
               font=font(c.FONT_TEXT, px), fill=c.INK_SOFT)
        top = y
        y += lh
        for hi, (n, col, text) in enumerate(hits, 1):
            n_all += 1
            lead = len(text) - len(text.lstrip())
            shown, at = text[lead:], col - lead
            if len(shown) > room:                       # keep the word in sight
                start = max(0, min(at - room // 3, len(shown) - room))
                shown = ("..." if start else "") + shown[start + (3 if start else 0):start + room]
                at -= start
            d.text((left + 20, y), f"{n:>4}", font=mono, fill=c.INK_SOFT)
            x = left + 110
            d.text((x, y), shown, font=mono, fill=(170, 176, 186))
            if 0 <= at and at + len(word) <= len(shown):
                d.rectangle((x + at * cw - 3, y + 2, x + (at + len(word)) * cw + 3, y + lh - 6), fill=(74, 56, 20))
                d.text((x + at * cw, y), word, font=monob, fill=c.ACCENT)
            box = [left + 6, y - 3, right - 6, y + lh - 5]
            parts[f"hit{n_all}"] = box
            parts[f"f{fi}h{hi}"] = box
            y += lh
        parts[f"file{fi}"] = [left - 10, top - 6, right + 10, y - 2]
        y += 16
    if not total:
        d.text((left, y + 10), "No results found.", font=font(c.FONT_TEXT, 36), fill=c.INK_SOFT)
    return img, {"kind": "card", "parts": parts, "count": total, "files": len(found)}
