# C5-11 video script - A ruin on the map

> **STATE ON 2026-10-10, evening.** Written and played against the libraries of that
> morning (sbs_utils `ae05dac7`, LegendaryMissions `b37a320`). Lint, and every row of
> Step 5's tables, were measured again that evening on the released tool `sbs` 0.14 and
> libraries (sbs_utils `ed811ecb`, LegendaryMissions `cc9cd06`, Open Universe
> `80e9397`); the plays were not run again. Everything was run by script in the game's
> stand-in (the mock), from a copy of `MyUniverse` placed where its save cannot reach a
> player's own. A script sent the Quest Log's Engage, moved the ship to the ruin's
> mouth, connected one stand-in console and seated it at Comms, pressed the Boarding
> Party app's own button, put the suit at two places in the ruin, and used the suit's
> own tool on the slab. **The copy could not reach the art packs, so the suit was the
> stock shuttle and the ruin's walls were the stand-in's. Nothing in this lecture has
> been run on a real console, and nobody has seen any of its screens.** In the real
> game's server, with no console attached, the library's own ruin test offered suits at
> the door and finished a quest from a cut barrier and a collected piece.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 9 leaves it. `story.json` has the line with `boarding` in it |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | `MyUniverse` open, `kestrel_verge.amd` in a tab, font size raised |
| Game | Closed. Started on camera in scene 7 with `sbs run server,helm,comms,science,weapons -m MyUniverse map=0`, and again in scene 9 |

## Confirm on camera

**In the mock, by script, on 2026-10-10, with the page's own files:**

1. The finished seven files lint `clean`. `Done when: signal slab_open`, `signal
   bowl_taken`, and `relic_piece` left off the niche each give exactly one warning
   (`unfired-signal`), on the step that waits.
2. At the start the Quest Log is handed four leads. Engaging A Hole in the Chart puts
   the ship at 2, -3; the game is asked to show "Location charted: The Hollow"; the lead
   is Done and Cut Through is Active. The ruin is built.
3. With the ship 29,882 from the entrance, no ruin is offered. With the ship 600 from
   it, the ship is offered the ruin `hollow`, called The Hollow, and the seated
   console's Boarding Party button reads SUIT UP.
4. Pressed: the crew member is out, in the room `mouth`. The suit's Nav list is The
   Gallery Door and The Niche.
5. With the suit at The Gallery Door, its targets are The Fallen Slab, a barrier, 450
   away, tool `beam`. The beam is a 12 second job. Afterward the barrier is open,
   `slab_opened` was sent, Cut Through is Done, credits 600, and What the Hollow Kept
   is Active.
6. With the suit at The Niche the piece is taken, `hollow_taken` was sent, the step is
   Done, credits 900. COME ABOARD puts the crew member back at Comms.
7. With the ship 9,000 from the entrance the offer is gone.
8. Home and back in the same game: the ruin is built again with the slab open and no
   piece; neither signal is sent again; credits 900.
9. A second launch on the same save: the ship at 2, -3, the ruin built, the slab open,
   the niche empty, credits 900, all three steps Done. The save holds the ruin's state.
10. Step 5's tables: 16 variants linted, 14 of them played with a shorter script that
    opened the slab and carried the piece out by the library's own calls. One of the 14
    is the stock-shuttle line in "If something goes wrong".

**Read in the game's guides, not run:** the 3,000 and 3,450 distances; that the way in
is a contact on the map; that a ship's beams open a barrier; that ordinary loot returns.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. Every screen: the ruin, the handheld, the suit's apps.
2. The exosuit, and the known fault with it. If a console closes when the suit appears,
   say so on camera and use the way round it on the page.
3. A suit flown by a person from the mouth to the Gallery door. The script put it
   there.
4. How the bowl is taken at a console: by flying into it, or by the TETHER tool.
5. Science scanning anything inside.

## Scenes

### 1. Cold open

**Screen:** The main screen inside The Hollow. Then a handheld with SUIT UP on it.

**Say:** "Every place in your universe so far | is somewhere the crew looks at from the
bridge. ||| This one they fly into. || And then one of them gets out. ||| By the end of
this lecture | your universe has a ruin in it, | and a story that runs through its
rooms. ||"

### 2. What a universe needs of a ruin

