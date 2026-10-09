# Class 1, Lecture 6 - Lint is your editor

## What you will have at the end

A habit. After every change you run one command, read one line, fix one thing, and run it
again.

You will break your mission in five places on purpose, and mend it each time. Each break is
one a new writer makes in the first week. When you make one by accident later, you will
have seen its message before.

*[Screenshot to add: the command prompt with one warning line from lint, its four parts
marked.]*

You will type in one file, `mission.amd`. At the end it is exactly as it was at the start.

## The video

*[Link to add when recorded.]*

## Before you start

- Your mission from Lecture 3, made from the `amd` template. In this page its folder is
  called `MyMission`. Use your own folder's name.
- VS Code, with the mission folder open and `mission.amd` in front.
- A command prompt open in `data\missions`.
- The game closed.

The line numbers on this page are for the file Lecture 5 left you, with your Derelict
Intel record at the end of it. If yours differ, go by the words.

Words for this lecture:

| Word | Meaning |
|---|---|
| Lint | A program that reads your mission's files and lists what looks wrong. It changes nothing in them |
| Finding | One line that lint prints, about one problem |
| Error | A finding about a line the game cannot read the way you wrote it |
| Warning | A finding about a line the game can read, but which will not do what you meant |
| Key | The word in round brackets at the end of a heading |
| Log | A text file the game writes notes in while it runs |

The title uses "editor" the way a publisher does: the person who reads your manuscript and
marks it up. Lint marks. You fix.

## Step 1 - Run lint on a file with nothing wrong

In the command prompt, type:

```
sbs lint MyMission
```

The answer:

```
== mission.amd ==
  clean

1 amd + 1 mast file(s): 0 error(s), 0 warning(s)
```

| Line | What it tells you |
|---|---|
| `== mission.amd ==` | The file the lines below are about |
| `clean` | Lint found nothing to say about that file |
| `1 amd + 1 mast file(s)` | What it read: one fact sheet, `mission.amd`, and one story file, `story.mast` |
| `0 error(s), 0 warning(s)` | The count. This is the line to read first, every time |

Read the count line even when the answer is `clean`. If it ever says `0 amd`, lint did
not find your fact sheet at all.

## Step 2 - Break 1: a field name

Find the record **Find the Derelict**. In its fence, change `Done when:` to `Done wen:`.

```
Done wen: signal derelict_found
```

Save the file with `Ctrl+S`. Lint reads the file on your disk, so a change you have not
saved does not exist yet.

Run lint again. In the command prompt, press the up arrow and then Enter.

```
== mission.amd ==
  [WARNING] line 28:1: `Done wen` is not a field a quest has, so nothing reads this line. Did you mean `Done when`? (unknown-field)

1 amd + 1 mast file(s): 0 error(s), 1 warning(s)
```

That long line is a finding. Every finding has the same four parts.

| Part | Here | Meaning |
|---|---|---|
| The level | `[WARNING]` | A warning or an error |
| The place | `line 28:1` | Line 28 of the file, and character 1 of that line. Both count from 1. Some findings give only the line |
| The sentence | `Done wen is not a field a quest has ... Did you mean Done when?` | What is wrong, in words |
| The code | `(unknown-field)` | Lint's short name for this kind of problem. The tables in this course use it |

To go to line 28 in VS Code, press `Ctrl+G`, type `28`, and press Enter. VS Code shows
your place at the bottom of the window as `Ln` and `Col`. Lint's `28:1` is VS Code's
`Ln 28, Col 1`.

Read the sentence to its end. This one says three things, and most do:

| In the sentence | What it is |
|---|---|
| `Done wen is not a field a quest has` | What is wrong |
| `so nothing reads this line` | What the game does about it |
| `Did you mean Done when?` | What to write |

Lint guesses like this when your word is close to a real one. When it is not close, lint
cannot guess. It then lists the first few field names in a-b-c order, and adds a note
about `amd_register_fields`, which is for programmers. Skip both, and check your spelling
against the record above or below.

Fix the line, save, and run lint. You want `clean` again.

