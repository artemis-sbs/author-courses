# Class 3, Lecture 13 - What the crew sees

## What you will have at the end

The same mission, read from the other side of the screen.

For six lectures you have written records. Your crew never sees a record. They see a
handheld with eight apps, and each app is made of your words: a heading here, a key
there, a title after the words `Go to`. Some of those words you chose with care. Some
you typed in a hurry as a name for yourself, and they are on the screen too.

Today you go through the handheld one app at a time, find what reads badly in `MyAway`,
and fix it. You also give the two crew members with nothing to do something to do.

*[Screenshot to add: the handheld on the ground, with its eight tiles.]*

One thing to know before you start. **Nobody has seen these screens yet.** Everything on
this page about what an app shows was captured by running the app's own drawing code
with a recorder where the screen should be. So this page can tell you which words an
app shows, and in what order. It cannot tell you where they sit, how big they are or
what color they are, and it does not try.

You change four files: `mission.amd` and the three maps.

## The video

*[Link to add when recorded.]*

## Before you start

- `MyAway` as Lecture 12 left it. `sbs lint MyAway` says `clean`.
- A command prompt open in `C:\Cosmos\data\missions`.

Words for this lecture:

| Word | Meaning |
|---|---|
| Handheld | What a console becomes when its crew member beams down |
| App | One tile on the handheld: Crew, Act, Look, Pack, Tasks, Beam, Scan, Fire |
| Bar | The line that is always there: your name, your jobs, and where you are |
| Covering | Offered a choice that belongs to a job you do not have |

## Step 1 - Read the screen

Type nothing in this step. Read what your mission puts on the handheld today.

### The bar

Three things, always there. This is Dr Hale in the first second on the ground:

```
Dr Ines Hale | medical, science | pad
```

Her name and her jobs come from your roster: the heading, and the `Roles:` line. The
third word is where she is standing, and it is the name of a **mark** in your map file.
Hold that thought until Step 2.

When she is hurt the bar says so, and when she is down it says nothing else:

```
Dr Ines Hale | medical, science | Kesh Relay - HP 2/3
Dr Ines Hale | medical, science | DOWN - needs a medkit
```

### The eight apps

Each tile has a name and one line under it. They are the same in every mission:

```
Crew | Who is out here, and the way home
Act | What you can do here
Look | What is within reach
Pack | What you are carrying
Tasks | What is asked of you
Beam | Where the ship can put you
Scan | Read the room you are in
Fire | Arm, then click the map
```

Here is what each one lists, and which of your words it uses.

| App | What it lists | Your words in it |
|---|---|---|
| Crew | The ship, each person on the ground and where they stand, `Everyone`. For the one you pick: jobs, place, health, the last thing they said. Buttons: `Report in`, `Beam up`, `Call` and a name, `Call for help` | The title on the card, roster names, `Roles:`, mark names |
| Act | The scene that is open: every line so far, then your choices | Every `%` line and every choice |
| Look | Things in reach, as `Use` and a name, or `Talk to` and a name. Ways out, as `Go to` and an area's title. Then `Further off`: up to four things in sight. Then the last thing that happened to you | Prop and person headings, area titles |
| Pack | What you carry, as an item and a count. `Use medkit`. `Give to` and a name, for somebody standing next to you | Item keys |
| Tasks | Your own side story, then the party's quests, then `Leads`: what each quest points at and where | Quest headings, `Leads to:`, area titles |
| Beam | `To` and an area's title, for each area the ship can put you in | Area titles |
| Scan | The place you stand, then everything in sight with its `Scan:` line | Mark names, area titles, headings, `Scan:` lines |
| Fire | `SAFE` or `ARMED`, three settings, what the chosen one does, `Arm` or `Make safe` | None |

Two of those numbers were read from the game's code and not counted on a screen: Look
shows at most six things in reach and four further off, and Tasks shows at most four
leads.

Not every console has all eight. A console in a party of rooms, like Lecture 6's, has
Crew and Act, and Tasks if its person holds a story. Look, Pack, Beam, Scan and Fire
need a map to stand on.

### Act is a transcript

Act does not show one room. It keeps everything this console has read, in order. Here
is Chief Okoro's Act app after one talk and three pickups. The long first line is cut
short here:

```
Chief Okoro picked up Medical kit.
~ ~ ~
The conversation is over.
Chief Okoro picked up Pump house key.
Chief Okoro picked up Toolbox.
```

