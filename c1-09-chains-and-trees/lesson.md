# Class 1, Lecture 9 - Chains and trees

## What you will have at the end

A story with a beginning, a middle and two endings. The crew closes on the hulk. Only then
are they told to bring her log home. One extra step is theirs to take or leave. Getting
home in time wins the game. Running out the clock loses it.

*[Screenshot to add: the Quest Log showing "Salvage Run" with its steps under it.]*

You will edit one file, `mission.amd`. Nothing in `story.mast` changes.

## The video

*[Link to add when recorded.]*

## Before you start

- Your mission as Lecture 8 left it: both files, with the quest **Close Inspection** in
  `mission.amd`. It is the same mission you have had since Lecture 3.
- `sbs lint MyMission` says `clean`.
- VS Code with the mission folder open, a command prompt open in `data\missions`, and the
  game closed.

You will not throw Close Inspection away. In Step 2 it becomes the first step of your
story, word for word as you wrote it.

In Lecture 8's exercise you added a second quest of your own, under Close Inspection.
Leave it where it is. Step 3 tells you how to work around it.

Lecture 6 taught you to read a finding from lint, and to fix the first one first. This
page prints findings and does not explain their parts again.

Line numbers on this page are for a `mission.amd` that matches Lecture 8's finished file
line for line. If you did Lecture 7's exercise, yours are a line or two higher. Go by the
words.

Two words for this lecture:

| Word | Meaning |
|---|---|
| Arc | A story: a heading with steps under it |
| Step | One quest inside an arc |

## Step 1 - Give the story a heading

Open `mission.amd`. Find this line:

```
### [Close Inspection](approach)
```

Click at the very start of that line, in front of the first `#`. Type:

```
### [Salvage Run](salvage)
---
Arc
Scope: shared
Starts when: at once
---
The hulk's reactor is failing. Get her flight log back to DS 1 before she goes.
```

After the last line press Enter twice. That leaves one blank line between your new record
and Close Inspection.

The new thing is the single word `Arc`, alone on the first line inside the fence. It has no
colon. It says this record is a heading over a run of steps.

## Step 2 - Put Close Inspection under it

Add one hash to the Close Inspection heading, so it has four:

```
#### [Close Inspection](approach)
```

That is all it takes. A record with four hashes is a step of the nearest three-hash record
above it. Close Inspection is now the first step of Salvage Run.

Its key has not changed, but its full address has. From anywhere else in the file it is
now `salvage/approach`: the arc, a slash, the step.

## Step 3 - A second step, and the line that starts it

Click at the end of Close Inspection's description line. Press Enter twice. Type:

```
#### [Bring the Log Home](home)
---
Scope: shared
Starts when: revealed
Objective: Return to within 1000 of DS 1
Done when: reach station 1000
Reward: 200 credits
---
You have her flight log. Carry it back to DS 1.
```

> **Where you type it matters.** A four-hash step belongs to the nearest three-hash record
> ABOVE it. If your own quest from Lecture 8 sits under Close Inspection, the new step goes
> above that quest, not below it. Below it, the step becomes a step of your quest, and the
> game is won the moment the crew reaches the hulk. Lint warns you when that happens. Step
> 7 shows you the warning, and one thing it says that you must not do.

`Starts when: revealed` means this step is hidden and asleep. It is not in the Quest Log,
and nothing can finish it, until another quest reveals it.

Nothing reveals it yet. Save with `Ctrl+S`, and ask lint:

```
sbs lint MyMission
```

```
== mission.amd ==
  [WARNING] line 68: `Bring the Log Home` waits to be revealed, and nothing reveals it: no `Then: reveal salvage/home` on another step, and no answer or story line names `home`. It never appears, and the story it belongs to cannot finish (never-revealed)

1 amd + 1 mast file(s): 0 error(s), 1 warning(s)
```

Lint read `Starts when: revealed` on line 68 and looked for the line that wakes this step.
There is none. Its sentence spells that line out for you: `Then: reveal salvage/home`.

If lint says `clean` here, one of your own sentences has the word `home` in it. Step 7
explains. Go on to the next line either way.

Now make Close Inspection reveal it. Add one line to Close Inspection's fence, under its
`Reward:` line:

```
Then: reveal salvage/home
```

Save. Run lint: `clean`.