Now the lesson of this break. It was only a warning, and nothing stops you from playing a
mission that has warnings. But with that one line misspelled, Find the Derelict never
finishes, and the step after it never appears. **A warning can stop your story as surely
as an error.** Fix both.

## Step 3 - Break 2: words from a word processor

Find the description of Find the Derelict:

```
Fly out and locate the drifting hulk.
```

Replace it with this sentence. Copy it from this page, or type it in your word processor
and paste it in. Either way the quote marks come out curly.

```
Fly out and locate the “ghost ship”. It isn’t answering.
```

Save. Run lint.

```
== mission.amd ==
  [WARNING] line 31:24: `“` is not a plain keyboard character (a word processor puts these in by itself). The game cannot draw it and shows `"` in its place. Type the plain one, so every tool reads this line the same way (non-ascii)
  [WARNING] line 31:35: `”` is not a plain keyboard character (a word processor puts these in by itself). The game cannot draw it and shows `"` in its place. Type the plain one, so every tool reads this line the same way (non-ascii)
  [WARNING] line 31:44: `’` is not a plain keyboard character (a word processor puts these in by itself). The game cannot draw it and shows `'` in its place. Type the plain one, so every tool reads this line the same way (non-ascii)

1 amd + 1 mast file(s): 0 error(s), 3 warning(s)
```

Three findings, one paste: one for each curly mark. All three are on line 31, and the
number after the colon tells them apart: character 24, character 35, character 44. In
VS Code, click just in front of the first curly mark and look at the bottom of the
window. It says `Ln 31, Col 24`.

Read each sentence to its end again. It says what the game does: it cannot draw the curly
mark, and it shows the plain one in its place. So the crew would read this:

```
Fly out and locate the "ghost ship". It isn't answering.
```

That is the game being kind, and it is still a warning. The words in your file are no
longer the words on the screen. And the game has a plain twin for only some characters. A
long dash becomes `-`. Three dots that your word processor turned into one character become
`...`. An accented letter loses its accent. An emoji is left out.

Fix it by typing the marks again in VS Code. Delete each curly mark and press the plain
key: `"` and `'`. Save, and run lint: `clean`.

Then put the first sentence back, so your file matches the rest of this page:

```
Fly out and locate the drifting hulk.
```

## Step 4 - Break 3: a key that no longer matches

Find the heading of the second step:

```
#### [Study the Derelict](study)
```

Change its key to `examine`:

```
#### [Study the Derelict](examine)
```

Save. Run lint.

```
== mission.amd ==
  [WARNING] line 29:14: `find` Then reveals `first_contact/study`, and no record has that key, so nothing is revealed (dangling-reveal)
  [WARNING] line 36: `Study the Derelict` waits to be revealed, and nothing reveals it: no `Then: reveal first_contact/examine` on another step, and no answer or story line names `examine`. It never appears, and the story it belongs to cannot finish (never-revealed)

1 amd + 1 mast file(s): 0 error(s), 2 warning(s)
```

You changed line 33. Lint is talking about line 29 and line 36, and it says nothing about
line 33. Look at both:

```
Then: reveal first_contact/study
```

```
Starts when: revealed
```

Line 29 points at a record by its key, and the key it names is gone. Line 36 is in the
record you renamed: that step waits to be pointed at, and nothing points at `examine`.
They are the two ends of one broken link. Lint names the line that points and the line
that waits. The line you changed is between them.

| In the message | In plain words |
|---|---|
| `` `find` `` | The key of the record that line 29 is in |
| `Then reveals first_contact/study` | What line 29 points at |
| `no record has that key, so nothing is revealed` | The step it points at will never appear |
| `waits to be revealed` | Line 36 says `Starts when: revealed`. That step stays hidden until another line names it |
| `no Then: reveal first_contact/examine on another step` | The line that would name it, spelled with its new key |
| `no answer or story line names examine` | Two other ways a step can be named. You meet them later in the course |
| `It never appears, and the story it belongs to cannot finish` | What the game does |

There is a second way to ask what line 29 points at. Type:

```
sbs lint MyMission --missing
```

```
1 thing(s) referenced but not written yet:

  first_contact/study
      revealed by `find`   mission.amd:29
```

