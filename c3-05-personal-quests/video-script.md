# C3-5 video script - Personal quests

> **STATE ON 2026-10-09. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0 from
>   Steam or itch.io, with a current tool and libraries.
> - **Starts from Lecture 4's finished files** in `MyBoarding`. Both files change, so
>   `example\` holds `mission.amd` and `story.mast`.
> - **One card, changed once.** The student adds `stories=...` to the end of the
>   `boarding_visit` line of Lecture 2's card. There is no second card.
> - **`Leads to:` is not taught here.** It points at a thing on a map, and a place made of
>   rooms has none. Lint is silent about it. It is on the page as a note.

> **Measured 2026-10-09, in the mock.** Tool `sbs` as installed, library as packaged
> (sbs_utils `ae2bbf4a`). The steps were typed onto Lecture 4's files and linted at each
> one. The finished files were played headless with stand-in consoles: two aboard, the
> engineer alone, and the surgeon beaming down late. Then 40 one-change variants, each
> linted and played. No engine, no window.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyBoarding` with Lecture 4's files. Lint clean |
| VS Code | `MyBoarding` folder open, `mission.amd` and `story.mast` in two tabs |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 7 with a server, Helm, Engineering and Science |

## Confirm on camera

1. After Step 1 lint prints the two warnings on the page; after Step 2 only the first;
   after Step 3 it is `clean`, and it stays clean. (Lint.)
2. With both aboard, Six Names is held by Dr Hale and A Cold Core by Chief Okoro, both
   active; each handheld has three apps, Crew, Act and Tasks. (Mock.)
3. Dr Hale's reading of the tags completes Six Names and Account for the Crew at one
   press, and the side's credits go from 100 to 250. Chief Okoro's reading completes A
   Cold Core. The ship is told `Quest complete:` for each. (Mock.)
4. The engineer alone: Six Names is handed to nobody; the covered reading teaches the
   fact and Account for the Crew stays active; A Cold Core still completes. (Mock.)
5. The surgeon beaming down after the engineer is handed Six Names when she arrives.
   (Mock.)
6. Every row of the page's tables. (Lint, Mock.)

Seen on a real screen by the earlier pilot, with three real consoles: the Tasks app on
the surgeon's handheld and its list, Six Names marked Active with the ship's quests under
Party.

Not seen by anyone. If one is not as described, stop and fix the page:

1. This rewrite's files in the real game.
2. The two `Quest complete:` lines on a bridge console as the reading is taken.
3. The Back button's place on the handheld.
4. Account for the Crew in the Quest Log: the heading, and the person and
   tablet icons as the two bullets.

## Scenes

### 1. Cold open

**Screen:** The Science console's handheld with the Tasks app open: one story under Dr
Hale's name. Then the airlock, and her reading.

**Say:** "Everyone in this party reads the same room. || But one of them came aboard with
a question of her own, | and it's listed on her handheld, under her name. ||| Whose suits
are these? || Today you give one person a quest that's theirs, | and you make it lead
somewhere. ||"

### 2. A section for side stories

**Screen:** The Science console's handheld again, its Tasks app: Six Names under Dr
Hale's name, and under Party the ship's quests. Then `mission.amd`, the end of the file.
Type the Side Stories heading and Six Names. Highlight `For: medical`. Lint: two warnings.

**Say:** "This is the doctor's handheld, aboard the hulk, | with its Tasks app open. || The
row under her name is a side story, | and the rows under Party are the ship's quests. |||
A side story is a quest. || It has the fields you learned in Class 1, | and it
lives in a section of its own, at the end of the file. ||| What's new is this line. | For,
and then a job. || A quest in your Quests section belongs to the whole ship. | This one
belongs to one person. ||| It starts at once, | it has an objective, | and it's done when
a signal arrives. Lint warns twice, | and both warnings are true for now. | Nothing sends
that signal yet, | and nothing hands the story out. || The word after For is a job from
your roster, | or it can be a person: their key, or their name. ||"

### 3. Her own reading finishes it

**Screen:** The airlock on the Science console's handheld: Read the name tags on the
suits. Then `mission.amd`, The Airlock. On the surgeon's choice, add a comma and
`signal names_read` after `learn suits`. Lint: one warning left.

