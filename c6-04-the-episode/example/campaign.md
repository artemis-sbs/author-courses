# The Long Count

A campaign for The Kestrel Verge. This file is for the writer and for whoever runs the
table. It is not for the crew. The game never reads it.

## Premise

The Tern carried forty-one people and five boats. When she was found, the boats were
gone. The campaign is the count: find the five boats, then find the people.

## The pressure

The Gleaners strip every dead hull in the Verge. A boat the crew does not reach first is
a boat they find in pieces.

## The loop

Every evening goes round the same way.

1. At Kestrel Relay the crew has one lead.
2. They jump to it.
3. They find out one thing.
4. Something gets in the way.
5. They carry what they found home, and the next lead is waiting.

## Three evenings written by hand

| Where | Evening | What happens |
|---|---|---|
| Opening | 1 | The Wren. The boats were launched, so somebody lived |
| Midpoint | 10 | The crew learns who bought the people, and that it was not the Gleaners |
| Finale | 20 | The fourth colony. The count is closed, one way or the other |

## What came back (measured on evening 1)

| What I checked | Before I stopped | After Continue |
|---|---|---|
| Where the ship is | Kestrel Relay, (0, 0) | The same |
| Credits | 400 | 400 |
| Standing with Hollin | 20 | 20 |
| The lead, One of Five | Done | Done |
| The job in hand | Hollin Compact: Escort, Active | The same |
| Charted Locations | Kestrel Relay, The Wren | The same |

## Evening 1 - One of Five

| Part | What happens | The record | Minutes |
|---|---|---|---|
| Open | The Compact has a fix on a boat at (2, 2). The crew jumps | `s01_go` | 5 |
| Objective | Read the Wren's log. Science scans her | `s01_scan` | 15 |
| Climax | Three ships are already cutting her up. Fight them, or scan and run | `Guards:` on `the_wren` | 10 |
| Hook | Home to Kestrel Relay. The log names a second boat, the Dunlin | `s01_home`, then `s02_go` | 5 |

- **The crew learns:** the boats were launched. Nine people were in this one.
- **It pays:** 300 credits, at home.
- **Who is busy:** Helm for two jumps, Science for the scan, Weapons if they stay to fight.
- **It ends when:** the ship is home and Two of Five is in the Quest Log. Close the game there.
- **Played in:** ___ minutes. (Fill this in after the first table plays it.)

## The pattern

One evening, with the words that change in capital letters. Copy it into
`kestrel_verge.amd`: the landmark into the Landmarks chapter, the three steps into the
Narrative chapter. Then fill it in.

```
### [PLACE NAME](PLACE_KEY)
---
At: X, Y
Kind: derelict
Terrain: COVER
Guards: SHIPS
---
ONE LINE THE CREW IS TOLD ON ARRIVAL.

### [The Long Count: OPEN TITLE](sNN_go)
---
Scope: shared
Starts when: revealed
Done when: reach X, Y
Then: reveal sNN_DEED
---
WHAT WAS FOUND LAST WEEK. WHERE TO GO. WHAT IS STRANGE ABOUT IT.

### [The Long Count: OBJECTIVE TITLE](sNN_DEED)
---
Scope: shared
Starts when: revealed
Done when: ENDING
Then: reveal sNN_home
---
WHAT IS HERE. WHAT TO DO ABOUT IT.

### [The Long Count: HOME TITLE](sNN_home)
---
Scope: shared
Starts when: revealed
Done when: reach 0, 0
Then: reveal sMM_go
Reward: PAY credits
---
WHAT THE CREW NOW KNOWS. TAKE IT HOME.
```

## The sheet, blank

| Part | What happens | The record | Minutes |
|---|---|---|---|
| Open | | `sNN_go` | |
| Objective | | `sNN_DEED` | |
| Climax | | | |
| Hook | | `sNN_home`, then `sMM_go` | |

- **The crew learns:**
- **It pays:**
- **Who is busy:**
- **It ends when:**
- **Played in:** ___ minutes.

## Evening 2 - Two of Five

| Part | What happens | The record | Minutes |
|---|---|---|---|
| Open | The Wren's log points past the Fields, to (-2, 3). A voice answers on the Dunlin's channel | `s02_go` | 5 |
| Objective | The voice is a recording. Two ships are waiting in the cloud. Destroy them | `s02_clear` | 20 |
| Climax | The same thing. Tonight the fight is the point | `Guards:` on `the_dunlin` | - |
| Hook | Home. The Dunlin was empty and stocked. The Deepwell sold a third boat | `s02_home`, then `s03_go` | 5 |

- **The crew learns:** nobody starved in the boats. They were taken off.
- **It pays:** 350 credits, at home.
- **Who is busy:** Weapons and Engineering. Science finds them in the cloud.
- **It ends when:** the ship is home and Three of Five is in the Quest Log.
- **Played in:** ___ minutes.