`--missing` lists every key you have pointed at and not written. It is a to-do list for a
story you are still drafting.

You have two ways to fix this one: put the key back, or change line 29 to the line the
second finding spells out. Put the key back to `study`. Save, and run lint: `clean`. Both
findings go at once.

If you had played it: Find the Derelict finishes when the ship reaches the hulk, and Study
the Derelict never appears.

## Step 5 - Break 4: a fence left open

Find the record **Derelict Hull**, near the end of the file:

```
### [Derelict Hull](derelict_scan)
---
Scan of: derelict
Tab: scan
---
% The hull is cold. Whatever happened here happened a long time ago.
% Hull plating is intact but every port is dark. No power anywhere aboard.
```

Delete the second `---`, the one under `Tab: scan`. Save. Run lint.

```
== mission.amd ==
  [ERROR] line 48: the fence that opens here has no closing `---` before the next heading, `### [Derelict Materials](derelict_mat)` on line 54. The lines under its fields are read as fields, so `### [Derelict Hull](derelict_scan)` has no text. Add a `---` line under its last field (unclosed-data-fence)

1 amd + 1 mast file(s): 1 error(s), 0 warning(s)
```

This is your first error.

You deleted line 51. Lint names line 48. Look at line 48: it is the first `---`, the one
that opens the fence. Lint names the line where the fence opens, because that is the
fence that never closes. The sentence then tells you where the missing line goes.

| In the message | In plain words |
|---|---|
| `the fence that opens here` | The `---` on line 48 |
| `before the next heading ... on line 54` | The game stops reading this fence at the next heading. The record that starts there, Derelict Materials, is not harmed |
| `The lines under its fields are read as fields` | Your two readings were taken for fields, and they are not fields |
| `has no text` | So this record keeps its fields and has nothing to show |
| `Add a --- line under its last field` | The fix. The last field is `Tab: scan` |

Type the `---` back under `Tab: scan`. Save. Run lint: `clean`.

This is break 3 again in another place: the line lint names is not always the line you
changed. Read the sentence. It says where to look.

If you had played it: the hulk keeps its `mat` reading and has no `scan` reading.

## Step 6 - Break 5: the number of hashes

The hashes in front of a heading say where a record sits. In this file `##` starts a
section, `###` starts a record in it, and `####` starts a step of the record above it. You
will get the count wrong two ways, on one heading.

**One hash too many.** On the same record, add a fourth hash to the heading:

```
#### [Derelict Hull](derelict_scan)
```

Save. Run lint.

```
== mission.amd ==
  [ERROR] line 47: `#### [Derelict Hull](derelict_scan)` has 4 hashes and the heading it sits under has 2: 1 too many. The game reads it as if it had 3, which may not be the record you meant it to be (heading-level-jump)

1 amd + 1 mast file(s): 1 error(s), 0 warning(s)
```

| In the message | In plain words |
|---|---|
| `the heading it sits under has 2` | The nearest heading above with fewer hashes: `## [Scans](scans)` |
| `1 too many` | A heading can have one more hash than the heading it sits under, and no more |
| `The game reads it as if it had 3` | What the game does: it takes the extra hash off for you |
| `which may not be the record you meant it to be` | The game is guessing, and a guess can be wrong |

Here the guess is right. Three hashes is what this record should have, so the game reads
it and nothing is lost. It is still an error, and it is still yours to fix: with two
hashes too many on Study the Derelict, the same guess makes it a step of Find the
Derelict, and it never appears.

Take the fourth hash off. Save. Run lint: `clean`.

In break 1 a warning stopped your story. Here an error cost you nothing. So do not judge a
finding by its level. Read its sentence: that is where lint says what the game will do.

**Too few hashes.** Now take two hashes off the same heading, so it has one:

```
# [Derelict Hull](derelict_scan)
```

Save. Run lint.

