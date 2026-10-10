# C4-5 video script - What is inside

> **STATE ON 2026-10-09. Read this first.**
>
> - **Everything this page needs is released.** The page is written for Artemis Cosmos
>   1.4.0, installed from Steam or itch.io, with a current tool and libraries. Record on
>   such an install.
> - **The student's mission is `MyRuin`** as Lecture 4 left it: a fresh
>   `sbs create MyRuin -t amd` mission whose `mission.amd` is
>   `c4-04-places-that-speak\example\mission.amd` (199 lines). `story.mast` is the
>   template's, untouched. The game is started with
>   `sbs run server,helm,comms -m MyRuin map=0`.
> - **`mission.amd` only.** `story.mast` is not opened.
> - **`example\` holds the one file that differs from the start:** `mission.amd` (247
>   lines).
> - **The template picks things up since 2026-10-09.** Its `story.json` loads Legendary
>   Missions' `items` addon. A `MyRuin` made before that date does not: with that folder
>   every thing is drawn and none can be taken, lint says `clean`, and the log is empty.
>   Record on a folder made today. The page gives the one line for an older folder.
> - **The lecture can be done after Lecture 7 as well as after Lecture 4.** The steps
>   find their place by a comment line that both files have. Typed onto Lecture 7's
>   finished file they lint `clean` and play the same (that file is the start of
>   Lecture 8).

> **Measured 2026-10-09, in the mock.** Tool `sbs` as installed in `data\missions`,
> library as packaged in `__lib__` (sbs_utils `e84602e7`, Legendary Missions `b37a320`).
> The page's steps were typed one at a time onto Lecture 4's finished file, with lint
> after each. Then 41 one-change variants of the finished file, each linted and all but
> one played headless by a probe that asks the library what it placed, puts the ship on a
> thing, and prints the hold, the quests, the pay, the word and what the crew is told.
>
> **What the script did, and what it did not.** It MOVED the ship onto each thing. It did
> not fake the pick-up: the stand-in's own contact rule reported it, the `items` addon's
> own route took the thing, and the library sent `hollow_taken`. No engine, no window.
> Nobody has flown a ship into a thing in this mission.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyRuin` as Lecture 4 leaves it, lint clean, made with today's template. `mission.amd` has 199 lines |
| `story.json` | Has the line with `items` in it. Check before recording |
| VS Code | `MyRuin` folder open, `mission.amd` in one tab, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 8 with a server, a Helm console and a Comms console |

## Confirm on camera

"Lint" means the installed tool, run from `data\missions` on a folder holding the files
with that one change. "Mock" means the mission was then played headless with the packaged
library. If an item fails while recording, stop and fix the page.

1. Lint is `clean` after each of Steps 2 to 6. (Lint.)
2. At the start the library has placed one pick-up of `canister` at 3600, 0, 20500 and one
   of `stone_bowl` at 3000, 0, 17500, and is watching one piece. The quest list holds
   What the Survey Left and The Bowl. (Mock.)
3. With the ship put on the canisters: the hold has 3, the crew is told
   `Pickup: Survey Canister x3`, What the Survey Left is done, the side has 60. (Mock.)
4. With the ship put on the bowl: the hold has 1, the piece is taken, the library has sent
   `hollow_taken`, The Bowl is done, the side has 260. (Mock.)
5. With no ship near, after six seconds: nothing is taken and no word is sent. (Mock.)
6. The ship 1500, 1000, 800 and 700 from the canisters takes nothing. At 500 it takes
   them. (Mock. This is the stand-in's own distance rule, read from the art's ship data.)
7. With the `items` line taken out of `story.json`: lint `clean`, both things placed,
   the ship put on each, nothing taken, no word, log empty. (Lint, Mock.)
8. Every row of the tables in Step 7 and the three "not mistakes": lint for all of them,
   and the mock for what the game does. (Lint, Mock.)
9. A forced Science scan of the canister and of the bowl reads
   `Salvageable cargo - no upgrade signature detected.`, with and without a scan record
   for `canister`. (Mock.)
10. The exercise: two caches and `collect 2 canister` finish on the second pick-up with 6
    in the hold; `Starts when: reach cache 900` places the canisters when the ship is
    within 900; `Starts when: signal bowl_shown` with the answer's `signal bowl_shown`
    places the bowl when Comms marks the Gallery. (Lint, Mock.)

Read in the library's code, not measured: the piece is also "taken" when it is carried
clear of every room on a tether (the only case measured is a place typed outside the
rooms, which sends the word at once).

Not seen by anyone. If one is not as described, stop and fix the page:

1. A canister or the bowl drawn in the ruin, from Helm or the main screen.
2. A ship taking a thing by flying into it, in THIS mission, and how close it has to be.
3. Where `Pickup: Survey Canister x3` is drawn.
4. The quest list with the two quests, and each one completing.
5. Science selecting a thing and reading the `scan` tab.
6. The Cache as a contact on Helm's map.

