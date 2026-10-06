"""Stills + the storyboard's marks -> one 1920x1080 frame per beat, and the cross-fades.

A still is <out>/stills/<name>.png with <name>.json beside it (where its lines of text
are, and any named parts). Cards are drawn here every time; captures are made by
capture.py. A still that does not exist yet becomes a grey placeholder, and the run says so.
"""
import json
import os

from PIL import Image, ImageDraw

import cards
import config as c


def _lesson(folder):
    with open(os.path.join(folder, "lesson.md"), encoding="utf-8") as f:
        return f.read()


def step_titles(folder):
    import re
    out = {}
    for ln in _lesson(folder).split("\n"):
        m = re.match(r"^## Step (\d+) - (.*?)\s*$", ln)
        if m:
            out[int(m.group(1))] = m.group(2)
    return out


def make_card(sb, folder, spec):
    kind, opts = spec[1], spec[2]
    if kind == "title":
        k, t, s = sb.TITLE
        return cards.title(opts.get("kicker", k), opts.get("title", t), opts.get("sub", s))
    if kind == "table":
        header, rows = cards.table_of(_lesson(folder), opts["heading"], opts.get("nth", 1))
        if opts.get("rows"):                          # only these rows of a long table (1 is the first)
            rows = [rows[i - 1] for i in opts["rows"]]
        return cards.table(opts.get("kicker", opts["heading"]), header, rows)
    if kind == "rows":                                # a table whose words are the storyboard's (the page's own)
        return cards.table(opts["kicker"], list(opts["header"]), [list(r) for r in opts["rows"]])
    if kind == "list":
        return cards.numbered(opts.get("kicker", opts["heading"]), cards.list_of(_lesson(folder), opts["heading"]))
    if kind == "points":                              # the words are the storyboard's own
        return cards.points(opts["kicker"], opts["items"])
    if kind == "page":
        return cards.page(opts.get("kicker", ""), opts["text"], find=opts.get("find", ()),
                          strike=opts.get("strike", ()), notes=opts.get("notes", ()),
                          caption=opts.get("caption", ""))
    if kind == "search":                              # counted in the state's own files, then drawn
        import states
        found = cards.find_whole(states.files_of(sb, opts["state"]), opts["word"])
        n = sum(len(h) for _, h in found)
        if "want" in opts and opts["want"] != (n, len(found)):
            raise ValueError(f"a search for {opts['word']!r} in state {opts['state']} finds {n} in {len(found)} "
                             f"file(s), and the storyboard says the script wants {opts['want']}")
        return cards.search(opts["word"], found, kicker=opts.get("kicker", "Search the folder"))
    raise ValueError(f"unknown card kind {kind}")


def load_still(sb, folder, stills_dir, name):
    """-> (image at 1920x1080, meta, real?)"""
    spec = sb.STILLS.get(name)
    if spec and spec[0] == "card":
        img, meta = make_card(sb, folder, spec)
        return img, meta, True
    png, js = os.path.join(stills_dir, name + ".png"), os.path.join(stills_dir, name + ".json")
    if not os.path.exists(png):
        note = (spec[0] + ": " + str(spec[1])) if spec else "not in the storyboard"
        img, meta = cards.placeholder(name, note[:70])
        return img, meta, False
    img = Image.open(png).convert("RGB")
    meta = json.load(open(js, encoding="utf-8")) if os.path.exists(js) else {"kind": "image", "parts": {}}
    if img.size != (c.W, c.H):
        img, meta = _fit(img, meta)
    return img, meta, True


def _fit(img, meta):
    """Scale a still of another shape (the game's windows are 4:3) to fit the frame. What is
    left over at the sides is the same picture, blurred and darkened: quieter than black bars."""
    s = min(c.W / img.width, c.H / img.height)
    w, h = int(round(img.width * s)), int(round(img.height * s))
    ox, oy = (c.W - w) // 2, (c.H - h) // 2
    out = backdrop(img)
    out.paste(img.resize((w, h), Image.LANCZOS), (ox, oy))
    meta = dict(meta)
    meta["parts"] = {k: [ox + r[0] * s, oy + r[1] * s, ox + r[2] * s, oy + r[3] * s]
                     for k, r in meta.get("parts", {}).items()}
    if "text" in meta:
        t = dict(meta["text"])
        t["y_line1"] = oy + t["y_line1"] * s
        t["x0"] = ox + t["x0"] * s
        t["line_h"] *= s
        t["char_w"] *= s
        t["clip"] = [ox + t["clip"][0] * s, oy + t["clip"][1] * s, ox + t["clip"][2] * s, oy + t["clip"][3] * s]
        meta["text"] = t
    meta["image_rect"] = [ox, oy, ox + w, oy + h]
    return out, meta


