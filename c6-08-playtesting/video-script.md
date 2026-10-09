# C6-8 video script - Playtesting

> **STATE ON 2026-10-09.** Written and measured today against the released tools: `sbs`
> 0.13, the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions
> `b20726f`, the Open Universe engine library in `__lib__`). Everything was run by script
> in the game's stand-in (the mock), from a copy of the mission placed where its save
> cannot reach a player's own. **Nothing in this lecture has been run in the real game,
> nobody has seen any of its screens, and no table of people has played this campaign.**
> The save file shown is a real one, written by the stand-in at the end of a scripted
> walk through Act One. The advice about running a table is advice.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 7 leaves it: both files match `c6-07-mixing-the-play-styles\example\` |
| Saves | A save from a walk through Act One, to open in scene 6. Then deleted before scene 9 |
| VS Code | `MyUniverse` open, font size raised |
| Browser | Ready to open the bible page in scene 3 |
| Game | Closed. Started on camera in scene 9 with `sbs run server,helm,science,comms -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-09, with the page's own files:**

1. The finished files lint `clean` and play with no errors and an empty
   `mast.runtime.log`. `playtest.md` and `campaign.md` in the folder change nothing.
2. `sbs docs MyUniverse --lens bible` writes one page. In it, each step of The Long
   Count carries `reached from` and `leads to` as the page's table says, and the
   Deepwell Hail leads to The Plover's Price by signal.
3. The save file after a walk through Act One holds the `reputation`, `side_credits`
   and `shared_quests` blocks quoted on the page, with those names for the pairs.
4. `state:` values seen in saves: 1 open, 2 hidden, 99 done, 98 failed, 0 for a step
   with no `Starts when:` line.
5. With `Objective:` typed on Her Log, the step's order is `Scan the Wren from Science`.
   The game's own order for that step is `Scan 1 derelict`.
6. Each row of the table "What each check sees" was tried: lint on the variant, the
   bible on two of them, a scripted walk on four.
7. The two mistakes in Step 5, each linted.

**Read in Class 1's pages, not run again:** that a typed `Objective:` is shown in the
Quest Log above the description. That was seen in the real game for a Class 1 mission.

**NOT seen or tried by anyone.** If one is not as the page says, stop and fix the page:

1. A playtest. Every word of Step 2 is practice from tabletop games, not a measurement.
2. Putting a kept copy of a save back in place.
3. The typed order in the Quest Log of this universe.
4. The bible page in a browser.

## Scenes

### 1. Cold open

**Screen:** `playtest.md` with a clock table filled in by hand.

**Say:** "You've walked your act alone. | You know it works. ||| What you don't know is
how long it takes, | what a crew does when they don't know the answers, | or which of
your sentences nobody understood. ||| Today you find out, with real people. || And then
you read what the game wrote down, | and you change three things, and only three. ||"

### 2. Lint first

**Screen:** `sbs lint MyUniverse`. `clean`.

**Say:** "Three checks before anybody arrives. | Each sees something the others can't.
||| The first is lint. || If it isn't clean, you're not ready. ||"

### 3. Read the spine

**Screen:** `sbs docs MyUniverse --lens bible`. Open the page. Scroll the beats, reading
only `reached from` and `leads to`.

**Say:** "The second is the printed bible. || Go down the beats, | and read only two
lines under each step. | Reached from, and leads to. ||| The first step leads somewhere,
and is reached from nowhere, and that's right. || Every later step is reached from the
one before. || And the act's ending leads nowhere, for now. ||| If a later step is sitting
up in the first beat, with no reached from line, | then nothing reveals it, and no crew will ever see it.
||"

### 4. Walk, then delete

**Screen:** The game, engaging down the spine quickly. Then File Explorer: delete the
save.

**Say:** "The third check is the walk. || You go down the spine alone, as fast as you
can. ||| And then you delete the save. || This is the one people forget. || I'd forget it too, | so it's written on the page in bold. ||| A crew that
sits down to a save you've walked through | starts at the end of your act. ||"

### 5. At the table

**Screen:** The five rules in Step 2.

**Say:** "Now for the people. | There are five rules, and they're harder than they look. || Say what
the game is, and nothing about the story. || Don't answer questions. Write them down.
|| Where do we go, isn't a question for you. | It's a lead that didn't say where. |||
Write the time whenever a step shows done. ||| Don't stop them leaving the spine. | If
they take three jobs instead, | that's the best thing you'll learn all week. ||| And end
it yourself. ||"

### 6. Read the save

**Screen:** File Explorer to `common_data\saves`. Open the save in VS Code. Scroll to
`reputation`, then `side_credits`, then `shared_quests`.

**Say:** "When they've gone, look at what the game recorded. ||| The runtime log should
be empty. ||| Then open the save. | Don't change it. Just read. ||| Under the ship's
name is what the ship has earned with each side. || Below that, the credits. ||| And
then every step of your story, | each with a state. || One is open, and two is hidden. |
Ninety-nine means it's done. || Now search for state one. || There should be exactly one step of
your spine. | That's the hook, and that's where next week begins. ||"

### 7. Keep a copy

**Screen:** Copy the save to Documents as `evening_01.yaml`.

**Say:** "Before you close that folder, copy the file. || Name it for the evening. |||
The start screen has a new game choice | that replaces the save without asking. || A
copy every week is the only undo a campaign has. ||| And remember what's in it. | Every
hidden step, word for word. || So keep it where the crew doesn't look. ||"

### 8. Three changes

**Screen:** The table in Step 4. Then add `Objective:` to Her Log and The Plover's
Price.

**Say:** "Now compare your notes with your plan, | and write three changes. No more.
|| More than three, and you can't tell next week which one helped. ||| The commonest first one is this. | The crew arrives, and somebody asks, what do we
do now? ||| A description is atmosphere. || So give the step an order, on a line of its
own. || And name the console in it. ||| Scan the Wren from Science. || That's the
cheapest fix in this class. ||"

### 9. Again, with new people

**Screen:** Lint: `clean`. Run the game. The step in the Quest Log, with its order.

**Say:** "Lint still says clean. || So delete the save, | and play it again with different
people if you can. ||| A crew that's seen evening one | can't tell you if the new order
helps. ||| Every playtest of an evening needs people who haven't seen it. || So save your friends for the evenings you're least sure of. ||"

### 10. Close

**Screen:** The table "What you need to know about a playtest".

**Say:** "So a walk proves the steps are joined, and nothing else. ||| The game records
what happened, | and only your notes say why. ||| So make three changes, keep a copy of the save, |
and then write the next evening. ||"
