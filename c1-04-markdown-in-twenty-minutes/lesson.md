# Class 1, Lecture 4 - Markdown in twenty minutes

## What you will have at the end

Three things.

- A one-page story bible for your mission, in a file called `story-bible.md`: a title,
  three headings, a list of people, a numbered list and one link.
- You can look at `mission.amd` and say what each mark in it is for.
- You know which marks the game draws, and which it prints on the crew's screens exactly
  as you typed them.

*[Screenshot to add: VS Code with `story-bible.md` on the left and its preview on the
right.]*

You will type in one new file. You will read `mission.amd`. Only the last step changes
it, and that step is optional and puts it back.

## The video

*[Link to add when recorded.]*

## Before you start

- The mission you made in Lecture 3 (your editor and your first run): the folder
  `MyMission`, with its libraries fetched (Lecture 3, Step 4). If you gave your folder
  another name, use that name wherever this page says `MyMission`.
- VS Code, with the `MyMission` folder open in it and trusted (Lecture 3, Step 5).
- For the last step only, and that step is optional: a command prompt open in
  `data\missions` (Lecture 2), and every game window closed.

Nothing today waits for the Artemis AMD add-on:

| Steps | The file | What does the work | Without the add-on |
|---|---|---|---|
| 1 to 8, and 10 | `story-bible.md`, a page of your own | The markdown preview. It is part of VS Code itself | The same. The preview opens even in a folder VS Code does not trust |
| 9 | `mission.amd`, to read | Your eyes. The add-on puts the file in color | The file is all one color. The marks are the same |
| 11 (optional) | `mission.amd`, to change and put back | The game. It reads the saved file | The same |

If `mission.amd` is all one color, or the Status Bar says `Restricted Mode`, the add-on is
off or only partly on. Carry on with this lecture. Then do the trust table in Lecture 3,
Step 5, before Lecture 5.

Words for this lecture:

| Word | Meaning |
|---|---|
| Markdown | A way of writing a page with nothing but a keyboard. A few marks in the text say "this is a heading", "this is a list", "this is a link" |
| Mark | One of those characters: a hash `#`, a hyphen `-`, a star `*`, a bracket |
| Preview | VS Code's picture of your page as a reader would see it |
| Plain text | Letters, digits and punctuation, and nothing more. No fonts and no bold button. VS Code saves plain text. A word processor does not |
| Story bible | A writer's own page of facts about a story: who is in it, where it happens, what happens |

Why you are learning this: `mission.amd`, the file you will write in for the rest of the
course, is shaped like markdown. Twenty minutes here saves you guessing at every line of
it.

## Step 1 - Make the file and open the preview

1. In VS Code, look at the file list in the Side Bar. Its top line is your folder's name,
   `MYMISSION`, and under it are `mission.amd`, `story.mast` and the other files of your
   mission.
2. Right-click an empty place under the last file. Choose **New File...**
3. Type the name and press Enter:

```
story-bible.md
```

4. The file opens, empty. Type one line:

```
# Nobody Aboard
```

5. Press `Ctrl+K`, let go, then press `V`. The preview opens beside your file.
6. Press `Ctrl+S` to save.

On the left is what you type. On the right is what a reader sees. The hash is gone from
the right-hand side, and the words are a title.

In a `.md` file VS Code folds a long line to fit the window. That is called word wrap,
and for this kind of file it is on from the start. The line is still one line in the
file. The key `Alt+Z` switches word wrap off, and on again.

The game does not read this file. It reads `mission.amd` and `story.mast`. So this page
is yours: nothing you type in it can break your mission.

## Step 2 - A title and three headings

Click at the end of the title line and press Enter twice. That leaves a blank line under
the title. Then type three headings, with a blank line between them. Your file now reads:

```
# Nobody Aboard

## Premise

## People

## What happens
```

| You type | It is |
|---|---|
| `#`, a space, words | The title. One on a page, at the top |
| `##`, a space, words | A heading |
| `###`, a space, words | A smaller heading, inside the `##` above it |

