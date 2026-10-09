# C2-11 video script - Capstone: a boss with a voice

> **STATE ON 2026-10-08. First version of this lecture.**
>
> - Everything the page needs is released. The page is written for Artemis Cosmos 1.4.0
>   from Steam or itch.io.
> - **Starts from Lecture 10's finished files** (`c2-10-siege-boss-quests\example\`: the
>   boss file and the hook's folder). `example\` here holds all three finished files.
> - **THE HEADLINE FINDING.** A boss cannot hold a cast or a scene in her one file. Siege
>   reads a boss file for the boss's own lines and for quests, and nothing else: a
>   Characters or Dialogue section typed into it is handed to the crew as quests (six idle
>   jobs, measured), lint says nothing about it, and no call is placed. A call needs a
>   second `.amd` and two lines of MAST to read it, and the only place both can go is a
>   folder inside LegendaryMissions, which an update of LegendaryMissions deletes (the
>   plan's B87, still open). So the capstone is written in two parts: what the one file
>   carries (her words, and the Morrigan calling the clock with `Speaker:` and `Signal
>   says:`), then the call, which needs the folder. "Hand her to a friend" says what plays
>   from one file and what needs the folder.
> - **One lint warning is taught as wrong.** `Speaker: morrigan` on a boss objective lints
>   `dangling-speaker` ("not in the cast"). In the game the role resolves to the ship and
>   she speaks. The finished boss file therefore lints with one warning, and the page says
>   so, prints it, and says when it would be true.
> - **Measured**, in a probe that is a small missions folder of its own (a copy of
>   LegendaryMissions in the shape `sbs fetch` leaves, its own `common_data\bosses`, a
>   copy of the packaged libraries): the lesson's stages typed in order and linted, and
>   57 headless Siege games, one at a time, with a stand-in Comms console that
>   opens the call and chooses answers, and a tap on everything sent to the crew's ships.
> - **Not run in the real game.** Nobody has seen a call, a face, or a message from the
>   Morrigan on a console.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Boss file | `common_data\bosses\corsair_queen.amd` exactly as Lecture 10's `example\` |
| Hook folder | `LegendaryMissions\corsair_queen\__init__.mast` exactly as Lecture 10's `example\`. No `voice.amd` yet |
| VS Code | The `data\missions` folder open, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started with `sbs run server,helm,comms -m LegendaryMissions`, Difficulty 5 |
| `mast.runtime.log` | In `LegendaryMissions`, empty or deleted |

## Confirm on camera

"Lint" is the installed tool. "Mock" is a headless Siege from the probe copy.

1. With the two lines of Step 2 and a three-minute limit, Comms is sent three messages
   from the Morrigan, titled `Sink the Morrigan`: `You have 1:59, little ship. Then this
   sector is mine.`, then `0:59`, then `0:29`. (Mock. A 45-second limit sent one, `0:30`.)
2. `sbs lint common_data\bosses` prints the one `dangling-speaker` warning, on line 35.
   (Lint.)
3. A Characters and a Dialogue section typed into the boss file: no finding about them,
   no call, and six extra quests in the idle state. (Lint, Mock.)
4. With `voice.amd`, the three lines first on the card, and the Beat: a call titled `The
   Corsair Queen - The Corsair Queen` is waiting on Comms a few seconds after she arrives.
   (Mock: the row the Comms list is built from. The call was still in the ship's queue 75
   seconds later. The harness's stand-in console stopped listing it after about 20
   seconds in LegendaryMissions; that is the stand-in, and a real console is unseen.)
5. With the three lines pasted after the wait: no call, and `mast.runtime.log` says there
   is no dialogue scene called `queen_calls`. (Mock.)
6. `Then fly with us.`: the crew is told `Quest complete: The Queen Calls`, `Quest
   complete: Turn the Badb`, `Quest failed: Sink the Badb`; the Badb's side becomes `tsn`;
   the raiders counted drop from 25 to 24; `Quest complete: The Badb Turns` follows.
   (Mock.)
7. `We do not stand down.` and `Then stay out of our way.` finish The Queen Calls and
   change nothing else. (Mock.)
8. Nobody answers: the game is still won, with 1,100 credits. (Mock.)
9. The boss file alone, with no folder: the Morrigan still calls the clock; no sentence,
   no Nemain, no call; lint prints three warnings. (Lint, Mock.)
10. Every row of the two mistake tables in Step 9. (Lint on each; Mock on each.)
11. **What the Badb does after she changes sides is not known.** The mock shows her side
    and the count. Whether she fights the raiders, sits still, or is shot by them needs
    the real game.
12. Unseen, all of it: the call on a Comms console, the Queen's face, the message from the
    Morrigan, where on Comms a message with a title is shown, the Quest Log with two
    Beats in it.

Also capture the screenshot the page asks for.

## Scenes

### 1. Cold open

**Screen:** The game, a Comms console. A call from The Corsair Queen, her face, two
answers. (Reuse footage from scene 9.)

**Say:** "This is the last lecture of the class, | and it puts the whole class together. ||
You have a boss, with ships and objectives and a hook. | And you know how to write a
scene, a call, and an answer. ||| Today, at last, she speaks. || And along the way, you'll find the
one hard limit in everything you've learned so far. ||"

### 2. Her voice on the clock

**Screen:** `corsair_queen.amd`, the fence of Sink the Morrigan. Add `Speaker: morrigan`
and the `Signal says:` line under `Lose:`.

**Say:** "Last time, the crew had ten minutes to sink the Morrigan, | and nothing warned
them as the time ran down. || Two lines fix that. || Speaker says who gives the warning, |
and here it's a role: the name of her flagship, in small letters. || Signal says is what
she sends. ||| Where I write the word time, in curly brackets, | the game puts in the time
that's left. || It's sent at five minutes, at two, at one, and at thirty seconds, | and
only the ones that fit inside your limit. ||"

### 3. The one warning you keep

**Screen:** Command prompt: `sbs lint common_data\bosses`. One warning, ending
`dangling-speaker`.

**Say:** "Now run lint, and it complains. || It says morrigan isn't in the cast. ||| And
for a boss file, that warning is wrong. || Lint's looking for a Characters section, | and
a boss file hasn't got one. || The game looks for a character first, | and then for a
ship wearing that role, and it finds her. || So this is the only warning in the whole
course that I'll tell you to keep. || Read it every time, though. | If the name in it
isn't on your Named line, then it's true. ||"

### 4. Hear her

**Screen:** Start the game with a Comms console. She arrives. A minute later, a message
from the Morrigan on Comms.

**Say:** "For testing, I've set the limit to three minutes. || She arrives, and I do
nothing. || About a minute later, Comms gets a message from the Morrigan, | with the
objective's name as its title. ||| You have one fifty-nine, little ship. | Then this
sector is mine. || That's her voice, in my words, | and it's in the one file. || If I
send that file to a friend, they hear it too. ||"

### 5. What one file can't hold

**Screen:** The page's table for Step 4. Then, briefly, a boss file with a Characters
section typed into it, and a quest list with odd entries.

**Say:** "So you'd think the call goes in that file as well. || A Characters section, a
Dialogue section, and a Beat to place the call. ||| It doesn't work, and I want you to
see why. || The Siege reads a boss file for two things: | the boss's own lines, and
quests. || Everything under the boss is treated as a quest. || So your cast and your
scenes turn up in the crew's quest lists, as jobs, | and no call ever comes. || And lint
doesn't say a word. ||"

### 6. Her voice file

**Screen:** VS Code. Right-click `LegendaryMissions\corsair_queen`, New File, `voice.amd`.
Type the Characters section and the scene.

**Say:** "So her cast and her scenes get a file of their own, | in the folder you made
last time. || It's a small mission file. || It has a title line, | a Characters section with
the Queen in it, | and a Dialogue section with one scene. ||| The scene is exactly what
you wrote in Lecture 3. | A speaker, two blocks of takes, and an answer. || And that
answer finishes a quest called parley, | which we haven't written yet. ||"

### 7. Three lines on the card

**Screen:** Open `__init__.mast`. Paste the three lines directly under the label line.

**Say:** "Something has to read that file, and that's her card. || Three lines, and you
copy them as they are. || The first opens the file. | The second brings its people into
the game, | and the third makes its scenes ready to be called. ||| You've seen the last
two before, | because your own mission's story file has them. || One rule: they go first,
right under the label. || The call is placed the moment she arrives, | so the scenes have
to be read before anything waits. ||"

### 8. Place the call, and make an answer matter

**Screen:** At the end of the boss file, type The Queen Calls. Then, in `voice.amd`, the
second answer and the scene The Badb Answers. Then the records Turn the Badb and The Badb
Turns.

**Say:** "The call is placed the way you placed one in Lecture 5: | a Beat, with an Action
line that says, queen hails, and the scene's key. || It goes in the boss file, | because
that's where her quests are. ||| Now the answer that matters. || A second answer leads to
a second scene, | where the Badb's first mate comes on the line. || And if the crew says,
then fly with us, | three things happen after the semicolon. || The call is finished. |
Turn the Badb is finished, which reveals one more step. | And that step has an Action of
its own: | badb joins T S N. || So the ship changes sides. ||"

### 9. Play every road

**Screen:** Both lint commands. Then the game: the call waiting, the Queen's face,
Continue, the Badb's answer, "Then fly with us." The text on the console. Then a second
game: "We do not stand down."

**Say:** "Check both files, and then play it. || There's her call, waiting, with her name
and the title. || I open it, she makes her offer, | and I talk to the Badb instead. |||
Then fly with us. || The crew's told the call is done, the Badb is turned, | and the bonus
for sinking her is closed. || That's a real choice: | three hundred credits, or one raider
fewer. || Then play it again and refuse her, | and play it a third time and never answer
at all. || The game has to be winnable on every road. ||"

### 10. Hand her to a friend

**Screen:** File Explorer: `common_data\bosses\corsair_queen.amd` in one window, the
`corsair_queen` folder with its two files in another. The page's table.

**Say:** "Now be honest about what you're handing over. || If you send the one file, | your
friend gets the boss, her ships, her objectives, | and the Morrigan calling the clock. ||
They don't get the arrival line, the reserve ship, or the call. ||| For those, they need
the folder too, inside their Legendary Missions. || And an update removes that folder, for
them and for you. || So keep a copy outside the game, | and put it back when it's gone. ||
Lint will tell you: one warning when the folder's there, | and three when it isn't. ||"

### 11. The rubric, and what comes next

**Screen:** The rubric on the page, scrolled slowly.

**Say:** "The page ends with a rubric, | and every line on it is something you can check
yourself. || She's yours, she's checked, she plays, and she travels. ||| When every line
is ticked, you've finished Class 2. || You can write a cast, a conversation, | and a boss
who talks back. || In the next class, the crew leaves the bridge. ||"
