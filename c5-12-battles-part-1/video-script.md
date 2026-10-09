# C5-12 video script - Battles, part 1: how dangerous a system is

> **STATE ON 2026-10-09.** Written and measured against the released tools: `sbs` 0.13,
> the published v1.4.0 libraries (sbs_utils `4941820e`, LegendaryMissions `b20726f`, the
> Open Universe engine library built 2026-10-08). Everything was run by script in the
> game's stand-in (the mock), from a copy of the mission placed where its save cannot
> reach a player's own. Ships were counted, not fought: no weapon fired. **Nothing in
> this lecture has been run in the real game, and nobody has seen any of its screens.**
> The one number about the real game, 190 fighting ships, is the game makers' own, from
> a test with no consoles connected.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 9 leaves it: the six `.amd` files match `c5-09-organizing-a-big-universe\example\`; `story.mast` and `settings.yaml` are untouched since Lecture 2 |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | `MyUniverse` open; `settings.yaml`, `story.mast` and `kestrel_verge.amd` in tabs, font size raised |
| Game | Closed. Started on camera in scene 9 with `sbs run server,helm,comms -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-09, with the page's own files:**

1. Lint gives the three `ledger_read` warnings of Lecture 9 and nothing else. The
   mission plays with no errors (116 labels run) and an empty `mast.runtime.log`.
2. The game holds Difficulty 4, `DANGER` Quiet, `ENCOUNTERS` Dormant, terrain "some".
3. The table of ships per fleet in Step 1 is the game's own fleet tables, read while it
   ran.
4. An enemy system held 1, 3, 4, 6, 11 and 24 Gleaner ships at Difficulty 1, 3, 4, 5, 8
   and 11, in 1, 2, 2, 2, 3 and 4 fleets.
5. At The Tern: one `pirate_longbow` marked as the landmark's guard, on the raiders'
   side, 7,620 from the ship, and the card `The Tern is guarded - hostiles on approach.`
6. At the Gleaners' home, Difficulty 4: one Torgoth destroyer and four fighters named
   The Gleaners Red 1 to 4, the nearest 1,758 away. Fighters were there on five visits
   of seven.
7. At The Bone Pile: three guards (`torgoth 7`) 17,574 away and four Gleaner ships
   42,570 away. With the guards removed by script and the system left and entered
   again: no guards, no Threat card, and the save holds `guards_cleared`.
8. `DANGER`: 14, 33 and 54 enemy systems of 169. `ENCOUNTERS`: nearest ship 18,606 on
   arrival, 40,701 dormant.
9. Every row of the tables in Step 7: 40 variants linted, 22 played one at a time, and
   16 `Guards:` lines played in one game on sixteen landmarks.

**The game makers' numbers, not ours:** about 190 fighting ships at full speed, and
100,000 rocks, on the real game with no consoles connected (2026-07-03).

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. The Difficulty slider on the start screen, and that it starts at the number in
   `settings.yaml`.
2. The Threat card on a console, and on which consoles.
3. Any fight. Whether one light cruiser can take three Torgoth at tier 7 is a question
   for a play test, not for this page.
4. The four fighters at a foe's home in the real game, and what they look like. In the
   stand-in they are named for the Gleaners and use the crew's own fighter model.
5. What a full bridge of consoles does to the 190.
6. Guards staying gone after a real fight and a real save.

## Scenes

### 1. Cold open

**Screen:** Helm arriving at The Tern. The card: The Tern. Then the Threat card.

**Say:** "Up to now, you've been writing a universe with enemies in it, | and letting
the game decide how many. || Today you take that over. ||| By the end, you'll know how
many ships are waiting in every kind of system, | and which line of which file put them
there. || And you'll have a budget, | a number you wrote down on purpose. ||"

### 2. Three places the ships come from

**Screen:** The first table in Step 1 of the page.

**Say:** "There are only three places an enemy ship comes from. ||| One is an enemy
system, | the kind the game rolls from your mixes in Lecture Five. || Two is a foe's
home, where their station is. || And three is a landmark with guards on it. ||| You've
already written all three. || What you haven't done is count them. ||"

### 3. Fleets and tiers

**Screen:** The table of ships per fleet in Step 1. Run a finger along the Torgoth row.

