# --------------
# Composite a video
# --------------

import argparse
import moviepy.editor as mp
from random import shuffle, uniform, choice, sample, randrange
from os import makedirs, path, getcwd, listdir
from os.path import isfile, join
import re
from shutil import rmtree
import datetime

PATH = getcwd()
COMPOSITION_PATH = PATH + '/compositions/'
NO_CONTROL_VIDEOS_PATH = PATH + '/VIDEOS/NO_CONTROL/'
CONTROL_VIDEOS_PATH = PATH + '/VIDEOS/CONTROL/'
now = datetime.datetime.now()

# PARAMETERS TO CHANGE
TOPICS = ['all']
DURATION = 120
CLIP_DURATION = 2
# END OF PARAMETERS

tags_to_videos = {}
clips_from_video = {}
possible_videos = set()
composition_clips = []
no_control_videos = [f for f in listdir(NO_CONTROL_VIDEOS_PATH) if isfile(join(NO_CONTROL_VIDEOS_PATH, f)) and '.mp4' in f]
control_videos = [f for f in listdir(CONTROL_VIDEOS_PATH) if isfile(join(CONTROL_VIDEOS_PATH, f)) and '.mp4' in f]
open_videos = set()

def config(options):
  '''
  Config settings to make a composition with ip cameras
  '''
  # dir to store compositions
  if not path.exists(COMPOSITION_PATH):
    makedirs(COMPOSITION_PATH)

  # make a map of tags -> videos
  # ie: {'shop': ['181.58.119.179,shop,mall.mp4'], 'car': ['181.58.119.179,house,car.mp4'],
  for name in no_control_videos:
    tags = name.split(',')
    tags.pop(0) # remove the ip
    tags[-1] = tags[-1].split('.')[0] # from the last tag, get rid of the .mp4 extension
    for tag in tags:
      if '.' not in tag:
        if tag in tags_to_videos:
          tags_to_videos[tag].append(name)
        else:
          tags_to_videos[tag] = [name]


  # make a map of video -> clips only for the selected tags
  # ie: {'181.58.119.179,shop,mall.mp4': [<clip0>,<clip1>]}
  for topic in TOPICS:
    if topic == 'all':
      for tag in tags_to_videos:
        for video_name in tags_to_videos[tag]:
          if video_name not in open_videos:
            print('Getting clips from {}...'.format(video_name))
            start = 0
            duration = CLIP_DURATION
            end = start + duration
            clips = []
            video = mp.VideoFileClip(NO_CONTROL_VIDEOS_PATH + video_name)
            open_videos.add(video_name)
            while end < int(video.duration):
              clip = video.subclip(start, end).resize((600,400)) #clip = video.subclip(start, end)
              clips.append(clip)
              start = start + duration
              end = end + duration

            clips_from_video[video_name] = clips
            print('Got {} clips for {}'.format(len(clips), video_name))
        
    else:
      if topic in tags_to_videos:
        for video_name in tags_to_videos[topic]:
          if video_name not in open_videos:
            print('Getting clips from {}...'.format(video_name))
            start = 0
            duration = CLIP_DURATION
            end = start + duration
            clips = []
            video = mp.VideoFileClip(NO_CONTROL_VIDEOS_PATH + video_name)
            open_videos.add(video_name)
            while end < int(video.duration):
              clip = video.subclip(start, end).resize((600,400)) #clip = video.subclip(start, end)
              clips.append(clip)
              start = start + duration
              end = end + duration

            clips_from_video[video_name] = clips
            print('Got {} clips for {}'.format(len(clips), video_name))
  
  # store all possible video matching the TOPIC
  if TOPICS[0] == 'all':
    for tags in tags_to_videos:
      for video in tags_to_videos[tags]:
        possible_videos.add(video)
  else:
    for topic in TOPICS:
      if topic in tags_to_videos:
        for video in tags_to_videos[topic]:
          possible_videos.add(video)
          
def make_composition():
  '''
  Make a simple composition of videos
  '''
  print('Making a composition')
  clips_amount = int(DURATION/CLIP_DURATION)
  selected_videos = set()
  
  for clip in range(clips_amount):
    video = sample(possible_videos, 1)[0]
    possible_videos.remove(video)
    composition_clips.append(choice(clips_from_video[video]))

  composition = mp.concatenate(composition_clips)
  composition.write_videofile("{}{}.mp4".format(COMPOSITION_PATH, now), 
    fps=25,   
    codec='libx264', 
    audio_codec='aac', 
    temp_audiofile='temp-audio.m4a', 
    remove_temp=True
  )

def make_grid():
  '''
  Makes a grid of videos
  '''
  print('Making a grid')
  ROWS = 10

  #Load clip
  clips = []

  for name in no_control_videos:
    clip = mp.VideoFileClip(NO_CONTROL_VIDEOS_PATH + name).subclip(0,30)
    clip = clip.resize((600,400))
    clips.append(clip)

  clips_list = []
  #Build clips list
  for i in range(ROWS*ROWS):
    video = choice(clips)
    new_clip = video.set_start(0)
    clips_list.append(new_clip)
		
  #chunks array into rows
  arranged_clips = mp.clips_array(chunkIt(clips_list,ROWS))

  #renders video
  arranged_clips.write_videofile("{}{}.mp4".format(COMPOSITION_PATH, now), 
    fps=25,   
    codec='libx264', 
    audio_codec='aac', 
    temp_audiofile='temp-audio.m4a', 
    remove_temp=True
  )


def chunkIt(seq, num):
  '''
  Separates clip list into chunks
  '''
  avg = len(seq) / float(num)
  out = []
  last = 0.0

  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg

  return out

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Make a composition with ip videos')
  parser.add_argument('--q', type=str, help='The query string to search for videos')
  args = parser.parse_args()
  #config(args)
  #make_composition() 
  make_grid()