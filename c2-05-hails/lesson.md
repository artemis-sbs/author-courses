# Class 2, Lecture 5 - Hails

## What you will have at the end

The salvage job no longer finishes by itself. When the beacon is set, the quest list tells
the crew to report. DS 1 calls, a second voice comes on the line, and the job pays when
Comms says the words.

You will also know three things about every call you write from now on: which call sits at
the top of the list, which ships are called, and what a Comms officer can do with a call
that is waiting.

*[Screenshot to add: the Comms console with the report call open on Chief Ives's line, and
one answer in the list.]*

You will change two quest records, add one character and rewrite one scene in
`mission.amd`. Nothing in `story.mast` changes.

## The video

*[Link to add when recorded.]*

## Before you start

- Your mission from Lecture 4. A crew that tells Quill "We will tag her." gets the job
  **Tag the Hulk**, and about 30 seconds later she calls back.
- `sbs lint MyMission` says `clean`.
- You can start the mission with a Helm console and a Comms console.

In this page the mission folder is called `MyMission`. Use your own folder's name.

## Step 1 - A step only an answer can finish

In Lecture 4 the job finished on a clock and paid. Then Quill called to say well done.
Nothing waited on that call. The crew could leave it in the list for the rest of the game.

Now the job is not over until the crew has reported.

Find **Tag the Hulk** in the Quests section. Make three changes: take out the `Reward:`
line, change the `Then:` line, and add a sentence to the description.

```
### [Tag the Hulk](tag_hulk)
---
Scope: shared
Starts when: revealed
Objective: Give the salvage beacon 30 seconds to set
Done when: 30 seconds
Then: reveal report_in
---
DS 1 wants a salvage beacon on the hulk before the scavengers find her. It pays when
the ship reports back.
```

Below it is the beat **Beacon Set**. Replace the whole record with this one:

```
### [Report to DS 1](report_in)
---
Scope: shared
Starts when: revealed
Objective: Answer DS 1 and tell her the beacon is set
Reward: 150 credits
Action:
  - quill hails quill_thanks
---
The beacon is live. DS 1 pays when she hears it from the ship.
```

This is a quest, not a beat. Compare it with the beat it replaces.

| Line | What it means |
|---|---|
| No `Beat` line | A quest is in the quest list while it is running. A beat is not. The crew can now see that something is expected of them |
| `Objective:` | The sentence the crew reads. Here it sends them to Comms |
| `Reward:` | The pay has moved here. It is paid when this step completes |
| `Action:` | The same two lines the beat had. `Action:` works on any quest. It happens the moment the quest starts |
| No `Done when:` line | Nothing in the game finishes this step by itself. Only an answer can |

## Step 2 - The answer that finishes it

Go to the end of the file, to the scene **Quill Calls Back**. She should ask now, not
congratulate. Change her takes and the answer:

```
### [Quill Calls Back](quill_thanks)
---
Speaker: quill
When: hail
Title: Your beacon
---
% Something just started singing out by that hulk. Tell me it is yours.
% I have a new beacon on my board, out by the hulk. Is that your work?

- [It is ours, DS 1. The beacon is set.]() ; completes report_in
```

`completes` is one of the four words from Lecture 4. It finishes the step and pays its
`Reward:`.

One rule for a call that a step is waiting on.

**Every answer that ends the call finishes the step.** Suppose you add a second answer,
`- [Not now, DS 1.]()`. A crew that picks it has ended the call. The call does not come
back, and Report to DS 1 stays in the quest list for the rest of the game. Lint cannot see
this.

The crew already has a way to say "not now". It is **Back**, from Lecture 3: the call goes
back in the list, and the step waits with it.

## Step 3 - A second voice

A call can have more than one person on the line.

First the person. In the Characters section, below Harbormaster Quill, add:

```
### [Chief Ives](ives)
---
Face: terran_male
---
Keeps the salvage ledger on DS 1. Counts everything twice.
```

If Lecture 2 left you with other people, use one of them, and write that person's key
wherever this page says `ives`.

