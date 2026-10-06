# C2-10 video script - A Siege boss, part 3

> **CHECKED IN THE REAL ENGINE, 2026-10-04 (server only, by script, from a probe copy of
> LegendaryMissions; the boss picked by the `BOSS_SELECT` setting).** She arrived with both
> named ships and seven escorts; the tree read `sink_morrigan=ACTIVE sink_badb=ACTIVE
> reserve=ACTIVE sink_nemain=SECRET`; the hook's Nemain arrived 8 s later at (0, 0, 28000)
> and Her Reserve completed, revealing Sink the Nemain; a REAL kill of the Nemain (84 s of
> fire) completed that objective and paid 400. So `Done when: destroy 1 <role>` does
> complete in the engine. The run was stopped at five minutes with the Badb still alive
> (the probe's gunner was slow), so the full win and the 1,800 total were NOT reached in
> the engine. `mast.runtime.log` empty. Nothing was looked at on a console.
>
> **Changed since this script was written (LegendaryMissions `1fec027`):** a `Hook:` that
> names a label the mission does not have no longer stops the game. She arrives without
> it and `mast.runtime.log` says so. The page's tables and "Keep your work safe" are
> updated; re-cut the scene that showed the error page.
>
> **DECISION WAITING ON THE USER (B87):** an author's hook has no home that an update
> leaves alone.

> **NOT CHECKED IN THE REAL ENGINE, and nothing here has been seen on a screen.**
> Everything was measured on 2026-10-04 in the mock: real Siege games played headless,
> one at a time, with the packaged library (sbs_utils `488df12c`, LegendaryMissions
> `abab230`). Games with no hook file were played from the real LegendaryMissions folder.
> Games with the hook file were played from a copy of LegendaryMissions as a student has
> it (`data\missions\_c210_probe`), because the pilot could not add a folder to the real
> one. The boss was chosen by the `BOSS_SELECT` setting. Nobody fired a shot: a ship was
> "sunk" by a script that tells the quest system of the kill the way the engine does,
> then removes the ship. The mock's own kill cannot finish a `destroy` objective; the
> engine's can (Lecture 9's engine check).

Target length: 22 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| `common_data\bosses` | Holds `corsair_queen.amd` exactly as Lecture 9 finished it (`c2-09-siege-boss-fields\example\corsair_queen.amd`). Nothing else |
| LegendaryMissions | A clean v1.4.0 folder, `abab230` or later. No `corsair_queen` folder in it yet |
| Library | sbs_utils `488df12c` or later, built into `__lib__` |
| Tools | An `sbs` that lints a shared folder (sbs_cli `fd357ee` or later). On 2026-10-04 the downloaded `sbs.pyz` does not: every lint result on the page was produced by running the CLI from source. `sbs compile` in the downloaded `sbs.pyz` is the one the page was checked with |
| VS Code | The `data\missions` folder open, Artemis AMD extension installed, font size raised |
| Tabs | `corsair_queen.amd`; `LegendaryMissions\maps\siege_quests.amd` for scene 3 |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. It is started and restarted on camera. Siege, Difficulty 5, one player ship. A second person on Weapons helps for scenes 4 and 11 |
| A copy | A spare copy of the finished `corsair_queen` folder, outside LegendaryMissions, for scene 12 |

## Confirm on camera

Each item says how it was checked. If one fails on camera, stop and fix the page.

1. With `Done when: destroy 1 morrigan`, sinking the Morrigan completes the objective and
   pays 600 at that moment, and the game is not won until every raider is gone. (Mock,
   scripted kill: objective COMPLETE, side credits 600, then 1,100 at the win. The
   engine's own kill completing a `destroy` objective was seen in Lecture 9's check, not
   in this one.)
2. Sink the Badb pays 300 and is not needed to win. (Mock: 1,400 with it, 1,100 without.)
3. With `Fails when: 30 seconds`, `Fatal: true` and `Lose:`, the game ends about thirty
   seconds after she arrives, with the sentence. (Mock: arrival at 4.5 s, the end at 37.8 s,
   `The Morrigan broke the line. The sector is hers.`, side credits 500.)
4. With a `Win:` line, the game ends the moment the Morrigan is sunk, with that sentence.
   (Mock, scripted kill: ended in the same tick, 36 raiders still counted.)
5. `Hook: biomech_infestation` brings BioMechs with her. (Mock: six objects with the role
   `biomech` three seconds after the arrival in two games, eight in a third. What a
   BioMech looks like, and how many are in view, is unseen.)
