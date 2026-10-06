# Class 1, Lecture 10 - Things quests point at

## What you will have at the end

Two things in the game that you wrote, and a story that points at both.

Science scans the hulk and reads your words, on a tab you added. A lifeboat of your own
drifts on the map with its own scan text. And the story now runs from the hulk to the
lifeboat and then home.

*[Screenshot to add: the Science console with the hulk selected and your new tab open.]*

You will edit one file, `mission.amd`. Nothing in `story.mast` changes.

## The video

*[Link to add when recorded.]*

## Before you start

- Your mission as Lecture 9 left it: both files, with the arc **Salvage Run** in
  `mission.amd`. It is the same mission you have had since Lecture 3.
- `sbs lint MyMission` says `clean`.
- VS Code with the mission folder open, a command prompt open in `data\missions`, and the
  game closed.

This page leans on three earlier ones, and does not explain them again.

| Lecture | What you learned there |
|---|---|
| 5 | The shape of a scan record: `Scan of:`, `Tab:`, and a `%` in front of each reading |
| 6 | How to read a finding from lint, and to fix the first one first |
| 7 | What a role is, and what lint says when a line names a role that nothing wears |

Line numbers on this page are for a `mission.amd` that matches Lecture 9's finished file
line for line. If you did an exercise in Lecture 5, 7, 8 or 9, yours are higher. Go by the
words.

Two words for this lecture:

| Word | Meaning |
|---|---|
| Tab | One page of what Science learns about an object. There are five: `scan`, `status`, `intel`, `mat`, `bio` |
| Landmark | A thing on the map that you place by writing a record |

One idea runs through the whole lecture. A quest never names an object. It names a role,
and the game finds whatever wears that role. Scan text works the same way. In Lecture 7
the hulk got its roles from a list in `story.mast`. Today you place a thing yourself, and
give it its role in `mission.amd`. So: give a thing a role, then point at the role.

## Step 1 - Read the scans you already have

Open `mission.amd`. Find this line:

```
## [Scans](scans)
```

You know this section. In Lecture 5 you wrote a record in it, and in Lecture 7 you hung
that record on a role of your own. Three records are under the line now:

| Record | Its `Scan of:` line | Its `Tab:` line |
|---|---|---|
| Derelict Hull | `derelict` | `scan` |
| Derelict Materials | `derelict` | `mat` |
| Derelict Intel | `ghost_ship` | `intel` |

The hulk wears both roles, so it has text on three tabs.

Here is the first record again:

```
### [Derelict Hull](derelict_scan)
---
Scan of: derelict
Tab: scan
---
% The hull is cold. Whatever happened here happened a long time ago.
% Hull plating is intact but every port is dark. No power anywhere aboard.
```

| Part | Meaning |
|---|---|
| `Scan of: derelict` | Whose text this is: every object that wears the role `derelict` |
| `Tab: scan` | Which of the five tabs it goes on |
| Each line that starts with `%` | One reading |

With one `%` line, that line is the reading. With more than one, the game picks one of
them when the scan finishes.

## Step 2 - Add a tab of your own

Give the hulk a fourth tab: `bio`.

Go to the end of the file. The last record is your **Derelict Intel**, and its reading is
the last line. If you did the exercise of Lecture 5 or of Lecture 7, a record of your own
comes after it: go below that one. Leave one blank line, then type:

```
### [Derelict Life Signs](derelict_bio)
---
Scan of: derelict
Tab: bio
---
% No life signs. Six suits hang in the airlock, and all six are empty.
% No life signs. The air aboard went bad a long time ago.
% One faint reading aft. It is a plant in a pot, and it is doing fine.
```

Three readings this time. Save with `Ctrl+S`, and run lint: `clean`.

Five rules for scan text. Lint checks the first four. Nothing checks the fifth.

1. **One reading, one line.** Do not press Enter inside a reading. A reading split over
   two lines becomes two readings, and the crew may get half a sentence.
2. **One role, spelled the way the object wears it.** `derelict`, not `derelicts`, and
   never two roles with a comma.
3. **One record for each role and tab.** A second record with the same role and the same
   tab replaces the first.
4. **Always write the `Tab:` line.** Without it the text goes on the `scan` tab, and
   replaces what was there.
5. **No curly brackets.** A `{word}` in a reading is a fill-in mark, and filling it in
   needs a line of script you have not met yet. Until then the crew is shown the brackets
   and the word, exactly as typed.

