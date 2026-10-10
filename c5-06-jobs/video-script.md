# C5-6 video script - Jobs

> **RE-MEASURED 2026-10-10** on the released tool `sbs` 0.14 and libraries (sbs_utils
> `ed811ecb`, LegendaryMissions `cc9cd06`, Open Universe `80e9397`), in the game's
> stand-in and by lint. Nothing ran in the real game and nobody saw a screen. Lint on the
> finished file and on all 46 one-change variants. One row moved: `Reward: 150 credits
> earns ...` with no comma is a warning now (`earns-shape`). Nothing was played again.

> **STATE ON 2026-10-08.** Written and measured today against the released tools: `sbs`
> 0.13, the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions
> `b20726f`, the Open Universe engine library rebuilt 2026-10-08 from `421ff4a`).
> Everything was run by script in the game's stand-in (the mock), from a copy of the
> mission placed where its save cannot reach a player's own. **Nothing in this lecture
> has been run in the real game, and nobody has seen any of its screens.** In the
> stand-in a script told the game "the ship destroyed this", "the ship picked up that"
> and "Science scanned the Tern". No ship fired and nobody sat at Science.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 5 leaves it: `kestrel_verge.amd` matches `c5-05-the-map\example\` |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | `MyUniverse` open, `kestrel_verge.amd` in a tab, font size raised |
| Game | Closed. Started on camera in scene 8 with `sbs run server,helm,comms,science -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-08, with the page's own file:**

1. The finished file lints `clean` and plays with no errors (146 labels run) and an empty
   `mast.runtime.log`. `story.mast` is unchanged from Lecture 2.
2. At standing 0 Comms is sent `Escort (250 cr)` for Hollin Compact and no Patrol. After
   the levy: `Patrol (240 cr)` and `Escort (300 cr)`.
