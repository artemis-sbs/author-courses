# C5-15 video script - The Admiral, part 2: an Admiral alongside a bridge crew

> **STATE ON 2026-10-10.** Written and measured against the released tools: `sbs` 0.13,
> the published v1.4.0 libraries (sbs_utils `ae05dac7`, LegendaryMissions `b37a320`, the
> two Open Universe libraries of 2026-10-09). Everything was run by script in the game's
> stand-in (the mock), from copies of `MyUniverse` placed where their save cannot reach
> a player's own, with the libraries a student's mission loads. The Admiral's console
> was never opened. A script made the Admiral's camera the way the console does,
> selected the worldlet and the platforms through the game's own Comms routes, and
> pressed the buttons the game sent, by their text. **Nothing in this lecture has been
> run on a real console, and nobody has seen any of its screens.** In the real game's
> server, with no console attached, a campaign from this template with Admiralty and
> Worldlets chapters was started and its pools were seeded.

The companion page is `lesson.md`; the finished `kestrel_verge.amd` is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 13 leaves it. `story.json` ends with the `universe_core` line and the `admiral` line |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | `MyUniverse` open, `kestrel_verge.amd` in a tab, font size raised |
| Game | Closed. Started on camera in scenes 7 and 9 with `sbs run server,admiral,helm,comms -m MyUniverse map=0`, and in scene 8 with `sbs run server,helm,comms,weapons -m MyUniverse map=0` on a deleted save |

## Confirm on camera

**In the mock, by script, on 2026-10-10, with the page's own files:**

1. The finished file lints with the three `ledger_read` warnings, the third still on
   line 219, and nothing else.
2. The Admiral is on (`campaign`, pace `epic`, raids `off`), the Admiral console's
   condition is true, and the home system holds one worldlet, Hollin Prime. Pools 3,600
   ore, 1,200 gas, 480 crew, each able to hold 14,400.
3. The worldlet is sent `Build Headquarters (150 ore, 15 crew)`. Thirty-three seconds
   after the press: "Headquarters complete." The worldlet is then sent eight more
   buttons.
4. Extractor, Academy, Shipyard and Lab, started together: all four stand inside 60
   seconds. With the Extractor, ore rose 16 in 30 seconds.
5. The Shipyard is sent one button, Maren's. Commissioned: fleet F1, three ships on the
   crew's side. A ship of the fleet is sent `Hail` and five orders.
6. The Lab is sent `Research Deeper Silos [engineering]`. Forty-one seconds after the
   press it is done, each pool can hold 14,900, and the Lab is sent `Research Hot
   Drills [engineering]`.
7. Throughout: credits 500 and the Quest Log's three leads, unchanged.
8. A second launch on the same save: pools 2,634 / 1,131 / 419, tanks of 14,900, five
   platforms, the fleet, Deeper Silos done. Twenty seconds later the ore was 2,646.
9. The three conditions, each left out in turn (23 one-change variants linted and
   played in all): no library line, no Admiralty chapter, no Worldlets chapter, `Mode:
   story`, or `Mode: campaign` with no chapters: no Admiral, no worldlet, empty pools.
10. With the seat empty, Lecture 16's two sittings were walked on this file: every
    probe line the same as Lecture 16's own run but the raiders' names and one more
    object at home, the world. Then a third launch after the win: one card titled
    Campaign won, and the pools still seeded.

**Read in the game's guide, not run:** border raids; the two victory quests that need a
second commanded side.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. The Admiral console, and whether `sbs run server,admiral,...` opens one.
2. Hollin Prime on the Admiral's map, and on Helm's and Science's.
3. Whether a bridge console shows anything new when the Admiral's library is loaded.
4. A fleet obeying an order.
5. A real fight at the Bone Pile with an Admiral's fleet in the game.

## Scenes

### 1. Cold open

**Screen:** Two windows side by side: the Admiral console over Kestrel Relay's system,
and Helm's Quest Log with the three leads.

**Say:** "Last time you wrote for the admiral's seat, in a lab. || Today that seat comes
home. ||| Your universe gets a second way to play, | right beside the bridge crew. ||
And here's the part that matters most to a writer. || If nobody wants that chair, | the
crew's evening doesn't change at all. ||"

