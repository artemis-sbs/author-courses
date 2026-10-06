# Class 1, Lecture 8 - Your first quest

## What you will have at the end

A quest of your own in the crew's quest list. It starts when the game starts, it finishes
when the ship gets close to the drifting hulk, and it pays a reward.

*[Screenshot to add: the Quest Log showing "Close Inspection".]*

You will write nine lines in one file. You will not touch any code.

## The video

*[Link to add when recorded.]*

## Before you start

- Your mission as Lecture 7 left it: the `amd` template, your sentence in First Contact,
  your **Derelict Intel** record, the hulk wearing `ghost_ship`, and your word list at the
  top of `mission.amd`.
- VS Code, with the mission folder open.
- A command prompt open in `data\missions`.
- The game closed.

In this page the mission folder is called `MyMission`. Use your own folder's name. Line
numbers on this page are for files that match Lecture 7's finished files line for line. If
you did Lecture 7's exercise, yours are a line or two higher. Go by the words.

Two words for this lecture:

| Word | Meaning |
|---|---|
| Verb | The first word after `Done when:`. It says what the game watches for |
| On offer | A quest the crew can read and has not taken. It does nothing until somebody accepts it |

## Step 1 - Find the quests

Open `mission.amd`. Find this line:

```
## [Quests](quests)
```

Everything under it, down to the next line that starts with two hashes, is the Quests
section. It holds one story already: **First Contact**, with two steps, **Find the
Derelict** and **Study the Derelict**.

Leave those alone. You are adding a quest of your own after them.

## Step 2 - Find the spot

Scroll to the end of the **Study the Derelict** record. Below it is a note that begins
`// ---- Science scans.`

Put your cursor on the blank line above that note. Your quest goes there: after the last
step of First Contact, and still inside the Quests section.

## Step 3 - Write the quest

Type these lines exactly:

```
### [Close Inspection](approach)
---
Scope: shared
Starts when: at once
Objective: Close to within 500 of the hulk
Done when: reach derelict 500
Reward: 100 credits
---
The hulk is not answering hails. Bring the ship in close and take a look.
```

Leave one blank line after it. Save with `Ctrl+S`.

| Line | What it means |
|---|---|
| `### [Close Inspection](approach)` | Three hashes, the name the crew sees, then the key |
| `Scope: shared` | One quest for the whole crew |
| `Starts when: at once` | It is live the moment the game starts |
| `Objective:` | The order, in one sentence. The crew reads it in the Quest Log, above your description |
| `Done when: reach derelict 500` | What finishes it: any player ship within 500 of the hulk |
| `Reward: 100 credits` | What finishing it pays. The credits go to the crew's side |
| The last line | The description. It is the text the crew reads when they select the quest |

## Step 4 - Read the `Done when:` line

`Done when:` is the line that matters most. It says what finishes the quest. It has three
parts, in this order.

| Part | Here | Meaning |
|---|---|---|
| A verb | `reach` | What has to happen |
| A role | `derelict` | Which things count |
| A number | `500` | For `reach`, how close |

**The role.** You met roles in Lecture 7. This is the same promise that `Scan of: derelict`
makes: something in `story.mast` has to wear the word. The hulk does. Its list on line 68
of `story.mast` is `"tsn, derelict, ghost_ship"`: its side, then the template's role, then
the one you added. Look, but do not change anything in that file today.

`reach ghost_ship 500` would finish in the same place, because the hulk wears both words.
Keep `derelict`. Later lectures use it.

**The verb.** In Lecture 7 a step waited for a signal, and a line of `story.mast` had to
say it. This line names no signal. `reach` is built in: the game itself watches for a
player ship coming that close to anything that wears the role. So this quest needs no
change to `story.mast` at all.

**The number.** It comes last, and it is a plain number: `500`, with nothing after it.
Leave it off and the game uses 5000.

## Step 5 - Check it

In the command prompt, type:

```
sbs lint MyMission
```

You want to see:

```
== mission.amd ==
  clean

1 amd + 1 mast file(s): 0 error(s), 0 warning(s)
```

Lecture 6 showed you how to read lint's answer. Now make the two classic slips on this
line, once each, so that you know their messages.

**Slip 1.** Take the word `Done` off the line:

```
When: reach derelict 500
```

Save. Run lint.

```
== mission.amd ==
  [WARNING] line 52: `When: reach derelict 500` STARTS `Close Inspection` (`When:` is short for `Starts when:`), and nothing here finishes it: it stays active for good; its reward is never paid. If this is what finishes it, write `Done when: reach derelict 500` (quest-never-finishes)

1 amd + 1 mast file(s): 0 error(s), 1 warning(s)
```

`When:` on its own does not mean "when it is done". It means "when it starts". Put `Done`
back. Save.

**Slip 2.** Misspell the role:

```
Done when: reach derelect 500
```

Save. Run lint.

```
== mission.amd ==
  [WARNING] line 52: nothing in this mission wears a role called `derelect`, so `reach` matches nothing. Check the spelling against the `Roles:` line of the thing you mean, or the roles in `story.mast` (role-nothing-wears)

1 amd + 1 mast file(s): 0 error(s), 1 warning(s)
```

This is the finding you met in Lecture 7, on a new line. Put the word back. Save, and run
lint: `clean`.

Both slips are only warnings, and with either one the quest sits in the list and never
finishes.

Every row below was tried on this mission, one at a time. Lint was run. Then the game was
run without a screen, by a script that put the ship 1500 from the hulk, then 600, then
450, or straight to 300. The last column is the code at the end of lint's line.

**The `Done when:` line:**

| Mistake | What the game does | Lint says |
|---|---|---|
| `When: reach derelict 500` (the word `Done` left off) | Close Inspection is in the list and never finishes. The reward is never paid | `quest-never-finishes`. Its sentence gives the line to write |
| `Done when: reach derelect 500` | The same. Nothing wears `derelect` | `role-nothing-wears` |
| `Done when: reach the derelict 500` | The same. The game looks for a role called `the derelict` | `role-nothing-wears`. Its sentence names `the` |
| `Done wen: reach derelict 500` | The same | `unknown-field`. It guesses the word you meant |
| `Done when reach derelict 500` (no colon) | The same | `fence-syntax`, an error |
| `Done when: arrive derelict 500`, or a sentence: `Done when: the ship gets close to the hulk` | The same | `unknown-trigger`. Its sentence lists the verbs |
| `Done when: two minutes`, `2:00`, `120` or `1.5 minutes` (the exercise) | The same | `unknown-trigger`. Its sentence says a time is a number and a unit |
| Two `Done when:` lines in one fence | The second one is used | `repeated-field` |

**The other lines of the fence:**

| Mistake | What the game does | Lint says |
|---|---|---|
| `Starts when: at onse` | Close Inspection is only on offer. It never starts by itself | `unknown-trigger`. Its sentence lists what you can write |
| `Start when: at once` | The same | `unknown-field`. It guesses the word you meant |
| `Starts when: revealed` (copied from Study the Derelict) | Close Inspection stays hidden. It never appears | `never-revealed` |
| `Rewards: 100 credits` | The quest finishes, and nothing is paid | `unknown-field`. It guesses the word you meant |
| `Reward: 100 credits` typed below the closing `---` | The quest finishes, and nothing is paid. The line becomes the first words of the description | `field-below-fence` |
| `Objetive:` | The line is not read. Nothing else changes | `unknown-field`. It guesses the word you meant |
| `Scope: shard` | Nothing changes in this mission | `unknown-enum-value` |

**The heading, and where the record goes:**

