"""Build the course site's pages from the lecture folders.

    python _tools/site.py            # writes site_src/ ; then: mkdocs build  (or serve)

The lectures live one folder each at the top of the repository (`c1-05-...`), with
`lesson.md` as the page a student reads. mkdocs wants one docs folder, so this copies each
published lecture's page into `site_src/`, puts its video at the top, and zips its
`example/` folder for download. `site_src/` is generated: do not edit it, do not commit it.

Which classes are published is PUBLISHED below. A lecture's video and subtitles are named
in `videos.json` at the top of the repository; a lecture with no entry says so on its page.
"""
import json
import os
import re
import shutil
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "site_src")
REPO = "https://github.com/artemis-sbs/author-courses"

PUBLISHED = {
    1: "Class 1 - The Writer's Desk and Your First Quest",
}

VIDEO_SECTION = re.compile(r"^## The video\s*\n.*?(?=^## )", re.S | re.M)


def lectures(class_number):
    out = []
    for name in sorted(os.listdir(ROOT)):
        m = re.match(rf"^c{class_number}-(\d\d)-(.+)$", name)
        if m and os.path.isfile(os.path.join(ROOT, name, "lesson.md")):
            out.append((int(m.group(1)), name))
    return out


def title_of(text, fallback):
    m = re.search(r"^# (.+)$", text, re.M)
    return m.group(1).strip() if m else fallback


def video_block(entry, name):
    if not entry:
        return ("## The video\n\n*The video for this lecture is not posted yet. The page "
                "below is complete without it.*\n\n")
    lines = ["## The video", ""]
    if entry.get("youtube"):
        lines += ['<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/'
                  f'{entry["youtube"]}" title="{name}" allowfullscreen></iframe></div>', ""]
    elif entry.get("url"):
        lines += [f'[Watch the video]({entry["url"]})', ""]
    if entry.get("minutes"):
        lines += [f'About {entry["minutes"]} minutes. Subtitles are available in the player.', ""]
    return "\n".join(lines) + "\n"


def zip_example(folder, target):
    src = os.path.join(folder, "example")
    if not os.path.isdir(src):
        return False
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for base, dirs, files in os.walk(src):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in sorted(files):
                full = os.path.join(base, f)
                z.write(full, os.path.relpath(full, src))
    return True


def main():
    videos = {}
    vpath = os.path.join(ROOT, "videos.json")
    if os.path.isfile(vpath):
        with open(vpath, encoding="utf-8") as f:
            videos = json.load(f)
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "downloads"))
    for extra in ("index.md", "reviewers.md", "extra.css"):
        shutil.copyfile(os.path.join(ROOT, "site", extra), os.path.join(OUT, extra))

    nav = ["nav:", "  - Home: index.md", "  - For reviewers: reviewers.md"]
    for number, heading in PUBLISHED.items():
        os.makedirs(os.path.join(OUT, f"class-{number}"))
        nav.append(f"  - {json.dumps(heading)}:")
        for n, name in lectures(number):
            with open(os.path.join(ROOT, name, "lesson.md"), encoding="utf-8") as f:
                text = f.read().replace("\r\n", "\n")
            title = title_of(text, name)
            block = video_block(videos.get(name), title)
            text = VIDEO_SECTION.sub(lambda m: block, text, count=1) if VIDEO_SECTION.search(text) \
                else text
            got_zip = zip_example(os.path.join(ROOT, name), os.path.join(OUT, "downloads", name + ".zip"))
            tail = ["", "---", ""]
            if got_zip:
                tail.append(f"[Download this lecture's finished files](../downloads/{name}.zip) "
                            f"(a zip of its `example` folder).")
                tail.append("")
            tail.append(f"[Report a problem with this lecture]({REPO}/issues/new?"
                        f"template=lecture-feedback.md&title={name}%3A+) | "
                        f"[This page's source]({REPO}/blob/main/{name}/lesson.md)")
            page = f"class-{number}/{n:02d}-{name.split('-', 2)[2]}.md"
            with open(os.path.join(OUT, page), "w", encoding="utf-8", newline="\n") as f:
                f.write(text.rstrip("\n") + "\n" + "\n".join(tail) + "\n")
            short = re.sub(r"^Class \d+, Lecture \d+ - ", "", title)
            nav.append(f"    - {json.dumps(str(n) + '. ' + short)}: {page}")
    with open(os.path.join(ROOT, "mkdocs.base.yml"), encoding="utf-8") as f:
        base = f.read().rstrip("\n")
    with open(os.path.join(ROOT, "mkdocs.yml"), "w", encoding="utf-8", newline="\n") as f:
        f.write(base + "\n" + "\n".join(nav) + "\n")
    print(f"site_src written: {sum(len(lectures(n)) for n in PUBLISHED)} lectures")


if __name__ == "__main__":
    main()
