# C5-2 video script - Your universe file

> **STATE ON 2026-10-08.** Re-measured against the released tools: `sbs` 0.13, the
> published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions `b20726f`, the Open
> Universe engine library built 2026-10-05), and the `ou` template that `sbs create`
> downloads today (starter `60c30bc`). The template now carries the two travel lines, and
> lint now checks that `story.mast` loads, so the page no longer teaches a card for the
> first or a second command for the second.
>
> Everything was run by script in the game's stand-in (the mock), from a copy of the
> mission placed where its save cannot reach a player's own saves. Nothing was run in the
> real game today. The engine run of 2026-10-03 (below) was on the first version of these
> files; the three records the student writes have not changed since.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | None yet. `MyUniverse` is made on camera in scene 2. There must be no `MyUniverse` folder already |
| Saves | No file named `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves`. If one is there, the first start on camera continues an old game |
| Tool and libraries | `sbs` current (`sbs update`), then `sbs fetch "MyUniverse" --update-libs` on camera in scene 2 |
| VS Code | Open on `C:\Cosmos\data\missions`, font size raised, a command prompt beside it |
| Game | Closed. Started on camera in scene 9 with `sbs run server,helm,comms -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-08, with the page's own files:**

1. A mission fresh from `sbs create -t ou --title "The Kestrel Verge"`: lint is `clean`,
   and it plays with nothing changed (133 labels run, no errors). Engage is on and
   charted places are on, from the template's own two lines.
2. The page's steps were applied to that fresh mission by a script. The two searches find
   4 and 2. The result is `example\`. Lint is `clean`.
3. First start: mode `story`; the arrival card is handed `Kestrel Relay` and the page's
   line; two stations at home, Kestrel Relay and Starbase, both on the players' side; the
   Quest Log is handed a `Charted Locations` group holding Kestrel Relay.
4. Comms, selecting either station, is sent these buttons: Market, Hail, Build Weapons,
   Request Priority Docking, Accept Cargo Run, Transport a passenger, Accept Patrol
   Mission.
5. The function behind **Accept Cargo Run**, then the signal **Engage** sends: the ship
   arrives in another system (2, -3 with the test's seed), the run is Done, credits go
   from 500 to 900. The Quest Log's own gate says Helm is offered Engage on the accepted
   run and Comms is offered Abandon; Helm's hint reads "Manage quests at the Admiral or
   Comms console."
6. The save file `universe_save_the_kestrel_verge_1.yaml` holds that system and
   `tsn: 900`. A second start begins there with the run still Done. Engaging the charted
   Kestrel Relay brings the ship home, with both stations there.
7. A start with **New Game** replaces the save: a new seed, home, 500 credits.
8. Every row of the four tables in Step 8: 46 variants, one change each, each linted and
   played.

**In the real engine (2026-10-03, by a probe, on the first version of these files):** a
new game, the cargo run, the jump, the save, then Continue and the way home. Server with
a Helm and a Comms console. Nobody looked at a screen.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. The arrival card: where it is drawn, on which windows, for how long.
2. Comms: the station's buttons as a list, and **Accept Cargo Run** among them.
3. Helm's Quest Log: the cargo run listed, an **Engage** button, and a group named
   **Charted Locations**.
4. The jump, and the card on arrival. The system a run leads to is unnamed, so its card
   would read `Uncharted` and two numbers. The numbers change with every new game.
5. The start screen without `map=0`: the title, the two lines, and a **Start** list
   reading **Continue**, with **New Game** as its other choice.
6. What a player sees when the universe file was not loaded. The mock shows only the line
   in `mast.runtime.log`.
7. In VS Code: `Ctrl+H` showing 4 and 2, and **Rename** on a file's right-click menu.

> The folder `narration\` beside this file was made from the script of 2026-10-04 and is
> out of date.

## Scenes

### 1. Cold open

**Screen:** The arrival card reading Kestrel Relay, then Helm's Quest Log with Charted
Locations open.

**Say:** "In Class 1, you wrote a mission with one map in it. || This class is about a
mission that's a whole universe, | with many systems, and a game you can stop and pick up
again. ||| And this is the first minute of yours: | a title, a place to start with a name
you gave it, | and a save file. || It's one file of your own, | and a few words changed in
another. ||"

### 2. Make the mission

**Screen:** The command prompt. Type `sbs create MyUniverse -t ou --title "The Kestrel
Verge"`. Then `sbs fetch "MyUniverse" --update-libs`. Then `sbs lint MyUniverse`.

**Say:** "You know this command from Class 1, | and only one word is different. || The
template isn't a m d any more, | it's o u, for Open Universe. || So this is a new folder,
| and you're not building on your Class 1 mission. ||| Then I fetch its libraries, the way
I did before, | and I run lint. || It says clean, and I haven't written a word yet. || It
even plays as it is. | Everything from here is me replacing what I was given. ||"

### 3. What's in the folder