| Mistake | What the game does | Lint says |
|---|---|---|
| `## [Close Inspection](approach)` (two hashes) | It is a section, not a quest. It never appears | `section-not-loaded`. Its sentence says to give it three hashes |
| The record typed above the `## [Quests](quests)` line | It never appears. `mast.runtime.log` gets one line | `heading-level-jump`, an error, and then `section-not-loaded`. Both talk about hashes. Leave the hashes alone and move the record below the `## [Quests](quests)` line |
| The record typed below the `## [Scans](scans)` line, or at the end of the file | It never appears | `unknown-field`, five times: once for each line of your fence. Each says the record "is being read as a scan because of where it sits" |
| The record typed between Find the Derelict and Study the Derelict | Study the Derelict becomes a step of YOUR quest, and never appears. First Contact finishes as soon as Find the Derelict does. `mast.runtime.log` gets one line | `dangling-reveal`, on the `Then:` line of Find the Derelict. Its sentence offers a line to write. Do not write it. Move your record below Study the Derelict |
| The record typed under First Contact's own description, above its two steps | Both steps become steps of your quest. Study the Derelict never appears, and First Contact never finishes. `mast.runtime.log` gets the same line | The same finding. Move your record below Study the Derelict |
| A key that is taken: `(first_contact)`. Or, in the exercise, a second quest left with `(approach)` | The second record with that key is dropped | `duplicate-key` |
| `###[Close Inspection](approach)`, `### [Close Inspection]`, or `### Close Inspection (approach)` | The record is not there | `broken-heading`, an error. Lecture 6, Step 7 has the whole table |
| The closing `---` left out | The quest works, and it has no description. `mast.runtime.log` gets one line | `unclosed-data-fence`, an error |
| The opening `---` left out, or both | It is only on offer, and the lines of its fence are its description | `fence-not-opened`, an error |

### What lint cannot see

For every row below lint says `clean`. Both logs stay empty too.

| You wrote | What happens |
|---|---|
| `# [Close Inspection](approach)` (one hash) | Your quest is gone, and so is every reading on the hulk: the Scans section below your heading is no longer read. Study the Derelict never finishes |
| `##### [Close Inspection](approach)` (five hashes) | It becomes a step of Study the Derelict. It is not in the Quest Log until Find the Derelict finishes |
| `#### [Close Inspection](approach)` (four hashes) | It becomes a third step of First Contact, and is listed under it. First Contact now waits for it as well |
| `### [Close Inspection]()` (nothing in the round brackets) | The quest is not there |
| No `Starts when:` line | The quest is only on offer. It is not in the Quest Log. It is on a second list, Available Quests, and nothing happens until somebody accepts it |
| No `Done when:` line. Or `Done when:` with nothing after it, or with `reach` alone | The quest is in the list and never finishes |
| `Done when: reach 500 derelict` (the number first) | The number is not read, and the game uses 5000. In the test it finished 1500 from the hulk |
| `Done when: reach derelict 1,500` | It finishes at 500. The game takes the last number it finds |
| Anything after the number, or round the role: `reach derelict 500 units`, `500m`, `500.`, `within 500`, `five hundred`, `reach "derelict" 500` | It never finishes. The extra became part of the role's name |
| A word from the hulk's NAME: `reach hulk 500`, or `reach Unknown Hulk 500` | It never finishes. A name is not a role |
| A word your own ship wears too: `reach ship 500`. Or your side: `reach tsn 500` | It finishes the moment the game starts, and the reward is paid |
| `Reward: 100`, `Reward: 100credits`, `Reward: one hundred credits`, or `Reward: 1,000 credits` | The quest finishes, and nothing is paid |
| In `story.mast`, `derelict` misspelled in the hulk's list | It never finishes. This is the fourth row of "What lint cannot see" in Lecture 7 |

So when your quest misbehaves and lint says `clean`, read three things: the number of
hashes, the `Starts when:` line, and the `Done when:` line against Step 4. A verb, a role,
a number, and nothing else.

### These are fine

| You wrote | Result |
|---|---|
| `Done when: reach derelicts 500` | Works. In a `Done when:` line the game takes the `s` off |
| `Done When: Reach Derelict 500` | Works. Capitals do not matter on this line |
| `Done when: reach ghost_ship 500` | Works. The hulk wears that role too |
| `Done when: reach derelict` (no number) | Works. The game uses 5000 |
| `Starts when: now` | Works. It means the same as `at once` |
| `Reward: 100 Credits`, `Reward: 100 credit`, or `Reward: 100 credits.` | Works. 100 credits are paid |
| `Reward: The thanks of the fleet` | Allowed. It is a reward in words, and nothing is paid |
| No `Scope:` line | Works the same in this mission |
| No `Objective:` line, no `Reward:` line, or no description | Works. The Quest Log shows no order above the description, the quest pays nothing, or it has no text |
| A blank line or a `//` note inside the fence. No blank line before the record, or after it | Works |
| The record typed first in the Quests section, above First Contact | Works |

## Step 6 - Play it