> Keep off camera: suits. And the Upgrades app on the handheld: a thing with
> `Type: item/quest` is deliberately not listed there.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The game. Helm flying into The Nave; three canisters ahead. The ship reaches
them. Cut to the quest list: What the Survey Left, done. Cut to the niche and the bowl.

**Say:** "So far the ruin has rooms, and places, and a voice. || Today it has things in
it. || There are sample canisters in the big room, | and a stone bowl at the back of the
built one. || A ship that flies up to either one takes it aboard. ||| And when the bowl is
taken, | the game itself tells the story so. ||"

### 2. A thing, a place and a word

**Screen:** The first table from Step 1 of the page, then the second.

**Say:** "It takes three records to make a thing you can take. || The item says what the
thing is. | A place says where one of them lies. | And a quest says what the story does
about it. ||| A quest can wait in two ways. || It can wait for a kind of thing, by its
key, | and that's for ordinary finds. || Or it can wait for a word, | and that's for the
one thing the whole ruin is about. || The game sends that word by itself. ||"

### 3. The Items section

**Screen:** `mission.amd`. Find the Characters comment. Above it, type the Items comment,
the heading and Survey Canister. Point at `(canister)`, then at `Art:`.

**Say:** "Items live in a section of their own. || I find the comment above Characters, |
and I type the new section above it. || Two hashes for the section, and three for the
item. ||| The key is canister, | and that's the word everything else will use. || Type
says item, slash, quest, | which means the story carries it. || And Art is what it looks
like. ||| That last line matters more than you'd think. || A ship takes a thing by flying
into it, | and only some shapes can be flown into. || The table on the page lists them. ||
Leave the line out, or misspell it, | and the thing just sits there for the whole game. ||
Lint won't tell you. ||"

### 4. A place that holds it

**Screen:** Relics section. Below The Niche, type The Cache. Highlight `Item: canister`
and `Qty: 3`.

**Say:** "Now a place for it. || This is a place like the ones from Lecture three, | with
two new lines. || Item, and the item's key, means one of these lies here. || And Qty,
three, means it's worth three. ||| The crew takes all three in one go. || So this is one
thing to pick up, | and it's worth three in the hold. | Remember that for the next step.
||"

### 5. A quest that waits for it

**Screen:** Quests section. Above the Scans comment, type What the Survey Left. Highlight
`Done when: collect canister`.

**Say:** "Here's the quest that waits for them. || Everything in it is from Class one,
except one line. || Done when, collect, canister. | The word after collect is the item's
key. ||| And here's the catch. || The game counts pick-ups, | it doesn't count what a
pick-up is worth. || My cache is one pick-up. || If I write collect three canister, | the
game waits for three separate pick-ups, | and with one cache, it waits forever. ||| Lint
says clean either way. | So I write collect canister, with no number. ||"

### 6. The piece

**Screen:** Items section: type The Stone Bowl. Then The Niche: add `relic_piece` to
`Roles:` and add `Item: stone_bowl`. Highlight both.

**Say:** "Now the thing the ruin was hiding. || First the item, a stone bowl. || Then I go
back to the Niche, and I change two lines. ||| On the Roles line I add a comma, and relic
underscore piece. || That role isn't mine. | It's the game's own word, | the way entrance
was in Lecture three. || It means the thing in this place is the piece. ||| And then Item,
stone bowl. || It takes both lines. | The role alone is an empty place, | and the item
alone is just another find. ||"

### 7. The word the game sends

**Screen:** Quests section. Type The Bowl. Highlight `signal hollow_taken`. Scroll to `###
[The Hollow](hollow)` and point at the key.

**Say:** "And the second quest. || Done when, signal, hollow taken. ||| Now, nothing in my
file sends that word, | and lint still says clean. || That's because the game sends it. ||
It takes the key of the ruin, which is hollow, | and it adds underscore taken. ||| It's
the ruin's key. | It's not the place's, and it's not the thing's. || Lint will catch you
if you use either of those. ||| The word is sent once. || So the quest has to be running
before anybody can reach the bowl. | That's why this one starts at once. ||"

### 8. Lint, and play

**Screen:** Command prompt: `sbs lint MyRuin`, clean. Delete the `Art:` line from the
canister, save, lint: clean. Put it back. Then `sbs run server,helm,comms -m MyRuin
map=0`. The quest list. Fly into The Nave and at the canisters. Fly to the far end of The
Gallery and at the bowl.

**Say:** "I run lint, and it's clean. || Now I take out the Art line, | and lint is still
clean. || That's the one to check by eye, so I put it back. ||| Then I start the game. ||
Both quests are in the list. || I fly into the Nave and straight at the canisters. |
There's the pick-up, times three, and the first quest is done. ||| Now the Gallery, all
the way to the back. || And there's the stone bowl. | I take it, and the second quest is
done. || And I never wrote the line that said so. ||"

### 9. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Add a second cache, and make the quest want both. || Make
the canisters appear only when the ship comes near. || Make the bowl appear only when
Comms has heard Rook out. ||| Then break one line where lint can see it, | and one where
it can't. || Later in this class, someone goes in and takes that bowl by hand. ||"