**Say:** "So first, the signal. || On the doctor's handheld, in the airlock, | her reading
is the button that should finish her story. ||| In the file I find that choice, the one
only the surgeon is offered, | and I
add a second outcome after the first, | with a comma between them. Learn the fact, comma,
send the signal. || The name has to match the story's, letter for letter. || And don't
lose that comma. | Without it, the signal is never sent. ||"

### 4. Hand the stories to the visit

**Screen:** `story.mast`, the card at the end. On the `boarding_visit` line, type the
`stories=` part before the last bracket. Lint: clean. Then the doctor's handheld with its
three apps.

**Say:** "Then the handing out. || I open the story file | and find the card from Lecture
2. || One line on it starts the visit, | and I add a few words to the end of that line.
Stories equals, | and then the section of the fact sheet to read them from. || The key in
quotes is the key on my Side Stories heading. ||| That's the whole change. || From now on
each person is handed their story as they beam down, | and that includes someone who beams
down late. ||"

### 5. A second story, and where one leads

**Screen:** The Engineering console's handheld, its Tasks app: A Cold Core under Chief
Okoro's name. Type A Cold Core, and add its signal to the engineer's choice. Then add
`Then: signal names_known` to Six Names. Helm's handheld, the Quest Log: Account for the
Crew's page. Type Account for the Crew in the Quests section, with its heading and two
icon bullets. Draw the chain with the cursor: the choice, the story, the ship's quest.

**Say:** "The engineer gets one too. || Here it is on his handheld, under his name, | and
it's finished by his own reading. ||| And a side story
can lead on, | the same way any quest does, with Then. || When the surgeon's story
completes, it sends a second signal, | and a quest for the whole ship is waiting to hear
it. ||| So read the chain from the top. | She reads the tags. | That finishes her story. |
Her story finishes the ship's quest, | and the ship is paid. || A story can carry a reward
of its own as well, | and it's paid to the ship that person came from. |||
The ship's quest gets a page, | because the Quest Log shows all of it. || This is the
Quest Log on Helm's handheld. | A heading, and two bullets with a small picture for a dot.
|| In the file, the word after icon names the picture. ||| The side story stays short. | Tasks only shows its heading. ||"

### 6. Four rules, and lint

**Screen:** The four rules on the page. Then the command prompt: lint, clean. Change
`For: medical` to `For: medcal`, lint, undo. Remove the comma before `signal`, lint, undo.

**Say:** "Four rules. A side story is a bonus, and never the only way, | because nobody
covers for a person. || One job word goes in three places: | the roster, the story, and
the choice that finishes it. || For takes one job, or one person. || And one story goes to
one person. ||| Lint is good here. | It tells you when a story is for nobody, | and it
tells you when two outcomes have run together. ||"

### 7. Play it

**Screen:** `sbs run server,helm,engineering,science -m MyBoarding map=0`. Two plays,
each with Helm left on the bridge to watch. First the surgeon goes alone: on Science,
Back, the three apps, Tasks, Six Names. Back, Act. She reads the tags; the ship's log
line on Helm. Then the engineer goes alone: the suit tags offered to him, marked as
covering; he reads them; Account for the Crew still Active in Helm's Quest Log. Aft; he
reads the record; Helm's log line.

**Say:** "I play it twice, and each time Helm stays on the bridge to watch. || First the
doctor goes across. | On her handheld I go back one step, | and there are three apps now,
| and the third one is Tasks. || There's her story, under her name. ||| She reads the
tags, | and the bridge is told twice: | her story is complete, and so is the ship's
quest. ||| Then the chief goes across alone, | and that's a short crew. || He's offered
her reading, marked as covering, | and the party learns the fact. || But her story was
never handed out, | so the ship's quest stays open. ||| Then he reads his own record,
and his story completes. || The next lecture shows you the way round that open quest.
||"

### 8. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Write a story for your third person, | finished by their own reading. || Give
the chief's story somewhere to lead. Then break it. | Misspell the job after For, | read
what lint says, | and play it once anyway. ||| Next time is the checkpoint: | one away
scene of your own, planned on paper and played. ||"