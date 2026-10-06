# Class 2, Lecture 3 - Dialogue, part 1

## What you will have at the end

When the crew finishes **Close Inspection**, the station calls the ship. The call waits in
a list on the Comms console. When Comms opens it, Harbormaster Quill says one of three
opening lines, then one of two closing lines. Play it again and it may read differently.

*[Screenshot to add: the Comms console with Quill's call open.]*

You will write a character, a scene and one short record in `mission.amd`. Nothing in
`story.mast` changes.

## The video

*[Link to add when recorded.]*

## Before you start

- Your mission from Class 1, with the quest **Close Inspection** from Lecture 8. Any quest
  of yours that finishes will do. This page uses that one.
- `sbs lint MyMission` says `clean`.
- You can start the mission with a Helm console and a Comms console.
- Your `story.mast` is the one the template gave you. It already reads a Characters
  section and a Dialogue section, if your file has them.

In this page the mission folder is called `MyMission`. Use your own folder's name.

## Step 1 - Someone to speak

A scene needs a speaker, and a speaker is a character record.

If Lecture 2 left you with a `## [Characters](characters)` section, keep it. Pick one of
your own people and use that person's key wherever this page says `quill`.

If you have no such section, go to the end of `mission.amd` and type:

```
// ---- Characters. The people in the story.
## [Characters](characters)

### [Harbormaster Quill](quill)
---
Face: terran_female
---
Runs traffic control on DS 1. Has watched this lane for eleven years.
```

The word in round brackets, `quill`, is her key. Everything in this lesson points at her
by her key, never by her name. Keep keys in small letters, with no spaces.

## Step 2 - Write the scene

Below the characters, at the end of the file, type:

```
// ---- Dialogue. A scene is who speaks and what they say.
## [Dialogue](dialogue)

### [Quill Checks In](quill_hello)
---
Speaker: quill
When: hail
Title: About that hulk
---
% Artemis, DS 1. We watched you go in close.
% Artemis, this is Quill on DS 1. You got nearer to that hulk than I would have.
% DS 1 to Artemis. Nice flying out there.
```

| Line | What it means |
|---|---|
| `## [Dialogue](dialogue)` | The section that holds your scenes. Its key must be `dialogue`, in small letters |
| `### [Quill Checks In](quill_hello)` | Three hashes, a name for your own use, then the scene's key |
| `Speaker: quill` | Who is talking: a character's key |
| `When: hail` | This scene is a call that comes in to the ship |
| `Title: About that hulk` | What the call is about. The crew reads it beside her name before they answer |
| The `%` lines | What she says |

## Step 3 - Takes

Each `%` line is a **take**: one way of saying the same thing. Each time the scene plays,
the game uses one take, picked by chance. Write two or three and the character stops
sounding like a recording.

Three rules for a take.

1. **One take is one line in the file.** However long it is, do not press Enter in the
   middle of it. A take broken onto two lines becomes two takes, and the crew gets half a
   sentence.
2. **Takes are alternatives, not a list.** The crew hears one of them. If she must say two
   things, that is Step 4.
3. **Plain keyboard characters only.** No curly quotes and no long dashes from a word
   processor. And never begin a take with a curly bracket, `{`: the game reads that as a
   condition, and the take is not used.

## Step 4 - Say a second thing

To make her say one thing and then another, write blocks. Each block starts with a line
that is `@` and her key.

Change the lines under the fence so the scene reads:

```
### [Quill Checks In](quill_hello)
---
Speaker: quill
When: hail
Title: About that hulk
---
@quill
% Artemis, DS 1. We watched you go in close.
% Artemis, this is Quill on DS 1. You got nearer to that hulk than I would have.
% DS 1 to Artemis. Nice flying out there.

@quill
% Now tell me she is as dead as she looks.
% So. Is anybody home?
```

Each `@quill` line starts the next thing she says. The game picks one take from each
block, so this scene can read six different ways. The crew reads the first block, presses
**Continue**, and reads the second.

Write `@quill`, the key. `@Harbormaster Quill` does not work.

Keep to one voice in a scene for now.

## Step 5 - Have the story place the call

A scene is words on a page until something in the story places the call. That takes two
small edits in the Quests section.

First, find your **Close Inspection** quest. Add one line inside its fence, after
`Reward:`:

```
Then: reveal ds1_calls
```

The quest now reads:

```
### [Close Inspection](approach)
---
Scope: shared
Starts when: at once
Objective: Close to within 500 of the hulk
Done when: reach derelict 500
Reward: 100 credits
Then: reveal ds1_calls
---
The hulk is not answering hails. Bring the ship in close and take a look.
```

Second, on the blank line below Close Inspection, add a new record:

```
### [DS 1 Calls](ds1_calls)
---
Beat
Starts when: revealed
Action:
  - quill hails quill_hello
---
DS 1 saw the ship go in close, and wants to hear about it.
```

| Line | What it means |
|---|---|
| `Beat` | A kind word, alone on the first line of the fence. A beat is a moment in the story, not a job. It does not show in the quest list |
| `Starts when: revealed` | It waits until another quest reveals it |
| `Action:` | What happens the moment it starts |
| `  - quill hails quill_hello` | Two spaces, a dash, a space. Then who calls, the word `hails`, and the key of the scene |

`Starts when: revealed` is what makes the call wait for Close Inspection. Leave that line
out and the beat is running from the first moment, so the call arrives as the game starts.

## Step 6 - Check it

```
sbs lint MyMission
```

You want `clean` under `mission.amd`. Lint catches some of the mistakes you can make here
and not others.

| Mistake | What lint says |
|---|---|
| `Speaker: quil` (a misspelled key) | A warning: the voice is nobody in the cast. In the game the caller is named `quil` and has no face |
| `- quill hails quill_helo` (a misspelled scene) | A warning: no record has that key |
| `- quill hail quill_hello` (the verb misspelled) | A warning: no action verb |
| `Then: reveal ds1_call` (a misspelled beat) | A warning: it reveals something that is not there |
| The dash under `Action:` missing, or not indented | An error |
| `Beat` on the second line of the fence | An error: a kind word has to be the first line |
| No `When: hail` line | A warning. The call still arrives |
| Curly quotes or a long dash in a take | A warning for each one |
| Two scenes with the same key | A warning. The game uses the second one |
| A scene with no takes | A warning: it opens with nothing said |
| `####` on the scene's heading | An error: the heading jumps a level |
| A take broken onto two lines | `clean`. Each half is a take, so the crew gets half a sentence |
| `##` on the scene's heading | `clean`. The call never arrives |
| The section written `(Dialogue)` or `(conversations)` | `clean`. The call never arrives |
| `Starts when: at once` on DS 1 Calls, or no `Starts when:` line | `clean`. The call arrives as the game starts, before anyone has flown anywhere |
| The `Then: reveal ds1_calls` line left out | `clean`. The call never arrives |
| `@Harbormaster Quill` instead of `@quill` | `clean`. Now and then her line is the words "@Harbormaster Quill" |
| A take that begins with `{` | `clean`. That take is never used |

For the ones lint misses, check four names by eye. Each is written in two places, and the
two must match letter for letter.

| Name | Where it is made | Where it is used |
|---|---|---|
| `quill` | The character's heading | `Speaker:`, each `@` line, the first word of the `Action:` line |
| `quill_hello` | The scene's heading | The last word of the `Action:` line |
| `ds1_calls` | The beat's heading | `Then: reveal` in Close Inspection |
| `characters`, `dialogue` | The two section headings | Nowhere in your file. `story.mast` looks for exactly these two keys |

## Step 7 - Play it

Start your mission as the server, with a Helm console and a Comms console.

1. Fly to the Unknown Hulk and go inside 500. **Close Inspection** completes.
2. On Comms, a list named **Incoming Hails** now has one row:
   **Harbormaster Quill - About that hulk**. Nothing was there before the quest finished.
3. Select the row. The call opens with Quill's face, her name, and one of your three
   opening takes.
4. The list now offers **Back** and **Continue**. Press **Continue** for one of your two
   closing takes.
5. The list offers **Back** and **Close**. Press **Close**. The call is over.

**Back** puts the call back in the list without ending it. Comms can read it through and
open it again when the captain is ready.

Start the mission again and play to the same point. The takes are picked again, so the
scene may read differently.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| The quest completes and no call arrives | Work down this list. The Dialogue section's key is not `dialogue`. The scene's heading has two hashes. The `Then: reveal` line is missing or names the wrong key |
| The call arrives as the game starts | DS 1 Calls does not say `Starts when: revealed` |
| The caller is named `quill`, with no face | The Characters section's key is not `characters` |
| The call opens and nothing is said | Every take in a block begins with `{`, or the scene has no takes |
| A line reads as half a sentence | A take is broken onto two lines |
| She says one thing where you wrote two | The second thing has no `@quill` line above it, so it became more takes of the first |
| A blank line is said | A `%` with nothing after it |

## Exercise

In the Lecture 8 exercise you wrote a quest that finishes on a timer.

1. Write a second scene in the Dialogue section. Give it a new key, a `Title:`, and two or
   three takes. One voice.
2. Below your timed quest, add a second beat. It says `Starts when: revealed`, and its
   `Action:` line calls your new scene.
3. Add a `Then: reveal` line to your timed quest, naming the new beat.
4. Run lint, then play. When the timer runs out, a second call arrives. If the first call
   is still waiting, both are in the list.

## Checkpoint

You are done when all four are true:

- `sbs lint MyMission` shows `mission.amd` as `clean`.
- No call is waiting before Close Inspection completes.
- After it completes, **Harbormaster Quill - About that hulk** is in the Incoming Hails
  list. Opened, she says two things, with **Continue** between them and **Close** at the
  end.
- Over a few games, her opening line is not always the same one.

## Next

Lecture 4 gives the crew something to say back: choices, conditions on a choice, and what
an answer does.

## Further reading

- "Incoming hails" in the library documentation: everything a call can carry, and a
  table of when an `Action:` runs.
- "The AMD file format": the `@Speaker` and `Action:` sections.
- "Dialogue" in the Open Universe writer's guide. It is written for Open Universe. Its
  scenes say `When: comms`, which does nothing in a mission like yours.
