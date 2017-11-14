from moviepy.editor import *
import argparse
from random import choice, randrange, uniform
#Separates clip list into chunks
def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0

  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg

  return out

def main(): 
  inputfile = ''
  outputfile = 'output.mp4'
  rows = 3
  delay = 0.25
  rand = 0  

  #Load clip
  videos = []
  video1 = VideoFileClip('VIDEOS/NO_CONTROL/67.78.24.86:8080,pool,beach,palm trees,resort,florida,palm harbor.mp4').subclip(0,-0.1)
  video1 = video1.resize(width=((video1.w)/rows))

  video2 = VideoFileClip('VIDEOS/NO_CONTROL/75.145.217.140:8081,ducks,animals,tennessee,memphis.mp4').subclip(0,-0.1)
  video2 = video2.resize(width=((video2.w)/rows))

  videos.append(video1)
  videos.append(video2)
  #init clips list
  clips_list = []
  offset = 0

  #Build clips list
  for i in range(rows*rows):
    video = choice(videos)
    new_clip = video.set_start(int(randrange(1,int(video.duration))))
    clips_list.append(new_clip)
    offset += (delay + uniform((rand*-1),rand))	
		
  #chunks array into rows
  arranged_clips = clips_array(chunkIt(clips_list,rows))

  #renders video
  arranged_clips.write_videofile(outputfile, 
    fps=25,   
    codec='libx264', 
    audio_codec='aac', 
    temp_audiofile='temp-audio.m4a', 
    remove_temp=True)

if __name__ == "__main__":
  main()