def backdrop(img):
    """The picture, filling the frame, out of focus and dark."""
    from PIL import ImageEnhance, ImageFilter
    s = max(c.W / img.width, c.H / img.height)
    small = img.resize((max(1, int(img.width * s / 8)), max(1, int(img.height * s / 8))), Image.BILINEAR)
    small = small.filter(ImageFilter.GaussianBlur(7))
    big = small.resize((int(img.width * s) + 1, int(img.height * s) + 1), Image.BICUBIC)
    x, y = (big.width - c.W) // 2, (big.height - c.H) // 2
    return ImageEnhance.Brightness(big.crop((x, y, x + c.W, y + c.H))).enhance(0.38)


def zoomed(img, scale, origin):
    """The frame pushed in by scale, about origin (frame pixels): what Blender shows when
    the strip's transform has that scale and that origin."""
    if scale <= 1.0005:
        return img
    ox, oy = origin
    box = (ox - ox / scale, oy - oy / scale, ox + (c.W - ox) / scale, oy + (c.H - oy) / scale)
    return img.resize((c.W, c.H), Image.BICUBIC, box=box)


def rects_of(mark, meta, where):
    """A mark -> the rectangles it draws (one, except for words a Command Prompt wrapped)."""
    if mark[0] in ("span", "out", "cmd"):
        if meta.get("kind") != "terminal":
            raise ValueError(f"{where}: mark {mark} is for a Command Prompt still")
        try:
            if mark[0] == "cmd":                      # words of the typed command itself
                return cards.flow_rects(meta, mark[1], a_text=mark[2], nth=mark[3] if len(mark) > 3 else 1,
                                        kind="cmd")
            if mark[0] == "span":
                return cards.flow_rects(meta, mark[1], a_text=mark[2], nth=mark[3] if len(mark) > 3 else 1)
            return cards.flow_rects(meta, mark[1], line=mark[2])
        except ValueError as e:
            raise ValueError(f"{where}: {e}")
    return [rect_of(mark, meta, where)]


def rect_of(mark, meta, where):
    """A mark -> [x0, y0, x1, y1] in frame pixels."""
    kind = mark[0]
    if kind == "rect":
        box = meta.get("image_rect", [0, 0, c.W, c.H])
        w, h = box[2] - box[0], box[3] - box[1]
        return [box[0] + mark[1] * w, box[1] + mark[2] * h, box[0] + mark[3] * w, box[1] + mark[4] * h]
    if kind == "part":
        if mark[1] not in meta.get("parts", {}):
            raise ValueError(f"{where}: no part {mark[1]!r}; it has {sorted(meta.get('parts', {}))}")
        return list(meta["parts"][mark[1]])
    t = meta.get("text")
    if not t:
        raise ValueError(f"{where}: mark {mark} needs a still that knows where its text is")
    lines, lh, cw = t["lines"], t["line_h"], t["char_w"]

    def text_of(n):
        if not 1 <= n <= len(lines):
            raise ValueError(f"{where}: line {n} is not in the file ({len(lines)} lines)")
        return lines[n - 1]

    def box(a, b, col0, col1, pad=(10, 3)):
        lo, hi = t["visible"]
        if a < lo or b > hi:
            raise ValueError(f"{where}: lines {a}-{b} are marked and only {lo}-{hi} are on screen")
        if "row_of" in t:                               # a wrapped file: a line may take several rows
            ra, rb = t["row_of"][a - 1], t["row_of"][b - 1] + len(t["breaks"][b - 1])
            return [t["x0"] + col0 * cw - pad[0], t["y_line1"] + ra * lh - pad[1],
                    t["x0"] + col1 * cw + pad[0], t["y_line1"] + rb * lh + pad[1]]
        return [t["x0"] + col0 * cw - pad[0], t["y_line1"] + (a - 1) * lh - pad[1],
                t["x0"] + col1 * cw + pad[0], t["y_line1"] + b * lh + pad[1]]

    def on_row(n, at, length):
        """Where words of a wrapped line are: (row, column in that row, length that fits on it)."""
        starts = t["breaks"][n - 1]
        k = max(i for i, s0 in enumerate(starts) if s0 <= at)
        end = starts[k + 1] if k + 1 < len(starts) else at + length
        return t["row_of"][n - 1] + k, at - starts[k], min(length, max(1, end - at))

    if kind == "lines":
        a, b = mark[1], mark[2]
        width = max([len(text_of(n).rstrip()) for n in range(a, b + 1)] + [4])
        if "row_of" in t:
            width = min(width, t["cols"])
        r = box(a, b, 0, width)
        r[2] = min(r[2], t["clip"][2] - 6)
        return r
    if kind == "text":
        line, s = text_of(mark[1]), mark[2]
        at = -1
        for _ in range(mark[3] if len(mark) > 3 else 1):
            at = line.find(s, at + 1)
            if at < 0:
                raise ValueError(f"{where}: {s!r} is not on line {mark[1]}: {line!r}")
        if "row_of" in t:
            box(mark[1], mark[1], 0, 1)                 # (is the line on screen?)
            row, col, n = on_row(mark[1], at, len(s))
            return [t["x0"] + col * cw - 5, t["y_line1"] + row * lh - 2,
                    t["x0"] + (col + n) * cw + 5, t["y_line1"] + (row + 1) * lh + 2]
        return box(mark[1], mark[1], at, at + len(s), pad=(5, 2))
    if kind == "hashes":
        line = text_of(mark[1])
        n = len(line) - len(line.lstrip("#"))
        if not n:
            raise ValueError(f"{where}: line {mark[1]} does not start with a hash: {line!r}")
        return box(mark[1], mark[1], 0, n, pad=(5, 2))
    if kind == "after":
        n = len(text_of(mark[1]).rstrip())
        return box(mark[1], mark[1], n + 0.3, n + 5, pad=(0, 2))
    raise ValueError(f"{where}: unknown mark {kind}")