```
== mission.amd ==
  [ERROR] line 47: `# [Derelict Hull](derelict_scan)` has 1 hash, and the next record (line 55) has 3. One hash starts a new title, so this record and the ones after it are no longer in their section. Give it 3 (heading-level-jump)
  [WARNING] line 55:6: `Derelict Materials` has 3 hashes, which makes it a section of its own, and nothing in this mission reads a section keyed `derelict_mat`. If it is a record, give its heading 4 hashes so it sits inside the section above it (section-not-loaded)
  [WARNING] line 55:6: `Derelict Materials` is nested under the scan record `Derelict Hull`, so it is not read. Give it the same number of hashes (scan-record-level)
  [ERROR] line 62: `### [Derelict Intel](derelict_intel)` has 3 hashes and the heading it sits under has 1: 1 too many. The game reads it as if it had 2, which may not be the record you meant it to be (heading-level-jump)
  [WARNING] line 62:6: `Derelict Intel` has 3 hashes, which makes it a section of its own, and nothing in this mission reads a section keyed `derelict_intel`. If it is a record, give its heading 4 hashes so it sits inside the section above it (section-not-loaded)
  [WARNING] line 62:6: `Derelict Intel` is nested under the scan record `Derelict Hull`, so it is not read. Give it the same number of hashes (scan-record-level)

1 amd + 1 mast file(s): 2 error(s), 4 warning(s)
```

One changed line made six findings.

Do not work through all six. Read the first one only.

The first is about line 47, the line you changed. It says what happened: one hash starts
a new title, so this record and the ones after it are no longer in their section. It ends
with the fix: `Give it 3`.

The other five are about line 55 and line 62. Those are Derelict Materials and your own
Derelict Intel, two records you did not touch, and they have nothing wrong with them.
They are the same mistake seen from further down the file. Look at the advice for line
55: one finding says to give it four hashes, and the other says to give it the same
number as the record above. Do either, and you have two mistakes.

Put the three hashes back on line 47. Save. Run lint: `clean`. All six are gone.

**The rule: fix the first finding, then run lint again.** Never start from the bottom of
the list.

If you had played it with one hash: the hulk has no scan text at all, and the game writes
the sentence of lint's first finding, word for word, in `mast.runtime.log`.

You will put the fourth hash back for a minute in Step 8, to see what the game says about
it.

## Step 7 - Check it

You have now read your first findings. These tables hold the rest of what a new writer
runs into. Every row was tried on this mission. The last column is the code at the end of
lint's line.

**The heading:**

| Mistake | What the game does | Lint says |
|---|---|---|
| `###[Derelict Hull](derelict_scan)` (no space after the hashes) | The record is gone. The hulk has no `scan` text | `broken-heading`, an error. Its sentence gives the line to write |
| `### [Derelict Hull] (derelict_scan)` (a space before the round bracket) | The same | `broken-heading`, an error. Its sentence names the space |
| `### [Derelict Hull](derelict_scan` (no closing round bracket) | The same | `broken-heading`, an error |
| `### [Derelict Hull(derelict_scan)` (no closing square bracket) | The same | `broken-heading`, an error |
| `### Derelict Hull (derelict_scan)` (no square brackets) | The same | `broken-heading`, an error |
| `### [Derelict Hull]` (no key) | The same | `broken-heading`, an error |
| A note typed after the heading, on the same line | The same | `broken-heading`, an error |
| Spaces in front of a heading | The same | `broken-heading`, an error |
| `[Derelict Hull](derelict_scan)` (the hashes left off) | The same | `broken-heading`, an error. Its sentence gives the line to write |
| `#### [Derelict Hull](derelict_scan)` (four hashes straight under two) | The game reads it as three. Nothing is lost. It writes one line in `mast.runtime.log` | `heading-level-jump`, an error |
| `# [Derelict Hull](derelict_scan)` (one hash on a record) | The hulk has no scan text at all | Six findings. The first is `heading-level-jump`, an error, on that line |
| The `#` title line at the top deleted, or typed with no brackets | Nothing in the file is read: no quests, no scan text | Four findings. The first is `heading-level-jump`, an error. It says there is no title, and shows how to write one |
| `### [Find the Derelict](find)` (three hashes on a step) | Find the Derelict becomes a story of its own. Study the Derelict never appears, and First Contact never finishes | `dangling-reveal`, a warning, on the `Then:` line. Its sentence offers a line to write. Do not write it. Put the hash back |
| `##### [Study the Derelict](study)` (five hashes on a step) | First Contact finishes as soon as Find the Derelict does. Study the Derelict never appears | `reveal-path`, a warning, on the `Then:` line |

