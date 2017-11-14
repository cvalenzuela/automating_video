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
from os import path, makedirs, remove
import datetime

now = str(datetime.datetime.now())[20:-1]

# Paths
VIDEO_PATH = './VIDEOS/'
NO_CONTROL_CAMERAS_PATH = VIDEO_PATH + 'NO_CONTROL/'
CONTROL_CAMERAS_PATH = VIDEO_PATH + 'CONTROL/'
HAND_PICK_PATH = VIDEO_PATH + 'HANDPICK/'

TIME_TO_RECORD = '00:00:10'
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

  if not path.isfile('tags.txt'):
    with open('tags.txt', 'xt') as f:
      f.write(', '.join(TAGS))
      f.close()
  
 
def get_videos(args):
  '''
  Download videos
  ** Watch out for this, its memory instensive **
  '''
  # Change the type/amount of camera to use here
  for camera in cameras["control"][10:20]:
    ip = camera["ip"]
    print('getting', ip)

    # name for the video that has its tags
    video_name = ip
    for tag in camera["tags"]:
      video_name = video_name + ',' +  tag
    video_path = CONTROL_CAMERAS_PATH + video_name + '.mp4'

    # record the video
    record(ip, video_path, TIME_TO_RECORD, False, '15')

def get_one(args):
  '''
  Download just one defined IP video
  '''
  IP = '182.253.78.11:84' # 
  video_path = HAND_PICK_PATH + IP + '.mp4'
  record(IP, video_path, TIME_TO_RECORD, False, '20')

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Make me a trailer please. With big fries, diet coke.')
  parser.add_argument('--q', type=str, help='The query string to search for videos')
  args = parser.parse_args()
  
  #init(args) # init
  #get_videos(args)# download videos
  get_one(args) # get one specific video


