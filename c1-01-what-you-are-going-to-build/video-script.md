# C1-1 video script - What you are going to build

> **Rewritten 2026-10-05 for a 1.4.0 install, got from Steam or itch.io.**
>
> - Removed: the two trouble rows and the notes that told a student with an older
>   Legendary Missions to watch the quest and the boss on the video. On 1.4.0 Stops 2 and
>   3 are PLAYED. One trouble row is left for an older copy. Stops 4 and 5 stay on video.
> - Changed: the game is started from the store's own app, not from a file the student
>   unpacked.
> - The page was checked against the mission's files as they are on the `v1.4.0_dev`
>   branch (LegendaryMissions `b20726f`, library `1fd5e171`, tool 0.12). The only game
>   archive on the writing machine is 1.3.7, and its Legendary Missions has no quest
>   tree and no bosses: that archive says nothing about what 1.4.0 holds.

> **SEEN (2026-10-05, in the real game on the developer's machine, a development build,
> by the session that sent the pilot).**
>
> - The first screen: the game's name, "Report to the Bridge, Defend the Cosmos", the
>   version at top left, and three buttons at bottom left, **Start Server**, **Start
>   Client**, **Options**.
> - **Start Server** leads to a screen headed "Artemis Cosmos Server" and **Choose
>   Mission**: a scrolling list in groups (Classic, Development, Example, Open Universe,
>   Probes on this machine), each line a name, a sentence and tags; **Initialize Mission**
>   at bottom right; **System Options** and **Exit Server** at top left; the computer's
>   IP address at top right.
> - Legendary Missions, initialized: **Legendary Missions:** and its overview; "Select a
>   mission. 7 types."; **Siege** and its description with a **next** arrow; an
>   **Options** panel with Main (Player Ships, Difficulty, **Boss** set to None, Theater,
>   Music, Crew) and Map (Map Size, Terrain, Lethal Terrain, Friendly Ships); a **Presets**
>   drop-down above it; **Start Mission** along the bottom; **Mission Select** and
>   **Options** at the top.
> - The page's Stop 1 was written from these three screens.
> - **Later the same day the whole lone-player path was walked, on one computer:**
>   **Start Mission** leaves the server on a notice ("Congratulations on installing and
>   starting a server for Artemis Cosmos! ... you must start the game on another computer
>   (as a client) ... Connect using this server's IP address"). A SECOND copy of the game,
>   **Start Client**: "Detected game server list:" with one button, **Connect to Cosmos
>   Server**, and below it a box to type an address (it holds `127.0.0.1`) with **Connect
>   To Server**. Then the ship-and-console screen: the ship's name and description, a
>   **Ships** list (`Artemis - tsn`), a **Consoles** list (Helm, Weapons, Engineering,
>   Science, Communication, Mainscreen, Cinematic, Flight Hangar, Game Master, each with a
>   line of words), the crew member's face and name with **Edit**, and **ready**. Helm,
>   ready: the Helm console. Handheld icon: the ePADD (Status, Messages, Upgrades; Quests,
>   Library, Help). **Quests**: the Quest Log. Under **Game**: Repel the Siege, Break the
>   Siege, Hold the Starbases, Break It in Time, all `Active`, shown as FOUR LINES AT ONE
>   LEVEL (not one line with three under it). Under **Ship**: `Ace: 6 raider kills` and
>   `Guardian: keep every starbase`. The page's steps 9 to 12 and Stop 2 are from this.
>   NOT followed: a boss arriving, the game ending, the way back to the start screen.
> - Two things a recording will show that are not the lesson's business: on a machine
>   with many missions the list is long (a player's list is short); and one long
>   description in the list was drawn over the line below it.
> - **Two of the four tour stops cannot be played by a student on day one.** A boarding
>   scene and a ruin are in no map of LegendaryMissions (checked by search: no map calls
>   `boarding_visit` or `relics_spawn`). Nobody has said that the missions which have
>   them (Dawnline, Open Universe, Storm's Beacon) are in the 1.4.0 download. So Stops 4
>   and 5 are played by the presenter and watched.

Target length: 18 minutes. Game footage with voice-over for Stops 1 to 5; File Explorer
and two files shown in an editor for Stop 6; slides or stills for Stop 7. The companion
page is `lesson.md`. There is no `example\` folder: the lecture makes no file.

## Before recording

| Item | State needed |
|---|---|
| The real 1.4.0 download | On a real Steam install AND a real itch.io install of 1.4.0, check three things. (1) The folder's path (Lecture 2 needs it). (2) That a command prompt there can write files (`sbs create`, `sbs update`: Lectures 2 and 3 need it). (3) What the download holds. For this lecture: start it from the store's app, choose Legendary Missions, choose Siege, and look for a `Boss` line in the Options panel and for "Repel the Siege" in the quest list. The page assumes both are there. Also write down which other missions are in the list |
| Starting the game | The button's name in each store's app (**Play** in Steam, **Launch** in the itch.io app), and whether a launcher or a question comes before the game's first screen. Fix step 1 of Stop 1 if so |
| The first screen | Record the path from the store's app to the mission list, and from there to a console on the same computer, with no command prompt. Write the steps into Stop 1 of the page |
| Stop 2 and 3 footage | A crew, or the presenter with `sbs run server,helm,weapons,science -m LegendaryMissions`. Boss chosen by hand in the Options panel, on camera: the menu is the point |
| Getting the Warlord to arrive | She arrives when the raiders are at or under 25% of their peak count. Lower Difficulty and bring a Weapons officer. Budget time for this off camera: how long it takes has not been measured |
| Stop 4 footage | The finished mission of Class 3, Lecture 6 (`c3-06-boarding-checkpoint\example\`), in a mission folder made the way that lesson says, with at least Engineering and one more console. Its predecessors were played in the real game (Lecture 2 with one console, Lectures 4 to 6 with two and three) |
| Stop 5 footage | Two missions. The finished one of Class 4, Lecture 7 (`c4-07-quests-through-a-ruin\example\`) for the flight, the quest and the call. Lecture 6's (`c4-06-clues-side-stories-cutscenes\example\`) for the cutscene: Lecture 7's files do not carry it. Helm, Comms, Science and a main screen |
| Stop 6 | File Explorer on a mission folder made by `sbs create ... -t amd` (seven files), with file name extensions shown. `c1-11-just-enough-mast\example\mission.amd` at line 61 and `story.mast` at line 108, in VS Code with the add-on, so the color is what the student will later see |
| Saved games | Stops 4 and 5 do not use Open Universe or Storm's Beacon, on purpose: both write saved games. If you would rather show a shipped mission, Dawnline (`sbs fetch LandingParty --branch master`) and Storm's Beacon (`sbs fetch StormsBeacon`) are the candidates. Neither fetch was run for this page |

## Confirm on camera

"Read" means it comes from a file and was not watched. "Measured" means a script called
the game's own reader, or the headless stand-in ran the mission. "SEEN" means it was
looked at in the real game by an earlier pilot. "UNSEEN" means nobody has looked.

**Stop 1 - starting and choosing**

1. The game's first screen, and **Start Server**. (SEEN, on a development build
   started from its own folder. From the Steam Library or the itch.io app: UNSEEN. The
   button names **Play** and **Launch** are from memory of those apps, not read today.)
2. The game's list of missions shows "Legendary Missions" and its sentence. (SEEN.)
3. The mission's start screen opens with the title "Legendary Missions:" and the
   overview that begins "Select a mission type below from the set of customizable
   scenarios". (Read: `consoles\server_console.mast` builds the text with
   `server_start_text` from the mission's `@map/__overview__` label, in
   `maps\mission_story.mast`. SEEN.)
4. "Select a mission. 7 types.", with Siege shown first. (SEEN. The count on a 1.4.0
   download is not known.)
5. An **Options** panel, with groups **Main** and **Map**, and a **Start Mission**
   button. (SEEN.)
6. How a console is chosen after Start Mission. UNSEEN.
7. That one person on one computer can hold the server and Helm without a command
   prompt. UNSEEN. If it cannot be done from the game's menus, Stop 1 of the page needs
   rewriting: the student would watch, and play for the first time in Lecture 3.

**Stop 2 - the quest**

8. Siege grants one quest with three parts at the start: Repel the Siege; Break the
   Siege; Hold the Starbases; Break It in Time. (Measured: the game's quest reader on
   `maps\siege_quests.amd` returns these four, with `required` on the second and
   `critical` on the third and fourth. Not watched in a game.)
9. Each player ship also gets "Ace: N raider kills" and "Guardian: keep every starbase".
   (Read: `maps\siege.mast`, `siege_bonus_objectives`. N depends on Difficulty.)
10. The Quest Log is reached by the handheld icon in the top bar, then Quests. (SEEN, on
    a mission made from the template. In Siege: UNSEEN.) How the tree is drawn there, and
    where the two per-ship quests sit, UNSEEN.
11. The game ends on "Victory! The starbases held." (Read: the `Win:` line. Where the
    words are drawn is UNSEEN.)
12. Siege runs in the headless stand-in for 30 seconds with no error: `labels 114/901`,
    `PASS - no runtime errors`. (Measured, map 0, seed 7.)

**Stop 3 - the boss**

13. The Boss list holds None, Continuous, Infestation, Ragnarok, Warlord. (Measured: the
    mission's own `siege_boss_list()`, on a machine with an empty `common_data\bosses`.
    The order on screen is as returned. The dropdown itself is UNSEEN.)
14. Warlord: arrives at 25% of the peak, two fleets, one flagship named Warlord on a
    `kralien_dreadnought`. Ragnarok: 30%, three fleets, Ragnarok and XORN. (Measured: the
    mission's own boss readers.)
15. On arrival "Defeat the Warlord" joins the quest list, 500 credits. (Read:
    `maps\bosses\warlord.amd` and the `siege_enemies_low` route. An arrival was checked
    in the real game by script for the Class 2 pilots. Never watched.)
16. How to leave a finished game and get back to the start screen. UNSEEN.

**Stop 4 - the boarding party**

17. The Boarding Party tile on the handheld, "Going down to The Hulk", **BEAM DOWN**, the
    bar with name, job and room, the buttons, and the return to the station. (SEEN, in
    the Class 3 pilots, on those lessons' own missions.)
18. Two consoles in one room with different buttons. (SEEN, Class 3 Lectures 4 to 6.)
19. No map of LegendaryMissions starts a boarding visit. (Measured by search of the
    mission's files. The `boarding` add-on it loads only supplies the consoles.)

**Stop 5 - the ruin**

20. The ruin on Helm's map and on the main view. (SEEN, one screenshot each, Class 4
    Lecture 2.) The ship inside it, close up: UNSEEN.
21. The cutscene: the main screen leaves the ship, two shots, a line of words under
    each, then back. (SEEN, Class 4 Lecture 6.)
22. A place calling the ship, and an answer revealing a hidden place. (Checked in the
    real game by script, Class 4 Lectures 4 and 7. Not watched on a console.)
23. The page says the opening is "wide enough for the ship". Check it with the hull the
    footage uses, or cut the words.

**Stop 6 - the folder**

24. A mission from the `amd` template is seven files. (Measured: the Lecture 3 example
    folder.) How File Explorer shows them: UNSEEN.
25. Every line in a code block on the page is a line of a real file. (Measured:
    `c101\verify_page.py`, 53 lines and 16 phrases, exit 0.)

## Scenes

### 1. Cold open

**Screen:** Four quick cuts, about ten seconds each: a quest finishing in the quest
list; a flagship arriving; a console turning into a handheld; a ship flying into a ruin.

**Say:** "Here's a quest, and here's a boss. | Here's a boarding party, and a ruin. || A
writer typed every one of these, in plain words, in a text file. || And by the end of this
course, that writer is you. ||| Today, you type nothing. || You play, and you watch, | and I
show you what you're going to build. ||"

### 2. What the game is

**Screen:** A bridge: several consoles and a main screen.

**Say:** "Artemis Cosmos is a starship bridge. || One copy of the game runs the story, and
we call that the server. || Every other screen is one station: | Helm steers, Weapons fires,
Science scans, | Comms talks, and Engineering keeps her running. ||| What the crew is asked
to do, who calls them, and what they find: | all of that is a mission. || And a mission is
what you'll write. ||"

### 3. Stop 1: start it and choose Siege

**Screen:** The game started from the Steam Library. The first screen. The mission list.
Legendary Missions chosen. The start screen: the maps, the Options panel, Start Mission.
A console taken.

**Say:** "Start the game with me. || The first screen has the game's name, | and three
buttons at the bottom left: start server, start client, and options. || One computer runs
the game for everybody, so press start server. ||| Now you choose twice. || First, you
choose a mission, and that's Legendary Missions. | Press initialize mission, and wait a few
seconds. || Then you choose a map inside it, and that's Siege. ||| Remember those two lists,
| because in two lectures' time, there's a line in the first one that you made. ||| Now
press start mission. || The server only runs the game, | so to fly, you start the game a
second time, and press start client. || Connect to your own server, pick Helm, and press
ready. ||"

### 4. Stop 2: the quest

**Screen:** Siege under way. The handheld icon, Quests. "Repel the Siege" with its three
parts. Then `siege_quests.amd` open at "Break the Siege".

**Say:** "Here's what the game has asked us to do. || It's one job, in three parts: | break
the siege, don't lose every starbase, and mind the clock. ||| Now look at this, because this
is the file. || The square brackets hold the name on the screen, | and the last line is what
the crew is told. || Required, true, means you can't win without it. ||| Nobody programmed
this quest. Somebody typed it. || And Class One ends with you having typed a chain of these.
||"

### 5. Stop 3: the boss

**Screen:** Back at the start screen. The Options panel, the Boss line opened, Warlord
chosen. Cut to late in the battle: the flagship arrives; "Defeat the Warlord" joins the
quest list. Then `warlord.amd`.

**Say:** "Now the same map, with one change. || On the start screen, the options panel has a
line called Boss, | and I choose the Warlord. ||| A boss doesn't come at the start. || She
waits until we've destroyed three raiders in every four. || Then she arrives, and a new job
joins the list. ||| Now here's her file. || Twenty-five percent means a quarter are left. |
Then two fleets, and her name and her hull. || In Class Two, you copy this file, change the
words, | and your own boss is in that list. ||"

### 6. Stop 4: the boarding party

**Screen:** The Class 3 mission. The ship reaches the hulk. The handheld, the Boarding
Party tile, BEAM DOWN. One console walking two rooms. Then two consoles side by side in
one room.

**Say:** "This one, you can't play today. || It isn't in the game's menus, so just watch.
||| Some of the crew leave the ship, | and each console becomes a handheld. || There's a
line of story, and the ways out, as buttons. ||| Now think of two of them together. ||
They're in the same room, with different choices: | the surgeon is offered what the engineer
isn't. || It's a story told in rooms, and every reader has their own copy. | And that's
Class Three. ||"

### 7. Stop 5: the ruin

**Screen:** The Class 4 mission. Helm's map with the ruin named. The flight in. A step
finishing, a new place on the map. The call. The cutscene.

**Say:** "And then there's this. || It's a built place, and it's old, with rooms. || The
writer didn't draw it. || The writer wrote, a room, this big, here, | and the game put up
the walls. ||| A quest leads the ship through it, | and a place speaks. || And for ten
seconds, the story takes the main screen. || And that's Class Four. ||"

### 8. Stop 6: a mission is three things

**Screen:** File Explorer on a mission folder: seven files. `mission.amd` highlighted,
then opened at "Close Inspection". `story.mast` highlighted, then opened at the card.

**Say:** "So what is a mission? || It's a folder, with seven files, | and five of them are
made for you. || The two that matter are the fact sheet, and the story file. ||| The fact
sheet is every word the crew reads. || Here's one quest: its name, | its facts between the
two rows of hyphens, | and what the crew is told. || Done when, reach derelict five hundred.
| It means just what it says. ||| The story file is short, and it comes ready-made. || Now
and then, you paste a few lines into it from a card, like this one. || It says: when the
step starts, wait twenty seconds, | bring in a tug, and tell the quests. ||| You'll be able
to read this by Lecture Eleven. || And you'll never write one from a blank page. ||"

### 9. Stop 7: the six classes

**Screen:** The table of six classes, then one still per class.

**Say:** "There are six classes. || One is your desk, and a story told in quests. | Two is
people who talk, and a boss of your own. || Then come three that you can take in any order:
| three is boarding parties, four is ruins, | and five is a universe of your own. || And six
is twenty evenings of play in that universe. ||| Some of the later lectures are still being
made, and the page says which. ||"

### 10. Your turn

**Screen:** The exercise table from the page.

**Say:** "So play ten minutes of Siege. || Write down three things that happened, | and who,
or what, caused each one. || And keep the page, | because next time, we find where all of
this lives on your computer. ||"
