import cv2 as cv
import numpy as np
from random import shuffle
import math


mode, drawing = True, False
ix, iy = -1, -1
B = [i for i in range(256)]
G = [i for i in range(256)]
R = [i for i in range(256)]

def onMouse(event, x, y, flags, param):
  global ix, iy, drawing, mode, B, G, R
  
  if event == cv.EVENT_LBUTTONDOWN:
    drawing = True
    ix, iy = x, y
    shuffle(B), shuffle(G), shuffle(R)
  elif event == cv.EVENT_MOUSEMOVE:
    if drawing:
      if mode: # rectangle mode
        cv.rectangle(param, (ix, iy), (x, y), (B[0], G[0], R[0]), -1)
      else:
        r = (ix - x)**2 + (iy-y)**2
        r = int(math.sqrt(r))
        cv.circle(param, (ix, iy), r, (B[0], G[0], R[0]), -1)
  elif event == cv.EVENT_LBUTTONUP:
    drawing = False
    if mode:
      cv.rectangle(param, (ix, iy), (x, y), (B[0], G[0], R[0]), -1)
    else:
      r = (ix - x)**2 + (iy-y)**2
      r = int(math.sqrt(r))
      cv.circle(param, (ix, iy), r, (B[0], G[0], R[0]), -1)


def mouseBrush():
  global mode

  img = np.zeros((512, 512, 3), np.uint8)
  cv.namedWindow('paint')
  cv.setMouseCallback('paint', onMouse, param=img)

  while True:
    cv.imshow('paint', img)
    k = cv.waitKey(1)
    if k == 27:
      break
    elif k == ord('m'):
      mode = not mode

  cv.destroyAllWindows()

mouseBrush()