## Step 3 - Put a lifeboat on the map

So far everything on the map came from `story.mast`: the station and the hulk. Now you
place something yourself.

Go to the very end of `mission.amd`. Leave two blank lines, then type:

```
// ---- Places. Each record is one thing on the map. `Roles:` is the label quests and
// scans point at, `Art:` is what it looks like, and `Loc:` is where it sits.
## [Landmarks](landmarks)

### [The Lifeboat](lifeboat)
---
Kind: wreck
Roles: lifeboat
Art: wreck
Loc: 6000, 0, 6000
---
The hulk's lifeboat. It left her with the flight log aboard.
```

The section line needs care. Two hashes, and the key in the round brackets is
`landmarks`. The game looks for that key. The name in the square brackets is yours to
change.

| Line | Meaning |
|---|---|
| `### [The Lifeboat](lifeboat)` | Three hashes, the object's name in the game, then its key |
| `Kind: wreck` | What sort of thing it is |
| `Roles: lifeboat` | The label it wears. Quests and scans point at this word |
| `Art: wreck` | What it looks like |
| `Loc: 6000, 0, 6000` | Where it sits |
| The last line | A note for you |

### Roles

**This is the line that matters.** Since Lecture 7, lint's sentence about a role has
ended "Check the spelling against the `Roles:` line of the thing you mean, or the roles in
`story.mast`". This is that `Roles:` line. It does for a landmark what the list on line 68
of `story.mast` does for the hulk.

Two differences from that list:

- **Roles only.** The first word of the list in `story.mast` is the side. A `Roles:` line
  has no side in it. A side gets a line of its own, further down.
- **For more than one role, put a comma between them:** `Roles: lifeboat, wreckage`.

Now keep your word list true. At the top of the file, under the `ghost_ship` line of the
list you wrote in Lecture 7, add one line:

```
// ROLE    lifeboat          worn by The Lifeboat, a landmark in this file
```

### Kind

| You write | You get |
|---|---|
| `Kind: wreck` | Wreckage. Scenery, not a ship |
| `Kind: ship` | A ship. Missions that ship with the game also write `Kind: npc`, which means the same |
| `Kind: station` | A base |

Write `Kind:` with its colon, every time. Lint warns when the line is missing. It does
not check the word after it: a word the game does not know gets you a ship.

### Art

`Art:` is a word from the game's own list of ships. Lint cannot check it, so copy it
exactly. These three are in the list:

| You write | It looks like | Goes with |
|---|---|---|
| `Art: wreck` | Wreckage | `Kind: wreck` |
| `Art: cargo_ship` | A freighter | `Kind: ship` |
| `Art: starbase_civil` | A civilian station | `Kind: station` |

A record with no `Art:` line is not placed at all.

### Loc

Three numbers with commas between them.

| Thing | Its three numbers |
|---|---|
| DS 1 | `0, 0, 0` |
| The hulk | `0, 0, 9000` |
| Your lifeboat | `6000, 0, 6000` |

The middle number is height. Leave it at `0`. The first and the third say where on the
map. Your lifeboat is about 8500 from DS 1 and about 6700 from the hulk.

Write all three numbers, and write each one plain: `6000`, not `6,000`. With fewer than
three numbers, or with no `Loc:` line, the lifeboat is put at `0, 0, 0`, which is inside
DS 1.

### A side, for ships and stations

A wreck needs no side. Give a ship or a station the side it is on, with one more line.
This mission has one side, `tsn`:

```
Side: tsn
```

Lint does not check the side word.

Two things to know before you place a station. Both were measured on this mission.

- **A station's art brings the role `station` with it.** Your story has a step that says
  `reach station 1000`, and it finishes at anything that wears that role. A second
  station in this mission is a second place to win.
- **A station on the crew's own side shows the game's stock text** on `scan`, `status`,
  `intel` and `bio`, as DS 1 does. A scan record of yours for its role shows on `mat`
  only. You met this in Lecture 7's exercise. A ship on the crew's side, a wreck, and a
  station with no side all show your records.

Save. Run lint: `clean`.

## Step 4 - Give the lifeboat scan text

The lifeboat wears the role `lifeboat`. That is all a scan record needs.

Go back up to the Scans section. Leave one blank line below your Derelict Life Signs
record. Then, above the `// ---- Places` note, type:

```
### [Lifeboat Hull](lifeboat_scan)
---
Scan of: lifeboat
Tab: scan
---
% A lifeboat, cold and tumbling. The hatch was opened from the inside.

### [Lifeboat Intel](lifeboat_intel)
---
Scan of: lifeboat
Tab: intel
---
% The flight log is aboard, sealed in the pilot's locker.
```

Give every role a `scan` tab before you give it any other. `scan` is the first look: it
is the tab the ship's own sensors ask for.

Save. Run lint: `clean`.

## Step 5 - Point the story at it

The story goes hulk, then home. Put the lifeboat in the middle.

First the new step. Find **Close Inspection** in the Quests section. Type this directly
below its description line, above **Bring the Log Home**:

```
#### [Find the Lifeboat](boat)
---
Scope: shared
Starts when: revealed
Objective: Get within 500 of the hulk's lifeboat
Done when: reach lifeboat 500
Reward: 100 credits
Then: reveal salvage/home
Part of: salvage
Required: true
---
Her log is not aboard, and one lifeboat cradle is empty. Find the boat.
```

Leave one blank line after it. Save, and ask lint before you go on:

```
sbs lint MyMission
```

```
== mission.amd ==
  [WARNING] line 75: `Find the Lifeboat` waits to be revealed, and nothing reveals it: no `Then: reveal salvage/boat` on another step, and no answer or story line names `boat`. It never appears, and the story it belongs to cannot finish (never-revealed)

1 amd + 1 mast file(s): 0 error(s), 1 warning(s)
```

You met this warning in Lecture 9, Step 3. The new step waits to be revealed, and nothing
reveals it yet. Lint's sentence spells out the line that is missing.

So change one line in **Close Inspection**. It reveals the new step now, and not the old
one:

```
Then: reveal salvage/boat
```

Save. Run lint: `clean`.

The chain is now: Close Inspection, then Find the Lifeboat, then Bring the Log Home.

Look at the new step's `Done when:` line. It has the three parts you met in Lecture 8.

| Part | Here | Meaning |
|---|---|---|
| A verb | `reach` | A player ship has to get close |
| A role | `lifeboat` | Close to anything that wears this role |
| A number | `500` | How close. Leave it off and the game uses 5000 |

**The middle word is the role.** It is the word on your `Roles:` line. It is not the key
in the heading, and it is not the name.

In this lesson the key and the role are the same word, `lifeboat`. Lecture 7 said not to
give a role the same word as a key, and for a quest or a scan record that still holds. A
landmark is the one place this course does it, for two reasons. Lines you will meet later
point at a landmark by its key, so one word for both means you cannot pick the wrong one.
And when the `Roles:` line is missing, lint can then tell you exactly what happened. Step
6 shows you.

## Your finished pieces

At the top of the file, in your word list:

```
// ROLE    lifeboat          worn by The Lifeboat, a landmark in this file
```

In the Quests section, inside Salvage Run:

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

#### [Find the Lifeboat](boat)
---
Scope: shared
Starts when: revealed
Objective: Get within 500 of the hulk's lifeboat
Done when: reach lifeboat 500
Reward: 100 credits
Then: reveal salvage/home
Part of: salvage
Required: true
---
Her log is not aboard, and one lifeboat cradle is empty. Find the boat.
```

At the end of the Scans section:

```
### [Derelict Life Signs](derelict_bio)
---
Scan of: derelict
Tab: bio
---
% No life signs. Six suits hang in the airlock, and all six are empty.
% No life signs. The air aboard went bad a long time ago.
% One faint reading aft. It is a plant in a pot, and it is doing fine.

### [Lifeboat Hull](lifeboat_scan)
---
Scan of: lifeboat
Tab: scan
---
% A lifeboat, cold and tumbling. The hatch was opened from the inside.

### [Lifeboat Intel](lifeboat_intel)
---
Scan of: lifeboat
Tab: intel
---
% The flight log is aboard, sealed in the pilot's locker.
```

At the end of the file:

```
## [Landmarks](landmarks)

### [The Lifeboat](lifeboat)
---
Kind: wreck
Roles: lifeboat
Art: wreck
Loc: 6000, 0, 6000
---
The hulk's lifeboat. It left her with the flight log aboard.
```

Both whole files are in `example\`. `story.mast` there is Lecture 9's, unchanged.

## Step 6 - Check it

```
sbs lint MyMission
```

```
== mission.amd ==
  clean

