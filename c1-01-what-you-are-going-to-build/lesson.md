# Class 1, Lecture 1 - What you are going to build

## What you will have at the end

A picture in your head of the whole course, and ten minutes of the game played.

You will have seen four things on a starship's bridge: a quest, a boss, a boarding party
and an ancient ruin. You will know which of the six classes teaches you to write each
one. And you will know what a mission is made of: a folder, a fact sheet in plain words,
and a short story file.

*[Screenshot to add: the four stops side by side - the crew's quest list, the Boss line on
the Siege setup screen, a boarding party's handheld, and a ruin on Helm's map.]*

You type nothing in this lecture. You play, and you watch.

## The video

*[Link to add when recorded.]*

Two of the four stops are on the video only. The game as you install it does not hold a
boarding scene or a ruin you can reach from its menus. Stops 4 and 5 say so again. You
will build both yourself, in Classes 3 and 4.

## Before you start

- A computer with Windows 10 or Windows 11.
- Artemis Cosmos 1.4.0, installed from Steam or from itch.io.
- Nothing else. No editor and no command prompt.

Words for this lecture:

| Word | Meaning |
|---|---|
| Mission | One thing the game can play. On disk it is a folder. The game lists the missions it finds |
| Map | One scenario inside a mission. The mission Legendary Missions holds several: Siege is one |
| Server | The copy of the game that runs the mission. There is one. Its screen is where the mission is chosen and started |
| Console | One station on the bridge: Helm steers, Weapons fires, Science scans, Comms talks, Engineering keeps the ship running |
| Quest | A job the game gives the crew, in words, with a way to finish it |
| Boss | A named enemy who arrives late in a battle, with ships of their own and a job for the crew |
| Boarding party | Some of the crew leave the ship and walk through a place, room by room |
| Ruin | An old, built place in space, with rooms and passages a ship can fly into |

## Stop 1 - Start the game and choose Siege

1. Start the game the way you start any game from that store: **Play** in the Steam
   Library, or **Launch** in the itch.io app. Its first screen has the game's name, the words "Report to the Bridge,
   Defend the Cosmos", and three buttons along the bottom left: **Start Server**,
   **Start Client** and **Options**. The version number is in the top left corner.
2. Press **Start Server**. One computer runs the game for everybody, and that computer
   is the server. Today it is yours.
3. The next screen is headed **Choose Mission**. It is a list in groups, such as
   **Classic** and **Example**. Each line is a mission: its name, a sentence about it,
   and a few words at the right. Click **Legendary Missions**. Its sentence is "Missions
   similar to the original Artemis Solo Missions list."
4. Press **Initialize Mission**, at the bottom right. Wait a few seconds.
5. You are now on the mission's own start screen. It opens with **Legendary Missions:**
   and these words: "Select a mission type below from the set of customizable scenarios
   reimagined from the original Artemis: Spaceship Bridge Simulator Solo missions."

6. On the left it says **Select a mission. 7 types.** and shows one of them: **Siege**.
   Its description begins "In this scenario, bases will be located in the center of the
   sector". A **next** arrow under it steps through the others. Stay on Siege.
7. On the right is a panel named **Options**: Player Ships, Difficulty, Boss, and more
   below. Leave it alone for now. Stop 3 comes back to it.
8. Press **Start Mission**, the bar along the bottom.
9. The server's screen now shows a notice that begins "Congratulations on installing and
   starting a server for Artemis Cosmos!" It is telling you that the server only runs
   the game. To fly, you need a console, and a console is the game started a second
   time. Leave this window open.
10. Start the game again, the same way you did in step 1. A second window opens. This
    time press **Start Client**.
11. Under **Detected game server list** is a button, **Connect to Cosmos Server**. Press
    it. That is your own server, on your own computer.
12. You are asked which ship and which console. There is one ship, Artemis. In the list
    named **Consoles**, click **Helm** ("Pilot the ship"), then press **ready** at the
    bottom right. You are at the helm.

With friends, each of them does steps 10 to 12 on their own computer and takes a
different console.

What to notice: you chose twice. First a mission, then a map inside it. When you make
your own mission in Lecture 3, it will be a line in the first list, with one map in the
second.

## Stop 2 - A quest: Repel the Siege

**Taught in Class 1.**

Siege is a battle. Starbases sit in the middle of the map and raiders come at them from
every side. The game tells the crew what winning means with a quest.

Open the crew's quest list. On your console, press the small handheld icon in the top
bar, beside your crew member's name. It opens the ePADD, the crew's handheld. Press
**Quests**. The screen is headed **Quest Log**.

