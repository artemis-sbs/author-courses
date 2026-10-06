# C2-1 video script - Sides and factions

> **CHECKED IN THE REAL ENGINE, 2026-10-04, real Helm, Science and Comms.** The probe's
> report matched the mock: three sides, the six relations, the yard's stock scan and its
> Hail, Build Weapons and Request Priority Docking buttons, docking offered at the yard,
> the cutter's enemy scan and Hail / Taunt / Surrender now, nothing moved or fired in 30
> seconds; `mast.runtime.log` empty. SEEN: on Science the hostile cutter is drawn RED and
> its panel reads "Breaker Cutter (breaker)", with side chips `tsn`, `breaker`, `guild`;
> on Helm the allied yard is BLUE like DS 1 and the crew's ship green. So the map colors a
> contact by its RELATION to you, not by the side's `Color:`. The engine's stock scan text
> for the cutter reads "The captain cannot be taunted pirate." Not seen: the side's color
> anywhere but the side word, docking carried through, a bad `Color:`.
>
> **Changed since this script was written:** lint names a side key that names nothing
> (`dangling-side`, sbs_utils `488df12c`) and the game writes `Side not found` to
> `mast.runtime.log`. The local `amd` template now has the line that reads a Sides section
> (starter repo `60c30bc`, NOT pushed): when it is, Step 3's card retires.

Target length: 19 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | The Lecture 11 mission: the arc **Salvage Run**, the lifeboat, the tug card at the end of `story.mast`. One side, `tsn`. Lint clean, compile prints nothing |
| Library | sbs_utils v1.4.0 at `98725836` or later and LegendaryMissions at `e61b415` or later, as released. Every run behind this script used the packaged library in `data\missions\__lib__` |
| Template | The mission comes from the local `amd` template (`mast_starter\templates\amd`). That template has NO line that reads a Sides section, which is why scene 4 pastes one. If the template gains the line, cut scene 4 and the page's Step 3, and keep the lint warning in scene 3 only as "what you would see on an older mission" |
| VS Code | `MyMission` folder open, `mission.amd` in one tab scrolled to the end, `story.mast` in another at line 18 |
| Game | Closed. Started on camera in scene 10 with a server, a Helm, a Science and a Comms console |

## Confirm on camera

Nothing in this lesson has been seen on a real screen, and nothing has been run in the
real engine. Everything below was measured on 2026-10-04 in headless runs (the mock) on the
packaged library, by a probe that calls the game's own functions and prints what they
return.

What the runs showed, on the finished example:

- Three sides exist with the names, keys and colors in the file. TSN and the Breakers are
  hostile, TSN and the Guild are allied, the Breakers and the Guild are hostile. One
  `Enemies:` line sets the relation both ways.
- The two functions that build the Science console's title return, for the cutter, the
  name `Breaker Cutter` in color `#FF6B6B` and the word `breaker` in `#F80`. For the yard:
  `Guild Yard` in `springgreen` and `guild` in `#0C6`. For DS 1 and the hulk: `springgreen`
  and `tsn` in `#07F`. For a contact with no scan text: the word `unknown` in grey, and no
  side word.
- A forced scan of the cutter stores "Enemy vessel. Exercise caution." on the `scan` tab,
  "Ready for combat." on `status`, "The captain cannot be taunted ." on `intel` and
  "A bunch of  creatures." on `bio`. A forced scan of the yard stores "This is a friendly
  station."
- Comms selecting the cutter is sent the buttons Hail, Taunt, Surrender now. Hail is
  answered "Go away, Artemis! You talk too much!". Surrender now is answered "Go climb a
  tree, Artemis!" and changes nothing. Comms selecting the yard is sent Hail, Build
  Weapons, Request Priority Docking. Hail is answered "Hello, Artemis. We stand ready to
  assist", the shield and hull figures, "You have full docking privileges" and a table of
  torpedoes.
- Inside 600 of the yard the ship is offered the yard to dock with, and a dock request is
  accepted. Beside the cutter no dock is offered. With the cutter 500 from the ship, a dock
  request at DS 1 is refused; with it 2000 away the request is accepted.
- 25 and 30 seconds with the ship 400 from the cutter: the cutter's position does not
  change, no shield value changes, and no ship has a weapon target.
- The whole story: hulk, lifeboat, tug (300 credits with the bonus), then the yard: Bring
  the Log Home stays running. Then DS 1: the game ends with the `Win:` sentence.
- The page's steps were applied one at a time to the Lecture 11 example, with `sbs lint`
  and `sbs compile` after each. The two lint lines the page quotes are the ones that came
  back.
- Every row of the three mistake tables was produced by making that one change, running
  `sbs lint` and `sbs compile` on a folder holding only the student's two files, then
  running the game headless on the same files. The exercise was run step by step the same
  way.

Not seen by anyone. If one of these is not as described, stop and fix the page:

