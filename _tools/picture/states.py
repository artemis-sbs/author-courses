"""The student's mission folder at each moment of a lecture, built from the storyboard's STATES.

A state is a starting folder (the previous lecture's example; "over" lays later lectures'
changed files on top of it) with edits applied in order.
Every edit must apply exactly: a storyboard that has drifted from the page fails here,
loudly, rather than showing a file the page does not have.
"""
import os
import shutil

import config


def files_of(sb, name, _seen=()):
    """{relative file name: text} for a state (text files only, as str with \\n ends)."""
    if name in _seen:
        raise ValueError(f"state {name} is its own base")
    st = sb.STATES[name]
    if "folder" in st:
        folder = os.path.join(config.COURSES, st["folder"])
        out = {}
        for f in sorted(os.listdir(folder)):
            p = os.path.join(folder, f)
            if os.path.isfile(p) and f not in st.get("skip", ()):
                with open(p, encoding="utf-8", newline="") as fh:
                    out[f] = fh.read().replace("\r\n", "\n")
        for over in st.get("over", ()):                # a later lecture's example holds only the files it changed
            folder = os.path.join(config.COURSES, over)
            for f in sorted(os.listdir(folder)):
                p = os.path.join(folder, f)
                if os.path.isfile(p):
                    with open(p, encoding="utf-8", newline="") as fh:
                        out[f] = fh.read().replace("\r\n", "\n")
    else:
        out = dict(files_of(sb, st["base"], _seen + (name,)))
    for edit in st.get("edits", ()):
        kind, f = edit[0], edit[1]
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
        else:
            raise ValueError(f"state {name}: unknown edit {kind}")
    same = st.get("same_as", ())
    for path in ([same] if isinstance(same, str) else same):       # one file of the page's example, or several
        f = os.path.basename(path)
        with open(os.path.join(config.COURSES, path), encoding="utf-8", newline="") as fh:
            want = fh.read().replace("\r\n", "\n")
        if out[f] != want:
            raise ValueError(f"state {name}: {f} is not the same as {path}")
    return out


def check(sb):
    """Build every state once. -> {state: {file: text}}"""
    return {name: files_of(sb, name) for name in sb.STATES}


def materialize(sb, name, dest):
    """Write the state's files into dest (the stand-in's mission folder), replacing what
    is there. Logs and caches the tools left behind are removed, so the folder looks as
    the student's would."""
    files = files_of(sb, name)
    os.makedirs(dest, exist_ok=True)
    for f in os.listdir(dest):
        p = os.path.join(dest, f)
        if os.path.isdir(p):
            shutil.rmtree(p, ignore_errors=True)
        else:
            os.remove(p)
    for f, text in files.items():
        with open(os.path.join(dest, f), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    return files