Under **Game** are four lines, each marked `Active`: one job, and the three parts of it.

| Quest | What it says | What it does |
|---|---|---|
| Repel the Siege | Break the siege on the starbases. | The whole job. The three below belong to it |
| Break the Siege | Destroy the attacking fleets before they overwhelm the starbases. | Finish this and the game is won |
| Hold the Starbases | Do not let every starbase fall - losing the last one loses the siege. | Fail this and the game is lost |
| Break It in Time | Break the siege before the clock runs out. | The clock. On the usual setting, lasting until it runs out counts as holding |

Each player ship also gets two smaller quests of its own: an **Ace** quest for
destroying raiders, and **Guardian: keep every starbase**.

Nobody programmed those four as code. A writer typed them. This is "Break the Siege",
exactly as it sits in the game's files:

```
# [Break the Siege](break_siege)
---
Scope: shared
State: active
Parent: siege_mission
Required: true
Done when: signal siege_won
---
Destroy the attacking fleets before they overwhelm the starbases.
```

You cannot read all of it yet. Read what you can. The name in square brackets is what
the crew sees. The last line is what the crew is told. `Parent:` says which quest it is
part of, and `Required: true` says the parent cannot be won without it. By Lecture 9 you
will have written one like it.

What to notice while you play: the game wins or loses by its quests. When the last
raider dies, "Break the Siege" finishes, "Repel the Siege" finishes with it, and the game
ends with the words "Victory! The starbases held." Those words are a line in the same
file.

## Stop 3 - A boss: the Warlord

**Taught in Class 2.**

Go back to the mission's start screen. *[Steps from the recording: how to end a game and
return.]* Choose Siege again and look at the **Options** panel. Its first group has a
line named **Boss**. The list holds:

| Boss | What arrives |
|---|---|
| None | Nothing extra. This is the setting you played in Stop 2 |
| Warlord | A flagship named Warlord and two fleets, when the raiders are down to a quarter of their greatest number |
| Ragnarok | A flagship named Ragnarok, a cruiser named XORN and three fleets. The crew can try to talk XORN into changing sides |
| Infestation | A swarm that breeds |
| Continuous | No flagship. Wave after wave until the clock runs out |

Choose **Warlord** and start the mission.

A boss does not come at the start. The Warlord waits until the crew has destroyed three
raiders in every four. Then the flagship arrives with her fleets, and a new quest joins
the list: **Defeat the Warlord**, worth 500 credits.

That takes a while, and a first-time crew may lose the starbases before it happens. The
video shows the arrival. You do not need to reach it today.

The whole Warlord is 28 lines in one file. These are the lines that make her:

```
# [Warlord](warlord)
---
Boss
Trigger: enemies_low
Low: 25%
Flies: 50% Kralien, 50% Torgoth
Fleets: 2
Difficulty: +1
Named: Warlord kralien_dreadnought
---
A raider warlord and their honor guard warp in to break the defenders.
```

`Low: 25%` is "a quarter". `Fleets: 2` is the two fleets. `Named:` gives the flagship her
name and her hull. In Class 2 you copy this file, change the words, and your own boss is
in that list beside these.

## Stop 4 - A boarding party (video only)

**Taught in Class 3.**

You cannot reach this one from the game's menus today. None of the maps in Legendary
Missions sends a party aboard anything. So the video plays the scene a student builds in
the first six lectures of Class 3.

What happens on the video:

1. The ship pulls alongside a dead hulk. A quest finishes.
2. On a crew member's console, the handheld in the top bar offers a new tile, **Boarding
   Party**. It names the place: The Hulk.
3. The crew member presses **BEAM DOWN**. Their console is no longer Engineering. It is a
   handheld. A bar across the top says who they are, their job, and the room they are
   in: Chief Okoro, engineering, The Airlock.
4. Under the bar is a line of story, and under that the ways out of the room, each one a
   button.
5. A second crew member, at another console, is in the same room and has different
   buttons. The surgeon is offered things the engineer is not.
6. When the party returns to the ship, every console goes back to its station by itself.

What to notice: it is a short story told in rooms, and each reader gets their own copy.
The crew go as themselves, with the names and jobs they had on the bridge. A room is
about ten lines of plain words in the fact sheet.

## Stop 5 - A ruin (video only)

**Taught in Class 4.**

This one is on the video for the same reason. The video flies the ruin a student builds
in Class 4. It is called The Hollow.

What happens on the video:

1. Helm's map shows a named place past the hulk. The ship flies to it.
2. On the main screen the ruin is a built thing in space: rooms joined by passages, with
   an opening wide enough for the ship.
