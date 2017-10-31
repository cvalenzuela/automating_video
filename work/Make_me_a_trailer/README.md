# Make me a trailer

Generate a movie trailer based on other movie trailers.

Generated Trailers:

- [Action Movie](https://youtu.be/gCDcsX4-P4M)
- [~~Romance Movie~~]()
- [~~Horror Movie~~]()

## Install

```bash
pip install -r requirements.txt
```

## Create a Trailer

### 1. Using a list of videos

```bash
python main.py --videos videos.txt
```

The `.txt` file should look like:

`videos.txt`:
```bash
https://www.youtube.com/watch?v=nW7ImhXMrl8
https://www.youtube.com/watch?v=1z0RaFiQo0g
[more links]
```

### 2. With a search term

```bash
python main.py --q 'action movie trailer' --max 25
```

This will query youtube for videos using that search term.

## Usage

```bash
usage: main.py [-h] [--q Q] [--max MAX] [--transitions_src TRANSITIONS_SRC]
               [--transitions_data TRANSITIONS_DATA] [--videos VIDEOS]

Make me a trailer please. With big fries, diet coke.

optional arguments:
  -h, --help            show this help message and exit
  --q Q                 The query string to search for videos
  --max MAX             Max results to search in Youtube
  --transitions_src TRANSITIONS_SRC
                        A video source in mp4 Use this arg to create
                        transitions from a specific video.
  --transitions_data TRANSITIONS_DATA
                        The data from where to get the transitions, must be in
                        .csv
  --videos VIDEOS       File with the video urls
```




