# C5-13 video script - Battles, part 2: a battle that waits for the story

> **STATE ON 2026-10-09.** Written and measured against the released tools: `sbs` 0.13,
> the published v1.4.0 libraries (sbs_utils `4941820e`, LegendaryMissions `b20726f`, the
> Open Universe engine library built 2026-10-08). Everything was run by script in the
> game's stand-in (the mock), from a copy of the mission placed where its save cannot
> reach a player's own. The story was walked by script: the script jumped the ship, sent
> the ledger's signal, and told the game "the ship destroyed this". No weapon fired and
> no console was connected. **Nothing in this lecture has been run in the real game, and
> nobody has seen any of its screens.**

The companion page is `lesson.md`; the finished `story.mast` is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 12 leaves it: `kestrel_verge.amd`, `story.mast` and `settings.yaml` match `c5-12-battles-part-1\example\` |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | `MyUniverse` open; `story.mast` and `kestrel_verge.amd` in tabs; word wrap OFF so the long line shows as one line |
| Game | Closed. Started on camera in scene 8 with `sbs run server,helm,comms -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-09, with the page's own files:**

1. Lint gives the three `ledger_read` warnings and nothing else. The mission plays with
   no errors (115 labels run) and an empty `mast.runtime.log`.
2. Arriving at -4, -3 at the start, with the goal hidden: seven hostile ships (four
   Gleaners, three guards), no battle line, no card of ours.
3. After The Tern and the ledger's signal, arriving with What the Gleaners Keep open:
   that step is Done, Break the Bone Pile is open, and there is one more Gleaner fleet
   of four ships (three destroyers and a leviathan), the nearest 7,014 from the ship.
   The info panel is sent our sentence under the title Threat.
4. Leaving for -3, 0: no ship of The Bone Pile is left. Coming back: one battle line
   again, of five ships this time, not two lines.
5. A second game continued from that save starts at -4, -3 with the goal open and a
   battle line of five, and is sent the card.
6. Four Gleaner kills reported: the game says game over, a win, with the goal's `Win:`
   sentence.
7. Without `await delay_sim(1)`: no battle line at the story's arrival.
8. With the card waiting on a step that is then finished (The Breaking Yard): a battle
   line while it is open, none on the next arrival after it is Done.
9. Asked about 400 seeds, the game makes -4, -3 an enemy system in 245.
10. Every row of the tables in Step 5: 35 variants linted, 33 played.

**Read in the code, not run:** that a `//signal` route runs once for each console; that
a second ship arriving in a system that is already built does not say `universe_arrived`.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. The battle line on Helm or Science, and whether 6,000 each way reads as "between you
   and the Bone Pile" on a real screen.
2. Our card on a console, beside the game's own Threat card for the guards.
3. The ships attacking. In the stand-in they are on the Gleaners' side and hostile to
   the crew; nobody watched them fight.
4. A ceasefire with the Gleaners while the battle line is on the field.
5. A real Continue from the game's start screen, landing at The Bone Pile.
6. The card with consoles connected. If the battle line is doubled, the route line is
   wrong on the page.

## Scenes

### 1. Cold open

**Screen:** Helm arriving at The Bone Pile. Three cards in turn: the place, the guards,
ours.

**Say:** "Last time, you learned to set the odds. || How many systems have enemies, how
big the fleets are, | how close they wait. ||| But a story has one place where odds
aren't good enough. || When the crew gets to the end, | the fight has to be there. |||
Today you stage that one fight yourself. ||"

### 2. Why the dice aren't enough

**Screen:** The goal record, Break the Bone Pile. Highlight its last line. Then the
Breakers region and `Enemy mix: 60%`.

**Say:** "Here's the end of my story. || It says four Gleaner hulls stand between you
and them. ||| Well, do they really? || Last time I counted four Gleaner ships at the Bone Pile. ||
But they're only there because the game rolled an enemy system, | and every new game
rolls again. ||| In the game I measured, | five of the nine systems in that region were
not enemy systems. || If the Bone Pile is one of those, | the crew arrives for the last
fight and finds three raiders. ||"

### 3. The card

**Screen:** `story.mast`, scrolled to the very end. Paste the card. Word wrap off: the
long line runs off the right of the window.

**Say:** "So here's a card. || It's the only new piece of MAST in this whole class, |
and you don't need to be able to write it. || You copy it from the page, | to the very
end of the story file. ||| One of these lines is long. || It's one line, so don't
break it. |||"

### 4. Read it, top to bottom

**Screen:** The card. Highlight each line in turn as it is named.

**Say:** "Let's read it once, from the top. || The line with two slashes is a route. ||
The game says, a ship has arrived, | and this block hears it. || The rest of that line
says, only in this system. ||| Then it waits one second. || Then it asks, is this step
of the story open right now? | If not, it stops. ||| And if it is, | it finds where the
system is, makes one fleet, | and shows the crew a card. ||"

### 5. The seven words

**Screen:** The "words you may change" table on the page, beside the card. Point at
each in the card.

**Say:** "There are seven things you change, and nothing else. ||| The two numbers of
the system, | which you copy from the landmark. || The key of the step, in quotes. ||
The kind of ship, and the tier, | and you know both of those from last time. || The key
of the side they fight for, | which has to come first inside those quotes. || How far
away they form up. || And the sentence the crew reads. ||"

### 6. Shared, and one second

**Screen:** Highlight `//shared/signal`. Then highlight `await delay_sim(1)`.

**Say:** "Two parts of this card look like details, and they aren't. ||| The first is
the word shared. || A route without it runs once for every console that's connected. ||
Anything that makes a ship goes on a shared route, | or every console makes its own
fleet. ||| The second is the one-second wait. || When the crew arrives, | the game
finishes one step and reveals the next, at that same moment. || Without the wait, my
card looks too early. | It sees a hidden step, and it makes nothing. || I took that
line out to check, and that's exactly what happened. ||"

### 7. When the battle is there

**Screen:** The five-row table in Step 3 of the page.

**Say:** "So when is the battle there? || I played every case. ||| If the crew wanders
in early, there's nothing, | because the step is still hidden. || If they arrive on the
story's business, it's there. ||| If they run and come back, there's one battle line,
not two, | because the system is taken down when they leave. || After a Continue, it's
there again. || And once the step is done, it's gone. ||| There's one warning here. || The tier on
the card doesn't move with Difficulty, | so add it to your budget from last time. ||
Mine comes to eleven or twelve ships, | which is a lot for one cruiser. ||"

### 8. Check, and play it

**Screen:** `sbs lint MyUniverse`: the same three warnings. Then
`sbs run server,helm,comms -m MyUniverse map=0`. The Tern, the Assay Office hail, then
Engage What the Gleaners Keep: three cards. Leave, come back.

**Say:** "Lint gives the same three warnings as before. || And once again, it can't see
most of what goes wrong on this card, | so use the list on the page. ||| Now let's
play the story. || The Tern first, and then the ledger. | And then the place the
Gleaners won't talk about. ||| There are three cards. | The place, the guards, and
mine. || Now I'll run, and come back. || There's still one battle line. ||"

### 9. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Find the one place in your story where the fight has
to be there. || If you don't have one, you don't need this card. ||| If you do, paste
it, | change the seven words, and then go there early on purpose. || There should be
nothing waiting. ||| Next time, somebody else gets to play your universe, from above. ||"