3. Both taken: the Quest Log's Ship section holds `Hollin Compact: Patrol` and `Hollin
   Compact: Escort`. Patrol's objective is `Destroy 3 enemies`.
4. Engage on Patrol leaves the ship at 0, 0. Engage on Escort takes it to 3, 1, where
   Escort is done: credits 400 to 700, standing with Hollin 20 to 25.
5. The Assay Office is sent `Wreck Survey (220 cr)` and `Relay Run (180 cr)`. With the
   Tern reported scanned, the survey is done: credits 920, standing with Deepwell 5.
6. At -3, -2, with three enemy kills reported (two after the first two leave the patrol
   open), Patrol is done: credits 1160, standing with Hollin 35.
7. After the bold answer the Gleaners' station is sent `Salvage (180 cr)`. One crate of
   ore changes nothing; two of tech finish it: credits 1340, standing with the Gleaners
   25, and standing with Hollin 35 to 26.
8. Engage on Relay Run takes the ship to 0, 0: done, credits 1520. Hollin Compact is
   then sent `Patrol (252 cr)` and `Escort (315 cr)`, and Patrol taken again is Active.
9. Every row of the two tables in Step 5: 46 variants, one change each, each linted and
   played. A Relay Run given twenty seconds fails and takes its penalty.
10. `dock station` finishes when the game is told the ship docked. `scan 1 wreck` also
    works; the page teaches `derelict`.

**Read in the code, not run:** that a count of three or more kills grows with
difficulty; that a ceasefire stops a side's ships counting as enemies; that a failed
job can be taken again; the words the game says when Engage has nowhere to go.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. A real kill counting toward a patrol: the game's own report of a destroyed ship,
   from a real weapon. And a foe's station counting.
2. A real crate of tech picked up, and whether a Gleaner system holds two.
3. Science scanning the Tern, by hand or by itself, and the survey finishing.
4. Docking finishing a `dock station` job.
5. The countdown on the Relay Run in the Quest Log.
6. Where the game's own Accept Patrol Mission sits beside your Patrol on Comms.
7. Anything about Available Quests, if the crew has such a list. In the stand-in, a job
   that has been finished once is no longer listed there, though Comms still offers it.

## Scenes

### 1. Cold open

**Screen:** Comms on the Assay Office: Wreck Survey and Relay Run among the buttons.
Then Helm's Quest Log with three jobs under Ship.

**Say:** "You've been writing leads, | and a lead happens once. || Today you write the
other kind of quest, | the kind a crew can take again and again. ||| That's what a job is: a
station offers it, the crew takes it, | they do it, and they're paid. || And when they
come back, it's there again. ||"

### 2. The life of a job

**Screen:** The table in Step 1 of the page, one row at a time.

**Say:** "Here's the whole life of a job, in five stages. || First it's offered, when Comms
selects a station, and each job is a button, with its pay. ||| Then it's taken, and it
goes into the Quest Log, under the ship's name. || Then it's done, when its ending comes
true, | wherever the ship happens to be. ||| Then it's paid, in credits, and in standing
with the side that offered it. || And then it's offered again. ||| Now, the template gave
you three jobs, | and two of them have no ending at all. || A crew can take them, and
never finish them. ||"

### 3. Five endings

**Screen:** The table in Step 2. Then type `Done when: destroy 3 enemies` into Patrol.

**Say:** "An ending is one line, Done when, | and it's an order to the captain in plain
words. ||| There are five first words. || Destroy. Recover. Scan. Reach. And dock. ||
After the word comes a number, and what to count. ||| So, for Patrol: Done when, destroy
three enemies. || Enemies is a word the game knows. | It means anything at war with the
crew. ||| And the game shows that same line to the crew as their objective, | so write
it the way you'd say it. ||"

### 4. A reward that costs something

**Screen:** Salvage. Type the `Done when:` line, then add `, earns hollin selfish 20` to
the reward. Highlight the comma.

**Say:** "Salvage is the Gleaners' job. || Its ending is, recover two tech, | and tech
is a key from your Goods chapter. ||| Now look at the reward. || After the credits I'm
adding a comma, | and then a deed, the same three words as in Lecture Four. || A side, a
trait, and a number. ||| So this job pays, and it pleases the Gleaners. || But the
farmers hear who's been stripping wrecks, | and they think a little less of the crew.
||| And mind that comma. | Leave it out, and the credits are paid, | the deed is dropped,
and lint gives you a warning about it. ||"

### 5. Three more jobs

**Screen:** Type Wreck Survey, Relay Run and Clear the Lanes. Highlight `Fails when:`,
`Penalty:`, then `Tier: 3`.

**Say:** "Three more jobs, quickly. || A survey, which ends when Science scans a dead ship. ||| A run
home, against the clock. || Fails when, ten minutes, | and a penalty if it does. || You
know both of those lines from Class One. ||| And a strike, at tier three. || That one's
only offered to a crew the Compact really trusts. ||| The relay run does something else
for me. || It ends at home, | so it's a way back that pays. ||"

### 6. On offer

**Screen:** The Sides chapter. Change Hollin's and the Deepwell's `Offers:` lines.

**Say:** "A job nobody offers is never seen. || So, back up to the sides. ||| The
farmers get patrol, escort and strike. || The miners get the survey and the relay run.
||| I'm taking the escort away from the miners, | because it ends at their own front
door. || A job that ends at a place | belongs to a side that lives somewhere else. ||"

### 7. Check

**Screen:** Save. `sbs lint MyUniverse`: clean. Then the second table in Step 5.

**Say:** "I save, and lint says clean. ||| And today that's less than half the check. ||
Lint knows the five first words, | so a misspelled one gets a warning. || But it doesn't
read what comes after. ||| Write the number as a word, | and the job never finishes. ||
Name a good you don't have, and it never finishes. ||| And here's the one that will
catch you. || You can't write, destroy three gleaners. || The game takes the s off, |
looks for something called a gleaner, and finds nothing. || So write enemies instead. ||"

### 8. Work the board

**Screen:** `sbs run server,helm,comms,science -m MyUniverse map=0`. Comms: Hollin
Compact, the levy, Patrol and Escort. Helm: Quest Log, Engage Escort. Comms: Assay
Office, both jobs. Helm: The Third Colony; Science on the Tern. Then The Breaking Yard.

**Say:** "At home, the farmers offer one job. || I pay the levy, | and now there are
two, and the escort pays more. ||| I take both, and here they are in the Quest Log. || I
engage the escort, and on arrival it's done. ||| The miners' office has my two new
jobs. || I take them, and the clock on the relay run is running. ||| The survey wants a
dead ship, | and I know where one is. || And the patrol wants enemies, | and I know
where those are too. ||"

### 9. Paid, and offered again

**Screen:** Gleaners' station: the bold answer, Salvage. Then Engage Relay Run. Comms on
Hollin Compact: Patrol and Escort at new prices.

**Say:** "The Gleaners will deal with me now, | so I take their salvage. ||| When it's
done, watch the farmers. || My standing with them just dropped, | and I never spoke to
them. ||| Now the relay run takes me home, inside its ten minutes. || And look at the
farmers' list. || Patrol is back, and it pays a little more than last time. ||| That's
the thing to remember about a job. || It never runs out. || So think about how often
you want a crew to be able to please each side. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Write one job for each side that only that side would
offer. || Make one of them tier two. | Make one that costs the crew somewhere else. ||
And put one against the clock, and let it fail once. ||| Next time, your universe gets a
story, | with a beginning and an end. ||"
