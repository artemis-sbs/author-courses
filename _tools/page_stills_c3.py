import os
from PIL import Image

SRC = "R:/cosmos/courses"
DST = "E:/a/author_courses"
GAP = 16
GAP_COLOR = (16, 16, 24)

# (lesson folder, output name, [source stills], crop box or None)
JOBS = [
    ("c3-01-what-a-boarding-party-is", "landing-field-handheld",
     ["c3_01/stills/game_l1_field.png"], (0, 0, 1280, 460)),
    ("c3-02-party-and-place", "boarding-party-app",
     ["c3_02/stills/game_l2_app.png"], (0, 0, 1280, 330)),
    ("c3-03-everyone-gets-a-menu", "reactor-room-two-consoles",
     ["c3_03/stills/game_l3_eng_reactor.png", "c3_03/stills/game_l3_sci_reactor.png"], None),
    ("c3-04-crew-and-skills", "reactor-roll",
     ["c3_04/stills/game_roll_eng.png"], None),
    ("c3-05-personal-quests", "tasks-six-names",
     ["c3_05/stills/game_tasks_sci.png"], (0, 0, 1280, 740)),
    ("c3-06-boarding-checkpoint", "captains-cabin-two-handhelds",
     ["c3_06/stills/game_cabin_sci.png", "c3_06/stills/game_cabin_eng.png"], None),
    ("c3-07-anatomy-of-a-long-away-mission", "kesh-relay-on-the-ground",
     ["c3_07/stills/game_l7_walk.png"], None),
    ("c3-08-tile-map-editor-part-1", "gully-in-the-editor",
     ["c3_08/stills/d_art.png"], (0, 0, 1920, 760)),
]

for folder, name, srcs, crop in JOBS:
    ims = [Image.open(os.path.join(SRC, s)).convert("RGB") for s in srcs]
    if crop:
        ims = [im.crop(crop) for im in ims]
    if len(ims) == 1:
        out = ims[0]
    else:
        w = sum(im.width for im in ims) + GAP * (len(ims) - 1)
        h = max(im.height for im in ims)
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
    print(p, out.size)
