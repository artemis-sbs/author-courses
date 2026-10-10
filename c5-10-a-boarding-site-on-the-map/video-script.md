# C5-10 video script - A boarding site on the map

> **STATE ON 2026-10-10, evening.** Written that morning, and re-measured the same
> evening against the released tools: `sbs` 0.14, the published v1.4.0 libraries
> (sbs_utils `ed811ecb`, LegendaryMissions `cc9cd06`, Open Universe `80e9397`). Lint, the
> three long plays, and every row of Step 11 that the release touched were run again.
> Everything was run by script
> in the game's stand-in (the mock), from a copy of `MyUniverse` placed where its save
> cannot reach a player's own, with the `frontier` and `station` tile art copied into
> the copy's own media folder. A script reported the ship docked (it did not fly it),
> opened each call and gave its answer by the game's own calls, seated one stand-in
> console as Weapons, let a test setting beam it down, pressed the offered choices, and
> clicked map cells by the game's own call. The shot at the loader was the library's
> strike call, not the Fire app. **Nothing in this lecture has been run on a real
> console by a person, and nobody has seen any of its screens.** In the real game, with
> one Helm console connected and a script driving, the build's own sample of these two
> sites opened both from their calls, refused the door without the key, opened it with
> the key, ended the visit on beam-up, and kept its state through a jump and a Continue.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 9 leaves it. `story.json` has the line with `boarding` in it |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| Art packs | Fetched on camera in scene 6. Check beforehand that the download works |
| VS Code | `MyUniverse` open, `kestrel_verge.amd` in a tab, font size raised |
| Game | Closed. Started on camera in scene 5 with `sbs run server,helm,comms,weapons -m MyUniverse map=0`, and again in scenes 9 and 10 |

## Confirm on camera

**In the mock, by script, on 2026-10-10, with the page's own files:**

1. Part 1's seven files, the finished eight, and Lecture 9's six all lint `clean`:
   `0 error(s), 0 warning(s)`.
2. At the start the shared story holds four running leads. `ship_docked` at the Customs
   House puts one call on the ship after a few seconds, titled Customs House, with the
   two answers. The first answer opens a visit titled CUSTOMS HOUSE in the room
   `customs_counter`.
3. The stand-in console is offered the choices on the page, in that order. The back
   office offers two choices before the manifest is read and three after. Reading the
   manifest finishes `lead_customs` (credits 500 to 550) and, in the finished files,
   opens `yard_count`. The counter then speaks its second line. The empty-bracket
   answer ends the visit.
4. Docked again: the call comes again, the counter opens on its second line, and reading
   the manifest again leaves credits at 550.
5. At Tally Yard the call opens a walked visit on an area 24 by 10 with both art sets
   loaded. The stand-in from Weapons stands at 4, 3 and holds `yard_clear`; the strike
   puts the loader down and finishes it.
6. A click on the terminal walks to 14, 6 and opens its scene. A click on the door
   walks to 16, 6 and leaves it shut. A click on the keycard puts `yard_key` in the
   pack. The next click on the door opens it. The ledger, at 16, 5, speaks the "Two
   crates short" line, and closing it finishes `yard_count` (credits 550 to 700).
   Beaming up ends the visit.
7. Docked again: call again, state as left. A jump to 1, 0 and back: the site is bound
   to a new station object, state as left. The save holds the three blocks on the page.
8. A second launch on the same save: the same state, both steps Done, credits 700; a
   jump with the stand-in on the map ends the visit and brings the console home; the
   Customs House opens on its second line.
9. Step 11's tables: 42 variants linted again on the evening's tool, each one change to
   the finished files; 41 were played when the page was written, and these were played
   again that evening: the area key, no `ground` files, `Site: custom`, a missing
   `Site file:`, the text site's rooms under `scenes`, the call with no
   `boarding_down` and with a misspelled one, `## [Hails](hail)`, Stay aboard then
   docking again, and a comma missing from `story.json`. The two "no call" rows were
   played with no console seated: the script marked the ship docked, then undocked,
   by hand, and the visit ended within six seconds.
10. Lecture 11's, 12's and 16's finished files with this lecture's lines added lint
    `clean`; the file counts are in "What changes in later lectures".

**Read in the tool's or the game's code, not run:** that `sbs fetch --update-libs`
downloads and unpacks what `shared_media` lists; that the call waits four seconds;
that only a Comms console can open or answer a call; that a job word or a name after
`For:` needs a crew roster. **Read in the game's guide:** that a pack's contents and a
`Hidden until:` prop are not kept through Continue.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. Every screen: the call on Comms, the Boarding Party app, the rooms, the map.
2. How Helm docks with a station here, and how close the ship has to be. The script
   sent the docking signal. The two stations have no `Side:` line, so they are the
   crew's own.
3. Whether the two new stations sit clear of Kestrel Relay in the home system.
4. A person beaming down with the button. A test setting sent the stand-in.
5. The Fire app putting the loader down, and the loader attacking anyone.
6. Which console a crew member comes back to. In the stand-in, a console seated as
   Weapons reported itself as Helm afterward; that may be the stand-in's own doing.
7. The map with no art (black), and with art.
8. The Customs House's facts are per place: nothing shows the crew a list of them.

## Scenes

### 1. Cold open

**Screen:** A handheld in the Customs House, three choices on it. Then a handheld
showing the yard's map.

**Say:** "Your crew has spent this whole class on the bridge. ||| Today they get up, |
and they leave the ship, twice over. ||| Once into a place made of rooms and choices. ||
And once onto a map they walk across. ||| And both of them hang on one line of a
landmark. ||"

