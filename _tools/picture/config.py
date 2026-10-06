"""Where things are, and the one look every frame shares.

Nothing here is per lecture. A lecture's own facts live in its narration/storyboard.py.
Every path can be moved with an environment variable of the same name, prefixed PICTURE_.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
COURSES = os.path.dirname(os.path.dirname(HERE))          # e:\a\author_courses


def _p(name, default):
    return os.environ.get("PICTURE_" + name, default)


OUT_ROOT = _p("OUT_ROOT", r"R:\cosmos\courses")            # <OUT_ROOT>\<c1_05>\...
WORK = _p("WORK", os.path.join(OUT_ROOT, "_work"))         # throwaway: stand-in install, VS Code profile
VOICE_ROOT = _p("VOICE_ROOT", r"R:\cosmos\voice_local")    # <VOICE_ROOT>\<c1_05>\<shot>_<n>.wav (voice_local.py, Chatterbox)
BLENDER = _p("BLENDER", r"C:\b\stable\blender-5.2.2-lts.d13f752e3b9c\blender.exe")
VSCODE = _p("VSCODE", os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs", "Microsoft VS Code", "Code.exe"))

# The stand-in install the "student" works in. capture builds it from these three sources.
STANDIN = os.path.join(WORK, "Cosmos")                     # .\data\missions\MyMission, .\PyRuntime (a junction)
STANDIN_MISSIONS = os.path.join(STANDIN, "data", "missions")
SRC_PYRUNTIME = _p("SRC_PYRUNTIME", r"E:\a\Cosmos-dev\PyRuntime")
SRC_TOOL = _p("SRC_TOOL", "")                              # folder holding sbs.pyz, sbs.bat and __lib__ (released ones)
SRC_VSC_EXT = _p("SRC_VSC_EXT", "")                        # an --extensions-dir with the Artemis AMD add-on in it
PROMPT = "C:\\Cosmos\\data\\missions>"                     # the course's stand-in path (Lecture 2)

# The throwaway VS Code profile. NEVER the user's own.
VSC_DATA = os.path.join(WORK, "vsc_data")
VSC_EXT = os.path.join(WORK, "vsc_ext")

FPS = 30
W, H = 1920, 1080
FADE = 8                 # frames of cross-fade at a cut between two beats
MIN_BEAT = 24            # a beat never shorter than this

# The one kind of motion: a slow push-in. A still that is held for PUSH_HOLD frames or more
# in one beat drifts toward its marks for as long as it stays on screen (all its beats).
PUSH_HOLD = 180          # six seconds
PUSH_RATE = 0.0045       # of the frame, per second
PUSH_MAX = 1.06          # never closer than this
TERM_COLS = 100          # a drawn Command Prompt wraps here, as a real one does at its width

# The look. One accent, nothing else.
ACCENT = (255, 176, 32)
INK = (232, 234, 237)
INK_SOFT = (150, 156, 166)
PAPER = (24, 26, 31)
PANEL = (34, 37, 44)
RULE = (62, 66, 76)
TERM_BG = (12, 12, 12)
TERM_INK = (204, 204, 204)

FONTS = r"C:\Windows\Fonts"
FONT_TEXT = os.path.join(FONTS, "segoeui.ttf")
FONT_BOLD = os.path.join(FONTS, "segoeuib.ttf")
FONT_LIGHT = os.path.join(FONTS, "segoeuil.ttf")
FONT_MONO = os.path.join(FONTS, "consola.ttf")
FONT_MONO_BOLD = os.path.join(FONTS, "consolab.ttf")

# VS Code editor text sizes, in CSS px (the capture machine's scaling multiplies them).
# "wide" and "close" are the pilot's, with the Side Bar. "mid" and "big" are for stills taken
# with the Side Bar hidden ({"side": False}): the same reach of the file, in larger text.
EDITOR_FONT = {"wide": 14, "close": 22, "mid": 18, "big": 25}
EDITOR_LINE = {"wide": 20, "close": 31, "mid": 26, "big": 35}
# A colour nobody would pick by accident: the editor paints the cursor's line with it, and
# capture finds that band to learn where every other line is. Close to the background, so
# it does not read as a mark.
LINE_TELL = "#22252b"


def short_name(lecture):
    """c1-05-the-shape-of-a-record -> c1_05"""
    import re
    return re.sub(r"^(c\d+)-(\d+).*$", r"\1_\2", os.path.basename(lecture.rstrip("/\\")))


def lecture_dir(lecture):
    return lecture if os.path.isabs(lecture) else os.path.join(COURSES, lecture)


def out_dir(lecture):
    return os.path.join(OUT_ROOT, short_name(lecture))