Three rules:

1. **The hashes start at the left edge.**
2. **One space after the hashes.** `##Premise` is not a heading.
3. **More hashes means further inside.** A `###` belongs to the `##` above it.

You will count hashes again in Lecture 5. In `mission.amd` they say which record is
inside which.

## Step 3 - Paragraphs

Click at the end of the title line and press Enter twice. Type this, all on one line. Do
not press Enter in the middle of it:

```
A dead ship has drifted across the border. Nobody sent her, and nobody will say whose she is.
```

Your paragraph now has a blank line above it and a blank line below it.

Click at the end of the `## Premise` line, press Enter twice, and type:

```
The crew has one watch to find out what happened aboard, before somebody else comes to claim her.
```

Three rules:

1. **A paragraph is one line in the file, however long.** Word wrap folds it for you.
2. **A blank line ends a paragraph.**
3. **Never start a line with the Tab key or the space bar.** Writers indent a paragraph
   without thinking. In markdown an indented line is something else: the preview shows it
   in a box, in typewriter letters.

Why rule 1 matters. If you press Enter in the middle of a paragraph, the preview joins
the two halves again and you see no difference. The game does not join them. It starts a
new line wherever you pressed Enter. One paragraph on one line reads the same in both.

## Step 4 - A list of people

Click at the end of the `## People` line, press Enter twice, and type three lines:

```
- Captain Mara Vell, who gives the order and hates it
- Chief Osei, who has seen a hull like this one before
- The Voice, still talking on the hulk's radio
```

Each line is a hyphen, one space, then words. The list has a blank line above it and a
blank line below it.

That is the pattern for the whole page: **a blank line above and below every heading,
every paragraph and every list.**

## Step 5 - A numbered list

Click at the end of the last line, `## What happens`, press Enter twice, and type:

```
1. The crew finds the hulk.
2. Science takes a full scan of the hull.
3. Not written yet: somebody answers.
```

Each line is a number, a period, one space, then words. Use a numbered list when the
order matters. These three lines are the steps of your story. In Lectures 8 and 9 each
one becomes a step of a quest.

## Step 6 - One link

A link is two pairs of brackets, with nothing between them:

```
[the words a reader sees](where the link goes)
```

Square brackets first, then round brackets. No space between `]` and `(`.

Click at the end of the paragraph under `## Premise`. Type a space, then this sentence, on
the same line:

```
The idea comes from [the Mary Celeste](https://en.wikipedia.org/wiki/Mary_Celeste), a ship found sailing with nobody aboard.
```

VS Code helps as you type: when you type `[` it adds the `]`, and when you type `(` it
adds the `)`. Keep typing. When you reach the closing bracket, type it yourself as usual.

In the preview the words `the Mary Celeste` are a link, and the address is out of sight.

Remember this shape. In Lecture 5 you will see it at the start of every record in
`mission.amd`:

```
### [Derelict Hull](derelict_scan)
```

Hashes, a space, and a link. In that file the round brackets do not hold a web address.
They hold a short name the game uses, called a key.

## Step 7 - Bold and italic

Two stars each side of a word make it bold. One star each side makes it slanted.

In the Premise paragraph, put two stars each side of `nobody`:

```
a ship found sailing with **nobody** aboard.
```

In the numbered list, put one star each side of `Not written yet:`

```
3. *Not written yet:* somebody answers.
```

No space between the stars and the word.

Use these in your story bible as much as you like. Do not use them in `mission.amd`. The
game does not make anything bold: the crew would read the stars. Step 10 has the list.

## Step 8 - The plain keyboard

Markdown is plain text. Every mark on this page is a key on your keyboard.

A word processor is not plain. It changes three kinds of character as you type, and it
does not ask:

| A word processor puts in | Called | The plain one to type |
|---|---|---|
| “ ” | Curly double quotes | `"` |
| ‘ ’ | Curly single quotes, and the curly apostrophe | `'` |
| — | A long dash | `-` |
| … | Three dots joined into one character | `...` |

