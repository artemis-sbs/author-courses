# C6-5 video script - Campaign architecture

> **STATE ON 2026-10-09.** Written and measured today against the released tools: `sbs`
> 0.13, the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions
> `b20726f`, the Open Universe engine library in `__lib__`). Everything was run by script
> in the game's stand-in (the mock), from a copy of the mission placed where its save
> cannot reach a player's own. **Nothing in this lecture has been run in the real game,
> and nobody has seen any of its screens.** The budget's counts of records are counted
> from the files. Its minutes are blanks for the student: nobody has timed the writing.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 4 leaves it: both files match `c6-04-the-episode\example\` |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| VS Code | `MyUniverse` open, both files in tabs, font size raised |
| Browser | Ready to open the bible page in scene 7 |
| Game | Closed. Started on camera in scene 8 with `sbs run server,helm,science -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-09, with the page's own files:**

1. The finished files lint `clean` and play with no errors and an empty
   `mast.runtime.log`.
2. The act walks end to end: each of Three, Four and Five of Five reveals the next on
   arrival; Five Boats is done at (0, 0) and pays 1000; afterward no step of The Long
   Count is open.
3. The walk passes through (3, 1) and (-3, -2), which finishes the Class 5 leads The
   Second Colony and The Breaking Yard.
4. A `Win:` on a step: the game-over signal fires with the sentence; the save holds the
   step as Done; a second launch continues in the system where it was won, nothing ends
   the game again, and the step stays Done.
5. `sbs docs MyUniverse --lens bible` writes one page; its block "The shape of it"
   holds the counts printed on the page.
6. Every row of the tables in Step 6: 4 variants, each linted.

**Read in the notes, not run:** Storm's Beacon's makers moving their ending as episodes
were added.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. The end-of-game screen with the `Win:` sentence, in this universe. (It was seen in
   the real game for a Class 1 mission.)
2. The bible page in a browser.
3. The Quest Log during the walk.

## Scenes

### 1. Cold open

**Screen:** The four-act table in `campaign.md`.

**Say:** "You have two evenings. | A campaign is twenty. ||| Today you'll put all twenty
on one page, | and you'll lay the first act down in the game, from its first lead to
its last. ||| And then you'll count what it's going to cost you. ||"

### 2. Acts

**Screen:** Type the four acts into `campaign.md`.

**Say:** "Twenty evenings is too many to hold in your head, | but five of them isn't. ||| So a
campaign is acts, | and an act is about five evenings with one question. ||| What
happened to the boats? | Who took the people off them? || Where did they go? | And do
they want to be found? ||| Notice how each answer is the next question. || And notice
the last row is one line. || You don't know yet what your crew will have done by then.
||"

### 3. Act One, as a table

**Screen:** The Act One table. Point down the Place column.

**Say:** "Now the act you're about to build, evening by evening. ||| Look at the place
column before anything else. || Two of these five evenings go somewhere you built in the
last class. ||| And that's quite deliberate. || A campaign that only goes to new places | teaches
the crew that nowhere matters. || So send them back. ||"

### 4. Stubs

**Screen:** `kestrel_verge.amd`. Add the `Then:` line to Three of Five. Add The Petrel.
Add Four of Five, Five of Five, Five Boats.

**Say:** "You've written two evenings in full. | The other three start as stubs. ||| A
stub is an open with nothing behind it yet. || One lead, that shows the next lead. |||
With three of them, the act can be walked from end to end tonight. || And lint can see
that every evening's joined to the one before. ||| A stub is a real evening, only a
short one. || If the crew outruns your writing, | they get a thin evening, and not a
dead end. ||"

### 5. The act's ending

**Screen:** Five Boats. Point at the missing `Then:` line.

**Say:** "The act ends at home, with a big payment, | and a text that answers the act's
question. ||| And it has no next step. || Act two isn't written, | so no new lead
appears, and that's the truth. ||| When you have evening six, you join it on here. ||
The capstone shows how to do that for a crew that's already finished. ||"

### 6. Where the ending goes

**Screen:** The table in Step 4.

**Say:** "A word about winning, because I measured it. ||| A step with a win line ends
the game the moment it's done. || The save keeps that step as done. ||| The crew can
continue afterward, | and the game simply goes on. || But that win can never happen
again, because it's been spent. ||| So a campaign has one, | on the last step of the last evening,
| and you write it last. ||"

### 7. The budget

**Screen:** `sbs docs MyUniverse --lens bible`. Open the page. "The shape of it". Then
the two count tables on the lesson page.

**Say:** "Now it's time to count. || The printed bible does some of it for you. ||| Near the top is a
block that says how many records you have, | and how many beats are on the spine. |||
Then count one evening by hand. | Four records. About ten sentences the crew reads. |||
Seventeen ordinary evenings, three tentpoles, four act endings. || That's about ninety
records, | and you've written thirteen. ||| Now write down how long evening two took
you to write, and multiply it up. || Do that before you promise anyone a campaign. ||"

### 8. Half the evening is free

**Screen:** The "Used once / There every week" table.

**Say:** "Here's the good news in that number. ||| The spine is only half an evening. ||
The other half is the universe you already built. ||| Jobs come round again every week.
| So do hails, and trade. || So you're not writing twenty evenings of things to do. ||
You're writing twenty reasons to go out there. ||"

### 9. Walk it

**Screen:** Lint: `clean`. Run the game. Engage each lead in turn to Five Boats.

**Say:** "Lint's clean, so let's walk the act. || I'm not playing. I'm checking the
joins. ||| Three of five, and four appears at once. || Four, and there's the Petrel. |
Five, and we're in the breaking yard. ||| And then we're home. || That's a thousand credits, | and every
line of the campaign is done. ||| And on the way, two old leads from the last class finished themselves, | because the spine goes through those systems. ||"

### 10. Close

**Screen:** The checkpoint list.

**Say:** "So you have four acts, one of them walkable, | and an honest number. ||| If
that number's too big, | the answer is fewer evenings, and not thinner ones. || Next
time, we give the acts something to turn on. ||"
