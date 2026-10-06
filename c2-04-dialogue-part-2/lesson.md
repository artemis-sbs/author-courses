# Class 2, Lecture 4 - Dialogue, part 2

## What you will have at the end

Harbormaster Quill asks a question, and now the crew can answer it. One answer asks her
for more. One takes a job. One hangs up. If the crew takes the job and finishes it, she
calls back.

*[Screenshot to add: the Comms console with Quill's call open and three answers in the list.]*

You will add answers, three short scenes and two records to `mission.amd`. Nothing in
`story.mast` changes.

## The video

*[Link to add when recorded.]*

## Before you start

- Your mission from Lecture 3. When the crew finishes **Close Inspection**, Quill calls
  and says two things.
- `sbs lint MyMission` says `clean`.
- You can start the mission with a Helm console and a Comms console.

In this page the mission folder is called `MyMission`. Use your own folder's name.

## Step 1 - Give the crew something to say

Open `mission.amd` and find **Quill Checks In**. Below her last take, leave a blank line
and type two lines:

```
- [She is cold. No power, no lights.]()
- [Not now, DS 1. Artemis out.]()
```

Each line is an **answer**: one thing the crew can say back. (The library documentation
calls this line a choice. It is the same thing.)

| Part | What it means |
|---|---|
| `- ` | A dash and a space. This is what makes the line an answer |
| `[She is cold. No power, no lights.]` | Square brackets. The words Comms reads in the list and picks |
| `()` | Round brackets, straight after the square ones, with no space between. They say where the conversation goes next. Empty means: the call is over |

Until now the call ended with **Close**. Now it ends with whichever answer Comms picks.

Two rules for an answer.

1. **An answer is one line.** The dash, both pairs of brackets and anything after them
   stay on the same line.
2. **Answers come at the end.** However many blocks she speaks, the answers are offered
   with the last one. Write them below her last take, so the page reads the way the call
   plays.

## Step 2 - An answer that leads somewhere

An answer does not have to end the call. Put a scene's key in the round brackets and the
conversation goes on there.

Change your first answer so its round brackets hold a key:

```
- [She is cold. No power, no lights.](quill_offer)
```

Now write that scene. Go to the end of the file and type:

```
### [The Offer](quill_offer)
---
Speaker: quill
---
% Then she is salvage, and somebody has to hang a beacon on her. Do you want the job?
% Dead, then. That makes her salvage, and salvage wants a beacon. Are you offering?

- [We will tag her.]()
- [Find someone else, DS 1.]()
```

This scene has no `When:` line and no `Title:` line. Nothing in the story places it as a
call. The only way in is the answer that names it, and it is part of the same call.

The heading has **three hashes**, the same as Quill Checks In. A scene never sits inside
another scene.

## Step 3 - A second way in

Add one more answer to **Quill Checks In**, between the two you have:

```
- [She is cold. No power, no lights.](quill_offer)
- [What do you know about her?](quill_history)
- [Not now, DS 1. Artemis out.]()
```

And write its scene, above The Offer:

```
### [What DS 1 Knows](quill_history)
---
Speaker: quill
---
% She came through the gate eleven days ago with her transponder off. Nobody has claimed her.
% No flight plan, no transponder, no crew list. She arrived, and she stopped.

- [She is cold, DS 1. No power, no lights.](quill_offer)
- [Thank you, DS 1. Artemis out.]()
```

Two different answers now lead to The Offer. That is fine. A crew that asks first hears a
little more and ends up in the same place.

A scene shows **four answers at most**. Write a fifth and it is never offered.

## Step 4 - An answer that does something

So far an answer moves the conversation or ends it. It can also change the story.

First, the job Quill is offering. In the Quests section, on the blank line below
**DS 1 Calls**, add:

```
### [Tag the Hulk](tag_hulk)
---
Scope: shared
Starts when: revealed
Objective: Give the salvage beacon 30 seconds to set
Done when: 30 seconds
Reward: 150 credits
---
DS 1 wants a salvage beacon on the hulk before the scavengers find her.
```

`Starts when: revealed` keeps the job hidden until something starts it. That something is
the crew saying yes.

Now go back to The Offer and add to its first answer:

```
- [We will tag her.]() ; accepts tag_hulk
```

| Part | What it means |
|---|---|
| `;` | A semicolon. Everything after it is what the answer **does** |
| `accepts` | Start a quest that is waiting |
| `tag_hulk` | Which quest: its key, not its name |

## Step 5 - Two things at once, and the four words

An answer can do more than one thing. Write **one** semicolon, then put a **comma**
between the things.

Change the two answers in The Offer to:

```
- [We will tag her.]() ; accepts tag_hulk, completes ds1_calls
- [Find someone else, DS 1.]() ; completes ds1_calls
```

`ds1_calls` is the beat from Lecture 3, the one that places this call. Either way the
crew has answered Quill, so the moment is over, and `completes` says so. A beat stays out
of the quest list while it is running. Once it is complete it is listed as done.

There are four words you can write after the semicolon.

| After the `;` | What it does |
|---|---|
| `accepts tag_hulk` | Starts a quest that is hidden or on offer |
| `completes tag_hulk` | Finishes a quest. It pays the `Reward:` and runs the `Then:` line. It works even on a quest that has not started |
| `fails tag_hulk` | Fails a quest that is running, and charges its `Penalty:`. It does nothing to a quest that has not started |
| `signal some_word` | Sends a word into the story. A quest with `Done when: signal some_word` finishes. A quest with `Starts when: signal some_word` starts |

A step inside an arc is named by its path, arc first: `completes first_contact/study`,
not `completes study`.

An answer can lead somewhere and do something at once:
`- [words](quill_offer) ; completes ds1_calls` is allowed.

## Step 6 - A call that comes back

What the crew said can have consequences later. Make Quill call again when the beacon is
set.

Add one line to **Tag the Hulk**, after `Reward:`:

```
Then: reveal beacon_set
```

Below Tag the Hulk, add a beat. This is the pattern from Lecture 3:

```
### [Beacon Set](beacon_set)
---
Beat
Starts when: revealed
Action:
  - quill hails quill_thanks
---
The beacon is live, and DS 1 calls to say so.
```

At the end of the file, write the scene it calls:

```
### [Quill Calls Back](quill_thanks)
---
Speaker: quill
When: hail
Title: Your beacon
---
% Your beacon is singing, Artemis. The claim is logged in your name.
% Beacon is live. That makes her yours, on paper.

- [Glad to help, DS 1. Artemis out.]()
```

This scene is a call of its own, so it has `When: hail` and a `Title:` again.

Only a crew that took the job, and finished it, ever gets this call. A crew that said
"Find someone else" never hears it.

## Step 7 - Answers that depend on the story

You now have two ways to make an answer exist only when something is true.

| You want | Do this |
|---|---|
| An answer only for a crew that said something earlier in the call | Put it in a scene that only that earlier answer leads to. "We will tag her." is only offered to a crew that told Quill the hulk was cold |
| An answer only once something has happened in the story | Put it in a call that only comes then. "Glad to help" is only offered after the job is done |

In other documentation you will see a third way, a condition written on the answer:

```
- [words](scene_key) if some_name >= 10 ; accepts tag_hulk
```

**Do not use it in this mission yet.** A condition can read only a few things: which side
the answering ship is on, and what a boarding party has learned or is good at. Those are
Class 3. It cannot read your quests or your credits. A name it cannot read counts as zero,
so the condition is never true, the answer is never offered, and lint cannot tell.

You will use `if` for real in Class 3.

## Step 8 - Check it

```
sbs lint MyMission
```

You want `clean` under `mission.amd`. Lint catches nearly every mistake you can make here.

**The answer line:**

| Mistake | What lint says | What the game would do |
|---|---|---|
| `- [Not now, DS 1. Artemis out.]` (no round brackets) | It looks like an answer and is read as a spoken line | Have Quill say it out loud, brackets and all |
| A space before the round bracket, or a `*` where the dash goes | The same warning | The same |
| The `; accepts ...` part on a line of its own | The same warning, on that line | Do nothing, and speak the stray line |
| `() accepts tag_hulk` (no semicolon), or a colon in its place | What follows the round brackets is ignored. `Put a ; in front` | Nothing |
| `(quill_ofer)` (a misspelled scene key) | The answer points at something that is not there | End the call |
| A fifth answer in one scene | It can never be picked | Not show it |
| A curly quote in an answer | Plain keyboard characters only | Show a wrong character |

**What the answer does:**

| Mistake | What lint says | What the game would do |
|---|---|---|
| `; acepts tag_hulk`, or `; accept tag_hulk` without the `s` | Not a word an answer can use. It lists the words it knows | Nothing |
| `; accepts tag_hulkk` (a misspelled quest key) | No quest has the key `tag_hulkk` | End the call and start no job. It also writes a line in `mast.runtime.log` |
| `; accepts Tag the Hulk` (the name, not the key) | `accepts` needs one quest key | The same |
| `; accepts tag_hulk and completes ds1_calls` | The same warning | Neither thing |
| `; completes study` (a step without its arc) | That quest is `first_contact/study` to the game | Nothing |
| `; reveal tag_hulk` | `reveal` is what `Then:` says. From an answer, write `accepts` | Nothing |
| `; accepts tag_hulk if some_name >= 10` (the `if` after the `;`) | The condition has to come first | Offer it to everybody, and start no job |
| `if some_name => 10` (the sign backwards) | Not a condition the game can read | Never offer the answer |
| `; signal some_word` when no quest waits for that word | Nothing listens for it | Nothing |

**The scenes and the story:**

| Mistake | What lint says | What the game would do |
|---|---|---|
| `#### [The Offer](quill_offer)` (four hashes) | It is nested under the scene above, and that scene disappears from the game | Lose the scene above it. The answer that leads there ends the call |
| `## [The Offer](quill_offer)` (two hashes) | Nothing in the mission reads a section with that key | Lose that scene and every scene below it |
| Two scenes with the same key | No path can tell them apart | Use one of them |
| `Then: reveal beacon_sett` (a misspelled beat) | It reveals something that is not there | Never start the beat |
| `- quill hails quill_thank` (a misspelled scene) | No record has that key | Never make the call. `mast.runtime.log` says why |

Lint says `clean` for these, and they may still not be what you meant:

| You wrote | What happens |
|---|---|
| `if some_name >= 10` on an answer | The answer is never offered (Step 7) |
| A quest's key in the round brackets | The call ends |
| No `Starts when: revealed` on Tag the Hulk | The job is on offer from the first moment, before Quill has asked |
| No `Done when:` on Tag the Hulk | The job is taken and never finishes, so she never calls back |

Two things that used to go wrong and no longer do:

- A second semicolon works the same as a comma: `; accepts tag_hulk ; completes ds1_calls`.
- Curly brackets in an answer's words are shown as you typed them.

## Step 9 - Play it

Start your mission as the server, with a Helm console and a Comms console.

1. Fly inside 500 of the Unknown Hulk. On Comms, open
   **Harbormaster Quill - About that hulk** and press **Continue**.
2. With her second line, the list offers **Back** and your three answers.
3. Choose **What do you know about her?** She tells you. The list offers **Back** and
   two answers.
4. Choose **She is cold, DS 1. No power, no lights.** She makes the offer.
5. Choose **We will tag her.** The call is over. The quest list now has **Tag the Hulk**,
   running, and **DS 1 Calls**, done.
6. Wait 30 seconds. **Tag the Hulk** completes and pays 150 credits. Comms has a new row:
   **Harbormaster Quill - Your beacon**. Open it and answer.

Play it twice more.

- Choose **Find someone else, DS 1.** No job starts, and no second call comes.
- Choose **Not now, DS 1. Artemis out.** The call is gone, and it does not come back.

**Back** is different from an answer. It puts the call back in the list, unanswered, and
nothing happens in the story. Opened again, the call picks up at the scene the crew had
reached.

So the crew always has a way to say "not now". An answer that hangs up is for when the
story can go on without the call. If your story cannot, do not write one.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| Quill says one of your answers out loud, with its brackets | That line is not an answer. The round brackets are missing, there is a space before them, or the line does not start with a dash |
| She says `; accepts tag_hulk` out loud | The part after the semicolon is on a line of its own |
| An answer ends the call when it should lead on | The key in its round brackets is not a scene's key. Or the scene it names has two hashes on its heading. Or the scene directly below that one has four |
| No call arrives at all, and it did in Lecture 3 | A scene directly below Quill Checks In has four hashes |
| "We will tag her." and no job starts | The quest key is misspelled, the semicolon is missing, or there are two semicolons |
| Tag the Hulk is on offer before Quill calls | Tag the Hulk has no `Starts when: revealed` line |
| The job never finishes | Tag the Hulk has no `Done when:` line |
| The job finishes and she does not call back | Work down this list. `Then: reveal beacon_set` is missing. The beat's key is not `beacon_set`. The heading of Quill Calls Back, or of a scene above it, has two hashes |
| An answer is never offered | It has an `if` on it, or it is the fifth answer in its scene |

## Exercise

In the Lecture 3 exercise you wrote a second scene. A second beat places it as a call
when your timed quest runs out.

1. Give that scene two answers. One leads to a new scene. One ends the call.
2. Write the new scene. Give it one answer that sends a word into the story. Invent the
   word: `- [your words]() ; signal told_truth`
3. In the Quests section, add a quest that finishes on that word:

   ```
   ### [A Straight Answer](straight_answer)
   ---
   Scope: shared
   Starts when: at once
   Objective: Tell DS 1 who was flying
   Done when: signal told_truth
   Reward: 25 credits
   ---
   ```

4. Run lint, then play. The quest is in the list from the start. It completes when Comms
   gives that answer, and not before.

## Checkpoint

You are done when all five are true:

- `sbs lint MyMission` shows `mission.amd` as `clean`.
- Quill's call ends with three answers in the list, not with **Close**.
- **What do you know about her?** leads to a scene, and that scene leads to the offer.
- **We will tag her.** puts **Tag the Hulk** in the quest list. About 30 seconds later it
  completes, and **Harbormaster Quill - Your beacon** is waiting on Comms.
- **Find someone else, DS 1.** starts no job, and no second call comes.

## Next

Lecture 5 takes the call further: a job the crew can only get by answering, and a step
they finish by reporting back.

## Further reading

- "Incoming hails" in the library documentation: the section "What an answer means", and
  the table of what the linter checks. Its longer examples use `if credits >= 200` and
  `costs`, which belong to Open Universe and do nothing in a mission like yours.
- "The AMD file format": choices, and the `Action:` section.
- "Dialogue" in the Open Universe writer's guide. It shows conditions on answers. They
  work there because Open Universe gives a condition something to read.
