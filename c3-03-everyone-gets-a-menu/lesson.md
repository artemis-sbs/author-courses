# Class 3, Lecture 3 - Everyone gets a menu

## What you will have at the end

The hulk keeps a secret, and no one person can find it. The engineer is offered one
reading, the surgeon another, and the captain's log only opens once the party has put two
readings together.

*[Screenshot to add: two consoles side by side in the airlock, with different choices.]*

You will edit one section of `mission.amd`. Nothing in `story.mast` changes.

## The video

*[Link to add when recorded.]*

## Before you start

- Your mission from Lecture 2: the crew roster, three rooms, and the recipe card.
- `sbs lint MyMission` says `clean`.
- Two consoles if you can manage it, Engineering and Science. One console also works, and
  Step 7 explains what you see then.

## Step 1 - A choice for one job

Open `mission.amd` and find **The Airlock**. Add one choice above the others:

```
- [Read the name tags on the suits](suits) if medical ; learn suits
```

Then add the room it leads to, below the airlock:

```
### [Six Suits](suits)
% Six suits, six names, and every one of them is here. Nobody left this ship through the airlock.

- [Step back](airlock)
```

The new choice has three parts.

| Part | What it means |
|---|---|
| `[Read the name tags on the suits](suits)` | The words the crew reads, and the room it leads to. Same as before |
| `if medical` | Only someone whose job is `medical` is offered this choice |
| `; learn suits` | When it is taken, the party learns a fact named `suits` |

The job word is the one you wrote on `Roles:` in your crew roster. Dr Hale has
`Roles: medical`, so this choice is hers. Chief Okoro never sees it.

The fact name is yours to invent. One word, no spaces.

## Step 2 - A choice for the other job

In **The Reactor Room**, add:

```
- [Read the shutdown record](shutdown) if engineering ; learn shutdown
```

and its room:

```
### [The Shutdown Record](shutdown)
% Shut down from this room, and then the restart key was taken out and carried away. Whoever did it did not mean for her to wake up.

- [Step back](reactor)
```

Now each of your two people has one thing only they can read.

## Step 3 - A door that opens when they know enough

In **The Bridge**, add a choice above the others:

```
- [Answer the log](last_entry) if learned >= 2
```

and the room behind it, at the end of the file:

```
### [The Last Entry](last_entry)
% Six aboard. Core cold. Key over the side. The last entry is one word: QUARANTINE.

- [Return to the ship]()
```

`learned` is how many different facts the party has. It belongs to the whole party, not to
one person: the surgeon's reading and the engineer's reading both count.

A fact counts once. Reading the suit tags twice is still one fact.

## Step 4 - A line that changes

Replace the bridge's one `%` line with two:

```
%{learned < 2} Every station is dark but one. The log is open on the captain's chair, locked behind a question you cannot answer yet.
%{learned >= 2} Every station is dark but one. The log is open on the captain's chair, and now you know what it is going to ask.
```

A condition in curly brackets right after the `%` decides whether that line can be used.
The first line tells a party that arrives too early that there is more to find. Without
it, they see a room with nothing to do and wonder if the game is broken.

## Step 5 - Three rules for a menu

1. **Nobody gets an empty menu.** Every room keeps at least one choice with no `if`. Yours
   all have a way back and a way home, so this is already true.
2. **A reading goes somewhere and comes back.** The choice leads to a short room that says
   what was found. That room's only choice returns to where the party was.
3. **Count your facts.** You have two facts and the log asks for two. If you ask for
   three, the log can never open. Lint cannot count them for you.

## Step 6 - Check it

```
sbs lint MyMission
```

You want `clean` under `mission.amd`. Lint catches some of the mistakes you can make here
and not others.

| Mistake | What lint says |
|---|---|
| `; lern suits` | A warning: `lern` is not an outcome verb |
| `if learned => 2` (the sign backwards) | A warning: not a condition the game can read |
| `if medical, learn suits` (a comma, not a semicolon) | The same warning |
| `; learn suits if medical` (the `if` after the `;`) | A warning: the choice would be offered to everybody |
| A choice that leads to a room you have not written | A warning that names the room and the key |
| `if medcal` (a misspelled job) | `clean`. Nobody is ever offered the choice |
| `if learned >= 5` when you only have two facts | `clean`. The log never opens |
| `%{learnd < 2}` (a misspelled word in the curly brackets) | `clean`. That line is always allowed, so once the party knows enough the bridge picks between your two lines at random |

For the three that lint misses, check by eye: every word after `if` or inside `{ }` is
either `learned` or a job from your roster.

## Step 7 - Play it

**With two consoles**, Engineering and Science:

1. Fly inside 500 of the hulk. On both consoles, press the tablet icon, open **Boarding
   Party** and press **BEAM DOWN**. Each console becomes the boarding handheld, open on
   the airlock.
2. In the airlock, the Science console (Dr Hale) is offered **Read the name tags on the
   suits**. The Engineering console is not.
3. Go forward to the bridge first. The log is locked, and the line says so.
4. Go back. Dr Hale reads the suit tags. Go aft. Chief Okoro reads the shutdown record.
5. Go forward again. The line has changed, and **Answer the log** is there for both.

The party moves together. When anyone picks a way out, everyone goes.

**With one console**, say Engineering: you are Chief Okoro, and there is no surgeon in the
party. The game hands her reading to you, marked so you know whose it is:

```
Read the name tags on the suits (covering for medical)
```

A short crew can still finish the story. This only happens for a job that someone in your
roster holds, or one of the game's standard jobs.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| Nobody is offered a reading | The word after `if` is not the word on that person's `Roles:` line |
| The doctor is in the party and her reading says "covering for medical" on another console | Same cause. The roster says one word and the choice says another |
| The log never opens | The number after `learned >=` is bigger than the number of different facts in your rooms, or two readings `learn` the same name |
| The log is open before anyone has read anything | The `if learned >= 2` is missing from the choice, or sits after a `;` |
| A choice has disappeared for everyone | Its condition is not one the game can read. Run lint |

## Exercise

In Lecture 2 you added a third person to your roster, at Helm, with a job of your
choosing.

1. Give that person a reading on the bridge: a choice with `if` and your job word, and
   `; learn` with a new fact name.
2. Write the short room it leads to, with a way back to the bridge.
3. Leave the log at `learned >= 2`. Now any two of the three readings open it, so there is
   more than one way through your story.
4. Run lint, then play it with one console and find your reading marked as covering.

## Checkpoint

You are done when all four are true:

- `sbs lint MyMission` shows `mission.amd` as `clean`.
- The log is locked when the party goes straight to the bridge, and the line says why.
- Each reading is offered to the person whose job it is, or marked as covering when that
  person is not in the party.
- With two facts learned, **Answer the log** appears and leads to the last entry.

## Next

Lecture 4 gives your crew skills, so a choice can ask how good someone is and not only
what their job is.

## Further reading

- "Boarding parties" in the library documentation: guards, `learn`, and what happens when
  a party is short of people.
- The header of the Open Universe site file `quiet_shore.amd`: a longer scene built on the
  same three rules.