def draw_marks(img, rects, dim):
    if not rects:
        return img
    img = img.convert("RGBA")
    if dim:
        shade = Image.new("RGBA", img.size, (0, 0, 0, 150))
        hole = ImageDraw.Draw(shade)
        for r in rects:
            hole.rounded_rectangle([r[0] - 6, r[1] - 6, r[2] + 6, r[3] + 6], radius=10, fill=(0, 0, 0, 0))
        img = Image.alpha_composite(img, shade)
    over = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    for r in rects:
        d.rounded_rectangle(r, radius=7, fill=c.ACCENT + (30,), outline=c.ACCENT + (255,), width=4)
    return Image.alpha_composite(img, over).convert("RGB")


def draw_chip(img, text, corner="br"):
    d = ImageDraw.Draw(img)
    f = cards.font(c.FONT_BOLD, 30)
    w = int(d.textlength(text, font=f))
    pad = 22
    x1, y1 = c.W - 48, c.H - 84
    x0, y0 = x1 - w - 2 * pad - 10, y1 - 62
    d.rounded_rectangle((x0, y0, x1, y1), radius=8, fill=c.PAPER, outline=c.RULE, width=2)
    d.rectangle((x0, y0 + 10, x0 + 6, y1 - 10), fill=c.ACCENT)
    d.text((x0 + pad + 6, y0 + 11), text, font=f, fill=c.INK)
    return img


