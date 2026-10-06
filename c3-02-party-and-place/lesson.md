# Class 3, Lecture 2 - A party and a place

## What you will have at the end

When the ship pulls alongside the hulk, a boarding party forms. Your crew go aboard as
themselves: the people you wrote, at the consoles they sit at. Inside are three rooms, and
from every room there is a way back and a way home.

*[Screenshot to add: the Boarding Party app offering "The Hulk".]*

You will write two short sections in `mission.amd`, add one line to a quest, and paste
one recipe card into `story.mast`.

## The video

*[Link to add when recorded.]*

## Before you start

- Your mission from Class 1, with the **Close Inspection** quest from Lecture 8.
- You have pasted a recipe card into `story.mast` before (Class 1, Lecture 11).
- `sbs lint MyMission` says `clean`.

## Step 1 - Your crew

Open `mission.amd`. Go to the very end of the file and add a new section:

```
## [The Watch](watch)
---
crew
Ship: Artemis
Names: locked
---
The people aboard for this story.

### [Chief Okoro](okoro)
---
Console: engineering
Face: terran_female
Roles: engineering
---

### [Dr Hale](hale)
---
Console: science
Face: terran_male
Roles: medical
---
```

This is a crew roster. Each record is the person at one console. Whoever sits at
Engineering is Chief Okoro, on the bridge and aboard the hulk. There is one cast, and it
is the crew.

| Line | What it means |
|---|---|
| `crew` | What kind of section this is. A bare word, on the first line of the fence |
| `Ship: Artemis` | The ship these people crew. `Artemis` is the first ship in this mission |
| `Names: locked` | These are your people. A player's own saved name is not used at these consoles |
| `Console: engineering` | Which seat this person fills |
| `Face:` | Their portrait |
| `Roles: engineering` | Their job. Next lecture, it decides which choices they are offered |

Leave out `Names: locked` and the roster still names the consoles, but any player who has
saved a name of their own keeps it. Lock it when the story needs your cast.

A console the roster does not mention, such as Helm, gets a name from the game.

## Step 2 - The place

Below the crew section, add the rooms:

```
## [Scenes](boarding)

### [The Airlock](airlock)
% The outer door was never sealed. Frost on the inside of the glass, and a row of suits still on their hooks.

- [Go aft, toward the reactor](reactor)
- [Go forward, to the bridge](bridge)
- [Return to the ship]()

### [The Reactor Room](reactor)
% Cold. The core was shut down by hand, in the right order, by someone who had time.

- [Go back to the airlock](airlock)
- [Return to the ship]()

### [The Bridge](bridge)
% Every station is dark but one. The log is open on the captain's chair, and the last entry is a single word.

- [Go back to the airlock](airlock)
- [Return to the ship]()
```

A room is a record with two parts.

| Part | How to write it | What it does |
|---|---|---|
| What the party finds | One line starting with `%` | Everyone in the party reads it |
| The ways out | Lines starting with `- [words](key)` | Each is a choice. The key names the room it leads to |

Keep each `%` line on one line, however long it gets. If you write two `%` lines in one
room, the game picks one of them at random each time.

A choice with empty round brackets, `()`, leads nowhere. Taking it ends the visit: the
party closes and everyone is returned to their station.

Keep the section key `boarding` exactly as written. The recipe in Step 4 finds your rooms
by that key.

## Step 3 - Two rules for every room

Read your rooms again and check each one against these.

1. **A way back.** Every room has a choice that leads to a room the party has already
   been in. A room whose choices only lead onward is a trap.
2. **A way home.** Every room has a `()` choice. Without it, a party that has seen enough
   cannot leave.

Lint checks one of the mistakes you can make here and not the other.

| Mistake | What lint says |
|---|---|
| A choice whose key is misspelled, such as `(brige)` | A warning that names the room and the bad key |
| A room with no choices at all | `clean`. Nothing warns you |

## Step 4 - Start it

Two edits.

**In `mission.amd`**, add one line to your Close Inspection quest, above `Reward:`:

```
Then: signal board_hulk
```