1 amd + 1 mast file(s): 0 error(s), 0 warning(s)
```

### One finding to see before you need it

This is the mistake the whole lecture is about. Make it once, on purpose.

Delete the `Roles: lifeboat` line from The Lifeboat's fence. Save. Run lint.

```
== mission.amd ==
  [WARNING] line 77: `lifeboat` is the KEY of the landmark `The Lifeboat`, and `reach` looks for a ROLE. Nothing wears a role called `lifeboat`, so this matches nothing. Add `Roles: lifeboat` to that landmark's fence (role-is-a-key)
  [WARNING] line 146: `lifeboat` is the KEY of the landmark `The Lifeboat`, and `Scan of:` looks for a ROLE. Nothing wears a role called `lifeboat`, so this matches nothing. Add `Roles: lifeboat` to that landmark's fence (role-is-a-key)
  [WARNING] line 153: `lifeboat` is the KEY of the landmark `The Lifeboat`, and `Scan of:` looks for a ROLE. Nothing wears a role called `lifeboat`, so this matches nothing. Add `Roles: lifeboat` to that landmark's fence (role-is-a-key)

1 amd + 1 mast file(s): 0 error(s), 3 warning(s)
```

Three lines of your file point at the role: the step, and the two scan records. Lint
names all three. None of them is where the mistake is. As in Lecture 7, lint names the
line that makes the promise, and its last sentence says where to keep it.

If you played this, the lifeboat would be on the map with no text on any tab, and Find the
Lifeboat would never finish.

Put the line back. Save. Run lint: `clean`.

### What lint says about the rest

Every row below was tried on this mission, one at a time. Lint was run. Then the game was
run without a screen, by a script that put the ship beside the hulk, then beside the
lifeboat, then beside DS 1, and had first the ship's own sensors and then Science scan
what was there. The last column is the code at the end of lint's line.

A misspelled field, a missing colon, a broken fence, a curly quote: you met these in
Lectures 5 and 6, and lint says the same about them here.

**Scan records.** The mistake is in your Derelict Life Signs record, unless the row names
another.

| Mistake | What the game does | Lint says |
|---|---|---|
| `Tab: life`, or a tab misspelled: `Tab: boi` | The hulk has no `bio` tab. Your readings are shown nowhere | `unknown-scan-tab`. Its sentence lists the five |
| `Tab: bio, mat` (two tabs in one record) | The same | `unknown-scan-tab`. One record, one tab |
| `Scan of: derelect`, or `derelicts` | The same | `role-nothing-wears` |
| `Scan of: lifeboat, derelict` (two roles) | The same. Neither the hulk nor the lifeboat gets the readings | `scan-of-many`. One record, one role |
| No `Tab:` line | Your three readings take over the hulk's `scan` tab. The two that were there are gone, and there is no `bio` tab | `duplicate-scan`. Its sentence says a record with no `Tab:` line is the `scan` tab |
| A second record with `Scan of: derelict` and `Tab: bio` | Only the lower record's readings are shown | `duplicate-scan`. Its sentence gives the line of the first |
| Both lifeboat records say `Tab: scan` | The lifeboat's `scan` tab shows the line about the flight log. It has no `intel` tab | `duplicate-scan` |
| A reading split over two lines | Four readings, not three. The crew may be shown `and it is doing fine.` and nothing else | `reading-wrapped` |
| A reading typed above the closing `---` | That line is not read. The other readings are shown | `fence-syntax`, an error |
| Four hashes on the bio record | The hulk has no `bio` tab | `scan-record-level` |
| Two hashes on the bio record | The hulk has no `bio` tab, and the lifeboat has no text at all: the two records below went with it | `section-not-loaded`, and `scan-record-level` twice |
| The lifeboat's two scan records typed at the end of the file, below The Lifeboat | The lifeboat has no text on any tab | Ten findings. For each record, `landmark-no-art`, `landmark-no-loc` and `landmark-no-kind`, and `unknown-field` twice. The `unknown-field` sentence is the true one: the record "is being read as a landmark because of where it sits". Move both records up, above the `// ---- Places` note |
| Step 4 done before Step 3: the lifeboat's scan records, and no lifeboat yet | Nothing to see: nothing wears the role | `role-nothing-wears`, twice |

**Landmarks.** The mistake is in The Lifeboat's record, or on the section line above it.