6. A folder `corsair_queen` holding `__init__.mast`, inside LegendaryMissions, is read.
   (Mock, in the copy: the label ran. The compiler walks the mission folder for files of
   that name; read in `sbs_utils\mast\mast.py`, `find_imports`.)
7. The smallest card tells the crew `The Corsair Queen has entered the sector.` as she
   arrives. (Mock: the text sent to the player ship at 4.4 s. WHERE a crew reads it - which
   console, which panel - is unseen. Find it before recording scene 8.)
8. Ten seconds after her arrival the Nemain is on the map at 0, 0, 28000, with the roles
   `boss`, `nemain`, `raider`, and she moves. (Mock: there at the next look, 400 units away
   eight seconds later. What she looks like and what she attacks are unseen.)
9. Her Reserve completes as the Nemain arrives, and Sink the Nemain appears then and not
   before. (Mock: `reserve` ACTIVE then COMPLETE; `sink_nemain` SECRET then ACTIVE.)
10. The whole finished pair, with the real numbers: arrival at 6 raiders of 16 (40%), the
    sentence, the Nemain 90 seconds later, 1,500 credits at the win with the Badb left
    alone, 1,800 with all three. (Mock, in the copy.)
11. `sbs lint common_data\bosses` prints the three `clean` lines, and `sbs compile
    LegendaryMissions` prints nothing. (Lint: CLI from source, read against the copy that
    holds the hook. Compile: the downloaded `sbs.pyz`, on the copy.)
12. With one letter changed in the `Hook:` line, both checks are silent and the game stops
    with an error as she arrives. (Mock: a page-level runtime error, `Calling undefined
    label`, and game time stopped. Her ships and objectives were already there. The error
    page itself is unseen.)
13. With a quote mark missing in the card, `sbs compile LegendaryMissions` names the file
    and the line, and LegendaryMissions starts nothing. (Compile: seen. Mock: the story
    ran 0 labels. What the game shows is unseen.)
14. The quest list wording: `Quest complete: ...`, `Mission complete: Sink the Morrigan`,
    `Mission failed: ...`. (Mock: the text sent to the player ship.)

Not checked at all: how the quest list draws four objectives and an `Objective:` line; how
a new objective is noticed by a crew; what a deadline looks like on any console; whether
the editor underlines any of the mistakes in scene 10.

Also capture the screenshot the page asks for.

## Scenes

### 1. Cold open (0:00 - 0:40)

**Screen:** The game. The Queen arrives; the red sentence; the quest list with three
objectives. Cut to the Nemain arriving. (Reuse footage from scene 11.)

**Say:** "This is the Corsair Queen after today. The crew is told she is here. They have
ten minutes to sink her flagship. There is a bonus for her second ship. And ninety seconds
in, a third ship she was holding back. Three of those are lines you already know. The last
is one card."

### 2. The test setting (0:40 - 1:10)

**Screen:** `corsair_queen.amd`. Change `Low: 40%` to `Low: 100%`.

**Say:** "Same as last time. Low one hundred percent, so she arrives four seconds in. We
put the real number back at the end."

### 3. How a Siege ends (1:10 - 3:00)

**Screen:** `LegendaryMissions\maps\siege_quests.amd`. Highlight each of the four records
in turn, then the `Parent: siege_mission` line in `corsair_queen.amd`.

**Say:** "Before we change her story, read the Siege's own. Four quests. Repel the Siege
is the top: finish it and the game is won. Break the Siege is required, and it is done
when every raider is gone. The other two are the ways to lose. Now look at your
objective. Parent, siege mission. That line hangs it on this tree. Required true means
one more thing the crew must finish before they win. Leave Required off, and it is extra."

### 4. Destroy one morrigan (3:00 - 5:00)

**Screen:** Replace the `Done when:` line with the `Objective:` and `Done when:` lines.
Show the roles table from the page. Restart, choose the boss, sink the Morrigan (cut the
fight), show the objective complete.

**Say:** "Sink the Morrigan has never meant sink the Morrigan. It meant destroy
everything. One line fixes it: done when, destroy one morrigan. Morrigan here is a role.
Every named ship gets its own name, in small letters, as a role. And I add an objective
line, the sentence the crew reads. Now the objective is done when she is, and the reward
is paid right then. The game is not over yet: Break the Siege still wants every raider."

### 5. A bonus (5:00 - 6:10)

**Screen:** Type the Sink the Badb record at the end of the file.

**Say:** "A second objective. Two hashes, like the first. Destroy one badb, three hundred
credits. And no Required line. So it is a bonus: pay if they do it, win if they do not."

### 6. A way to lose (6:10 - 8:40)

