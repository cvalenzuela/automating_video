# --------------
# Download a video or a series of videos using youtube-dl
# Cristóbal Valenzuela
# cv965@nyu.edu
# --------------

from __future__ import unicode_literals
import youtube_dl

def download_videos(path, videos, should_I_download_them):
  '''
  Download a video or a set of videos from youtube using youtube-dl
  '''

  ydl = youtube_dl.YoutubeDL({
    'outtmpl': path + '%(id)s%(ext)s',
    'format': '137+best'
    })
  with ydl:
    for video in videos:
      try:
        result = ydl.extract_info(video, download=should_I_download_them)
      except:
        print('Couldnt download a video, sorry!')
  
  print('Done with downloading the videos')