**Screen:** The file list in VS Code. Point at `my_universe.amd`, `story.mast`,
`description.yaml`.

**Say:** "Three files matter today. || There's the universe itself, which I write. | There's
the story file, which tells the game which universe to load. | And there's the one line
for the game's list of missions, | which already has my title. ||| Notice there's no file
called mission. || In this kind of mission, the fact sheet is the universe file, | and I
get to name it. ||"

### 4. Name the file, and the title record

**Screen:** Rename `my_universe.amd` to `kestrel_verge.amd`. Open it. Rewrite the `#`
record.

**Say:** "So first, I give the file my own name. || Then the record at the top, the one
with a single hash. || One hash means, this is the universe itself, | and there's only
one of those in the file. ||| Inside the fence is the word Universe, on a line by itself.
| It says what kind of record this is, just as the word Arc did in Class 1. || Under the
fence I write what this place is. || Now here's the thing to know: | the game never shows
this record to a player. || It's the title page of my manuscript, | and it's for me and
my co-writers. ||"

### 5. The scenario

**Screen:** Type the `## [Scenario](scenario)` record under the title record.

**Say:** "Next comes a chapter, with two hashes, called Scenario. || It holds one line
today, Mode, | and the mode says what kind of game this is. || Story is one ship and an
ending. | Campaign is a long game over many evenings. | Sandbox is an open world with no
ending. ||| Today all three play alike, | so I write the one that's true of my story. ||
And the key has to be the word scenario, | because that's the word the game looks for.
||"

### 6. A front door

**Screen:** Scroll to the end of the file. Type the Landmarks chapter and the Kestrel
Relay record. Highlight `At: 0, 0`.

**Say:** "Now the place they start. || At the bottom I add a chapter called Landmarks, |
and one landmark under it, with three hashes. || The line At says which system it's in, |
and zero, zero is home, where every new game begins. ||| That one record does three
things. || When the crew arrives, a card names the system, | and shows my line under the
name. || There's a station there with that name. || And it goes on the crew's list of
charted places, | so they can find their way back. ||| Keep the line under the fence to
one line, | because the card only shows the first. ||"

### 7. The story file

**Screen:** `story.mast`. `Ctrl+H`: `My Universe`, 4 found, Replace All. Then
`my_universe.amd`, 2 found, Replace All. Then the two lines under `@map/`. Then point at
the two travel lines.

**Say:** "The story file still has the template's names in it. || So I press control H, |
I search for My Universe, and it finds four. || I replace all four with my title. || Then
I search for the old file name, | it finds two, and I replace those. ||| If your counts
aren't four and two, | stop and look before you replace. ||| Next, the two lines under the
map line. | Those are what a player reads on the start screen, | so I write my own. || And
these two lines near the top I leave alone. || The first gives Helm an Engage button, |
and the second keeps the list of charted places. ||"

### 8. Check it

**Screen:** Save both files. `sbs lint MyUniverse`: clean. Then change one letter on the
`display:` line, save, lint again: still clean. Put it back.

**Say:** "Lint reads both files now, and it says clean. ||| But I want you to see the one
it can't catch. || I change a single letter of the title, on this one line, | and lint
still says clean. || If I played that, my universe wouldn't load. | The game would start
anyway, with a place called Home Port, | and none of my work in it. || So the title has to
be spelled the same way, all four times. || If it ever happens to you, | the runtime log
in your mission folder says so. || I put the letter back. ||"

### 9. Play it

**Screen:** `sbs run server,helm,comms -m MyUniverse map=0`. The arrival card. Comms:
select a station, Accept Cargo Run. Helm: the handheld, Quests, the cargo run, Engage.
The jump. Charted Locations.

**Say:** "Here's the card, with my station's name on it, and my line. || On Comms, I
select a station, | and I take the cargo run it offers. || Then on Helm, I open the Quest
Log, | I pick the run, and I press Engage. || And that's the jump you're watching. ||| We're somewhere new, and
the run has paid. || And look at this group, Charted Locations. | Kestrel Relay is in it,
| and that's my way home. || But I'm not going home yet. | I'm closing the game right
here. ||"

### 10. The save, and coming back

**Screen:** File Explorer: `common_data\saves`. Open the save file; highlight
`current_system`. Start the game again with the same command. Helm: Charted Locations,
Kestrel Relay, Engage.

**Say:** "This is what the game kept. || It's a file named after my title, | and here's
the system I stopped in. ||| I start the game again, with the same command, | and I'm
where I left off, with the money from the run. || Then I pick Kestrel Relay, I press
Engage, and we're home. ||| Two things to remember about that file. || It's named from
the title, | so if you change the title, you start a new, empty game. || And to begin
again on purpose, | close the game and delete the file. ||"

### 11. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now make it yours: | your title, your file name, your home port, and your two
lines. || Before you play, write down what you think the save file will be called, | and
then go and look. ||| Next time, we fill this place with people: | three factions, and one
of them shoots first. ||"
