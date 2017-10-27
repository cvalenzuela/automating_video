# -----------
# Automating Video
# Week 1

# Create a video with random short videos
# -----------

import moviepy.editor as mp
from random import shuffle 

video = mp.VideoFileClip("videos/president.mp4")

clips = []

# variables
start = 0
duration = 0.5
end = start + duration

# cut the video in segments of 'duration'
while end < video.duration:
  clip = video.subclip(start, end)
  clips.append(clip)
  start = start + duration
  end = end + duration

# shuffle and just get the first 10 'clips'
shuffle(clips)
clips = clips[0:10]

# Make the video
composition = mp.concatenate(clips)
composition.write_videofile("videos/random.mp4")