| Part | Meaning |
|---|---|
| `Then:` | What happens when this quest finishes |
| `reveal` | Start another quest |
| `salvage/home` | Which one: its full address |

That is a chain. Finishing one step starts the next.

Three rules for `Then: reveal`:

1. Write the full address, `salvage/home`. Not `home` on its own.
2. One `Then:` line per quest. A second one replaces the first.
3. Every `Starts when: revealed` step needs some other quest to reveal it.

## Step 4 - A step the crew can skip

Click at the end of Bring the Log Home's description line. Press Enter twice. Type:

```
#### [Quick Work](quick)
---
Scope: shared
Starts when: at once
Objective: Reach the hulk inside two minutes
Done when: reach derelict 500
Fails when: 2 minutes
Reward: 50 credits
---
Optional. DS 1 pays a bonus for a fast approach.
```

`Fails when:` is new. It is the opposite of `Done when:`. This quest can end two ways,
and whichever happens first decides it.

| What happens first | Result |
|---|---|
| The ship gets within 500 of the hulk | Quick Work is complete. The side is paid 50 |
| Two minutes pass | Quick Work has failed. Nothing is paid |

Quick Work and Close Inspection have the same `Done when:` line. A fast crew finishes both
at the same moment and is told about each.

## Step 5 - Say which steps the story needs

Right now the story would wait for every step under it, Quick Work included. And if Quick
Work failed, the story could never be finished at all.

Fix that by marking the two steps the story needs. Add these two lines to the fence of
**Close Inspection**, and the same two lines to the fence of **Bring the Log Home**:

```
Part of: salvage
Required: true
```

Do not add them to Quick Work.

| Line | Meaning |
|---|---|
| `Part of: salvage` | This step counts toward finishing the arc whose key is `salvage` |
| `Required: true` | The arc is not finished until this step is |

Now the arc is finished when its required steps are done. Quick Work can be finished,
failed or ignored. It no longer matters to the ending.

## Step 6 - An ending each way

There are two arcs in your file now, and both begin with the same three lines. Make sure
you are in the **Salvage Run** record.

Add three lines to the Salvage Run fence, under `Starts when: at once`:

```
Fails when: 10 minutes
Win: The log is home. DS 1 knows what happened out there.
Lose: The reactor let go with the log still aboard.
```

| Line | Meaning |
|---|---|
| `Win:` | When this record is finished, the game is won. The sentence is the reason given |
| `Lose:` | When this record FAILS, the game is lost. The sentence is the reason given |
| `Fails when: 10 minutes` | What fails it: ten minutes after it starts |

Compare this with Quick Work. Both have a `Fails when:` line. Quick Work failing costs the
crew a bonus. Salvage Run failing ends the game, because Salvage Run has a `Lose:` line.

**`Fails when:` only fails a quest. `Lose:` is what makes a failure end the game.**

`Lose:` only acts when its quest FAILS. On a quest that simply gets finished, the game does
not end. So a `Lose:` line needs something that can fail the quest, and in this lecture
that is a `Fails when:` line on the same record.

### Writing a time

You wrote a time in Lecture 8's exercise. `Fails when:` takes the same thing: a whole
number, in digits, and a unit.

| You write | What you get |
|---|---|
| `10 minutes` | Ten minutes |
| `90 seconds` or `90 sec` | Ninety seconds |
| `1 hour` | One hour |
| `2 minutes 30 seconds` | Two and a half minutes |
| `10 min` or `10m` | Ten minutes. The short forms work |
| `ten minutes`, `2.5 minutes`, `10:00`, or `10` with no unit | No time limit at all. Lint warns you |

The number has to be digits. A number written as a word is not a time.

### The crew gets no warning

Nobody calls the crew to say time is running out. The only clock is in the Quest Log, for
a crew that opens it. Everyone else first hears of the limit when the mission has failed.

So tell them yourself, in words they read at the start: the arc's description, and the
`Objective:` line or the description of its first step. The Quest Log shows all three to
a crew that opens it.

## Your finished arc

