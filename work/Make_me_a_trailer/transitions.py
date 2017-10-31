# --------------
# Get small clips from a videos
# This script is used to get the transition in between scences of the action trailers
# Cristóbal Valenzuela
# cv965@nyu.edu
# --------------

import argparse
import csv
import moviepy.editor as mp

from os import getcwd
PATH = getcwd()

def get_subclips(options):
  '''
  Get sub clips from a video. If save_as_files is True, 
  then save all subclips to disk, if not, return a list of clips.
  '''
  video = mp.VideoFileClip(options['src'])
  clips = []

  with open(options['data'], 'r') as csvfile:
    time_frames = csv.reader(csvfile, delimiter=',', quotechar='|')
    for start, end in time_frames:
      subclip = video.subclip(int(start), int(end))
      if(options['save_to_disk']):
        subclip.write_videofile("{}/{}{}.mp4".format(PATH,start,end), codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)
      else:
        clips.append(subclip)
  
  print('Done with transitions. Got {} transitions.'.format(len(clips)))
  return clips

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Get subclips from a video')
  parser.add_argument('--src', type=str, help='The video to get subclips from. There should also be a csv file with the same name', default='transitions.mp4')
  parser.add_argument('--data', type=str, help='A file.csv that holds the data to cut', default='transitions.csv')
  parser.add_argument('--save_to_disk', help='Save files to disk?', default=True)
  args = parser.parse_args()
  get_subclips(args)