# C6-10 video script - Publishing

> **STATE ON 2026-10-10.** Lint and doctor re-measured 2026-10-10 on the released tool
> `sbs` 0.14 (the doctor's count is 23 libraries for a folder with today's template
> `story.json`; it was 21). Written 2026-10-09 against `sbs`
> 0.13, the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions
> `b20726f`, the Open Universe engine library in `__lib__`). Lint and doctor were run on
> the page's own files. **Nothing was sent to anybody, nothing was fetched, nothing was
> published, and nothing ran in the real game.** The other computer's side of this
> lecture is Class 1 Lecture 12's, which was measured on a second copy of the game for a
> Class 1 mission. It was not repeated for a universe.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 8 leaves it, with `campaign.md` and `playtest.md` in the folder |
| A spare copy | The whole folder copied to Documents first. Scene 6 deletes files |
| VS Code | `MyUniverse` open, `description.yaml` in a tab, font size raised |
| File Explorer | Open at `C:\Cosmos\data\missions` |

## Confirm on camera

**By the tools, on 2026-10-09, with the page's own files:**

1. With the new `Description:` line the mission lints `clean`.
2. A hyphen in that line, and a colon in it: lint's answers are in the page's table.
3. `sbs doctor` on the folder ends with the block on the page: `1 sbslib, 23 mastlib,
   0 media`, all libraries present, and `0 problems`.
4. Copies of the mission under several folder names all linted and played, and all read
   and wrote one save file, named from the title.
5. A universe with a changed title started a new game and wrote a second save file.
6. A save was continued after the universe file had changed: added records appeared,
   rewritten ones showed new words, a deleted one was still there.
7. After lint and docs have run, the folder holds `__pycache__` and `__docs__` beside
   the seven files and the two pages.

**Read from Class 1 Lecture 12, not run again:** the zip, `sbs fetch "..."
--update-libs` on the other computer, and what goes wrong there.

**NOT seen or tried by anyone.** If one is not as the page says, stop and fix the page:

1. A host following the note. Nobody has.
2. Whether a console on another computer needs the mission folder.
3. Replacing the folder for Act Two on a host's computer with a real save.
4. Putting a kept copy of a save back.
5. The mission list, and where the `Description:` line shows on it.
6. The GitHub way. Not tried in Class 1 either.

## Scenes

### 1. Cold open

**Screen:** The zip file beside the folder, and the note.

**Say:** "Act one is written, and a table has played it. || Now it has to work in
somebody else's house. ||| You've sent a mission before, at the end of the first class.
|| A campaign's the same job, | with four differences that matter. ||"

### 2. Four differences

**Screen:** The table in Step 1 of the page.

**Say:** "A mission's played once. | A campaign's played for months, from a save. ||| A
mission's sent once. | A campaign's sent again, every time you finish an act. ||| The
title of a mission can change. || The title of a campaign names the save, so it can't.
||| And your notes are in the folder, | with the whole plot in them. ||"

### 3. The line on the list

**Screen:** `description.yaml`. Change the `Description:` line. Run lint.

**Say:** "First, say what this is. || One line in the description file. | A campaign
for one ship, act one, five evenings, version one. ||| No hyphen in that line, and no
colon. || That's the one mistake that can stop the game for everybody, | and lint
checks it for you. ||| And leave the name alone. | From the first evening on, | that
name is where the crew's save is. ||"

### 4. The folder's name

**Screen:** File Explorer. Rename `MyUniverse` to `KestrelVerge`. Open it in VS Code.

**Say:** "Next, the folder gets a name of its own. ||| I measured two things about that
name. || Nothing inside the files holds it. ||| And the save doesn't follow the folder.
| It follows the title. ||| So renaming the folder doesn't lose your save. || But two
folders with one title | are playing the same campaign, | whether you meant that or not. ||"

### 5. Three checks

**Screen:** `sbs lint KestrelVerge`. `sbs doctor KestrelVerge`. The folder's block.

**Say:** "Then the three checks, in the usual order. ||| I run lint, and it's clean. ||
Then I run doctor, | and the last block is your folder. ||| Twenty-three libraries, where your first
mission had about a dozen. || That's the universe machinery. ||| And then the walk, on a
deleted save. || And delete the save again when you're done. ||"

### 6. Take out what isn't the mission

**Screen:** The folder in File Explorer. Move `campaign.md` and `playtest.md` out.
Delete `__docs__`, `__pycache__`, the logs. Count seven files.

**Say:** "Now the step a campaign adds. || Your own pages come out. ||| The campaign
page is every act, and the ending. || The playtest page is what other crews did. ||| And
any save you kept in here | has every hidden step in it. ||| Then delete what the tools
made. | The printed bible especially. ||| Seven files are left. || Those seven are the
mission. ||"

### 7. Zip it

**Screen:** Right-click the folder, compress. `KestrelVerge.zip`.

**Say:** "Zip the folder itself, | the way you did in the first class. ||| One honest
word here. || The universe file is plain text, and it's the whole act. || A host who
opens it has read your campaign. ||| That's what a host is for. || It's the same as
handing someone the adventure to run. ||| It also means you can't be crew in your own campaign | unless somebody else is willing to read it. ||"

### 8. The note

**Screen:** The note in Step 6, scrolling slowly.

**Say:** "The note is where a campaign really differs. ||| The setup's the same three
commands as before. || Then four things only a campaign needs. ||| Start it the same way
every week, | and never choose new game. || Leave the ship's name alone if you can. || End each evening
by jumping home. || And copy the save file somewhere safe, every week. || The note
gives its name, and where it lives. ||"

### 9. Act two

**Screen:** The table in Step 7.

**Say:** "When act two's ready, you send the folder again, | and there are three rules. ||| The title
doesn't change, not by a letter. || Nothing the crew has met is deleted or renamed, |
because you only ever add. ||| And act two has to be opened by a step they haven't finished yet. |
The capstone shows you how. ||| The host swaps the folder. || The save isn't in it, | so the
crew carries on. ||| And before you send it, check it yourself. | Start the new folder on your own save from the end of act one, | and see that the first new lead is there. ||"

### 10. Close

**Screen:** The checkpoint list.

**Say:** "So that's a release. | A named folder, a clean zip, and a note. ||| The
capstone's next, when it's written. || And everything it'll ask of you | is already on
your campaign page. ||"
