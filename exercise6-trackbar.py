import cv2 as cv
import numpy as np

def onChange(x):
  pass

def trackbar():
  img = np.zeros((200, 512, 3), np.uint8)
  window_name = 'color_palette'

  cv.namedWindow(window_name)

  cv.createTrackbar('B', window_name, 0, 255, onChange)
  cv.createTrackbar('G', window_name, 0, 255, onChange)
  cv.createTrackbar('R', window_name, 0, 255, onChange)

  switch = '0: OFF\n1: ON'
  cv.createTrackbar(switch, window_name, 0, 1, onChange)

  while True:
    cv.imshow(window_name, img)
    k = cv.waitKey(1)

    if k == 27:
      break

    b = cv.getTrackbarPos('B', window_name)
    g = cv.getTrackbarPos('G', window_name)
    r = cv.getTrackbarPos('R', window_name)
    s = cv.getTrackbarPos(switch, window_name)

    if s == 0:
      img[:] = 0
    else:
      img[:] = [b, g, r]

  cv.destroyAllWindows()

trackbar()