The game can draw only plain keyboard characters. When it reads `mission.amd` it swaps
each of these for the plain one, so the crew still reads your sentence. But the words on
the screen are then not the words in your file, and the other tools you will use read the
file too. Lecture 6 shows you the warning each one gets.

So the habit, from today:

1. **Write in VS Code.** It never changes what you type.
2. **If you bring words over from a word processor, type the quote marks, the dashes and
   the dots again.** Those are the three it changed.
3. **Keep your story bible plain too.** One day you will copy a sentence out of it and
   into `mission.amd`.

Nothing checks your story bible: no tool reads the file. The habit is the check.

## Your finished page

```
# Nobody Aboard

A dead ship has drifted across the border. Nobody sent her, and nobody will say whose she is.

## Premise

The crew has one watch to find out what happened aboard, before somebody else comes to claim her. The idea comes from [the Mary Celeste](https://en.wikipedia.org/wiki/Mary_Celeste), a ship found sailing with **nobody** aboard.

## People

- Captain Mara Vell, who gives the order and hates it
- Chief Osei, who has seen a hull like this one before
- The Voice, still talking on the hulk's radio

## What happens

1. The crew finds the hulk.
2. Science takes a full scan of the hull.
3. *Not written yet:* somebody answers.
```

The same file is `example\story-bible.md`.

## Step 9 - Read `mission.amd` with new eyes

Click `mission.amd` in the file list. Do not change anything in it.

The add-on may show small words above a heading, such as `1 reference(s)`. They are the
add-on's, and they are not in your file. And in this file word wrap starts off, so a long
line runs off the right-hand side. `Alt+Z` folds it.

You can now read most of its marks. Five of them do not mean what they mean in markdown.
Find one of each:

| In `mission.amd` | In markdown it would be | In this file it is |
|---|---|---|
| `### [Derelict Hull](derelict_scan)` | A heading whose words are a link | The first line of a record. The square brackets hold a name for people. The round brackets hold a key for the game. Nothing else may be on the line |
| `---` on the line under a heading | A line drawn across the page | A fence. Two of them, with the record's facts between |
| `% The hull is cold. Whatever happened here happened a long time ago.` | Nothing. A percent sign and two sentences | One reading for the Science screen |
| The line that starts `// ---- Quests.` | Nothing. Two slashes and a sentence, shown to the reader | A note to yourself. The game skips the whole line |
| `[[study]]` (not in your file yet) | Nothing. The reader sees the brackets | A link to another record. The game prints that record's name: `Study the Derelict` |

So this file is shaped like markdown, and it is not markdown. It has its own name, AMD,
and it is read by the game, not by a preview. The preview you opened in Step 1 is for
`.md` files only.

Lecture 5 takes one record of this file apart, line by line.

## Step 10 - Check it

Look at the preview of `story-bible.md`. You should see one title, three headings, two
paragraphs, a list of three people, a list numbered 1 to 3, one link, one bold word and
one slanted phrase. No hash, hyphen, star or bracket should be left showing.

### When the preview looks wrong

Each row is a slip somebody made. The middle column is what markdown makes of it.

