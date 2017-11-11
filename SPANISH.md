# Videogrep en Español!

## Getting the subtitles

- Using youtube-dl:

```bash
youtube-dl --write-sub "https://www.youtube.com/watch?v=i2ELoGAUmr8"
```

- Skip the video and just get the subtitles

```bash
youtube-dl --write-sub --skip-download "https://www.youtube.com/watch?v=i2ELoGAUmr8" 
```

- Convert from vtt (youtube format) to .srt
First:

```bash
npm install -g vtt-to-srt
```

Then:

```bash
vtt-to-srt example.vtt example.srt
```

## Using spanish subtitles

There are two ways of working with spanish subtitles.

### With subtitles or cc for sentence recognition

1. Download a video:

```bash
youtube-dl https://www.youtube.com/watch?v=i2ELoGAUmr8 --write-sub
```

2. (Optional): If the video doesn't have subtitles, you will need to download the close caption and then convert them to `.srt`

  - 1 Download with [downsub](http://downsub.com/)
  - 2 Convert with `vtt-to-srt input.vtt output.srt`

3. Make the video
```bash
videogrep --input "video.mp4" --search 'perro' --output output.mp4
```

## With pocketsphinx for word level recognition.

1. Install pocketsphinx

  ```bash
  brew tap watsonbox/cmu-sphinx
  brew install --HEAD watsonbox/cmu-sphinx/cmu-sphinxbase
  brew install --HEAD watsonbox/cmu-sphinx/cmu-sphinxtrain
  brew install --HEAD watsonbox/cmu-sphinx/cmu-pocketsphinx
  ```

2. Download the dictionary from [here](/es). Everything should be in a folder called `es`

3. Convert the audio from the video file to `.wav`. This is the format pocketsphinx uses to transcribe

  ```bash
  ffmpeg -y -i video.mp4 -acodec pcm_s16le -ac 1 -ar 16000 video.wav
  ```

3. Get the transcribe pointing to the dictionary and the downloaded model.

  ```bash
  pocketsphinx_continuous -infile "video.wav" -time yes -logfn /dev/null -vad_prespeech "10" -vad_postspeech "50" -hmm cmusphinx-es-5.2/model_parameters/voxforge_es_sphinx.cd_ptm_4000/ -lm cmusphinx-es-5.2/etc/es-20k.lm.gz -dict es.dict > video.mp4.transcription.txt
  ```

This will save a file called `video.mp4.transcription.txt`.

4. Run videogrep with transcribe

  ```bash
  videogrep --input video.mp4 --use-transcript --search-type word --search 'que'
  ```

## Videogrep

- Make a video with a .srt file and video file. They need to have the same name.
This will output a video with all the sentences where `dog` is found.

```bash
videogrep --input "video.mp4" --search 'dog' --output output.mp4
```

- Regex based search

```bash
videogrep --input "video.mp4" --search 'why|because' --output output.mp4
```

- Get the subtitles for a video with pocketsphinx. This is for word level cuts.

```bash
videogrep --input "video.mp4" --transcribe
```

The output will be `video.mp4.transcription.txt`

- Using word level cuts

The transcribe should be `video.mp4.transcription.txt`

```bash
videogrep --input debate.mp4 --use-transcript --search-type word --search 'dog'
```