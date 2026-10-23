"""Classes 5 and 6 page stills: one picture per lesson, from the game stills, put where the
page says `*[Screenshot to add: ...]*`.

    python _tools/page_stills_c5_6.py

Writes <lesson>/images/<name>.jpg and replaces the placeholder in that lesson.md with the
picture and its caption. A lesson whose placeholder is already gone is left alone.
A caption says what is on screen and never describes a face.
"""
import os
import re
from PIL import Image

SRC = "R:/cosmos/courses"
DST = "E:/a/author_courses"
GAP = 16
GAP_COLOR = (16, 16, 24)
PLACEHOLDER = re.compile(r"\*\[Screenshot to add:.*?\]\*\n", re.S)

# (lesson folder, output name, [source stills], alt text, caption)
JOBS = [
    ("c5-01-what-open-universe-is", "the-quest-log",
     ["c5_01/stills/game_c51_quests.png"],
     "Helm's Quest Log in The Silver Reach, with The Dimming and Break the Veil in it",
     "Helm's Quest Log in The Silver Reach: The Dimming, Break the Veil and the cargo run."),
    ("c5-02-your-universe-file", "the-arrival-card",
     ["c5_02/stills/game_c52_card.png"],
     "The card the crew sees on arrival, reading Kestrel Relay",
     "The card on arrival, reading Kestrel Relay: your file's own words."),
    ("c5-03-sides-diplomacy-goods", "a-station-selected",
     ["c5_03/stills/game_c53_hollin.png"],
     "Comms with the station Hollin Compact selected, Patrol and Escort among its buttons",
     "Comms with Hollin Compact selected: Patrol and Escort among its buttons."),
    ("c5-04-reputation", "before-and-after-the-levy",
     ["c5_04/stills/game_c54_hollin.png", "c5_04/stills/game_c54_hollin_after.png"],
     "Comms on Hollin Compact before and after the levy is paid",
     "Hollin Compact before the levy, and after: Patrol is on offer and Escort pays 300."),
    ("c5-05-the-map", "the-bone-pile",
     ["c5_05/stills/game_c55_bone.png", "c5_05/stills/game_c55_charted.png"],
     "The arrival at The Bone Pile, and Helm's Quest Log with the places under Charted Locations",
     "The Bone Pile on arrival, and the Quest Log's Charted Locations."),
    ("c5-06-jobs", "jobs-on-comms",
     ["c5_06/stills/game_c56_assay.png", "c5_06/stills/game_c56_log3.png"],
     "Comms on the Assay Office with its jobs, and Helm's Quest Log with the jobs under Ship",
     "The Assay Office's jobs on Comms, and the three jobs under Ship in the Quest Log."),
    ("c5-07-narrative-and-goals", "a-story-and-its-end",
     ["c5_07/stills/game_c57_ledger.png", "c5_07/stills/game_c57_end.png"],
     "Helm's Quest Log with The Assay Ledger newly in it, and the end-of-game screen",
     "A chapter newly in the Quest Log, and the end-of-game screen with the goal's own sentence."),
    ("c5-08-captains-and-rivals", "hail-sable-orrin",
     ["c5_08/stills/game_c58_sable_btn.png"],
     "Comms on the Gleaners' station with the button Hail Sable Orrin, the Tallyman",
     "The Gleaners' station on Comms, with the button Hail Sable Orrin, the Tallyman."),
    ("c5-09-organizing-a-big-universe", "the-library",
     ["c5_09/stills/game_c59_library.png"],
     "The in-game Library, open at The Three Colonies",
     "The in-game Library, open at The Three Colonies: prose that lives in lore.amd."),
    ("c5-10-a-boarding-site-on-the-map", "the-counter-and-the-yard",
     ["c5_10/stills/game_c510_ccounter.png", "c5_10/stills/game_c510_ymap.png"],
     "A handheld in the Customs House with three choices, and a handheld showing the yard's map",
     "The Customs House counter with its choices, and the yard's map on a handheld."),
    ("c5-11-a-ruin-on-the-map", "inside-the-hollow",
     ["c5_11/stills/game_c511_inside.png", "c5_11/stills/game_c511_suit.png"],
     "The main screen inside The Hollow, and a handheld with the Boarding Party app showing SUIT UP",
     "Inside The Hollow, and the handheld's Boarding Party app offering SUIT UP."),
    ("c5-12-battles-part-1", "the-tern-is-guarded",
     ["c5_12/stills/game_c12_tern.png"],
     "Comms after arriving at The Tern, with the line titled Threat",
     "On arrival at The Tern: \"The Tern is guarded - hostiles on approach.\""),
    ("c5-13-battles-part-2", "a-battle-forms-up",
     ["c5_13/stills/game_c13_arrive.png"],
     "Comms at The Bone Pile with the two Threat lines, the second a Gleaner battle line forming up",
     "At The Bone Pile: the guards' Threat line, and ours, \"A Gleaner battle line is forming up.\""),
    ("c5-14-admiral-part-1", "build-headquarters",
     ["c5_14/stills/game_c14_hq.png"],
     "The Admiral console looking down on a system, a worldlet selected, with the Build Headquarters button",
     "The Admiral console: Hollin Prime selected, and the button \"Build Headquarters (150 ore, 15 crew)\"."),
    ("c5-15-admiral-part-2", "the-admiral-and-the-bridge",
     ["c5_15/stills/game_c15_home.png", "c5_15/stills/game_c15_helm.png"],
     "The Admiral console with Hollin Prime selected, and Helm's Quest Log with the three leads",
     "The Admiral looking down on the home system, and the bridge crew's Quest Log with the three leads."),
    ("c5-16-a-playable-universe", "the-end-screen",
     ["c5_16/stills/game_c16_win.png"],
     "The end-of-game screen with the goal's Win sentence and its citation",
     "The end of the evening: your goal's own sentence, and its citation under it."),
    ("c6-01-from-one-session-to-twenty", "the-quest-log",
     ["c6_01/stills/game_c61_log4.png"],
     "Helm's Quest Log with the four Class 5 leads and The Long Count: One of Five",
     "Helm's Quest Log: the four Class 5 leads, and The Long Count: One of Five beside them."),
    ("c6-02-what-the-game-remembers", "report-what-the-gleaners-said",
     ["c6_02/stills/game_c62_report.png"],
     "The Hollin hail on Comms with Report what the Gleaners said among the answers",
     "The Hollin hail, with \"Report what the Gleaners said\" among the answers: the game remembered."),
    ("c6-03-designing-a-session", "the-end-of-the-evening",
     ["c6_03/stills/game_c63_end.png"],
     "Helm's Quest Log with Two of Five open and three steps of The Long Count under Done",
     "The end of evening 1: Two of Five open, and three steps of The Long Count under Done."),
    ("c6-04-the-episode", "evening-two",
     ["c6_04/stills/e_sheet2.png"],
     "campaign.md open at Evening 2, with the table of parts and records",
     "campaign.md at Evening 2: each part, and the record that carries it."),
    ("c6-05-campaign-architecture", "the-walk-ends",
     ["c6_05/stills/game_c65_done.png"],
     "Helm's Quest Log at the end of the walk, with every line of The Long Count under Done",
     "The end of the walk: every line of The Long Count under Done."),
    ("c6-06-reputation-arcs", "ask-to-see-the-manifest",
     ["c6_06/stills/game_c66_hail4.png"],
     "Comms in a hail with the Hollin Compact, with the answer Ask to see the Tern's manifest",
     "After two levies the hail has a fourth answer: \"Ask to see the Tern's manifest.\""),
    ("c6-07-mixing-the-play-styles", "two-ways-to-ask",
     ["c6_07/stills/game_c67_ask.png"],
     "Comms in the Deepwell hail with the two ways to ask for the Plover's bill of sale",
     "The Deepwell hail: two ways to ask for the Plover's bill of sale, and Sign off."),
    ("c6-08-playtesting", "a-step-with-no-order",
     ["c6_08/stills/game_c68_order.png"],
     "Helm's Quest Log with Her Log selected, its order reading Scan the Wren from Science",
     "A step in the Quest Log with its order: \"Scan the Wren from Science.\""),
    ("c6-09-revising-between-sessions", "the-was-line",
     ["c6_09/stills/e_r1_was.png"],
     "kestrel_verge.amd open at Enter It Twice, with the Was: line",
     "A revised step in kestrel_verge.amd, with its `Was:` line naming the step it replaces."),
    ("c6-10-publishing", "the-mission-folder",
     ["c6_10/stills/x_zip.png"],
     "The missions folder with the mission folder and its zip beside it",
     "The mission folder, and the zip you hand to a friend."),
    ("c6-11-capstone-studio", "the-campaign-file",
     ["c6_11/stills/e_camp2.png"],
     "campaign.md open at Act Two, with the table of steps",
     "campaign.md at Act Two: the plan your campaign was built from."),
]

for folder, name, srcs, alt, caption in JOBS:
    ims = [Image.open(os.path.join(SRC, s)).convert("RGB") for s in srcs]
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
    print(folder[:5], out.size, "replaced" if n else "no placeholder")