Start your mission as the server with a Helm console, the way you did in Lecture 3.

1. Open the quest list. At the top of the console, beside your crew member's name, is a
   handheld icon. It opens the ePADD. Choose **Quests** to open the **Quest Log**.
2. **Close Inspection** is in the list on the left. Select it. On the right are its
   `State`, its `Reward`, then your `Objective:` sentence, then your description.
3. Fly to the Unknown Hulk. It is about 9000 from the station, DS 1.
4. Inside 2000, Find the Derelict shows `Done`. That is Lecture 7's signal, not your
   quest. Study the Derelict appears, and a few seconds later it shows `Done` as well.
   Close Inspection has not moved.
5. Keep closing. Inside 500, Close Inspection shows `Done`, and the crew's side is paid
   100 credits.
6. Close the game. Open `mast.compile.log` and `mast.runtime.log`. Both are empty.

## Other built-in verbs

| Write | It finishes when |
|---|---|
| `Done when: reach derelict 500` | A player ship is within 500 of anything that wears that role |
| `Done when: 2 minutes` | That much time has passed since the quest started |
| `Done when: dock station` | A player ship docks with something that wears that role |
| `Done when: destroy 3 raiders` | Three things that wear that role are destroyed |
| `Done when: scan 1 derelict` | Something that wears that role is scanned |

A time is a number and a unit: `2 minutes`, `120 seconds`, `1 hour`, `2 minutes 30 seconds`.

`raiders` means the role `raider`: the game takes the `s` off. This mission has a station
and a hulk and no enemies, so `destroy` has nothing to count here. Lint says `clean` for
that line all the same, because `raider` is a role the game hands out by itself in other
missions.

Scans get their own lecture. In this mission the ship's sensors scan the hulk by
themselves once it is close, as you saw in Lecture 7. So a `scan` quest about the hulk
finishes with nobody at Science.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| Lint says anything but `clean` | Find its code in the tables in Step 5. For the rest, Lecture 6, Step 7 |
| The quest is not in the Quest Log, and lint is clean | No `Starts when: at once` line: it is under Available Quests. Or one hash on its heading, or nothing in the round brackets |
| It is listed as a step of First Contact | The heading has four hashes |
| It appears only after Find the Derelict finishes | The heading has five hashes |
| It is in the list and never shows `Done` | Run lint. If lint is clean, read the `Done when:` line against Step 4: a verb, a role, a number, nothing else |
| It shows `Done` the moment the game starts | The word after `reach` is one your own ship wears too, such as `ship`, or it is your side, `tsn` |
| It shows `Done` a long way from the hulk | The number is missing, or it is in front of the role. The game is using 5000 |
| It shows `Done` and the side is not paid | `Reward:` needs a number, a space, and the word `credits`: `100 credits`. No comma in the number |
| The hulk has lost its readings on Science | One hash on your heading. Give it three |
| Lint prints `== story.mast (compile) ==` and an error | You changed `story.mast` by accident while you were looking at line 68. Lint gives the line. Press `Ctrl+Z` in that file until it is as it was, and save |
| Lint warns `non-ascii` on your description | Curly quotes or a long dash from a word processor. The game shows the plain ones. Lecture 6, Step 3 |

## Exercise

Add a second quest of your own under the first.

1. Give it a new name and a new key.
2. Make it finish on time: `Done when: 2 minutes`.
3. Write your own objective sentence and description.
4. Pick your own reward.
5. Run lint. Then play: stay where you are for two minutes and watch it show `Done`.

## Checkpoint

You are done when all five are true:

- `sbs lint MyMission` answers `clean`, with `0 error(s), 0 warning(s)`.
- Both of your quests are in the Quest Log when the game starts.
- **Close Inspection** shows `Done` when you fly inside 500 of the hulk, and not before.
- Your second quest shows `Done` by itself two minutes in.
- After the play, `mast.compile.log` and `mast.runtime.log` are both empty.

## Next

Lecture 9 joins quests together: a quest that reveals the next one, and a story whose
steps decide whether the crew wins.

## Further reading

- "Quests" in the library documentation: every quest field, and under "Triggers" every
  verb.
- "The AMD file format" in the library documentation: headings, fences, and how a record
  says what it is.
