# Class 1, Lecture 5 - The shape of a record

## What you will have at the end

Two things in the game that are your words, and one new skill.

- The quest list shows a sentence you wrote, beside **First Contact**.
- Science scans the hulk and reads a line you wrote, on a tab the hulk did not have.
- You can look at any record in `mission.amd` and name its parts.

*[Screenshot to add: the quest list with First Contact selected and the new sentence
beside it.]*

You will edit one file, `mission.amd`. You will not open `story.mast`.

## The video

*[Link to add when recorded.]*

## Before you start

- The mission you created in Lecture 3 with `sbs create`, using the `amd` template.
- VS Code with the Artemis AMD extension, and the mission folder open in it.
- A command prompt open in `data\missions` (Lecture 2).

In this page the mission folder is called `MyMission`. Use your own folder's name.

Seven words for this lecture:

| Word | Meaning |
|---|---|
| Record | One thing in your story: a quest, a reading, later a person or a place |
| Heading | The first line of a record. It starts with hashes |
| Name | The words in the square brackets. People read them |
| Key | The word in the round brackets. The game uses it, and other lines point at it |
| Fence | Two lines of three hyphens, `---`, with the record's facts between them |
| Field | One fact inside the fence: a label, a colon, a value |
| Body | The sentences under the fence |

## Step 1 - Find the eight headings

Open `mission.amd`.

The first eight lines start with `//`. Those are notes. The game skips a line that starts
with `//`, so you can write notes to yourself the same way.

Now find every line that starts with a hash. There are eight:

```
# [Sample Mission](sample_mission)
## [Quests](quests)
### [First Contact](first_contact)
#### [Find the Derelict](find)
#### [Study the Derelict](study)
## [Scans](scans)
### [Derelict Hull](derelict_scan)
### [Derelict Materials](derelict_mat)
```

All eight have one shape: hashes, one space, a name in square brackets, a key in round
brackets. You met the last two in Lecture 4. They are a markdown link.

The number of hashes says what is inside what.

| Hashes | What it is | In this file |
|---|---|---|
| `#` | The title line. One in a file, at the top | Sample Mission |
| `##` | A section: a drawer for one kind of record | Quests, Scans |
| `###` | A record | First Contact, Derelict Hull, Derelict Materials |
| `####` | A record inside the record above it | Find the Derelict and Study the Derelict, the two steps of First Contact |

A heading belongs to the nearest heading above it that has fewer hashes. So Derelict Hull
is in Scans, and Scans is in Sample Mission.

Two things about a section line:

- Its **key** is a word the game looks for. Leave `(quests)` and `(scans)` as they are.
  Change `(scans)` to `(readings)` and no reading is ever shown.
- Its **name** is yours. `## [What Science Sees](scans)` works the same.

## Step 2 - Take one record apart

Find this record. It is the first step of First Contact.

```
#### [Find the Derelict](find)
---
Scope: shared
Starts when: at once
Done when: signal derelict_found
Then: reveal first_contact/study
---
Fly out and locate the drifting hulk.
```

It has three parts.

| Part | Where | What it is for |
|---|---|---|
| Heading | The first line | It names the record |
| Fence | From the first `---` to the second | Facts the game acts on, one on each line |
| Body | Below the second `---`, down to the next heading | Sentences for people |

You do not need to know what these four fields mean. That is Lecture 8. Today, see their
shape: a label, a colon, a value.

Look at the last field, `Then: reveal first_contact/study`. It points at another record
by its keys: `first_contact`, a slash, `study`. This is what a key is for. Nothing in
this file ever points at a name.

Only the heading is required. A record can have no fence, and it can have no body.

## Step 3 - Find the parts in two more

**First Contact:**

```
### [First Contact](first_contact)
---
Arc
Scope: shared
Starts when: at once
---
A derelict has drifted into the sector. Find out what happened to it.
```

One line in this fence has no colon: `Arc`. The first line of a fence may be a single
word. It says what kind of record this is. `Arc` means a story with steps, and you will
use it in Lecture 9. Every other line in a fence needs its colon.

**Derelict Hull:**

```
### [Derelict Hull](derelict_scan)
---
Scan of: derelict
Tab: scan
---
% The hull is cold. Whatever happened here happened a long time ago.
% Hull plating is intact but every port is dark. No power anywhere aboard.
```

Two fields. The body is two lines, and each starts with `%`. In a scan record every line
of the body is one reading, and Science is shown one of them.

## Step 4 - What shows, and where