**Screen:** The first table in Step 1 of the page.

**Say:** "Writing a ruin is a whole class of its own. || So today I'm handing you one,
finished. ||| What we're learning is how a universe holds it. || A ruin in a universe
never says where it is. | The landmark says that. ||| It needs one place marked as its
entrance. || And it needs two keys. | One on the thing that blocks the way, | and one
on the ruin itself. ||"

### 3. The ruin's file

**Screen:** New file, `hollow.amd`. Paste. Scroll slowly: the three rooms, The Way In,
The Fallen Slab, The Niche, the bowl.

**Say:** "A new file, called hollow. || I paste the whole ruin in. ||| Don't read every
line, just read its shape. ||| Three rooms, joined by passages, | and one way in. || A slab,
fallen across one doorway. || And behind the slab, a niche with a stone bowl in it. |||
The bowl is an item, | and it lives in this file with the ruin. ||"

### 4. The landmark

**Screen:** `kestrel_verge.amd`, the Landmarks chapter. Type The Hollow. Highlight
`Relic:` and `Relic file:`.

**Say:** "Now the landmark, in the universe file. || It's a landmark like any other, |
with two more lines. ||| Relic, and the ruin's key. || Relic file, and the name of the
file. ||| That's the whole join. || And there's no terrain line, | because a ruin
brings its own cloud. ||"

### 5. Three steps of story

**Screen:** The Narrative chapter. Type the three steps. Highlight `signal slab_opened`
and `signal hollow_taken`.

**Say:** "And now the story. || A lead that takes the crew there. || A step that's done
when the slab is cut. || And a step that's done when the bowl is taken. ||| Look at
those two signals. || I didn't make them up, | and nothing in my files sends them, |
because the game does. ||| It builds each word from a key in the ruin's file. || Slab, then
opened, and hollow, then taken. ||"

### 6. Lint

**Screen:** Save all. `sbs lint MyUniverse`: seven files, each one `clean`. Then change
`slab_opened` to `slab_open`, run lint again, and put it back.

**Say:** "I run lint, and all seven files are clean. ||| Lint looked in the ruin's
file. || It found a barrier called slab, | so it knows the game sends slab opened. |||
Watch what happens if I get the word wrong. || There's one warning, on the step that
waits, | and it says nothing sends that word. || So I fix it, and it's clean again. ||"

### 7. Play it

**Screen:** Run the game. The ten rows of Step 6: the lead, the arrival, the approach,
SUIT UP, the suit's Nav and Fire apps, the cut, the niche, COME ABOARD.

**Say:** "Let's go in, then. || There's a fourth lead in the quest log, | and I engage it.
|| The Hollow is charted, | and the next step appears. ||| I bring the ship up to the
way in. || And now a handheld has something new on it. | It says suit up. || So out I go. || The
suit knows two places, | the gallery door and the niche. ||| At the door, the slab is a
target. || I cut it, and that takes twelve seconds. || The step is done, and paid. ||
Then on to the niche. || The bowl comes with me, | and that's the last step. ||"

### 8. An honest word

**Screen:** The note on the suit under Step 6.

**Say:** "I have to be honest about what you just saw. || When I checked this page, a
script flew all of it, | and nobody was watching a screen. ||| And the exosuit has one
known fault. || A console can close the first time it meets one mid-game. || It's
reported, and it isn't your file. | The way round it is on the page. ||"

### 9. The ruin remembers

**Screen:** Engage Kestrel Relay, then The Hollow again: the open slab. Close the game.
Run it again. The save file, the `relics` lines.

**Say:** "Now the part that makes a ruin fit a campaign. ||| I go home, and I come
back. || The game rebuilt the whole place. | And the slab's still cut. || The bowl's
still gone, | and nobody paid me twice. ||| Now I close the game, and continue, | and it's the
same again. ||| And here it is in the save. | The ruin, what was opened, and what was
taken. ||"

### 10. Your turn

**Screen:** The table "What changes in later lectures". Then the exercise.

**Say:** "One note before you go on. || The battle lectures were written for a universe
with no ruin. || So three small things read differently there, | and they're listed on
the page. ||| Now it's your turn. || Give The Hollow your own name and your own words.
|| Play it to the bowl. | Go home, come back, and look at that slab. ||"
