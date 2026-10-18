"""Class 4's page stills: one picture per lesson, from the game stills, put where the page
says `*[Screenshot to add: ...]*`.

    python _tools/page_stills_c4.py

Writes <lesson>/images/<name>.jpg and replaces the placeholder in that lesson.md with the
picture and its caption. A lesson whose placeholder is already gone is left alone.
"""
import os
import re
from PIL import Image

SRC = "R:/cosmos/courses"
DST = "E:/a/author_courses"
GAP = 16
GAP_COLOR = (16, 16, 24)
PLACEHOLDER = re.compile(r"\*\[Screenshot to add:.*?\]\*\n", re.S)

# (lesson folder, output name, [source stills], crop box or None, alt text, caption)
JOBS = [
    ("c4-01-what-a-ruin-is", "the-sink",
     ["c4_01/stills/game_c1_map.png", "c4_01/stills/game_c1_haze.png"], None,
     "Helm's map with The Sink past the hulk, and the purple haze inside its way in",
     "Helm's map with The Sink on it, and the main screen just inside the inlet: purple haze and rock."),
    ("c4-02-a-ruin-is-a-place", "the-mouth",
     ["c4_02/stills/game_c2_mouth.png"], None,
     "The ship in the middle of The Mouth, rock all round",
     "The Mouth from inside: three rooms and two passages are all it takes to make a place to fly."),
    ("c4-03-dressing-a-ruin", "the-ring",
     ["c4_03/stills/game_c3_ring.png"], None,
     "The Ring set across the first passage, with rock around it",
     "The Ring across the first passage: one Prop line and one Dress line."),
    ("c4-04-places-that-speak", "rook-at-the-altar",
     ["c4_04/stills/game_c4_call.png"], None,
     "The Comms console with Surveyor Rook's recording at the altar open",
     "Comms with \"Surveyor Rook - A recording at the altar\" open: the take, Back, and the two answers."),
    ("c4-05-what-is-inside", "the-cache",
     ["c4_05/stills/game_c5_cache.png", "c4_05/stills/game_c5_quests.png"], None,
     "The canisters of The Cache, and the quest list with What the Survey Left and The Bowl",
     "The Cache's canisters from the ship, and the quest list: What the Survey Left and The Bowl."),
    ("c4-06-clues-side-stories-cutscenes", "the-cairn-cutscene",
     ["c4_06/stills/game_c6_shot2.png"], None,
     "The main screen during the cutscene, The Cairn, Forty-one stones. One for each day.",
     "The main screen during the cutscene: \"The Cairn - Forty-one stones. One for each day.\""),
    ("c4-07-quests-through-a-ruin", "the-hollow-survey",
     ["c4_07/stills/game_c7_list3.png", "c4_07/stills/game_c7_vault.png"], None,
     "The quest list with The Hollow Survey's steps, and Helm in The Vault",
     "The Hollow Survey with its steps under it, and Helm in The Vault, at The Altar."),
    ("c4-08-eva", "a-suit-in-the-ruin",
     ["c4_08/stills/game_c8_nav_niche.png"], None,
     "A crew member's console in a suit inside the ruin, with Nav's list of places",
     "A crew member out in a suit, in The Vault: the view on the left, Nav's list of places on the right."),
    ("c4-09-station-repair", "repair-survey-mast",
     ["c4_09/stills/game_c9_fire.png"], None,
     "A suit beside DS 1, with the Fire app showing Repair: Survey Mast",
     "A suit beside DS 1, its Fire app offering \"Repair: Survey Mast\"."),
    ("c4-10-a-ruin-episode", "the-end-screen",
     ["c4_10/stills/game_c10_win.png"], None,
     "The end screen: The Hollow is surveyed, and what Rook put back is aboard.",
     "The end of the episode: \"The Hollow is surveyed, and what Rook put back is aboard.\""),
]

for folder, name, srcs, crop, alt, caption in JOBS:
    ims = [Image.open(os.path.join(SRC, s)).convert("RGB") for s in srcs]
    if crop:
        ims = [im.crop(crop) for im in ims]
    if len(ims) == 1:
        out = ims[0]
    else:
        h = min(im.height for im in ims)
        ims = [im.resize((round(im.width * h / im.height), h), Image.LANCZOS) for im in ims]
        w = sum(im.width for im in ims) + GAP * (len(ims) - 1)
        out = Image.new("RGB", (w, h), GAP_COLOR)
        x = 0
        for im in ims:
            out.paste(im, (x, 0))
            x += im.width + GAP
    if out.width > 1600:
        out = out.resize((1600, round(out.height * 1600 / out.width)), Image.LANCZOS)
    d = os.path.join(DST, folder, "images")
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, name + ".jpg")
    out.save(p, "JPEG", quality=85)
    lesson = os.path.join(DST, folder, "lesson.md")
    text = open(lesson, encoding="utf-8").read()
    new, n = PLACEHOLDER.subn(lambda _m: f"![{alt}](images/{name}.jpg)\n*{caption}*\n", text, count=1)
    if n:
        with open(lesson, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(new)
    print(p, out.size, "placeholder replaced" if n else "no placeholder")