**Screen:** Add the three lines with `30 seconds`. Restart, choose the boss, sit still.
The game ends. Then change to `10 minutes`, and change the `Objective:` and description
lines.

**Say:** "Now a clock. Three lines, and they go together. Fails when, thirty seconds: a
test number. Fatal true. And Lose, with the sentence the crew will read. I start the game
and do nothing. Thirty seconds after she arrives... there. My sentence. Now the real
number, ten minutes. One more thing. Nobody warns the crew about this clock. So I say it
where they will read it: in the objective, and in the description."

### 7. Another ending (8:40 - 9:50)

**Screen:** Add the `Win:` line. Restart, sink the Morrigan (cut the fight), the game
ends at once. Delete the line. Show the three-row table from Step 6.

**Say:** "One more line an objective can have. Win, and a sentence. Now the game is won
the moment she sinks, whatever else is flying. For some bosses that is the right ending.
Not for this one, because of what is coming. So I take it out again. Required, Win, and
the three lines for losing: those are your three endings."

### 8. A hook that is already written (9:50 - 11:10)

**Screen:** Add `Hook: biomech_infestation` under `Named:`. Restart. BioMechs with her.

**Say:** "Some things no line can say. For those a boss has a hook: a named block of
script that the Siege runs once, when she arrives. One comes with the game. Hook, biomech
infestation. And there they are. I wrote no script. But BioMechs are not her story."

### 9. Her own hook: the folder, the file, the smallest card (11:10 - 14:10)

**Screen:** In the file list: right-click `LegendaryMissions`, New Folder,
`corsair_queen`. Right-click it, New File, `__init__.mast`. Paste the three-line card.
Change the `Hook:` line. Run both commands. Restart; the sentence appears.

**Say:** "Her own hook is a label, and a label lives in a mast file. Here is the awkward
part. Her boss file is in common data, where updates never touch it. A hook cannot go
there. It has to be inside LegendaryMissions. So I make a folder of my own in there,
corsair queen, and one file in it. The name is exact: two underscores, init, two
underscores, dot mast. The game reads every file with that name."

"The card. A label: three equals signs and a name. One line that says a sentence to
every crew ship. And END. Back in the boss file, Hook, and the same name. Both checks:
lint, clean; compile, nothing. And when she arrives, the crew is told. Until now nothing
told them a boss had come."

### 10. The reserve (14:10 - 17:30)

**Screen:** Add the four lines to the card. Show the "change four things" table. Then
type the two objectives at the end of the `.amd`. Highlight `Then: reveal sink_nemain`
and `Starts when: revealed`.

**Say:** "Now the card does more. Wait: you know this one. Ten seconds for testing. Then
a guard: if the game is over, stop. Then the ship line. It is long, and it is one line.
You change four things: where, her name, her ship key, and her role, which is her name in
small letters. Last, finish a step: your other card, with a signal name."

"And two objectives. Her Reserve is done when that signal comes, and then it reveals
Sink the Nemain, which is hidden until then. Two traps. In your mission an address was
arc, slash, step. Here it is the key alone. And a hidden step has no State active line."

### 11. Check it, play it (17:30 - 19:40)

**Screen:** Both commands. Restart. The sentence; three objectives; ten seconds; the
Nemain; `Quest complete: Her Reserve`; Sink the Nemain in the list.

**Insert:** Change one letter in the `Hook:` line. Both commands: silent. Restart: the
game stops as she arrives. Undo.

**Say:** "Lint, clean. Compile, nothing. Four seconds: she is here, and so is the
sentence. Three objectives. Ten seconds... the Nemain, and a fourth objective. Now the
mistake nothing catches. One letter wrong in the Hook line. Lint is happy. Compile is
happy. And the game stops when she arrives. So check that word by eye, every time."

### 12. Real numbers, and keeping it safe (19:40 - 21:20)

**Screen:** `Low: 40%`; `delay_sim(90)`; the note at the top. Both commands. Then, in the
file list, copy the `corsair_queen` folder to a folder outside LegendaryMissions.

**Say:** "Testing is over. Forty percent, ninety seconds, and the note brought up to
date. One last thing, and it matters. Her boss file is safe from updates. Her hook is
not: it is inside LegendaryMissions, and an update replaces that folder. Then she is
still in the list, and the game stops when she arrives. So keep a copy of this folder
outside, and put it back after every update."

### 13. Your turn (21:20 - 22:00)

**Screen:** The exercise on the page.

**Say:** "Your own boss now. An objective that means what it says, a bonus, a clock, an
ending you chose, and one sentence when it arrives. Next time she gets a voice."
