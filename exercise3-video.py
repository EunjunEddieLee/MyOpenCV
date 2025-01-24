import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def showVideo():
  try:
    print('Turning on the camera.')
    # cap = cv.VideoCapture(0) # access webCam
    cap = cv.VideoCapture('./videos/goat.mp4') # import video

  except:
    print('Failed turning on. Exiting ...')
    return
  
  cap.set(3, 480) # 3: width
  cap.set(4, 320) # 4: height

  while True:
    ret, frame = cap.read()

    if not ret:
      print("Can't receive video frame. Exiting ...")
      break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Video', gray)

    k = cv.waitKey(1)
    if k == 27:
      break

  cap.release()
  cv.destroyAllWindows()

def writeVideo():
  try:
    print('Turning on the camera.')
    cap = cv.VideoCapture(0) # access webCam
    # cap = cv.VideoCapture('./videos/goat.mp4') # import video

  except:
    print('Failed turning on. Exiting ...')
    return
  
  fps = 20.0
  width = int(cap.get(3))
  height = int(cap.get(4))
  fcc = cv.VideoWriter_fourcc('D', 'I', 'V', 'X')

  out = cv.VideoWriter('./videos/exercise2-video-MyCam.avi', fcc, fps, (width, height))
  print('start recording ...')

  while True:
    ret, frame = cap.read()

    if not ret:
      print("Can't receive video frame. Exiting ...")
      break

    cv.imshow('frame', frame)
    out.write(frame)

    k = cv.waitKey(1)
    if k == 27:
      print('End recording ...')
      break
  
  cap.release()
  out.release()
  cv.destroyAllWindows()

# showVideo()
writeVideo()