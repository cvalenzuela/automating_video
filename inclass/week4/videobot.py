# -*- coding: utf-8 -*-
# chroma key with vidpy

import glob
import random
import time
from vidpy import Clip, Composition

# take all the elements in a folder that end with a specific extension 
videos = glob.glob('*.mp4') # this is an array
video = random.choice(videos)

clips = []
x = 0
y = 0
start = 0

backgrounds = ['#fffd43', '#fc8274', '#82ff72']

for i in range(0,10): 
  clip = Clip(video)
  clip.chroma(color='#A0A0A0')
  clip.set_offset(start)
  clip.position(y=y)
  clip.fadein(0.2)
  clip.fadeout(0.2)

  clips.append(clip)  

  start += 0.5
  x += 150
  y += 2

composition = Composition(clips, bgcolor=random.choice(backgrounds))
#this previews the video but it does not save it
composition.preview() 
#outname = 'coolvideo_{}.mp4'.format(int(time.time))
#composition.save(outname)