Now give him a block in the call. Change the lines under the fence of Quill Calls Back so
the scene reads:

```
### [Quill Calls Back](quill_thanks)
---
Speaker: quill
When: hail
Title: Your beacon
---
@quill
% Something just started singing out by that hulk. Tell me it is yours.
% I have a new beacon on my board, out by the hulk. Is that your work?

@ives
% Salvage desk. If it is theirs, I need to hear them say it.
% Chief Ives, salvage desk. Say it for the ledger, please.

- [It is ours, DS 1. The beacon is set.]() ; completes report_in
```

In Lecture 3 an `@quill` line started the next thing Quill said. An `@` line with another
character's key hands the call to that person. The name and the face change with the
block. The crew reads Quill, presses **Continue**, and reads Ives.

Four things to know.

1. **The call still belongs to the `Speaker:`.** In the list it is
   `Harbormaster Quill - Your beacon`, whoever speaks inside it.
2. **The line is `@` and a key, and nothing else.** `@ives`. Not `@Chief Ives`, not
   `@ ives`, not `@ives:`. Each of those stops being a block. His takes become more of
   Quill's takes, and lint says `clean`.
3. **Each block has its own takes.** The game picks one take from each block, the same as
   before.
4. **The answers still come with the last block,** wherever you type them. Keep them at the
   end of the scene.

A block can come first as well. Put `@ives` above `@quill` and he opens the call.

## Step 4 - Which call is on top

Calls wait in a list on the Comms console. You now have more than one call in your
mission, so it is worth knowing how the list is ordered.

| Fact | What it means for your writing |
|---|---|
| The newest call is at the top | A call that matters can be pushed down by a later one |
| A row reads `name - title` | The `Title:` line is the only thing that tells two calls from the same person apart. A call with no `Title:` reads `Harbormaster Quill` and nothing else |
| A call does not time out | It waits until Comms answers it. Nothing in your fact sheet takes a call back |
| One call is open at a time | While Comms is in a call, the others wait |

To keep a call at the top, give its scene a `Priority:` line. Add one to Quill Calls Back:

```
Speaker: quill
When: hail
Title: Your beacon
Priority: 5
```

A call with a higher number sits above every call with a lower one, however new they are.
A call with no `Priority:` line counts as 0. Write a whole number. Use it for a call that
a step is waiting on, and leave the others alone.

## Step 5 - Who gets called

You have never said which ship Quill calls. You do not have to: **every player ship is
called.** With one ship in the game there is nothing more to it.

Your mission can be started with more than one ship. This is what happens with two.

| Moment | With two ships |
|---|---|
| The call is placed | Each ship gets its own copy, in its own Comms list |
| One ship answers | Only that ship's copy ends. The other ship's copy is still waiting |
| One ship says "We will tag her." | The job starts for everyone. There is one Tag the Hulk, and both crews see it in their quest lists |
| The other ship then says "Find someone else, DS 1." | Nothing changes. The job goes on |
| The report call | Goes to both ships. The first to report finishes the step, and the side is paid once. A second report changes nothing |
| A ship says "We will tag her." after the job is finished | Nothing. A finished job stays finished |

Two things follow for a writer.

- **Write the words for any ship that might hear them.** Your opening take says
  `Artemis, DS 1.` The crew of the Intrepid reads the same line.
- **A job handed out by a call suits a mission flown by one ship.** The last row of the
  table is the reason.

All of this follows from the line `Scope: shared`: one quest for the whole table. The
library documentation also describes `Scope: ship`, a copy of the quest for each ship. In
a mission made from this template it changes nothing. Leave `Scope: shared` on your
quests.

## Step 6 - What Comms can do with a call

This step has nothing to type. It is what the person at Comms can do with what you wrote.

| Comms does this | What happens |
|---|---|
| Leaves the call in the list | It waits |
| Opens it | The conversation is drawn on the Comms console and on the main screen, so the whole bridge can follow. Only a Comms console can open a call or answer one |
| Presses **Back** | The call goes back in the list, unanswered. Nothing in the story changes. Opened again, it starts from the first block of the scene the crew had reached |
| Turns the dial above the list | Off, This Console, Main Screen or Both. It starts on Both. It moves where the conversation is drawn. It answers nothing |
| Opens the Hails tab of the info panel | Every finished call is kept there and can be read again. Reading one again cannot change what was answered |
| Reads the ship's log | Each finished call leaves one line: who called, what about, and what the crew answered |

