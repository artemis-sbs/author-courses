"""The Blender half: an edit list -> the sequencer -> a test frame, then the mp4.

    blender -b --factory-startup --python blend_assemble.py -- <edl.json> check|encode

edl.json (written by make.py): fps, size, frames, strips [{name, start, length, files}],
sounds [{name, file, start}], blend, check_png, check_frame, mp4. Frames in the list count
from 0; Blender's count from 1.

The trap this is written round (Blender 5.x): the sequencer belongs to the WORKSPACE. A
headless render of a scene that merely has strips renders that scene's empty 3D view, with
no error. So the edit's scene is named as the workspace's sequencer scene and the render is
asked for it; "check" writes one frame for make.py to look at before anything long runs.
"""
import json
import os
import sys

import bpy

SCENE = "EDIT"


def strips_of(editor):
    return editor.strips if hasattr(editor, "strips") else editor.sequences


def build(edl):
    for s in list(bpy.data.scenes):
        if s.name == SCENE:
            bpy.data.scenes.remove(s)
    scene = bpy.data.scenes.new(SCENE)
    r = scene.render
    r.fps = edl["fps"]
    r.resolution_x, r.resolution_y = edl["size"]
    r.resolution_percentage = 100
    scene.frame_start, scene.frame_end = 1, edl["frames"]
    try:
        scene.view_settings.view_transform = "Standard"   # stills must come out the colours they went in
        scene.view_settings.look = "None"
    except Exception as e:
        print("ASSEMBLE view transform:", e)
    editor = scene.sequence_editor_create()
    strips = strips_of(editor)
    pushed = 0
    try:
        bpy.context.preferences.edit.keyframe_new_interpolation_type = "LINEAR"
    except Exception as e:
        print("ASSEMBLE interpolation:", e)
    for n, s in enumerate(edl["strips"]):
        first = s["files"][0]
        strip = strips.new_image(name=s["name"], filepath=first, channel=1 + n % 2, frame_start=s["start"] + 1)
        if len(s["files"]) > 1:
            for f in s["files"][1:]:
                strip.elements.append(os.path.basename(f))
        else:
            try:
                strip.frame_final_duration = s["length"]
            except Exception:
                pass
            if strip.frame_final_duration != s["length"]:      # hold it the plain way
                for _ in range(s["length"] - 1):
                    strip.elements.append(os.path.basename(first))
        if strip.frame_final_duration != s["length"]:
            print(f"ASSEMBLE Error: {s['name']} is {strip.frame_final_duration} frames, wanted {s['length']}")
            sys.exit(2)
        if s.get("zoom"):                                      # the slow push-in: two keys, a straight line
            t = strip.transform
            u, v = s["origin"]
            t.origin = (u, 1.0 - v)                            # Blender counts up from the bottom
            f0, f1 = s["start"] + 1, s["start"] + s["length"]
            for frame, scale in ((f0, s["zoom"][0]), (f1, s["zoom"][1])):
                t.scale_x = t.scale_y = scale
                t.keyframe_insert("scale_x", frame=frame)
                t.keyframe_insert("scale_y", frame=frame)
            pushed += 1
    print("ASSEMBLE pushes:", pushed)
    for s in edl.get("sounds", []):
        strips.new_sound(name=s["name"], filepath=s["file"], channel=4, frame_start=s["start"] + 1)
    for m in edl.get("markers", []):
        scene.timeline_markers.new(m["name"], frame=m["start"] + 1)
    if bpy.context.window is not None:
        bpy.context.window.scene = scene
    try:
        bpy.context.workspace.sequencer_scene = scene
    except Exception as e:
        print("ASSEMBLE no workspace sequencer scene:", e)
    return scene


def render(**kwargs):
    try:
        bpy.ops.render.render(scene=SCENE, use_sequencer_scene=True, **kwargs)
    except TypeError:                                          # 4.x: the scene's own editor is the only one
        bpy.ops.render.render(scene=SCENE, **kwargs)


def check(scene, edl):
    r = scene.render
    try:
        r.image_settings.media_type = "IMAGE"
    except (AttributeError, TypeError):
        pass
    r.image_settings.file_format = "PNG"
    for frame, path in edl["checks"]:
        scene.frame_set(frame + 1)
        r.filepath = path
        render(write_still=True)
    print("ASSEMBLE CHECKED", len(edl["checks"]), "frames")


def encode(scene, edl):
    r = scene.render
    try:
        r.image_settings.media_type = "VIDEO"
    except (AttributeError, TypeError):
        pass
    r.image_settings.file_format = "FFMPEG"
    r.ffmpeg.format = "MPEG4"
    r.ffmpeg.codec = "H264"
    r.ffmpeg.constant_rate_factor = "HIGH"
    r.ffmpeg.gopsize = 30
    r.ffmpeg.audio_codec = "AAC" if edl.get("sounds") else "NONE"
    r.filepath = edl["mp4"]
    render(animation=True)
    print("ASSEMBLE ENCODED", edl["mp4"])


def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    with open(argv[0], encoding="utf-8") as f:
        edl = json.load(f)
    scene = build(edl)
    print(f"ASSEMBLE {len(edl['strips'])} strips, {edl['frames']} frames, blender {bpy.app.version_string}")
    if argv[1] == "check":
        check(scene, edl)
    else:
        bpy.ops.wm.save_as_mainfile(filepath=edl["blend"], check_existing=False)
        encode(scene, edl)


main()
