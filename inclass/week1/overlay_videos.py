# -----------
# Automating Video
# Week 1

# Overlay two videos
# -----------

from random import randint, uniform
import moviepy.editor as mp

# load the videos
video = mp.VideoFileClip("videos/president.mp4")
video2 = mp.VideoFileClip("videos/day.mp4")

clips = []

# grab the subclips from the original
clip1 = video.subclip(10,13)
clip2 = video2.subclip(20,23)

# set the position and size of the videos
clip1 = clip1.set_pos((100, 100)).resize((400,400))
clip1 = clip1.set_start(1)
clip1 = clip1.crossfadein(1)

# append to clips list
clips.append(clip2)
clips.append(clip1)

# make the videos
composition = mp.CompositeVideoClip(clips)
composition.write_videofile("videos/overlay.mp4", fps=25)