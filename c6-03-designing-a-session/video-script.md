# C6-3 video script - Designing a session

> **STATE ON 2026-10-09.** Written and measured today against the released tools: `sbs`
> 0.13, the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions
> `b20726f`, the Open Universe engine library in `__lib__`). Everything was run by script
> in the game's stand-in (the mock), from a copy of the mission placed where its save
> cannot reach a player's own. **Nothing in this lecture has been run in the real game,
> and nobody has seen any of its screens.** The minutes on the sheet are a plan. Nobody
> has timed this evening with people.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 1 leaves it: `kestrel_verge.amd` and `campaign.md` match `c6-01-from-one-session-to-twenty\example\` |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| VS Code | `MyUniverse` open, both files in tabs, font size raised |
| Game | Closed. Started on camera in scene 8 with `sbs run server,helm,science -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-09, with the page's own files:**

1. The finished files lint `clean` and play with no errors and an empty
   `mast.runtime.log`.
2. At the start the Quest Log has One of Five and neither Her Log nor Enter It.
3. On arrival at (2, 2): three ships on the raiders' side, the card
   `The Wren is guarded - hostiles on approach.`, The Wren charted, Her Log Active.
4. Two derelicts were in that system: The Wren and one of the game's own, named
   Derelict. Telling the game the ship scanned the game's own one finished Her Log.
5. Engaging Enter It: the ship at (0, 0), credits up by 300, Two of Five Active.
6. After Continue: Two of Five Active, the three steps of evening 1 Done.
7. Engaging Two of Five with no landmark at (-2, 3): the ship arrives, no hostile ship,
   no derelict, the lead Done.
8. Every row of the tables in Step 7: 6 variants, each linted, 3 of them played.

**Read in the code, not run:** that guards which were destroyed do not return (a flag on
the system). What was measured is the other half: guards that were not destroyed were
there again.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. Science scanning the Wren: how near, how long, and whether it happens by itself in
   sensor range. The stand-in never scans by itself. The real game is known to, in
   other missions.
2. The fight with the three guards.
3. The Quest Log and the arrival cards.
4. How long any of this takes with a crew.

## Scenes

### 1. Cold open

**Screen:** The Quest Log at the end of the evening: Two of Five open, three steps Done.

**Say:** "Last time, you wrote one lead. || Today that lead becomes a whole evening, |
with a beginning, something to do, a moment of danger, | and a reason to come back next
week. ||| It takes three records, | and one line on a landmark. ||"

### 2. Four parts

**Screen:** The table in Step 1 of the page.

**Say:** "An evening at a table has four parts. ||| The open is where the crew's told
where to go, and why it has to be tonight. || The objective is the one thing they have to do when
they get there. || The climax is the moment it could go wrong. || And the hook is the
last thing they learn, | which is why they come back. ||| I've put minutes beside each
one. || Those are a plan, not a measurement, | and you'll time a real table against
them later. ||"

### 3. What the game does not know

**Screen:** The second table in Step 1.

**Say:** "Here's something to be clear about before we build. || The game has no idea
what an evening is. ||| There's no end of session screen. | There's no recap of last
week. || And there's no timer that stops you at forty-five minutes. ||| So you do all
three yourself, | with the shape of the episode. || The last step ends at home, and you
stop there. || The open lead is your recap. || And the time limit is your watch. ||"

### 4. The sheet

**Screen:** `campaign.md`. Type the Evening 1 section.

**Say:** "Before any records, the sheet. || It's a small table in your campaign page, |
one row for each of the four parts. ||| Then a few lines under it. | What the crew
learns. What it pays. Who's busy. || And where the evening ends. ||| Fill in what the
crew learns first. || If you can't, it's a trip, | and not an episode. ||"

### 5. Open and objective

**Screen:** `kestrel_verge.amd`. Add `Then: reveal s01_scan` to One of Five. Add Her
Log under it.

**Say:** "Now for the records themselves. || The open is the lead you already have. | It gets one more
line, | so that finishing it shows the next step. ||| The next step is the objective. |
Science reads the Wren's log. ||| Two things I measured about that. || Any dead ship in
the system counts, | and the game may have put one of its own there. || So write the
text so either one makes sense. || And the step's hidden until the crew arrives, | so
nothing they scanned earlier counts. ||"

### 6. The climax

**Screen:** The Wren landmark. Add `Guards: torgoth`.

**Say:** "The climax isn't a step at all. | It's something at the place. ||| One line on
the landmark, | and three ships are waiting when the crew arrives. ||| And notice what
I haven't written. || Nothing says, destroy them. || So the crew has a real choice. |
They can fight. They can scan under fire and run. || Or they can leave, and come back
next week, | and the guards will be there again. ||"

### 7. The hook

**Screen:** Add Enter It and Two of Five. Select the text of Two of Five.

**Say:** "Last, the way home, and next week's lead. ||| The home step ends when the
ship's back at the relay, | and that's where it pays. || A crew that's just been paid, at
their own station, | is a crew you can send home. ||| And the moment it's done, the next
lead appears. || That's the hook, and it's the last thing they read tonight. ||| And next
week, after they continue, | it's the one open line of the campaign. || So it's the
recap as well. ||"

### 8. Lint and play

**Screen:** Save. Lint: `clean`. Run the game. Engage One of Five, the card, the scan,
Engage Enter It, the new lead. Close. Run again.

**Say:** "Save, lint, and it's clean. || So let's play it. ||| One line of the campaign
in the log, not three. || I engage the lead, | and here's the Wren, and the warning. ||| Science
scans her, and the way home appears, | so I engage that as well. ||| We're home, we're paid, |
and there's the second boat. || And that's the whole evening. ||| Now I close the game and start
it again. || And the hook's still there, waiting. ||"

### 9. Close

**Screen:** The table "What you need to know about an evening".

**Say:** "So an evening is four parts and three records. ||| You end it, because the
game won't. || And a step that's done stays done, | so a long evening is simply two
evenings. ||| Next time, we turn this one into a pattern, | and write the second
evening in a quarter of the time. ||"
