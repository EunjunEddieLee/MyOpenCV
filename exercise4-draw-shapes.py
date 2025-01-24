import cv2 as cv
import numpy as np

def drawing():
  img = np.zeros((512, 512, 3), np.uint8)

  sp = (0, 0) # start point
  ep = (511, 511) # end point
  c = (255, 0, 0) # color - BGR
  t = 5 # thickness (weight)
  cv.line(img, sp, ep, c, t) # draw a line
  cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3) # sp, ep, c, t
  cv.circle(img, (447, 63), 63, (0, 0, 255), -1) # center, radius, color, thickness(-1 : fill)
  cv.ellipse(img, (256, 256), (100, 50), 45, 0, 270, (255, 255, 0), -1) # center, (a, b), tilted angle, start angle, end angle

  font = cv.FONT_HERSHEY_SIMPLEX
  font_size = 4
  cv.putText(img, 'OpenCV', (10, 440), font, font_size, (255, 255, 255), 2)

  cv.imshow('drawing', img)
  cv.waitKey(0)
  cv.destroyAllWindows()

drawing()