| You typed | What markdown makes of it | Type this |
|---|---|---|
| `##Premise` (no space after the hashes) | Not a heading. The line is shown as typed, hashes and all | `## Premise` |
| `-Captain Mara Vell` (no space after the hyphen) | Not a list. The lines run together into one paragraph, hyphens and all | `- Captain Mara Vell` |
| `1.The crew finds the hulk.` (no space after the period) | Not a list. Shown as typed | `1. The crew finds the hulk.` |
| `[the Mary Celeste] (https://...)` (a space between `]` and `(`) | The words are not a link. The line is shown as typed, brackets and all. The preview turns the bare address into a link by itself, so it can look half right | Take the space out |
| `(the Mary Celeste)[https://...]` (the brackets the wrong way round) | The same: every bracket shows, and only the address is a link | Square brackets first |
| `[the Mary Celeste](https://...` (no closing bracket) | The same | Add the `)` |
| `** nobody **` (spaces inside the stars) | Not bold. The stars are shown | `**nobody**` |
| `**nobody` (stars on one side only) | Not bold. The stars are shown | Put two stars after the word as well |
| A paragraph that starts with the Tab key, or with four spaces | Not a paragraph. It is shown in a box, in typewriter letters | Delete the tab or the spaces |
| Enter pressed in the middle of a paragraph | Still one paragraph. The two halves are joined | Nothing is wrong here. In `mission.amd` it is a mistake: see the next table |
| `---` typed straight under a line of words | The line above becomes a heading | Leave a blank line above the `---`. Then it is a line across the page |
| A line that starts with a number and a period: `2187. A bad year.` | A list that starts at 2187 | Start the line with a word: `In 2187, a bad year.` |

### The same marks in `mission.amd`

This is the table to come back to. It says what the game does with each mark when you
type it in the two places your words go in this class: a quest's description, which the
crew reads in the Quest Log, and a reading, which the crew reads on the Science screen.

The last column is `sbs lint`, the checker you ran once in Lecture 3 and learn to read in
Lecture 6. It is here to make one point: lint says nothing about nearly all of these,
because none of them is a mistake of shape. The game just does not do what a preview
does.

**Marks the game acts on.** There are few, and most of them act only in a description:

| You type | In a quest's description | In a reading | Lint |
|---|---|---|---|
| `# Orders` or `## Orders` | Drawn as a heading: larger gray letters, the hashes gone. `#Orders` with no space is a heading too | Kept as typed, hash and all, as a reading of its own | Nothing |
| A line that is only a hash, `#` (the scene break of a typed manuscript) | Shown as typed: `#` | Kept as a reading of its own: `#` | Nothing for a description. `reading-wrapped`, a warning, for a reading |
| `- Find her.` (a hyphen, then a space) | Drawn as a list: indented, light blue, with its hyphen | Kept as typed, hyphen and all | Nothing |
| `1. Find her.` (a number, a period, then a space) | Drawn as a numbered list, indented. The game does the counting: a list typed `3.`, `4.` is shown `1.`, `2.`, and so is one typed `1)`, `2)` | Kept as typed | Nothing |
| A plain line straight under a list, with no blank line between | Drawn as part of the list: indented like the items, and in their color | Does not apply | Nothing |
| `` `drifting` `` (the backticks this course puts round words to type) | The backticks are left out. The word stays | Kept as typed, backticks and all | Nothing |
| `10^3` (a caret) | A new line starts where the caret was. The caret is gone | Kept as typed | Nothing |
| A tab in the middle of a line | One space | Kept as a tab | Nothing |
| A tab or spaces at the start of a line | Removed | Removed | Nothing |

**What the game prints as you typed it.** A preview would draw the first six:

