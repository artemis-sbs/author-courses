# Class 3, Lecture 4 - Crew and skills

## What you will have at the end

Your crew are good at different things, and the hulk notices. The surgeon turns out to be
the only one who can read the sensor record, and it has nothing to do with her job. Anyone
may try to wake the reactor, but the chief is three times as likely to manage it, and the
page shows the roll.

*[Screenshot to add: the reactor room after a roll, with the roll line above the room's line.]*

You will add two lines to your crew roster and two choices to your rooms in `mission.amd`.
You will not touch `story.mast`.

## The video

*[Link to add when recorded.]*

## Before you start

- Your mission from Lecture 3: the crew roster, the rooms, the two readings and the log.
- `sbs lint MyMission` says `clean`.
- Two consoles if you can manage it, Engineering and Science. One console also works.

## Step 1 - Say what each person is good at

Open `mission.amd` and find your crew roster. Add one line to each person, under `Roles:`:

```
### [Chief Okoro](okoro)
---
Console: engineering
Face: terran_female
Roles: engineering
Skills: engineering 4, science 1
---

### [Dr Hale](hale)
---
Console: science
Face: terran_male
Roles: medical
Skills: medical 4, science 3
---
```

A `Skills:` line is a list. Each entry is a word, a space and a number. Entries are
separated by commas.

| Part | What it means |
|---|---|
| `engineering` | The name of the skill. One word, no spaces. You may invent your own |
| `4` | How good this person is at it. A whole number |
| `,` | Goes between two skills |

Capital letters do not matter in a skill's name. `Science` and `science` are the same
skill.

A scale that works well:

| Number | Read it as |
|---|---|
| not listed | Cannot do it. The game counts this as 0, unless it is their job |
| 1 | Has had the training |
| 2 | Does it for a living |
| 3 | Good |
| 4 | The best aboard |

A person's job counts as 2 even with no `Skills:` line. Chief Okoro has
`Roles: engineering`, so before today the chief's engineering was 2. The `Skills:` line raises it
to 4.

Dr Hale's job is `medical`. Science is not her job. She is simply good at it. That is what
a skill is for.

## Step 2 - Nothing to paste

The game reads `Skills:` with the rest of the roster. You have nothing to add to
`story.mast`.

The numbers belong to the person on the roster, not to the name on the console. A player
who has saved a name of their own, and sits at Science, is still as good as Dr Hale.

## Step 3 - A choice for someone good enough

In **The Bridge**, add a choice below **Answer the log**:

```
- [Pull the sensor record](sensor_record) if skill science >= 3 ; learn sensors
```

Then add the room it leads to, below the bridge:

```
### [The Sensor Record](sensor_record)
% One contact, closing, eleven days before the core went cold. It never arrived. It is still out there.

- [Step back](bridge)
```

The condition has four parts.

| Part | What it means |
|---|---|
| `skill` | This condition asks about a skill, not a job |
| `science` | Which skill. The word from a `Skills:` line |
| `>=` | At least |
| `3` | The number to reach |

Dr Hale has science 3, so she is offered this choice. Chief Okoro has science 1, and is
not.

You now have three kinds of choice. They differ in who is offered them.

| You write | Who is offered it | If that person is not in the party |
|---|---|---|
| `if medical` | Someone whose job is `medical` | One console covers for them |
| `if skill science >= 3` | Someone whose science is 3 or more | Nobody is offered it |
| no `if` at all | Everyone | - |

Read the middle row twice. **Nobody covers for a skill.** With Dr Hale back on the ship,
the sensor record is not on anyone's menu.

## Step 4 - A choice anyone may try

In **The Reactor Room**, add a choice below **Read the shutdown record**:

```
- [Try to wake the core](core_wakes) ; check engineering 9 else core_dead, learn lockout
```

Then add two rooms, below **The Shutdown Record**:

```
### [The Core Turns Over](core_wakes)
% The board lights for four seconds. Long enough to read one line: MANUAL LOCKOUT, CAPTAIN'S KEY.

- [Step back](reactor)

### [The Board Stays Dark](core_dead)
% Nothing. Not a flicker. Whatever you tried, the core did not notice.

- [Step back](reactor)
```

There is no `if` on this choice, so everyone is offered it. What differs is how it turns
out.

| Part | What it means |
|---|---|
| `(core_wakes)` | The room the party goes to when it works |
| `check engineering 9` | Roll for it. The game picks a number from 1 to 10 and adds this person's engineering. A total of 9 or more works |
| `else core_dead` | The room the party goes to when it does not work |
| `, learn lockout` | After a comma. This happens only when the check worked |

The number after the skill is the target. This table shows how often a check works.

| Target | Skill 0 | Skill 2 | Skill 4 |
|---|---|---|---|
| 6 | 5 times in 10 | 7 in 10 | 9 in 10 |
| 9 | 2 in 10 | 4 in 10 | 6 in 10 |
| 12 | never | 1 in 10 | 3 in 10 |

So Chief Okoro wakes the core 6 times in 10. Dr Hale, with no engineering at all, manages
it 2 times in 10.

The page tells the crew what happened. After a try, the party's page gains a line like
this, and then the line of the room they landed in:

```
Chief Okoro - engineering 4, rolled 6: 10 vs 9, success.
```

In a scene made of rooms, each person rolls alone. Nobody helps.

## Step 5 - Four rules for skills

1. **A skill choice is a bonus, never the only way.** Nobody covers for a skill, so a room
   whose only way on is behind `if skill` can trap a short crew. Your log still opens at
   two facts, and there are four to find now, so any party can finish.
2. **A check always has an `else`, and both rooms lead back.** Write the room for failure
   as carefully as the room for success. Half your players will read it.
3. **Before the check always happens. After the check happens only on success.**
   `; check engineering 9 else core_dead, learn lockout` teaches the fact only when the
   core wakes. Put `learn lockout` in front of `check` and the party learns it either way.
4. **Skills belong to the seat's person, whatever the player calls them.** A player
   with a saved name of their own keeps both the job and the numbers.

A party may try a check again. The roll is for drama. It is not a lock.

## Step 6 - Check it

```
sbs lint MyMission
```

You want `clean` under `mission.amd`. Lint catches nearly every mistake you can make here.

| Mistake | What lint says | What the game would do |
|---|---|---|
| `Skill: medical 4` (no `s`) | `Skill` is not a known crew field | Ignore the line |
| `Skills medical 4` (no colon) | An error: it expected `Label: value` | Ignore the line |
| `Skills: medical 4 science 3` (no comma) | `medical 4 science 3` is not a skill and a number, so it is dropped | Lose both numbers |
| `Skills: medical: 4`, `medical=4`, `4 medical` or `medical four` | The same warning, naming that entry | Lose that number |
| Two `Skills:` lines on one person | `Skills:` is written twice, and only the last line counts | Use the second line only |
| A person written with four hashes | They are not directly under the roster. `Give this heading 3 hashes` | Give that seat an automatic name |
| `if skill science => 3` (the sign backwards) | Not a condition the game can read | Offer the choice to nobody |
| `if skill science 3` (no sign) | It has no sign and number | Offer the choice to nobody |
| `if science >= 3` (the word `skill` left out) | `science` on its own is a job, which is 1 or 0 | Offer the choice to nobody |
| `if skill sience >= 3` | Nobody on the roster has a skill or a job called `sience` | Offer the choice to nobody |
| `; chek engineering 9 else core_dead` | `chek` is not an outcome verb | Roll nothing. The choice always works |
| `check engineering else core_dead` (no number), `check engineering >= 9`, or `nine` | Nothing is rolled and the choice always works | Exactly that, and write a line in `mast.runtime.log` |
| `check enginering 9` | Nobody on the roster has `enginering`, so everyone rolls with 0 | Exactly that |
| `check engineering 9, else core_dead` (a comma before `else`) | `else` is not an outcome verb | Send a failed roll to the success room |
| `else core_ded` (a room that does not exist) | A failed roll goes to `core_ded`, and no room here has that key | End the visit on a failed roll |
| The room for success is not written | A warning that names the room and the key | End the visit when the roll works |

Lint says `clean` for these, and they may still not be what you meant:

| You wrote | What happens |
|---|---|
| `sience 3` on the ROSTER | That person has a skill called `sience`, and no science. Lint cannot know which word you meant |
| `if skill science >= 5`, and nobody has 5 | Nobody is offered the choice |
| `check engineering 9` with no `else` | Allowed. A failed roll still goes to the choice's own room, but nothing after the check happens |

A second `;` works the same as the comma: `; check engineering 9 else core_dead ; learn
lockout` is fine.

## Step 7 - Play it

**With two consoles**, Engineering and Science:

1. Fly inside 500 of the hulk. On both consoles, press the tablet icon, open **Boarding
   Party** and press **BEAM DOWN**.
2. Go forward to the bridge. The Science console (Dr Hale) is offered **Pull the sensor
   record**. The Engineering console is not.
3. Go back, then aft to the reactor. Both consoles are offered **Try to wake the core**.
4. Let Dr Hale try. The page shows her roll, with `engineering 0` in it. Most times she
   lands in The Board Stays Dark.
5. Step back. Let Chief Okoro try. This roll says `engineering 4`.

Look at the number in the roll line. If the chief's line says `engineering 2`, the game is
not reading the chief's `Skills:` line. Run lint: the line is misspelled, or its entry is
(Step 6).

**With one console**, say Engineering: you are Chief Okoro. The suit tags come to you
marked as covering, as they did last time. The sensor record does not come to you at all.
You can still try the core.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| The chief's roll says `engineering 2`, not 4 | The chief's `Skills:` line is misspelled, or its `engineering` entry is. Lint names it |
| The surgeon is in the party and nobody is offered the sensor record | The skill word in the room is not the word on her `Skills:` line, or her number is lower than the room asks for |
| A roll says `0` for someone who should be good | The skill word after `check` is not the word on the roster. The roll line shows the word as you typed it |
| Trying the core always works, and no roll line appears | The check has no number, or the number is written as a word, or there is a sign in it. Lint warns, and `mast.runtime.log` has a line each time it is picked |
| A failed roll leads to the room for success | The check has no `else`, or there is a comma before `else` |
| A failed roll ends the visit and everyone is back at their station | The room named after `else` does not exist. Lint warns about it |
| The numbers do nothing at all, and lint is clean | Your copy of the game's library is older than this lesson. Update it |

## Exercise

In Lecture 2 you added a third person to your roster, at Helm, with a job of your choosing.

1. Give that person a `Skills:` line: their job at 3 or 4, and one other skill at 2.
2. In one room, add a choice only they are offered, using `if skill` and their second
   skill. Write the short room it leads to, with a way back.
3. In another room, add a check with a target of 6 on a skill nobody has. Write both rooms.
   Play it and watch the rolls.
4. Change the 6 to 12 and play again. With a skill of 0, it never works. Change it back.
5. Break it on purpose: change `Skills:` to `Skill:` on one person. Run lint and read the
   warning. Then play once anyway, and see what disappears from that person's menu and
   what their roll line says. Put the `s` back.

## Checkpoint

You are done when all four are true:

- `sbs lint MyMission` shows `mission.amd` as `clean`.
- With the surgeon in the party, **Pull the sensor record** is offered to her and to
  nobody else.
- When the chief tries the core, the roll line says `engineering 4`.
- A try at the core leads to one of two rooms, and each has a way back to the reactor.

## Next

Lecture 5 gives one person a quest of their own: something only they are asked to do, and
somewhere it leads.

## Further reading

- "Crew rosters" in the library documentation: `Roles:`, `Skills:`, `Names:`, and who a
  console is.
- "Boarding parties" in the library documentation: job conditions, `learn`, `skill` and
  `check`, and what happens when a party is short of people.
- The headers of `landing_crew.amd` and `scenes.amd` in the Dawnline mission
  (`LandingParty`): a seven-person roster with skills, and a long scene file that uses
  `if skill` and `check` throughout. One line in the `scenes.amd` header is out of date:
  it says the outcomes beside a check happen whether or not the roll works. Today the
  ones written after the check happen only on success.
