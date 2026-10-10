# C6-2 video script - What the game remembers

> **STATE ON 2026-10-10, evening.** Written that morning against `sbs` 0.13 and the
> libraries of the day (sbs_utils `ae05dac7`, LegendaryMissions `b37a320`, saves version
> 2). Re-measured the same evening on the released tool `sbs` 0.14 and libraries
> (sbs_utils `ed811ecb`, LegendaryMissions `cc9cd06`, Open Universe `80e9397`): lint on
> the finished file and on all 17 variants, and two plays of a step with two `Then:`
> actions (two lines; one line with a comma). Both now reveal AND teach. A save filled
> with nonsense was Continued once: the game did not start, the file was unchanged, and
> a copy ending `.unreadable.bak` was beside it (a row under "If something goes wrong").
> The other plays were not run again. Everything was run by script
> in the game's stand-in (the mock), from copies of the mission placed where their save
> cannot reach a player's own. A script pressed the Comms buttons by their text and sent
> the Quest Log's Engage. **Nothing in this lecture has been run on a real console, and
> nobody has seen any of its screens.** In the real game's server, with no console
> attached, a Class 6 campaign was played, closed and continued on this save format
> (same credits and steps, no story text in the file).

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 1 leaves it (`c6-01-from-one-session-to-twenty\example\`) |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` and no `..._2.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | `MyUniverse` open, `kestrel_verge.amd` in a tab, font size raised |
| Game | Closed. Started on camera in scenes 6 and 7 with `sbs run server,helm,comms -m MyUniverse map=0`, and in scene 9 without `map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-10, with the page's own files:**

1. The finished file lints `clean` and plays with no errors and an empty
   `mast.runtime.log`.
2. Before anything is learned the Compact's hail gives three answers. At the Gleaners'
   yard the hail gives three, one of them Ask what became of the Tern's boats. After
   that answer the fact is known, and is in the save at once.
3. Back at Kestrel Relay the Compact's hail has a fourth answer, Report what the
   Gleaners said. Pressed with one fact known, the line is "Entered. One boat, broken
   for her cells..."; after The Second Colony is done, "Entered. And the Assay Office
   buys what the Gleaners break...".
4. A second launch with the same save: the ship at 0, 0, credits 700, standing 25, both
   facts known, the fourth answer still offered, the second line still said.
5. The save's last five lines are the two facts. No story step's title or text is in the
   file. A job's is.
6. With probe-only records added to a copy: a step that failed on its clock was in the
   save as failed, penalty paid, within seconds and with no jump; a clock with 258
   seconds left came back with 275; a ship renamed in `settings.yaml` (two ships in the
   game) kept its standing and its job; a title change wrote a second file and left the
   first; three guards not destroyed were there again.
7. A game started in slot 2 wrote `universe_save_the_kestrel_verge_2.yaml` and left the
   first file the same size. A start with New Game left
   `universe_save_the_kestrel_verge_1.yaml.previous.bak`, the size of the old campaign.
8. After a `Win:` step was finished and the game started again: one card titled
   Campaign won, the game not over, the ship able to jump.
9. Step 5's tables: 17 one-change variants linted (again on the evening's tool), 8 of
   them played. On the evening's tool `if learnt`, `if knows` and a guard with no curly
   brackets are warnings, and two `Then:` actions are `clean` and both happen.

**Read in the game's guide, not run:** a hail nobody answered does not call again;
ordinary loot in a ruin returns; a ship arrives at the edge of its system.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. Every screen, and first of all the **Save Slot** dial on the start screen. The slot
   was set by a line in `story.mast` for the measurement.
2. The Campaign won card on a console.
3. Whether an answer that is not offered is absent or greyed out.
4. Putting a `.previous.bak` file back.

## Scenes

### 1. Cold open

**Screen:** The Compact's hail on Comms, with Report what the Gleaners said among the
answers. Then the last five lines of the save file.

**Say:** "Last time, the game remembered steps, standing and credits, and nothing
else. ||| If your story turned on something the crew found out, | you had to fake it.
||| Today the game learns to remember what the crew knows. || And you'll see exactly
where it writes that down. ||"

### 2. What a fact is

