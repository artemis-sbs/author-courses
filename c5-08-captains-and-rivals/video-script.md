# C5-8 video script - Captains and rivals

> **STATE ON 2026-10-09.** Written and measured against the released tools: `sbs` 0.13,
> the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions `b20726f`, the
> Open Universe engine library rebuilt 2026-10-08 from `421ff4a`). Everything was run by
> script in the game's stand-in (the mock), from a copy of the mission placed where its
> save cannot reach a player's own. **Nothing in this lecture has been run in the real
> game, and nobody has seen any of its screens.** A captain's card, face and color are
> exactly what the stand-in cannot show: what was measured is what the game was asked
> to send.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 7 leaves it: `kestrel_verge.amd` matches `c5-07-narrative-and-goals\example\` |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | `MyUniverse` open, `kestrel_verge.amd` in a tab, font size raised |
| Game | Closed. Started on camera in scene 8 with `sbs run server,helm,comms -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, with the page's own file:**

1. The finished file lints `clean` and plays with no errors (150 labels run) and an empty
   `mast.runtime.log`. `story.mast` is unchanged from Lecture 2.
2. The game reads two captains: Edda Brake of `hollin`, at 0, 0, and Sable Orrin of
   `gleaners`, at -3, -2. Each speaks under name and title, in her side's color.
3. At home, both Hollin Compact and Kestrel Relay are sent the button `Hail Edda Brake,
   the Relay Warden`. At standing 0 she says the short line and has two answers.
4. After the news: standing with Edda 20, with Hollin 0. She says the kettle line, and
   the third answer is there.
5. At -3, -2 the Gleaners' station is sent `Hail Sable Orrin, the Tallyman`. The plain
   greeting, three answers. After the toll: credits 400, standing with Sable 20, with
   the Gleaners 0, and the answer about the Tern is there.
6. After the other answer twice: standing with Sable -30. She says the cold line, and
   the answer about the Tern is gone. Relations with the Gleaners, their ships and their
   station's other buttons are as they were.
7. The save holds `edda` and `sable` under the ship's reputation.
8. With `Rival when: standing < 50` on Sable, true from the first minute, every line the
   probe prints is the same as without it.
9. Every row of the two tables in Step 5: 40 variants linted, 26 of them played.

**Read in the code, not run:** that a captain with no side, or a misspelled one, loses
the side's color on her card; that an answer's guard can read `credits` and a trait (the
trait was played once, with `honest`).

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. A captain's card: the face on it, the color, the name and title.
2. Where the captain's button sits among a station's buttons.
3. The answers as buttons, and the game's own Leave beside them.
4. A friend hearing two greetings at random when three are written.
5. Anything at all happening when `Rival when:` comes true.

## Scenes

### 1. Cold open

**Screen:** Comms on the Gleaners' station: the button Hail Sable Orrin, the Tallyman.
Then her card.

**Say:** "Your sides are institutions. || They have stations, and fleets, and work. |||
Today you write people. || A captain is somebody with a name, | who belongs to one of
your sides, | and has an opinion of the crew that's all their own. ||| The crew can be
at war with the Gleaners, | and on good terms with their bookkeeper. || Or the other
way round. ||"

### 2. What a captain is, and isn't

**Screen:** The three numbered points in Step 1 of the page. Then the paragraph under
them.

**Say:** "A captain is three things. || A name on a button, at a station. | A voice, in
your Dialogue chapter, and a memory. ||| That's all, and I want to be plain about it.
|| A captain is not a ship. || The game doesn't put one in space for them, | and nobody
can shoot at them. ||| So everything a captain is, | you write in what they say, and what
they refuse to say. ||"

### 3. The Captains chapter

**Screen:** `kestrel_verge.amd`. Add the Captains chapter above the Jobs chapter. Type
Edda Brake, then Sable Orrin. Highlight `Side`, `Title`, `Values`, `Roams`.

