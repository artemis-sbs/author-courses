"""The student's mission folder at each moment of a lecture, built from the storyboard's STATES.

A state is a starting folder (the previous lecture's example; "over" lays later lectures'
changed files on top of it) with edits applied in order.
Every edit must apply exactly: a storyboard that has drifted from the page fails here,
loudly, rather than showing a file the page does not have.

A state holds subfolders as well (a tile-map mission keeps `ground\\*.tiles`). A file is
named by its path inside the mission folder, with forward slashes: "mission.amd",
"ground/gully.tiles". A storyboard may write either slash; `key()` makes them one.
"skip" names files or folders (a top-level name, or a path) that are left out.
"""
import os
import shutil

import config

JUNK_DIRS = ("__pycache__",)                    # what a tool leaves in an example folder, never the page's


def key(name):
    """A file's name inside the state: forward slashes, no leading ./"""
    k = name.replace("\\", "/")
    while k.startswith("./"):
        k = k[2:]
    return k


def _read_tree(folder, skip=()):
    """{relative path: text} for every file under folder, subfolders included."""
    skip = {key(s) for s in skip}
    out = {}
    for root, dirs, files in os.walk(folder):
        rel = os.path.relpath(root, folder)
        rel = "" if rel == "." else key(rel) + "/"
        dirs[:] = sorted(d for d in dirs if d not in JUNK_DIRS and not d.startswith(".")
                         and rel + d not in skip and d not in skip)
        for f in sorted(files):
            if rel + f in skip or (not rel and f in skip) or f.endswith(".pyc"):
                continue
            with open(os.path.join(root, f), encoding="utf-8", newline="") as fh:
                out[rel + f] = fh.read().replace("\r\n", "\n")
    return out


def _same_key(out, path):
    """Which file of the state a page's example file is: the longest tail of its path that
    the state has ("c1-04/example/mission.amd" -> "mission.amd",
    ".../example/ground/gully.tiles" -> "ground/gully.tiles")."""
    parts = key(path).split("/")
    for i in range(len(parts)):
        k = "/".join(parts[i:])
        if k in out:
            return k
    return parts[-1]


def files_of(sb, name, _seen=()):
    """{relative file name: text} for a state (text files only, as str with \\n ends)."""
    if name in _seen:
        raise ValueError(f"state {name} is its own base")
    st = sb.STATES[name]
    if "folder" in st:
        out = _read_tree(os.path.join(config.COURSES, st["folder"]), st.get("skip", ()))
        for over in st.get("over", ()):                # a later lecture's example holds only the files it changed
            out.update(_read_tree(os.path.join(config.COURSES, over)))
    else:
        out = dict(files_of(sb, st["base"], _seen + (name,)))
    for edit in st.get("edits", ()):
        kind, f = edit[0], key(edit[1])
        if kind == "replace":
            old, new = edit[2], edit[3]
            n = out[f].count(old)
            if n != 1:
                raise ValueError(f"state {name}: {old!r} is in {f} {n} times, wanted once")
            out[f] = out[f].replace(old, new)
        elif kind == "append":
            out[f] = out[f] + edit[2]
        elif kind == "write":
            out[f] = edit[2]
        elif kind == "delete":                         # a file the step takes away (or moves: delete + write)
            del out[f]
        else:
            raise ValueError(f"state {name}: unknown edit {kind}")
    same = st.get("same_as", ())
    for path in ([same] if isinstance(same, str) else same):       # one file of the page's example, or several
        f = _same_key(out, path)
        with open(os.path.join(config.COURSES, path), encoding="utf-8", newline="") as fh:
            want = fh.read().replace("\r\n", "\n")
        if out.get(f) != want:
            raise ValueError(f"state {name}: {f} is not the same as {path}")
    return out


def check(sb):
    """Build every state once. -> {state: {file: text}}"""
    return {name: files_of(sb, name) for name in sb.STATES}


TEMPLATES = os.environ.get("PIC_TEMPLATES", "E:/a/Cosmos-dev/data/missions/mast_starter/templates")


def template_files(name):
    """{relative path: text} of an `sbs create -t` template, or {} for None."""
    if not name:
        return {}
    root = os.path.join(TEMPLATES, name)
    if not os.path.isdir(root):
        raise FileNotFoundError(f"TEMPLATE_BASE {name!r}: no template folder {root}")
    out = {}
    for d, subs, fs in os.walk(root):
        subs[:] = [x for x in subs if x != "__pycache__"]
        for f in fs:
            rel = os.path.relpath(os.path.join(d, f), root).replace(os.sep, "/")
            out[rel] = open(os.path.join(d, f), encoding="utf-8").read()
    return out


def materialize(sb, name, dest):
    """Write the state's files into dest (the stand-in's mission folder), replacing what
    is there, subfolders and all. Logs and caches the tools left behind are removed, so
    the folder looks as the student's would."""
    files = files_of(sb, name)
    os.makedirs(dest, exist_ok=True)
    for f in os.listdir(dest):
        p = os.path.join(dest, f)
        if os.path.isdir(p):
            shutil.rmtree(p, ignore_errors=True)
        else:
            os.remove(p)
    # A board may say which `sbs create -t` template its mission was made from
    # (TEMPLATE_BASE). Its files go in FIRST, under the state's: a real student's folder
    # has script.py, story.json and the rest, and without them lint reported "No module
    # named 'script'" and every Open Universe field as unknown (the add-ons never loaded).
    # NOT its .amd: the lesson renames or replaces it, and a second universe file would be
    # linted beside the student's.
    for f, text in template_files(getattr(sb, "TEMPLATE_BASE", None)).items():
        if f not in files and not f.endswith(".amd"):
            p = os.path.join(dest, *f.split("/"))
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
    for f, text in files.items():
        p = os.path.join(dest, *f.split("/"))
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    return files