Every `broken-heading` row is one pattern gone wrong. A heading is hashes, a space, square
brackets, round brackets, with nothing in front, nothing between the two brackets, and
nothing after:

```
### [Derelict Hull](derelict_scan)
```

**The fence:**

| Mistake | What the game does | Lint says |
|---|---|---|
| The closing `---` deleted | That record keeps its fields and loses its text: the hulk has no `scan` text. The record after it is read as usual | `unclosed-data-fence`, one error, on the line where the fence opens |
| The closing `---` typed as `--`, as `___`, as `***`, as `- - -`, or changed to one long dash by a word processor | The same | `fence-shape`, an error, on that line. The long dash gets a `non-ascii` warning as well |
| The opening `---` deleted | That record's fields are read as text, so the hulk has no `scan` text. The rest of the file is read as usual | `fence-not-opened`, an error, on the first field |
| A sentence typed between the heading and the opening `---` | The same | `fence-not-opened`, an error. Its sentence says which line to move |
| A `---` typed inside a description, as a scene break | The `---` is kept as part of the description. The rest of the file is read as usual | Nothing. It is allowed |
| `Scope shared` (no colon), or `Scope = shared` | The game skips the line. In this mission nothing else changes | `fence-syntax`, an error |
| The description typed above the closing `---` | The step has no description | `fence-syntax`, an error. Its sentence gives the fix |
| `Tab: mat` typed below the closing `---` | The hulk's `scan` tab now reads either `Tab: mat` or the Materials sentence. Its own two readings and its `mat` tab are gone | `duplicate-scan` and `field-below-fence`, warnings. The second one is the mistake |

**The fields:**

| Mistake | What the game does | Lint says |
|---|---|---|
| `Done wen:` | Find the Derelict never finishes | `unknown-field`, a warning. It guesses the word you meant |
| `Scop: shared` | The game skips the line. In this mission nothing else changes | `unknown-field`, a warning |
| `Tabb: mat` | The Materials sentence replaces the hulk's `scan` text | `duplicate-scan` and `unknown-field`, warnings. The second one is the mistake |
| Spaces or a tab in front of a field line | The line is joined to the one above it. In front of `Done when:`, Find the Derelict is only on offer and never starts | `field-indented`, a warning |
| `Done when:` written twice in one fence | The second one is used | `repeated-field`, a warning |
| `Starts when: at onse` | Find the Derelict is only on offer. It never starts, and the story stops there | `unknown-trigger`, a warning. Its sentence lists what you can write |
| `Tab: sacn` | That text is put on a tab the game does not have. It is never shown | `unknown-scan-tab`, a warning |
| `Scope: shard` | Nothing changes in this mission | `unknown-enum-value`, a warning |
| `Then: revael first_contact/study` | Study the Derelict never appears | `unknown-then-verb` and `dangling-reveal`, warnings |

**Keys, and words that have to match:**

