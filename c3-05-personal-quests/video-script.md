# C3-5 video script - Personal quests

> **RE-CUT BEFORE RECORDING (2026-10-04).** This script was written before the library
> changed, and `lesson.md` has been rewritten since. What is different now:
>
> - There is no second recipe card. Step 3 adds `stories=amd_section(MISSION_DOC,
>   "side_stories")` to the `boarding_visit` line (sbs_utils `a928fbe0`).
> - The handheld of a person who holds a story has a **Tasks** app, and it lists the story
>   under their name (sbs_utils `a37072ea`). The "Hold the recording" note below no longer
>   applies. Flagged for review: whether Tasks belongs on a rooms-only handheld was a design
>   call, and this is the recommended answer built.
> - Lint names every mistake in the first table of Step 7. Only `Leads to:` in a place of
>   rooms and `Then: reveal` of a ship's quest stay silent.
> - A `Reward:` on a side story is paid to the ship (measured: 250 -> 310 credits).
>
> **Seen in the real engine, three consoles (Engineering, Science, Helm):** each person was
> handed their story with no card; Dr Hale's handheld showed Crew, Act and Tasks; Tasks
> listed `Dr Hale / Six Names / Active` above `Party`; Helm's ship log showed `Quest
> complete: Six Names`; `mast.runtime.log` was empty; both consoles came home as their own
> stations. **Not seen:** the Tasks app after the story completes (the handheld returns to
> Act when the room changes), and anything with a player's saved name.

Target length: 18 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | The Lecture 4 mission: the crew roster with `Skills:`, the rooms, two readings, the check, the log. Lint clean |
| Library | sbs_utils `70e4d939` or later. Read "Hold the recording" below first |
| Recipe card | One new card, two parts, nothing on it to change. It is in Step 3 of `lesson.md` |
| VS Code | `MyMission` folder open, `mission.amd` in one tab and `story.mast` in another |
| Game | Closed. Started on camera in scene 8 with a server and THREE consoles: Engineering and Science to go aboard, Helm to stay on the bridge and show the ship's quest list |

**Hold the recording.** As the library stands, the boarding handheld does not list a
person's own quests in a place made only of rooms: the Tasks app opens only on a map or
in a ruin. A side story is handed over, finishes and leads on, and its owner never reads
it. The page says so plainly and the script below is written for that. If the Tasks app
is opened for every boarding party before this is recorded, scenes 1, 2 and 8 change: the
story is then on the handheld under the person's name, and that is the thing to show.

## Confirm on camera

Nothing in this lecture has been run in the real game, and no screen has been seen.

Checked on 2026-10-03 in the mock only, sbs_utils `70e4d939`, by a probe that stood in
consoles, moved the ship alongside so the lesson's own routes ran, beamed the party down
with the same two calls the BEAM DOWN button makes, pressed choices by their words, and
printed what the game's own functions returned:

1. Engineering and Science aboard, Helm on the bridge. Six Names was handed to Dr Hale and
   A Cold Core to Chief Okoro. The surgeon's reading of the suit tags finished Six Names,
   which finished Account for the Crew, and the side's credits rose by 150. The engineer's
   reading finished A Cold Core. The ship's log held `Quest complete: Account for the
   Crew`, `Quest complete: Six Names` and `Quest complete: A Cold Core`, in that order.
   The run passed with an empty `mast.runtime.log`.
2. Engineering alone. Six Names was handed to nobody. The suit tags were offered marked as
   covering for medical; taking them left Account for the Crew open. A Cold Core finished.
3. Science alone. The mirror image: Six Names and Account for the Crew finished, A Cold
   Core was handed to nobody.
4. Asked of the library, not read off a screen: with a party aboard, the handheld's apps
   are Crew and Act; the ship's quest list holds Account for the Crew and neither side
   story.
5. Every row of the page's three tables: `sbs lint` on each mistake, and what the game did
   with it.

NOT seen. If one is not as described, stop and fix the page:

6. Where `Quest complete: Six Names` is drawn, and whether the party aboard sees it at all
   or only the people left on the bridge.
7. The quest list on a real console: Account for the Crew present at the start and
   complete at the end.
8. The handheld of a person who holds a side story. The page says it shows no list of
   quests. Look for a Tasks tile.
9. What a player sees when the card's `shared SIDE_STORIES` line is missing. Headless, the
   story stops with an error on the first beam down.
10. Two real consoles beaming down one after the other, each getting their own story.

## Scenes

### 1. Cold open (0:00 - 0:45)

**Screen:** Three consoles. On Science, in the airlock, press Read the name tags on the
suits. On Helm, still on the bridge, the two `Quest complete` lines arrive.

**Say:** "The doctor just read six name tags. Nobody asked the engineer to do that. Nobody
asked the ship. It was her job, on her list, and when she finished it something happened
for everyone. That is a side story: a quest that belongs to one person."

### 2. A quest with an owner (0:45 - 3:30)

**Screen:** `mission.amd`, the end of the file. Type the Side Stories heading and the Six
Names record. Then the four-row table from the companion page.

**Say:** "A new section, at the very end. Side Stories, and the key is `side_stories`.
Keep that key. Inside it, a quest. You know every line of this from Class 1 except the
first. `For`, colon, `medical`. That is a job word, the same word that is on the doctor's
`Roles` line in your roster. This quest is not the ship's. It is hers. `Starts when: at
once`, because I want it running the moment she has it. Leave that out and she is handed
a story that is asleep, and nothing ever wakes it. An objective. And `Done when: signal
names_read`. A signal I just invented. Something has to send it."

### 3. Her own reading finishes it (3:30 - 5:30)

**Screen:** The Airlock. Put the cursor at the end of the suit tags choice. Type the comma
and `signal names_read`. Zoom on the comma.

**Say:** "Here is the choice only the doctor is offered. After the semicolon it already
says `learn suits`. I add a comma, then `signal names_read`. Two things happen now when
she takes it: the party learns the fact, and her story hears its signal. Look at this
comma. If I forget it, the signal is never sent, and lint will not tell me. I am going to
show you that in a few minutes, because you will do it."

### 4. The card (5:30 - 8:00)

**Screen:** `story.mast`. Find `shared BOARDING_SCENES`. Paste the first part below it.
Scroll to the end of the file. Paste the second part. Then the terminal: `sbs lint
MyMission`, clean.

**Say:** "The game does not hand these stories out by itself, so there is a card. Two
parts. The first goes under the line from Lecture 2 that starts `shared BOARDING_SCENES`,
with the same indent. It reads my new section and keeps it. The second goes at the very
end of the file. It says: every time somebody beams down, hand them the story that is
for them. I change nothing on this card. I paste it. Lint is clean, and I have to be
honest about what that means here: lint cannot see this card at all. If I paste half of
it, lint still says clean."

### 5. A second story (8:00 - 9:30)

**Screen:** Type A Cold Core below Six Names. Then the Reactor Room: add `, signal
core_read` to the shutdown choice.

**Say:** "The chief gets one too. `For: engineering`. Find out how the core was stopped.
And the choice only he is offered sends the signal. Same shape, different job. Two people,
two stories."

### 6. Where a story leads (9:30 - 12:30)

**Screen:** Six Names: add `Then: signal names_known`. Scroll up to the Quests section.
Type Account for the Crew. Then the two-row table (waits, sends) and the three-row `Then:`
table from the companion page.

**Say:** "A side story can lead somewhere, and it does it the way every quest does: with
`Then`. When the doctor's story finishes, it sends `names_known`. And up here, in the
ship's own quests, a new one: Account for the Crew. `Scope: shared`, running from the
start, done when it hears `names_known`. So read the chain. She reads the tags. That
finishes her story. Her story finishes the ship's quest. One waits, one sends. Notice
where the reward is. On the ship's quest. A reward written on a side story is paid to
nobody. And one thing you will see in other people's files: `Leads to`. That points a
person at a thing on a map, or a place in a ruin. We have rooms, not a map, so it does
nothing here. We will use it later."

### 7. Rules, and lint (12:30 - 15:30)

**Screen:** The five rules on the companion page. Then the terminal. Delete the comma
before `signal` in the airlock choice, lint: clean. Undo. Change `For: medical` to `For:
medcal`, lint: clean. Undo. Change `names_read` on the choice to `names_red`, lint: two
warnings. Undo. Change the section key to `side_story`, lint: a warning that nothing reads
it. Undo.

**Say:** "Five rules. A side story is a bonus: nobody covers for a person, so never hang
the main story on one. One job word in three places: the roster, the story, the choice.
Name the job, not the person. No reward on a side story. And one story goes to one
person. Now lint, and I am going to start with the two it misses. The comma. Clean. That
story can never finish. A misspelled job on `For`. Clean. That story is handed to nobody.
Those two you check by eye. Here is what it does catch: a signal name that does not match,
two warnings, one from each end. And a section key the card is not looking for."

### 8. Play it (15:30 - 17:30)

**Screen:** Server and three consoles. On Helm, open the quest list: Account for the Crew.
Fly alongside. Engineering and Science beam down. Science takes the suit tags. Cut to
Helm: the two lines, then the quest list. Back aboard: go aft, Engineering takes the
shutdown record. Then close Science, start again with Engineering and Helm only, and take
the suit tags marked as covering: on Helm, Account for the Crew stays open.

**Say:** "Before we go: the ship's quest list. Account for the Crew is waiting. Both of
them beam down. The doctor reads the tags. Back on the bridge: quest complete, twice, and
the reward. Now the same mission with the doctor left behind. The chief is offered her
reading, marked as covering. He takes it. The party learns the fact. And on the bridge,
nothing. Her story was never handed out, because she never came. That is rule one."

### 9. Your turn (17:30 - 18:00)

**Screen:** The exercise on the companion page.

**Say:** "Your third crew member gets a story of their own, finished by the reading you
gave them. Give the chief's story somewhere to lead. Then break it on purpose: misspell
the job on `For`, watch lint say clean, and play it once to see what does not happen. Next
time you put all of it together, and play ten minutes of your own away mission."
