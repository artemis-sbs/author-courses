# C6-4 video script - The episode, your repeatable unit

> **STATE ON 2026-10-09.** Written and measured today against the released tools: `sbs`
> 0.13, the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions
> `b20726f`, the Open Universe engine library in `__lib__`). Everything was run by script
> in the game's stand-in (the mock), from a copy of the mission placed where its save
> cannot reach a player's own. **Nothing in this lecture has been run in the real game,
> and nobody has seen any of its screens.** The fight in particular: the stand-in was
> told ships had been destroyed. Nobody fired at anything.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 3 leaves it: both files match `c6-03-designing-a-session\example\` |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| VS Code | `MyUniverse` open, both files in tabs side by side, font size raised |
| Game | Closed. Started on camera in scene 7 with `sbs run server,helm,science -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-09, with the page's own files:**

1. The finished files lint `clean` and play with no errors and an empty
   `mast.runtime.log`.
2. After evening 1's home step, Two of Five is Active and Bait is hidden.
3. On arrival at (-2, 3): three ships on the raiders' side, the guarded card, The Dunlin
   charted, Bait Active.
4. After one ship is reported destroyed Bait is still Active. After two it is Done and
   Enter It Twice is Active.
5. Engaging Enter It Twice: the ship at (0, 0), credits up by 350, Three of Five Active.
6. Charted Locations holds Kestrel Relay, The Wren and The Dunlin.
7. With no `Guards:` line on the Dunlin there was no hostile ship at (-2, 3) at all.
8. Every row of the tables in Step 4: 6 variants, each linted and played.

**Read in the notes, not run:** what Storm's Beacon's makers wrote about their episode
pattern. Their pattern was read. Their mission was never started.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. The fight, and how long two ships of three take a crew.
2. The nebula round the Dunlin.
3. The Quest Log, the cards.

## Scenes

### 1. Cold open

**Screen:** Evening 1's four records beside evening 2's, in two columns.

**Say:** "Evening one took a whole lecture to build. || Evening two is going to take a
few minutes. ||| Because today, you write down what stays the same. || That's called a pattern,
| and a campaign is one pattern that you fill in twenty times. ||"

### 2. Build it once

**Screen:** The table in Step 1 of the page.

**Say:** "The people who built Storm's Beacon made themselves a rule. || Adding an
episode has to be a few mechanical edits, | and no new thinking about how. ||| And they
tested it. | They added a third episode to a campaign that had two. || It held, so they
wrote the rest. ||| You already have what an episode needs. || A lead that ends at a
place. | A line that shows the next step. || Guards and cover on a landmark. | And a
step that ends at home and pays. ||| None of that's new today. || Today's about writing down what stays the same, | so you never have to work it out again. ||"

### 3. The pattern

**Screen:** The pattern block in Step 2, with the capital-letter slots highlighted.

**Say:** "So here's evening one, with everything taken out that belongs only to evening
one. ||| A landmark, and three steps. || The words in capitals are the slots. ||| The
evening's number, two digits. || The system, twice, and it must be the same both times.
|| What's in the way. || What finishes the objective. | And what it pays. ||| Everything else is yours: | four titles, and four short pieces of text. ||| Keep the pattern
in your campaign page, | so it's there every time you sit down. ||"

### 4. Four endings

**Screen:** The table of endings in Step 2.

**Say:** "The slot that changes the evening most is the ending of the objective. |||
Scan, and it's an evening about finding something out. || Destroy, and it's a fight they
can't walk away from. ||| Signal, and it's a conversation, | which we'll write in a
later lecture. || And then there's reach, | for an evening that's about getting somewhere further on.
||| One of those four goes in the slot, | and the rest of the pattern doesn't change at all. ||"

### 5. Evening two

**Screen:** `campaign.md`: the Evening 2 sheet. Then `kestrel_verge.amd`: add The Dunlin.
Find Two of Five, add its `Then:` line. Add Bait, Enter It Twice, Three of Five.

**Say:** "The sheet first, as always. || Then the landmark, the Dunlin, | in cloud, and
guarded. ||| Now look at the open. | I don't have to write it. || It's already there,
because it was last week's hook. | It only needs its next step. ||| So I write three
things. || The objective: this one's a trap, | and they have to break it. || Then the way home, | and the hook for evening three. ||| That's the rhythm of the whole campaign. || Every time you sit down, the open's already written, | and you write a place, a deed, a way home, and the next hook. ||"

### 6. Two of three

**Screen:** Bait's `Done when: destroy 2 enemies`. Then the Dunlin's `Guards:` line.

**Say:** "Two details in that objective. ||| The game sends three guards, | and I ask
for two. || A fight to the very last ship | goes on five minutes after it stopped being
fun. ||| And the fight needs the guards line. || I measured it without: | there was
nothing hostile there at all, | and the evening couldn't be finished. ||| So an objective that ends with destroy | always gets a guards line on its landmark. ||"

### 7. Lint and play

**Screen:** Save. Lint: `clean`. Run the game. Evening 1 quickly. Engage Two of Five.
One ship, then two. Engage Enter It Twice. Charted Locations.

**Say:** "Lint says it's clean. || So I play evening one through to its hook, | and I engage the new lead. |||
Here's the Dunlin, the warning, and the new step. || One ship down, and it's still open. | Two,
and it's done. ||| Then we're home and paid, | and there's the lead for evening three. ||| And the
charted places now have both boats in them. ||"

### 8. Close

**Screen:** The table "What you need to know about a pattern".

**Say:** "So the open of every evening is the hook of the one before. || You never start
from nothing. ||| Renumber every key when you copy the pattern. || If you don't, the game keeps the first record with that key, | and quietly drops your new evening. || Lint does tell you, by name. ||| And the pattern's yours to break. | A tentpole can be longer. ||
Next time, all twenty evenings, on one page. ||"
