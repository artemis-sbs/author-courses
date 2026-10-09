# C5-9 video script - Organizing a big universe

> **STATE ON 2026-10-09.** Written and measured against the released tools: `sbs` 0.13,
> the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions `b20726f`, the
> Open Universe engine library rebuilt 2026-10-08 from `421ff4a`). The game side was run
> by script in the game's stand-in (the mock), from a copy of the mission placed where
> its save cannot reach a player's own. `sbs docs` and `sbs site` were run for real, on
> the page's own files, and their output was read as text. **Nothing in this lecture has
> been run in the real game, nobody has seen any of its screens, and nobody has looked
> at the printed pages in a browser.**

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 8 leaves it: `kestrel_verge.amd` matches `c5-08-captains-and-rivals\example\` |
| A copy | The whole `MyUniverse` folder copied somewhere safe |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | `MyUniverse` open, the file list showing, font size raised |
| Browser | Ready to open a file from `MyUniverse\__docs__` and `MyUniverse\__site__` |
| Game | Closed. Started on camera in scene 10 with `sbs run server,helm,comms -m MyUniverse map=0` |

## Confirm on camera

**Measured, with the page's own files:**

1. Lint reads six `.amd` files and gives three warnings, all about `ledger_read`, and no
   error. The same files with the Deepwell's call left in the main file under the fenced
   chapter give five other warnings and not those three.
2. In the mock the split universe plays with no errors and an empty `mast.runtime.log`.
   The game holds six jobs, twenty-three conversation records, two captains, one cast
   member, and the story as before.
3. Hollin Compact is sent the same buttons as in Lecture 8. After the levy: `Patrol
   (240 cr)` and `Escort (300 cr)`.
4. The game has a lifeform named Kestrel Traffic with the scene `traffic_hail`, and that
   scene gives one of the two greetings.
5. The Library is offered one source, `Codex`, from `lore.amd`, with four pages: The
   Kestrel Verge, The Three Colonies and The Gleaners under it, and Kestrel Relay.
6. `sbs docs` writes the four files named on the page. `sbs site` writes seven pages and
   indexes 67 records. With `--profile player` the conversation pages have no `earns` in
   them. The bible lists The Assay Ledger as reached from Deepwell Hail, by signal.
7. Every row of the two tables in Step 8: 46 variants linted, 22 of them played. Three
   `File:` lines in the Dialogue chapter leave only the Gleaners' eight records.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. **How the crew reaches Kestrel Traffic on Comms.** The page says plainly that it
   cannot tell the student. Find it on camera, then fix Step 9 and scene 10.
2. The Library on the handheld with a chapter called Codex, and how two hashes look
   there.
3. The four editions in a browser, and printed.
4. The website's menu, its search, and a click through a conversation.
5. The Assay Ledger closing in the real game with the call in a file of its own.
6. What the real game shows for a chapter file with three hashes: an error page, or a
   line in a log.

## Scenes

### 1. Cold open

**Screen:** `kestrel_verge.amd` scrolled from top to bottom, fast. Then the file list
with `jobs.amd`, `lore.amd` and the `dialogue` folder. Then the printed book in a
browser.

**Say:** "Your universe file is four hundred lines long. || It works, and it's getting
hard to find anything in. ||| Today we tidy up. || The jobs get a file of their own, |
and so does each side's dialogue. ||| And then there's a reward for the housekeeping. ||
We print the whole world, as a book, a script, and a website. ||"

### 2. A chapter that reads from a file

**Screen:** The four lines in Step 1 of the page: the Jobs heading, the fence, `File:
jobs.amd`.

**Say:** "Here's the whole idea, in four lines. || A chapter heading, a fence, | and
inside it, File, and a file's name. ||| When the game starts, it reads that file, | and
puts its records into this chapter. || As far as the game's concerned, | you typed them
right here. ||| There are three rules, and I'll show you each one as we go. ||"

### 3. Move the jobs

**Screen:** New file `jobs.amd`. Cut the six jobs from the main file, paste. Replace All
`### [` with `# [`: six changes. Then give the Jobs chapter its fence.

**Say:** "A new file, jobs dot a m d. || I cut the six jobs out of the main file, and
paste them in. ||| Now for rule one. || In the main file, a job has three hashes, | because
it sits under a title and a chapter. || In a chapter file there's no title and no
chapter. || So every record here starts with one hash. ||| Replace All does it, | and it
tells me six changes, which is how many jobs I have. ||| Back in the main file, the
chapter gets its fence. ||"

