# C3-3 video script - Everyone gets a menu

> **STATE ON 2026-10-09. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0 from
>   Steam or itch.io, with a current tool and libraries.
> - **Starts from Lecture 2's finished files** in `MyBoarding`. Only `mission.amd`
>   changes, so `example\` holds that one file.
> - **The Last Entry is the second room with a way home.** The other rooms have a way
>   back only, as Lecture 2 set out.

> **Measured 2026-10-09, in the mock.** Tool `sbs` as installed, library as packaged
> (sbs_utils `ae2bbf4a`). The steps were typed onto Lecture 2's files and linted at each
> one. The finished file was played headless with stand-in consoles: two aboard, then
> each alone. Then 22 one-change variants: each linted with the installed tool, and every
> party (each console alone, and both) walked through it with the library's own choice
> and answer functions. No engine, no window.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyBoarding` with Lecture 2's files. Lint clean |
| VS Code | `MyBoarding` folder open, `mission.amd` in one tab |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 7 with a server, Helm, Engineering and Science, the last two side by side |

## Confirm on camera

1. Lint is `clean` after every step. (Lint.)
2. In the airlock Dr Hale is offered the suit tags and Chief Okoro is not; in the reactor
   room Chief Okoro is offered the shutdown record and Dr Hale is not. (Mock.)
3. On the bridge with fewer than two facts the line is the "cannot answer yet" one and
   the log is not offered; with two it is the "now you know" one and the log is offered
   to both. Reading the tags twice counts once. (Mock.)
4. Engineering alone: the suit tags are a fourth button reading
   `Read the name tags on the suits (covering for medical)`; nine presses reach the last
   entry and home. Science alone is offered the shutdown record the same way. (Mock.)
5. Every row of both tables on the page. (Lint, and every party walked.)

Seen on a real screen by the earlier pilot, with one Engineering console: the covering
button with those words, the page gaining who chose, what they chose, and the next line,
and the bar naming the room.

Not seen by anyone. If one is not as described, stop and fix the page:

1. Two real consoles in the same room showing different buttons.
2. One console's press changing the other console's screen.
3. The bridge line changing between the first visit and the second.

## Scenes

### 1. Cold open

**Screen:** Two consoles side by side in the airlock. Point at the one button only the
Science console has.

**Say:** "Same room. Same moment. Two different menus. || The doctor can read something
the engineer can't, | and neither of them can open the captain's log alone. ||| That's the
whole trick of a boarding party, | and it costs you one word and one semicolon. ||"

### 2. A choice for one job

**Screen:** `mission.amd`, The Airlock. Type the new choice above the others. Then type
the Six Suits room under the airlock.

**Say:** "Here's a choice of the kind you already write, | with two things added on the
end. || The first is the word if, and then medical. | Only someone whose job is medical is
offered this. || That's the word on the Roles line in your roster, | so this one belongs
to Dr Hale. ||| The second comes after a semicolon. | Learn, and then a name I've made up.
|| When she takes it, the party knows a fact. ||| And the choice needs somewhere to go, |
so I write a short room that says what she found, | with one way back. ||"

### 3. The other job

**Screen:** The Reactor Room. Type the choice and the Shutdown Record room.

**Say:** "Then the same again, for the engineer. || A choice in the reactor room that only
engineering is offered, | a fact with its own name, | and a short room to hold what he
reads. ||| So now each of my two people has one thing that only they can read. || And
notice the shape, because you'll use it again and again. | A reading goes somewhere, says
one thing, and comes straight back. ||"

### 4. A door that opens when they know enough

**Screen:** The Bridge. Type the `Answer the log` choice. Type The Last Entry at the end
of the file. Highlight its `Return to the ship`.

**Say:** "Now the lock. On the bridge I add a choice with a different kind of condition.
It says learned, then at least, then two. ||| Learned is a number. | It's how many
different facts the party has. || The party, mind, and not the person, | so the surgeon's
reading and the engineer's both count. || And a fact counts once, | however many times
they read it. ||| Behind the lock is the last room of this story, | so it's the second
room that gets a way home. ||"

### 5. A line that changes

**Screen:** Replace the bridge's line with the two lines that start with a percent sign
and curly brackets.

**Say:** "There's one more thing to fix. || A party that walks to the bridge first finds a
room with nothing to do, | and they'll think the game is broken. ||| So I write the line
twice, | with a condition in curly brackets on each. || Too early, they're told there's
more to find. | Later, they're told it's time. || A room should never leave the party
wondering whether it's finished. | If there's more to find, say so in the room. ||"

### 6. Three rules, and lint

**Screen:** Highlight a choice with no `if` in each room. Then the command prompt:
`sbs lint MyBoarding`, clean. Type `lern`, lint, undo. Type the sign backwards, lint,
undo. Type `medcal`, lint: still clean. Undo.

**Say:** "Three rules. Nobody gets an empty menu, | so every room keeps a choice with no
condition. || A reading goes somewhere and comes back. || And count your facts: | I have
two, and the log asks for two. Lint is clean. || It catches a misspelled learn. | It
catches the sign the wrong way round. ||| It does not catch a misspelled job. | It says
clean, and nobody is ever offered that reading. || So check that one by eye. | Every word
after an if is the word learned, | or a job from your roster. ||"

### 7. Play it

**Screen:** `sbs run server,helm,engineering,science -m MyBoarding map=0`. Alongside.
Both beam down. Show the two menus. Go to the bridge: no log. Back. Science reads the
tags. Aft. Engineering reads the record. Forward: the line has changed. Answer the log.
Return to the ship. Then start again, beam down Engineering only, and show the covering
button.

**Say:** "Two people aboard. The doctor has the button, and the chief doesn't. || Straight
to the bridge: | no log, and the line says why. Back. | She reads the tags. Aft. | He
reads the record. Forward again, | and the line has changed, and there's the log. ||| Now
watch what happens when the doctor stays on the bridge. || Same room, one person, | and
her reading comes to me, marked as covering for medical. || A short crew still finishes
the story. || And the covering only happens for a job, | one that's on your roster, or one
of the game's standard jobs. || A word that's nobody's job isn't offered to anyone. ||"

### 8. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Your third crew member has a job you made up. || Give them a reading on the
bridge, | and leave the log at two. || Now any two of three readings will open it, | so
there's more than one way through. ||| Next time, we ask not only what someone's job is, |
but how good they are at it. ||"