### 2. Three things switch it on

**Screen:** The two tables in Step 1 of the page.

**Say:** "A campaign has no admiral unless you ask for one. || And you ask by writing
chapters. ||| Three things have to be true. || The admiral's library is loaded. || The
mode is campaign, with an admiralty chapter in your own file. || And there's a
worldlets chapter with a world in it. ||| I left each one out in turn, and played it. ||
Every time, no console, no world, and empty pools. ||| So the chapters are the switch.
||"

### 3. The library, and the mode

**Screen:** `story.json`, the last two lines of the mastlib list. Then `kestrel_verge.amd`,
the Scenario chapter: `story` becomes `campaign`.

**Say:** "First, I look in one file I never edit. || Story dot json is the list of
libraries. || The last two lines are the universe's own, | and then the admiral's. ||| If
yours has both, leave it alone. || That line does nothing by itself. ||| Now for the mode. ||
One word changes, from story to campaign. || For the crew, that's all it is: a word.
||"

### 4. The chapters come home

**Screen:** The end of `kestrel_verge.amd`. Paste the four chapters. Highlight Hollin
Prime, then Maren, then the two research steps.

**Say:** "Now the four chapters from the lab. || They go at the very end of the file, |
so nothing above them moves. ||| There are two worlds: | Hollin Prime, which never runs dry, and
the Lamp, which does. ||| An admiralty chapter with two dials. || One officer, Commodore
Maren. || And a ladder of two research steps. ||| The Compact's home is the system every
game starts in. || It still gets its world, | and it's the first one that says
unlimited. ||"

### 5. An honest number

**Screen:** The table in Step 5 of the page.

**Say:** "Now, the numbers, and I'll be straight with you. || I wrote nothing for
starting ore, | so the game used its own three hundred. || And it started with three
thousand six hundred. ||| Part of that is the pace, which is yours to set. || Most of it
is a test setting the game's makers left on. || It multiplies every stock and every
yield by eight. ||| Research isn't multiplied at all. || So for now, the ladder is cheap and
the tanks are huge. ||| Don't balance anything yet. || Just never start with less than a
headquarters costs. ||"

### 6. Lint

**Screen:** Save. `sbs lint MyUniverse`. The same three warnings.

**Say:** "I save, and I run lint. || It's the same three warnings as before, | on the
same lines. || The four chapters add none. ||"

### 7. Both seats filled

**Screen:** `sbs run server,admiral,helm,comms -m MyUniverse map=0`. The ten rows of
Step 7.

**Say:** "Now let's play it with both seats filled. ||| The admiral sees one world at
home, and it's mine. || I build a headquarters. | It takes about half a minute. ||| Then
an extractor, an academy, a shipyard and a lab. || The ore starts to climb. ||| The
shipyard offers Commodore Maren, | and she brings three ships. || The lab offers my
first step. | Forty seconds later, it's done, | and it offers the second. ||| And over
on the bridge? || Five hundred credits, and three leads. | Nothing at all has changed. ||"

### 8. The empty seat

**Screen:** A new game with `server,helm,comms,weapons`. The Quest Log. Then the table
in Step 8.

**Say:** "Now the question you should ask first. || What does this cost a table that
doesn't want an admiral? ||| So I walked the whole capstone evening, | with these
chapters in the file and that chair empty. ||| Every row came out the same. || The
world is there, as scenery. | The pools sit full, and never move. ||| So you can ship
one universe to both kinds of table. ||"

### 9. How it ends, and what comes back

**Screen:** The Goals chapter, `Win:` highlighted. Then the table in Step 10.

**Say:** "How does it end? || The admiral's game has no ending of its own here. || The
campaign ends where your goals chapter says. | That's your win line. ||| And when I stop
and continue? || The pools come back, to the last unit. || So do all five platforms, |
the fleet, and the research. ||| Twenty seconds in, the extractor's working again. ||"

### 10. Your turn

**Screen:** The exercise.

**Say:** "Now it's your turn. || Write your own home world, two officers, | and a ladder
of three steps. ||| Then take the admiral out, by changing one key, | and check the
crew's game is the same. || Then put it back, | and hand that chair to a friend. ||| Next
time is the capstone. || It works with an admiral in the file, or without. ||"
