"""Is the way east 'well clear of the sentry'? The library's own rules, re-done here:
four-connected BFS walking (tilemap_path, neighbor order +x -x +y -y), notice = Manhattan
distance <= Notice AND Bresenham line of sight through see-through cells (tilemap_sees).
The sentry may be anywhere on its loop (or on its start mark), so every cell of the walk
is checked against every cell of the loop.

    python walkcheck.py <landing.tiles> <starter.tileset> "<patrol>" <notice> <click> <click> ...
    a click is x,y
"""
import sys
from collections import deque


def load(tiles, tileset):
    kinds = {}
    for ln in open(tileset, encoding="utf-8"):
        s = ln.strip()
        if ":" in s and not s.startswith(("#", "tileset", "title", "kinds")):
            k, rest = s.split(":", 1)
            words = rest.split()
            kinds[k.strip()] = {"walk": "walk" in words, "see": "see" in words}
    text = open(tiles, encoding="utf-8").read().replace("\r\n", "\n")
    head, rows = text.split("\n---\n", 1)
    legend, on = {}, False
    marks = {}
    for ln in head.split("\n"):
        if ln.startswith("legend:"):
            on = True
            continue
        if on and ln.startswith("  ") and ":" in ln:
            ch = ln[2]
            rest = ln[4:].strip().split()
            legend[ch] = (rest[0], rest[1][1:] if len(rest) > 1 else None)
        elif on and ln and not ln.startswith(" "):
            on = False
    grid = [r for r in rows.split("\n") if r]
    for y, r in enumerate(grid):
        for x, ch in enumerate(r):
            if ch in legend and legend[ch][1]:
                marks.setdefault(legend[ch][1], []).append((x, y))
    return grid, legend, kinds, marks


def spec(grid, legend, kinds, x, y):
    if not (0 <= y < len(grid) and 0 <= x < len(grid[y])):
        return None
    ch = grid[y][x]
    return kinds.get(legend[ch][0]) if ch in legend else None


def walkable(g, l, k, x, y):
    s = spec(g, l, k, x, y)
    return bool(s and s["walk"])


def path(g, l, k, start, goal):
    prev = {start: None}
    q = deque([start])
    while q:
        cur = q.popleft()
        if cur == goal:
            break
        x, y = cur
        for nxt in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if nxt in prev or not walkable(g, l, k, *nxt):
                continue
            prev[nxt] = cur
            q.append(nxt)
    out, cur = [], goal
    while cur is not None and cur != start:
        out.append(cur)
        cur = prev[cur]
    return list(reversed(out))


def line(x0, y0, x1, y1):
    cells = []
    dx, dy = abs(x1 - x0), -abs(y1 - y0)
    sx, sy = (1 if x0 < x1 else -1), (1 if y0 < y1 else -1)
    err = dx + dy
    while True:
        cells.append((x0, y0))
        if (x0, y0) == (x1, y1):
            return cells
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy


def sees(g, l, k, a, b):
    for c in line(a[0], a[1], b[0], b[1])[1:-1]:
        s = spec(g, l, k, *c)
        if not (s and s["see"]):
            return False
    return True


def loop_cells(points):
    cells = []
    for i, a in enumerate(points):
        b = points[(i + 1) % len(points)]
        x, y = a
        while (x, y) != b:
            cells.append((x, y))
            x += (b[0] > x) - (b[0] < x)
            if x == b[0]:
                y += (b[1] > y) - (b[1] < y)
        cells.append(b)
    return sorted(set(cells))


def main():
    tiles, tileset, patrol, notice = sys.argv[1:5]
    notice = int(notice)
    g, l, k, marks = load(tiles, tileset)
    pts = [tuple(int(v) for v in p.split()) for p in patrol.split(";")]
    loop = loop_cells(pts) + marks.get("post", [])
    bad = [c for c in loop if not walkable(g, l, k, *c)]
    print("loop cells:", len(loop_cells(pts)), "unwalkable:", bad)
    at = marks["pad"][0]
    worst = None
    for click in sys.argv[5:]:
        goal = tuple(int(v) for v in click.split(","))
        p = path(g, l, k, at, goal)
        if not p or p[-1] != goal:
            print("  cannot reach", goal)
        for c in [at] + p:
            for s in loop:
                d = abs(c[0] - s[0]) + abs(c[1] - s[1])
                if d <= notice + 1 and sees(g, l, k, s, c):
                    if worst is None or d < worst[0]:
                        worst = (d, c, s)
                    if d <= notice:
                        print(f"  NOTICED: walker at {c} by sentry at {s} (distance {d})")
        print(f"  {at} -> {goal}: {len(p)} steps")
        at = goal
    print("closest seen approach:", worst)


main()