3. The ship flies inside. As it reaches each named place, a quest step finishes and the
   next place appears on the map.
4. At one place a recording calls the ship. Comms answers, and one of the answers puts a
   hidden room on the map.
5. For ten seconds the main screen leaves the ship and looks at two places in the ruin,
   with a line of words under each. This is a cutscene.

What to notice: the ruin is rooms and passages written as a list. Nobody modeled it in a
drawing program. The writer says "a room, this big, here" and the game builds the walls.

## Stop 6 - A mission is three things

This is the promise of Class 1. Do not open anything yet. Look at the picture.

*[Screenshot to add: File Explorer on a mission folder, showing the seven files below.]*

A mission is a folder. The one you make in Lecture 3 holds seven files:

| File | What it is | Who writes it |
|---|---|---|
| `mission.amd` | **The fact sheet.** Every word the crew reads, and every job they are given | You, from Lecture 5 on |
| `story.mast` | **The story file.** A short list of what happens and when | Mostly the template. You change marked words |
| `description.yaml` | The mission's name in the game's list | The tool, from the title you give |
| `settings.yaml` | Settings, such as how many player ships | The template |
| `story.json` | The list of libraries the mission asks for | The template |
| `script.py` | Starts the mission inside the game | The template |
| `__lib__.json` | The version of the libraries | The template |

So: **a folder, a fact sheet, a story file.** The other four files are made for you and
you leave them alone.

### The fact sheet

By the end of Class 1 your fact sheet is 185 lines long. This is one quest from it, whole:

```
#### [Close Inspection](approach)
---
Scope: shared
Starts when: at once
Objective: Close to within 500 of the hulk
Done when: reach derelict 500
Reward: 100 credits
Then: reveal salvage/boat
Part of: salvage
Required: true
---
The hulk is not answering hails. Bring the ship in close and take a look.
```

Read it as a card with three parts:

- The top line is the quest's name, and a short name for the files to use.
- Between the two rows of hyphens are its facts, one to a line: when it starts, when it
  is done, what it pays, what comes next.
- Under the second row of hyphens is what the crew is told.

There is no programming in it. `Done when: reach derelict 500` means what it says.

### The story file

By the end of Class 1 your story file is 115 lines long. Almost all of it came with the
template. In Lecture 11 you add eight lines, and you do not invent them. You copy them
from a card and change the marked words. The course calls this a **recipe card**. This is
that one:

```
#
# Wait for the Tug: what happens when that step starts.
#
//shared/signal/quest_started if QUEST_ID == "salvage/tug"
    await delay_sim(20)
    npc_spawn(5600, 0, 6000, "Salvage Tug", "tsn, tug", "cargo_ship", "behav_npcship")
    signal_emit("quest_signal", {"SIGNAL_NAME": "tug_arrived"})
    ->END
```

It says: when the step "Wait for the Tug" starts, wait twenty seconds, put a ship named
Salvage Tug on the map, and tell the quests that the tug has arrived. You will be able to
read that by Lecture 11. You will never be asked to write one from a blank page, in this
class or any other.

## Stop 7 - The six classes

| # | Class | You end with | You need first |
|---|---|---|---|
| 1 | The Writer's Desk and Your First Quest | A mission with a story told in quests | Nothing |
| 2 | People, Dialogue and Siege Bosses | A cast with voices, and a boss of your own in Siege | Class 1 |
| 3 | Boarding Parties | A boarding mission | Class 2 |
| 4 | Ancient Ruins and EVA | A ruin with a story | Class 2 |
| 5 | Open Universe: Building the World | A universe of your own to play in | Class 2 |
| 6 | Open Universe: Running the Campaign | The first act of a long campaign | Classes 3, 4 and 5 |

Classes 3, 4 and 5 can be taken in any order.

**Class 1 - The Writer's Desk and Your First Quest.** Twelve lectures. The first half is
your desk: files and folders, a command prompt, an editor, the marks a fact sheet is
written in, and the checker that reads your work back to you. The second half is a
story: a dead ship across the border, her missing lifeboat, a tug that arrives late, and
ten minutes to bring her flight log home. You end with a mission named Salvage Run whose
quests reveal one another, pay, and win or lose the game.
*[Screenshot to add: the Quest Log showing "Salvage Run" with its steps.]*