```
### [Salvage Run](salvage)
---
Arc
Scope: shared
Starts when: at once
Fails when: 10 minutes
Win: The log is home. DS 1 knows what happened out there.
Lose: The reactor let go with the log still aboard.
---
The hulk's reactor is failing. Get her flight log back to DS 1 before she goes.

#### [Close Inspection](approach)
---
Scope: shared
Starts when: at once
Objective: Close to within 500 of the hulk
Done when: reach derelict 500
Reward: 100 credits
Then: reveal salvage/home
Part of: salvage
Required: true
---
The hulk is not answering hails. Bring the ship in close and take a look.

#### [Bring the Log Home](home)
---
Scope: shared
Starts when: revealed
Objective: Return to within 1000 of DS 1
Done when: reach station 1000
Reward: 200 credits
Part of: salvage
Required: true
---
You have her flight log. Carry it back to DS 1.

#### [Quick Work](quick)
---
Scope: shared
Starts when: at once
Objective: Reach the hulk inside two minutes
Done when: reach derelict 500
Fails when: 2 minutes
Reward: 50 credits
---
Optional. DS 1 pays a bonus for a fast approach.
```

The whole file is in `example\mission.amd`.

## Step 7 - Check it

```
sbs lint MyMission
```

```
== mission.amd ==
  clean

1 amd + 1 mast file(s): 0 error(s), 0 warning(s)
```

### One warning to see before you need it

In this lecture a warning can decide who wins. See the worst one now, on purpose.

Take one hash off the Bring the Log Home heading, so it has three:

```
### [Bring the Log Home](home)
```

Save. Run lint.

```
== mission.amd ==
  [WARNING] line 65:14: `approach` Then reveals `salvage/home`, and no record has that key, so nothing is revealed. There is a `home` at `home`: write `Then: reveal home` (dangling-reveal)

1 amd + 1 mast file(s): 0 error(s), 1 warning(s)
```

You changed line 71. Lint names line 65, the `Then:` line in Close Inspection. That is
break 3 of Lecture 6 again: a finding about a `Then:` line is about the record it points
at.

With three hashes, Bring the Log Home is no longer a step of Salvage Run. It is a quest of
its own, and Quick Work below it has become ITS step. Salvage Run has one step left. If you
played this, the game would be WON the moment the crew reached the hulk.

Now read the end of the sentence. Lint found your step in its new place and offers a line
that points there: `Then: reveal home`.

**Do not write that line.** It makes lint say `clean`, and the game is still won at the
hulk. Your `Then:` line was right. The heading is wrong.

Put the fourth hash back. Save. Run lint: `clean`.

**When lint offers you a new `Then:` line, count the hashes on the step first.**

### What lint says about the rest

Every row below was tried on this mission, one at a time. Lint was run. Then the game was
run without a screen, by a script that put the ship beside the hulk and then beside DS 1.
The last column is the code at the end of lint's line.

A misspelled field, a missing colon, a space in front of a field, a key used twice: you met
these in Lecture 6, and lint says the same about them here. These tables tell you what each
one costs in THIS story.

**The chain.** The mistake is on Close Inspection's `Then:` line, unless the row names
another line.

| Mistake | What the game does | Lint says |
|---|---|---|
| `Then: reveal salvage/hmoe` (the step misspelled) | Bring the Log Home never appears, so the story cannot be finished | `dangling-reveal` |
| `Then: reveal home` (the arc and the slash left off) | The same | `reveal-path`. Its sentence gives the line to write |
| `Then: reveal Salvage/Home` (capitals), `salvage\home` (the other slash), or the step's name in place of its address | The same | `dangling-reveal` |
| `Then: reveal salvage/home, salvage/quick` (two at once) | The same | `dangling-reveal`, about `salvage/home,` with its comma |
| `Then: start salvage/home`, or `Then: reveals salvage/home` | The same | `unknown-then-verb` and `dangling-reveal`. The second one gives the line to write |
| Two `Then:` lines in one fence | Only the lower one counts. With the right line on top, Bring the Log Home never appears | `repeated-then` |
| The `Then:` line typed below the closing `---` | Bring the Log Home never appears | `field-below-fence` |
| A space in front of the `Then:` line | The same | `field-indented` |
| `Then reveal salvage/home` (no colon) | The same | `fence-syntax`, an error |
| The step's key changed, `(home)` to `(log_home)`, the `Then:` line left alone | The same | `dangling-reveal`, and `never-revealed` on the step that waits |
| The arc's key changed, `(salvage)` to `(salvage_run)`, the lines that name it left alone | The same | `dangling-reveal`: its sentence gives the line to write. And `dangling-parent`, twice |
| `Starts when: reveal` (the `ed` left off), or `Starts when: hidden` | Nothing the crew can see. The step is on offer, not hidden, and neither quest screen lists a step that is on offer. It still starts when Close Inspection finishes | `unknown-trigger`. Its sentence lists what you can write |
| `When: reach station 1000` where `Done when:` was meant | Bring the Log Home appears and can never be finished | `quest-never-finishes`. Its sentence gives the line to write |
| `Done when: reach staton 1000` (the role misspelled) | The same | `role-nothing-wears` |