The same part does not show in the same place for every kind of record.

| Part | In a quest | In a scan record |
|---|---|---|
| Name | The quest's line in the quest list | Nowhere. It is for you |
| Key | Nowhere | Nowhere |
| Body | Beside the list, when the quest is selected | The reading on Science |

The fields are not shown as you typed them. They tell the game what to do with the
record: whose reading it is, which tab it goes on, when a quest starts.

## Step 5 - Change one record's words

Find the body of **First Contact**:

```
A derelict has drifted into the sector. Find out what happened to it.
```

Select that line and type your own over it. This page uses:

```
A dead ship has drifted across the border. Nobody sent her, and nobody will say whose she is.
```

Keep it on one line, however long it gets. Do not touch the heading or the fence.

## Step 6 - Add a record of your own

Go to the end of the file. The last line is the reading of **Derelict Materials**. Leave
one blank line below it, then type:

```
### [Derelict Intel](derelict_intel)
---
Scan of: derelict
Tab: intel
---
% No flight plan was ever filed for this ship. Somebody wanted her forgotten.
```

| Line | What it means |
|---|---|
| `### [Derelict Intel](derelict_intel)` | Three hashes: a record in the Scans section. Then a name, then a key |
| `---` | The fence opens |
| `Scan of: derelict` | Whose reading this is. The hulk is the derelict |
| `Tab: intel` | Which page of the Science screen it goes on. The hulk already has `scan` and `mat` |
| `---` | The fence closes |
| The last line | The body: one reading |

Type it in VS Code. Do not write it in a word processor and paste it in. A word processor
can change hyphens into one long dash, and straight quotes into curly ones.

Seven rules for the shape. Each one is a mistake somebody made.

1. **The hashes start at the left edge.** No space in front of them.
2. **One space after the hashes.** `###[Derelict Intel]` is not a heading.
3. **Nothing between `]` and `(`, and nothing after `)`.**
4. **A key is small letters, digits and underscores.** No spaces and no capitals: a line
   that points at a key must match it letter for letter. Give
   every record its own key.
5. **A fence line is three hyphens and nothing else.** The first one sits under the
   heading, with no sentence in between. Do not type `---` anywhere else.
6. **Every field starts at the left edge.** Do not press Tab or the space bar in front of
   one.
7. **The body goes below the second `---`.**

## Your finished pieces

In the Quests section:

```
### [First Contact](first_contact)
---
Arc
Scope: shared
Starts when: at once
---
A dead ship has drifted across the border. Nobody sent her, and nobody will say whose she is.
```

At the end of the file:

```
### [Derelict Intel](derelict_intel)
---
Scan of: derelict
Tab: intel
---
% No flight plan was ever filed for this ship. Somebody wanted her forgotten.
```

The whole file is in `example\mission.amd`.

## Step 7 - Check it

Look at your file in VS Code. There should be no squiggly underlines.

Then use the command prompt in `data\missions`. This command is new, and Lecture 6 is all
about it. Today, type it and look for one word:

```
sbs lint MyMission
```

The word is `clean`:

```
== mission.amd ==
  clean

1 amd + 1 mast file(s): 0 error(s), 0 warning(s)
```

Under `clean` you may also see a line `== story.mast (compile) ==` and a line that starts
`not checked:`. They are not about your file. Leave them for Lecture 6.

If a line that starts with `[ERROR]` or `[WARNING]` is there in place of `clean`, the
shape of something is wrong. Read the sentence, mend that line of your file, and run the
command again. Lecture 6 teaches you to read these lines properly.

`clean` means lint found nothing. It does not mean the shape is right. A few mistakes get
past it, and they are in a table of their own below. So read your record against the
seven rules as well.

### When something looks wrong

You do not have to learn these tables. Come back to them when something looks wrong.

A line from lint has four parts: `[ERROR]` or `[WARNING]`, the line number in your file,
a sentence, and a short code in round brackets at the end. The third column gives a few
words of the sentence, and the code. Some lines have a second number, as in
`line 22:44`. That is how far along the line to look, counted from 1. VS Code shows the
same pair at the bottom of its window, as `Ln 22, Col 44`.

In each table the mistake is made in your new record, unless the row says otherwise.

**The heading:**

