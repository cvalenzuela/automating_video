# -*- coding: utf-8 -*-
# creating text

import glob
from vidpy import Clip, Composition, Text
import random
import time

text = '''
The history of all hitherto existing society 
is the history of class struggles. Freeman and 
slave, patrician and plebeian, lord and serf, 
guild-master and journeyman, in a word, oppressor
and oppressed, stood in constant opposition to
one another, carried on an uninterrupted, now 
hidden, now open fight, a fight that each time 
ended, either in a revolutionary reconstitution
of society at large, or in the common ruin of 
the contending classes.'''

sentences = text.split('\n')
sentence = random.choice(sentences)
sentence = sentence.strip()
sentence = sentence.upper()
print sentence

backgrounds = glob.glob('*.jpg')
background_image = random.choice(backgrounds)

background_clip = Clip(background_image) # add an image
# background_clip.squareblur(0.5) # animation
background_clip.squareblur('0=0.5;100=0;60=0.2;100=0.2') # define it by frames
clip = Text(sentence, olcolor='#000000', outline=10) # style the text
# clip.position(x=0) # this is not working for now
clip.glow()

# make the composition, if you dont set the duration it will go forever
composition = Composition([background_clip, clip], width=1200, height=700, bgcolor='#ff0000', duration=5)
composition.preview()
#composition.save('commie_{}.mp4'.format(time.time()))