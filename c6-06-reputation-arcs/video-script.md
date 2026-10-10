# C6-6 video script - Reputation arcs

> **RE-MEASURED 2026-10-10** on the released tool `sbs` 0.14 and libraries (sbs_utils
> `ed811ecb`, LegendaryMissions `cc9cd06`, Open Universe `80e9397`), in the game's
> stand-in and by lint. Nothing ran in the real game and nobody saw a screen. Lint on the
> finished file and its variants; `earns hollin lier 40` is a warning now. **One thing
> this page taught is no longer true and was corrected:** a deed on a step of the story
> does reach the ship (standing 40 to 51 when The Tern's Manifest carried `earns hollin
> honest 20`). Scenes 2, 3 and 9 and Step 1 of the page were rewritten for it: a prize,
> once, on a step; a price on everything that repeats. A split universe lints `clean` now.

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
7. `Reward: 200 credits, earns hollin honest 20` on a Narrative step (The Tern's
   Manifest), re-measured 2026-10-10 on the released libraries: credits paid, and the
   ship's standing with Hollin 40 to 51. `Standing: hollin honest 20` on the same step
   did the same. (When this page was first written the ship's standing did not move.)
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
A step of the story can carry a deed as well. ||| I put one on a lead and finished
it, | and the standing went from forty to fifty-one. || But a step is finished once. ||"

### 3. A prize and a price

**Screen:** The bold sentence under the table.

**Say:** "That gives you two tools, and most of this lecture is the second one. ||| A
prize is a deed on a step. || It's given once, on the evening you choose. ||| Everything
else, the crew can do again. || Jobs can be taken again, | and answers can be given
again. ||| So on those you put a price, | in credits or in time. || And you decide how
much of each an evening pays. ||"

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

**Say:** "So you award standing once, on a step, | and you price the rest. ||| Every answer that earns it gets
a cost. || And all of it lives in the ship's record, | which the save carries from week to week. |||
Next time, we look at the act from the crew's side of the table. ||"
