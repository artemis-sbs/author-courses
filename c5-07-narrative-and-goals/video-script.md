# C5-7 video script - Narrative and goals

> **STATE ON 2026-10-09.** Written and measured against the released tools: `sbs` 0.13,
> the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions `b20726f`, the
> Open Universe engine library rebuilt 2026-10-08 from `421ff4a`). Everything was run by
> script in the game's stand-in (the mock), from a copy of the mission placed where its
> save cannot reach a player's own. **Nothing in this lecture has been run in the real
> game, and nobody has seen any of its screens.** In the stand-in a script pressed the
> Comms buttons and told the game "the ship destroyed this". No ship fired.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 6 leaves it: `kestrel_verge.amd` matches `c5-06-jobs\example\` |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | `MyUniverse` open, `kestrel_verge.amd` in a tab, font size raised |
| Paper | The story in three lines, for scene 2 |
| Game | Closed. Started on camera in scene 8 with `sbs run server,helm,comms -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, with the page's own file:**

1. The finished file lints `clean` and plays with no errors and an empty
   `mast.runtime.log`. `story.mast` is unchanged from Lecture 2.
2. At the start the Quest Log holds The Second Colony, The Breaking Yard and The Third
   Colony. The Assay Ledger, What the Gleaners Keep and Break the Bone Pile are hidden.
3. On arrival at 1, -2 The Third Colony is done and The Assay Ledger is Active. Engage on
   it leaves the ship where it is.
4. The Assay Office is sent `Hail Deepwell Assembly`; the hail gives three answers. The
   fee answer: credits 500 to 350, then 550 with the beat's 200; standing with the
   Deepwell 20; The Assay Ledger done; What the Gleaners Keep Active.
5. The demand answer, in another run: no credits taken, the beat done, standing with the
   Deepwell down by 20.
6. Asking before the Tern is found: the fee is taken, standing is 20, the beat stays
   hidden, and it still needs the answer afterward.
7. On arrival at -4, -3: credits 950, Break the Bone Pile Active, seven hostile ships
   (five of the Gleaners, two raiders).
8. With four kills reported the goal is done. The game is sent a card titled VICTORY
   carrying the `Citation:`, and is told the game is over, won, with the `Win:` sentence.
9. Every row of the two tables in Step 5: 40 variants, one change each, each linted and
   played. Re-measured 2026-10-10 on the released libraries, with two ships:
   `Standing: gleaners fearsome 70` on a beat left both at 40 with the Gleaners, and
   `Reward: 200 credits, earns deepwell by-the-book 30` left both at 20 with the
   Deepwell; the fee answer then took the ship that gave it to 40 and left the other at
   20. When this page was first written a beat's deed reached no ship.
10. A goal given `Fails when: 5 seconds` and a `Lose:` sentence ends the game, lost, with
    that sentence.

**By lint's word and by the code, not seen to happen:** that a misspelled signal in one
answer stops that answer closing the chapter (the run used the other answer); that with
no comma between `costs` and `signal` the signal is not sent; that a signal written
before an unaffordable `costs` is sent anyway; that a shared reward pays each side once.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. A chapter appearing in the Quest Log while the crew watches, and its briefing there.
2. The VICTORY card on a console, and how long it stays.
3. The end-of-game screen in an Open Universe mission, with the `Win:` sentence on it.
4. What the crew can do after the game is won, and what Continue offers next time.
5. Real kills counting toward the goal.

## Scenes

### 1. Cold open

**Screen:** Helm's Quest Log with three entries. Then the same log with The Assay Ledger
newly in it.

**Say:** "Your universe has places, sides, and work. || What it doesn't have yet is a
story. ||| Right now the crew can see every lead you wrote, | from the first minute, in
any order. || That's a list of places. ||| Today you turn it into chapters, | where each
one opens the next. || And then you write the last page. ||"

### 2. Three lines on paper

**Screen:** A sheet of paper with the three chapters written as one line each.

**Say:** "Before I open the file, I write the story as three lines. ||| One. The crew
finds the third colony's ship, and she's been stripped. || Two. The miners' ledger says
who sold her cargo. || Three. That leads to a place the Gleaners won't talk about. |||
Each line ends with something the crew has just learned. || That's what makes it a
chapter, and not an errand. ||"

