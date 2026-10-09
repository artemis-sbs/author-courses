# C5-5 video script - The map

> **STATE ON 2026-10-08.** Written and measured today against the released tools: `sbs`
> 0.13, the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions
> `b20726f`, the Open Universe engine library built 2026-10-05). Everything was run by
> script in the game's stand-in (the mock), from a copy of the mission placed where its
> save cannot reach a player's own. **Nothing in this lecture has been run in the real
> game, and nobody has seen any of its screens.** A sky, a nebula, a color and a piece
> of music are exactly the things the stand-in cannot show: what was measured is that
> the game was asked for them.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 4 leaves it: `kestrel_verge.amd` matches `c5-04-reputation\example\` |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | `MyUniverse` open, `kestrel_verge.amd` in a tab, font size raised |
| Paper | A grid of squares, eleven by eleven, for scene 5 |
| Game | Closed. Started on camera in scene 9 with `sbs run server,helm,comms -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-08, with the page's own file:**

1. The finished file lints `clean` and plays with no errors (142 labels run) and an empty
   `mast.runtime.log`. `story.mast` is unchanged from Lecture 2.
2. The four dials are read as 8, 12, 20 and 60 in 100. The count of kinds in the table
   under Step 2 is the game's own, over the 169 systems nearest home, with one seed.
3. With the regions: all 25 systems of the Hollin Fields hold no enemy system and 5
   station systems; of the 9 systems of the Breakers, 7 are enemy systems and none is a
   station system.
4. On arrival at home the game is asked for the sky `sky1-blue`. In the Breakers it is
   asked for `sky-neb2-rvb` and the music `artemis2`. At 3, 1, in no region, it is asked
   for nothing.
5. The arrival card is handed: `Kestrel Relay` at home; `The Hollin Fields` and `(1, 1)`
   in a system of the Fields with no landmark; `The Tern`, `Assay Office` and `The Bone
   Pile` with their lines; `The Breakers` and `(-3, -2)` at the Gleaners' home.
6. The Tern is a wreck named The Tern, marked as a derelict. Assay Office is a station on
   the Deepwell's side with the model `starbase_industry`, and Comms is sent Escort
   (250 cr) for it.
7. At The Bone Pile: two Torgoth ships marked as the landmark's guards, on the raiders'
   side, beside five ships of the Gleaners that the enemy system brought.
8. After the four leads, Charted Locations holds Kestrel Relay, The Tern, Assay Office
   and The Bone Pile, and all four leads are Done.
9. Every row of the tables in Step 6: 36 variants, one change each, each linted and
   played.

**Read in the code, not run:** the chances in Step 1; that guards do not come back once
destroyed; that Science scanning a derelict pays salvage; the color word after `nebula`.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. The sky and the music changing on arrival in a region, and on which windows. The game
   is asked to change them for the server. Whether the consoles follow was not seen.
2. A region's `Color:` anywhere.
3. The nebula round The Tern and its color; the asteroids round The Bone Pile.
4. The guards attacking, and not returning after they are destroyed.
5. The Tern on Science, and what a scan of it says.
6. What a station with a model the game does not have looks like.

## Scenes

### 1. Cold open

**Screen:** The arrival card reading The Bone Pile. Then Charted Locations with four
places.

**Say:** "So far, you've written who lives in your universe, | and the game has decided
what every system looks like. || Today you take some of that back. ||| You'll change how
the whole galaxy is made, with four numbers. || You'll give two stretches of it a name
and a sky. || And you'll put three more places on the map by hand. ||"

### 2. How a system is filled

**Screen:** The two tables in Step 1 of the page.

**Say:** "First, how the game fills a system you never wrote. || It rolls once for each
one, | and the roll comes from the seed, | so it's the same every time for that system.
||| About one in seven is a station. | About one in seven is full of enemies. || Some are
nebula, a few are anomalies, | and half of them are empty. ||| And on top of that, a
system might have loot, | or a dead ship to scan, or a minefield. || Every one of those
chances is a number you can change. ||"

### 3. The dials

**Screen:** `kestrel_verge.amd`, the title record. Add the four dial lines. Then the
count table on the page.

**Say:** "Those numbers are called dials, | and they go in the title record, at the top
of the file. ||| My universe is a frontier that was abandoned. || So I want few ports, a
lot of cloud, | and a lot of dead ships, | and that's four lines. ||| And here's what they
did, counted over the nearest hundred and sixty-nine systems. || Stations went from
twenty-five to fifteen, | and nebulas from twenty-nine to forty. ||| One warning, and
it's the big one in this lecture. || Write the percent sign. || Leave it off, and twelve
means twelve hundred percent, | and lint won't say a word. ||"

