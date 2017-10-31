# --------------
# Project #1 Automating Video
# Make me a trailer
#
# Cristóbal Valenzuela
# cv965@nyu.edu
# --------------

import argparse
import moviepy.editor as mp
from random import shuffle, uniform, choice
from os import makedirs, path, getcwd, listdir
from os.path import isfile, join
import re
from shutil import rmtree
import datetime
import youtube_dl

from youtube_search import youtube_search
from download_video import download_videos
from transitions import get_subclips

PATH = getcwd()
TEMP_PATH = PATH + '/temp/'
VIDEOS_PATH = PATH + '/videos/'
now = datetime.datetime.now()

def make_video(options):
  '''
  Using the provided query string, this function will search in Youtube for 
  videos matching the query, download them to a /temp folder, cut them into 
  segments and create once single video. It will then clean the /temp folder
  leaving only one video.
  '''

  # dir to store videos temporary
  if not path.exists(TEMP_PATH):
    makedirs(TEMP_PATH)

  # make and get the transitions of given mp4 file
  if options.transitions_src:
    transitions = get_subclips({ 
      "src": options.transitions_src, 
      "data": options.transitions_data, 
      "save_to_disk": False 
    })

  # use a predifined file with urls or search for videos
  videos_urls = None
  if options.videos:
    file = open(options.videos, "r") 
    videos_urls = file.read().split('\n')
  else:
    videos_urls = youtube_search(options)

  # download the videos
  download_videos(TEMP_PATH, videos_urls, True)

  # get all the downloaded videos
  videos_src = [f for f in listdir(TEMP_PATH) if isfile(join(TEMP_PATH, f))]

  # divide the videos in small clips
  all_clips = []

  for video_src in videos_src:
    if '.mp4' in video_src:
      print('Getting clips from {}...'.format(video_src))
      start = 0
      duration = 4
      end = start + duration
      clips = []
      video = mp.VideoFileClip(TEMP_PATH + video_src)

      while end < int(video.duration):
        clip = video.subclip(start, end).resize((900,800))
        #clip = video.subclip(start, end)
        clips.append(clip)
        start = start + duration
        end = end + duration

      all_clips.append(clips)
      print('Got {} clips for {}'.format(len(clips), video_src))

  # get random clips to form the final movie
  final_clips = []

  # start with intros
  for n in range(5):
    source = choice(all_clips)
    clip = choice(source[:int(len(source)/3)])
    final_clips.append(clip)
    if options.transitions_src:
      final_clips.append(choice(transitions))

  # Middle
  for n in range(4):
    source = choice(all_clips)
    clip = choice(source[int(len(source)/3): int((len(source)/3))*2])
    final_clips.append(clip)
    if options.transitions_src:
      final_clips.append(choice(transitions))

  # end
  for n in range(4):
    source = choice(all_clips)
    clip = choice(source[int((len(source)/3))*2:len(source)])
    final_clips.append(clip)
    if options.transitions_src:
      final_clips.append(choice(transitions))

  print('Making a video with {} clips...'.format(len(final_clips)))
  composition = mp.concatenate(final_clips)
  composition.write_videofile("{}{}.mp4".format(VIDEOS_PATH, now), 
    fps=25,   
    codec='libx264', 
    audio_codec='aac', 
    temp_audiofile='temp-audio.m4a', 
    remove_temp=True
  )

  # remove temp folder
  clean_temp()

def clean_temp():
  '''
  Delete the /temp folder and all its videos
  '''
  rmtree(TEMP_PATH, ignore_errors=False, onerror=None)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Make me a trailer please. With big fries, diet coke.')
  parser.add_argument('--q', type=str, help='The query string to search for videos')
  parser.add_argument('--max', help='Max results to search in Youtube', default=25)
  parser.add_argument('--transitions_src', help='A video source in mp4 Use this arg to create transitions from a specific video.')
  parser.add_argument('--transitions_data', help='The data from where to get the transitions, must be in .csv')
  parser.add_argument('--videos', help='File with the video urls')
  args = parser.parse_args()
  make_video(args)