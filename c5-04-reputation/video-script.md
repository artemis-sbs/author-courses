# C5-4 video script - Reputation

> **STATE ON 2026-10-08.** Written and measured today against the released tools: `sbs`
> 0.13, the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions
> `b20726f`, the Open Universe engine library built 2026-10-05). Everything was run by
> script in the game's stand-in (the mock), from a copy of the mission placed where its
> save cannot reach a player's own. **Nothing in this lecture has been run in the real
> game, and nobody has seen any of its screens.**
>
> **This lecture teaches less than the plan lists, on purpose.** Measured today:
>
> - `Standing:` (or `earns` in a `Reward:`) on a quest in the Narrative chapter is kept
>   on the shared story, not on the ship. Nothing a player meets reads it there. The
>   page says so and teaches the two deeds that do reach the ship: a finished job and an
>   answer in a call.
> - `Standing:` on a job is thrown away. A job is always worth 5 for each tier.
> - `Rival when:` on a captain is read by nothing. It is not on the page. Lecture 8 will
>   need it.
> - An alliance is offered only to a side the crew has a ceasefire with. A side written
>   `neutral` never offers one.
> - Lint warns on all six threshold dials, though the game reads them.
>
> When any of these is mended, this page changes.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 3 leaves it: `kestrel_verge.amd` matches `c5-03-sides-diplomacy-goods\example\` |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | `MyUniverse` open, `kestrel_verge.amd` in a tab, font size raised |
| Game | Closed. Started on camera in scene 8 with `sbs run server,helm,comms -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-08, with the page's own files:**

1. The finished file lints `clean` and plays with no errors (146 labels run) and an empty
   `mast.runtime.log`. `story.mast` is unchanged from Lecture 2.
2. The standing table in Step 1, row by row, from the game's own function.
3. The thresholds in Step 4, from the game's own functions: tier 2 at 20 and tier 3 at
   50; a foe deals at 20; a ceasefire costs 600, 400, 200 and 0 at 0, 10, 20 and 30, and
   600 at -50; an alliance at 60; pay times 1.0, 1.2, 1.5 and 2.0 at 0, 20, 50 and 100.
4. Step 6, in order, each press made the way the game reports a press. At standing 0
   Hollin Compact is sent Hail Hollin Compact and Escort (250 cr), and no Patrol. The
   line picked is "Hollin Compact. State your business, captain." The hail's buttons are
   the three answers and Leave. After the levy: 400 credits, standing 20, Patrol (240 cr)
   and Escort (300 cr), and the line picked is "Kestrel Relay knows your ship, captain."
   Escort taken and engaged: the ship is at 3, 1, the job is Done, credits 700, standing
   25.
5. At the Gleaners: Negotiate Ceasefire is sent at 700 credits. After the bold answer:
   standing 20, Salvage (180 cr) is sent, and the ceasefire takes 200 credits. Two more
   bold answers: standing 57, fearsome score 100.
6. The save file holds the scores under the ship's name, and a second start reads them
   back: standing 25 and 57, and the ceasefire.
7. A tier 2 job finished at standing 20 leaves standing 30.
8. With both of the Gleaners' values at 100 and a ceasefire made, the station is sent
   Propose Alliance; pressing it makes the two sides allies, and the station then offers
   what the crew's own stations do. With Hollin at 100 and no ceasefire, no such button.
9. The six dials, written with other numbers, change the thresholds as the page says.
10. Every row of the three tables in Step 5: 41 variants, one change each, each linted
    and played. They were run on the finished file with the six dial lines written out
    at the game's own numbers; that file and the finished one play the same, line for
    line.

**Read in the code, not run:** that a refused answer tells the crew "You cannot afford
that."; that standing is kept by the ship's name.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. A hail: where the station's line appears, and that the answers are buttons on Comms.
2. **Patrol (240 cr)** appearing after the levy, without selecting the station again.
3. That nothing on any screen shows a standing as a number.
4. The Gleaners' station being selectable and hailable while their fleet is hostile.
5. What the crew is told when a job is finished and standing moves. The code sends a
   card that reads "Word of your deeds spreads among the sides."
6. What a player sees when a `Tier:` is not a number.

## Scenes

### 1. Cold open

**Screen:** Comms on Hollin Compact, before the levy and after: Patrol appears, Escort's
pay rises.

**Say:** "Last time, your three sides were just there. || They met every crew the same
way, | whatever that crew had done. ||| Today they start to remember. || Each side gets
something it values. | The crew earns a name with each one, | by what they say and by the
work they finish. || And that name changes prices, and jobs, | and how a station says
hello. ||"

### 2. What a side values

**Screen:** The table of seven trait pairs on the page. Then `kestrel_verge.amd`: add a
`Values:` line to each of the three sides.

