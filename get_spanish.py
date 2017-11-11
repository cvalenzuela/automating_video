'''
Get spanish subtitles from a video
'''

import argparse
from subprocess import call
from os import remove

def main(args):
  AUDIO_FILE = "{}.temp.wav".format(args.file)
  # Get the temp wav sound first
  call(["ffmpeg", "-y", "-i", args.file, "-acodec", "pcm_s16le", "-ac", "1", "-ar", "16000", AUDIO_FILE])
  print('Done with the {}'.format(AUDIO_FILE))
  # Get the transcription
  call(["pocketsphinx_continuous", "-infile", AUDIO_FILE, "-time", "yes", "-logfn", "/dev/null", "-vad_prespeech", "10", "-vad_postspeech", "50", "-hmm", "es/model_parameters/voxforge_es_sphinx.cd_ptm_4000/", "-lm", "cmusphinx-es-5.2/etc/es-20k.lm.gz", "-dict", "es.dict", ">>", "{}.transcription.txt".format(args.file)], shell=True)
  # remove the temp file
  remove(AUDIO_FILE)
  print('Listo!')

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Get spanish subtitles from a video')
  parser.add_argument('--file', type=str, help='The video file')
  args = parser.parse_args()
  main(args)
