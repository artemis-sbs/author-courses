# C6-6 video script - Reputation arcs

> **STATE ON 2026-10-09.** Written and measured today against the released tools: `sbs`
> 0.13, the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions
> `b20726f`, the Open Universe engine library in `__lib__`). Everything was run by script
> in the game's stand-in (the mock), from a copy of the mission placed where its save
> cannot reach a player's own. **Nothing in this lecture has been run in the real game,
> and nobody has seen any of its screens.** Every standing on the page is the game's own
> number, read after the deed.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 5 leaves it: both files match `c6-05-campaign-architecture\example\` |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| VS Code | `MyUniverse` open, both files in tabs, font size raised |
| Game | Closed. Started on camera in scene 8 with `sbs run server,helm,comms -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-09, with the page's own files:**

1. The finished files lint `clean` and play with no errors and an empty
   `mast.runtime.log`.
2. At standing 0 the Hollin hail has three answers. After two levies (200 credits,
   standing 40) it has four, and the fourth is Ask to see the Tern's manifest.
3. Pressing it: The Tern's Manifest is Done, 200 credits are paid, and the Compact's
   line is shown.
4. Selling the Count at the Gleaners' station: Hollin 40 to 17, Gleaners 0 to 15.
5. Back home at 17: Patrol is not on the station's list, Escort is offered at 292 where
   it was 350, the greeting is the under-20 line, and the hail has three answers.
6. A tier 2 job finished at 40 took the ship to 50. Sold at 50, the ship stood at 27.
7. `Reward: ..., earns hollin honest 20, earns hollin generous 20` on a Narrative step:
   credits paid, the ship's standing unchanged, the scores kept on the shared story.
8. Standing is in the ship's record in the save. Re-measured 2026-10-10 on the released
   libraries: a renamed ship kept its standing and its jobs (it was 0 when this page was
   first written).
9. Every row of the tables in Step 6: 6 variants, each linted, 5 of them played.

**Read from Class 5 Lecture 4, not run again:** the thresholds 20, 30, 50 and 60, and
the tier 1 job's 5.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. The hail on Comms, and how an answer that is not offered looks (absent, or greyed).
   The stand-in is simply not sent the button.
2. Whether the crew is told anything when standing changes. The stand-in is sent one
   card, `Word of your deeds spreads among the sides.`, at some point.
3. The ledger's guesses. They are arithmetic, not play.

## Scenes

### 1. Cold open

**Screen:** Comms in the Hollin hail, with Ask to see the Tern's manifest.

**Say:** "In the last class, you moved a crew's standing in one sitting. ||| A campaign
asks something harder. || How fast does it move, | and what does it open when it gets
there? ||| Today you'll build a door that only trust can open. || And then a way for
the crew to slam it on themselves. ||"

### 2. What moves it

**Screen:** The table in Step 1 of the page.

**Say:** "First, what actually moves standing over weeks. | I measured every row. |||
Finishing a side's job. | Five points, or ten for the harder kind. || Paying the levy in
a hail. | Twenty points, for a hundred credits. ||| And now look at the last row. ||
Finishing a step of the story does nothing. ||| You can write the words. | Lint says
clean, the credits are paid, | and the standing goes somewhere no door ever reads. ||"

### 3. Price, not prize

**Screen:** The bold sentence under the table.

**Say:** "That has a consequence, and it's the whole craft of this lecture. ||| Nothing
the crew does once can move standing. || Jobs can be taken again. | Answers can be given
again. ||| So you can't hand standing out as a prize. || You can only put a price on it,
| in credits or in time. || And you decide how much of each an evening pays. ||"

### 4. A door that opens

**Screen:** Add The Tern's Manifest to Narrative. Add the answer to Hollin Hail. Add
The Manifest record.

**Say:** "So here's a door, in three parts. ||| A lead the crew can see from the very
first evening. | It tells them what opens it. || That matters, because a door nobody
knows about | isn't a reason to do anything. ||| Then one answer in the Compact's hail.
|| After the key it says, if standing is forty or more. | Below that, the button isn't
there. ||| And the record it leads to, | where they're finally told. ||"

### 5. Why forty

**Screen:** The paragraph "Why 40".

**Say:** "Why forty, and not some other number? ||| At twenty it opens after one levy, |
on the first evening, and that isn't a door. || At sixty, a crew may never get there. |||
At forty, a crew that takes one job a week | and pays the levy once | arrives in about
the fourth week. || And that's where I want them to hear it, | right before the act ends. ||| So you choose the number by choosing the week. ||"

### 6. A door that closes

**Screen:** Add the answer to Gleaner Hail and the Sold record. Then the before and
after table.

**Say:** "A door that only opens is a reward. | A door that can close is a story. |||
So in the Gleaners' hail, I add one tempting answer. || Sell them a copy of the Count. |||
It earns the Gleaners' respect, | and in the same breath it costs the Compact's trust. ||
An answer with one side can do a deed with another. ||| Here's what I measured. | Forty
with the Compact became seventeen. || And at home, three things changed. || The greeting
went cold, the manifest was gone, | and so was the better work. ||"

### 7. The ledger

**Screen:** `campaign.md`. Type the standing ledger.

**Say:** "Now you plan it. || The ledger is one row for each evening, | with the
standing you expect, | and the door you expect to open. ||| The numbers are a guess, and
the crew won't follow them. || What matters is the last column. ||| For each door,
you've named an evening, | and you can check the price against the wages. || Too cheap,
and it opens on night one. | Too dear, and it never does. ||| And remember where all of this is kept. | It's in the ship's own record, in the save. ||"

### 8. Lint and play

**Screen:** Lint: `clean`. Run the game. Hail, three answers. Levy twice. Hail, four
answers. Ask. Engage The Breaking Yard. Hail the Gleaners, sell. Home. The station's
list, then the hail.

**Say:** "Lint's clean, so here it is. ||| Three answers, and no manifest. || I pay the
levy twice, | and now there are four. ||| I ask, and the lead is done. ||| Then out to
the breaking yard, | and I sell the Count. || Nothing tells me what that cost. ||| Back
home, the good work has gone from the list. || And the hail's down to three answers
again. ||"

### 9. Close

**Screen:** The table "What you need to know about an arc".

**Say:** "So you price standing, you don't award it. ||| Every answer that earns it gets
a cost. || And all of it lives in the ship's record, | which the save carries from week to week. |||
Next time, we look at the act from the crew's side of the table. ||"
