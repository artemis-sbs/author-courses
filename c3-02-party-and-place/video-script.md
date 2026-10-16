# C3-2 video script - A party and a place

> **STATE ON 2026-10-09. Read this first.**
>
> - **Everything this page needs is released.** The page is written for Artemis Cosmos
>   1.4.0, installed from Steam or itch.io, with a current tool and libraries.
> - **The class's mission is `MyBoarding`**, made in Lecture 1 with
>   `sbs create MyBoarding -t amd --title "The Hulk"`. This lecture starts from that
>   mission untouched: `mission.amd` is 60 lines.
> - **The quest is typed here.** Earlier drafts of this lecture leaned on a quest from
>   Class 1. The student now types Close Inspection in Step 4, with its `Then:` line.
> - **The card is one block at the end of `story.mast`.** There is no second line to put
>   inside the map any more: today's starter keeps the fact sheet where a route can read
>   it.
> - **The way home is in the arrival room only.** One press of it ends the visit for
>   everybody, so it is not in every room. Lecture 6 uses the same rule.
> - `example\` holds the two finished files, `mission.amd` and `story.mast`.

> **Measured 2026-10-08 and 09, in the mock.** Tool `sbs` as installed, library as
> packaged (sbs_utils `ae2bbf4a`). The steps were typed onto a fresh `sbs create`
> mission, linted at each step, and played headless with stand-in consoles: a probe moved
> the ship alongside, made the two calls the BEAM DOWN button makes, and pressed choices
> through the handheld page's own signal. Then 24 one-change variants, each linted and
> played. No engine, no window.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyBoarding` as `sbs create` made it. Lint clean. `mission.amd` 60 lines |
| VS Code | `MyBoarding` folder open, `mission.amd` and `story.mast` in two tabs |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 7 with a server, Helm and Engineering |

## Confirm on camera

1. With only the rooms typed, lint prints the `section-not-loaded` line on the page; with
   the quest and the card in, it is `clean`. (Lint.)
2. The Engineering console is Chief Okoro, engineering, locked; Science is Dr Hale,
   medical. Helm, not on the roster, gets a name from the game and the job `helm`.
   (Mock.)
3. Inside 500 of the hulk Close Inspection completes, 100 credits are paid, and a visit
   named The Hulk is on offer in the airlock. (Mock.)
4. Both consoles are offered the same three choices in the airlock. Any console's press
   moves everyone. The page keeps who chose, the choice, then the next line. (Mock.)
5. Return to the ship ends the visit for both at one press, and no party is on offer
   afterwards. (Mock.)
6. Every row of both mistake tables. (Lint, Mock.)

Seen on a real screen by earlier pilots of this lecture, with one console: the Boarding
Party tile, BEAM DOWN, the handheld's bar and buttons, and the console back at
Engineering afterwards. That was before this rewrite; the rooms and the card's shape have
changed since.

> **Seen in the real engine, 2026-10-15** (state final; server, Helm, Engineering). The
> Engineering console's handheld reads Chief Okoro from the start and again after the
> visit; one press of Return to the ship puts the console back on its station. In the
> Quest Log, Close Inspection's lead line sits ABOVE a small picture of the hulk, then
> the two paragraphs. At Helm's default zoom the hulk is off the map; one zoom-out shows
> it as an unnamed mark, named only within about 4K. Helm, not on the roster, gets a
> random name: do not quote it. Awaiting a re-shoot after library fixes: Chief Okoro's
> face, which did not draw on the Boarding Party app or beside his picks.

## Scenes

### 1. Cold open

**Screen:** The handheld on an Engineering console: a bar with Chief Okoro, engineering
and The Airlock, one line of text, three buttons.

**Say:** "This is a boarding party. || The ship is alongside a dead hulk, | and the
Engineering console has just gone aboard as Chief Okoro. ||| He's the person who sits at
Engineering in this story, | on the bridge and on the hulk. ||| Last time you played a scene
somebody else wrote. || Today you write your own: who goes, where they go, | and the few
lines that start it. ||"

### 2. Your crew

**Screen:** The game first: the Engineering console at the start, before anyone has
flown, the name Chief Okoro at the top beside the handheld icon. Then `mission.amd`, the
end of the file. Type the roster: the section with its fence, then the two people.

**Say:** "First, who goes. || This is the Engineering console at the start of the game, |
and the name at the top, Chief Okoro, is a name I wrote. ||| I go to the end of my fact
sheet and add a section, | and the first line inside its fence is one bare word, crew. || Then the ship these people crew, |
and a line that says the names are locked. ||| Under it, one record for each person. ||
Each one says which console they sit at, | what they look like, and their job. || So
whoever sits at Engineering tonight is Chief Okoro, | on the bridge and aboard the hulk.
|| There's one cast, and it's the crew. ||"

