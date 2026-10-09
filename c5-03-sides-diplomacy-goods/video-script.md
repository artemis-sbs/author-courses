# C5-3 video script - Sides, diplomacy and goods

> **STATE ON 2026-10-08.** Written and measured today against the released tools: `sbs`
> 0.13, the published v1.4.0 libraries (sbs_utils `ae2bbf4a`, LegendaryMissions
> `b20726f`, the Open Universe engine library built 2026-10-05). Everything was run by
> script in the game's stand-in (the mock), from a copy of the mission placed where its
> save cannot reach a player's own. **Nothing in this lecture has been run in the real
> game, and nobody has seen any of its screens.**
>
> **2026-10-08, later:** the page first carried a card for `story.mast`, a bridge
> over two faults in Open Universe. Those are mended and released, so the card, its
> step and its scene are gone. Lecture 5's files were then run without the card in
> the stand-in and in the real game's server (no console): no error either way.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyUniverse` as Lecture 2 leaves it: its two files match `c5-02-your-universe-file\example\` |
| Saves | No `universe_save_the_kestrel_verge_1.yaml` in `data\missions\common_data\saves` |
| Tool and libraries | Current: `sbs update`, then `sbs fetch "MyUniverse" --update-libs` |
| VS Code | `MyUniverse` open, `kestrel_verge.amd` open, font size raised |
| Game | Closed. Started on camera in scene 8 with `sbs run server,helm,comms -m MyUniverse map=0` |

## Confirm on camera

**In the mock, by script, on 2026-10-08, with the page's own files:**

1. The finished files lint `clean` and play with no errors (139 labels run) and an empty
   `mast.runtime.log`.
2. The three sides are read as written. The crew's side is hostile to the Gleaners from
   the start and has no set relation with Hollin or Deepwell. Hollin and the Gleaners
   have no set relation with each other.
3. Home holds three stations: Hollin Compact and Hollin Compact Outpost on Hollin's side,
   and Kestrel Relay on the crew's. There is no Starbase.
4. Comms is sent these buttons for Hollin Compact: Accept Cargo Run, Transport a
   passenger, Accept Patrol Mission, Patrol (200 cr), Escort (250 cr). For Kestrel Relay:
   Market, Hail, Build Weapons, Request Priority Docking, Accept Cargo Run, Transport a
   passenger, Accept Patrol Mission.
5. The Quest Log is handed both leads as Active. The Quest Log's own gate offers Helm
   **Engage** on a lead. Engaging The Second Colony puts the ship at 3, 1 with a station
   named Deepwell Assembly, whose buttons include Escort (250 cr) and no Patrol. The lead
   is Done.
6. Engaging The Breaking Yard puts the ship at -3, -2: a station named The Gleaners, an
   outpost, two Torgoth ships and four fighters, all on the Gleaners' side.
7. With 500 credits the Gleaners' station is sent no **Negotiate Ceasefire** button. With
   900 it is. The button was pressed the way the game reports a press: credits fell by
   600, and the relation went from hostile to neutral. The save file then held that
   relation, and a second start read it back.
8. The nearest system the game rolled as an enemy system held five Torgoth ships on the
   Gleaners' side. With no foe side in the file, the same system held six raiders of
   mixed kinds.
9. Loot: 2000 draws with the page's four weights gave 964 ore, 690 provisions, 222 tech,
   124 contraband, and no gas.
10. Every row of the two tables in Step 6: 41 variants, one change each, each linted and
    played.

**Read in the code, not run:** the greeting lines in the Character table; that a greeting
is sent on arrival in a side's system; the words of the ceasefire reply.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. Comms: a station's buttons as a list; **Patrol (200 cr)** on Hollin Compact; the
   market on Kestrel Relay.
2. Whether the crew can select and talk to a station of a side they are at war with, from
   where the jump leaves them. The mock answers a selection from any distance.
3. The Gleaners' fleet attacking on arrival, and stopping after the ceasefire.
4. The side's greeting on arrival: where it is drawn and for how long.
5. A side's `Color:` anywhere on a screen.
6. Loot crates in a system, and their names.
7. Whether the crew can dock at Hollin Compact.

## Scenes

### 1. Cold open

**Screen:** Comms with Hollin Compact selected. Then the Gleaners' station, a fleet beside
it.

**Say:** "Last time, you made a universe with one named place in it, | and nobody living
there but the crew. || Today it gets people. || There are three factions: | one runs the
port you start in, | one lives three jumps away, | and one shoots first. ||| You'll write
all three in one chapter, | and then you'll go and meet them. ||"

### 2. Out with the old

**Screen:** `kestrel_verge.amd`, the Sides chapter. Highlight `Disposition: hostile` on
Ashfall Run. Then delete both template sides.