So an answer is a decision the crew makes once. Everything else on the console lets them
put that decision off, or look back at it.

## Step 7 - Check it

```
sbs lint MyMission
```

You want `clean` under `mission.amd`. Lint names every mistake in this table. The words in
the last column are at the end of the line lint prints.

| Mistake | What the game would do | Lint says |
|---|---|---|
| `; completes report_inn` (a misspelled key) | End the call and leave Report to DS 1 running. It writes a line in `mast.runtime.log` | `outcome-quest-missing` |
| `; completes Report to DS 1` (the name, not the key) | The same | `outcome-quest-missing` |
| `Then: reveal beacon_set` left as it was | Never start the step. No call comes. It writes a line in `mast.runtime.log` | `dangling-reveal` |
| `@ivse` (a misspelled key) | Show his block under the name `ivse`, with no face | `dangling-speaker` |
| No record for Chief Ives in the Characters section | Show his block under the name `ives`, with no face | `dangling-speaker` |
| `Priorty: 5` | Place the call with no priority | `unknown-field` |
| `Priority: 5` typed in the fence of Report to DS 1 | Place the call with no priority | `unknown-field` |
| `Priority 5` (no colon) | Place the call with no priority | An error: it expected `Label: value` |
| `When: hail` left off the scene | Place the call anyway | `hail-not-a-hail` |
| `Scope: everyone` | Nothing different | `unknown-enum-value` |

Lint says `clean` for every row of this second table. Check these by eye.

| You wrote | What happens |
|---|---|
| The `Beat` line is still in the fence of Report to DS 1 | The step works and pays, but it is not in the quest list while it is running. The crew is never told to report |
| The answer in the report call is left as `()`, or the scene has a second answer that hangs up | The call ends and Report to DS 1 stays running for good |
| `Reward: 150 credits` is still on Tag the Hulk as well | The job pays twice |
| The `Then: reveal report_in` line is missing | The beacon sets and nothing follows. No step, no call |
| `Done when: 30 seconds` on Report to DS 1 | The step finishes by itself and pays. The call is left waiting in the list |
| `Starts when: at once` on Report to DS 1 | The call arrives as the game starts. Answering it pays 150 credits before any work is done |
| A `Fails when:` clock on Report to DS 1 | The step fails on time and charges its `Penalty:`. The call stays in the list. Answered late, it completes the step and pays anyway |
| `@Chief Ives`, `@ ives`, `@ives:`, `ives:`, or `% @ives` | His block is gone. His takes are now alternatives to Quill's, and so is the stray line |
| Chief Ives typed under the Dialogue heading | His block is shown under the name `ives`, with no face |
| `Priority: high` | The call never arrives. `mast.runtime.log` has a line that names `high` |
| `Scope: ship` | Nothing different. See Step 5 |

## Step 8 - Play it

Start your mission as the server, with a Helm console and a Comms console.

1. Fly inside 500 of the Unknown Hulk. On Comms, open
   **Harbormaster Quill - About that hulk** and answer through to **We will tag her.**
2. The quest list has **Tag the Hulk**, running.
3. About 30 seconds later Tag the Hulk is done, and the list has **Report to DS 1**,
   running. No credits yet. Comms has a new row: **Harbormaster Quill - Your beacon**.
4. Open it. Quill asks her question. The list offers **Back** and **Continue**.
5. Press **Continue**. The name and the face are now Chief Ives. The list offers **Back**
   and your answer.
6. Press **Back**. The call is in the list again, and Report to DS 1 is still running.
7. Open the call again. It starts with Quill. Press **Continue**, then choose
   **It is ours, DS 1. The beacon is set.**
