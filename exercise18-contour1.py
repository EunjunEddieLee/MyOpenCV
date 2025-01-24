import cv2 as cv
import numpy as np

# area, perimeter(rounded length of a contour), centeroid

# Image Moments -> used to calculate centeroid, area, etc.
# Spatial Moments / Central Moments / Central Normalized Moments
# cv.moments(array) - array : Nx1 or 1xN numpy array

def moments():
  img = cv.imread('images/MET_cat_small.jpg')
  imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

  ret, thr = cv.threshold(imgray, 127, 255, 0)
  contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

  contour = contours[0]

  mmt = cv.moments(contour)

  for key, val in mmt.items():
    print('%s: \t%.5f' %(key, val))

  # calculating centeroid axis
  cx = int(mmt['m10']/mmt['m00'])
  cy = int(mmt['m01']/mmt['m00'])

  print(cx, cy)


def contour():
  img = cv.imread('images/MET_cat_small.jpg')
  imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

  ret, thr = cv.threshold(imgray, 127, 255, 0)
  contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

  maxArea = 0
  maxI = 0
  for i in range(len(contours)):
    tmp = contours[i]
    tmpArea = cv.contourArea(tmp)
    if tmpArea > maxArea and tmpArea < 250000:
      maxI = i
      maxArea = tmpArea

  maxCnt = contours[maxI]
  perimeter = cv.arcLength(maxCnt, True)

  cv.drawContours(img, [maxCnt], 0, (0, 0, 255), 2)

  print('contour area: ', maxArea)
  print('contour length: ', perimeter)

  cv.imshow('threshold', thr)
  cv.imshow('contour', img)
  cv.waitKey(0)
  cv.destroyAllWindows()

# Contour Approximation
# change the contour into new simple contour which has less vertices

def approximation():
  img = cv.imread('images/MET_cat_small.jpg')
  img1 = np.copy(img)
  img2 = np.copy(img)
  imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

  ret, thr = cv.threshold(imgray, 127, 255, 0)
  contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

  maxArea = 0
  maxI = 0
  for i in range(len(contours)):
    tmp = contours[i]
    tmpArea = cv.contourArea(tmp)
    if tmpArea > maxArea and tmpArea < 250000:
      maxI = i
      maxArea = tmpArea

  cnt = contours[maxI]
  cv.drawContours(img, [cnt], 0, (0, 0, 255), 2)

  epsilon1 = 0.005*cv.arcLength(cnt, True)
  epsilon2 = 0.02*cv.arcLength(cnt, True)

  approx1 = cv.approxPolyDP(cnt, epsilon1, True)
  approx2 = cv.approxPolyDP(cnt, epsilon2, True)

  cv.drawContours(img1, [approx1], 0, (0, 255, 0), 2)
  cv.drawContours(img2, [approx2], 0, (255, 0, 0), 2)

  cv.imshow('contour', img)
  cv.imshow('Approx1', img1)
  cv.imshow('Approx2', img2)

  cv.waitKey(0)
  cv.destroyAllWindows()


# moments()
# contour()
approximation()