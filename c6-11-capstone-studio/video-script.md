# C6-11 video script - Capstone studio

> **STATE ON 2026-10-10.** Written and measured against the released tools: `sbs` 0.13,
> the published v1.4.0 libraries (sbs_utils `ae05dac7`, LegendaryMissions `b37a320`, the
> Open Universe libraries of 2026-10-09, saves version 2). The whole studio was walked
> by script in the game's stand-in (the mock), from a copy of the mission placed where
> its save cannot reach a player's own: one save, four launches, with the universe file
> changed between the first and the second exactly as the page changes it. The script
> pressed Comms buttons by their text, sent the Quest Log's Engage, and told the game
> "the ship scanned this" and "the ship destroyed this". No weapon fired and no console
> was connected. **Nothing in this lecture has been run on a real console, nobody has
> seen any of its screens, and no table of people has played any of it.**

The companion page is `lesson.md`; the finished `kestrel_verge.amd` and `campaign.md`
are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `KestrelVerge` as Lecture 10 leaves it, with Lecture 2's lines in `kestrel_verge.amd` and `campaign.md` still in the folder |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "KestrelVerge" --update-libs` |
| VS Code | `KestrelVerge` open, `kestrel_verge.amd` and `campaign.md` in tabs, font size raised |
| Game | Closed. Started on camera three times with `sbs run server,helm,comms,science,weapons -m KestrelVerge map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-10, with the page's own files:**

1. Sitting one, a new game on Lecture 10's file: evenings 1 and 2. At the end the ship
   is at 0, 0, credits 1050, standing with Hollin 20, Three of Five open, the Escort in
   hand.
2. The finished file lints with one warning, the true one about `act2_begins`. Four
   one-change variants add the warnings in Step 7; a fifth adds none.
3. Sitting two, the same save, the finished file: the open step is listed as The Long
   Count: The Plover. Evening 3: credits 1200 at the Assay Office after the fee, 1500 at
   home. Evening 4: on arrival at 4, -2, Her Beacon is Active; scanned, then home:
   credits 1800, standing Hollin 25, Deepwell 20.
4. Sitting three, the same save: at the Gleaners' home the hail gives four answers;
   after Ask what became of the Tern's boats it gives six; Buy the Skua's log leaves
   credits at 1500 and the step Done; Five Boats at home pays 1000: credits 2500, every
   step of The Long Count Done but While They Read, which is Active.
5. A fourth launch: the game continues and is not over. A fifth, with Act Two's three
   additions in the file: While They Read is Active and evening 6's step hidden; the
   Compact's hail has the new answer; pressed, While They Read is Done and The Seller's
   Mark is Active. On an earlier save with no step in between, `Then: reveal s06_go` on
   the finished Five Boats and an answer's `; reveal s06_go` both left it hidden.
6. `mast.runtime.log` was empty after every launch.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. Every screen.
2. A real scan of the Wren and the Petrel. The real game scans by itself when a ship is
   in range, so a scan step may finish before Science touches anything.
3. A real fight at the Dunlin.
4. How long any of it takes with people.

## Scenes

### 1. Cold open

**Screen:** The Quest Log with every line of The Long Count marked Done. Then
`campaign.md`, open at Act Two.

**Say:** "This is the last lecture, and it teaches you nothing new. ||| It's a studio, where
you build, you play, | and you write down what happened. ||| By the end you'll have
act one finished and walked, | and the other three acts on a page. ||"

### 2. The plan

**Screen:** The table in Step 1 of the page.

**Say:** "Three sittings, on one save. ||| In the first, I play evenings one and two, |
on the file exactly as it stands. || Then I stop, and I write evenings four and five.
||| I do that on purpose, | because it's how you'll write the other fifteen: | with a crew
already playing. ||| Then two more sittings to finish the act. ||"

### 3. Sitting one

**Screen:** Run the game. The walk of Step 2. Then the "When I stopped" table.

**Say:** "Sitting one is a walk, as fast as I can go. || The levy, a job, | the Wren
and home, | the Dunlin and home. ||| And here's where I stop. || The open step is three
of five. || Four and five are still stubs, | and the crew can't see them yet. ||| I
close the game. ||"

### 4. Write evening four

**Screen:** `kestrel_verge.amd`. Four of Five's `Then:` line changes. Two new steps go
in under it.

**Say:** "Now I write, with a game in progress. ||| Evening four is one step that goes
to the Petrel. || I change where it leads, | and I add an objective and a way home. |||
Is that safe for the save? || Yes, and I know why. | The crew hasn't finished that step,
| so its new line will be read when they do. || And the new steps are ahead of them,
not behind. ||"

### 5. Write evening five

**Screen:** Five of Five's `Then:` line. The Skua's Price. The two answers in the
Gleaner hail, `if learned` highlighted. The two reply records.

**Say:** "Evening five is a talk evening, in the Gleaners' yard. || There are two
answers, | and either one finishes it. ||| But this time they're held back. || If
learned, the Gleaners broke a boat. ||| A crew that hails them cold won't see either
answer. || They have to ask the right question first. ||| That's the fact from lecture
two, | doing a real job. ||"

### 6. One change they'll notice

**Screen:** Three of Five's heading becomes The Plover. Then Five Boats gains its
`Then:` line, and While They Read goes in. Save. `sbs lint KestrelVerge`: one warning.

**Say:** "And one change to something the crew has already seen. || The step they're
on had a placeholder for a title. || I change the title, | and I leave the key alone.
||| One more step, for act two to stand on. || It stays open when the act ends, |
and act two will finish it. ||| I save, and I run lint. || One warning, and for once
it's true. | Nothing sends that signal yet. ||| If it said a step is never revealed, |
I'd stop right here and fix it. ||"

### 7. Sitting two

**Screen:** Run the same line. The seven rows of Step 7.

**Say:** "Sitting two, and I don't delete the save. ||| The open step has its new
name. || My words reached a game in progress. ||| Evening three is the assay office,
and home. || Then comes evening four. || I arrive at the Petrel, | and there's the step I
wrote an hour ago. || I scan her, and I go home. ||| Now five of five is waiting. || I
close the game again. ||"

### 8. Sitting three

**Screen:** Run it again. The six rows of Step 8. End on the Quest Log.

**Say:** "And the last sitting. ||| At the yard, I hail the Gleaners. || There are four answers,
| and neither of my new ones. ||| I ask what became of the boats, | and I hail again.
|| Now there are six. ||| I buy the log. | The step is done, | and the act's ending
appears. ||| Home, and it pays. || Every line of the long count is done, | but the one that's
waiting for act two. ||"

### 9. The other three acts

**Screen:** `campaign.md`. Act One's table, updated. The table of sittings. Then Acts
Two, Three and Four.

**Say:** "Now for the page. || Act one's table says in full, all the way down. ||| I write
what I played: | three sittings, with the credits and the open step each time. ||| And
then the other three acts. || One table each, one row an evening. | A title, a place, a
style, and how it ends. ||| I don't write a single record. || There's one win in the
whole campaign, | and it's on evening twenty. ||"

### 10. The rubric, and what nobody has played

**Screen:** The rubric. Then the table "What nobody has played".

**Say:** "Mark yourself against the rubric. || And be honest, the way this page is.
||| Nobody has sat a crew down to this. || A script did the scanning and the fighting.
|| Every time on my sheets is a plan. ||| The last two points on the rubric are the
ones that count. || A crew that isn't you plays evening one, | and you watch without
helping. ||"

### 11. Close

**Screen:** `campaign.md`, the first empty row of Act Two.

**Say:** "And that's the course. ||| You have a universe, and a campaign with its
first act played. || You have a plan for the rest, | and the habits to write it while
a crew is playing. ||| So there's only one thing left to do. || Go and write evening
six. ||"