8. The call is over. Report to DS 1 is done, and the side is paid 150 credits. The ship's
   log has a new line:
   `Harbormaster Quill - Your beacon - answered (It is ours, DS 1. The beacon is set.)`
9. On Comms, open the Hails tab of the info panel. Both calls are listed. Choose one and
   read it through again.

Play it once more, and this time turn the dial above the list to **This Console** before
you open the first call. The conversation is drawn on Comms only.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| The beacon sets and nothing follows | Work down this list. `Then: reveal report_in` is missing or misspelled. The key on the heading of Report to DS 1 is not `report_in`. The `Action:` lines are missing |
| Report to DS 1 is not in the quest list while the call waits | The `Beat` line is still in its fence |
| Comms answers, and Report to DS 1 stays in the list | The answer has no `; completes report_in`, or the key is misspelled. Look in `mast.runtime.log` |
| The job pays as soon as the beacon sets | `Reward:` is still on Tag the Hulk |
| The job pays 300 credits | `Reward:` is on both records |
| The call arrives as the game starts | Report to DS 1 does not say `Starts when: revealed` |
| Ives's line is shown under Quill's name, and there is no **Continue** | His `@` line is not `@` and a key. See Step 3 |
| Now and then Quill says `@Chief Ives` out loud | The same |
| His block is shown under the name `ives`, with no face | His record is missing, or it is not in the Characters section |
| The call never arrives, and it did before you added `Priority:` | The value after `Priority:` is a word, not a number. `mast.runtime.log` names it |
| The report call sits below an older call | The `Priority:` line is in the wrong fence, or misspelled. Run lint |

## Exercise

In the Lecture 3 exercise you wrote a second call, placed by a beat when your timed quest
runs out. In the Lecture 4 exercise you gave it answers.

1. Turn that beat into a step the crew can see. Take out the `Beat` line. Add
   `Scope: shared`, an `Objective:` sentence and a `Reward:`.
2. Make every answer that ends that call finish the step. Add `; completes` and your
   step's key. An answer that already does something gets a comma:
   `; signal told_truth, completes your_step`
3. Give the call a second voice: an `@` block for another of your characters.
4. Run lint, then play. When your timer runs out, the step is in the quest list and the
   call is waiting. Whichever ending the crew picks, the step completes and pays.
5. Break it on purpose. Take `; completes your_step` off one ending. Run lint: `clean`.
   Play it and choose that ending. The call is gone, and the step is still in the list.
   Put it back.

## Checkpoint

You are done when all five are true:

- `sbs lint MyMission` shows `mission.amd` as `clean`.
- When the beacon sets, **Report to DS 1** is in the quest list, running, and no credits
  have been paid.
- The report call has two voices. The name and the face change when Comms presses
  **Continue**.
- **Back** returns the call to the list and leaves Report to DS 1 running.
- **It is ours, DS 1. The beacon is set.** completes Report to DS 1, and the side is paid
  150 credits.

## Next

Lecture 6 is a first look at reputation: a side that remembers what the crew did.

## Further reading

- "Incoming hails" in the library documentation: "Placing the call", "What the crew
  sees" and "Longer conversations".
- "Quests" in the library documentation: the table of quest fields.

That documentation shows four things this lecture left out. Two of them you can try on
your own now; two need something you do not have yet.

| You will see | Why it is not in this lecture |
|---|---|
| `At start: posting`, a job listed for the crew with no Accept button, taken only by answering a call | It works: the tablet's Available Quests lists it as `Posted`, and selecting it says it is taken by answering the call. Your hidden job, started by an answer, does the same work without showing the crew the job first. Use `posting` when you want them to see it coming |
| `Scope: ship` | See Step 5 |
| `Presentation: still` and `Presentation: orbit` | A call is drawn as a portrait unless you say otherwise, and that needs nothing. `still` needs a picture file and a `Backdrop:` line. `orbit` is a moving shot of a ship on the main screen: add `Subject:` and a landmark's key or a role (`Subject: derelict`) |
| `Audio:` | It plays a recorded line when the call opens. It needs a sound file you have recorded, as a `.wav`, kept inside your mission folder |
