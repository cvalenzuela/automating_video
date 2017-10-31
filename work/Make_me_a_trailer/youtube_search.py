# --------------
# Search for videos using the YouTube API
# Based on: https://developers.google.com/youtube/v3/code_samples/python#search_by_keyword
# Cristóbal Valenzuela
# cv965@nyu.edu
# --------------

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import private 
import json

# API stuff
DEVELOPER_KEY = private.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  '''
  Search for a list of youtube videos using Google's Cloud API.
  This will return a list of id urls with the format
  https://www.youtube.com/watch?v=VIDEOID
  '''
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
  search_response = youtube.search().list(
    q=options.q,
    part="id",
    maxResults=options.max
  ).execute()

  videos = []

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("https://www.youtube.com/watch?v=%s" % (search_result["id"]["videoId"]))

  print('Done with the youtube search. Got this results {}'.format(videos))
  return videos

if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="nyu")
  argparser.add_argument("--max", help="Max results", default=25)
  args = argparser.parse_args()

  youtube_search(args)