So a pickup writes a sentence, and the sentence is built from the prop's heading.
`Chief Okoro picked up Toolbox.` is true, and it is not what happened. What he has is
two fuses. That is Step 4.

### Who is offered what

All of this was played with stand-in consoles on your Lecture 12 files.

| What you wrote | Who gets it |
|---|---|
| A choice with no `if` | Everybody in the scene |
| `if medical` | The medic, when she is in the scene |
| `if medical`, and nobody in the scene is a medic | One person in the scene, with `(covering for medical)` after the words |
| `if skill science >= 3` | Only somebody that good. Nobody covers for a skill |
| `if holding fuse >= 3` | Only the one carrying them |
| `Needs: engineering` on a prop | Anybody else is told `You would need engineering for that.` |
| `For: medical` on a side story | Her Tasks app, and nobody else's. It is not on the ship's quest list |

The third row has a surprise in it. **Covering is worked out scene by scene.** Chief
Okoro walked up to Marrow alone, while Dr Hale stood on the landing pad. He was offered
her answer:

```
[Look at that cough (covering for medical)]
```

So a choice for a job is never out of reach because the right person is busy elsewhere.
If only a medic's hands will do, ask for a skill, not a job.

A scene opens for the one who clicked. With a prop's scene, a crew member standing
within two cells is brought into it as well. That last sentence is from the game's code;
the play showed it once, with two people at the terminal.

### Somebody with no job here

Now look at the mission as Lt Ross, your helm officer. Her Tasks app:

```
Party
Relight Kesh Relay
Hold at the Relay
Leads
! The beacon - Kesh Relay
```

No story of her own. At Marrow she gets the answers everybody gets, and one she is
covering. At the pump panel she is refused. Ens Vale at the terminal is the same: his
science is 2, so the door code is not even offered. Two of your five crew members have
come down to watch. That is Step 7.

## Step 2 - A mark is a word on the bar

The bar said `pad`. That is the mark `@pad` in `landing.tiles`. Any mark a crew member
can stand on is a word on their bar, in the Crew app beside their name, and at the top
of Scan. An underscore is shown as a space.

Now stand Dr Hale on the cell where the medical kit is hidden, before anybody has asked
Marrow about it:

```
Dr Ines Hale | medical, science | cache
```

The map just told her something is buried there. You named that mark for yourself in
Lecture 7's file, and it has been on screen ever since. The same walk through your other
maps gives `arrive`, `foot` and `crate`.

Two rules.

**Name a mark for the place, the way you would say it.** Open `ground\landing.tiles`
(press **Text** in the editor). Change two lines:

```
entry: landing_pad
```

```
  P: pad @landing_pad
```

In `ground\gully.tiles`:

```
entry: gully_mouth
```

```
  a: dust @gully_mouth
```

In `ground\cistern.tiles`:

```
entry: foot_of_the_stairs
```

```
  f: floor @foot_of_the_stairs
```

The gully names that last mark too, as the place its stairs come out. In
`ground\gully.tiles`, under `exits:`:

```
  to_cistern: cistern @foot_of_the_stairs
```

**Stand a hidden thing on a cell, not on a mark.** In `landing.tiles`, take the mark off
the `h` line:

```
  h: scrub
```

and in `mission.amd`, in the **Medical kit** record, change `Mark: cache` to the cell:

```
At: 6, 8
```

Do the same for the spare cell. In `cistern.tiles`:

```
  c: floor
```

and in the **Spare power cell** record, change `Mark: crate` to:

```
At: 16, 2
```

Save all four files and run lint. It says `clean`. Played again, the bar reads:

```
Dr Ines Hale | medical, science | landing pad
Dr Ines Hale | medical, science | gully mouth
```

and on the hidden kit's cell it says only `Kesh Relay`. A cell with no mark shows the
area's title.

Marks under a thing that blocks, like `door` and `tent`, are never stood on. Leave them.

## Step 3 - A title is read after "Go to"

An area's `title:` is used in five places. Here are three of them, from your Lecture 12
files:

```
Go to The Dry Gully
To The Dry Gully
! Sump crawler - somewhere not yet found
```

The first is a button in Look and the second a button in Beam. Both put a word in front
of your title, so a title that starts with `The` reads badly twice.

The third is a lead in Tasks. Once the party has found the area, the lead ends with the
area's title. The other two places are the bar and the top of Scan, when nobody is on a
mark.

In `gully.tiles` and `cistern.tiles`, change the two titles:

```
title: Dry Gully
```

```
title: Pump House Cistern
```

Played again:

```
Go to Dry Gully
To Dry Gully
! Sump crawler - Pump House Cistern
```

Look only lists a way out to an area the party knows. Your gully is `known: no`, so
until somebody has walked east there is no `Go to` button for it, and the trail sign is
the only thing that says it is there. That is by design. Know that it is so.

## Step 4 - What you pick up, and what the pack calls it

A prop you pick up is on screen under two names: its heading, and its `Item:` key.

| Where | What it showed |
|---|---|
| Look | `Use Brittle notice`, `Use Pump house door` |
| Further off | `? Pump house key - 5 E` |
| Act | `Chief Okoro picked up Toolbox.` |
| Pack | `fuse x2`, `pump key x1` |
| At the door | `pump key fits` |
| Handing over | `Handed over medkit.` |

The heading says `Pump house key`. The pack and the door say `pump key`, because that
is the item's key with its underscore turned into a space. To your crew those are two
different things.

**Make the item's key the same words as the heading.** Three lines name the pump house
key, and all three must change together. In the **Pump house key** record:

```
Item: pump_house_key
```

In the **Pump house door** record:

```
Opens with: key pump_house_key, check engineering 8, cut
```

And in Marrow's scene:

```
- [Show him the brass key](marrow_pump) if party pump_house_key
```

The relay keycard has the same fault. In the **Relay keycard** record:

```
Item: relay_keycard
```

In the **Relay door** record:

```
Opens with: key relay_keycard, check engineering 9, cut, signal relay_unlocked
```

The note above the keycard record names the old key too. Change it to match.

**Name a pickup for what ends up in the pack.** Change two headings:

```
### [Two fuses](toolbox)
```

```
### [Pim's medical kit](stash)
```

Only the words in square brackets change. The keys stay, because other lines join to
them.

Save and run lint: `clean`. Played again:

```
Chief Okoro picked up Two fuses.
pump house key x1
pump house key fits
relay keycard fits
```

Lint cannot help you with this step. Step 10 shows what happens when one of the three
lines is missed.

## Step 5 - Scenery still gets scanned

In Lecture 10 you learned that a prop with no words is scenery, and nothing offers to
use it. Scan does not know that. This is the yard through Scan, on your Lecture 12
files:

```
**Tent** - no reading
**Old Marrow** - One human. Elevated pulse, and a wet cough.
```

Scan lists everything in sight. For each thing it shows the `Scan:` line. With no
`Scan:` line it shows the description, and with neither it says `no reading`.

A `Scan:` line does not stop a prop being scenery. Give your three pieces of scenery
one each. In the **Tent** record, under `Blocks: yes`:

```
Scan: Canvas, a camp bed, and a kettle that is still warm.
```

In **The pump** record:

```
Scan: A two stage pump. No power to it, and nothing wrong with it.
```

In the **Crate** record:

```
Scan: Empty. Somebody has been using it as a seat.
```

Played again from the gully mouth:

```
**Crate** - Empty. Somebody has been using it as a seat.
**Pim** - One human, young. Cold, and not hurt.
```

A `Scan:` line is the cheapest clue you have. It costs the crew no walking. Use it to
say what a thing is for before they cross the map to find out.

## Step 6 - On the ground, a title is the whole task

On the ship, the quest log shows a quest's objective and its description. The Tasks app
does not. This is everything Dr Hale is shown about her own story:

```
Dr Ines Hale
The Caretaker's Cough
Active
Leads
! Old Marrow - Kesh Relay
```

A heading, a state, and a lead. So on the ground the heading has to be the instruction.
Change three headings in `mission.amd`. The keys stay as they are:

```
### [See to Marrow's Cough](cough)
```

```
### [Clear the Cistern Walkway](sump)
```

```
### [Bring Pim Her Tablet](pim_tablet)
```

**Clear the Yard** already says what to do. Leave it.

One more thing about `Leads to:`. The lead is shown from the moment the quest is, and
it names its target at once. Chief Okoro reads `! Sump crawler` in the first second on
the ground, before anybody knows there is a cistern. If the name is the surprise, leave
`Leads to:` off that story.

## Step 7 - The two with nothing to do

Give Lt Ross and Ens Vale a story each, and an answer that finishes it. You know every
word of this from Lecture 5.

In the Side Stories section, under the last line of the engineer's story, leave a blank
line and add:

```
### [Find a Place to Set Down](strip)
---
For: helm
Starts when: at once
Objective: Ask the caretaker where a shuttle could land
Done when: signal strip_found
Leads to: marrow
---
If the beacon cannot be lit, somebody will have to fly a new one down.

### [Hear the Last Call](last_call)
---
For: comms
Starts when: at once
Objective: Find out who the relay spoke to last
Done when: signal last_call_heard
Leads to: terminal
---
A relay does not go dark without telling somebody first.
```

Lint warns twice, `unfired-signal`, and it is right: nothing sends either signal yet.

In **Old Marrow**, under the brass key line, add:

```
- [Ask where a shuttle could set down](marrow_strip) if helm ; signal strip_found
```

and above **The Keycard**, add the room:

```
### [The Old Strip](marrow_strip)
% "South of the pad, where the scrub is flat. The supply boats used it before my time." He looks pleased that somebody asked.

- [Ask him something else](marrow)
- [Thank him]()
```

In **The Yard Terminal**, under the recognition update line, add:

```
- [Play back the last call it sent](terminal_call) if comms ; signal last_call_heard
```

and above **Nine Days**, add the room:

```
### [The Last Call](terminal_call)
% One call, nine days old, to a convoy tender that never answered: CELL FAILING. SEND A SPARE. The relay asked for help once, and then saved its power.

- [Step back](terminal)
```

Save and run lint: `clean`. Lt Ross's Tasks app now starts:

```
Lt Dana Ross
Find a Place to Set Down
Active
```

and after her answer it says `Done`.

These are jobs, so they are covered. When Dr Hale talked to Marrow alone she was
offered `Ask where a shuttle could set down`, marked as covering for helm. Taking it
sends the story's signal, whoever pressed. That is the price of using a job, and it is
why the party can never be stuck.

## Step 8 - How long is a line

Nobody has seen how much fits. What can be measured is what the shipped missions do, so
count yours against them.

| Counted | The starter | Yours, now | Dawnline |
|---|---|---|---|
| Choices | 28 | 64 | 148 |
| A choice, middle length | 19 characters | 20 | 16 |
| Nine choices in ten are under | 35 characters | 35 | 29 |
| The longest choice | 39 | 44 | 50 |
| A `%` line, middle length | 27 words | 27 words | 23 words |
| The longest `%` line | 37 words | 38 words | 74 words |
| A heading, middle length | 11 characters | 12 | 12 |

Three things from the game's code, to plan with:

- A choice that is covered grows by `(covering for medical)` and the like: up to 27 more
  characters on your longest job word.
- The first screen of the handheld shows the open scene's line above the tiles, in a
  space that scrolls. The Act app shows the whole transcript and scrolls too. So a long
  line is never cut off. It is only read less.
- In Act your choices are buttons at the end of the transcript, set one after another
  in a row that wraps. Short choices can share a row.

So keep to the starter's numbers until you have seen your own mission on a screen: a
choice under 35 characters, a line under 40 words. Your longest choice is 44 characters,
`Fit two, and bridge the third clip with wire`. It is on a prop that needs an engineer,
so it is never covered. Leave it, and look at it first when you play.

## Step 9 - What the bridge sees

Somebody stays aboard. Here is all of it.

On the ship's tablet, the **Boarding Party** screen lists who has gone:

```
Going down to Kesh Relay
Lt Dana Ross
helm
In the party
Chief Okoro
engineering
Dr Ines Hale
medical, science
Lt Sam Reyes
security
BEAM DOWN
```

The ship's quest log shows the shared quests, and nothing of anybody's side story:

```
Relight Kesh Relay
Active
Hold at the Relay
Done
```

Pim's quest joins that list when an answer starts it, and not before.

And Messages gets a line only when somebody on the ground presses **Report in**, in
their Crew app:

```
Dr Ines Hale, reporting in.
```

That is everything. No scene line reaches the bridge. So the shared quests are the
bridge's only window on the ground. Every time one starts or finishes, the bridge
learns something. Lecture 16 builds a quest tree with that in mind.

## Step 10 - Check it

Each row was tried on the finished files, one change at a time.

| The mistake | What lint says |
|---|---|
| The mark renamed in the legend, `entry:` left as it was | `tiles-entry`, an error |
| The mark taken off the legend, the record still says `Mark: cache` | `tiles-unknown-mark`: it is never placed |
| The mark renamed in the cistern, the gully's `exits:` line left | `tiles-exit` |
| `Scann:` for `Scan:` | `unknown-field`. It guesses `Scan` |
| `For: helmsman` | `for-nobody`. It lists every word that would work |
| The answer sends `strip_fond` | `unfired-signal` on the story, `signal-no-route` on the answer |

