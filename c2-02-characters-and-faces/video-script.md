# C2-2 video script - Characters and faces

> **STATE ON 2026-10-08. Read this first.**
>
> - **New lecture, written and measured today. Nothing in it has been seen on a screen.**
>   Not the Story Graph, not the Inspector, not the Face Builder, not a portrait in the
>   game. The first job before recording is to walk Steps 3 to 6 of the page in a real
>   VS Code and correct the page where a button or a list is not as described.
> - **The page is written for Artemis Cosmos 1.4.0** with a current tool, libraries and
>   the AMD add-on (0.9.4 was the one read).
> - **The student's mission is `MyMission`** as Lecture 1 of this class left it
>   (`c2-01-sides-and-factions\example\`). `example\` here holds the one file that
>   differs: `mission.amd`.

> **How each thing on the page is known.**
>
> - **Measured in the mock** (headless, packaged library, sbs_utils `ae2bbf4a`): the
>   template's line 48 makes a person from each record of a section keyed `characters`;
>   the face each person holds (a probe read it back from the game); every row of the
>   three tables in Step 8, one change at a time, lint and then the game.
> - **Measured by calling the library** (no game): the seven keywords and what any other
>   word does (`face_resolve`); that a keyword is rolled again on every call; that half of
>   4,000 rolls of `female` and `male` came up with a skin tint from the second half of
>   the Terran tone table (yellow, green, blue, pink); the slider names for each race
>   (`FACE_FEATURES`); that the builder's own functions rebuild a face from its string.
> - **Measured by calling the editor's language server** (the Python the add-on runs, no
>   window): the Inspector's form for `quill` has one field, `Face`, typed as a face,
>   which is what gets the **Face...** button; **Preview Node** on a character returns a
>   face, and for a keyword a new one on each call; the Story Graph's model has a section
>   `characters` with the three people in it.
> - **Rendered with the library's own face tool** (`_tools\face_render.py`, the same
>   compositing rule as the game, the game's own drawings) and LOOKED AT: the three face
>   strings on the page. Quill is a woman with brown hair up, in a tan uniform. Ives is a
>   man with ginger hair and orange eyewear, in a dark uniform. Sable is a red-skinned
>   Skaraan with a silver headpiece and a grey coat. Twelve keyword rolls were rendered
>   the same way: five had green, blue or violet skin.
> - **Read in the add-on's source** (`editors\vscode\src\extension.ts`,
>   `media\inspectorForm.js`, `package.json`, version 0.9.4) and NOT seen: every click in
>   Steps 3 to 6 and Step 9. In particular: a plain click on a box of the Story Graph
>   does not open the Inspector (the code only starts a drag); **right-click, Edit...**
>   does. The add-on has no Inspector docked in the Activity Bar, though its own help page
>   and the Open Universe tour both describe one.

> **Three things the page leaves out, and why.**
>
> - `Color:` on a character. It is read and kept, and a call in a mission like this never
>   uses it (measured in Lecture 3's runs: the call's color is empty).
> - `Roles:`, `Host:`, `Path:`, `Scene:` on a character. They belong to missions that put
>   people on a ship's Comms list, which this template does not do.
> - The in-game Avatar Editor. Nobody here has opened it. It is one line of "Further
>   reading".

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyMission` as Lecture 1 leaves it. `mission.amd` has 233 lines and ends with the Harbor Guild's description |
| Lint | `sbs lint MyMission` says `clean` |
| VS Code | `MyMission` folder open and trusted, the AMD add-on installed, `mission.amd` in one tab scrolled to the end. Font size raised. Word wrap as the viewer will have it: off, so that a face string runs off the right edge, and scene 8 can say so |
| The game's drawings | The mission folder is inside the game's own `data\missions`, so the add-on finds `data\graphics` and draws the portraits |
| Command prompt | Open in `data\missions`, cleared |
| Game | Not needed. Scene 10 can show it running to prove nothing has changed |

## Confirm on camera

If an item fails while recording, stop and fix the page.

Measured, and expected to hold:

1. Lint is `clean` after Step 1, and after each person is typed, with a keyword or with a
   face string.
2. The game makes three people, keyed `quill`, `ives` and `sable`, each holding the face
   string in the file, letter for letter.
3. With `Face: female` the game holds a different face string in two games.
4. Every row of the tables in Step 8.

Read in the source and never seen. Check each one before recording:

1. `Ctrl+Shift+P`, `story graph`: the command is listed as **Artemis AMD: Show Story
   Graph** and opens a tab beside the file.
2. The graph has a band for `characters` with three boxes. What the band is labelled.
3. Right-click a box: the menu has **Edit...**, and it opens a tab titled **AMD
   Inspector**.
4. The Inspector shows a `Face` box, a **Face...** button and a portrait.
5. **Face...** opens a list at the top of the window with these entries, in this order:
   Build custom..., Paste from Avatar Editor, female (keyword), male (keyword), Random
   Terran (female), Random Terran (male), Random Skaraan, Random Torgoth, Random Arvonian,
   Random Kralien, Random Ximni. (In the add-on the first entry ends with a single
   ellipsis character. The page types three dots.)
6. Choosing a **Random** entry rewrites the `Face:` line in `mission.amd` without a save,
   and the portrait changes.
7. Clicking the portrait opens **AMD Face Builder**, started from the face in the file.
   The sliders for a Terran are the eleven the page lists. Moving one rewrites the line.
8. What the Inspector draws for a KEYWORD. The code hands the word `female` to the
   drawing routine as if it were a face string. It may draw nothing.
9. **Artemis AMD: Preview Node** with the cursor in a character's record opens a tab with
   the portrait and the name.
10. What the real game draws for a face that is not one (`Face: woman`). Nobody knows.
    This one needs Lecture 3's call to be seen at all.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The Face Builder beside `mission.amd`. A slider moves, and the portrait and
the `Face:` line change together. Then three portraits side by side: Quill, Ives, Sable.

**Say:** "Your map has sides now, | but there's nobody on them. || Today we fix that. ||
We're going to write three people, | and give each of them a face. ||| It's one new
section in your fact sheet, | and you won't touch the story file at all. ||"

### 2. One person

**Screen:** `story.mast`, line 48 highlighted. Then `mission.amd`, the end of the file. Two
blank lines. Type the note, the section line, and Quill's record with `Face: female`.
Save. Command prompt: `sbs lint MyMission`, clean.

**Say:** "First, one line of the story file, just to read. || In Lecture 11 this line was
marked for Class 2. || It makes a person from every record of a section called characters,
| so that's the key my section needs. ||| Now the section itself is two hashes, the word
Characters, and that key. || Then the person, with three hashes, | her name, and her key
in round brackets. || Inside the fence there's one line, | Face, and the word female. ||
And below the fence there's a sentence about her, | which is a note for me. || I save, I
run lint, and it's clean. ||"

### 3. What one word gets you

**Screen:** The keyword table on the page. Then two different rolled women side by side,
one of them with green skin.

**Say:** "That word female is called a keyword, | and there are seven of them, all for
humans. || But a keyword doesn't choose a face. | It asks the game to roll one. ||| So
every time the game starts, | she gets new eyes, new hair and new clothes. || And about
half the time she gets skin that's green or blue. || That's fine for a voice the crew
hears once. || But it's wrong for a person with a name, | because your crew should know
her when she calls again. ||"

### 4. A face that stays

**Screen:** `Ctrl+Shift+P`, type `story graph`, Enter. The graph tab. Find the characters
band. Right-click Harbormaster Quill, choose Edit. The AMD Inspector tab. Click the Face
button. The list. Choose Random Terran (female). Cut to `mission.amd`: the long line.

**Say:** "To keep a face, the line has to spell it out, | and I'm not going to type that
myself. || I press Control, Shift and P, | which opens a box that runs any tool the editor
has. || I type story graph, and press Enter. ||| Here are my records, drawn as boxes, |
with one band for each section. || I right-click Quill's box, and I choose Edit. || This
tab is the Inspector, | and it shows her record as a form. || Beside her face there's a
button, so I click it, | and from the list I choose a random Terran woman. ||| Now look at
my file. || The keyword is gone, | and in its place there's one long line. || That line is
her face, written down. ||"

### 5. Change one thing

**Screen:** In the Inspector, click the portrait. The AMD Face Builder tab. Point at Race,
the sliders, a tick box, the Face string box. Drag Hair: the portrait and the line in
`mission.amd` change. Back to the file. `Ctrl+S`.

**Say:** "A roll gets me close, | and the builder gets me the rest of the way. || I click
her picture, and the Face Builder opens, | starting from the face she already has. ||
There's a slider for each feature: | eyes, mouth, hair, clothes and so on. || And a tick
box beside some of them | turns that feature off altogether. ||| So I move the hair, | and
her line in my file changes while I drag. || There's nothing to press. || When she looks
right, I go back to the file and I save. ||"

### 6. The second person

**Screen:** Type Chief Ives with `Face: male`. Save. Graph: right-click his box, Edit,
Face, Random Terran (male). The line in the file.

**Say:** "The second one goes faster. || I type Chief Ives below her, | with the keyword
male, and I save. || The graph has already drawn a box for him. || So it's right-click,
Edit, the face button, | and a random Terran man. || If I don't care for him, I roll
again. ||"

### 7. Someone who is not human

**Screen:** Type Captain Sable with `Face: female`. Save. Graph: right-click, Edit, Face,
Random Skaraan. Then open the builder and show the Race box with its six entries.

**Say:** "My third person flies the Breaker Cutter, | and she doesn't have to be one of
us. || The game has six peoples, | and only the humans have keywords. || For the other
five there's no word to type, | so the editor is the only way in. ||| I type her record
the same way, | and this time, from the list, I choose a random Skaraan. || And in the
builder, this box at the top is her race. ||"

### 8. Four rules

**Screen:** `mission.amd`, the three face strings. Show one running off the right edge.
Then, on a copy: press Enter in the middle of Sable's string, save, lint: the
`fence-syntax` error. `Ctrl+Z`. Lint: clean.

**Say:** "You'll copy these lines and move them about, | and they break easily, so here
are four rules. || A face string is one line, however long it is. || You keep all of it,
down to the last semicolon. || You put no quote marks round it. || And you change it with
the builder, never by hand. ||| Here's what the first rule looks like when it's broken. ||
I press Enter in the middle, | and lint gives me an error on the second half. || That's
the only one of the four that lint can see, | so the other three are yours to watch. ||"

### 9. What lint cannot see

**Screen:** Change Quill's line to `Face: woman`. Save. Lint: clean. Show the table "What
lint cannot see" on the page. `Ctrl+Z`.

**Say:** "And now the one that will catch you. || I write Face, woman, | which looks just
as good as female, | and lint says clean. ||| But woman isn't one of the seven words, | so the
game doesn't roll anything. || It takes the word itself as her face, | and that's no face
at all. || Lint knows where a person's record belongs. | It doesn't read what comes after
Face. || So that part you check with your own eyes. ||"

### 10. Look at them

**Screen:** Click inside Quill's record. `Ctrl+Shift+P`, `preview node`, Enter: her
portrait. The same for Ives and for Sable.

**Say:** "Nobody speaks yet, so the game has nothing new to show. || But I can look at my
cast right here. || I click inside her record, | I open that box again, and I type preview
node. || There's Quill, and she'll look like that in every game from now on. || And
there's Ives, and there's Sable. ||"

### 11. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn: add a fourth person of your own, | from a people you haven't
used. || Roll a face, and then change two things about it in the builder. ||| Next time,
the harbormaster picks up the microphone. ||"
