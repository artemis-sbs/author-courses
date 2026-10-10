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

## The four acts

| Act | Evenings | The question | It ends when |
|---|---|---|---|
| 1. Five Boats | 1 to 5 | What happened to the Tern's boats? | All five are found. Nobody died in them |
| 2. The Buyers | 6 to 10 | Who took forty-one people off five boats? | The crew learns it was not the Gleaners |
| 3. The Breakers | 11 to 15 | Where were they taken? | The crew has a heading, and has chosen a side to get it |
| 4. The Fourth Colony | 16 to 20 | Are they still there, and do they want to be found? | The count is closed |

## Act One - Five Boats

| Evening | Title | Place | The objective ends with | Written |
|---|---|---|---|---|
| 1 | One of Five | The Wren, (2, 2) | `scan` | In full |
| 2 | Two of Five | The Dunlin, (-2, 3) | `destroy` | In full |
| 3 | The Plover | Assay Office, (3, 1) | `signal`, from a hail | In full |
| 4 | Four of Five | The Petrel, (4, -2) | `scan` | In full |
| 5 | Five of Five | The Gleaners' yard, (-3, -2) | `signal`, from a hail the crew has to earn by asking first | In full |
| End | Five Boats | Kestrel Relay, (0, 0) | `reach` | In full |

## Budget

| Thing | Count |
|---|---|
| Ordinary evenings | 17 |
| Tentpoles | 3 |
| Records to write, about | 93 |
| Records written | 13 |
| One evening takes me | ___ minutes to write |
| Act One will take me | ___ |
| The campaign will take me | ___ |

## Standing ledger - Act One

What I expect, if the crew takes one Hollin job a week and pays the levy when they can.

| End of evening | Hollin | Deepwell | Gleaners | A door I expect to open or close |
|---|---|---|---|---|
| 1 | 5 | 0 | 0 | |
| 2 | 30 | 0 | 0 | Hollin tier 2 jobs |
| 3 | 35 | 20 | 0 | Deepwell tier 2 jobs |
| 4 | 45 | 20 | 0 | The Tern's manifest |
| 5 | 50 | 20 | 0 | Hollin tier 3 jobs. Or, if they sold the Count in the yard: Hollin 27, Gleaners 15, and tier 3 is out of reach again |

Prices I have set: the levy, 100 credits for +20. Wages: 300, 350, then 300 an evening.

## Rotation - Act One

| Evening | Title | Style | Whose evening | On offer beside it |
|---|---|---|---|---|
| 1 | One of Five | Search, with a fight they can refuse | Science | Escort, the levy |
| 2 | Two of Five | Fight | Weapons, Engineering | Patrol, if they are trusted |
| 3 | Three of Five | Talk | Comms | The Deepwell's work |
| 4 | Four of Five | Race | Helm | Lamp Run, from the Compact |
| 5 | Five of Five | Politics | Comms, the captain | A ceasefire with the Gleaners |
| End | Five Boats | - | Everyone | The Tern's manifest, if they have earned it |

Styles I am keeping for later acts, when I have taken the lecture:
boarding (Class 5 Lecture 10), ruin (Lecture 11), battle (Lectures 12, 13), Admiral
(Lectures 14, 15).

## Act One, as played

Three sittings, one save. Walked alone, by the writer, before any crew.

| Sitting | Started with | Evenings | Credits at the end | Standing at the end | The open step when I stopped |
|---|---|---|---|---|---|
| 1 | A new game | 1 and 2 | 1050 | Hollin 20 | Three of Five |
| | *I wrote evenings 4 and 5 here, and retitled evening 3* | | | | |
| 2 | Continue | 3 and 4 | 1800 | Hollin 25, Deepwell 20 | Five of Five |
| 3 | Continue | 5, and the act's end | 2500 | Hollin 25, Deepwell 20 | While They Read, which waits for Act Two |

## Act Two - The Buyers (outline)

The question: who took forty-one people off five boats?

| Evening | Title | Place | Style | The objective ends with | What the crew learns |
|---|---|---|---|---|---|
| 6 | The Seller's Mark | Assay Office, (3, 1) | Talk | `signal`, from a hail | The Plover's seller used a Compact seal |
| 7 | Whose Seal | Kestrel Relay, (0, 0) | Politics | `signal`, behind `if standing >= 40` | The seal was reported lost, eleven years ago |
| 8 | The Hollow | A ruin, to be placed | Ruin (Class 5 Lecture 11) | `signal hollow_taken` | Somebody camped here, and counted days |
| 9 | Eleven Years | The Petrel, (4, -2) | Search | `scan` | The beacon was moved the same month |
| 10 | Not the Gleaners | The Gleaners' yard, (-3, -2) | Talk. **Tentpole** | `signal`, behind `if learned` | The Gleaners were paid to break the boats, not to empty them |

Facts this act teaches, and where: `the seal was compact` (evening 6, an answer),
`the seal was lost` (evening 7, an answer).

## Act Three - The Breakers (outline)

The question: where were they taken?

| Evening | Title | Place | Style | The objective ends with |
|---|---|---|---|---|
| 11 | The Paymaster | To be placed, in the Breakers | Search | `reach`, then `scan` |
| 12 | A Price for a Heading | The Gleaners' yard | Politics | `signal`, with a cost in credits or in standing |
| 13 | The Convoy | To be placed | Fight | `destroy` |
| 14 | What the Compact Knew | Kestrel Relay | Talk | `signal`, behind The Tern's Manifest |
| 15 | A Side | Wherever the crew stands | Politics | Two leads. Finishing one closes the other for the story |

## Act Four - The Fourth Colony (outline)

The question: are they still there, and do they want to be found?

| Evening | Title | Place | Style | The objective ends with |
|---|---|---|---|---|
| 16 | Off the Chart | A new landmark, far out | Search | `reach` |
| 17 | The Picket | The same system | Fight, or talk | `destroy`, or `signal` |
| 18 | Forty-One | The fourth colony | Talk | `signal` |
| 19 | What They Ask | The fourth colony | Politics | `signal` |
| 20 | The Count Is Closed | Kestrel Relay. **Tentpole, and the finale** | Everyone | `reach`, with the campaign's one `Win:` |

## Rules for changes

1. The title never changes.
2. A step the crew is on is never deleted, and a key is never renamed without `Was:`.
3. New steps go after the open step, never behind a finished one.