**Class 2 - People, Dialogue and Siege Bosses.** Your mission gets people. A station
that calls the ship; a harbormaster who says one of three things each time; a call the
crew must answer to be paid. Then you go back to Stop 3 and write a boss for Siege: the
Corsair Queen, with a flagship, two escort fleets, a quest that must be finished to win,
and a reserve ship she holds back. One lecture, on how the game remembers what a side
thinks of the crew, is in preparation.
*[Screenshot to add: the Siege setup screen with "Corsair Queen" chosen in the Boss
list.]*

**Class 3 - Boarding Parties.** Stop 4. In six lectures you write a place in rooms, give
each job on the crew its own choices, add skills and a little luck, and hand two of the
crew a story of their own. You end those six with an away scene about ten minutes long,
with two endings, that a party of one, two or three can finish. The second half of the
class, where the party walks a painted map, is in preparation.
*[Screenshot to add: three handhelds in the captain's cabin, with the two endings as
buttons.]*

**Class 4 - Ancient Ruins and EVA.** Stop 5. You write a ruin as rooms and passages,
dress it, name its places, make a place call the ship, hide a room behind an answer, and
run a quest through it from the way in to the heart. The lectures where a crew member
leaves the ship in a suit are being finished; one, on repairs outside a station, is in
preparation.
*[Screenshot to add: the quest list showing "The Hollow Survey" with its steps, and
Helm's map with The Altar on it.]*

**Class 5 - Open Universe: Building the World.** Open Universe is a mission that is a
whole galaxy: many systems, sides that trade and fight, work to take, and a game you can
stop today and continue tomorrow. Its world is one fact sheet. Here is a side from a
shipped one, The Silver Reach:

```
### [The Lantern Combine](lantern)
---
Color: #ffcc44
Character: trader
Disposition: neutral
Home: -4, 2
Values: honest 40, generous 30, peaceful 20
Offers: escort, bounty
Flies: Arvonian
Jump Charge: lantern_charge
---
Convoy families who keep the freight lanes lit. Fair dealers with long
memories for a kept promise - and longer ones for a broken cargo contract.
```

You write your own: sides, a map, jobs, a story, rivals. Two lectures are in
preparation.
*[Screenshot to add: the card the crew sees on arrival, reading Kestrel Relay.]*

**Class 6 - Open Universe: Running the Campaign.** Your universe becomes twenty evenings
of play: how to shape one session, how to plan acts, how the crew's name with each side
opens and closes doors over weeks. Most of this class is in preparation. It is the last
to be recorded.
*[Screenshot to add: to be chosen when the class is piloted.]*

## If something goes wrong

Only these rows were checked. Starting the game itself is on the video, not here.

| What you see | Why | What to do |
|---|---|---|
| The Options panel for Siege has no **Boss** line, or the quest list has no "Repel the Siege" | Your copy of the game is older than this course | Let the store update the game to 1.4.0. Until then, watch Stops 2 and 3 on the video: the battle is the same battle |
| You chose a boss and no boss came | She comes only when the raiders are down to her share of their greatest number: a quarter for the Warlord | Keep fighting. Or watch the arrival on the video |
| **Quests Offered** is in the Options panel and you see no offers | It is set to `none` in Siege unless you change it | Nothing. It is an extra, for work between waves |
| You cannot find a boarding party or a ruin | They are not in the game's menus | Stops 4 and 5 are on the video |

## Exercise

Play ten minutes of Siege. Any console, any setting. Win or lose.

Then write down three things that happened, and for each one, who or what caused it.
Like this:

| What happened | Who or what caused it |
|---|---|
| A starbase called for help | The raiders reached it |
| A line appeared in the quest list | The game started |
| The game ended | The last starbase fell |

Keep the page. In Lecture 7 you learn the two words the game uses for "what happened"
and "who": signals and roles. Your three lines are three of each.

## Checkpoint

You are done when all four are true:

- You have started the game, chosen Legendary Missions, then Siege, and sat at a console.
- You can say, for each of these, which class teaches it: a quest, a boss, a boarding
  party, a ruin.
- You can name the three things a mission is made of.
- You have your three lines from the exercise.

## Next

Lecture 2, "Files, folders and the command prompt", finds the game's folder on your
computer, and the `missions` folder inside it where every mission you saw today lives.
You open a window there and type your first command. For that you need the game
installed and started once. You have done both.

## Further reading

Nothing here is needed for Lecture 2.

- "Playing" and "Game features" in the Legendary Missions documentation: what the
  options on the Siege setup screen do.
- "Writing a Siege boss" in the same documentation. It is the reference for Class 2. Look
  at the first example and stop.
- The writer's walkthrough in the Open Universe documentation, "The Silver Reach". It is
  the reference for Class 5.
