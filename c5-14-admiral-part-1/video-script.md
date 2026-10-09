# C5-14 video script - The Admiral, part 1: the game from above

> **STATE ON 2026-10-09.** Written and measured against the released tools: `sbs` 0.13,
> the published v1.4.0 libraries (sbs_utils `4941820e`, LegendaryMissions `b20726f`, the
> two Open Universe libraries built 2026-10-08). **The headline of this lecture is a
> fault: a universe made with `sbs create -t ou` cannot have an Admiral today.** That
> was measured, and the page says so first. Everything else was measured in a copy of
> the Open Universe mission, placed where its save cannot reach a player's own, in the
> game's stand-in (the mock). The Admiral's console was never opened. A script made the
> Admiral's camera the way the console does, selected worldlets and platforms through
> the game's own Comms routes, and pressed the buttons the game sent, by their text.
> **Nothing in this lecture has been run in the real game, and nobody has seen any of
> its screens.**

The companion page is `lesson.md`. The finished `skirmish_arena.amd` is in `example\`;
it belongs in the `AdmiralLab` copy, not in `MyUniverse`.

## Before recording

| Item | State needed |
|---|---|
| Open Universe | The `OpenUniverse` folder in `data\missions`, current (Lecture 1, Stop 1) |
| The lab | Made on camera in scene 3: a copy of `OpenUniverse` named `AdmiralLab` |
| Saves | No `universe_save_skirmish_the_broken_accord_1.yaml` in `data\missions\common_data\saves`. Move a real one somewhere safe first |
| VS Code | Ready to open `AdmiralLab`; font size raised |
| Game | Closed. Started on camera in scene 9 with `sbs run server,admiral -m AdmiralLab` |

## Confirm on camera

**The fault, measured in the mock with `MyUniverse` as Lecture 13 leaves it:** with the
Admiral's library on a line of its own in `story.json`, `Mode: sandbox`, and Worldlets,
Admiralty, Officers and Research chapters in `kestrel_verge.amd`, the game runs 85
labels of 620 with no error and an empty `mast.runtime.log`. The Admiral's functions are
loaded. The game's own test for "is the Admiral's library here" answers no, the Admiral
console's condition is false, and the home system has no worldlet.

**In the mock, by script, in a copy of the Open Universe mission, with the page's own
`skirmish_arena.amd`:**

1. Lint of a whole copy of the mission: 13 `.amd` and 13 `.mast` files, two warnings,
   neither in `skirmish_arena.amd`. With the page's changes: those two, and four that
   say `Costs` and `Time` are not fields. With `Also: economy` added to a research
   record those go, and the game reads its `Time: 40` as 2,400.
2. The Admiral is on (`skirmish`), the console's condition is true, and the home system
   holds one worldlet, Hollin Prime. Untouched, it was Haven World.
3. The pools start at 6,000 ore, 1,200 gas and 480 crew, each able to hold 7,200.
4. The worldlet is sent one button, `Build Headquarters (150 ore, 15 crew)`. Thirty-one
   seconds after the press the Headquarters stands, and the worldlet is sent eight more
   buttons, with the costs in the page's table.
5. Extractor, Academy, Shipyard and Lab, started together: the Extractor stands inside
   30 seconds and all four inside 60. With the Extractor, ore rose 32 in 30 seconds and
   crew 24.
6. The Shipyard is sent seven buttons, Maren's first. Commissioned: fleet F1, three
   ships on the Admiral's side, and a card in her name and title.
7. A ship of the fleet is sent `Hail` and five orders.
8. The Lab is sent `Research Deeper Silos [engineering]`. Forty-one seconds after the
   press it is done, each pool can hold 7,700, and the Lab is sent `Research Hot Drills
   [engineering]`.
9. The fleet bonuses in Step 6 are the game's own function, asked about all seven
   officers.
10. Every row of the tables in Step 8, and the modes in Step 3: 52 variants linted and
    played. In the variant runs the platforms were placed by script, not built.

**From the game's guide or its code, not run:** what each platform is for; that
`border` sends raids; the fleet's cost of 180 ore, 40 gas and 24 crew (the pools fell
by about that).

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. **The Admiral console.** How a window gets it (`sbs run server,admiral`), what it
   looks like, and whether selecting a worldlet on its map gives the buttons the script
   was sent.
2. The start screen's Universe list, and Skirmish - The Broken Accord in it.
3. A worldlet in the 3D view, and its `Palette:`.
4. A fleet obeying an order.
5. Whether a second player ship is needed. The arena's own notes say Skirmish is for
   two sides. The script ran it with one.
6. The save shared with the real Open Universe mission.

## Scenes

### 1. Cold open

**Screen:** The Admiral console, looking down on a system. A worldlet selected, the
Build Headquarters button.

**Say:** "Everything you've written so far is seen from a bridge. || One ship, one
crew, | one system at a time. ||| There's another seat in this game. || The Admiral
doesn't fly anything. || The Admiral looks down on a whole system, | builds on its
worlds, and sends fleets out. ||| Today you write for that seat. ||"

### 2. Where it runs today

**Screen:** The "Read this first" section of the page. Then `MyUniverse\story.json`
with the Admiral's library line added, and the game starting with no Admiral console.

**Say:** "And I have to start with some bad news, | because I'd rather you heard it
from me. ||| The Admiral's game doesn't run in the universe you made in Lecture Two, |
not as things stand today. ||| I did try it. || I added the Admiral's library, | I changed the mode, | and
I wrote the chapters. || The game started, and nothing happened. || There was no
console and no error. ||| That's a fault in how two libraries find each other, | and
it's been reported. || It isn't something you can fix from your mission folder. ||| So
today, we work where the Admiral does run, | which is inside the Open Universe mission
itself. || And what you write there | is exactly what your own universe will take
later. ||"

### 3. Make the lab

**Screen:** File Explorer in `data\missions`. Copy `OpenUniverse`, paste, rename to
`AdmiralLab`. Open it in VS Code.

**Say:** "First, we make a copy. || Never change the Open Universe folder itself, | because an
update will replace it. ||| I copy it, paste it, and call the copy Admiral Lab. |||
One warning about saves. || A save is named after the universe, not the folder, | so
the lab and the real thing share one. || If you've got a skirmish game you care
about, | move that file somewhere safe first. ||"

### 4. What an Admiral does

**Screen:** The first table in Step 2 of the page. Then the platforms table.

**Say:** "Here's the whole game, so you know what you're writing for. ||| The Admiral
selects a world, and builds a headquarters. || Then comes an extractor, | and ore starts
coming in. || Then an academy and a shipyard, | and the shipyard offers officers to
commission. || Each officer gets a fleet of three ships. || And a lab offers research.
||| You don't write any of those buildings. || They're the same in every universe. ||
You write the worlds, the people, and the ladder. ||"

### 5. A world of your own

**Screen:** `skirmish_arena.amd`, the Worldlets chapter. Type Hollin Prime above Cinder
World. Highlight `Yields`, then `Reserve: unlimited`.

**Say:** "This is the arena file, and it's short. || Here are its three kinds of
world. | I'm adding a fourth, above them. ||| Yields is what one extractor brings in
each minute. || Reserve is how much there is before the world runs dry. ||| And here's
the rule that matters. || The home system always gets one world, | and it's the first
one in the file that never runs dry. || I put mine first, | so my Admiral starts on my
world. ||"

### 6. Dials, and an honest number

**Screen:** The Admiralty chapter. Add the three lines. Then the "multiplied" table on
the page.

**Say:** "Next come the dials, and there are three I'm setting. || There's the starting ore, | how
many fleets at once, | and no border raids while I'm learning. ||| Now, an honest
number. || I wrote five hundred ore. || The game started with six thousand. ||| Part of
that is the mode, which is fair. || But most of it | is a test setting the game's
makers left switched on. || It runs the Admiral's economy eight times fast. ||| So
don't balance anything today. || Write the numbers your story suggests, | and tune them
when that setting is gone. ||"

### 7. An officer

**Screen:** The Officers chapter. Type Commodore Ilse Maren above Vale. Highlight
`Values`. Then the three-row table in Step 6.

**Say:** "Officers look like the captains from Lecture Eight, | and their values are
the same traits. ||| Here, though, three of those traits do something. || By the book
means the fleet burns less gas. || Resourceful means more salvage. || Fearsome means it
engages from farther out. ||| Every other trait is character. || It's who she is, | for
the day a crew talks to her. ||"

### 8. Research

**Screen:** The end of the file. Type the Research chapter. Highlight `Requires` and
`Unlocks`. Then `sbs lint AdmiralLab`.

**Say:** "The arena has no research, so I'm adding the chapter. || There are two steps.
|| Each one has a cost, a time in seconds, | and what it unlocks. || The second one
requires the first, | and that's what makes it a ladder. ||| Now I run lint. || Two
warnings were there before I started. || And there are four new ones, | saying the game
doesn't read my costs or my times. || It does read them. | I watched it take the ore,
and the forty seconds. ||| There's a line that makes those warnings go away, | and I'm
asking you not to write it. || It quietly turns forty seconds into forty minutes. ||
So for today, six warnings is what done looks like. ||"

### 9. Play it

**Screen:** `sbs run server,admiral -m AdmiralLab`. The start screen: Universe set to
Skirmish - The Broken Accord, Start set to New Game. Then the seven play steps on the
page.

**Say:** "Now let's play it. || On the start screen I pick the skirmish universe, and a new
game. ||| There's one world at home, and it's mine. || I build a headquarters, | then
the extractor, the academy, the shipyard and the lab. || The ore is climbing. ||| The
shipyard offers my officer first, | by her name and her title. || And the lab offers
my first step, | and then, once that's done, my second. ||"

### 10. Your turn

**Screen:** The "What your own universe will need" table. Then the exercise.

**Say:** "Now it's your turn. || In the lab, write the world your own side starts
on, | then two officers, and a ladder of three steps. ||| Keep them there for now. || When
the fault is mended, | it's three small moves to bring them home, | and they're on the
page. ||| The lecture after this one isn't ready yet, | so go on to the capstone. ||"
