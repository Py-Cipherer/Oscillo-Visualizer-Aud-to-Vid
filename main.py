import json
import numpy as np
import cv2
from visuals.background import generate_frame
from visuals.captions import draw_caption
from moviepy import AudioFileClip
import moviepy.video.io.ffmpeg_writer as ffmpeg_writer

energy = np.load("audio/energy.npy")
segments = json.load(open("captions/transcript.json", encoding="utf-8"))

fps = 30
duration = len(energy) / fps

audio = AudioFileClip("audio/input.m4a")
audio_duration = audio.duration

writer = ffmpeg_writer.FFMPEG_VideoWriter(
    "Generation.mp4",
    (1080, 1920),
    fps,
    codec="libx264",
    audiofile="audio/input.m4a"
)

for i, e in enumerate(energy):
    t = i / fps
    if t > audio_duration:
        break
    frame = generate_frame(e)

    for seg in segments:
        if seg["start"] <= t <= seg["end"]:
            frame = draw_caption(frame, seg["text"])

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    writer.write_frame(frame)

writer.close()
audio.close()
print("Progress complete.")

