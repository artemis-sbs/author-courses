# C3-11 video script - People and hostiles

> **STATE ON 2026-10-10. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0, with a
>   current tool and libraries.
> - **Starts from Lecture 10's finished files** in `MyAway`. Two files change:
>   `ground\gully.tiles` (one mark) and `mission.amd` (one person, one hostile, two
>   rooms, one side story). `example\` holds those two.
> - **A person and a hostile are one kind of record.** The library reads the People and
>   the Hostiles sections the same way; `Calm: yes` is the difference.
> - **Nobody is ever out of the game.** A party that is all down wakes at the area's
>   entry eight seconds later with 1 HP each. For one person alone, down is all down.
> - **A FULL shot destroys any prop**, the beacon included, and then the mission cannot
>   be won and nothing says so. Measured. The page warns in plain words; say it on camera.

> **Measured 2026-10-10, in the mock.** Tool `sbs` as installed, library as packaged
> (sbs_utils `ae05dac7`). The five steps were typed in order and linted at each one.
> Played headless with stand-in consoles: Pim's scene; the crawler stunned, cut twice
> and put down, its drop picked up, the engineer's story complete; one crew member
> downed by the crawler and stood up with a medical kit; two downed and waking at the
> entry. Then 16 one-change variants, each linted, and the ones lint is silent about
> played. The stand-ins were put beside things by the probe to save the walk, and a
> crew member's HP was taken away by the probe for the revive test. The shots went
> through the Fire app's own arming call and a map click.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyAway` with Lecture 10's files. Lint clean |
| VS Code | `MyAway` folder open; `mission.amd` at the People section; `gully.tiles` in a second tab |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 7 with a server, Engineering, Weapons and Science |

## Confirm on camera

1. Lint is `clean` after each of the five steps. (Lint.)
2. A click on Pim opens her room; the Scan line for her is the `Scan:` field. (Mock.)
3. The crawler: a stun reports `stunned`, each cut `wounded`, a full `down`. When it is
   down it leaves the map, a pickup named `tablet` is on its cell, and The Thing in the
   Sump is complete. (Mock, by script.)
4. A strike tells the one hit: `Hit by Relay sentry - 2 of 3 left.`, then `1 of 3
   left.` (Mock, from the sentry.)
5. A FULL shot at the yard terminal, and one at the beacon: each is gone from the map,
   and the game does not end. (Mock.)
6. A medical kit used from the next cell: `Chief Okoro is back on their feet.`, with 2
   HP. Two crew down: still down five seconds later, both at 3, 1 with 1 HP ten seconds
   later. (Mock; the HP was taken by the probe.)
7. Every row of the page's tables. (Lint, Mock.)

Not seen by anyone. If one is not as described, stop and fix the page:

1. The Fire app: three settings, **Arm**, the loud ARMED line, **Make safe**. (Read from
   the library's source.)
2. A figure walking a patrol, chasing, and a crew figure lying down.
3. The Pack app's **Use medkit** button, and whom it offers to use it on.
4. A face beside a person's words in the Act app.
5. The Tasks app marking the story complete.
6. What a person looks like when `Face:` is a word the game does not know.
7. The + Entry form and the paint click for the `camp` mark in `gully.tiles` (read from
   the add-on's source, as in Lecture 8).

## Scenes

### 1. Cold open

**Screen:** The gully: a figure sitting against a rock. Then the cistern: something low
moving along the far side of the water, and a crew figure at the foot of the stairs.

**Say:** "Two maps of yours are still empty of people. || Today there's somebody in the
gully to talk to, | and something in the cistern you can't talk to at all. ||| They turn
out to be the same kind of record, | with one line between them. ||"

### 2. A person

**Screen:** `gully.tiles`: + Entry, scrub, camp, m; paint cell 5, 8. Then `mission.amd`,
the People section: type Pim. Highlight `Calm: yes` and `Talk scene:`.

**Say:** "Pim belongs to a spot, | so first she gets a mark. || Then her record, under Old
Marrow's. ||| Area and Mark put her on the map, | the way they put a prop there. || Sprite
is her figure. | Face is the face shown beside what she says. ||| And these two lines are
the ones that matter. || Calm, and then yes, | means she never attacks. || And Talk scene
is the key of the room a click on her opens. ||| A person says Talk scene, | and a prop
says Scene. | Lint tells you if you mix them up. ||"

### 3. What she says

**Screen:** The end of the file: type the two rooms.

**Say:** "Her rooms go at the end of the file, | and there's nothing new in them. || She
came out here to start the pump, | and something below took her tablet. ||| Next lecture
gives her a great deal more to say. ||"

### 4. A hostile

**Screen:** The Hostiles section: type the sump crawler. The table of seven fields from
the page. Then `cistern.tiles` in the editor: the crawler and its dashed patrol loop.

**Say:** "Now the crawler, under the sentry. || Look at what's missing. | There's no Calm
line, | and that's all it takes to make a hostile. ||| HP is how much hurt it can take. ||
Damage is how much it does with each strike. || Notice is how close you can get before it
sees you, counted in cells. || Patrol is the walk it takes. | And Drops is what it leaves
behind. ||| A hostile walks its patrol | until a crew member is close enough and in view.
|| Then it chases them, | and strikes every two seconds from the next cell. ||| So think
about where you put it. || This one keeps to the east end of the walkway, | well away from
the stairs. | A party that arrives has room to stop and look. ||"

### 5. A quest it finishes

**Screen:** The Side Stories section: type The Thing in the Sump. Highlight the `Done
when:` line and `Leads to:`.

**Say:** "When a hostile goes down for good, | the game sends a signal by itself. || The
name is hostile, down, and the record's key, joined with underscores. ||| So a quest can
wait for it, | with no answer and no card. || This one is a side story for the engineer.
||| And Leads to finally has something to point at. | It's the key of the thing on the map
this story is about. ||"

### 6. A fight, and getting hurt

**Screen:** The table of three settings. Then the two ways back up, from the page.

**Say:** "Every crew member carries a weapon, | and it's the Fire app on the handheld. ||
Pick a setting and press Arm, | and the next click on the map is a shot. || One shot, and
it's safe again. ||| Stun holds a hostile still. || Cut takes one point off it. || And
full puts it down, | whatever it had left. || Full also destroys any thing it hits, the
beacon included, | so keep it for what's attacking you. ||| The crew has three points
each. || At nothing, you're down, | and you can't walk or act. ||| Somebody beside you
with a medical kit can stand you up. || And if everybody is down, | the whole party wakes
at the entry eight seconds later, | with one point each. ||| So nobody is ever out of the
game. | But one person alone wakes up next to whatever put them down. ||"

### 7. Play it

**Screen:** `sbs run server,engineering,weapons,science -m MyAway map=0`. Talk to Pim.
Open the pump house. Down the stairs. Scan. Fire: stun, cut, cut, full. The tablet. The
engineer's Tasks app.

**Say:** "Three consoles this time. || The doctor talks to Pim. ||| Then two of them go
down the stairs, | and stop at the foot. || Scan tells them what's in sight. ||| From the
weapons console: | stun, then cut, twice, and then full. || And down it goes. | There's a
tablet on the walkway where it fell, | and the engineer's story is complete. ||"

### 8. What lint can't see, and your turn

**Screen:** The second table on the page. Then the exercise.

**Say:** "Lint knows a lot here. | It knows the names of those signals, | and it knows a
crawler can't stand in water. ||| It can't see a missing Calm line, though. | Leave that
line out, | and Pim attacks the first crew member who walks up. || And it can't see a Talk
scene that names no room. | You click her, and nothing happens. ||| For the exercise, make
the crawler tougher, then gentler, | and play each one. ||| Next time, Pim wants that
tablet back. ||"