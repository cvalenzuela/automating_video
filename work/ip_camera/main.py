# --------------
# Project #2 Automating Video
# IP Camera
#
# Cristóbal Valenzuela
# cv965@nyu.edu
# --------------

import argparse
import cv2
from ipcamera import record
from cameras import cameras
import requests
import subprocess
import time
import numpy as np
from os import path, makedirs

# Paths
VIDEO_PATH = './VIDEOS/'
NO_CONTROL_CAMERAS_PATH = VIDEO_PATH + 'NO_CONTROL/'
CONTROL_CAMERAS_PATH = VIDEO_PATH + 'CONTROL/'

TAGS = set()

def init(args):
  '''
  Create the destination paths for the videos
  and get all the available tags
  '''
  # make the dirs
  if not path.exists(NO_CONTROL_CAMERAS_PATH):
    makedirs(NO_CONTROL_CAMERAS_PATH)

  if not path.exists(CONTROL_CAMERAS_PATH):
    makedirs(CONTROL_CAMERAS_PATH)

  # get the tags

  for camera in cameras["no_control"]:
    for tag in camera["tags"]:
      TAGS.add(tag)

  for camera in cameras["control"]:
    for tag in camera["tags"]:
      TAGS.add(tag)
  print(len(TAGS))
  get_videos(args)
  
def get_videos(args):
  '''
  Download videos
  '''
  # for camera in cameras["no_control"][:10]:
  #   print(camera)
  #ip = camera["ip"]
  ip = '100.38.83.153:8081'
  video_path = NO_CONTROL_CAMERAS_PATH + ip + '.mp4'
  record(ip, video_path, '00:00:45', False, '15')

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Make me a trailer please. With big fries, diet coke.')
  parser.add_argument('--q', type=str, help='The query string to search for videos')
  args = parser.parse_args()
  init(args)


