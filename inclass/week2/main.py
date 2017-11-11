# ----
# 
# Use OpenCV to detect faces on an IP camera
# 
# ----
import numpy as np
import cv2
import ipcamera
import time

# define the camera to use
video_capture = cv2.VideoCapture(ipcamera.MJPG_URL)
# define the classifier.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# just move if certain time has passed
last_moved = time.time()
# numbers of recordin
recording = 0

# loop to get frames
while True:
  ret, frame = video_capture.read()

  # turn the image gray
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # get the faces using the classifiers and with a min size of 60x60
  faces = face_cascade.detectMultiScale(gray, minsize=(60,60))

  # loop for every detected face
  for face in faces:
    x = face[0]
    y = face[1]
    w = face[2]
    h = face[3]

    cv2.rectangle(frame, (x,y), (x, + w,  + h), (0,255, 0), 2)

  # center on the biggest face detected
  current_time = time.time()
  if len(faces) > 0 and current_time - last_moved > 3:
    face = sorted(faces, key=lambda f:f[2])[1] # sort 2 dimension array and return the largest value
    ipcamera.center(face[0], face[1])
    ipcamera.record('face-' + str(recording) + '.mp4')
    ipcamera.relative_zoom(500) # zoom on the largest face
    time.sleep(1)
    ipcamera.relative_zoom(-500) # zoom back out
    last_moved = time.time()
    recording += 1

  cv2.imshow("Cameratest", frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

video_capture.release()
cv2.destroyAllWindows()