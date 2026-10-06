# Class 1, Lecture 7 - Roles and signals

## What you will have at the end

Two words of your own, each written in two files, and a list that keeps track of them.

- The hulk wears a role you named, `ghost_ship`. Your Intel reading hangs on that word.
- The story says a signal you named, `ghost_ship_found`. Your first step waits for it.
- The top of your fact sheet holds a short list: every role and every signal in your
  story, and where each one comes from.
- You know what lint says when the two files disagree, and where it says nothing.

*[Screenshot to add: VS Code's search panel showing `8 results in 2 files` for `derelict`.]*

You will open `story.mast` for the first time. You will not learn to read it. You will
change four places in it, and every word you type there goes between quote marks that are
already on the page, or into a note.

## The video

*[Link to add when recorded.]*

## Before you start

- Your mission as Lecture 6 left it: the `amd` template, your sentence in First Contact,
  and your **Derelict Intel** record from Lecture 5.
- VS Code, with the mission folder open.
- A command prompt open in `data\missions`.
- The game closed.

In this page the mission folder is called `MyMission`. Use your own folder's name. Line
numbers on this page are for a file that matches Lecture 5's line for line. If yours has
more lines, go by the words.

Five words for this lecture:

| Word | Meaning |
|---|---|
| Role | A word that a thing in the game wears, like a name tag. Your fact sheet points at the word, never at the thing |
| Signal | A word the story says out loud at one moment. A step of a quest can wait for it |
| Side | Whose a thing is. The crew's own side in this mission is called `tsn` |
| Note | A line the game skips. In `mission.amd` a note starts with `//`. In `story.mast` it starts with `#` |
| Working line | A line of `story.mast` that is not a note. The game does what it says |

The crew never sees a role or a signal. They see what those words connect: a reading on
Science, a step that shows `Done`.

## Step 1 - Two files, three promises

Your mission is two files that have to agree.

| File | What it holds | Who writes it |
|---|---|---|
| `mission.amd` | What the story IS: the quests, the readings | You |
| `story.mast` | What makes it HAPPEN: it puts things in the game and notices what the crew does | The template wrote it. You change a few words |

Open `mission.amd`. Five lines in it lean on the other file:

| Line in `mission.amd` | The word | What kind |
|---|---|---|
| `Scan of: derelict` (three times, in the Scans section) | `derelict` | A role |
| `Done when: signal derelict_found` | `derelict_found` | A signal |
| `Done when: signal derelict_scanned` | `derelict_scanned` | A signal |

Each one is a promise about `story.mast`.

- `Scan of: derelict` promises that something in the game wears the role `derelict`.
- `Done when: signal derelict_found` promises that the story will say `derelict_found`.

In this mission nothing in `mission.amd` can keep those promises. `story.mast` keeps them.
If it does not, the reading is never shown and the step never finishes.

Now open `story.mast`: click it in the file list. Three rules for this file, today and
until Lecture 11:

1. **Change only what is between quote marks, or in a note.**
2. **Never delete a quote mark, and never add one.**
3. **Leave every comma where it is.**

## Step 2 - Find the role

You are going to find a word in both files at once.

1. Press `Ctrl+Shift+F`. A search box opens on the left.
2. Type `derelict`
3. At the right end of the box are small buttons. Turn on `Aa` (Match Case) and the one
   beside it, `ab` (Match Whole Word).

Match Whole Word matters. Without it you also get `derelict_found` and `derelict_scan`.
Match Case leaves out the names, such as Find the Derelict.

Under the box: `8 results in 2 files`. Three are in `mission.amd`: your three `Scan of:`
lines. Five are in `story.mast`. Click any result to go to its line.

| Line in `story.mast` | It starts with | What it is |
|---|---|---|
| 66 and 67 | `#` | A note |
| 68 | `hulk =` | A working line. It puts the hulk in the game |
| 100 | `#` | A note |
| 103 | `//science` | A working line. It asks a question about roles |

If your count is higher than 8, one of your own sentences uses the word. That is fine.

Careful with line 103. In `mission.amd`, `//` starts a note. In `story.mast` it does not:
there, only `#` starts a note. Line 103 is a working line.

**Line 68** is where the hulk gets its roles:

```
    hulk = npc_spawn(0, 0, 9000, "Unknown Hulk", "tsn, derelict", "tsn_warpster", "behav_npcship")
```

Read only the four pieces in quotes.

| In quotes | What it is |
|---|---|
| `"Unknown Hulk"` | The name the crew sees |
| `"tsn, derelict"` | A list: its side, then the roles it wears |
| `"tsn_warpster"` | Which ship model is drawn |
| `"behav_npcship"` | How it behaves |

The second piece is the one for you. It is a list of words with commas between them,
inside ONE pair of quote marks. The first word is the side. Every word after it is a
role. So the hulk is on the side `tsn`, and it wears `derelict`.

That is the promise kept. `Scan of: derelict` in your fact sheet, and `derelict` in this
list.

Two things about what a thing wears:

- **Any number of things can wear one role.** Whatever your fact sheet says about
  `derelict`, it says about every one of them.
- **One thing can wear many roles.** The hulk wears more than you can read on this line:
  its ship model brings a few of its own, and `ship` is one of them.

**Line 103** uses the same word a second time:

```
//science if has_roles(SCIENCE_SELECTED_ID, "derelict")
```

In plain words: when Science scans something, does it wear `derelict`? If it does, the
line under it runs. That line is your second signal, and it is next.

## Step 3 - Find the signals

In the search box, type `derelict_found`. Leave both buttons on.

`4 results in 2 files`. One is in `mission.amd`, line 28. Three are in `story.mast`:

| Line in `story.mast` | It starts with | What it is |
|---|---|---|
| 86 and 87 | `#` | A note |
| 93 | `signal_emit` | A working line. It says the signal |

**Line 93:**

```
            signal_emit("quest_signal", {"SIGNAL_NAME": "derelict_found"})
```

Three pieces in quotes. Only the last one is yours.

| In quotes | What it is |
|---|---|
| `"quest_signal"` | Fixed. It means "this is for the quests". Never change it |
| `"SIGNAL_NAME"` | Fixed. Never change it |
| `"derelict_found"` | The signal: the word your step waits for |

The lines above line 93 decide WHEN the word is said: when a player ship comes within
2000 of the hulk. You do not need to read them. The note above the block tells you what
it is for.

Now search for `derelict_scanned`. `2 results in 2 files`: line 37 of `mission.amd`, and
line 104 of `story.mast`, straight under the question on line 103. So `derelict_scanned`
is said when Science scans anything that wears `derelict`.

One more thing about a signal. **It is said once, and it is not remembered.** A step
hears it only if that step has already started. A step that starts later has missed it.

## Step 4 - Name a role

In your story the hulk is a ghost ship. Give it that role, and hang your Intel reading on
it. You will do it in the wrong order on purpose, so that you see the files disagree.

You are adding a word, not changing `derelict`. Leave `derelict` alone: it is on two
working lines of `story.mast`, 68 and 103, and every later lecture uses it.

In `mission.amd`, find your record **Derelict Intel**. Change its `Scan of:` line:

```
Scan of: ghost_ship
```

Save with `Ctrl+S`. In the command prompt:

```
sbs lint MyMission
```

```
== mission.amd ==
  [WARNING] line 64: nothing in this mission wears a role called `ghost_ship`, so this scan text matches nothing. Check the spelling against the `Roles:` line of the thing you mean, or the roles in `story.mast` (role-nothing-wears)

1 amd + 1 mast file(s): 0 error(s), 1 warning(s)
```

Lint has read both files. Your fact sheet made a promise, and nothing keeps it.

| In the message | In plain words |
|---|---|
| `nothing in this mission wears a role called ghost_ship` | No list in `story.mast` has that word |
| `this scan text matches nothing` | The reading will never be shown |
| ``the `Roles:` line`` | Another way to give a role. You meet it in Lecture 10 |
| ``the roles in `story.mast` `` | The list on line 68 |

If you played it now, the hulk would have two tabs on Science, `scan` and `mat`. Your
Intel reading would be gone.

Now keep the promise. In `story.mast`, line 68, click just before the quote mark that
closes the list. Type a comma, a space, and the word:

```
    hulk = npc_spawn(0, 0, 9000, "Unknown Hulk", "tsn, derelict, ghost_ship", "tsn_warpster", "behav_npcship")
```

You added `, ghost_ship` and nothing else. Save. Run lint:

```
== mission.amd ==
  clean

1 amd + 1 mast file(s): 0 error(s), 0 warning(s)
```

The hulk now wears `derelict` and `ghost_ship`. Two of its readings hang on the first
word and one on the second. On Science nothing looks different, and that is the point: a
role changes what your lines can point at, not what the crew sees. Lecture 8 points a
quest at a role in the same way.

Four rules for a role word, and for a signal word too. Each one is a mistake somebody
made.

1. **Small letters, digits and underscores. Nothing else.** No spaces, no hyphens, no
   capitals. `ghost_ship`, not `Ghost Ship`.
2. **Letter for letter the same in both files.**
3. **One thing, not many.** `ghost_ship`, not `ghost_ships`.
4. **In a list, your word goes last, after a comma.** The first word is the side.

Search for `ghost_ship` with both buttons on: `2 results in 2 files`.

## Step 5 - Rename a signal

The step should wait for your word. Again, break it first.

In `mission.amd`, in **Find the Derelict**, change line 28:

```
Done when: signal ghost_ship_found
```

Save. Run lint:

```
== mission.amd ==
  [WARNING] line 28:19: `find` waits for the signal `ghost_ship_found`, and nothing in the mission sends it, so that wait never ends. Check the spelling against the line in the story that sends it (unfired-signal)

1 amd + 1 mast file(s): 0 error(s), 1 warning(s)
```

| In the message | In plain words |
|---|---|
| `` `find` `` | The key of the record that line 28 is in |
| `28:19` | Line 28. The word starts at the 19th character |
| `nothing in the mission sends it` | No working line in `story.mast` says that word |
| `that wait never ends` | Find the Derelict never shows `Done`, and the step after it never appears |
| `the story` | `story.mast` |

Now make the story say it. Search for the OLD word, `derelict_found`. It has three
results left, all in `story.mast`. Do the working line first.

**Line 93.** Change the last word in quotes, and only that one:

```
            signal_emit("quest_signal", {"SIGNAL_NAME": "ghost_ship_found"})
```

Save. Run lint: `clean`.

**Lines 86 and 87** are a note. The game skips it, and so does lint. Change the word there
too, so the note stays true:

```
# `Done when: signal` in mission.amd. A plain signal_emit("ghost_ship_found") would reach
# a `//signal/ghost_ship_found` route and no quest.
```

Save. Then count, both ways:

| Search for | You want |
|---|---|
| `derelict_found` | No results. The old word is gone from the folder |
| `ghost_ship_found` | `4 results in 2 files`: one in `mission.amd`, three in `story.mast` |

Counting is your own check. For a signal, lint would have caught a slip as well. For a
role it often cannot, and Step 7 shows why.

## Step 6 - Write the word list

You now know every word your two files share. Write them down where you will see them.

In `mission.amd`, find the title line, `# [Sample Mission](sample_mission)`. Click at the
end of it and press Enter twice. Type:

```
// ---- Words this file shares with story.mast. Keep this list true.
// ROLE    derelict          worn by the Unknown Hulk
// ROLE    ghost_ship        worn by the Unknown Hulk
// SIGNAL  ghost_ship_found  said when a ship comes within 2000 of the hulk
// SIGNAL  derelict_scanned  said when Science scans anything that wears derelict
```

Every line starts with `//` at the left edge, so the game skips all five. The list is for
you. When your story has thirty of these words, it is how you will spell the thirty-first
the same way twice.

Save. Run lint: `clean`.

## Your finished pieces

In `mission.amd`, three places:

```
// ---- Words this file shares with story.mast. Keep this list true.
// ROLE    derelict          worn by the Unknown Hulk
// ROLE    ghost_ship        worn by the Unknown Hulk
// SIGNAL  ghost_ship_found  said when a ship comes within 2000 of the hulk
// SIGNAL  derelict_scanned  said when Science scans anything that wears derelict
```

```
Done when: signal ghost_ship_found
```

```
### [Derelict Intel](derelict_intel)
---
Scan of: ghost_ship
Tab: intel
---
% No flight plan was ever filed for this ship. Somebody wanted her forgotten.
```

In `story.mast`, four lines:

```
    hulk = npc_spawn(0, 0, 9000, "Unknown Hulk", "tsn, derelict, ghost_ship", "tsn_warpster", "behav_npcship")
```

```
# `Done when: signal` in mission.amd. A plain signal_emit("ghost_ship_found") would reach
# a `//signal/ghost_ship_found` route and no quest.
```

```
            signal_emit("quest_signal", {"SIGNAL_NAME": "ghost_ship_found"})
```

Both whole files are in `example\`.

## Step 7 - Check it

```
sbs lint MyMission
```

You want `clean`, and `1 amd + 1 mast file(s): 0 error(s), 0 warning(s)`.

Every row below was tried on this mission, one at a time. Lint was run. Then the game was
run without a screen, by a script that put the ship beside the hulk and had its sensors
scan it. The last column is the code at the end of lint's line. "Find" and "Study" are the
two steps, Find the Derelict and Study the Derelict.

**The role word in `mission.amd`** (the mistake is on your Intel record):

| Mistake | What the game does | Lint says |
|---|---|---|
| `Scan of: ghost_ship` before the hulk wears it | The hulk has no `intel` tab | `role-nothing-wears` |
| `Scan of: derelect` | The same | `role-nothing-wears` |
| `Scan of: derelicts`, or `ghost_ships` | The same | `role-nothing-wears` |
| `Scan of: ghostship` when the hulk wears `ghost_ship` | The same | `role-nothing-wears` |
| `Scan of: derelict_intel` (the record's own key) | The same. A key is not a role | `role-nothing-wears` |
| `Scan of: ghost ship`, or `Scan of: Unknown Hulk` | The same | `scan-of-many`. It means: one word |
| All three `Scan of:` lines misspelled | The hulk has no text on any tab, and Study never finishes | `role-nothing-wears`, three times |

**The hulk's list in `story.mast`:**

| Mistake | What the game does | Lint says |
|---|---|---|
| `"tsn, derelict, ghost_shp"`, or `ghost_ships` | The hulk has no `intel` tab | `role-nothing-wears`, on your `Scan of:` line |
| `"tsn, derelict, ghost ship"` (a space where the fact sheet has `_`) | The same | `role-nothing-wears` |
| The closing quote mark deleted | Nothing in the mission runs. The game shows an error page | `mast-compile`, an error, on line 68 of `story.mast` |
| Curly quote marks, pasted from a word processor | The same | `mast-compile`, an error. It says `invalid character`. And `role-nothing-wears` |
| Quote marks typed round your word, inside the list: `"tsn, derelict, "ghost_ship""` | The same | `mast-compile`, an error, and `role-nothing-wears` |

**The signal word:**

| Mistake | What the game does | Lint says |
|---|---|---|
| `Done when: signal ghost_ship_found` before the story says it | Find never finishes. Study never appears | `unfired-signal` |
| `Done when: signal ghost_ship_fond` | The same | `unfired-signal` |
| `Done when: ghost_ship_found` (the word `signal` left out) | The same | `unknown-trigger`. Its sentence lists what you can write |
| `Done when: signal`, with no word after it | The same | `signal-no-name` |
| `Done when: signal ghost_ship_found.` (a full stop), or quote marks round the word | The same | `unfired-signal` |
| The word changed in `mission.amd` and in the note on lines 86 and 87, and not on line 93 | The same | `unfired-signal`. A note does not send anything |
| Line 93 changed and `mission.amd` not, or the word misspelled on line 93 | The same | `unfired-signal` |
| Line 93 cut down to `signal_emit("ghost_ship_found")`, or its `"quest_signal"` changed to your word and the rest left | The same. A quest hears nothing that is not sent as `quest_signal` | `unfired-signal`, with another sentence: it gives the line to write |
| `"SIGNAL_NAME"` on line 93 misspelled, or changed to your word | The same. `mast.runtime.log` gets one line: "a `quest_signal` was sent with no name" | `unfired-signal` |
| `"SIGNAL_NAME": "derelict_scaned"` on line 104 | Study never finishes, so First Contact never does | `unfired-signal`, on the `Done when:` line of Study the Derelict: the line that waits |
| The closing quote mark of the word deleted | Nothing in the mission runs | `mast-compile`, an error, on line 93. And `unfired-signal` |
| Both quote marks round the word deleted | An error page when the ship reaches the hulk | `unfired-signal` |

For a role or a signal, lint names the line in `mission.amd` that makes the promise. The
mistake may be in the other file.

### What lint cannot see

Lint checks your two kinds of word in two different ways.

- For a SIGNAL it looks for a working line of `story.mast` that sends that word to the
  quests. So it catches nearly every slip in the table above, whichever file it is in.
- For a ROLE it only looks for the word between quote marks, somewhere in `story.mast`.
  It does not ask whether the word is in a list of roles, or in the right list.

So lint catches a wrong role in `mission.amd`. It misses most wrong roles in
`story.mast`. For every row below lint says `clean`. Both logs stay empty too, except in
the one row that says otherwise.

| You did | What the game does |
|---|---|
| Typed your role FIRST: `"ghost_ship, tsn, derelict"` | The hulk leaves the crew's side. Its side is now `ghost_ship`, which is no side at all. On Science it is drawn grey, not in a friendly ship's color. `mast.runtime.log` gets one line: `Side not found: [ghost_ship]` |
| Left out the comma: `"tsn, derelict ghost_ship"`. Or typed `;` or `and` for it | The hulk wears one role called `derelict ghost_ship`. It has lost `derelict`: no text on any tab, and Study never finishes |
| Typed your role OVER the old one: `"tsn, ghost_ship"` | The hulk loses its `scan` and `mat` readings, and Study never finishes |
| Misspelled the old role in the list: `"tsn, derelect, ghost_ship"` | The same. Lint found `derelict` in quotes on line 103 and looked no further |
| Renamed `derelict` itself in the fact sheet and on line 68, and not on line 103 | The readings are shown, and Study never finishes. Line 103 still asks for `derelict` |
| Typed your role into the name: `"Unknown Hulk, ghost_ship"` | The crew sees a hulk called `Unknown Hulk, ghost_ship`. It has no `intel` tab |
| Typed your role on the line above, the station's | The hulk has no `intel` tab. Your reading is shown nowhere |
| Gave the station the hulk's role as well: `"tsn, station, derelict"` | DS 1 gets a `mat` tab with the hulk's reading, and Study finishes when Science scans the STATION. Two things wear the word, so both count |
| `Scan of: hulk` (a word from the name) | The hulk has no `intel` tab. A name is not a role |
| `Scan of: wreck` | The same. `wreck` is on lint's own list of roles the game gives out by itself, so lint lets it pass. Nothing in this mission wears it |
| `Scan of: "ghost_ship"`, or `Scan of: ghost_ship.` | The same. The quote marks, or the full stop, became part of the word |

One slip with a signal gets past lint as well:

| You did | What the game does |
|---|---|
| Made Study the Derelict wait for `ghost_ship_found` too | Study never finishes. The word was said before Study had started |

One more stops the game instead of going quiet. Lint says `clean` for it too.

| You did | What the game does |
|---|---|
| Deleted the comma AFTER the list's closing quote, or typed your role as a quoted word of its own: `"tsn, derelict", "ghost_ship",` | An error page as the mission starts |

And lint is wrong the other way once. This works in the game, and lint warns:

| You wrote | Lint says |
|---|---|
| A role with a space that the hulk really wears: `ghost ship` in both files | `scan-of-many`. It says nothing wears it |

Keep to rule 1 in Step 4, small letters and underscores, and lint's answer is true.

### These are fine

| You wrote | Result |
|---|---|
| `Scan of: Ghost_Ship`, or capitals in the hulk's list | Works. The game reads a role in small letters, in both files |
| A signal with capitals, in either file or in both: `Ghost_Ship_Found` | Works. The game reads a signal in small letters, in both files |
| Spaces for the underscores of a signal, in either file or in both: `ghost ship found` | Works. The game reads the spaces as underscores |
| A space before the closing quote in `story.mast`: `"ghost_ship_found "` | Works. The game drops the space |
| A signal with hyphens, the same in both files: `ghost-ship-found` | Works |
| `"tsn, derelict,ghost_ship"` (no space after the comma) | Works |
| `'tsn, derelict, ghost_ship'` (single quote marks, both ends) | Works. Keep the double ones: they are what the file uses |
| A role with the same word as a key, a section's key, or a signal | Works. They are three separate lists. It is confusing: do not |
| Only line 93 changed, and the note left with the old word | Works. The note is now wrong, and a search for the old word still finds it |

## Step 8 - Play it

Start your mission as the server with a Helm console and a Science console, the way you
did in Lecture 3.

1. On Helm, open the quest list: the handheld icon at the top, beside the crew member's
   name, then **Quests**. **First Contact** is there, with **Find the Derelict**.
2. Fly to the Unknown Hulk. It is about 9000 from the station, DS 1.
3. Inside 2000, Find the Derelict shows `Done`. That is your signal. The story said
   `ghost_ship_found`, and your step was waiting for that word.
4. **Study the Derelict** appears. The ship's sensors scan a contact that is close, with
   nobody pressing a button, so it shows `Done` a few seconds later.
5. On Science, select the hulk in the list on the right. It has three tabs: `scan`, `mat`
   and `intel`. Open `intel`. That is your role: the reading hangs on `ghost_ship`, and
   the hulk wears it.
6. Close the game. Open `mast.compile.log` and `mast.runtime.log`. Both are empty.

Now see one disagreement in the game, so you know it when you meet it.

1. In `story.mast`, line 68, change `derelict` to `derelect`. Leave the rest of the list
   alone. Save.
2. Run lint. It says `clean`. This is the fourth row of "What lint cannot see".
3. Play. Fly to the hulk. Study the Derelict appears, and never shows `Done`. On Science
   the hulk has lost its `scan` and `mat` readings.
4. Close the game. Both logs are empty. Nothing told you.
5. Search for `derelict`, with both buttons on. With your word list in the file you want
   nine results, and there are eight. The count told you.
6. Put the word back. Save. Search again: `9 results in 2 files`.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| Lint says `role-nothing-wears` | The word after `Scan of:` is in no list in `story.mast`. Compare the two, letter by letter |
| Lint says `unfired-signal` | The word after `signal` is not sent by a working line of `story.mast`. Compare it with line 93 or line 104. A note does not count. If the sentence says `a plain signal_emit`, line 93 has lost its `"quest_signal"`: the sentence gives the line to write |
| Lint says the same thing after you fixed it | You saved one file and not the other. A dot on a tab in VS Code means that file is not saved |
| Lint prints `== story.mast (compile) ==` and an error | A quote mark is missing, extra, or curly. Lint gives the line. Put back one plain `"` at each end of the word or the list |
| An error page as the mission starts | A comma outside the quote marks was deleted, or a new pair of quote marks was added on the hulk's line |
| An error page when the ship reaches the hulk | On line 93, the quote marks round your signal are gone |
| `mast.runtime.log` says a `quest_signal` was sent with no name | On line 93, `SIGNAL_NAME` is misspelled or was changed. Put it back as the template had it |
| Lint says `signal-no-name` | A `Done when: signal` line has no word after it. Write the signal's name there |
| Lint is clean and Study the Derelict never shows `Done` | The hulk no longer wears `derelict`. Look at its list on line 68: a comma between every two words, and `derelict` still there |
| Lint is clean and the hulk has no `intel` tab | Your role is not in the hulk's list: it is in the name, in the wrong line, or joined to the word before it |
| `mast.runtime.log` says `Side not found: [ghost_ship]` | Your role is the first word of the list. The first word is the side. Move yours to the end |
| The search finds nothing at all | Match Whole Word is on and you typed part of a word, or the folder open in VS Code is not your mission's |

## Exercise

Do it again with words of your own.

1. Pick the word for what DS 1 is in your story. This page uses `home_port`. Add it to the
   end of the station's list in `story.mast`, line 64: `"tsn, station, home_port"`.
2. At the end of `mission.amd`, write one scan record for that role, with `Tab: mat` and
   one reading. The station has no `mat` tab of its own, so yours is the only text there.
   Use `mat`: on `scan` and `intel` the station shows the game's own stock text, and yours
   would not appear.
3. Rename the second signal, `derelict_scanned`, to a word of your own, in both files. It
   is on one line of `story.mast` and two of `mission.amd`: the step, and your word list.
   Search for the old word afterwards: no results.
4. Add one line to your word list for the new role.
5. Run lint, then play. On Science, DS 1 has a `mat` tab with your reading, and Study the
   Derelict still shows `Done`.

## Checkpoint

You are done when all five are true:

- `sbs lint MyMission` answers `clean`, with `0 error(s), 0 warning(s)`.
- A search for `derelict_found` finds nothing. A search for your signal finds it once in
  `mission.amd` (twice, with your word list) and three times in `story.mast`.
- In the game, Find the Derelict and Study the Derelict both show `Done`, and the hulk
  has `scan`, `mat` and `intel` tabs.
- After the play, `mast.compile.log` and `mast.runtime.log` are both empty.
- You can point at a word in `mission.amd` and say whether it is a role, a signal or a
  key, and which line of `story.mast` keeps its promise.

## Next

Lecture 8 writes your first quest. Its `Done when:` line names a role, and the game does
the watching itself: no signal, and nothing to change in `story.mast`.

## Further reading

- "Quests" in the library documentation, the parts called "Triggers" and "Signals": every
  way a step can finish, and what `quest_signal` is.
- "Signal routes" in the library documentation. It is written for people who script. Read
  the first screen, and stop there.
- "The AMD file format" in the library documentation: notes, and what a key is.
