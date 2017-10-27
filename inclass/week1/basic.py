# -----------
# Automating Video
# Week 1

# Download a video with: youtube-dl -f 22 YOUTUBEURL 
# -----------

import moviepy.editor as mp

# load the videos
presidentVideo = mp.VideoFileClip("videos/president.mp4").subclip(0,3)
dayVideo = mp.VideoFileClip("videos/day.mp4").subclip(2,5)

# Resize in case videos have issues 
# presidentVideo = video.resize((800,600))
# dayVideo = video.resize((800,600))

# set all clips to create video
clips = [presidentVideo, dayVideo]

# create a composition by concatenate the videos in the clips list
composition = mp.concatenate(clips)
composition.write_videofile("videos/composition.mp4")
