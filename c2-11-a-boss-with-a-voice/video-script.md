# C2-11 video script - Capstone: a boss with a voice

> **STATE ON 2026-10-10. Second version: the boss file carries its own cast and scenes.**
>
> - Everything the page needs is released. The page is written for Artemis Cosmos 1.4.0
>   from Steam or itch.io.
> - **Starts from Lecture 10's finished files** (`c2-10-siege-boss-quests\example\`: the
>   boss file and the hook's folder). `example\` here holds the one file that differs,
>   `corsair_queen.amd`. The card is Lecture 10's, unchanged.
> - **WHAT CHANGED FROM THE FIRST VERSION.** The first version taught that a boss file
>   could not hold a cast or a scene, and worked round it with a second file
>   (`voice.amd`) and three lines on the card. Siege now reads a boss file's own
>   `## [Characters](characters)` and `## [Dialogue](dialogue)` sections when that boss
>   arrives. So the second file and the three card lines are gone, Step 4's table of what
>   one file cannot hold is gone, and "Hand her to a friend" now says that the one file
>   carries everything but the arrival sentence and the reserve ship. Nothing else in the
>   lecture changed: the clock, the Beat, the answer that turns the Badb, the rubric.
> - **One lint warning is still taught as wrong.** `Speaker: morrigan` on a boss objective
>   lints `dangling-speaker` ("not in the cast"), with or without a Characters section in
>   the file (measured both ways). In the game the role resolves to the ship and she
>   speaks. `Speaker: queen`, the person, lints `clean`, and in the stand-in the warning
>   then goes out under the crew's own ship's name, so the page keeps `morrigan` and says
>   why.
> - **Measured**, in a sandbox that is a small missions folder of its own (a copy of
>   LegendaryMissions in the shape `sbs fetch` leaves, taken from the released tree, its
>   own `common_data\bosses`, a copy of the packaged libraries for lint): every stage of
>   the lesson linted (bosses folder, then LegendaryMissions), three stage plays, and 37
>   one-change variants, each linted and each played as a headless Siege, one at a time,
>   with a stand-in Comms console that opens the call and chooses answers, and a tap on
>   everything sent to the crew's ships. Library sbs_utils `ae05dac7`, LegendaryMissions
>   `b37a320`, as packaged.
> - **2026-10-15, for the video:** scenes 2, 5, 6, 8 and 9 show each thing in the game first
>   (Comms: the Morrigan's message, Incoming Hails, the open call, Orla's answers; the Quest
>   Log on Helm's handheld), then the line that makes it. The storyboard is
>   `narration\storyboard.py`.
> - **Not run in the real game.** Siege with the shipped bosses has been booted on the
>   real server. Nobody has seen a call, a face, or a message from the Morrigan on a
>   console.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Boss file | `common_data\bosses\corsair_queen.amd` exactly as Lecture 10's `example\` |
| Hook folder | `LegendaryMissions\corsair_queen\__init__.mast` exactly as Lecture 10's `example\`. Nothing else in the folder |
| VS Code | The `data\missions` folder open, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started with `sbs run server,helm,comms -m LegendaryMissions`, Difficulty 5 |
| `mast.runtime.log` | In `LegendaryMissions`, empty or deleted |

## Confirm on camera

"Lint" is the installed tool. "Mock" is a headless Siege from the sandbox copy.

1. With the two lines of Step 2 and a three-minute limit, Comms is sent three messages
   from the Morrigan, titled `Sink the Morrigan`: `You have 1:59, little ship. Then this
   sector is mine.` (the engine, 2026-10-15: `2:00`), then `1:00` or `0:59`, then `0:29`. (Mock: `1:00` in one game, `0:59`
   in another. A 45-second limit sent one, `0:30`.)
2. `sbs lint common_data\bosses` prints the one `dangling-speaker` warning, on line 35,
   before and after the file has a Characters section. (Lint.)
3. With the Beat typed and no scene: a second warning, `dangling-action-ref`, on line 93;
   in the game no call, and `mast.runtime.log` says there is no dialogue scene called
   `queen_calls`. (Lint, Mock.)
4. With the two sections at the end of the file: lint is back to the one warning. A call
   titled `The Corsair Queen - The Corsair Queen` is waiting on Comms a few seconds after
   she arrives; opened, it is spoken under the name The Corsair Queen. No line was added
   to the card. (Lint, Mock: the row the Comms list is built from.)
5. `Then fly with us.`: the crew is told `Quest complete: The Queen Calls`, `Quest
   complete: Turn the Badb`, `Quest failed: Sink the Badb`; the Badb's side becomes `tsn`;
   `Quest complete: The Badb Turns` follows about eight seconds later. (Mock.)
6. `We do not stand down.` and `Then stay out of our way.` finish The Queen Calls and
   change nothing else. (Mock.)
7. Nobody answers: the game is still won, with 1,100 credits. The Badb turned and the
   Morrigan sunk: 1,100 as well. (Mock. The 1,400 and 1,500 rows of the page's table are
   from the first version's games and were not played again.)
8. The boss file alone, with no folder: the Morrigan still calls the clock, the Queen
   still calls and the answer still turns the Badb; no arrival sentence, no Nemain;
   lint prints two warnings. (Lint, Mock.)
9. Every row of the three tables in Step 9. (Lint on each; Mock on each.)
10. **What the Badb does after she changes sides is not known.** The mock shows her side.
    Whether she fights the raiders, sits still, or is shot by them needs the real game.
11. Unseen, all of it: the call on a Comms console, the Queen's face, the message from the
    Morrigan, where on Comms a message with a title is shown, the Quest Log with two
    Beats in it, and the objectives' pages (a 3D ship at the top, the icon bullets, the
    paragraphs; read in the library's text area code only).

Also capture the screenshot the page asks for.

## Scenes

### 1. Cold open

**Screen:** The game, a Comms console. A call from The Corsair Queen, her face, two
answers. (Reuse footage from scene 9.)

**Say:** "This is the last lecture of the class, | and it puts the whole class together. ||
You have a boss, with ships and objectives and a hook. | And you know how to write a
scene, a call, and an answer. ||| Today, at last, she speaks. || And all of her voice goes in the one
file you already have. ||"

### 2. Her voice on the clock

**Screen:** The game first: Comms, the message from the Morrigan titled Sink the Morrigan (from
scene 4). Then `corsair_queen.amd`, the fence of Sink the Morrigan. Add `Speaker: morrigan`
and the `Signal says:` line under `Lose:`.

**Say:** "Last time, the crew had ten minutes to sink the Morrigan, | and nothing warned them as the time ran down. || Here's the warning we're about to make: | a
message on Comms from the Morrigan, | with the objective's name as its title. || Two lines
in her file make it. || Speaker says who gives the warning, |
and here it's a role: the name of her flagship, in small letters. || Signal says is what
she sends. ||| Where I write the word time, in curly brackets, | the game puts in the time
that's left. || It's sent at five minutes, at two, at one, and at thirty seconds, | and
only the ones that fit inside your limit. ||"

### 3. The one warning you keep

**Screen:** Command prompt: `sbs lint common_data\bosses`. One warning, ending
`dangling-speaker`.

**Say:** "Now run lint, and it complains. || It says morrigan isn't in the cast. ||| And
here, that warning is wrong. || Lint's looking for a person, in a Characters section, | and
the Morrigan is a ship. || The game looks for a character first, | and then for a
ship wearing that role, and it finds her. || So this is the only warning in the whole
course that I'll tell you to keep. || Read it every time, though. | If the name in it
isn't on your Named line, then it's true. ||"

### 4. Hear her

**Screen:** Start the game with a Comms console. She arrives. A minute later, a message
from the Morrigan on Comms: its header `Morrigan (pirate)` at the top, clicked to read it.

**Say:** "For testing, I've set the limit to three minutes. || She arrives, and I do
nothing. || About a minute later, Comms gets a message from the Morrigan, | with the
objective's name as its title. ||| You have two minutes, little ship. | Then this
sector is mine. || That's her voice, in my words, | and it's in the one file. || If I
send that file to a friend, they hear it too. ||"

### 5. Place the call

**Screen:** The game first: Comms, Incoming Hails with the row The Corsair Queen - The Corsair
Queen (from scene 9). Then the end of `corsair_queen.amd`. Type the Beat The Queen Calls. Command prompt:
`sbs lint common_data\bosses`. Two warnings; highlight `dangling-action-ref`.

**Say:** "Now for the call itself. || On Comms it waits in Incoming Hails, | under her name and
the title I give it. || You know the three parts from your own mission: | a Beat that
places it, a cast, and a scene. || All three go in the boss file, | and I start with the
Beat. ||| It has an Action line that says, queen hails, and a scene's key. || I run lint, and there's a second warning, | and this one is true. || The Beat names a scene that nobody
has written yet, | so right now, no call would come. ||"

### 6. Her people and her scene

**Screen:** The game first: Comms, the Queen's call open: her face, her name, her offer, the
answer (from scene 9). Then the very end of the file. Type `## [Characters](characters)` with the Queen
and First Mate Orla, then `## [Dialogue](dialogue)` with the scene The Queen Calls. Lint:
back to one warning.

**Say:** "Here's the call opened on Comms: | her face, her name, her offer, and an answer. || To
make it, I go to the very end of the file, | and I type two sections you already know.
|| Characters, with the Queen and her first mate. || And Dialogue, with one scene. ||| The
sections have two hashes, like her objectives, | and the people and the scenes inside
them have three. || The scene is just what you wrote in Lecture 3: | a speaker, two
blocks of takes, and an answer. || That answer finishes the Beat. ||| I run lint again, and the warning about the call has gone. ||"

### 7. What the Siege does with her file

**Screen:** The table in Step 6 of the page. Then the card, `__init__.mast`, open and
untouched.

**Say:** "There's nothing to paste for this. || When she arrives, the Siege reads her file
itself. || Her objectives go to the crew, | her people come into the game, | and her
scenes are made ready to be called. ||| Two things follow from that. || Her people don't
exist until she arrives, | which is fine, because her Beats don't either. || And her card
isn't part of this at all. || It still brings the third ship, | and I haven't added a line
to it. ||"

### 8. An answer that matters

**Screen:** The game first: Comms, First Mate Orla's line and her two answers. Then in the
Dialogue section, the second answer and the scene The Badb Answers.
Then the Quest Log on Helm's handheld with The Badb Turns, then, above
`## [Characters](characters)`, the records Turn the Badb and The Badb Turns.

**Say:** "Now I make an answer matter. || Here's where it ends up on Comms: | First Mate Orla on
the line, with two answers of her own. || A second answer leads to a second scene, | where
the Badb's first mate comes on the line. || And if the crew says, then fly with us, | three things happen after the semicolon. ||| First, the call is finished. || Turn the Badb is finished,
which reveals one more step. || And that step has an Action of its own: | badb joins
T S N. || So the ship changes sides. || In the Quest Log, on Helm's handheld, | The Badb Turns appears,
with her ship drawn at the top. ||| Notice where I typed those two records: | among
her objectives, above the Characters line. || Her people and her scenes stay last in the
file. ||"

### 9. Play every road

**Screen:** Both lint commands. Then the game: the call waiting, the Queen's face,
Continue, the Badb's answer, "Then fly with us." The strip on Helm (one line at a time:
`Quest complete: The Badb Turns`). The Quest Log: The Queen Calls, Turn the Badb and The Badb
Turns Done, Sink the Badb Failed. Then a second game: "We do not stand down."

**Say:** "Check both, and then play it. || On Comms, there's her call, waiting in Incoming Hails, | with her name and the title. || I open it, she makes her offer, | and I talk to the Badb instead. ||| I choose, then fly with us. || Helm shows it one line at a time, | and the last line
says, the Badb turns. || In the Quest Log, the call is done, the Badb has turned, | and the
bonus for sinking her has failed. || That's a real choice for the crew: | three hundred credits, or one raider fewer. || Then play it again and refuse her, | and play it a third time and never answer
at all. || The game has to be winnable on every road. ||"

### 10. Hand her to a friend

**Screen:** VS Code's file list: `common_data\bosses\corsair_queen.amd`, then the
`corsair_queen` folder in LegendaryMissions with its one file. The page's table.

**Say:** "Now, what are you handing over? || Nearly all of her is the one file. || Send
just that one file, | and your friend gets the boss, her ships, her objectives, | the Morrigan
calling the clock, | and the Queen's call with the answer that turns the Badb. ||| What
they don't get is the arrival line and the reserve ship. || Those two are her card, | and the card lives in a folder inside Legendary Missions. || An update removes that folder, for
them and for you. || So keep a copy outside the game. || Lint will tell you: one warning
when the folder's there, | and two when it isn't. ||"

### 11. The rubric, and what comes next

**Screen:** The rubric on the page, scrolled slowly.

**Say:** "The page ends with a rubric, | and every line on it is something you can check
yourself. || She's yours, she's checked, she plays, and she travels. ||| When every line
is ticked, you've finished Class 2. || You can write a cast, a conversation, | and a boss
who talks back. || In the next class, the crew leaves the bridge. ||"
