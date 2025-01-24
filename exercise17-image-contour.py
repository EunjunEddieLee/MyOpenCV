import cv2 as cv
import numpy as np

# Contour
# a line or an edge that connects points that have a same value.

def contour():
  img = cv.imread('images/globe.jpg')
  imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

  ret, thr = cv.threshold(imgray, 127, 255, 0)
  contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

  cv.drawContours(img, contours, -1, (0, 0, 255), 1)
  cv.imshow('thresh', thr)
  cv.imshow('contour', img)

  cv.waitKey(0)
  cv.destroyAllWindows()

contour()