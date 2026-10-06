# C3-4 video script - Crew and skills

Target length: 18 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | The Lecture 3 mission: the crew roster, the rooms, two readings, the log. Lint clean |
| Library | sbs_utils `0d127f6e` or later (released 2026-10-03): it reads `Skills:` with the roster and lints skill gates and checks. On an older library the numbers do nothing |
| Recipe card | None. `story.mast` is not opened in this lecture |
| VS Code | `MyMission` folder open, `mission.amd` in one tab |
| Game | Closed. Started on camera in scene 7 with a server and TWO consoles, Engineering and Science, side by side |

## Confirm on camera

Checked on 2026-10-03, after the library began reading `Skills:` by itself (sbs_utils
`f3d4e831`, `0d127f6e`):

- **In the real engine, with a server and two real consoles** (Engineering and Science),
  the lesson's `mission.amd` and a `story.mast` with NO skills line in it. A probe moved
  the ship alongside so the lesson's own route called `boarding_visit`, beamed both
  consoles down, and wrote what the game's own functions returned to a file:
    1. Chief Okoro is engineering 4 and science 1; Dr Hale is medical 4 and science 3.
    2. On the bridge, Pull the sensor record is offered to Science and not to Engineering.
    3. In the reactor, Try to wake the core is offered to both. With the die fixed at 5,
       Okoro lands in The Core Turns Over and the party learns `lockout`; Hale lands in
       The Board Stays Dark and learns nothing. With real dice, both rooms were reached.
    4. Both consoles went home to their own stations, and `mast.runtime.log` was empty.
- **SEEN, one screenshot of each console standing on the bridge:** the handheld's bar
  reads `Chief Okoro / engineering / The Bridge` on one and `Dr Hale / medical / The
  Bridge` on the other. Engineering has two buttons, Go back to the airlock and Return to
  the ship. Science has three: Pull the sensor record first. The roll lines sit in the
  transcript, one to a line, above the room's own line, and each fits on one line at this
  width. Nothing on the handheld shows a person their own skill numbers: the only number
  a player sees is in a roll line. Say so on camera.
- **In the mock:** over 2000 real rolls each at target 9, Okoro 58%, Hale 18%; no roll
  was helped by the other person. Every row of the page's lint table was re-run against
  the current linter.

NOT seen. If one is not as described, stop and fix the page:

5. A real roll made by pressing the button, and the room that follows it (the probe made
   the rolls; nobody pressed anything).
6. Engineering alone: the suit tags marked as covering, and no sensor record.
7. A player with a saved name at an unlocked seat. Fixed in the library and covered by a
   unit test (`tests/test_boarding_roster_skills.py`); not tried with a real saved name.

## Scenes

### 1. Cold open (0:00 - 0:45)

**Screen:** The reactor room on two consoles. The Science console tries the core. A roll
line appears, then The Board Stays Dark. The Engineering console tries. Another roll line,
then The Core Turns Over.

**Say:** "Same button. Two people. One of them is the chief engineer and one of them is a
surgeon, and the ship can tell the difference. Last time a choice asked what your job is.
This time it asks how good you are."

### 2. Skills on the roster (0:45 - 3:15)

**Screen:** `mission.amd`, the crew roster. Type the two `Skills:` lines. Then the scale
table from the companion page.

**Say:** "One new line each. `Skills`, colon, then a list: a word, a number, a comma. The
chief: engineering four, science one. The doctor: medical four, science three. The word is
the name of the skill and you can invent your own, as long as it is one word. The number
is how good they are. I use a scale that tops out at four. Two means you do it for a
living, and here is something the game gives you for nothing: a job counts as two. The
chief was already engineering two before I typed anything. Now look at the doctor. Her job
is medical. Science is not her job. She is just good at it."

### 3. Nothing to paste (3:15 - 4:00)

**Screen:** Terminal: `sbs lint MyMission`, clean. Stay on `mission.amd`.