A story that cannot be finished ends one way. The ten minutes run out, and the game is
lost.

**Where a step sits.**

| Mistake | What the game does | Lint says |
|---|---|---|
| Three hashes on Bring the Log Home | The game is WON the moment the crew reaches the hulk | `dangling-reveal`. Its sentence offers `Then: reveal home`. Do not write it |
| The new steps typed below another three-hash quest | The same. They become steps of that quest | `dangling-reveal`. It offers a line with that quest's key in it. Do not write it |
| Three hashes on Close Inspection (Step 2 not done) | Salvage Run has no steps and can never be finished. Bring the Log Home never appears | `dangling-reveal`. It offers `Then: reveal approach/home`. Do not write it |
| Five hashes on Bring the Log Home | It becomes a step of Close Inspection and never appears. The game is won at the hulk | `reveal-path`. Its sentence ends "or check the number of hashes". Do that |
| Six hashes on Bring the Log Home | The same | `reveal-path`, and `heading-level-jump`, an error |
| Two hashes on Bring the Log Home | It and Quick Work are no longer quests at all. The game is won at the hulk | Three findings. First `dangling-reveal`, with a line you must not write. Then `section-not-loaded`, on your line. The error, `heading-level-jump`, is on the NEXT step's heading |
| One hash on Bring the Log Home | The same | Three findings. First `dangling-reveal`, the same. Then the error, `heading-level-jump`, on your line: it ends `Give it 4`. Then `section-not-loaded`, about the next step |
| Two hashes on Quick Work | Quick Work is gone. The rest of the story plays | `section-not-loaded` |
| A step copied to make the next one, with the key left the same: two steps keyed `(home)` | The second one is dropped. There is no Quick Work | `duplicate-key`. Its sentence gives both line numbers |

**Time.**

| Mistake | What the game does | Lint says |
|---|---|---|
| `Fails when: ten minutes` | No time limit. The story can no longer fail | `unknown-trigger`. Its sentence shows how to write a time |
| `Fails when: 2.5 minutes`, `10:00`, or `10` with no unit | The same | `unknown-trigger` |
| `Fails when: reach station 1000` | The same. Getting somewhere cannot fail a quest | `unsupported-fail-trigger` |
| `Fail when:` (no `s`), or `Lose when:` | The same | `unknown-field`. It guesses the word you meant. For `Lose when` it guesses `Done when`, and that guess is wrong: write `Fails when` |

**What the story needs.** The mistake is in Bring the Log Home's fence.

| Mistake | What the game does | Lint says |
|---|---|---|
| `Part of: salvge` | Bring the Log Home no longer counts. The game is won at the hulk | `dangling-parent`. Where its sentence says "Parent", read `Part of:` |
| `Requierd: true` | The same | `unknown-field`. It guesses `Required` |
| `Required true` (no colon) | The same | `fence-syntax`, an error |
| A space or a tab in front of `Required: true` | The same | `dangling-parent` and `field-indented`. The second one is the mistake |
| `Part of: Salvage Run` on both steps (the name, not the key) | A quick crew sees nothing wrong. If Quick Work fails, reaching DS 1 does not end the game | `dangling-parent`, twice |

**The arc's own lines.**

| Mistake | What the game does | Lint says |
|---|---|---|
| `Kind: Arc`, `Arc:`, or `Ark` | Nothing you can see in this mission | `unknown-field` for the first two, `unknown-kind-line` for `Ark` |
| `Arc` typed on the second line of the fence | The same | `fence-syntax`, an error. Its sentence says where the word goes |
| `Wins:`, or `Win` with no colon | The story is finished at DS 1, and the game goes on | `unknown-field`, which guesses `Win`. Or `fence-syntax`, an error |
| `Loose:` | When the time runs out the story fails, and the game goes on | `unknown-field`. It guesses `Lose` |
| The three lines of Step 6 typed in Bring the Log Home's fence | The game is still won at DS 1. But the ten minutes start only when Bring the Log Home appears. Until then there is no time limit | `required-step-dead-end` |