def crop_to(img, crop):
    u0, v0, u1, v1 = crop
    box = (int(u0 * c.W), int(v0 * c.H), int(u1 * c.W), int(v1 * c.H))
    part = img.crop(box)
    s = min(c.W / part.width, c.H / part.height)
    part = part.resize((int(part.width * s), int(part.height * s)), Image.LANCZOS)
    out = Image.new("RGB", (c.W, c.H), c.PAPER)
    out.paste(part, ((c.W - part.width) // 2, (c.H - part.height) // 2))
    return out


def compose(sb, folder, out, beats):
    """Write frames/<beat>.png for every beat. -> (frame paths by beat name, problems, missing stills)
    Each beat also learns its "focus": the middle of its marks, where a push-in heads."""
    stills_dir = os.path.join(out, "stills")
    frames_dir = os.path.join(out, "frames")
    os.makedirs(frames_dir, exist_ok=True)
    for f in os.listdir(frames_dir):
        if f.endswith(".png"):
            os.remove(os.path.join(frames_dir, f))
    steps = step_titles(folder)
    cache, problems, missing, paths = {}, [], set(), {}
    for b in beats:
        if b["still"] not in cache:
            cache[b["still"]] = load_still(sb, folder, stills_dir, b["still"])
        base, meta, real = cache[b["still"]]
        img = base.copy()
        where = f"{b['scene']} beat {b['n']} ({b['still']})"
        b["focus"], b["real"] = None, real
        if not real:
            missing.add(b["still"])
        else:
            rects = []
            for m in b["marks"]:
                try:
                    rects.extend(rects_of(m, meta, where))
                except ValueError as e:
                    problems.append(str(e))
            img = draw_marks(img, rects, b["dim"])
            if rects and not b["crop"]:
                b["focus"] = [sum((r[0] + r[2]) / 2 for r in rects) / len(rects),
                              sum((r[1] + r[3]) / 2 for r in rects) / len(rects)]
            if b["crop"]:
                img = crop_to(img, b["crop"])
        if b["chip"] is not None:
            img = draw_chip(img, f"Step {b['chip']}  {steps.get(b['chip'], '')}".rstrip())
        path = os.path.join(frames_dir, b["name"] + ".png")
        img.save(path)
        paths[b["name"]] = path
    return paths, problems, sorted(missing)


def pushes(beats):
    """Decide the motion. Beats that follow each other on the same still are one "hold".
    A hold that has a beat of config.PUSH_HOLD frames or more pushes in, slowly and without
    stopping, from its first frame to its last, toward the middle of its marks. Everything
    else stays still. A beat with "move": False keeps its whole hold still.
    Sets on each beat: "push" = None, or (first frame, last frame, final scale, [x, y])."""
    i = 0
    while i < len(beats):
        j = i
        while (j + 1 < len(beats) and beats[j + 1]["still"] == beats[i]["still"]
               and beats[j + 1]["crop"] == beats[i]["crop"] and beats[j + 1]["scene"] == beats[i]["scene"]):
            j += 1
        hold = beats[i:j + 1]
        first, last = hold[0]["start"], hold[-1]["start"] + hold[-1]["length"] - 1
        push = None
        if (max(b["length"] for b in hold) >= c.PUSH_HOLD and all(b.get("move", True) for b in hold)
                and all(b.get("real") for b in hold)):
            scale = min(c.PUSH_MAX, 1 + c.PUSH_RATE * (last - first + 1) / c.FPS)
            pts = [b["focus"] for b in hold if b.get("focus")]
            if pts:
                fx, fy = sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)
                # head toward the marks, but not so far off-centre that the other side seems to slide away
                origin = [c.W / 2 + (fx - c.W / 2) * 0.6, c.H / 2 + (fy - c.H / 2) * 0.6]
            else:
                origin = [c.W / 2, c.H / 2]
            push = (first, last, scale, origin)
        for b in hold:
            b["push"] = push
        i = j + 1


def scale_at(b, frame):
    """How far in the beat's picture is at a frame of the timeline (1.0 = not at all)."""
    if not b.get("push"):
        return 1.0
    first, last, scale, _ = b["push"]
    t = min(1.0, max(0.0, (frame - first) / max(1, last - first)))
    return 1 + (scale - 1) * t


def frame_at(b, path, frame):
    """The picture a beat shows at a frame, pushed in as far as it is by then."""
    img = Image.open(path).convert("RGB")
    return zoomed(img, scale_at(b, frame), b["push"][3]) if b.get("push") else img


def fades(out, beats, paths):
    """The frames of each cross-fade. -> the edit list Blender reads:
    [{name, start, length, files, zoom: [scale at its first frame, at its last], origin: [u, v]}]
    (zoom only on a strip that pushes in; origin in fractions of the frame, from the top left)."""
    x_dir = os.path.join(out, "frames", "x")
    os.makedirs(x_dir, exist_ok=True)
    for f in os.listdir(x_dir):
        os.remove(os.path.join(x_dir, f))
    pushes(beats)
    half = c.FADE // 2
    edl = []
    for i, b in enumerate(beats):
        start, end = b["start"], b["start"] + b["length"]
        nxt = beats[i + 1] if i + 1 < len(beats) else None
        lead = half if i else 0                       # frames given to the fade from the beat before
        tail = c.FADE - half if nxt else 0
        same_next = nxt and _same(paths[b["name"]], paths[nxt["name"]]) and b.get("push") == nxt.get("push")
        prev = beats[i - 1] if i else None
        if prev and _same(paths[prev["name"]], paths[b["name"]]) and prev.get("push") == b.get("push"):
            lead = 0
        if same_next:
            tail = 0
        strip = {"name": b["name"], "start": start + lead, "length": end - tail - start - lead,
                 "files": [paths[b["name"]]]}
        if b.get("push"):
            strip["zoom"] = [scale_at(b, strip["start"]), scale_at(b, strip["start"] + strip["length"] - 1)]
            strip["origin"] = [b["push"][3][0] / c.W, b["push"][3][1] / c.H]
        edl.append(strip)
        if nxt and not same_next:
            cut = end - tail + c.FADE // 2            # both pictures as far in as they are at the cut
            a_img, b_img = frame_at(b, paths[b["name"]], cut), frame_at(nxt, paths[nxt["name"]], cut)
            files = []
            for k in range(c.FADE):
                p = os.path.join(x_dir, f"{b['name']}_{k:02d}.png")
                Image.blend(a_img, b_img, (k + 1) / (c.FADE + 1)).save(p)
                files.append(p)
            edl.append({"name": b["name"] + "_x", "start": end - tail, "length": c.FADE, "files": files})
    return edl


def _same(p, q):
    with open(p, "rb") as a, open(q, "rb") as b:
        return a.read() == b.read()