### 4. A region

**Screen:** Add the Regions chapter in front of Landmarks. Type The Hollin Fields.
Highlight `Center`, `Radius`, `Skybox`, then the two dials.

**Say:** "A dial in the title record is the same everywhere. || A region is a patch of
the map where it's different. ||| It has a center, which is a system, and a radius. ||
A region is a square, so a radius of two | is five systems on a side. ||| It has a sky,
from a list of seven on the page. || And it can have any of the dials. || Here I've said,
no enemy systems at all, and more stations. || So this is safe, farmed space around the
home port. ||"

### 5. A second region, and the grid

**Screen:** Type The Breakers. Then the paper grid: mark the three homes, draw both
squares.

**Say:** "And here's the opposite: the Breakers. || There's a red sky, different music,
| enemies in most systems, no ports, and mines. ||| I drew it on paper first, | and I'd
ask you to do the same. || Mark each side's home, and draw each region as a square. |||
It shows you two things. || One is whether two regions overlap. | If they do, a system
belongs to the one written first. || The other is whether a side's home is inside the
region you meant for it. || Nothing moves a home into a region for you. | You keep those
two lines in step yourself. ||"

### 6. A landmark that names a home

**Screen:** The Landmarks chapter. Type Assay Office. Highlight `Side: deepwell`.

**Say:** "Now for the landmarks. || You wrote one in Lecture 2, | and here are three more, each
for a different reason. ||| The first is a station at the miners' home. || Last time, when
the crew arrived there, | the card just said uncharted, and two numbers. || A side's home
doesn't name itself, | but a landmark does. ||| So now the card will read Assay Office, |
and the place goes on the crew's list of charted locations. || And because of this line,
Side, | the station belongs to the miners and offers their work. ||"

### 7. A dead ship, and a guarded one

**Screen:** Type The Tern, then The Bone Pile. Highlight `Kind: derelict`, `Terrain:`,
`Guards:`.

**Say:** "The second is a dead ship. || Kind, derelict, makes it a wreck for Science to
scan. || The game scatters wrecks of its own, but they have no names. || This one has a
name, a line on the card, | and a nebula around it, whatever the game rolled there. |||
And the third is a fight. || Guards puts a fleet on the landmark, | the first time the
crew arrives. ||| One thing to know about them. || The guards belong to nobody. | They're
raiders, even in Gleaner country, | so a ceasefire with the Gleaners won't call them off.
||"

### 8. Leads, and check

**Screen:** Add the two leads in the Narrative chapter. Save. `sbs lint MyUniverse`:
clean.

**Say:** "The crew still needs a reason to go, | so I add two leads, the way we did in
Lecture 3. || The Assay Office doesn't need one, | because an old lead already goes
there. ||| I save, and lint says clean. || And again, clean isn't the whole check today.
|| Lint doesn't know a sky's name from a typing mistake, | and it doesn't count your
percent signs. || So read down the list on the page. ||"

### 9. Fly the map

**Screen:** `sbs run server,helm,comms -m MyUniverse map=0`. Helm: Quest Log, four leads.
Engage The Third Colony: the card, the wreck. Engage The Second Colony: the card reads
Assay Office; Comms on it. Engage What the Gleaners Keep: the sky, the card, the fleet.
Engage The Breaking Yard: the card reads The Breakers. Charted Locations.

**Say:** "Four leads in the Quest Log now. || First, the third colony. | There's her
name on the card, and my line. ||| Then the miners' home, | and this time it has a name.
|| On Comms, the Assay Office offers the miners' escort. ||| Now the one the Gleaners
won't talk about. || This is the Breakers, and somebody's waiting. ||| And last, the
Gleaners' own home. || It has no landmark, | so the card falls back to the region's
name. ||| Here's Charted Locations, with four places in it. || Those are my landmarks,
and only my landmarks. || A region doesn't get charted, | and neither does a home with
no landmark in it. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Say what your galaxy is like in one sentence, | and set no more
than four dials to match. || Draw the grid on paper. || Give every side's home a landmark, | and
write one place that's only a story, and one that's a fight. ||| Next time, the work a
station hands out gets a beginning and an end. ||"