**Say:** "Lint is happy, and that is all there is to it. The game reads these numbers with
the rest of the roster. I do not open the other file today. One thing worth knowing: the
numbers belong to the person on the roster, not to the name on the screen. If a player
has saved a name of their own and sits in the doctor's chair, they are still as good as
the doctor."

### 4. A choice for someone good enough (5:30 - 8:30)

**Screen:** The Bridge. Type the sensor record choice. Type The Sensor Record room. Then
the three-row table: job, skill, no `if`.

**Say:** "On the bridge, a new choice. `if skill science`, at least three. Four parts: the
word `skill`, which skill, a sign, a number. The doctor has science three, so she is
offered it. The chief has science one, and is not. And here is the difference from last
time. When a job is missing from the party, one console covers for it. Nobody covers for a
skill. If the doctor stays on the ship, the sensor record is on nobody's menu. So a skill
choice is a bonus. Never put the only way forward behind one."

### 5. A choice anyone may try (8:30 - 12:00)

**Screen:** The Reactor Room. Type the check choice slowly, pausing on each part. Type the
two rooms. Then the odds table.

**Say:** "Now the other kind. No `if` at all, so everyone is offered it. After the
semicolon: `check engineering 9`. The game rolls a number from one to ten and adds your
engineering. Nine or more, it works, and the party goes to the room in the brackets. Then
`else`, and the room for when it does not work. So this one choice needs two rooms, and I
write the failure as carefully as the success, because half my players are going to read
it. Last part: a comma, and `learn lockout`. Anything after the check, after a comma, only
happens when the check worked. The odds: target nine, skill four, six times in ten. Skill
zero, two in ten. Twelve is hard. Six is easy."

### 6. Rules, and lint (12:00 - 14:30)

**Screen:** The four rules on the companion page. Then the terminal: lint, clean. Type
`Skill:` with no `s`, lint, undo. Take the comma out of a `Skills:` line, lint, undo.
Delete the 9 from the check, lint: a warning that nothing is rolled. Undo. Change
`core_dead` after `else` to `core_ded`, lint: a warning that a failed roll has nowhere to
go. Undo. Take the word `skill` out of the bridge choice, lint: a warning that a job is
one or zero. Undo.

**Say:** "Four rules. A skill choice is a bonus. A check has an `else`, and both rooms
lead back. Before the check always happens, after it only on success. And the numbers go
with the seat, whatever the player calls themselves. Lint. A misspelled `Skills`. A
missing comma: it tells me that entry is dropped. A check with no number: nothing would be
rolled, and it would always work. An `else` that points at a room I never wrote: that one
would end the visit, and only on a failed roll, so I would not find it by playing once.
And `if science` at least three, with the word `skill` left out: science on its own is a
job, and a job is one or zero. Lint reads all of these. Two things it cannot know: a skill
you misspelled on the roster itself, and a number nobody has."

### 7. Play it (14:30 - 17:15)

**Screen:** Server and two consoles. Alongside. Both beam down. Forward to the bridge:
show the two menus. Back, aft to the reactor. Science tries the core: point at
`engineering 0` in the roll line. Step back. Engineering tries: point at `engineering 4`.
Then close Science, start again with Engineering only, and show the bridge with no sensor
record.

**Say:** "The bridge. The doctor has the sensor record. The chief does not. The reactor.
The doctor tries. There is her roll: engineering zero, and the board stays dark. The chief
tries. Engineering four. That four is the number I typed on the roster, and that is the
thing to look for: if it says two, that person's `Skills` line is not being read, and lint
will tell you why. Now the chief alone. The suit tags arrive marked as covering for medical. The sensor
record does not come to anyone."

### 8. Your turn (17:15 - 18:00)

**Screen:** The exercise on the companion page.

**Say:** "Your third crew member gets two skills. Give them a choice only they can see and
a check anyone can try. Then break it on purpose: take the `s` off one `Skills`, read what lint
says, and play it once to see what that person loses. Next time, one of these people gets a
quest that is theirs alone."
