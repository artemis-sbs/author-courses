# C6-9 video script - Revising between sessions

> **STATE ON 2026-10-10.** Written and measured against the released tools: `sbs` 0.13,
> the published v1.4.0 libraries (sbs_utils `ae05dac7`, LegendaryMissions `b37a320`, the
> Open Universe libraries of 2026-10-09, saves version 2). Everything was run by script
> in the game's stand-in (the mock), from copies of the mission placed where their save
> cannot reach a player's own. One campaign was played two evenings in, then continued
> six times, with the universe file changed before each. A script pressed the Comms
> buttons, sent the Quest Log's Engage, and told the game "the ship scanned this" and
> "the ship destroyed this". **Nothing in this lecture has been run in the real game,
> and nobody has seen any of its screens.**

The companion page is `lesson.md`. `example\` holds the lab's files as Step 6 leaves
them: they belong in `RevisionLab`, not in `MyUniverse`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 8 leaves it. It is copied on camera, and never changed |
| Saves | No `universe_save_the_kestrel_verge_6.yaml` in `data\missions\common_data\saves`. The slot 1 save may be there: the point of the scene is that it is not touched. Note its size before recording |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | Empty window, font size raised |
| Game | Closed. Started on camera six times with `sbs run server,helm,comms,science,weapons -m RevisionLab map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-10, with the page's own changes:**

1. With evenings 1 and 2 walked: the ship at 0, 0, credits 1050, standing with Hollin
   20, six steps Done, Three of Five open, the Escort in hand.
2. Round one, linted: two warnings, `dangling-reveal` and `never-revealed`, both from
   the deleted step. Continued: the reworded open step and the reworded finished step
   show their new titles; the added lead is Active; the deleted step is gone and the
   game reports it parked; the step renamed with `Was:` is Done under its new key; the
   step renamed without `Was:` is hidden under its new key and its old key is parked;
   the step added behind a finished one is hidden.
3. Round two, continued: the record put back is Done again; the hidden step given `at
   once` is still hidden; with the open step deleted, The Plover's Price is hidden and
   the Quest Log has no open step of The Long Count.
4. Round three, continued: `State: active` on the stranded step leaves it hidden. The
   same record under a new key with `at once` is Active (measured for The Dunlin's
   Lockers, then for The Plover's Price).
5. In the same launches: the ship renamed in `settings.yaml` kept its standing and its
   job; the Narrative chapter moved to `story.amd` kept every state.
6. With the title changed: a new campaign in a new file, and the old file the same
   size.
7. Three guards at the Wren, not destroyed, were there again after Continue.

**Read in the game's guide, not run:** that a changed `Done when:` is used from then on;
`Was: a, b`.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. Every screen. The Quest Log is described from the list the game hands a console.
2. The lab in slot 6 with a real save. In the stand-in the rounds were played in slot 1
   of a private saves folder; slot 6 was measured separately, by continuing a copy of
   that save.
3. A real scan of the Wren and two real kills in Step 3. If the walk takes more than
   ten minutes on camera, cut to the result table.
4. That the slot 1 save is the same size at the end of the recording.

## Scenes

### 1. Cold open

**Screen:** The Quest Log with no open step of The Long Count. Then the same Quest Log
with The Plover's Price back in it.

**Say:** "This is a campaign with nowhere to go. || The crew finished evening two, | and
then I tidied my file. ||| I deleted one step, the one they were on. || And everything
after it is hidden, | with nothing left to reveal it. ||| By the end of this lecture
you'll know how that happens, | how to get it back, | and how to never do it to a real
crew. ||"

### 2. Two halves

**Screen:** The save file from Lecture Two beside `kestrel_verge.amd`. Highlight a key
in each.

**Say:** "Here's the whole idea, in one sentence. || The save holds what the crew
did. | Your file holds what there is to do. ||| The save has no words in it. || It has
keys, and a state for each key. ||| So every time the game starts, | it joins the two
halves by key. || Change your words, and the crew sees new words. || Change a key, and
the save doesn't know that record any more. ||"

### 3. Make the lab

**Screen:** File Explorer: copy `MyUniverse`, rename the copy `RevisionLab`. VS Code:
`story.mast`, the new line under the title line. `sbs lint RevisionLab`.

**Say:** "We don't practice on a live campaign. || So I copy the folder, | and I call
the copy revision lab. ||| Now, the copy has the same title, | and a save is named for
its title. || Left alone, the two folders would share one save. ||| So I add one line to
the lab's story file. || Save slot, equals six. ||| Now the lab keeps its own campaign,
in its own file, | and mine is somewhere else entirely. ||"

### 4. A campaign in progress

**Screen:** Run the lab. The walk: the levy, the Escort, evening one, evening two. Then
the table in Step 3 of the page.

**Say:** "The lab needs a campaign that's partway through. || So I walk two evenings, as
fast as I can. ||| And here's where it stands. || Six steps are done, | and one is open, three
of five. || Everything after that is hidden. | And there's a job in hand. ||| Now I close
the game, | and I start changing things. ||"

### 5. Round one

**Screen:** `kestrel_verge.amd`. The seven changes of Step 4, each highlighted as it is
made. Then lint, with its two warnings. Then the game, and the Quest Log.

**Say:** "Seven changes, all at once. ||| I reword the step they're on, | and one
they've finished. || I add a lead, | and I delete a finished step. ||| I rename a step the
right way, | with a line that says what it was called before. || I rename another the
wrong way, with no such line. || And I add a new step behind one that's already done.
||| Lint has two warnings, | and both are about the step I deleted. || It's telling me
I've cut my spine. ||| Now I continue the game. || There are new words in both places, | and the new
lead is there. || The deleted step is gone. || The step I renamed properly is still
done. || The one I renamed badly has vanished. | And the new step behind a finished one
never shows up. ||"

### 6. Round two

**Screen:** Put the deleted record back. Change the hidden step to `at once`. Delete the
open step. Continue.

**Say:** "In round two, I put the deleted step back, | and it comes back done. || The
save had kept its state for me. ||| I tell the hidden step to start at once, | and it's still hidden. || The save
remembered it as hidden, and the save won. ||| And now the
accident. | I delete the step the crew is on. ||| The step after it is stranded. || No
next lead, in a campaign somebody has put weeks into. ||"

### 7. Getting it back

**Screen:** Step 6 of the page. Try `State: active`: still hidden. Then the new key with
`at once`: the step is in the Quest Log.

**Say:** "The game's own guide has a cure for this. || I tried it, and it didn't work.
||| What does work is a new key. || The save decides the state of every key it's seen.
| Your file decides the state of a key it hasn't. ||| So I give the stranded step a
key the save has never met, | and I tell it to start at once. ||| And there it is, back
in the quest log. ||"

### 8. The list

**Screen:** The table in Step 8, top to bottom. Stop on the last row.

**Say:** "So here's the list. || Reword anything you like. || Add leads, and add steps
ahead of the crew. | That's just writing the campaign. ||| Rename a key only with the
line that says what it was. || Never add a step behind one that's finished. || Never
delete the step they're on. ||| And never, ever change the title. | That's a different
campaign. ||"

### 9. Your turn

**Screen:** The exercise. Then the saves folder, with the slot six file being deleted.

**Say:** "Now it's your turn. || Make a lab from your own campaign. || Strand a step on
purpose, | and bring it back both ways. ||| Then write three rules on your campaign
page, | the three things you'll never do to a file a crew is playing. ||| Next time, we
pack the whole thing up and send it out. ||"
