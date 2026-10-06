# picture: the picture for a lecture video, with no one recording a screen

Makes a silent draft video for one lecture, cut to its narration. The voice is made later
by another tool; subtitles are a separate file and are never drawn on the frame.

## What it reads and writes

| Reads | What it is |
|---|---|
| `<lecture>\narration\shots.py` | The narration, from `_tools\narration.py`: scenes, captions, frames at 30 a second |
| `<lecture>\narration\storyboard.py` | Written by hand: the states of the student's folder, the stills, and which still and marks go with which caption. Its docstring is the format |
| `<lecture>\lesson.md` | Tables, numbered lists and step titles for the drawn cards |

| Writes, in `R:\cosmos\courses\<c1_05>\` | |
|---|---|
| `stills\` | One PNG per still, with a `.json` saying where its lines of text are |
| `frames\` | One composed 1920x1080 frame per beat; `frames\x\` holds the cross-fades |
| `contact.png`, `contact2.png` | Every beat as a thumbnail, in order |
| `draft.mp4`, `draft.blend`, `edl.json` | The video, the Blender file it was cut in, the edit list |
| `draft.srt` | The written sentences, timed to THIS picture |

## The commands

```
python make.py c1-05-the-shape-of-a-record --plan       # the beats and their times; checks the storyboard
python make.py c1-05-the-shape-of-a-record --capture    # make missing VS Code and Command Prompt stills, then all the rest
python make.py c1-05-the-shape-of-a-record              # compose, contact sheets, Blender check, encode
python make.py c1-05-the-shape-of-a-record --no-video   # frames and contact sheets only (7 seconds)
python make.py <lecture> --capture --redo ed_top term1  # make those stills again ("all" for every one)
```

Times on the pilot: capture 12 s a VS Code still and 14 s a command (about 5 minutes for 23);
compose 7 s; Blender check and encode about 100 s for 5 minutes of video.

Once per machine, before the first capture:

```
python capture.py --setup --tool "<folder with the released sbs.pyz, sbs.bat and __lib__>" --ext "<a VS Code --extensions-dir holding the Artemis AMD add-on>"
```

That builds `R:\cosmos\courses\_work\`: a stand-in install (`Cosmos\data\missions`, with
`PyRuntime` and `PyAddons` copied from the dev install) and a throwaway VS Code profile.
If lint there prints `not checked:`, run `sbs fetch "MyMission" --update-libs` in the
stand-in once, as Lecture 3 has the student do.

## The game (separate, by hand, a few minutes)

`game.py` starts the real game on a probe mission and takes screenshots through `eng.ps1`.
It is not run by `make.py`: clicks need the game's window in front. For Lecture 5:

```
set L=c1-05-the-shape-of-a-record
python game.py %L% start                                  # hulk 9000 away: the quest is still Active
python game.py %L% click helm 0.215 0.022 helm_padd       # the handheld icon
python game.py %L% click helm 0.15 0.58 helm_log          # Quests
python game.py %L% click helm 0.085 0.167 helm_fc         # First Contact
python game.py %L% keep helm_padd game_epadd
python game.py %L% keep helm_fc game_quests
python game.py %L% stop
python game.py %L% start --patch "npc_spawn(0, 0, 9000, \"Unknown Hulk\"=>npc_spawn(0, 0, 2500, \"Unknown Hulk\""
python game.py %L% click science 0.81 0.668 sci_1         # Unknown Hulk in the list
python game.py %L% click science 0.825 0.07 sci_2         # the intel tab
python game.py %L% keep sci_1 game_science
python game.py %L% keep sci_2 game_intel
python game.py %L% stop                                   # also deletes _pic_probe
```

The `--patch` is a probe-only change: the hulk is put next to the ship so nobody has to fly.

## How it stays true

- A state is the previous lecture's `example\` plus edits that must each apply exactly once;
  a state marked `same_as` must equal the lecture's own `example` file byte for byte.
- VS Code is real: a fresh window per still, throwaway profile, the add-on running. The
  editor paints the cursor's line a set color; capture finds that band, so it knows where
  every line is. A mark on a line that is not on screen stops the run.
- A Command Prompt frame is drawn, but the command was run and the text is what it printed.
  The prompt path is the course's `C:\Cosmos\data\missions>`, not the real folder.
- Blender renders three frames first and they are compared with the composed frames;
  nothing is encoded if one is blank or different.

## What a storyboard can ask for (added for Lectures 6 to 8)

| In the storyboard | What it does |
|---|---|
| `("vscode", state, line, size, {"side": False})` | The Side Bar hidden, for a scene about the file's text. Sizes `"mid"` and `"big"` are for these stills (`"wide"` and `"close"` are the pilot's) |
| `{"file": "story.mast"}`, `{"file": "mast.runtime.log", "wrap": True}` | Another file of the folder. A wrapped line cannot be marked by its words: use `("rect", ...)` |
| a state with `"over": (folder, ...)` | Later lectures' `example\` folders (they hold only the changed files) laid over the starting folder |
| `"same_as": (file, file)` | The state must equal several files of the page's example |
| `("span", run, "words")`, `("out", run, n)` | On a Command Prompt still: those words, or the run's nth printed line, followed across a wrap. The window wraps at 100 columns, as a real one does at its width |
| `("card", "search", {"state", "word", "want": (hits, files)})` | The word counted in the state's own files (match case, whole word) and drawn plainly. A count that is not the script's stops the run |
| `("card", "page", {...})`, `("card", "points", {...})` | A sheet of prose with an editor's marks; a list of the script's own words |
| `("card", "table", {"heading", "rows": (1, 2)})` | Only those rows of a long table. A table shrinks its text until it fits |
| a beat with `"move": False` | Keeps that still from pushing in |

To type a record on screen, make a state for each line and take every still at the SAME
line number, so the window does not scroll under the new line (Lecture 8, `e_q1` to `e_q9`).

`game.py` also has `log <name>` (keeps the probe's two logs before `stop` deletes it) and
`--patch-amd "old=>new"` (a probe-only change to the fact sheet, printed like `--patch`).

## Motion, and the game's side bars

- **One kind of motion: a slow push-in.** Beats that follow each other on the same still
  are one hold. A hold with a beat of six seconds or more drifts toward the middle of its
  marks, without stopping, from its first frame to its last (0.45% a second, never past
  6%). Everything else is still. It is done by Blender (two keys on the strip's scale), so
  it costs no frames on disk; the cross-fades in and out of it are composed at the scale
  the picture has reached. `make.py` checks one moving frame against what it expects.
- **A still that is not 16:9** (the game's windows are 4:3) sits on a blurred, darkened
  copy of itself instead of black bars.

## Known limits

- Capture turns off CodeLens (`1 reference(s)` rows), sticky scroll, the minimap and
  breadcrumbs, so a student's window has a little more in it than the picture.
- Each VS Code still starts a window, which takes the keyboard focus for a moment
  (it is handed back). Do not type while capture runs.
- No typing, no scrolling, no mouse pointer: a search, a click on a tab or a key press is
  shown by its result (a drawn search card, a new still), never by the act.

## More kinds of still (added for Lectures 1 to 4)

Lectures 1 to 4 happen in File Explorer, a Command Prompt, a web browser and VS Code's
panels. Each kind below is made by `make.py <lecture> --capture`, like the others.

Once, before the first of them: `python capture.py --student` makes the stand-in look like
a student's game folder (the game's program and DLLs, `data` with its art and sound, and
Legendary Missions, Secret Meeting and Walk the Line from the dev install's committed
files). Then, in the stand-in, `sbs fetch "LegendaryMissions" --update-libs`, so that
`sbs doctor` ends `0 problems` there.

| In STILLS | What it is |
|---|---|
| `("explorer", "data\\missions", {opts})` | A REAL File Explorer window on that folder of the stand-in. `explorer.exe "<folder>"` starts it; it is found by being new and by its title; sized with SetWindowPos (1280x720, so it fills the frame at one and a half times); read with PrintWindow; closed by WM_CLOSE to that one window. No click, no key. Marks: `("part", "row:<name>")`, `"rows"`, `"address"`, `"tab"` |
| `("session", [commands], {opts})` | The commands typed into ONE real `cmd.exe` in the stand-in, so `cd` changes the prompt as it does for a student. The window is drawn; the text is the session's. Stills that name the same commands share one run |
| `("web", "https://...", {"wait": 8})` | A page drawn by headless Edge with a throwaway profile: no window. `"wait"` is real seconds before the picture is taken; without it Edge's `--screenshot` and `--virtual-time-budget` are used |
| `("web", "debug", {"state": ..., "map": "0"})` | Starts `sbs debug <mission> --map 0` in the stand-in, waits for its "GUI server started" line, lets Edge open `http://localhost:8765/`, stops it, deletes its pid file and what it left in `data\missions`. Also writes `<name>_term`: what the command had printed before the browser came, as a Command Prompt with no prompt back (declare it `("derived", "...")`) |
| `("vscode", state, line, size, {"beside": "preview"})` | VS Code's own markdown preview beside the file, in one window |
| `("vscode", ..., {"do": [[command, args...], ...]})` | VS Code commands run when the window is up: the Extensions panel (`workbench.extensions.search`), the Outline (`outline.focus`), Problems (`workbench.actions.view.problems`), an unsaved dot (`["type", {"text": " "}]`) |
| `("vscode", ..., {"trust": False})` | The folder in Restricted Mode: the band, and `AMD: trust this folder`. With `"plain": True` and `"do": [["workbench.trust.manage"]]`, the Workspace Trust page |
| `("vscode", None, line, size, {"folder": "LegendaryMissions", "file": "maps\\x.amd"})` | Another mission folder of the stand-in, as it is on disk |
| `("card", "rows", {"kicker", "header", "rows"})` | A table whose words are the storyboard's (the page's own) |
| `("card", "table", {"heading", "nth": 2})` | The second table under a heading |

