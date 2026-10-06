# C3-3 video script - Everyone gets a menu

Target length: 16 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | The Lecture 2 mission: crew roster, three rooms, the recipe card. Lint clean |
| Library | A build with the 2026-10-03 boarding batch (committed, not yet released) |
| VS Code | `MyMission` folder open, `mission.amd` in one tab |
| Game | Closed. Started on camera in scene 7 with a server and TWO consoles, Engineering and Science, side by side |

## Confirm on camera

Checked in the real engine on 2026-10-03 by a script that called the game's own functions
and wrote what it found to a file. Three runs:

- Engineering and Science together: the Science console (Dr Hale) was offered the suit
  tags and Engineering was not; Engineering (Chief Okoro) was offered the shutdown record
  and Science was not; the bridge line and the log choice changed at two facts; reading
  the tags twice counted once; both consoles ended back at their stations.
- Engineering alone: the suit tags were offered to it as a forwarded choice.
- Engineering alone, with the exercise done (a Helm officer whose job is `quartermaster`):
  the invented job's reading was forwarded too, and stores plus shutdown opened the log.

SEEN on the real screens, 2026-10-03 (one Engineering console, driven by mouse, with the
fixes made that day - they are not released yet):

1. On the boarding handheld (the xESS), the forwarded choice is a fourth button that
   reads `Read the name tags on the suits (covering for medical)`.
2. Taking it adds to the page: who chose, what they chose, then the Six Suits line and
   one button, Step back.
3. The bar at the top names the room the party is in.

NOT seen yet. If one is not as described, stop and fix the page:

4. Two consoles in the same room show different choices.
5. When one console picks a way out, the other console's screen changes room without
   being touched.
6. The bridge line is the "cannot answer yet" one before two readings and the "now you
   know" one after.

Known: facts are kept for the rest of the mission, not for one visit. It does not matter
in this lesson, which has one visit. It is build item B34.

## Scenes

### 1. Cold open (0:00 - 0:45)

**Screen:** Two consoles side by side in the airlock. Point at the one choice only the
Science console has.

**Say:** "Same room. Same moment. Two different menus. The doctor can read something the
engineer cannot, and neither of them can open the captain's log alone. That is the whole
trick of a boarding party, and it is one word and one semicolon."

### 2. A choice for one job (0:45 - 4:00)

**Screen:** `mission.amd`, The Airlock. Type the new choice. Then type the Six Suits room.

**Say:** "A choice you already know, with two things added. `if medical`: only someone
whose job is medical is offered it. That word is the one on `Roles` in your roster. Then
a semicolon, and `learn suits`: when she takes it, the party knows a fact, and I have
named it `suits`. And the choice needs somewhere to go: a short room that says what she
found, with one way back."

### 3. The other job (4:00 - 5:45)

**Screen:** The Reactor Room. Type the choice and the Shutdown Record room.

**Say:** "The same again for the engineer. Now each of my two people has one thing only
they can read."

### 4. A door that opens when they know enough (5:45 - 8:15)

**Screen:** The Bridge. Type `- [Answer the log](last_entry) if learned >= 2`. Type The
Last Entry.

**Say:** "`learned` is a number: how many different facts the party has. The party, not
the person. So this choice appears for everyone once the surgeon and the engineer have
each done their part. And a fact counts once, however many times they read it."

### 5. A line that changes (8:15 - 9:45)

**Screen:** Replace the bridge's line with the two gated lines.

**Say:** "A party that walks here first finds a locked log. If I say nothing, they think
the game is broken. So two versions of the line, and a condition in curly brackets on
each. Too early, they are told there is more to find. Later, they are told it is time."

### 6. Three rules, and lint (9:45 - 12:00)

**Screen:** Highlight the ungated choices in each room. Then the terminal: `sbs lint
MyMission`, clean. Type `lern`, lint, undo. Type `=>`, lint, undo. Type `medcal`, lint:
still clean. Undo.

**Say:** "Three rules. Nobody gets an empty menu, so every room keeps a choice with no
`if`. A reading goes somewhere and comes back. And count your facts: two facts, and the
log asks for two. Lint. Clean. It catches a misspelled `learn`. It catches the sign the
wrong way round. It does not catch a misspelled job. That one you check by eye: every
word after `if` is `learned`, or a job from your roster."

### 7. Play it (12:00 - 15:00)

**Screen:** Server and two consoles. Alongside. Both beam down. Show the two menus. Go to
the bridge: locked. Back. Science reads the tags. Aft. Engineering reads the record.
Forward: the line has changed. Answer the log. Return to the ship. Then close Science,
start again with Engineering only, and show the covering choice.

**Say:** "Two people. The doctor has it; the chief does not. Straight to the bridge:
locked, and it says so. Back. She reads. Aft. He reads. Forward: and there it is. Now
watch what happens when the doctor stays home. Same room, one person, and her reading
comes to me, marked: covering for medical. A short crew still finishes the story."

### 8. Your turn (15:00 - 16:00)

**Screen:** The exercise on the companion page.

**Say:** "Your third crew member has a job you made up. Give them a reading on the
bridge. Leave the log at two, and now any two of three will open it: more than one way
through. Next time, we ask not only what someone's job is, but how good they are at it."