**Say:** "The template gave me two sides, and I'm deleting both. || But before they go,
look at this line: Disposition, hostile. || You'd think that side was an enemy, | and it
never was. || The game knows two words on that line, | and hostile isn't one of them. |||
Lint said clean the whole time. || So keep that in mind today: | clean means the record is
well made. | It doesn't mean the words inside it are words the game knows. ||"

### 3. The first side

**Screen:** Type the Hollin Compact record. Highlight each line as it is named.

**Say:** "A side is a record with three hashes, | a name, and a key. || The key matters,
because everything else names this side by it. ||| Then come its facts, starting with a color. || There's a
character, in one word, which decides how they greet the crew. || A disposition, which
I'll come back to. || A home, which is a system, written as two numbers. || The jobs they
offer, | and the ships they fly. ||| Now look at the home: zero, zero. | That's where the
crew starts. || So the station the game put there last time | now belongs to these
people, and carries their name. ||"

### 4. Two more, and who shoots first

**Screen:** Type Deepwell Assembly and The Gleaners. Highlight `Disposition: foe`.

**Say:** "Here are the other two. || The second colony is neutral, like the first, | and
its home is three systems over and one up. ||| The third one says foe, in small letters.
|| That's the only other word there is. || Neutral means they talk, and their station
offers work. || Foe means they're at war with the crew from the first minute. ||| And a
foe gets things from the game for free. || There's a fleet guarding its home. || And every
system the game fills with enemies, | anywhere in the universe, | is filled with their
ships. || So one word gives your villains a navy. ||"

### 5. Two leads

**Screen:** End of the `.amd`. Type the Narrative chapter with the two leads. Highlight
`Done when: reach 3, 1`.

**Say:** "My sides live in three systems, | and the crew can only jump where a job sends
them. || So I give them two jobs whose whole point is the trip. ||| These are quests, like
the ones you wrote in Class 1, | and they live in a chapter called Narrative. || The new
part is this: Done when, reach, and two numbers. || That means, arrive in that system. ||
And because the quest has somewhere to go, | Helm gets an Engage button on it. ||"

### 6. Goods

**Screen:** Type the Goods chapter between Landmarks and Narrative. Highlight a `Weight:`
line.

**Say:** "Last comes the economy, and it's a small one. || Crates drift in most systems, |
and the game knows five kinds of cargo. || This chapter says which of the five my world
has, | and how common each one is. ||| The weights are just compared with each other. ||
So with these numbers, about half the crates are ore, | a third are food, | and
contraband is rare. || I left gas out altogether, | so there isn't any, anywhere. |||
That's the whole of what a writer decides here. || The prices in a market belong to the
game. ||"

### 7. Check it

**Screen:** Save both files. `sbs lint MyUniverse`: clean. Then the page's list of six
things to check by eye.

**Say:** "Lint says clean, and today that's only half the check. || So I read down this
list by eye. ||| Disposition is neutral or foe. || Every home is two numbers, and no two
sides share one. || Every job after Offers is a key in the Jobs chapter. || Every ship
after Flies is one of the six. || Every good is one of the five. || And the numbers after
reach are that side's home. ||"

### 8. Meet the neighbors

**Screen:** `sbs run server,helm,comms -m MyUniverse map=0`. Comms: Hollin Compact, its
buttons. Then Kestrel Relay. Take the cargo run. Helm: Quest Log, Engage the cargo run,
then The Second Colony.

**Say:** "On Comms, I select Hollin Compact. || There's the work I gave them: | a patrol,
and an escort. || Kestrel Relay doesn't have those, | because it's the crew's own. ||| I
take a cargo run, because I'm going to need the money. || On Helm, there are my two leads
in the Quest Log. || I fly the cargo run first, | and then I engage The Second Colony. ||
And here's the Deepwell's own station, | offering an escort and nothing else, | just as I
wrote it. ||"

### 9. The ones who shoot first

**Screen:** Helm: Engage The Breaking Yard. The arrival. Comms: select the Gleaners'
station; Negotiate Ceasefire.

**Say:** "Now the other lead. || This is the Gleaners' home, | and that's their fleet. |||
On Comms, I select their station, | and there's a button: Negotiate Ceasefire. || It costs
six hundred credits. || A new crew starts with five hundred, | which is why I flew that
cargo run first. || I press it, and the war is off. ||| It's the whole side, everywhere, |
and it's written into the save. || But it's a ceasefire, and not a friendship. | They still
won't give me work. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now make the three of them yours: | new names, new keys, new homes. || Choose
each one's character, | and read its greeting out loud. || Then decide what's common in
your world, and what's rare. ||| Next time, each side gets something it values, | and
what the crew does starts to change what people think of them. ||"