1. **The map.** What color each thing is drawn in on Helm, Science and Comms: the side's
   own color, or a color for "enemy" and "friend". The page says the color is used for the
   side's ships on the map. Only the library's own note says so. This mission never sets
   the colors the game uses for hostile and neutral, so those are the game's defaults.
2. **The Science title.** The name in red or green and the side's key beside it. The key
   has a narrow column: check that `breaker` fits.
3. **The side word in the engine's own lists.** The engine fills a ship's "side" for its
   own readouts from the hull, not from the mission: a pirate hull may read `Pirate` and a
   civilian station `USFP`. If a console shows that word, the page needs a line about it.
4. **Whether anything shoots or moves.** The page says the cutter does neither. In the mock
   a ship fires only at a target a script gave it. If the cutter, DS 1 or the yard opens
   fire in the real game, Step 7 and Step 9 are wrong.
5. **Docking at the Guild Yard** with Helm's own control, start to finish.
6. **The refusal** when an enemy is close: the words the crew is shown.
7. **Scanning.** Whether the ship's sensors read the cutter and the yard by themselves in
   range, and what Science shows while it tries to scan a contact that has no text (the
   exercise's stranger).
8. **A color that is not one** (`burnt orange`, `#F8`). The words go to the engine as
   typed. Nobody knows what it draws, or whether it objects.
9. **The crew's own color.** The template sets `tsn` to `#07F` at the top of `story.mast`,
   before the game makes its world. In the mock that color never reaches the game's table;
   it does once the TSN record is in the Sides section. If the crew's ship is the wrong
   color in a Class 1 mission and right after this lecture, that is why.

Known, and kept out of the lesson on purpose:

- An allied SHIP gets no ready-made scan text. Only a station does, or a ship that also
  wears the role `friendly`. So an allied ship is `unknown` until the writer gives it a
  scan record, which is why the lesson's friend is a station and the exercise adds a scan
  record. `friendly` is not taught.
- `players` and `civilians` in a relation line. They work (`Enemies: players` was run),
  and a mission with one player side does not need them.
- `Done when: reach breaker 2000` works in the game: a side's key is also a role. Lint
  calls it a role nothing wears, so the page does not teach it.
- A writer's own `scan`, `intel` or `bio` text for an enemy ship, and `scan` text for a
  friendly station, is not shown: the game's ready-made reading replaces it. A `mat` record
  for the cutter IS shown, because the game has no reading for that tab. The page says so
  under Step 9, in one row of Step 8 and in one exercise step.

## Scenes

### 1. Cold open (0:00 - 0:50)

**Screen:** The Science console. Select the Breaker Cutter: its name in red, `breaker`
beside it, "Enemy vessel. Exercise caution." Select the Guild Yard: green, `guild`,
"This is a friendly station." Cut to Helm docking at the yard.

**Say:** "Last class, everything on your map was on one side. Yours. Today the map gets
politics. These people want your hulk. These people will fix your ship. That is two
records in your file, and one line that says who is whose enemy."

### 2. The side you already have (0:50 - 2:30)

**Screen:** `story.mast`, lines 18 to 20 highlighted. Then line 59, line 63, and the tug
card at the end: highlight the first word inside the quote marks each time.

**Say:** "You read these three lines in Lecture 11. They make a side called tsn, and give
it a name and a color. Look where else that word turns up. DS 1: tsn, station. The hulk:
tsn, derelict. Your tug: tsn, tug. Inside the quote marks, the first word is the side. The
rest are roles. The crew's own ship is on tsn too. So tsn is the key of your own side.
Hold on to that word."

### 3. A Sides section (2:30 - 5:15)

**Screen:** `mission.amd`, the end of the file. Two blank lines. Type the note, the
section line, the TSN record. Point at the key. Then show the color table on the page.
Terminal: `sbs lint MyMission`, with the warning.

**Say:** "Sides are records, like everything else. A section: two hashes, Sides, and the
key is sides, exactly. One record for a side: three hashes, a name, a key. My own side
goes first, and its key is tsn, because that is the word my ship already carries. A color:
hash, then three characters, for red, green and blue. Zero is none, F is all. And a line
about who they are. Lint. Nothing in this mission reads a section keyed sides. And lint is
right: the script has a line for quests, a line for scans, a line for landmarks. Nothing
for sides. Yet."

### 4. The card (5:15 - 7:15)

**Screen:** `story.mast`, line 35. Cursor to the end of the line. Enter twice. Type the
comment and the `sides_declare_amd` line, four spaces in. Scroll down to line 52 to show
the landmarks line beside it. Terminal: lint, clean. Compile, nothing.

**Say:** "One card today, and there is nothing on it to change. Line 35 reads my file. I
go to the end of that line, press Enter twice, and type two lines, lined up with it. A
note. And the line: make the sides, from the section called sides. It is the same shape as
the landmarks line further down. Where it goes matters. Below line 35, because line 35 is
what reads the file. And four spaces in, above the arrow END, so it is one of the map's
lines. Both checks. Clean, and nothing."

### 5. Two more sides (7:15 - 9:15)

**Screen:** `mission.amd`, below the TSN record. Type The Breakers, then Harbor Guild.
Highlight `Enemies: tsn`, then `Allies: tsn`.

**Say:** "Now the people who are not me. The Breakers. Key, breaker. Orange. And the line
that matters: Enemies, tsn. The Harbor Guild. Key, guild. Green. Allies, tsn. After the
colon comes a key, never a name. And I say it once. Enemies tsn on the Breakers makes them
my enemy and makes me theirs. I do not go back and write it on my own record."

### 6. Something on each side (9:15 - 11:15)

**Screen:** Scroll up to the Landmarks section. Below The Lifeboat, above the Sides note,
type the Breaker Cutter and the Guild Yard. Highlight the two `Side:` lines. Lint, clean.

**Say:** "A side with nothing on it is a name in a file. So, two landmarks. A ship: kind
npc, side breaker. Out past the hulk. A station: side guild. West of DS 1. The Side line
takes the key. Watch where I am typing. These go in the Landmarks section, above the Sides
heading. Type a landmark below that heading and the game reads it as a side called Breaker
Cutter, and puts no ship anywhere."

### 7. A second station (11:15 - 13:00)

**Screen:** The step Bring the Log Home, `Done when: reach station 1000` highlighted.
Change it to `reach home 1000`. Lint: the warning. `story.mast`, line 62: add `, home`
inside the quote marks. Lint, clean. Compile, nothing.

**Say:** "Lecture 10 warned you about this one. My story ends with: reach station. Station
is a role, and every station wears it. I have just built a second station. The crew could
carry the log to the Guild and win. So DS 1 gets a role of its own. In the step: reach
home. Lint says nothing wears a role called home. True. So, line 62, where DS 1 is made.
Inside the quote marks, after station: comma, space, home. Side first, then roles. Clean."

### 8. Who is what to whom (13:00 - 14:45)

**Screen:** The three-pair table on the page. Then change the Breakers' line to
`Enemies: tsn, guild`. Then the table "What a relation does in the game".

**Say:** "Three sides, three pairs. Me and the Breakers: enemies. Me and the Guild: allies.
The Breakers and the Guild: nobody said. And a pair nobody mentions is nothing to each
other. The game does not guess. Scavengers and harbor pilots are not strangers, so:
Enemies, tsn, comma, guild. What does a relation buy you? An enemy reads as an enemy on
Science, and Comms can taunt it. A friendly station lets you dock. And one thing it does
not buy you: a fight. The cutter has no orders. It will sit there."

### 9. Lint, and what lint cannot see (14:45 - 16:45)

**Screen:** Terminal. Type `Enemy: tsn` in the Breakers: lint, unknown field. Undo. Move
the cutter below the Sides line: lint, `Kind` is not a known side field. Undo. Then
`Enemies: tsm`: lint, clean. Then `Side: braker` on the cutter: lint, clean. Undo both.
Show the second table on the page.

**Say:** "Lint. A field I misspelled: caught. A landmark in the wrong section: caught. Now
watch. Enemies, t s m. Clean. Side, braker. Clean. Lint does not check that a key after
Enemies, or after Side, is a side that exists. In the game those two mistakes look the
same: the cutter reads unknown, forever, and Comms has nothing to say to it. So for this
lecture, clean is not enough. Read the three key words by eye: the one in the heading, the
one after Side, the one after Enemies."

### 10. Play it (16:45 - 19:20)

**Screen:** Server, Helm, Science and Comms. Science: select the Guild Yard, wait for the
scan. Comms: select it, press Hail. Helm: fly inside 600 and dock. Undock. Fly past the
hulk. Science: select the Breaker Cutter. Comms: select it, press Hail. Hold near the
cutter for ten seconds. Then cut to the end of the story: Bring the Log Home showing, the
ship at the Guild Yard, nothing; the ship at DS 1, the win.

**Say:** "The yard. Unknown, until the scan is done. Green. Guild. A friendly station.
Comms: hail them. Full docking privileges. And Helm can dock. Now the other one. Red.
Breaker. Enemy vessel, exercise caution. Hail. Go away. And it sits there: enemies, and
no fight. Last thing. The log, to the yard. Nothing. To DS 1. Home."

### 11. Your turn (19:20 - 19:50)

**Screen:** The exercise on the companion page.

**Say:** "Write a faction of your own, with one ship. Say nothing about it, and Science
calls it unknown. Give it a scan record, and it has a name. Make it an enemy, then a
friend, and watch the name change color. Next time: the people who fly these ships."