**Say:** "The game measures a captain on seven pairs of traits. || There's honest or liar, fearsome or cowardly, |
generous or selfish, and four more. ||| Neither end is the good
one. || A navy can value doing it by the book, | and a gang of wreckers can value being
feared. ||| So each side gets one line, Values, | with the traits it cares about, and a
weight on each. || The farmers want honest and generous. || The miners want it by the
book. || And the wreckers want fearsome. ||"

### 3. Standing is an average

**Screen:** The standing table for Hollin on the page. Highlight the rows for 20 and 20,
then 35 and 0, then 100 and 0.

**Say:** "From those, the game works out one number for each side, called standing. ||
It starts at zero, | and it's an average across what that side values. ||| Look at what
that means. || Twenty in both of Hollin's values is a standing of twenty. || But honesty
alone has to reach thirty-five to do the same. || And honesty alone, pushed all the way, stops at fifty-seven. ||| So a crew can't win a side over by being good at one thing. ||
They have to be the whole of what that side admires. ||"

### 4. A deed in work

**Screen:** The Jobs chapter. Add `Done when: reach 3, 1` to Escort and `Tier: 2` to
Patrol.

**Say:** "How does the crew earn it? | There are two ways, and the first is work. || When
a ship finishes a side's job, | its standing with that side goes up by five. || I write
nothing for that. | It comes with the job. ||| But the template's jobs don't have endings
yet, | so I give the escort one: | done when the ship reaches the miners' home. || And I
give the patrol a rank, tier two. || A side only offers tier two work | to a ship at
twenty or more. ||"

### 5. A deed in talk

**Screen:** End of the file. Type the Dialogue chapter: the Hollin hail and its three
short records. Highlight the guard, then the `earns` clause.

**Say:** "The second way is what the crew says. || This is a call, | and if you've taken
Class 2 you know its shape. || If you haven't, this is all of it. ||| Speaker is the side.
|| When comms means this opens when the crew hails that side's station. || A line
starting with a percent sign is something the station says. || And a line starting with a
hyphen is an answer, which becomes a button. ||| Now the two parts that are about today.
|| After the semicolon is what the answer does: | it costs a hundred credits, | and it
earns twenty honest and twenty generous with Hollin. || That answer is the deed. ||| And up here,
in curly brackets, is a guard. || This line is only said to a ship at twenty or more. ||
So the station greets a friend differently, | and that's how the crew finds out where
they stand. ||"

### 6. Two traps in a call

**Screen:** Highlight the two guarded lines. Then the Gleaner hail; highlight the answer
with no `costs`.

**Say:** "Two things to know before you write your own. ||| First, guard every line, or
none. || A line with no guard can always be said, | so a friend would hear either one, at
random. ||| Second, an answer can be given again. || The crew can hail as often as they
like, | and the deed happens every time. || That's why the levy costs money. ||| Here's
the wreckers' call, and I've left the cost off on purpose. || Watch what that does when I
play it. ||"

### 7. The thresholds

**Screen:** The threshold table on the page. Then lint: clean.

**Say:** "Standing only matters where it crosses a line. || At twenty, a side offers
better work, | and an enemy will deal with you at all. || Every point above zero adds one
percent to the pay. || A ceasefire costs twenty credits for each point short of thirty. |
So it's six hundred to a stranger, and free to a friend. ||| You can move every one of
those lines, | and the page shows you how. || I'm leaving them where they are, | and lint
says clean. ||"

### 8. Play it: the farmers

**Screen:** `sbs run server,helm,comms -m MyUniverse map=0`. Comms: Hollin Compact, no
Patrol. Hail; the cold line; Pay the relay levy. Select the station again: Patrol, and
Escort at 300. Hail again: the warm line. Take Escort; Helm: Engage.

**Say:** "Here's Hollin Compact, with an escort for two fifty, and no patrol. ||| I
hail them, and I get the cold line, the one for strangers. || I pay the levy. ||| Now
look at the station again. || There's the patrol, and the escort pays three hundred. ||
I hail once more, and this time they know my ship. ||| So I take the escort, | and on
Helm I engage it. || It's done on arrival, | and that's five more with Hollin. ||"

### 9. Play it: the wreckers

**Screen:** Helm: Engage The Breaking Yard. Comms: the Gleaners' station; Negotiate
Ceasefire is there. Hail; the bold answer. Station again: Salvage, and the ceasefire.
Press it. Then the bold answer twice more.

**Say:** "Now for the Gleaners. || The ceasefire is on offer, | and it would cost me six
hundred. || I don't press it. ||| I hail them instead, | and I tell them I go where I
like. || That's one bold answer, and my standing is twenty. ||| Look at the station now.
|| They'll give me work, | and the ceasefire costs two hundred, | so I take it. ||| And now
the trap I left. || I give the same answer twice more, for nothing, | and I'm at
fifty-seven with people who were shooting at me. || It stops there, because they value
something else as well. || But that's what a free deed does to a story. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Give each of your sides two or three values, | and say
out loud why they'd care. || Rewrite both calls in their voices, and keep the guards. ||
And fix my trap: | make being feared by one side cost the crew something with another.
||| Next time, we draw the map. ||"