### 2. One line on a landmark

**Screen:** `kestrel_verge.amd`, the Landmarks chapter. Type Customs House. Highlight
`Site: customs`.

**Say:** "Here's a station, like the ones you've written before. || It's in the home
system, | so nobody has to fly anywhere. ||| And it has one new line. | Site, and a key.
||| That line says the crew can leave the ship here. || And the key is the name of a
file. | Customs, dot a m d. ||"

### 3. The site's file

**Screen:** New file, `customs.amd`. Type or paste. Scroll: Voices, Hails, Scenes.
Highlight `; signal boarding_down`, then `(boarding)`.

**Say:** "So I make that file, | and the whole place goes in it. ||| It has three chapters in it. || Voices says who's talking. || Hails is the call that comes when we dock. ||| Look at
this answer. || After it comes a semicolon, the word signal, and boarding down. || That's
the game's own word, | and it's what sends a party. ||| Then come the rooms, | and the first one is where they arrive. || Every room has a way back, | and every room has a way home.
||"

### 4. A fact, and a step of story

**Screen:** The Counter's two lines and the manifest answer. Then the Narrative chapter:
type Nothing to Declare. Highlight `signal manifest_read` in both files.

**Say:** "Two more things on this one answer. ||| The first is learn the manifest. || Now the party knows a fact, | and the place keeps it. || This line is only spoken before they know it,
| and this one only after. ||| And then signal, manifest read. || That word is mine. ||
Over in the universe file, I add a step of story | that's done when it hears that same
word. ||| That's how a place finishes a step. ||"

### 5. Lint, and play

**Screen:** `sbs lint MyUniverse`: seven files, each one `clean`. Then run the game: dock,
the call, the answer, BEAM DOWN, the rooms of Step 5's table.

**Say:** "Lint first, and it's clean. || There are seven files now, | and it read the
new one with the rest. ||| It knows boarding down is the game's own word. || And it
found my signal at both ends, | the answer in one file and the step in the other. |||
Now let's dock with it. || A call comes in from the Customs House. || Comms
answers, and sends a party. || And here's the counter. ||| I read the manifest, | and
the step is done and paid. || Back at the counter, | the clerk has a different line for
me now. ||"

### 6. The same idea, walked

**Screen:** The rule from Step 6, large. Then `story.json` with the two new lines,
`settings.yaml` with the last line, and `sbs fetch "MyUniverse" --update-libs`.

**Say:** "Now the second place, and here's the rule for it. || Say it with me. ||| The
landmark says site, tally yard. || The map's first line says area, tally yard. || It's
the same key, | and nothing else joins them. ||| A map needs pictures, | and they come
in two art packs. || So I add two lines to story dot json, | and I watch my commas. ||
One line at the end of the settings file. || And then I fetch them, once. ||"

### 7. The map and its file

**Screen:** New folder `ground`. Paste `starter.tileset`, then `tally_yard.tiles`.
Highlight `area: tally_yard`. Then paste `tally_yard.amd` and scroll: Props, People,
Hostiles, Scenes, Side Stories.

**Say:** "I'm handing you this map finished, | because drawing one is a class of its
own. ||| Read it as a picture. || There's a landing pad on the left, | and a walled
house with one door. ||| And there's the first line, area, tally yard. ||| Then the
site's own file. || It has the same call as before. || And then what stands on the map.
| A door, a keycard, a terminal, a ledger. || A calm man to talk to, | and a loader that
attacks. ||| Every key starts with the word yard. || Keep to that, and two places can never share a key. ||"

### 8. The landmark, the step, and lint

**Screen:** `kestrel_verge.amd`: the Tally Yard landmark, the `Then: reveal` line, the
step The Short Count. Then lint: eight files, each one `clean`.

**Say:** "One more landmark, with its one line. || One more step of story, | opened by
the first one. ||| And lint says clean, for all eight files. || It reads the map as
well. ||| Change the map's first line to some other word, | and lint tells you the
site will not exist. || The game's log says the same. ||"

### 9. Walk it

**Screen:** Run the game. Dock with Tally Yard, the call, BEAM DOWN from Weapons. The
rows of Step 12's first table: the loader, the terminal, the door refusing, the
keycard, the door open, the ledger, Keeper Kell, BEAM UP.

**Say:** "So we dock with the yard, | and the call comes. || I go down from Weapons, |
and the side story is mine. ||| First I deal with the loader. || Then I try the door, |
and it stays shut. || The keycard's lying out in the yard. || I pick it up, and now the
door opens. ||| Inside there's the ledger. || I close it, and the short count is done and paid. ||| And when the last of us beams up, | the visit is over. ||"

### 10. It remembers

**Screen:** Dock again and go down: the open door. Engage another system and come back.
Close the game, run it again. The save file, the lines under `state:`.

**Say:** "Now I dock again, and go back down. || The door's still open, | and the
loader's still down. ||| I leave the system, and I come back. || The game built that
station new, | and the yard is just as I left it. ||| Then I close the game, and
continue. | It's the same again. ||| And here it is in the save. | The door, the
keycard, the loader, | and what we learned in each place. ||"

### 11. An honest word, and your turn

**Screen:** The section about a site with no call, on the page. Then the exercise.

**Say:** "Two honest words before you go. ||| When I checked this page, a script did
all of it, | and nobody was watching a screen. ||| And always give a site a call. || A
place with no call opens the moment you dock, | and nobody asked the crew first. || If
they cast off without going down, | that visit just ends. ||| Now it's your turn. || Rename the
customs house, | and give it a fifth room. || Then walk the yard as far as the ledger.
||"
