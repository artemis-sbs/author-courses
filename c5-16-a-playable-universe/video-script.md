# C5-16 video script - Capstone: a playable universe

> **STATE ON 2026-10-09.** Written and measured against the released tools: `sbs` 0.13,
> the published v1.4.0 libraries (sbs_utils `4941820e`, LegendaryMissions `b20726f`, the
> Open Universe engine library built 2026-10-08). The whole session on the page was
> walked by script in the game's stand-in (the mock), in two runs with the save kept
> between them, from a copy of the mission placed where its save cannot reach a
> player's own. The script selected stations, pressed Comms buttons by their text, sent
> the Quest Log's Engage for each lead, and told the game "the ship destroyed this" four
> times. No weapon fired and no console was connected. **Nothing in this lecture has
> been run in the real game, and nobody has seen any of its screens.**

The companion page is `lesson.md`; the finished `kestrel_verge.amd` is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 13 leaves it: `story.mast` matches `c5-13-battles-part-2\example\`; `kestrel_verge.amd` and `settings.yaml` match `c5-12-battles-part-1\example\` |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | `MyUniverse` open, `kestrel_verge.amd` in a tab, font size raised |
| Paper | The table from Step 1, printed, and a pen |
| Game | Closed. Started on camera twice, in scenes 5 and 7, with `sbs run server,helm,comms,weapons -m MyUniverse map=0` (Weapons is needed for the last row) |

## Confirm on camera

**In the mock, by script, on 2026-10-09, with the page's own files:**

1. With the session card added, lint gives the three `ledger_read` warnings (the third
   now on line 230) and nothing else.
2. First sitting, a new game: every "You should see" of rows 1 to 12, as text the game
   was asked to send. Credits 500, 400, 700, 750. Standing with Hollin 20 after the
   levy and 25 after the escort; with Deepwell 20 after the fee. 142 labels run, an
   empty `mast.runtime.log`.
3. Second sitting, the same save: the game says Continue, the ship is at 3, 1, credits
   750, the Quest Log as it was left.
4. Engage on What the Gleaners Keep: the ship is at -4, -3; four cards are sent (the
   Gleaners' greeting, the guards' Threat card, the charted card and ours); credits
   1150; eleven hostile ships, four of them the battle line.
5. Four Gleaner kills reported: the game says game over, a win, with the `Win:`
   sentence, and sends a card titled VICTORY with the `Citation:` sentence.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. Row 18, for real: four Gleaner ships destroyed by a crew, the VICTORY card, the end
   screen. If one light cruiser cannot do it, lower the tier on Lecture 13's card and
   say so on camera.
2. Every button's exact text on Comms. The page prints them as the game was asked to
   send them. `Escort (300 cr)` was sent with two spaces before the bracket.
3. Whether the arrival card and the Threat cards overlap or queue on a console.
4. Continue from a real save, with `map=0`.
5. The Anomaly Signal job at The Tern. It depends on the game's seed, and may not be
   there.
6. How the crew reaches Kestrel Traffic. Still unknown since Lecture 9.

## Scenes

### 1. Cold open

**Screen:** The end-of-game screen with the `Win:` sentence. Then the printed
run-through table, every row ticked.

**Say:** "This is the last lecture of the class, | and it doesn't teach you anything
new. || It asks you to finish. ||| By the end you'll have played one whole evening | in
your own universe, with a list in your hand, | and you'll know that every part of it
works. || You'll also know, honestly, what doesn't. ||"

### 2. Plan the evening

**Screen:** The table in Step 1 of the page, on paper. Point down the Place column.

**Say:** "Don't start the game yet. || Write down where a crew will go, in order, | and
what should happen at each place. ||| I've got six rows, in two sittings. || The relay,
the Tern, and the Assay Office. || Then they save, and come back another night | for
the Bone Pile. ||| I follow three rules. || Three places make an evening. || End a
sitting somewhere safe, | because the save keeps the system the crew is in. || And put
the save between the mystery and the fight, | so they leave knowing where to go next.
||"

### 3. The session card

**Screen:** `kestrel_verge.amd`, the very top. Type the session card.

**Say:** "Now, ten lines of notes at the top of the main file. || Two slashes start a
note, so the game doesn't read these. | They're there for people. ||| Who the game is for, and
the three dials from the battles lecture. || The budget for my worst system, | and then the two
sittings. ||| And the most useful part, the words. || These are the words that have to
match in two places, | and lint can't check any of them for me. || So when I rename
something, | this is my list of where else to go. ||"

### 4. Before you play

**Screen:** `sbs lint MyUniverse`: three warnings. The saves folder, with no save in
it. `settings.yaml` line 53. The two card lines in `story.mast`.

**Say:** "There are four checks before I play. || Lint gives the three warnings we know
about, and no others. || The save is gone, | because a run-through starts from a new
game. || The dials say what my card says. || And the libraries are up to date. ||"

### 5. The first sitting

**Screen:** `sbs run server,helm,comms,weapons -m MyUniverse map=0`. Play rows 1 to 12
of the page, ticking the paper after each: the Quest Log; the hail and the levy; the
escort; The Tern and its Threat card; the Assay Office; the question; the Quest Log.

**Say:** "Here we go, and I tick each row as it happens. ||| There are three leads in
the Quest Log. || On Comms, I hail the Compact and pay the levy. || Now there's more
work on offer, and the escort pays better, | so I take it. ||| On to the Tern. || There's
her card, and there's the warning from the battles lecture. || The first lead is done,
and a new step has appeared. ||| Now the Assay Office. || The escort pays out as I
arrive. || I ask about the Tern, and pay the fee. | That closes the step, | and it tells
the crew where to go next. ||| That's twelve rows, and twelve ticks. ||"

### 6. Close it

**Screen:** Close all four windows. The saves folder: the save is there now.

**Say:** "And now I close the game, on purpose. || This is the part of an open universe
that a single mission doesn't have. || There's the save, and I'm going to leave it alone.
||"

### 7. The second sitting

**Screen:** The same command. The ship at Assay Office. The Quest Log. Engage What the
Gleaners Keep: three cards. Science: the contacts. The fight. The VICTORY card and the
end screen.

**Say:** "I start it with the same line, | and we're back at the Assay Office, with
the same credits. || The Quest Log is just as I left it. ||| Now for the place the
Gleaners won't talk about. || Three cards come up. | The place, the guards, and the
one I wrote. ||| I count eleven ships. || Four of them are a long way off, | three are
by the wreck, | and four are right in front of me. || That's the battle line from last
time. ||| I have to tell you something about this last row. || When I checked this
page, | a script told the game the four ships were destroyed. || Nobody has fought
this fight. || So this is the first time, and we'll find out together. ||"

### 8. After you play

**Screen:** `mast.runtime.log`, empty. The ticked table. Then the table in Step 7 of
the page.

**Say:** "There are three things to read afterward. || The runtime log, which should be
empty. || Your ticks, every one of them. || And your standings, which should match the page. ||| And then
there's one more table, | the things this universe doesn't do yet. || It has no admiral
of its own. || A story beat can't move standing. || Lint has three warnings that are
wrong. ||| None of those is your mistake. || But a writer who knows them | writes
around them, and that's why they're on the page. ||"

### 9. Your turn

**Screen:** The rubric on the companion page. Then the exercise.

**Say:** "Now it's your turn, | and this time it really is yours. || Plan two
sittings, and write your card. || Write down what you should see before you play, | from
your own files. ||| Then give it to a crew, | sit behind them, and don't help. |||
That's a whole universe, and you wrote it. || Well done, and thank you. ||"