| Mistake | What the game does | Lint says |
|---|---|---|
| `## [Places](places)`, or `## [Landmark](landmark)` | Nothing is placed. Find the Lifeboat appears and can never be finished, so the story cannot be won | `section-not-loaded`. Its sentence lists the keys the story asks for |
| The section line left out, or typed with three hashes | The same | `unknown-field`, three times. Each says the record "is being read as a scan because of where it sits" |
| Two hashes on The Lifeboat | The same | `section-not-loaded`. Its sentence says to give the heading 3 hashes |
| Four hashes on The Lifeboat | The lifeboat is placed all the same, and the story plays. `mast.runtime.log` gets one line | `heading-level-jump`, an error |
| A second landmark typed with four hashes | The second one is not placed | `landmark-record-level` |
| Two landmarks with the same key | Only the first is placed | `duplicate-key` |
| No `Art:` line, or `Arts:` | The lifeboat is not placed, and Find the Lifeboat can never be finished | `landmark-no-art`. With `Arts:`, `unknown-field` as well: it guesses `Art` |
| No `Loc:` line, or `Location:`, or `At:` | The lifeboat is put at `0, 0, 0`, inside DS 1. After the hulk the crew flies home, both steps finish there, and the game is won without the trip | `landmark-no-loc`. With `Location:`, `unknown-field` as well |
| `Loc:` with two numbers, in words, or in round brackets | The lifeboat is put at `0, 0, 0` | `landmark-bad-loc` |
| No `Roles:` line, or `Role:`, or the role misspelled: `Roles: lifebaot` | The lifeboat is placed. It has no scan text, and Find the Lifeboat can never be finished | `role-is-a-key`, three times. With `Role:`, `unknown-field` as well: it guesses `Roles` |
| `Roles: lifeboat wreckage` (two roles and no comma) | The same. The lifeboat wears one role called `lifeboat wreckage` | `role-is-a-key`, three times |
| `Roles lifeboat` (no colon) | The same | `role-is-a-key`, three times, and `fence-syntax`, an error |
| No `Kind:` line | The lifeboat is made the way a station is, not as scenery. In the test the story still played | `landmark-no-kind`. Its sentence says the lifeboat "wears the role `station`". With `Art: wreck` it does not: that role comes with a station's art |
| The bare word `wreck`, with no `Kind:` in front, or `Kind wreck` with no colon | The same | `landmark-no-kind`, and `unknown-kind-line` for the bare word or `fence-syntax`, an error, for the missing colon |

**The step that points at it.** The mistake is in Find the Lifeboat, unless the row names
another step.