| You type | In a quest's description | In a reading | Lint |
|---|---|---|---|
| `**drifting**`, `*drifting*`, `_drifting_` or `<b>drifting</b>` | Shown as typed, stars and all. Nothing is bold or slanted | The same | Nothing |
| `[the old report](https://example.com/report)`, anywhere in a line | Shown as typed, brackets and address. Nothing to click | The same | Nothing |
| `> She was the pride of the fleet.` | Shown as typed, with the `>` | The same | Nothing |
| `* Find her.` (a star for a list) | Shown as typed, star and all. Only a hyphen makes a list | The same | Nothing |
| `---` on a line of its own, between two paragraphs | Shown as typed: three hyphens, and no line across the screen | One more reading: `---` | Nothing for a description. `reading-wrapped`, a warning, for a reading |
| Two spaces at the end of a line (markdown's way to break a line) | Nothing. The spaces are dropped | The same | Nothing |
| `dead_reckoning` (an underscore in a word) | Shown as typed | The same | Nothing |
| A sentence that only looks like a mark: `40 years ago this ship was reported lost.`, `-Find her.`, `[Static] Is anyone aboard?`, `$500 says she is not empty.` | Shown as typed | The same | Nothing |

**Lines and gaps:**

| You type | In a quest's description | In a reading | Lint |
|---|---|---|---|
| A blank line between two paragraphs | The second paragraph starts on a new line. There is no gap between them | Two readings. The crew is shown one of them | Nothing |
| Enter pressed in the middle of a paragraph | The same as a blank line: a new line starts there | Two readings. The crew may be shown half a sentence | Nothing for a description. `reading-wrapped`, a warning, for a reading |

Three rules cover the three tables:

1. **In `mission.amd`, write plain sentences.** No stars, no backticks, no links. The crew
   would read the marks, or lose them.
2. **One paragraph, one line.**
3. **A heading and a list are the two marks a description draws.** Give a list a blank
   line above it and a blank line below it. Neither is drawn in a reading.

Of the characters a sentence is likely to open with, three can make a mark: a hash; a
hyphen followed by a space; a number followed by a period and a space. So `40 years ago`
opens a sentence. But `2187. A bad year.` is taken for the first item of a numbered list,
and the crew reads `1. A bad year.` And `#1 priority is the hulk.` is taken for a heading:
the crew reads `1 priority is the hulk.`, large and gray.

## Step 11 - Play it (optional)

This step is the only one that changes `mission.amd`, and it changes it back. It takes
five minutes. If you would sooner watch, the video does it.

1. In `mission.amd`, find this line. It is line 31, the description of **Find the
   Derelict**:

```
Fly out and locate the drifting hulk.
```

2. Select the whole line and type these nine lines over it. The third, the sixth and the
   eighth are blank:

```
# Orders
Fly out and locate the **drifting** hulk.

- Find her.
- Scan her.

Her last word was `stay`.

Read [the old report](https://example.com/report) first.
```

3. Press `Ctrl+S`. The game reads the saved file, not your screen.
4. Start the game the way you did in Lecture 3, Step 7. In the command prompt, in
   `data\missions`:

```
sbs run server,helm,science -m MyMission map=0
```

5. Go to the `helm` window. Do not fly anywhere yet. Click the handheld icon at the top,
   beside the crew member's name, then **Quests**. The page that opens is the **Quest
   Log**.
6. In the list on the left, select **Find the Derelict**. It is the line under First
   Contact.

On the right, under `State` and `Active`:

| You typed | The crew reads |
|---|---|
| `# Orders` | `Orders`, as a heading: larger gray letters, and no hash |
| `Fly out and locate the **drifting** hulk.` | The same, stars and all |
| `- Find her.` and `- Scan her.` | A list: indented, light blue, each line with its hyphen |
| ``Her last word was `stay`.`` | `Her last word was stay.` The backticks are gone |
| `Read [the old report](https://example.com/report) first.` | The same, brackets and address. There is nothing to click |
| The three blank lines | Nothing. Each line starts straight under the one before it |

A preview would have drawn all six. The game drew two, the heading and the list. It
printed two as you typed them, took the backticks away, and took no notice of the blank
lines.

7. Close all three game windows.
8. Put the file back. In `mission.amd`, press `Ctrl+Z` until the nine lines are one line
   again. If that no longer works, delete the nine lines and type the one line back:

```
Fly out and locate the drifting hulk.
```

9. Press `Ctrl+S`.

Do not leave the nine lines in. Lectures 5 and 6 start from `mission.amd` as it was when
you began today, and they name its lines by number.

Two files in `example\` are named `mission.amd`:

| File | What it is |
|---|---|
| `example\mission.amd` | The file as you hand it on to Lecture 5: the one Lecture 3 gave you, with nothing changed |
| `example\step-11-only\mission.amd` | The same file with the nine lines in place. It is there to copy from. It is not how this lecture ends |

## If something goes wrong

| What you see | Likely cause |
|---|---|
| No preview opens | The file's name does not end in `.md`, or the cursor is not in the file. Click in the file, then press `Ctrl+K`, let go, and press `V` |
| A long paragraph runs off the right-hand side of the window | Word wrap is off. Press `Alt+Z` |
| The preview shows a line with its hashes | No space after the hashes, or seven hashes and more |
| Your list is one paragraph with hyphens in it | No space after the hyphens |
| A paragraph is in a box, in typewriter letters | It starts with a tab or with four spaces |
| A line of words has turned into a heading | There is a `---` on the line straight under it |
| The link shows its brackets | A space between `]` and `(`, or the brackets the wrong way round, or a bracket missing |
| The stars are showing | A space inside the stars, or stars on one side only |
| There are two `]` or two `)` where you typed one | VS Code added the closing bracket, and you typed another after moving away. Delete one |
| The numbers in your list are not the ones you typed | Markdown counts for you, from the first number. `1.` three times is shown as 1, 2, 3 |
| Step 9: `mission.amd` is all one color | The add-on is off, or not installed. The marks are the same, so carry on. See "Before you start" |
| Step 11: the game does not start, or it starts on another mission | The `run` line. Type it as Lecture 3, Step 7, has it, and look in that lecture's "If something goes wrong" |
| Step 11: the right-hand side says `Select a quest from the list.` | Nothing is selected yet, or you clicked the line above First Contact. Click **Find the Derelict** |
| Step 11: the right-hand side shows one sentence, then `Find the Derelict` and `... more to follow` | You selected First Contact. That is its own sentence and a list of its steps. Select **Find the Derelict**, the line under it |
| Step 11: `State` says `Done`, and Find the Derelict is not the line straight under First Contact | The ship has been to the hulk, so the step is finished and has moved down the list. Select it by its name. The lines under `State` are the same |
| Step 11: the right-hand side shows the old sentence | You did not save `mission.amd` before you started the game. Close the game, press `Ctrl+S`, and start it again |

## Exercise

Write the story bible for a mission of your own. Make a second file, `my-story.md`, in the
same folder, and give it:

1. A title, with one hash.
2. One paragraph under the title: the story in two sentences.
3. Three headings, with two hashes: `## Premise`, `## People`, `## What happens`.
4. A list of at least three people. One line each: a name, a comma, and the one thing the
   crew should know about them.
