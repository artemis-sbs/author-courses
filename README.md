# Cosmos Author Courses

Courses that teach a storyteller to write missions for Artemis Cosmos, the starship bridge
simulator. The student writes plain text files; they do not program.

**The site:** https://artemis-sbs.github.io/author-courses/

**Status:** Class 1 (twelve lectures) is a complete draft, out for review. Classes 2 to 6
have draft lectures here that are not published on the site.

## What is in here

| Folder | What |
|---|---|
| `c1-01-...` to `c5-...` | One folder per lecture: `lesson.md` (the page a student follows), `video-script.md` (scenes, narration, and notes on what has and has not been checked), `example/` (the finished files the lecture produces), `narration/` (generated: the spoken lines, subtitles, and the video's storyboard) |
| `site/` | The site's own pages: home, reviewers |
| `_tools/` | How the site and the videos are made |
| `videos.json` | Where each lecture's video is hosted |

Class 1's lectures chain: each starts from the finished `example/` of the one before.

## Giving feedback

Every lecture's page ends with **Report a problem with this lecture**, which opens an issue
here. Or open one yourself; say which lecture.

## Building the site

```
pip install mkdocs-material
python _tools/site.py
mkdocs serve
```

`_tools/site.py` copies each published lecture's `lesson.md` into `site_src/` and writes
`mkdocs.yml`. Both are generated; edit the lecture folders and `mkdocs.base.yml`.

## How the videos are made

Nobody records a screen or a voice.

1. `_tools/narration.py <lecture>` reads the **Say:** blocks of `video-script.md`. They are
   written for the ear and carry their own pauses (`|` a breath, `||` a beat, `|||` a
   longer one). Each stretch between two marks becomes one spoken piece and one subtitle.
2. `_tools/voice_local.py <lecture>` speaks each piece with a local text-to-speech model
   (Chatterbox) from a short sample of the author's voice.
3. `_tools/picture/make.py <lecture>` builds the picture from the lecture's
   `narration/storyboard.py`: real captures of the editor, File Explorer, the game and web
   pages, with marks drawn on them, cut to the spoken pieces and assembled in Blender.

The videos, takes and captures are build output and are not in this repository.
`_tools/picture/README.md` has the details. The tools are written for one Windows machine
with the game installed; paths at the top of `_tools/picture/config.py` say where things are.