| Mistake | What the game does | Lint says |
|---|---|---|
| `Done when: reach lifebaot 500` | Find the Lifeboat appears and never finishes. The story cannot be won | `role-nothing-wears` |
| `Done when: reach The Lifeboat 500` (the name) | The same | `role-nothing-wears`. Its sentence names `the` |
| `Done when: reach boat 500` (the step's own key) | The same | `role-nothing-wears` |
| Close Inspection still says `Then: reveal salvage/home` | Find the Lifeboat never appears. Bring the Log Home appears at the hulk and finishes at DS 1, and the game does not end | `never-revealed` |
| No `Then:` line on the new step | Find the Lifeboat finishes, and Bring the Log Home never appears | `never-revealed`, about Bring the Log Home |
| `Then: reveal salvage/boat` on the new step (its own address) | The same | `reveal-self`, and `never-revealed` |
| Three hashes on the new step | The game is WON the moment the crew reaches the hulk. `mast.runtime.log` gets one line | `dangling-reveal`, twice. Each offers a line to write. Do not write it: Lecture 9, Step 7 |

A story that cannot be won ends one way. The ten minutes run out, and the game is lost.

### What lint cannot see

For every row below lint says `clean`. Both logs stay empty too.

| You wrote | What happens |
|---|---|
| `# [The Lifeboat](lifeboat)` (one hash) | The lifeboat is not placed, and Find the Lifeboat can never be finished. The Lifeboat is the last record in the file, and that is the one place lint misses a single hash |
| `Loc: 6,000, 0, 6,000` (commas inside the numbers) | The lifeboat is put at `6, 0, 0`, inside DS 1. The game is won at DS 1 without the trip |
| `Kind: lifeboat` (a word that is not a kind) | The lifeboat is made as a ship, not as scenery |
| `Art: wrek` | Not known. The test places it all the same, and the test draws nothing. Nobody has tried a wrong art word in the real game. Copy the word from the table |
| `Side: navy`, with no side of that name in the mission | The thing is on a side called `navy`, which nobody declared |
| `Roles: lifeboat, station` | The lifeboat wears the role `station`. Bring the Log Home finishes there the moment it appears, so the game is WON at the lifeboat |
| The lifeboat made a station on the crew's side: `Kind: station`, `Side: tsn`, `Art: starbase_civil` | The same, and two things more. The crew starts the game beside it, not beside DS 1. And it shows the game's stock text in place of your two readings |
| A second station of its own, anywhere on the map, with those same three lines | Bring the Log Home finishes at either station. In the test the game was won 9000 from DS 1. The crew also starts the game beside the new station |
| `Roles: lifeboat, derelict` | The lifeboat shows the hulk's `mat` and `bio` readings as well as its own. Whatever your file says about `derelict`, it now says about the lifeboat too |
| A `{word}` in a reading | It is shown exactly as you wrote it, curly brackets and all. Nothing in this lecture fills it in |
| The lifeboat with an `intel` record and no `scan` record | In the test the ship's own scan had nothing to show. The `intel` reading appeared only when Science scanned every tab |

Three checks to make by eye:

- The Lifeboat's heading has exactly three hashes.
- Every number on the `Loc:` line is plain digits.
- The word after `reach`, the word after `Scan of:`, and the word on the `Roles:` line
  are the same word.

### These are fine

| You wrote | Result |
|---|---|
| `Tab: Bio`, `Scan of: Derelict`, `Roles: Lifeboat`, or `Kind: Wreck` | Works. Capitals do not matter in these words |
| `Roles: lifeboat, wreckage` (two roles, with a comma) | Works. The lifeboat wears both |
| `Roles: tsn, lifeboat` (a side typed first, as in `story.mast`) | Works, and the lifeboat is on no side. It wears a role called `tsn`. Take the word out |
| `Loc: 6000 0 6000` (no commas) | Works |
| `## [Places](landmarks)`, or `## [Landmarks](Landmarks)` | Works. The name is yours, and a capital in the key is read as a small letter |
| `### [Escape Pod Four](lifeboat)` (the name changed) | Works. The crew sees the new name |
| `### [The Lifeboat](pod)` (the key changed, the `Roles:` line left alone) | Works. Quests and scans go by the role |
| No note line under The Lifeboat's fence | Works |
| No `Tab:` line on Lifeboat Hull | Works. It is the role's only record without one, so it is the `scan` tab |
| `Done when: reach lifeboats 500` | Works. In a `Done when:` line the game takes the `s` off |
| The new step typed below Bring the Log Home | Works. The order of the steps in the file is not the order they happen in |
| A second wreck that wears `lifeboat` too | Works. Find the Lifeboat finishes at whichever one the crew reaches, and both show the readings |

## Step 7 - Play it

Start your mission as the server with a Helm console and a Science console.

1. Open the Quest Log, as you did in Lecture 8: the handheld icon at the top, then
   **Quests**. **Salvage Run** is there with two steps under it: Close Inspection and
   Quick Work.
2. Fly to the Unknown Hulk. Inside 500, Close Inspection shows `Done`, and **Find the
   Lifeboat** is now in the list.
3. On Science, select the hulk in the list on the right. It has four tabs with text:
   `scan`, `mat`, `intel` and your `bio`. Open `bio`. One of your three readings is there.
4. Fly to The Lifeboat. It is about 6700 from the hulk. On Science, select it. It has
   your two tabs, `scan` and `intel`.
5. Inside 500 of the lifeboat, Find the Lifeboat shows `Done`, and **Bring the Log Home**
   is now in the list.
6. Fly back to DS 1, about 8500 away. Inside 1000, the game ends with your `Win:`
   sentence.
7. Close the game. Open `mast.compile.log` and `mast.runtime.log`. Both are empty.

First Contact, the template's own story, finishes its steps at the hulk too, as it did in
Lecture 9.

What the side is paid:

| Ending | Credits |
|---|---|
| Won, with the bonus | 450 |
| Won, bonus missed | 400 |

Your own quest from Lecture 8 is still running beside the story. When its two minutes are
up it pays its reward on top of these.

### The ship scans by itself

You saw in Lecture 7 that the ship's sensors scan a contact that is close, with nobody
pressing a button. How much they fill depends on whose the thing is.

| Thing | The ship's own sensors fill | Left for Science to scan |
|---|---|---|
| The hulk. It is on your side | Every tab that has text | Nothing |
| The lifeboat. It has no side | `scan` | `intel` |

So do not be surprised if the hulk's tabs already have their text the first time Science
selects it. And that is why Step 4 said to give every role a `scan` tab first.

It is also why this lesson has no step that says `Done when: scan 1 lifeboat`. The line
works. But the step is finished by the ship's own sensors, with nobody at Science. And in
the test, a scan made before the step was revealed did not count toward it. When you want
the crew to do something, use `reach`.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| Lint says anything but `clean` | Find its code in the tables in Step 6. For a code that is not there, Lecture 6, Step 7 |
| The lifeboat is not on the map | Run lint. If it says `clean`, count the hashes on The Lifeboat's heading. One hash is the slip lint cannot see |
| The lifeboat is sitting on DS 1 | `Loc:` is missing or misspelled, has fewer than three numbers, or has a comma inside a number. Lint catches all but the last |
| The game is won at DS 1, and you never went to the lifeboat | The same. The lifeboat is inside DS 1 |
| The game is won at the lifeboat | The lifeboat wears the role `station`: it has a station's art, or `station` is on its `Roles:` line |
| The game is won at a station that is not DS 1, or the crew starts the game in a new place | You placed a second station on the crew's side. Its art gives it the role `station` |
| The game is won at the hulk | A step under Salvage Run has the wrong number of hashes. Lecture 9, Step 7 |
| The lifeboat has no scan text | No `Roles:` line, or the `Scan of:` word is not the role, or its two scan records are typed below The Lifeboat and not in the Scans section |
| The lifeboat's first tab shows the line about the flight log | Both of its records say `Tab: scan` |
| The hulk's new tab is not there | The `Scan of:` word is not `derelict`, the `Tab:` word is not one of the five, or the record has four hashes |
| The hulk's first tab shows your new text | Your record has no `Tab:` line |
| A reading shows a word in curly brackets | You typed `{word}`. It is shown as written. Take the brackets out |
| Half a sentence on a tab | A reading split over two lines |
| Find the Lifeboat never appears | Close Inspection still says `Then: reveal salvage/home`. Lint's `never-revealed` gives the line to write |
| Find the Lifeboat appears and never finishes | The word after `reach` is not the role on the `Roles:` line, or the lifeboat is not on the map |
| Bring the Log Home never appears | Find the Lifeboat has no `Then: reveal salvage/home` line |
| You reach DS 1 and the game does not end | Find the Lifeboat was never finished. See the three rows above |
| `mast.runtime.log` has a line that starts `AMD error:` | A heading has one hash too many, and the game mended it as it read the file. The line gives the line number |

## Exercise

Place a second thing of your own, and let the crew choose to visit it.

1. In the Landmarks section, add a second record below The Lifeboat, with three hashes.
   Give it your own name and key. Use `Kind: wreck` and `Art: wreck`, a role of your own,
   and a `Loc:` that is not near anything else.
2. Add a line for your new role to the word list at the top of the file.
3. In the Scans section, give its role a `scan` tab with two readings.
4. In Salvage Run, add a step below Quick Work, with a name and key of your own. Copy
   Quick Work's fence, take out its `Fails when:` line, and change its `Done when:` line
   to `reach`, your role, and a distance. Write your own objective and reward. Quick Work
   has no `Part of:` or `Required:` line, so the story will not wait for your step
   either.
5. Run lint. Then play it and fly there.

## Checkpoint

You are done when all six are true:

- `sbs lint MyMission` answers `clean`, with `0 error(s), 0 warning(s)`.
- The hulk has text on a tab you added.
- The Lifeboat is on the map, away from DS 1, and has your scan text.
- Find the Lifeboat appears after the hulk and shows `Done` at the lifeboat, not before.
- Reaching DS 1 after the lifeboat ends the game with your `Win:` sentence.
- After the play, `mast.compile.log` and `mast.runtime.log` are both empty.

## Next

Lecture 11 goes back into `story.mast`. This time you read what is in it, and paste your
first recipe cards.

## Further reading

- "The AMD file format" in the library documentation: headings, fences, and how a section
  name says what its records are.
- "Quests" in the library documentation: every quest field and every trigger verb.
- `maps\peacetime_remastered.amd` in LegendaryMissions: a shipped file with a Scans
  section and a Landmarks section. Look for `## [Scans](scans)` and
  `## [Landmarks](landmarks)`.