5. A numbered list of three things that happen, in order.
6. One link, to a page that gave you the idea.
7. One bold word and one slanted phrase.

Then read it once more for the plain keyboard: straight quotes, plain hyphens, three
separate dots.

Last, open `mission.amd`, change nothing, and find: a line that is a heading, a line that
is a fence, a line that is a note, and a line that is a reading.

Keep `my-story.md`. The people become characters in Class 2. The three things that happen
become the steps of your first quest in Lectures 8 and 9.

## Checkpoint

You are done when all four are true:

- The preview of `story-bible.md` shows a title, three headings, a list of people, a
  numbered list and a link, with no mark left showing.
- `my-story.md` has the same parts, for your own story.
- You can point at a heading, a fence, a note and a reading in `mission.amd`, and say
  which of them would mean something else in markdown.
- `mission.amd` is exactly as it was when Lecture 3 ended. Line 31, its description of
  Find the Derelict, is one line: `Fly out and locate the drifting hulk.`

## Next

Lecture 5 (the shape of a record) takes three records of `mission.amd` apart, and you
type one of your own. It starts from the file as it is now.

## Further reading

- "The AMD file format" in the library documentation: "Headings" has the table of which
  marks a quest's description and a reading draw, and "Writing the body" has the marks
  that are AMD's own.
- "Markdown and Visual Studio Code" in the VS Code documentation: the preview, and the
  editor's other help for `.md` files.
- "CommonMark" (commonmark.org): the rules of markdown itself, with a ten-minute
  tutorial.