Options of an Explorer or session still: `"without": ("MyMission",)` (those folders of
`data\missions` wait in `_work\_hold` meanwhile, and whatever the commands made under
their names is thrown away after: a lecture that comes before `sbs create` must not show
the folder); `"state"` (the mission's files first). Explorer also takes `"rename": {old:
new}` and `"add": {path: "file" | "dir" | "zip:<folder>"}`, both undone after the still.
A session also takes `"show": (first, last)`, `"head"` / `"tail"` (rows of a long answer),
`"banner": True` (the lines a new window opens with), `"shell": "powershell"`, `"keep"`
and a command written `(command, (answers,))` for a tool that stops to ask (`""` is Enter).
Marks on a session: `("cmd", run, "words")` for words of the typed line, `("part",
"run2:prompt")`, `("part", "end:prompt")`, and the terminal marks there were before.

How these stay true, and where they do not:

- **No key is pressed and nothing is clicked.** The `do` commands are run by a helper
  add-on (`course.picture-helper`) that exists ONLY in the throwaway VS Code profile; it
  reads the list from a file named by `PICTURE_DO`. It would show in the Extensions panel,
  so a still of that panel is filtered (`@installed Artemis`).
- **File Explorer is this machine's own, minus what is personal.** Its view, theme and
  whether file name extensions are shown are the user's settings and are not touched:
  the other state of a setting is a card. Two things keep the machine's owner out of the
  picture. (1) The window is opened on `C:\Cosmos\...` (`config.COURSE_ROOT`), a directory
  junction to the stand-in, so the address bar reads `This PC > Windows (C:) > Cosmos >
  data > missions` as the page does. Make it once per machine: `mklink /J C:\Cosmos
  "<the stand-in's local path>"`; capture stops if it is missing or leads elsewhere.
  (Take it away with `rmdir C:\Cosmos`, never `rmdir /s`.) (2) The navigation pane, which
  lists the owner's pinned folders, drives and cloud accounts, is cut out of every still:
  `wincap.pane_box` finds the pane's right edge from the window's own tree control, the
  window is looked at a second time made wider by that much, and the file list from the
  wider look is laid over the pane. Title, tab, address bar, toolbar and status bar are
  the first look's. If neither the tree nor the file list can be found, a fixed box is
  cut (372 px of 1280). LOOK at every new Explorer still all the same. Row marks are
  placed for the Details view at 1280x720: look at the frame.
- **What a tool prints is not changed, except one thing:** the stand-in's real folder is
  written `C:\Cosmos`, as the page and the drawn prompt write it (`dir`'s "Volume in drive"
  line too). A session is read in code page 1252, so a long dash pasted from a word
  processor arrives as one.
- **A wrapped file** (`"wrap": True`, as a `.md` file is in VS Code): the rows each line
  takes are worked out as the editor folds them (whole words), so a mark lands on its
  line. A mark on words that the fold splits covers the part on their first row.
- **Windows that leave something behind:** a still that shows the unsaved dot leaves a
  backup in the throwaway profile; every VS Code still deletes that folder first.
- The store apps, the VS Code installer, a word processor and every menu are cards in the
  page's own words. Nobody else's software is drawn.

The game with no arguments (Lecture 1's tour of the first screens) is not in `game.py`:
it was started by hand and clicked with `eng.ps1`, a screenshot before each click.