Three of those, as lint printed them:

```
  [ERROR] line 12:8: entry 'pad' is neither a mark on this map nor x, y (tiles-entry)
```

```
  [WARNING] line 212:7: cache: no mark 'cache' in landing - it is never placed (tiles-unknown-mark)
```

```
  [WARNING] line 22:3: exit to_cistern arrives at @foot, which is not a mark in cistern (tiles-exit)
```

### What lint cannot see

All of these lint `clean`. The first three were played.

| The mistake | What happens |
|---|---|
| The item renamed on the pickup, and the door still says `key pump_key` | The key does not open the door. The door goes straight to its skill check, and says nothing about a key |
| The item renamed on the pickup, and Marrow's line still says `if party pump_key` | `Show him the brass key` is offered to nobody |
| `Item: pump house key`, with spaces | The pack shows `pump house key x1`, and it opens nothing and is asked for by nothing |
| A mark name that gives a secret away | It is on the bar of anybody who stands there |
| A title that starts with `The` | `Go to The Dry Gully` |
| A pickup named for its box | `picked up Toolbox.` |
| A choice too long to read at a glance | Nobody has measured what fits |

So after any rename, search the file for the old word. In VS Code, Ctrl+F, type the old
key, and look at every line it finds.

## Step 11 - Play it

```
sbs run server,helm,comms,science -m MyAway map=0
```

This time do not play to win. Play to read.

1. All three beam down. On each console, open every tile once and press **Back**.
2. Read the bar. Walk off the pad and read it again.
3. As Lt Ross, open **Tasks**, then talk to Marrow. Find her answer.
4. As Ens Vale, walk to the terminal. Mind the sentry. Find his answer.
5. As Dr Hale, pick up the brass key by the tent. Open **Pack**, then **Act**.
6. Open **Scan** in the yard. Then walk east into the gully and open **Look**.
7. On the server window, or a fourth console left aboard, open the handheld's
   **Boarding Party** and **Quests**.

Write down every word that makes you wince. That list is your exercise.

## If something goes wrong

| What you see | Why | What to do |
|---|---|---|
| Lint says `tiles-entry` | You renamed a mark and not the `entry:` line above it | Make the two match |
| Lint says `tiles-exit` | The gully's `exits:` line still names the old mark in the cistern | Step 2 |
| The brass key no longer opens the pump house | The door's `Opens with:` still has the old item key | Step 4. Lint cannot see it |
| A story is `Done` and its owner never touched it | Somebody else took the answer as covering | Step 7. Use `if skill` if only one person may |

## Exercise

1. The marks `sentry` and `keycard` in `landing.tiles` can both be stood on. Stand on
   each in the game and read the bar. Fix them the way you fixed `cache`.
2. Read every prop heading in your file after the word `Use`, and after the words
   `picked up`. Change the ones that jar.
3. Read every `Scan:` line. Each should tell the crew something they could not see.
   Rewrite two.
4. Find your three longest choices. Can each lose five words and keep its meaning?
5. Break it and read lint: `entry: pad`; `Mark: cache`; `Item: pump_key` on the key
   only. Which one does lint miss?

Then answer on paper, from the file alone:

- Which words in your file are on the bar at some time? List the marks.
- A party of Lt Ross and Ens Vale. Which answers are they covering, and for whom?
- What does the bridge learn, and when, if nobody presses **Report in**?

## Checkpoint

You are done when all five are true:

- `sbs lint MyAway` says `clean`.
- No mark that can be stood on gives a secret away.
- The pack, the door and the heading use the same words for each key.
- Every crew member on your roster has a story or an answer of their own.
- You can say which of your words each of the eight apps shows.

## Next

Lecture 14 puts a clock on this mission. It measures how long everything takes, and
checks by hand that every party can reach every ending.

## Further reading

Nothing here is needed for Lecture 14.

- "Boarding parties" in the library documentation: "Where the crew reads it".
- "Ground tile maps" in the library documentation: the table of fields under "Placing
  things on the ground", and the paragraph on scenery.
- "The ePADD" in the library documentation, if you want to know how the ship's tablet is
  put together. You do not need it to write a mission.
