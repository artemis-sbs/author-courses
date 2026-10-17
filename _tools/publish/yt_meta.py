"""Add a class's lectures to yt_meta.json, in the form Class 3 was published with.

    python yt_meta.py 4            add any Class 4 lecture not already there
    python yt_meta.py 4 --show     print what would be added, change nothing

The title comes from the lesson's own heading ("# Class 4, Lecture 8 - EVA"), the page
link from the folder name. Entries already in the file are left exactly as they are, so a
hand edit to a title survives. Then upload the drafts, put each video id in yt_ids.txt
("4.8 <id>"), and run yt_c3.py 4.1 4.2 ... (it reads any class).
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
COURSES = os.path.dirname(os.path.dirname(HERE))
META = os.path.join(HERE, "yt_meta.json")
SITE = "https://artemis-sbs.github.io/author-courses/"

DESC = ("Class {cls}, Lecture {lec} of the Cosmos Author Courses: writing missions for Artemis Cosmos, "
        "for storytellers, not programmers.\n\nThe page for this lecture, with every step written out and "
        "the finished files to download:\n" + SITE + "class-{cls}/{page}/\n\nThe whole course: " + SITE +
        "\n\nThis is a review draft. The voice is generated from the author's own.")


def entry(folder):
    m = re.match(r"c(\d+)-(\d+)-(.+)$", folder)
    cls, lec, slug = int(m.group(1)), int(m.group(2)), m.group(3)
    with open(os.path.join(COURSES, folder, "lesson.md"), encoding="utf-8") as fh:
        head = fh.readline().strip()
    h = re.match(r"#\s*Class \d+, Lecture \d+ - (.+)$", head)
    if not h:
        sys.exit(f"{folder}/lesson.md: first line is not '# Class N, Lecture M - Title': {head!r}")
    name = h.group(1).strip()
    return {
        "folder": folder,
        "file": f"Class {cls} Lecture {lec:02d}",
        "title": f"Cosmos Author Courses {cls}.{lec}: {name}",
        "desc": DESC.format(cls=cls, lec=lec, page=f"{lec:02d}-{slug}"),
        "cls": cls,
        "lec": lec,
    }


def main():
    cls = int(sys.argv[1])
    show = "--show" in sys.argv
    with open(META, encoding="utf-8") as fh:
        meta = json.load(fh)
    have = {m["folder"] for m in meta}
    folders = sorted(f for f in os.listdir(COURSES) if re.match(rf"c{cls}-\d+-", f))
    new = [entry(f) for f in folders if f not in have]
    for e in new:
        print(f"{e['cls']}.{e['lec']:<3} {e['title']}")
    if not new:
        print(f"Class {cls}: every lecture is already in yt_meta.json")
    if show or not new:
        return
    meta += new
    meta.sort(key=lambda m: (m["cls"], m["lec"]))
    with open(META, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(meta, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(f"added {len(new)} to {META}")


if __name__ == "__main__":
    main()
