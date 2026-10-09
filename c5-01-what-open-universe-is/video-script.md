# C5-1 video script - What Open Universe is

> **STATE ON 2026-10-08. Read this first.**
>
> - **The plan called this lecture "plays Silver Reach". Today a crew cannot play it past
>   the first system**, and the page says so. Measured today in the game's stand-in (the
>   mock), on a copy of the Open Universe mission: with The Silver Reach chosen, the
>   Engage switch is off, charted places are off, the Navigation console is off and the
>   Admiral console is inactive. Nothing on any console moves the ship. The same is true
>   of The Fading Signal. In Default the Admiral console is active; that was not played.
> - **A second fault waits behind it.** When the probe sent the message an Engage button
>   would send, the ship arrived at the Lantern Combine's home, and selecting a station
>   there on Comms stopped the mission (`name 'sides_standing' is not defined`). That
>   fault was mended in Open Universe later the same day and is released.
> - So the lecture is a short true play, then a reading of `silver_reach.amd` beside a
>   table of what the file becomes. **When the mission is mended** (one line switches
>   Engage on in its `story.mast`, and the engine's missing names are restored), Stop 3
>   can go on to the Lantern Combine's home and scenes 4 and 5 can be played instead of
>   read.
> - **Whether a student's game holds the Open Universe mission is not known**, and the
>   line that fetches it was read and not run. Stop 1 carries a note in italics that has
>   to be settled before the page is published.
> - Nothing was run in the real game, and nobody has seen any screen in this lecture.

The companion page is `lesson.md`. There is no `example\`: the student writes nothing.

## Before recording

| Item | State needed |
|---|---|
| The game | Artemis Cosmos 1.4.0, with the `OpenUniverse` folder in `data\missions`. Settle Stop 1's note first |
| Saves | No `universe_save_the_silver_reach_1.yaml` in `data\missions\common_data\saves`, or the first start continues an old game |
| VS Code | Open on `C:\Cosmos\data\missions\OpenUniverse`, `silver_reach.amd` in a tab, font size raised. Do not save anything in this folder |
| Command prompt | Open in `C:\Cosmos\data\missions` |
| Game | Closed. Started on camera in scene 2 with `sbs run server,helm,comms -m OpenUniverse` |

## Confirm on camera

**In the mock, by script, on 2026-10-08, on a copy of the Open Universe mission:**

1. The Universe list is handed four names: Default, The Silver Reach, The Fading Signal,
   Skirmish - The Broken Accord.
2. With The Silver Reach: mode `sandbox`; the arrival card is handed `Home Port`; one
   station, Starbase, on the crew's side; 500 credits.
3. Comms is sent these buttons for Starbase: Market, Hail, Build Weapons, Request
   Priority Docking, Accept Cargo Run, Transport a passenger, Accept Patrol Mission.
4. The Quest Log is handed The Dimming: A Cold Lane and Break the Veil, both Active.
5. The Quest Log's own gate, asked about the story's first step on Helm: no Engage, and
   the hint "Manage quests at the Admiral or Comms console."
6. The save file is `universe_save_the_silver_reach_1.yaml`, written beside the copy and
   not among a player's own saves.
7. "What the crew would find" in Stop 4: the probe sent the Engage message itself. The
   ship arrived at -4, 2. The card was handed `Lighthouse Station` and the first line of
   its text. Two stations, Lighthouse Station and The Lantern Combine, both on the
   Combine's side. The board of work on offer listed Convoy Escort at 260, Veil Bounty
   at 300, and Transport Brother Calen at 500 to 5, -4, at both. The Quest Log then
   held The Dimming: Ash on the Manifest, with A Cold Lane done.

**Read in the files, not run:** the option names on the start screen (Universe, Start,
Save Slot, Player Ships, Difficulty, and a second group); the five modes and what each
allows; every line quoted from `silver_reach.amd`; the lecture list in Stop 7.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. Whether the game's list of missions has Open Universe in it, and under what heading.
2. The start screen: the Universe list, and Start reading Continue.
3. The arrival card, and where it is drawn.
4. Helm's Quest Log with a job selected and no Engage button.
5. Everything in Stop 1: what `dir OpenUniverse` prints, and what the fetch does.

## Scenes

### 1. Cold open

**Screen:** The Quest Log in The Silver Reach. Then `silver_reach.amd` scrolling in VS
Code.

**Say:** "In Class 1, you built a mission with one map and one story. || This class is
about something larger: | a mission that's a whole galaxy, | with factions, work, a
story, | and a game the crew can leave and come back to. ||| It's called Open Universe.
|| And the surprising part is how it's made. | All of it comes from one text file, | of
the kind you already know how to write. ||| Today you'll start one, read the file behind
it, | and decide what kind of universe you're going to make. ||"

### 2. Start it, and choose a universe

**Screen:** The command prompt: `sbs run server,helm,comms -m OpenUniverse`. The start
screen; open the Universe list; choose The Silver Reach. Point at Start reading Continue.
Start Mission.

> If the mission is not in the game, do Stop 1 on camera first.

**Say:** "Open Universe is a mission, like Legendary Missions, | so I start it the same
way. || I leave the map off the end this time, | because I want the start screen. |||
Here's a list called Universe, with four on it. || I want The Silver Reach, | which is
the one written as an example for writers. || And notice this setting, Start, which says
Continue. || A game here is kept between sessions, | and that's half of what this class
is for. ||"

### 3. The first system

**Screen:** The arrival card, Home Port. Comms: select Starbase; Accept Cargo Run. Helm:
the handheld, Quests; the three entries. Select the story's first step; point at the
place an Engage button would be.

**Say:** "This is the system every new game starts in, | and the card calls it Home Port.
|| There's one station here. || On Comms I select it, and I take a cargo run. ||| Now the
Quest Log, on Helm. || There's the first step of this universe's story, | there's the way
to win, | and there's my cargo run. || All three of them send me to another system. |||
And this is where I have to stop. || In this mission, as it's published today, | the
button that makes the jump is switched off. || That's a fault in the mission, and it
isn't anything you did. || The mission you make next time has that button on. || So I'll
close the game, | and show you the rest from the inside. ||"

### 4. One file

**Screen:** VS Code, `silver_reach.amd`. Scroll slowly from top to bottom, pausing on
each two-hash heading.

**Say:** "Everything about The Silver Reach is in this file. || It's about three hundred
and sixty lines. ||| At the top is one record with a single hash, | and that's the
universe itself. || Under it are chapters, each with two hashes. || There are the sides,
which are the factions. | There are the jobs their stations offer. || Here's the story,
in three steps, | and each step is a quest like the ones you wrote in Class 1. || Then
regions and landmarks, which are the map. || And then the people, | and what they say.
||| Each of those chapters is a lecture in this class. ||"

### 5. From a record to a place

**Screen:** The Lantern Combine record. Highlight `Home: -4, 2`. Then the Lighthouse
Station landmark. Then the page's table "What the crew would find there".

**Say:** "Let me show you one record becoming a place. || This is a side, the Lantern
Combine. || You can read most of it already: | a heading, a fence, and a fact on each
line. ||| Home is minus four, two. | That's a system, and it's the one the story sends
the crew to first. ||| When a ship arrives there, the game puts a station in it, | named
after this side. || This landmark, further down, puts a second station beside it. || And
this line, Offers, | is why both stations hand out an escort job and a bounty. ||| Nobody
placed those stations on a map. || The record says where these people live, | and the
game does the rest. ||"

### 6. What isn't in the file

**Screen:** Scroll the whole file once more, fast. Then the save file in VS Code:
`universe_seed`, `current_system`.

**Say:** "Now notice what isn't here. || There's no list of systems. || Nobody wrote the
stars, or the nebulas, | or the raiders in the dark between places. ||| The game makes
all of that from one number, called the seed. || The same seed always gives the same
galaxy, | so a place you leave is the same place when you come back. ||| And here's the
save, which is tiny. || It holds the seed, where the ship is, | and what the crew has
changed. ||| That's the bargain of this class. || You write the people, the places and
the events. | You don't draw the map. ||"

### 7. Choose your mode

**Screen:** The mode table on the companion page.

**Say:** "One decision before next time. || Every universe says what kind of game it is,
with one word. ||| Story is one ship, and a tale with an ending. || Campaign is one ship
too, | played over many evenings. || Sandbox is an open world with no ending. || And the
last two are wars between admirals, | which come late in this class. ||| For one crew in
one ship, the first three play alike today. || So choose the one that's true of what you
want to write. ||"

### 8. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Two things on paper. || First, read the file, | and answer the five questions
on the page. || Each answer is one line of it. ||| Then write three sentences about your
own universe: | who lives there, who shoots first, | and what the crew is there to do.
||| Next time, that page becomes a mission, | and you take it on its first jump. ||"