| Mistake | What the game does | Lint says |
|---|---|---|
| `(study)` changed to `(examine)`, the `Then:` line left alone | Find the Derelict finishes. Study the Derelict never appears | `dangling-reveal` on the `Then:` line and `never-revealed` on the step that waits, both warnings |
| The story's own key changed, `(first_contact)` to `(contact)`, the `Then:` line left alone | The same | `dangling-reveal`, a warning. Its sentence gives the line to write |
| `Then: reveal first_contact/stdy` | The same | `dangling-reveal` and `never-revealed`, warnings |
| `Then: reveal study` (the story's key and the slash left off) | The same | `reveal-path`, a warning. Its sentence gives the line to write |
| The `Then:` line deleted. Or a new step with `Starts when: revealed`, and no `Then:` line that names it | The step that waits never appears, and First Contact never finishes | `never-revealed`, a warning, on the `Starts when:` line. Its sentence gives the line to write |
| A step copied to make a new one, with the key left the same | The copy is dropped. The game keeps the first record with that key | `duplicate-key`, a warning |
| `## [Quests](quest)` | No quests at all | `section-not-loaded`, a warning. Its sentence lists the keys the story asks for |
| The `## [Scans](scans)` line deleted | The two scan records become two quests on offer. The hulk has no scan text | `unknown-field`, four times. Each one asks whether the `##` heading is missing |
| `Scan of: derelect` | The hulk has no `scan` text | `role-nothing-wears`, a warning |
| `Done when: signal derelict_fond` | Find the Derelict never finishes | `unfired-signal`, a warning |

**Text:**

| Mistake | What the game does | Lint says |
|---|---|---|
| Curly quotes, a curly apostrophe, a long dash, three dots as one character | The game shows the plain one in its place: `"`, `'`, `-`, `...` | `non-ascii`, a warning. Its sentence says what the game shows. Marks side by side share one warning |
| An accented letter | The game shows the letter without its accent | `non-ascii`, a warning |
| An emoji | The game leaves it out | `non-ascii`, a warning |
| A reading (a `%` line) broken over two lines | It becomes two readings. The crew can be shown half a sentence | `reading-wrapped`, a warning |

**The files:**

| Mistake | What the game does | Lint says |
|---|---|---|
| `mission.amd` given another name | The mission stops as it starts: the story asks for `mission.amd` by name | `amd-file-missing`, an error, under `== story.mast ==`. Its sentence names the `.amd` files the folder does have |
| `mission.amd` saved as `mission.amd.txt` | The same | `amd-file-missing`, an error. Its sentence names the `.txt` file. The count line says `0 amd` |
| Every line of `mission.amd` deleted | No quests and no scan text | `no-headings`, an error |
| A stray key press in `story.mast` | Nothing in the mission runs | `mast-compile`, an error, under `== story.mast (compile) ==`. It gives the line |

### What `clean` does not mean

`clean` means four things. Every heading, fence and field has a shape lint knows. Every
key that a line points at exists. Every character is a plain one. And the game can read
`story.mast`.

It does not mean the mission does what you meant. For each row below, lint says `clean`.

| You wrote | What happens | What tells you |
|---|---|---|
| `# [Derelict Materials](derelict_mat)` (one hash on the last record in the file) | That record is gone. The hulk has no `mat` text | Nothing |
| Three hashes on a step, and then the `Then:` line that lint offers for it | First Contact never finishes | Nothing. This is why the heading table says to put the hash back |
| A note that starts with `#`, or with one `/` | The note becomes part of a description | Nothing. In this file a note starts with `//` |
| `Done when: signal derelict_scanned` on Find the Derelict (a real signal, on the wrong step) | Find the Derelict waits for Science, not for the ship | Nothing. Lint cannot know which one you meant |

So when something is missing in the game and lint says `clean`, look at two lines: the
heading of the record that is missing, and the `Then:` line that names it.

### Three switches

| You type | What you get |
|---|---|
| `sbs lint MyMission --missing` | The to-do list from Step 4. It is not a check. It says `Nothing missing` about a file that has errors in it |
| `sbs lint MyMission --strict` | The same lines as plain lint. When there are warnings and no errors it adds one more line under the count: `FAILED: --strict counts a warning as a failure`. The switch is for a program that runs lint for you |
| `sbs lint MyMission --format compact` | One line for each finding, with the file name in front. When the mission is clean it prints nothing at all |

You do not need `--strict`. Treat every warning as something to fix, and you have it
already.

## Step 8 - Play it: the second check

Lint reads your files. It does not run them. The second check is to play the mission for
a minute and then read the two logs.

First see what a log looks like when the game has something to say.

1. Put the first half of break 5 back: four hashes on **Derelict Hull**. Save.
2. Start your mission the way you did in Lecture 3, and take a console.
3. Open the quest list. At the top of the console, beside your crew member's name, is a
   handheld icon. It opens the ePADD. Choose **Quests** to open the **Quest Log**. The
   list is on the left, and **First Contact** is in it. Select it: its `State` and its
   text are on the right. Nothing looks wrong, because the game took the extra hash off
   for you.
4. Close the game.
5. In VS Code, open `mast.runtime.log` from the file list.

```
AMD error: line 47: `#### [Derelict Hull](derelict_scan)` has 4 hashes, and a heading here can have at most 3. It is read as if it had 3. Take the extra off, or put back the heading above it
```

One line. It names the file's line, says what the game did, and says how to fix it.

Compare that with what lint said about the same mistake in Step 6. It is the same line
number and the same advice. Lint gave it to you before you played. That is why lint comes
first. The log is for what only shows while the mission runs.

Now mend it.

6. Take the fourth hash off. Save. Run lint: `clean`.
7. Open `mast.runtime.log` again. The line is still there. Lint leaves the logs alone:
   they are the game's notes on your last play, and they stay until you play again.
8. Play again. Open the quest list as before. **First Contact** is in it.
9. Close the game. Open `mast.compile.log` and `mast.runtime.log`. Both are empty. The
   game starts each play with two empty logs.

| Log | It has lines in it when |
|---|---|
| `mast.compile.log` | The game could not read `story.mast`. Nothing ran |
| `mast.runtime.log` | Something went wrong while the mission was running, or the game had to guess at a line in `mission.amd` |

Two empty logs after a play mean the game noticed nothing wrong.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| `ERROR: not a folder: MyMision` | The folder name is misspelled, or the command prompt is not in `data\missions` |
| `ERROR: not a folder: MyMission\mission.amd` | You gave lint the file. Give it the folder |
| `ERROR: which mission? Put its folder name after the command:` | You typed `sbs lint` with no folder name, or `sbs lint .` Type your folder's name after it |
| `Error: No such command 'lnt'. Did you mean 'lint'?` | A typing slip. |
| Lint says the same thing after you fixed it | You did not save. Press `Ctrl+S` and run lint again |
| The count line says `0 amd` | There is no file ending in `.amd` in the folder. Lint prints an `amd-file-missing` error above the count. Look in the folder for `mission.amd.txt` |
| `== story.mast (compile) ==` and a line that starts `not checked:` | Not a mistake of yours. The part that checks `story.mast` is not on this computer yet. The line names the command that fetches it |
| A finding names a line that looks right | Look above it for the first finding. A finding about a fence names the line where the fence opens. A finding about a `Then:` line is about the key it points at |
| Lint says `clean` and something is missing in the game | Count the hashes on the heading of the missing record, and read the `Then:` line that names it. Then read "What `clean` does not mean" in Step 7 |
| `mast.runtime.log` still shows a line after you fixed the mistake | The log is from your last play. Lint does not change it. Play again, and read it after that |
| `sbs debug` prints a line about `EXTRA_SHIP_DATA` and a line about `@media/skybox` | Both are printed for the untouched template too. They are not about your work |

## Exercise

Use the habit on your own words.

1. Rewrite the three descriptions in the Quests section in your own words: First Contact,
   Find the Derelict, Study the Derelict. Keep the names and the keys as they are.
2. Rewrite the three readings the template gave you in the Scans section. The fourth,
   under Derelict Intel, is already yours. Keep each one on a single line, with its `%`
   in front.
3. After each one: save, run lint, read the count line.
4. When all six are done, play for a minute and read both logs.
5. Then pick two rows from the tables in Step 7 that you have not tried. Make each
   mistake, read the finding, and write down its code and what you did to fix it.

## Checkpoint

You are done when all four are true:

- `sbs lint MyMission` answers `clean`, and its count line reads `0 error(s), 0 warning(s)`.
- You can point at the four parts of a finding: the level, the place, the sentence, the
  code.
- After a short play, `mast.compile.log` and `mast.runtime.log` are both empty.
- The quest list shows First Contact, with your own description.

## Next

Lecture 7 gives names to two words you saw in this file today: the role `derelict`, and
the signal `derelict_found`.

## Further reading

- "The `sbs` CLI" in the library documentation, the part called "Validating AMD". It is
  about `sbs lint`.
- "The AMD file format" in the library documentation: headings, fences, and what a kind
  is.
- "AMD authoring tools" in the library documentation: the editor's own views of the same
  findings.
- "Troubleshooting - the five classic mistakes" in the Open Universe writer's guide. Its
  third mistake is the heading table in Step 7.