`Then:` says what happens when the quest completes. This one sends a signal named
`board_hulk`.

**In `story.mast`**, paste this recipe card. It has two parts. (Your crew roster needs
nothing here: the file already reads it.)

First, find the line that begins `science_define_scan_amd`. Below it, with the same
indent, add:

```
    # The rooms of the boarding scene, read once and kept for the route at the end.
    shared BOARDING_SCENES = dialogue_scenes(amd_section(MISSION_DOC, "boarding"))
```

Second, at the very end of the file, add:

```
#
# Start the boarding visit. `Then: signal board_hulk` in mission.amd sends this signal
# when the Close Inspection quest completes.
#
//shared/signal/board_hulk
    party_ship = next(iter(role("__player__")), None)
    ->END if party_ship is None
    boarding_visit(party_ship, BOARDING_SCENES, "airlock", title="The Hulk")
    ->END
```

You change three things on this card when you reuse it, and nothing else:

| On the card | Change it to |
|---|---|
| `board_hulk` (twice: here and in your quest) | The signal name your quest sends |
| `"The Hulk"` | What the crew should see as the name of the place |
| `"airlock"` | The key of the room the party arrives in |

## Step 5 - Check it

```
sbs lint MyMission
```

You want `clean` under `mission.amd`.

## Step 6 - Play it

1. Start your mission with a server and an Engineering console.
2. Look at the top of the console, beside the small tablet icon. The name there is Chief
   Okoro.
3. Fly inside 500 of the hulk. Close Inspection completes.
4. Press the tablet icon. This is the PADD. One of its tiles is **Boarding Party**, and it
   says The Hulk.
5. Press the tile. It says "Going down to The Hulk" and shows Chief Okoro.
6. Press **BEAM DOWN**. The console becomes the boarding party's handheld. The bar across
   the top says who you are, your job, and the room you are in: Chief Okoro, engineering,
   The Airlock. Under it is your line of text, with each way out as a button.
7. Choose a way out. The page keeps what you have read: the choice you made, then the
   next room's line under it. Walk all three rooms.
8. Take **Return to the ship** from any room. The visit ends, and the console is back at
   Engineering without another press.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| The console is not Chief Okoro | The ship is not named `Artemis`, the record's `Console:` is not the seat you took, or the first line of the roster's fence is not the word `crew` |
| No Boarding Party tile on the PADD when you reach the hulk | The quest has no `Then: signal board_hulk` line, or the name on the card does not match it |
| After BEAM DOWN the screen still shows the Boarding Party app, now with a BEAM UP button | Your mission does not load the boarding addon, so there is no handheld to show. A mission made from the current template has it; an older one needs a new `sbs create` |
| Every PADD tile says IMAGE NOT FOUND | The same cause: a mission made from an older template. Make a new one and copy your `mission.amd` and `story.mast` into it |
| The quest completes and no party forms | The Scenes section's key is not `boarding`, or the arrival room on the card is not one of your room keys. Lint does not warn about either |
| Taking a choice ends the visit | Its key is misspelled. Lint warns about this one |
| A room has no way out | It has no choices. Lint does not warn about this one |

## Exercise

Add a fourth room of your own, and a third crew member.

1. Give the room a name, a key and one `%` line.
2. Add a choice to it from one of the three rooms.
3. Give it a way back and a way home.
4. Add a person for the Helm console to your roster, with a job of your choosing.
5. Run lint, then walk to your room in the game.

## Checkpoint

You are done when all four are true:

- `sbs lint MyMission` shows `mission.amd` as `clean`.
- Each console in your roster shows the name you wrote.
- The Boarding Party forms when Close Inspection completes, and not before.
- You can reach all four rooms, and Return to the ship puts you back at your station.

## Next

Lecture 3 gives each person their own menu: the engineer sees one choice, the surgeon
another, and what the party learns depends on who went.

## Further reading

- "Boarding parties" in the library documentation: `boarding_visit`, and what it is built
  from.
- "Crew rosters" in the library documentation: `Names:`, `Roles:`, and who a console is.
