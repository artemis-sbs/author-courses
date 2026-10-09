# C6-1 video script - From one session to twenty

> **STATE ON 2026-10-09.** Written and measured today against the released tools: `sbs`
> 0.13, the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions
> `b20726f`, the Open Universe engine library in `__lib__`). Everything was run by script
> in the game's stand-in (the mock), from copies of the mission placed where their save
> cannot reach a player's own. **Nothing in this lecture has been run in the real game,
> and nobody has seen any of its screens.** The Continue round trip is the heart of this
> lecture: it was measured in the mock for every row of the page's tables. In the real
> game a smaller round trip (a finished cargo run, credits, the system and a charted
> place) was confirmed by script for Class 5 Lecture 2.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Class 5 leaves it. The page was measured on Lecture 5's file; a later one works the same |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | `MyUniverse` open, `kestrel_verge.amd` in a tab, font size raised |
| Game | Closed. Started on camera in scenes 3 and 7 with `sbs run server,helm,comms -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-09, with the page's own files:**

1. The finished files lint `clean` and play with no errors and an empty
   `mast.runtime.log`. `campaign.md` in the folder changes nothing: lint counts
   `1 amd + 1 mast file(s)`, the game runs the same, and the bible edition does not
   contain it.
2. At the start the Quest Log is handed four Class 5 leads and The Long Count: One of
   Five, all Active.
3. After the levy: credits 400, standing with Hollin 20, and Escort offered at 300.
4. Engaging One of Five puts the ship at (2, 2), charts The Wren, and marks the lead
   Done.
5. A second launch with the same save: the same system, credits, standing, story steps
   (done, open and hidden), jobs in hand, and Charted Locations.
6. The three guards of a landmark, not destroyed, were there again after Continue.
7. A step whose clock ran out (not followed by a jump) was Active again after Continue.
8. With the ship renamed in `settings.yaml`: credits, story and charts came back;
   standing was 0, no jobs, and the save then held only the new name.
9. With the title changed: a new game, a second save file, the first one untouched.
10. Between two launches the universe file was changed: a rewritten lead showed its new
    title and text; a deleted lead was still there; an added lead appeared.
11. Lint on the mistakes in Step 5: 2 variants, each linted and played.

**Read in the docs and code, not run:** the five decisions quoted from Storm's Beacon's
design notes were checked against its files (six episodes in its dispatcher list, three
tentpoles named, a 45 second pursuit fuse). Storm's Beacon itself was never started.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. Every screen: the Quest Log, the arrival card, the Comms buttons.
2. That closing the game's windows and typing the same line continues the save in the
   real game, for standing and story steps. (Class 5 Lecture 2's engine check saw it for
   a cargo run, credits, the system and a charted place.)
3. What VS Code asks when a new file is made.

## Scenes

### 1. Cold open

**Screen:** `campaign.md` beside the Quest Log with The Long Count: One of Five.

**Say:** "Your universe works, and a crew can sit down and play it for an evening. || This
class is about the evening after that, | and the eighteen after that. ||| Today you'll
give your crew a question that takes twenty evenings to answer. || And you'll find out,
by measuring it, | exactly what the game remembers from one week to the next. ||"

### 2. A campaign that shipped

**Screen:** The table in Step 1 of the page, one row at a time.

**Say:** "The people who make the game built a campaign on the same machinery you're
using. || It's called Storm's Beacon, | and they wrote down what they decided as they
went. ||| First, every episode goes round one loop. | Someone names a place, the crew
goes, finds one thing out, | gets interrupted, and reports back. || Second, only three
evenings are written by hand. | The rest come from one pattern. || Third, they built the
pattern before they wrote the episodes. ||| And they were honest about the hard part. ||
It isn't the machinery. | It's having enough for the crew to do. ||"

### 3. One evening's worth

**Screen:** Run the game. Helm's Quest Log, with the four Class 5 leads.

**Say:** "So let's look at what you have, the way a crew sees it on the first night. ||
There are four leads, and all four are open. ||| For one evening, that's generous. | For a
campaign, it's the whole map in the first minute. || Three things change when the same
people come back. ||| You show them one lead at a time. || A win belongs to the very last
evening. || And only what the game keeps is still true next week. ||"

### 4. The premise

**Screen:** VS Code. New file `campaign.md`. Type the premise, the pressure, the loop.

**Say:** "The plan for a campaign isn't for the game, | and it isn't for the crew. It's
for you. || So it goes in a plain page beside the universe file. ||| A premise: one
question. | Five boats and forty-one people are missing. || A pressure that's true every
single week. | Somebody else is stripping those boats. || And the loop, in five lines. |||
Lint doesn't read this page, | and neither does the game. || I tried, with a page made
to look exactly like a record. ||"

### 5. The first lead

**Screen:** `kestrel_verge.amd`. Add The Wren under the last landmark, then One of Five
under the last narrative record.

**Say:** "Now the part the game does read. || One landmark, a lifeboat called the Wren. |
And one lead that sends the crew to her. ||| You know every line of these from the last
class. || Two habits are new. || The title starts with the campaign's name, | because in
week six the Quest Log is a long list. || And the key starts with the evening's number, |
because you're going to write sixty of them. ||"

### 6. Lint

**Screen:** Save. `sbs lint MyUniverse`. `clean`. Point at the count of files.

**Say:** "I save, and I run lint, | and it says clean. ||| Now look at the count: one universe file, one
story file. || The campaign page isn't counted, | which is exactly what we want. ||"

### 7. Play, stop, come back

**Screen:** Run the game. Comms: hail, pay the levy, take the Escort. Helm: Engage One
of Five, then Engage Kestrel Relay. Fill the middle column. Close every window. Run the
same line. Fill the right column.

**Say:** "This next part is the measurement the whole class stands on. || I pay the
levy, | I take a job, | I follow the lead out to the Wren, and I come home. ||| Then I
write down six things. | Where the ship is. The credits. The standing. || The lead, the
job, | and the charted places. ||| Now I close the game. All of it. || And I type the
same line again. ||| It's the same system, | the same credits, and the same standing. || The lead is still
done, | the job is still mine, | and the Wren is still on the chart. ||"

### 8. What the game keeps

**Screen:** The first table under "What the game keeps, and what it does not".

**Say:** "So that's a campaign's memory. || Where the ship is, | what the side has in
the bank, | and what every side thinks of this ship. ||| Every step of the story, | done,
open, or still hidden. || The jobs in hand, | and every place they've charted. ||| That's
enough to build twenty evenings on. ||"

### 9. What it does not

**Screen:** The second table, one row at a time.

**Say:** "And here's what it doesn't keep. | Read this list twice. ||| Guards the crew
ran away from are back. || A countdown starts again. ||| A ship with a new name has no
standing and no jobs, | and the old name's record is gone for good. || A universe with a
new title is a new game. ||| And the big one. || The game has no memory for a fact of
your story | unless that fact is a step, a standing, or credits. || So in this class,
every turn of the plot is a step. ||"

### 10. Close

**Screen:** `campaign.md` with the table filled in.

**Say:** "So you have a premise, a first lead, | and a table you measured yourself. |||
End every evening the same way: | jump home, then close the game. || Next time, we build
a whole evening round that one lead. ||"