### 3. The place

**Screen:** The game first: Chief Okoro's handheld in the airlock: the bar naming The
Airlock, one line, three buttons. Then, below the roster, type the Scenes heading and the
three rooms. Point at a percent line, then at a choice, then at the empty brackets.

**Say:** "Now, where they go. || On the handheld, the bar names the room, The Airlock, |
and under it there's one line and three buttons. || All of that is one record I write. |||
A place is a section of rooms, | and a room is the simplest record you've written yet. |
It has no fence at all. ||| One line that starts with a percent sign is what the party
finds. || Each line that starts with a dash is a way out: | the words in square brackets
go on a button, | and the key in round brackets names the room it leads to. ||| And this
one has nothing in its round brackets. | On the handheld, it's the Return to the ship
button. || It leads nowhere, and taking it ends the visit. ||"

### 4. Lint notices

**Screen:** Command prompt: `sbs lint MyBoarding`. One warning, ending
`section-not-loaded`. Highlight the word `boarding` in it.

**Say:** "I save, and I run lint, | and for once it isn't clean. || It says nothing in
this mission reads a section with this key, | so my rooms are never loaded. That's true.
|| Nothing does read them yet. | So I leave the key exactly as it is, | and I go and add
the thing that reads it. ||"

### 5. Two rules

**Screen:** The game first: the handheld in the reactor room, its one button Go back to
the airlock. Then the three rooms. Highlight each `Go back to the airlock`. Then highlight
the single `Return to the ship`.

**Say:** "Before that, two rules. || One: every room has a way back. || In the reactor
room, the handheld has one button, | and it's the way back to the airlock. || A room with
no way out holds the party for good, | and lint won't tell you. ||| Two: the way home goes where
leaving is a decision. || One press of that button, by anyone, | ends the visit for
everybody, and the place isn't offered again. || So it's in the room they arrive in, | and
nowhere else for now. ||"

### 6. Start it

**Screen:** The game first: Helm's handheld icon, Quests: Close Inspection selected, with
the hulk's picture and two paragraphs. Then `mission.amd`, the Quests section: type Close
Inspection, and highlight its `Then:` line, then its description: the ship line at the
top, two paragraphs. Then the game: Engineering's handheld icon, the Boarding Party tile
offering The Hulk. Then `story.mast`, the very end: paste the card. Highlight
`board_hulk`, `"airlock"` and `"The Hulk"` in turn. Lint: clean.

**Say:** "Now the start. || On Helm, the handheld's Quest Log has a step called Close
Inspection, | with a picture of the hulk and two short paragraphs. ||| It's a quest of the
kind you wrote in Class 1: | bring the ship within five hundred of the hulk. || The new
line is this one. | When the quest completes, it sends a signal, | and I've named it board
hulk. ||| The description's a page, the way it was in Class 1. || A picture of the hulk at
the top, | then two short paragraphs. || The second one tells the crew a party can cross, |
so they think about who goes. ||| When the quest completes, Engineering's handheld has a
tile called Boarding Party, | offering a visit called The Hulk. || One recipe card makes
that happen. | I open the story file, go to the very end, and paste it. || I don't read
it. | I change three things on it, and they're on the page: the signal's name, | the key
of the room the party arrives in, | and the name the crew sees on the tile. ||| I run lint
again, and now it's clean. ||"

### 7. Play it

**Screen:** Command prompt: `sbs run server,helm,engineering -m MyBoarding map=0`. The
Engineering top bar: Chief Okoro. Fly Helm to the hulk (zoom the map out once: it is the
unnamed mark ahead). On Engineering: the handheld
icon, the Boarding Party tile, BEAM DOWN. Walk aft, back, forward, back. Return to the
ship.

**Say:** "I start the game with a server, a Helm and an Engineering console. || And
there's my name, before I've flown anywhere. ||| I bring the ship in close, | and the
quest completes. || On Engineering I open the handheld, | and there's a Boarding Party
tile offering The Hulk. I beam down. ||| Now this console is the party's handheld. | It
says who I am, my job, and the room I'm in, | and under that is my line, with a button for
each way out. || I go aft, and the page keeps what I've read. || Back, forward, back
again. ||| And from the airlock, I go home, | and the console is back at Engineering. ||"

### 8. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Your turn. Add a fourth room, with a way in and a way back, | and add a third
person to your roster, at Helm, with a job you make up. ||| Then break it on purpose. |
Delete the way back from your new room, | run lint, and read the word clean. || Then walk
into that room, and see what your crew would see. ||| Next time, everyone gets a different
menu. ||"