**Screen:** The table in Step 1 of the page.

**Say:** "A fact is a few plain words that you choose. || The Gleaners broke a boat. |||
The crew either knows it, or doesn't. || You write it where they learn it, | and again
wherever the story asks. ||| There are two ways to learn. | An answer in a hail, or
finishing a step. || And two ways to ask. | On an answer, or on a line. ||| A fact
belongs to the whole game, | and it doesn't move anybody's standing. ||"

### 3. Learned by finishing a step

**Screen:** `kestrel_verge.amd`, The Second Colony. Add the `Then: learn` line.

**Say:** "First, a fact from a step. || This is one of my old leads, the second colony.
|| I add one line. | Then, learn, and the words. ||| A then line can do more than one
thing. || Put a comma after the first, | and write the second. || So a step on your
spine can reveal the next step, | and teach a fact as well. ||| This lead only teaches,
so one is enough. ||"

### 4. Learned in a hail

**Screen:** The Gleaner hail. Add the answer with `; learn`. Then the new record at the
end of the file.

**Say:** "Second, a fact from a hail. || The Gleaners get a new answer. | Ask what
became of the boats. ||| After the semicolon, where a cost or a deed would go, | I write
learn, and the fact. ||| And the answer needs somewhere to lead, | so I add their reply
at the end of the file. ||"

### 5. Asking what they know

**Screen:** The Hollin hail: the answer with `if learned`. Then The Report, with its two
guarded lines. Save. `sbs lint MyUniverse`: clean.

**Say:** "Now the Compact asks. || A new answer, report what the Gleaners said. | And
after it, if learned, and the same words. ||| A crew that never asked the Gleaners
never sees this answer. ||| The reply has two lines. || One for a crew that's been to
the assay office, | and one for a crew that hasn't. || I guard both of them, | because a line
with no guard can always be said. ||| I save, and lint says clean. || And lint does read
facts. | Misspell one, and it tells you which. ||"

### 6. Play it

**Screen:** Run the game. Steps 1 to 5 of Step 6: the levy and the Escort; The Breaking
Yard and the question; home, and the report; The Second Colony; home, and the report
again.

**Say:** "Let's play it, then. || I pay the levy and take a job, | then I go to the breaking
yard and ask about the boats. ||| Now I go home. || There's the new answer, | and the
Compact gives me the first line. ||| Out to the second colony. || Nothing on the screen
says I've learned anything. | A fact is silent until something asks for it. ||| Home
once more, and I report again. || And now it's the second line. ||"

### 7. Stop, and come back

**Screen:** Close every window. Run the same line. Hail the Compact. Then the table in
Step 6.

**Say:** "Now I close the game, all of it, | and I start it again. ||| The answer's
still there, | and the line is still the second one. || The crew still knows both
facts. ||| Same system, same credits, same standing. ||"

### 8. Inside the save

**Screen:** The save file in VS Code. The last five lines. Then a step under
`shared_quests`. Search for `The Long Count`: nothing found.

**Say:** "Here's where it's kept. || The last five lines of the save | are what the
crew knows. ||| And look at a step of the story. || A key, and a state. | No title, and
no text. ||| I search for the name of my campaign, | and it isn't in here. ||| So the
save isn't a spoiler. || And when I change a step's words between evenings, | the crew
gets the new words. ||"

### 9. Slots, and a campaign that was won

**Screen:** Start without `map=0`. The start screen, the Save Slot dial set to two. The
saves folder with two files. Then the table in Step 10.

**Say:** "There are two more things. || The number at the end of the save's name is its slot, |
and there are six. ||| Each slot is its own campaign, in its own file. || So two tables can
play one universe, | and you can keep a slot for your own walks. ||| And a campaign
that's been won isn't a dead save. || Continue it, and the crew gets one card saying
so. || Then they fly on. ||"

### 10. Your turn

**Screen:** The whole list in Step 8, then the exercise.

**Say:** "The whole list of what's kept is on the page, | and every row of it was
measured. ||| Now it's your turn. || Write one fact the crew learns by asking, | and
one they learn by going somewhere. ||| Put an answer behind the first, | at a station
they can always get back to. || Then stop the game, come back, | and check they still
know. ||"