**Say:** "A new chapter, and its key is captains. ||| Each captain has four lines. ||
Side is the side they belong to. || Title follows their name on the button. || Values
are what this person cares about, | the same traits as a side has. || And Roams is the
system where they're found. ||| Look at Sable's values. || The Gleaners value fear. | She
values honesty, and doing things by the book. || She's a bookkeeper among wreckers. |
That gap is the character. ||"

### 4. Roams needs a station

**Screen:** Highlight `Roams: -3, -2`. Then the map grid from Lecture 5 with the
Gleaners' home marked, and the Bone Pile beside it.

**Say:** "One rule about Roams. || The button to hail a captain is on a station. ||| Any
station in that system will do, whoever owns it. || But if the system has no station, |
there's nothing to carry the button, | and the captain can't be reached. ||| So Sable
roams the Gleaners' home, which has one. || She does not roam the Bone Pile, which
doesn't. || And lint won't warn you about that. ||"

### 5. A captain's voice

**Screen:** The Dialogue chapter. Type Edda's hail. Highlight `Speaker: edda`, then
`%{standing >= 20}`, then `earns edda`, then `if standing >= 20`.

**Say:** "A captain talks the way a side talks, with one difference. || After Speaker,
it's the captain's key. ||| And that changes what one word means. || In this record,
standing is the crew's standing with her, | not with her side. || And a deed names her:
earns, edda. ||| Now here's something new. || After this answer, the word if, and a
comparison. || That's a guard on an answer. || The crew is only offered it when it's
true. ||| So Edda won't gossip with strangers. || Tell her the news once, and she will.
||"

### 6. A captain who can be crossed

**Screen:** Type Sable's hail. Highlight the two guarded lines, then the two answers
with deeds, then the guarded answer.

**Say:** "Now for Sable, who has two greetings, and the line between them is minus
twenty. ||| One answer pays her toll, | and earns both of the things she values. || The
other insults her, | and it names the far end of each of those traits. || Once is
enough to cross the line. ||| And the answer that matters, the one about the Tern, | is
only for a crew she trusts. ||| That's a rival, and that's all a rival is. || A line
you chose, | and what you wrote on each side of it. ||"

### 7. The line that does nothing

**Screen:** The note about `Rival when:` on the page. Then save, and `sbs lint
MyUniverse`: clean.

**Say:** "If you read the Open Universe's own files, | you'll see a line called Rival
when. ||| It looks like exactly what we want. || Lint accepts it, and today, the game
doesn't read it. || I tried it, and nothing changed. ||| So don't rely on it. || Make
your rival out of guards, the way we just did. ||| I save, and lint says clean. || And
as usual, the list on the page is the rest of the check. ||"

### 8. Make a friend

**Screen:** `sbs run server,helm,comms -m MyUniverse map=0`. Comms: Hollin Compact, the
Edda button. Hail her, give the news, hail again, ask about the bookkeeper.

**Say:** "At home, the station has a new button, | with Edda's name and title on it. |||
She's short with me, and I've got two answers. || I tell her the news. ||| I hail her
again, and it's a different greeting, | and there's a third answer. || She tells me
where to find Sable, | and to settle up first. ||"

### 9. Make a rival

**Screen:** Helm: Engage The Breaking Yard. Comms: the Gleaners' station, Hail Sable.
Pay the toll. Hail: the Tern answer. Then the insult, twice. Hail: the cold greeting.

**Say:** "This is Gleaner space, and we're at war with them. || And here's Sable,
anyway. ||| I pay her toll. || Now she'll answer the question about the Tern. ||| So
let's throw that away. || I tell her to bill the Compact, twice. ||| And listen to her
now. || The question's gone, too. ||| Nothing else has changed. | Nobody is out hunting me.
|| A rival greets you differently, | and keeps back what a friend would hear. || Write
that well, and it's plenty. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Write one captain for each side, | and give each a
value their side doesn't have. || Two greetings, three answers. | One earns, one costs,
and one is only for a friend. ||| Then decide whether the crew can win a rival back.
||| Next time, we tidy up. | Your file gets split into chapters, and you print the
world. ||"