### What lint cannot see

For every row below lint says `clean`. Both logs stay empty too, except in the one row
that says otherwise.

| You wrote | What happens when you play |
|---|---|
| No `Then:` line at all, in the finished file | Bring the Log Home never appears. Lint's `never-revealed` warning is silent, and the next paragraph says why |
| The `Then:` line in Quick Work's fence, not Close Inspection's | A quick crew sees nothing wrong. If Quick Work fails first, Bring the Log Home never appears |
| `Then: reveal salvage/quick` (another step's address) | Bring the Log Home never appears |
| `Then: reveal` with no address after it | Bring the Log Home never appears. This one does leave a line in `mast.runtime.log` |
| `Part of:` with no key after it, on Bring the Log Home | Bring the Log Home no longer counts. The game is won at the hulk |
| `Then: reveal salvage/approach` (the step's own address) | Close Inspection starts again each time it finishes. While the ship stays near the hulk it finishes every two seconds, and pays 100 each time |
| Three hashes on Bring the Log Home, and then the line lint offered, `Then: reveal home` | The game is won at the hulk |
| Five hashes on Quick Work | Quick Work becomes a step of Bring the Log Home, and is not in the Quest Log at the start. A quick crew finishes both at the hulk, is paid all 350, and wins there |
| `Required: ture` | Bring the Log Home no longer counts. The game is won at the hulk |
| `Part of:` and `Required:` on Close Inspection only | The game is won at the hulk |
| `Part of:` and `Required:` on neither step | A quick crew sees nothing wrong. If Quick Work fails, reaching DS 1 does not end the game |
| `Part of:` and `Required:` on Quick Work as well | If Quick Work fails, reaching DS 1 does not end the game |
| The three lines of Step 6 typed in First Contact's fence | The game is won when Science has scanned the hulk. In the real game the ship's sensors do that by themselves, seconds after you arrive |
| `Lose:` with no `Fails when:` line | No time limit. The story never fails, so `Lose:` never acts |
| `Starts when: at once` on Bring the Log Home | It is in the Quest Log from the start. A crew that visits DS 1 first finishes it there, then finishes it again after the hulk, and is paid 200 twice |
| `Win:` with no sentence after it | The game is won. The reason given is the arc's name, `Salvage Run` |

Why `never-revealed` is silent in the first row: lint looks for the step's key anywhere in
the file, and `home` is an ordinary word. Your `Win:` sentence says "The log is home." Lint
takes that for a line that names the step. In Step 3 the warning fired, because the
sentence was not there yet. So do not lean on that warning. For every step that says
`Starts when: revealed`, find its `Then: reveal` line with your own eyes.

Three more checks to make by eye:

- Each step under the arc has exactly four hashes.
- `Part of: salvage` and `Required: true` are on Close Inspection and on Bring the Log
  Home, and on no other step.
- `Fails when:`, `Win:` and `Lose:` are in the Salvage Run fence.

### These are fine

| You wrote | Result |
|---|---|
| `Then: reveal salvage / home` (spaces round the slash) | Works |
| `Then: Reveal salvage/home`, `Starts when: Revealed`, or `arc` in small letters | Works. Capitals do not matter in these words. They do matter in an address: `Salvage/Home` is not `salvage/home` |
| `Required: yes`, or `Required: True` | Works |
| `Done when: reach stations 1000` (the role as more than one) | Works |
| No blank line between one step and the next | Works |
| The same key under two arcs: a step `(find)` in Salvage Run | Works. `first_contact/find` and `salvage/find` are two addresses |
| `Fails when: 10 Minutes`, `10 mins`, or `after 10 minutes` | Works. Ten minutes |

## Step 8 - Play it

Start your mission as the server with a Helm console.

**To win:**

1. Open the Quest Log, as you did in Lecture 8: the handheld icon at the top, then
   **Quests**. **Salvage Run** is there with two steps under it: Close Inspection and
   Quick Work. Bring the Log Home is not.
2. Fly to the Unknown Hulk. Get inside 500.
3. Close Inspection completes. If you were quick, so does Quick Work.
4. **Bring the Log Home** is now in the list.
5. Fly back to DS 1. Inside 1000, it completes, and the game ends with your `Win:`
   sentence.

First Contact, the template's own story, finishes its steps at the hulk too. That is not
this lecture's doing, and it does not end the game.

**To lose,** without waiting ten minutes: change `Fails when: 10 minutes` to
`Fails when: 30 seconds`, start the mission, and sit still. The game ends with your `Lose:`
sentence. Then change it back.

What the crew is told, word for word:

| When | The crew is told |
|---|---|
| A step is finished | `Quest complete: Close Inspection` |
| Quick Work runs out of time | `Quest failed: Quick Work` |
| The arc is finished | `Mission complete: Salvage Run` |
| The arc runs out of time | `Mission failed: Salvage Run` |

What the side is paid:

| Ending | Credits |
|---|---|
| Won, with the bonus | 350 |
| Won, bonus missed | 300 |
| Lost at the start | 0 |

Your own quest from Lecture 8 is still running beside the story. When its two minutes are
up it pays its reward on top of these.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| Lint says `dangling-reveal` or `reveal-path` | The address after `Then: reveal` is not the address of a step. If the sentence offers you another line to write, count the hashes on that step before you do anything else |
| Lint says `never-revealed` | A step says `Starts when: revealed`, and no `Then: reveal` line names it |
| Lint says `dangling-parent` | A `Part of:` line names a key that no record has. "Parent" in the sentence is your `Part of:` line |
| Lint says `unknown-trigger` on a `Fails when:` line | The time is not a whole number in digits and a unit |
| Lint says `quest-never-finishes` | `When:` where `Done when:` was meant |
| The game is won as soon as you reach the hulk | Only Close Inspection counts. Bring the Log Home has the wrong number of hashes, or sits below a different three-hash quest, or has lost its `Part of:` or `Required:` line to a misspelling |
| Bring the Log Home never appears | `Then: reveal` does not say `salvage/home` exactly, or there are two `Then:` lines, or none, or the line is in another step's fence |
| Bring the Log Home is in the Quest Log from the start | Its `Starts when:` line says `at once`, not `revealed` |
| Bring the Log Home appears and never finishes | `When:` where `Done when:` was meant, or the role after `reach` is misspelled |
| You reach DS 1 and the game does not end | The `Win:` line is misspelled. Or Quick Work failed, and `Part of:` and `Required:` are on neither step, or on Quick Work as well |
| The time runs out and the game does not end | The `Lose:` line is misspelled or missing |
| The time limit never comes | The `Fails when:` line is misspelled, or its time is not digits and a unit. Lint warns about both |
| A step shows up under one of your other quests | It is typed below that quest. Move it up, under the arc |
| `mast.runtime.log` has a line that starts `Quest: there is no quest` | The game tried to reveal a step and found none at that address. Lint's `dangling-reveal` is the same mistake, found before you played |

## Exercise

Give your story a fourth step.

1. Add a step under Bring the Log Home, above Quick Work. Give it your own name and key.
2. Make it wait: `Starts when: revealed`.
3. Make it finish on time: `Done when: 30 seconds`.
4. Give it `Part of: salvage` and `Required: true`.
5. Add a `Then: reveal` line to Bring the Log Home, with your new step's full address.
6. Write the time limit into the arc's description, and into Close Inspection's, so the
   crew knows it.

Run lint after step 4, and again after step 5. After step 4 it should warn you:
`never-revealed`. After step 5 it has to say `clean`.

Now the game is won thirty seconds after the crew gets home, not the moment they arrive.

## Checkpoint

You are done when all five are true:

- `sbs lint MyMission` shows `mission.amd` as `clean`.
- Bring the Log Home is not in the Quest Log at the start, and is after you reach the hulk.
- Reaching DS 1 after the hulk ends the game with your `Win:` sentence.
- With the time set short, sitting still ends the game with your `Lose:` sentence.
- Reaching the hulk does NOT end the game.

## Next

Lecture 10 is about the things quests point at: scans, and places on the map.

## Further reading

- "Quests" in the library documentation: every quest field, and the mission tree.
- "The AMD file format", the section "Screenplay words": `Arc`, `Beat` and the other words
  a record can call itself.
- `maps\siege_quests.amd` in LegendaryMissions: a shipped story tree. It uses older
  spellings of some fields, such as `Parent:` for `Part of:`.
