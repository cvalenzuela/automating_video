# Automating Video
# Assigment 1

import urllib.request
import urllib.parse
import re
from subprocess import call
import moviepy.editor as mp
from random import shuffle, uniform

userInput = input("Videos to load: ")

queries = userInput.split(',')

urls = []
print("Preparing videos...")
for query in queries:
  query_string = urllib.parse.urlencode({"search_query" : query})
  html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
  search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
  urls.append("http://www.youtube.com/watch?v=" + search_results[0])

videos = []
print("Downloading videos...")
for i in range(len(urls)):
  name = "./temp/{}.mp4".format(i)
  videos.append(name)
  call(["youtube-dl", "-f", "22", urls[i], "-o", name])

videosBuffer = []
print("Got videos. Preparing to edit them...")
for i in range(len(urls)):
  videosBuffer[i] = mp.VideoFileClip(videos[i])

clips = []
print("Editing videos...")


for i in range(0, 10):
  start = uniform(0, video.duration - 1)
  end = start + 1
  clip1 = video.subclip(start, end)

  clips.append(clip1)

# make the videos
composition = mp.concatenate(clips)
composition.write_videofile("videos/juxtapose.mp4", fps=25)