### 4. Move the conversations

**Screen:** New folder `dialogue`, three files. Move the records by speaker. Replace All
in each. The Dialogue chapter's fence with three names on one line.

**Say:** "Dialogue is the big one, with twenty records. || I'm sorting them by who's
speaking, | one file for each side, in a folder. ||| A captain's lines go with her
side. || That's a habit, not a rule. ||| And here's rule two. || Three files, one line,
with commas. ||| Don't give each file a line of its own. || If you do, the game reads
only the last, | and lint doesn't say a word. ||"

### 5. Three warnings that are wrong

**Screen:** `sbs lint MyUniverse`. Six file names, three warnings. Highlight
`ledger_read` in each.

**Say:** "Now lint, and it's not clean. || Three warnings, and they're all about one
word. ||| Remember the signal from Lecture Seven. || An answer sends it, and a story
beat waits for it. || Those two are in different files now, | and today, lint reads
signals one file at a time. ||| So it tells each file the other half is missing, and it
isn't. || The game reads everything into one universe before it runs. ||| I'd rather
show you this than hide it. || For this lecture, done means these three and no others.
||"

### 6. Don't do it by halves

**Screen:** The note in Step 4 on the page. Then, briefly, the Deepwell records pasted
back under the fenced chapter and lint's five other warnings.

**Say:** "You might think, I'll leave the miners' call in the main file, next to the
beat. || That's rule three, and it doesn't help. ||| A chapter reads from files, or it
holds records. || Do both, and the game's happy, | but lint gets five different
warnings, also wrong. ||| So it's all in, or all out. || If you really want a clean
lint, | leave the dialogue chapter whole and split only the jobs. ||"

### 7. A voice from anywhere

**Screen:** Add the Lifeforms chapter and Kestrel Traffic. Then the three records at the
end of `dialogue\hollin.amd`.

**Say:** "One new thing for the crew. || A captain is hailed at a station. | A member
of the cast doesn't need one. ||| This is the relay's duty voice. || It has a face, a
color, | and a scene, which is the record that speaks for it. ||| The scene goes in a
dialogue file, like any other. || Notice there are no guards. || The cast keeps no
standing, | so use them for what a crew should always be able to find out. ||"

### 8. Lore

**Screen:** New file `lore.amd`. Type the four pages. Highlight that there are no
fences.

**Say:** "And one more file, called exactly lore dot a m d. ||| There are no fences in
this one. || A heading is a page, | and the words under it are what the crew reads. |||
The crew's handheld has a Library, | and this file becomes a chapter in it. ||| Put in
what somebody who lives here would know. || Keep the secrets of your story out. ||"

### 9. Print the world

**Screen:** `sbs docs MyUniverse --title "The Kestrel Verge" --lens all`. Open the prose
edition, then the screenplay, then the bible at The Assay Ledger. Then `sbs site
MyUniverse --emit site`, and `index.html`.

**Say:** "Now for the reward. || s b s docs, the folder, a title, | and I ask for all four
editions. ||| The prose one is the book. || The catalog sorts everything by kind. ||
The screenplay is only the conversations. | Read one aloud. It's the best test there
is. ||| And the bible is the plot. || Look at this beat. | It knows the call leads
here, across the two files. ||| Then there's the website. || One page for each file, a search
box, | and every answer is a link to where it goes. || Zip the folder and send it to
whoever's writing with you. ||"

### 10. Still the same game

**Screen:** `sbs run server,helm,comms -m MyUniverse map=0`. Comms on Hollin Compact:
the same buttons. Pay the levy. The handheld: Library, Codex.

**Say:** "And the game is the same game. || There's the same station, with the same
buttons. || The levy comes from one file now, and the jobs from another. ||| Here's
the Library, with my pages in it. ||| So, a last word about lint. || After a split,
it's noisier, | and it misses a couple of things it used to catch. || The list on the
page is longer today for that reason. ||"

### 11. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Split your universe, and account for every warning
lint gives you. || Write a voice anyone can ask for directions, | and four pages of
lore. ||| Then print the screenplay, and read one conversation out loud. || Change a
line because of what you heard. ||| Next time, the crew gets off the ship. ||"