| Mistake | What the game does | What lint says |
|---|---|---|
| `### [Derelict Intel]` (no key) | Makes no record. Your six lines become six more readings of the record above, so the Mat tab may read `Tab: intel` or `---` | An error: "there is no `(key)` after the `[Name]`" (`broken-heading`) |
| `### (Derelict Intel)[derelict_intel]` (the brackets swapped) | The same | The same error |
| `### [Derelict Intel] (derelict_intel)` (a space before the round bracket) | The same | An error: "there is a space between `]` and `(`" (`broken-heading`) |
| `###[Derelict Intel](derelict_intel)` (no space after the hashes) | The same | An error: "there is no space between the hashes and the `[`" (`broken-heading`) |
| ` ### [Derelict Intel](derelict_intel)` (a space before the hashes) | The same | An error: "there is a space in front of the hashes" (`broken-heading`) |
| `[Derelict Intel](derelict_intel)` (the hashes left off) | The same | An error: "this line has a fence under it and no hashes in front" (`broken-heading`). It ends with the line to type |
| `### Derelict Intel (derelict_intel)`, or `### Derelict Intel` (no square brackets) | The same | An error: "it is meant to start a record, but it is not written as one" (`broken-heading`) |
| `### [Derelict Intel](derelict_intel) my new one` (words after the key) | The same | An error: "this is nearly a heading, but not quite" (`broken-heading`) |
| `### [Derelict Intel](derelict_intel` (no closing bracket) | The same | The same error |
| `### [Derelict [new] Intel](derelict_intel)` (square brackets inside the name) | The same | The same error |
| A quest, or a step, copied and pasted with its key left the same | Keeps the first and drops the copy. It is never in the quest list | A warning: "`study` is the key of 2 records in the same place" and "the game keeps the first and drops the rest" (`duplicate-key`). It gives both line numbers |
| Two records in the Scans section with one key, on two different tabs | Shows both readings. A scan's key is not used | The same warning, with no word about dropping: "Nothing can point at one and not the other. Give each its own key" |
| `#### [Study the Derelict](Study)` (a capital in a key that a line points at) | Never shows that step. The line that points at it says `study` | Two warnings: "`find` Then reveals `first_contact/study`, and no record has that key, so nothing is revealed" (`dangling-reveal`), and "`Study the Derelict` waits to be revealed, and nothing reveals it" (`never-revealed`) |
| `### [First Contact](cold_hulk)` (a key changed, and the line that points at it left alone) | Never shows Study the Derelict | The `dangling-reveal` warning. It ends with the line to type: "write `Then: reveal cold_hulk/study`" |

Most `broken-heading` errors end "The game does not read it as a heading, so the record
is not there".

**The hashes, and where the record sits:**