### 3. The chain

**Screen:** The Narrative chapter. Add `Then: reveal tern_ledger` to The Third Colony.
Type The Assay Ledger. Change What the Gleaners Keep to `revealed`.

**Say:** "You know these lines from Class One. || Starts when, revealed, means the
chapter is hidden. || And Then, reveal, wakes the one with that key. ||| So the first
chapter keeps, at once, | and gets one new line that points at the second. || The second
is new. It's hidden, | and it points at the third. ||| And the third was already here as
a lead. || I change at once to revealed, and give it a reward. ||| Now read down the
Then lines. || That's your table of contents. ||"

### 4. The briefing

**Screen:** Highlight the text under The Assay Ledger. Then the words "at (3, 1)".

**Say:** "The words under a beat are the briefing. || They're what the crew reads when
the chapter appears. ||| A good one says what was just learned, | and where to go next.
|| And I mean where. I've written the place into the sentence. ||| That matters for
this chapter, | because it doesn't end at a place. || It ends on a signal. || So Helm
has nothing to engage, | and the crew gets there by reading. ||"

### 5. A chapter that ends in a call

**Screen:** The Dialogue chapter. Type Deepwell Hail. Highlight `signal ledger_read` in
both answers, then the two sets of deeds.

**Say:** "Done when, signal, ledger read. || Nothing sends that signal yet, so I write
the thing that does. ||| It's a call to the miners, like the two calls from Lecture
Four. || And there's one new item among an answer's outcomes: | signal, and the same
word. ||| Now look at both answers. || They both send it, so either one closes the
chapter. || But one pays the fee, politely, | and the miners think better of the crew.
|| The other demands the page, | and they think worse. ||| That's how a beat shifts
standing. || The deed goes in the answer, beside the signal. ||"

### 6. On the beat, or in the answer

**Screen:** The note under Step 3 on the page.

**Say:** "You could write the deed on the beat itself. || There's a line for it, called
standing, | and a beat's reward can hold one too. ||| A deed on the beat goes to every
ship in the game, | whoever finished it, and whichever way. || A deed in an answer goes
to the ship that gave the answer, | and to nobody else. ||| So ask yourself what you
want. || If it's the story's verdict, put it on the beat. || If it's a choice, put it in
the answer. || Here it's a choice. ||"

### 7. The last page

**Screen:** Add the Goals chapter. Highlight `Win:` and `Citation:`. Save. `sbs lint
MyUniverse`: clean.

**Say:** "A goal is a beat with one more line. || Win, and then a sentence. ||| When
this quest is done, the game ends, | and that sentence is on the last screen. ||
Citation is the line on the card the crew gets at that moment. ||| My goal is hidden
too, | and the third chapter reveals it. || So the ending arrives when the story has
earned it. ||| I save, and lint says clean. || Lint is good at chains. | It'll tell you
when a chapter can never appear. ||"

### 8. Play the story

**Screen:** `sbs run server,helm,comms -m MyUniverse map=0`. Helm: Quest Log, three
entries. Engage The Third Colony: The Assay Ledger appears. Engage The Second Colony.
Comms: Assay Office, Hail, pay the fee. Quest Log: What the Gleaners Keep.

**Say:** "Three entries at the start, and no sign of the rest. ||| I go and find the
Tern. || And there's chapter two, with its briefing. ||| It says to ask at the Assay
Office, so that's where I go. || I hail them, and I pay the fee. ||| The chapter's done,
it paid me, | and the miners like me a little more. || And here's chapter three. ||"

### 9. The end

**Screen:** Engage What the Gleaners Keep. Break the Bone Pile appears. The fight. The
VICTORY card. The end-of-game screen.

**Say:** "This is the place the Gleaners won't talk about. || And as I arrive, the goal
appears. ||| Four of them, and it's over. ||| There's my citation, on the card. || And
there's my sentence, on the last screen. ||| One thing before you go. || A universe
doesn't have to end. || Leave the goals out, and it's a sandbox for as long as the crew
likes. || Write a goal when your story has a last page. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Write your story as three lines on paper first. || Chain
them, with the first one open and the rest hidden. ||| End one chapter with a
conversation, | and give the crew two ways to get what they came for. || Then decide
whether your universe ends. ||| Next time, we put people in it. ||"
