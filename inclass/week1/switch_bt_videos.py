# -----------
# Automating Video
# Week 1

# Switch between two videos frames 
# -----------

from random import randint, uniform
import moviepy.editor as mp

# load the videos
video = mp.VideoFileClip("videos/president.mp4")
video2 = mp.VideoFileClip("videos/day.mp4")

clips = []

# create random short videos with the input videos
for i in range(0, 10):
  start = uniform(0, video.duration - 1)
  end = start + 1
  clip1 = video.subclip(start, end)

  start = uniform(0, video2.duration - 1)
  end = start + 1
  clip2 = video2.subclip(start, end)

  clips.append(clip1)
  clips.append(clip2)

# make the videos
composition = mp.concatenate(clips)
composition.write_videofile("videos/juxtapose.mp4", fps=25)
