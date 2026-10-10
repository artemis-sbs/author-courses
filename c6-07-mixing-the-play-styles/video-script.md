# C6-7 video script - Mixing the play styles

> **STATE ON 2026-10-09.** Written and measured today against the released tools: `sbs`
> 0.13, the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions
> `b20726f`, the Open Universe engine library in `__lib__`). Everything was run by script
> in the game's stand-in (the mock), from a copy of the mission placed where its save
> cannot reach a player's own. **Nothing in this lecture has been run in the real game,
> and nobody has seen any of its screens.** "Whose evening it is" is a design claim, not
> a measurement: no crew has played any of these evenings.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 6 leaves it: both files match `c6-06-reputation-arcs\example\` |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| VS Code | `MyUniverse` open, both files in tabs, font size raised |
| Game | Closed. Started on camera in scene 8 with `sbs run server,helm,comms -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-09, with the page's own files:**

1. The finished files lint `clean` and play with no errors and an empty
   `mast.runtime.log`.
2. Lamp Run: not on the Hollin station's list at standing 0; listed at 360 credits at
   20 and at 420 at 40. Taken and engaged, the ship is at (2, 2), the job is Done, the
   credits are paid and standing rises by 10.
3. Evening 3: on arrival at (3, 1) The Plover's Price is Active. The Deepwell hail has
   both answers and Sign off. Either answer finishes the step and reveals Enter It
   Again; that step pays 300 at home and reveals Four of Five.
4. The second answer leaves standing with the Deepwell at -6. The first costs 150
   credits and leaves it at 20.
5. A step of the spine with a clock: when the time ran out the step was Failed and its
   `Then: reveal` did nothing. With a `Penalty:` the credits were taken.
6. Re-measured 2026-10-10 on the libraries released 2026-10-09: a step that failed, with
   the game closed before any jump, was still Failed after Continue, with its penalty
   paid. (It was Active again when this page was first written.) A running clock came
   back with the time it had left.
7. `Starts when: reach ...`, `Starts when: signal ...` and `Starts when: 10 seconds`
   on a Narrative step: lint `clean`, and the step never started.
8. Every row of the tables in Step 6: 6 variants, each linted, 4 of them played.

**Read in the plan for this course, not built:** the four styles in the second table of
Step 1. Class 5 Lectures 11, 14 and 15 are written now. Lecture 10 is not.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. Any of the evenings with a crew. Whether Science really carries evening 1 depends on
   how scanning feels in the game.
2. How long Lamp Run takes. Ten minutes is a guess.
3. The hail on Comms.

## Scenes

### 1. Cold open

**Screen:** The rotation table in `campaign.md`.

**Say:** "Look at your first two evenings from the crew's side of the table. || One of
them belongs to Science. | The other belongs to Weapons. ||| If the next three are
fights as well, | half your crew spends a month watching. ||| Today you'll plan who
carries each evening, | and you'll build two new kinds. ||"

### 2. What a style is

**Screen:** The first table in Step 1 of the page.

**Say:** "A style is the answer to one question. | Whose evening is it? ||| A search is
Science's evening. || A fight belongs to Weapons and Engineering. ||| A talk belongs to
Comms. | A race belongs to Helm. || Politics is Comms again, with the captain. | And
trade is Helm and Comms together. ||| You can build all six of those today, | with what
you already know. ||"

### 3. Styles for later

**Screen:** The second table in Step 1.

**Say:** "There are four more styles in this course. || Boarding, a ruin, a set battle,
| and the Admiral's view from above. ||| A campaign in your universe can't use those
yet. || Each one's waiting on a lecture in the last class. ||| So plan for them, and
write them in your rotation as later. || But don't build them today. ||"

### 4. The rotation

**Screen:** Type the rotation into `campaign.md`. Point down the last column.

**Say:** "Three rules, and they're habits, not laws. ||| Never the same style twice
running. || Everyone carries an evening in every act. || And a tentpole mixes two. |||
Now look at the last column, | what's on offer beside the spine. || Half an evening is
the universe, remember. | This is where you plan that half. ||"

### 5. A talk evening

**Screen:** `kestrel_verge.amd`. Change Three of Five's `Then:` line. Add The Plover's
Price and Enter It Again. Add the two answers to the Deepwell hail and the two records.

**Say:** "Evening three is a stub, so let's make it an evening. ||| The open now leads
to an objective, | and the objective ends with a signal. || An answer in a hail sends
it. ||| And there are two answers. || Pay the fee, and be polite. | Or lean on the
clerk, for nothing. ||| Both of them finish the step. || But they leave the crew in
different places with the Deepwell, | and that's remembered for the rest of the
campaign. ||| There's one warning, though. | The answers are there from the first evening. || A curious
crew can ask early, | and it won't count. So word them for that. ||"

### 6. Where clocks go

**Screen:** The measured table in Step 4.

**Say:** "Now for the race. | A race is a step with a clock on it. ||| Before you put one on
the spine, here's what I measured. || When the time ran out, the step failed. | And the
next step was never revealed. ||| That's the campaign stopped, | in a save your crew has
put ten weeks into. ||| So a clock never goes on the spine. || And closing the game
doesn't undo a clock that ran out. ||"

### 7. A race that's safe

**Screen:** Add Lamp Run to Jobs. Add `lamp_run` to Hollin's `Offers:` line.

**Say:** "A clock belongs on a job. || A job that fails costs its penalty, | and the crew
can take it again. ||| This one goes back to the Wren, | so the place from evening one
still matters. ||| And it's tier two, which gives it a date. || The Compact only offers
it to a crew at twenty or more. | Your ledger says when that is. ||"

### 8. An evening off the map

**Screen:** The table in Step 5.

**Say:** "What about a boarding evening, or a ruin, right now? ||| You have those, as
missions of their own. || You can play one as an interlude, | the same people in the
same story. ||| But be exact about it, | because it's another save. || Nothing they do there
reaches your universe. ||| The only bridge is the next evening's hook, | so write that
hook after you've played. ||"

### 9. Lint and play

**Screen:** Lint: `clean`. Run the game. The station's list with no Lamp Run. Levy. The
list again. Take it, engage. Then Three of Five, the hail, an answer, home.

**Say:** "Lint says it's clean. || There's no lamp run on the list yet. ||| I pay the levy once, | and
there it is. || I take it and engage, | and it's done and paid. ||| Then it's evening three.
|| At the Assay Office I hail, | and I choose how to ask. ||| The step shows done, | and
the way home appears. ||"

### 10. Close

**Screen:** The checkpoint list.

**Say:** "So every evening has an owner, | and no style comes twice running. ||| No
clock on the spine. || And an interlude is joined by your writing, and nothing else. |||
Next time, real people sit down at the table. ||"
