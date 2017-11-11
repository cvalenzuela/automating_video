# ffmpeg util tools

## convert between formats
```bash
ffmpeg -i input.mp4 output.avi
```

## make a gif from a video

```bash
ffmpeg -i input.mp4 -r 3 -s:v 100x100 output.gif
```
- r: frame per second
- s:v set the size

## create images from video

```bash
ffmpeg -i input.mp4 -r 1 output_%d.jpg
```
%d is the frame #
- r: frames per second to store 

## make a video from a series of images

```bash
ffmpeg -f image2 -i image_collection_%d.jpg output.mp4
```

## extract audio from video

```bash
ffmpeg -i image2 output.mp3
```

## effects

- Fade in:

```bash
ffmpeg -i input.mp4 -vf "fade=in:0:20" output.mp4
```
- Blur:

```bash
ffmpeg -i input.mp4 -vf "boxblur=luma_radius=20-...." output.mp4
```
