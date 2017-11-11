# 
# Vidpy demo
# 

from vidpy import Clip, Composition

clip1 = Clip("vid1.mp4")
clip2 = Clip("vid2.mp4")

clip1.repeat(3)

comp = Composition([clip1, clip2], singletrack=True)

comp.preview()