| Mistake | What the game does | What lint says |
|---|---|---|
| Four hashes on your record | Puts it inside Derelict Materials, where it is not read. No Intel tab | A warning: it "is nested under the scan record `Derelict Materials`, so it is not read. Give it the same number of hashes" (`scan-record-level`) |
| Five hashes on your record | Reads it as four, so the same thing happens. No Intel tab | An error: it "has 5 hashes and the heading it sits under has 3: 1 too many" (`heading-level-jump`), and the warning above |
| Four hashes on Derelict Hull, the first record under `## [Scans](scans)` | Reads it as three. Nothing is lost. Take the extra hash off anyway | The same error: it "has 4 hashes and the heading it sits under has 2: 1 too many" |
| Two hashes on your record | Makes it a section of its own, which nothing reads. No Intel tab | A warning: "give its heading 3 hashes so it sits inside the section above it" (`section-not-loaded`) |
| One hash on a record in the middle of the Scans section | Takes that record, and every record below it, out of the section. None of them is read | An error on that record's line: "One hash starts a new title, so this record and the ones after it are no longer in their section. Give it 3" (`heading-level-jump`). More lines follow, about the records below. Mend the first and run lint again |
| One hash on the last step of a quest, the record just above `## [Scans](scans)` | Takes the step out of its quest, and the Scans section goes with it. No readings at all | One warning, about the `Then:` line that points at the step (`dangling-reveal`). It says nothing about the hash. Do not change the `Then:` line: put the hashes back |
| Your record typed under the title line, above every section | Makes it a section of its own, which nothing reads. No Intel tab | An error: it "has 3 hashes and the heading it sits under has 1: 1 too many" (`heading-level-jump`). A warning beside it says to give the heading 4 hashes. Do not: move the record into its section |
| The title line deleted | Finds no sections. No quests and no readings | An error: "there is no title above it" and "Without it the game finds no sections in this file" (`heading-level-jump`). Four warnings follow from it |
| Your record typed at the end of the Quests section | Lists it in the quest list as a quest, with the reading as its description. No Intel tab | Two warnings: "`Scan of` is a scan field, and this record is being read as a quest because of where it sits", and the same for `Tab` (`unknown-field`) |
| `## [Scans](readings)` (a section's key changed) | Shows no readings at all | A warning: "nothing in this mission reads a section keyed `readings`" (`section-not-loaded`). It lists the keys the story asks for |
| `### [Scans](scans)` (three hashes on the section line) | Shows no readings, and lists Scans and your three scan records as quests | Six of the `unknown-field` warnings. Each one asks "Is the `##` heading for its section missing, or misspelled?" |

**The fence:**

| Mistake | What the game does | What lint says |
|---|---|---|
| No closing `---` on your record, the last in the file | Reads no fields and no body. No Intel tab | One error, on the line where the fence opens: "the fence that opens here is never closed" (`unclosed-data-fence`) |
| No closing `---` on a record in the middle of the file | That record keeps its fields and loses its text. Do it to Derelict Hull and the hulk's first tab has nothing on it. The record below is not touched | One error, on the line where the fence opens: it "has no closing `---` before the next heading" (`unclosed-data-fence`) |
| No opening `---` | Reads no fields. No Intel tab | An error: the fields "have no `---` above them, so the game reads them as text" (`fence-not-opened`) |
| A sentence, or the body, typed between the heading and the first `---` | Reads no fields. No Intel tab | An error: "this `---` does not open a fence: a fence has to be the first thing under its heading" (`fence-not-opened`) |
| `--`, `***` or one long dash for the opening line, with the closing line right | Reads no fields. No Intel tab | An error: "`--` is not a fence line, so the fields below it are read as text" (`fence-shape`). A long dash gets a `non-ascii` warning as well |
| The same for the closing line, with the opening line right | Reads no fields and no body. No Intel tab | An error: "`--` is not a fence line, so the fence above it is still open" (`fence-shape`) |
| `--`, `***`, `___`, `- - -` or one long dash for BOTH fence lines, or words after the hyphens (`--- facts`) | Reads no fields. In a scan record: no tab. In a quest: the fields are shown to the crew as its description, and the step never starts | An error on the first of the two lines: "`--` is not a fence line, so the fields below it are read as text" (`fence-shape`). Mend both lines. A long dash gets `non-ascii` warnings as well |
| No fence lines at all, with the fields straight under the heading | The same | An error: the fields "have no `---` lines round them, so the game reads them as text" (`fence-not-opened`) |
| `Tab: intel` typed below the closing `---` | Puts your reading on the hulk's first tab, in place of the two that were there, with `Tab: intel` as a reading | Two warnings: "this line is BELOW the closing `---`" and "Move it up, between the two `---` lines" (`field-below-fence`), and `duplicate-scan` |
| A field of a quest typed below its closing `---` | Shows the line to the crew, in the quest's description. The field does nothing | The `field-below-fence` warning |

**The fields:**

| Mistake | What the game does | What lint says |
|---|---|---|
| One field with a tab or spaces in front of it | Glues it to the line above: `Scan of` becomes `derelict Tab: intel`. No Intel tab | A warning: "`Tab:` has a space or a tab in front of it, so the game reads this line as more of the line above" (`field-indented`) |
| `Tab: intel` and then `Tab: mat` in one fence | Uses the last one. Your reading replaces the Mat tab's | A warning: "`Tab:` is written twice in this fence" (`repeated-field`) |
| `Tab=intel` | Ignores the line. Your reading goes on the hulk's first tab, in place of the two that were there | An error: ""Tab=intel" looks like a kind" (`fence-syntax`). It means: no colon. And `duplicate-scan` |
| `Tab intel` (no colon) | The same | An error: "expected "Label: value"" (`fence-syntax`), and `duplicate-scan` |
| `Tabb: intel` (a misspelled label) | The same | A warning: "`Tabb` is not a field a scan has, so nothing reads this line. Did you mean `Tab`?" (`unknown-field`), and `duplicate-scan` |
| `Tab: intle` (a tab the game does not have) | Shows the reading on no tab | A warning: "`Tab: intle` is not a tab Science has (scan, status, intel, mat, bio), so this reading is never shown" (`unknown-scan-tab`) |
| `Tab: "intel"` (quotes round the value) | Shows the reading on no tab | The same warning |
| `Tab: intel // the intel page` (a note on the end of a field) | Shows the reading on no tab | The same warning |
| `Tab:` (nothing after the colon) | Shows the reading on no tab | The same warning, and `duplicate-scan` |
| `Scan of: derelict, Tab: intel` (two fields on one line) | Shows the reading on no tab | A warning: "`Scan of:` takes ONE role" (`scan-of-many`) |
| `- Scan of: derelict` and `- Tab: intel` (typed as a list) | Reads no fields. No Intel tab | Two warnings: "`- Scan of` is not a field a scan has" and "Did you mean `Scan of`?", and the same for `- Tab` (`unknown-field`) |
| `# which page` (a note with a hash, inside the fence) | Ignores the line. The record still works | An error: "expected "Label: value"" (`fence-syntax`). Use `//` for a note |
| A single word on the first line of the fence, such as `Intel` | Ignores the word. The record still works | A warning: "it is not a kind the game knows" (`unknown-kind-line`) |

**The body:**

| Mistake | What the game does | What lint says |
|---|---|---|
| A reading that runs onto a second line | Makes two readings. The crew may get half a sentence | A warning: "a reading has to stay on one line" (`reading-wrapped`) |
| A plain line, or a note that starts with `#`, typed straight under the last reading | Makes it one more reading. The crew may be shown your note | The same warning |
| `---` on a line between two readings | Makes it one more reading: the crew may read `---` | The same warning |
| `/*` at the start of a line, with no `*/` after it | Cuts the rest of the file: every record below it is gone | An error: "this /* was never closed" (`fence-syntax`) |

**Letters the game cannot draw:**

| Mistake | What the game does | What lint says |
|---|---|---|
| A curly quote, a long dash, or the three dots a word processor joins into one character | Shows the plain one in its place: `"`, `'`, `-` or `...` | A warning that names the character and says "The game cannot draw it and shows `"` in its place" (`non-ascii`) |
| An accented letter | Shows the letter with no accent | The same warning |
| Any other symbol, such as an emoji | Leaves it out | The same warning. It says "The game cannot draw it and leaves it out" |
| Any of these in a line that starts with `//` | Nothing. A note is never drawn | Nothing |
| Curly quotes round a field's value, as in `Scan of:` and then the role in curly quotes | Reads them as plain quotes, and the quotes become part of the value. The reading belongs to nobody. No Intel tab | Two `non-ascii` warnings. Take the quotes out altogether |

**The file itself:**

| Mistake | What the game does | What lint says |
|---|---|---|
| `mission.amd` deleted, renamed, or saved as `mission.amd.txt` | Stops as the mission starts | An error under `== story.mast ==`: "this line asks for `mission.amd`, and there is no file of that name" (`amd-file-missing`). If the file is there under another name, the sentence says which |
| A file with nothing in it, or with no heading in it | Reads nothing: no quests and no readings | An error: "the game reads nothing from it" (`no-headings`) |

### Lint says `clean` for these

Lint cannot see every mistake of shape. For each of these it says `clean`, and the game
does not do what you meant.

| You wrote | What the game does |
|---|---|
| `# [Derelict Intel](derelict_intel)` (one hash on the LAST record in the file) | Does not read the record. No Intel tab |
| `Scan of: "derelict"` (quotes round the value) | The reading belongs to nobody. No Intel tab |
| A plain line typed below the last reading, with a blank line between | Makes it one more reading |
| A line that starts with `#` above the first reading | Makes it one more reading |
| `---` on a line between two scan records, as a divider | Makes it one more reading of the record above: the crew may read `---` |
| A note that starts with `#`, or with one `/`, typed in a quest's body or below it | Shows it to the crew, as part of that quest's description |
| A `//` note on the end of a sentence, or on the end of a reading | Shows it to the crew. A note is a line of its own |
| `%` in front of a quest's sentence | Shows the `%` to the crew. The `%` is for readings |
| `-` and a space in front of a reading | Shows the `-` to the crew |
| A body line that starts with `=` and a space | Leaves it out. That mark means a note to yourself |

### These are fine

| You wrote | Result |
|---|---|
| A blank line under the heading, between two fields, or under the fence | Works |
| No blank line above a heading, or no blank lines anywhere | Works. The blank lines are for you |
| Four or more hyphens on a fence line, or spaces in front of the three hyphens or after them | Works |
| `Tab : intel`, `Tab:intel`, `tab: intel` or `Tab: Intel` | Works |
| Every field indented by the same amount | Works. One field indented is the mistake |
| A `//` note on a line of its own: under the heading, inside the fence, or in the body | Skipped. In a body it may have spaces or a tab in front of it |
| A colon inside a value: `Objective: Stage one: find the hulk` | Works. Only the first colon counts |
| Round brackets, or a question mark, inside a NAME: `[Who Sent Her?]` | Works |
| A question mark on the end of a key: `(derelict_intel?)` | Works. The question mark is dropped. Take it out anyway |
| A capital in a section's key: `## [Scans](Scans)` | Works. It is read as `scans` |
| Spaces round the slash in a line that points at a record: `Then: reveal first_contact / study` | Works |
| A sentence above the title line, or under a section line | Ignored |
| No `%` in front of a reading | Works. Keep the `%`: it shows where a reading starts |
| The file saved from Notepad as `UTF-16 LE` or `UTF-16 BE` | Works. Save it as `UTF-8` anyway: other tools expect that |

## Step 8 - Play it

Start your mission as the server with a Helm console and a Science console, the way you
did in Lecture 3.

1. Open the quest list. On any console, click the handheld icon at the top, beside the
   crew member's name, then **Quests**. The page that opens is the **Quest Log**.
2. Select **First Contact** in the list on the left. Your sentence is on the right.
3. Fly to the Unknown Hulk. It is about 9000 from the station, DS 1.
4. On Science, select the hulk in the list on the right. It has three tabs with text:
   `scan`, `mat` and your `intel`.
5. Open `intel`. Your reading is there.

In the real game the ship's sensors scan what is in range without anybody pressing a
button. So the tabs have their text soon after you arrive, and both steps of First
Contact finish by themselves. The Quest Log then shows First Contact as `Done`.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| The hulk has no Intel tab | Your heading is not a heading, or your fence is not a fence. Run lint. If it says `clean`, count the hashes on your heading (three), and take out any quotes round `derelict` |
| Another tab reads `---`, or `Tab: intel`, or your heading | Your heading is not a heading. Its lines went into the record above |
| The hulk's first tab shows your reading | The `Tab:` line is missing, misspelled, or below the closing `---` |
| The hulk's first tab has nothing on it | Derelict Hull has lost a fence line, or one of its fence lines is not three hyphens |
| The quest list is empty and no tab has text | The game found no sections in the file. Run lint. The title line is gone, or a `/*` has cut the file short, or the file is empty |
| The mission stops as soon as it starts | `mission.amd` is not in the folder under that exact name. Run lint: it says which names it found |
| Your record is in the quest list | It is in the Quests section. Move it below the last scan record |
| A quest's description shows `Scope: shared` and other fields | That quest's fence is not a fence. Run lint, and look at its two fence lines |
| A quest's description shows one of your notes | The note starts with `#` or with one `/`, or sits on the end of a sentence. A note is a line of its own that starts with `//` |
| A sentence shows plain quotes where you typed curly ones | Nothing is broken. The game swaps a character it cannot draw for a plain one. Type the plain one, and lint stops warning |
| First Contact still shows the old sentence | You did not save the file, or you edited a different folder's copy |
| `mast.runtime.log`, in your mission folder, has a line that starts `AMD error:` | The game mended a heading or a fence as it read the file. The line gives the line number and says what to do. Lecture 6 is about this file |

## Exercise

1. Give the hulk one more tab. Below your record, leave a blank line and write a second
   record of your own, with a new name, a new key, and `Tab: status`. Write one reading.
2. Give **Derelict Hull** a third reading: one more line that starts with `%`.
3. Reword the body of **Find the Derelict**.
4. Change the NAME of First Contact to a title of your own. Leave the key,
   `(first_contact)`, alone. Run lint, then play: the quest list shows your title, and
   nothing else changed. Later lectures call this record First Contact. Change it back,
   or remember that its key is still `first_contact`.

## Checkpoint

You are done when all four are true:

- `sbs lint MyMission` shows `mission.amd` as `clean`.
- The quest list shows your sentence beside First Contact.
- On Science, the hulk has an `intel` tab with your reading.
- You can point at any record in `mission.amd` and say which line is the heading, where
  the fence starts and ends, which lines are fields, and which are the body.

## Next

Lecture 6 breaks five things on purpose and reads what lint says about each one.

## Further reading

- "The AMD file format" in the library documentation: headings, the fence, and the marks
  a body can use.
- "Build a Universe - the writer's walkthrough" in the Open Universe documentation, the
  part called "The shape of the file". It is the same shape, in a bigger file.