**Say:** "Enemies come in fleets, and a fleet has a tier, | from one to eleven. || This
table is how many ships are in one fleet, at each tier, | for each of the six kinds of
ship. ||| Follow the Torgoth row. || It's one ship at the bottom, three in the middle, |
and six at the top. || And the ships get heavier as the fleet gets bigger. || At the top
tier, | that's six of the largest thing they fly. ||"

### 4. The Difficulty number

**Screen:** `settings.yaml`, line 53. Then the table in Step 2. Change 5 to 4.

**Say:** "So what sets the tier? || One number, called Difficulty, | and it lives in the
settings file, where you named your ship back in Class One. ||| Here's what it does to
one enemy system. || At five, there are six ships. | At eight there are eleven, | and at eleven
there are twenty-four. ||| It grows that fast because Difficulty counts twice. || It sets how
many fleets there are, | and it sets the tier of every one of them. ||| My universe is
a backwater with one ship in it, | so I'm setting it to four. ||"

### 5. Guards with a number

**Screen:** `kestrel_verge.amd`, The Bone Pile. Change `Guards: torgoth` to
`Guards: torgoth 7`. Then The Tern: add `Guards: pirate 2`.

**Say:** "In Lecture Five you put guards on the Bone Pile, | with just the kind of
ship. || Written like that, the guards follow Difficulty. ||| Put a number after the
word, and that's their tier, whatever Difficulty says. || Seven is three Torgoth
ships, every time. ||| And I'm adding a small guard to the Tern, | because somebody is
picking at that wreck. ||| There are four things to know about guards. || The crew gets
a warning card. || The guards wait by the landmark, not by the crew. || They're raiders,
so no ceasefire calls them off. | And once they're destroyed, they stay gone. ||"

### 6. A foe's home

**Screen:** The Step 4 table. Then the note about the four fighters.

**Say:** "A foe's home always has one fleet, at the Difficulty, | and it waits close.
|| It's the one place your crew arrives with the enemy already on top of them. |||
There's also something there you didn't write. || Most of the times I visited, | the
station launched four fighters of its own. || No line of yours sets that number, | so
just add four when you count. ||"

### 7. How thick, and how close

**Screen:** `story.mast`, the two travel lines. Paste the card under them. Highlight
`"Quiet"` and `"Dormant"`. Then the two small tables in Step 5.

**Say:** "There are two more dials, and they go in the story file, | right under the
two travel lines from Lecture Two. || It's a card, so copy it from the page. | The
only words you change are the two in quote marks. ||| The first is Danger. || It doesn't
add ships to a system. | It makes more systems enemy systems. || From quiet to
dangerous, | mine went from fourteen enemy systems to fifty-four. ||| The second is
Encounters. || Dormant puts an enemy system's fleets at the far edge, | so the crew
gets time to talk before the shooting starts. ||| Spell both words exactly as they are
on the page. || A wrong word isn't an error. | It's just the gentle setting, and nobody
tells you. ||"

### 8. The budget

**Screen:** The Bone Pile table in Step 6. Then the four facts under it.

**Say:** "Now add it up, for your worst system. || Mine is the Bone Pile. || At
Difficulty four it holds four Gleaner ships, | and three guards, so that's seven. || At eleven
it would be twenty-seven. ||| So how many is too many? || Here's what's known so far. || A
system only exists while a crew is in it. || So what counts is your worst system, |
times the crews that can be in different systems at once. ||| The people who make the
game pushed it until it slowed down, | and that was at about a hundred and ninety ships
fighting at once, | with no consoles connected. || Nobody has measured it with a full
bridge. || So stay a long way under that number. ||"

### 9. Check, and fly it

**Screen:** `sbs lint MyUniverse`: the same three warnings. Then
`sbs run server,helm,comms -m MyUniverse map=0`. Engage The Third Colony: the two cards.
Engage The Breaking Yard: the fleet close by.

**Say:** "Lint gives me the same three warnings as last time, and nothing new. || But
lint doesn't read the settings file at all, | so read the checklist on the page. |||
Now let's fly it. || First we go to the Tern, | and there's her card, and then the warning. || And
then the Gleaners' home. || This is what close looks like. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Decide who your game is for, and set Difficulty to
match. || List every system your story visits, | and count the three sources for each
one. || Then write your budget at the top of your file. ||| Next time, we stage a battle
ourselves, | at one place, at the moment the story gets there. ||"
