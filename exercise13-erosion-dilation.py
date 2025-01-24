import cv2 as cv
import numpy as np


# erosion, dilation
def morph():
  img = cv.imread('images/Binary.jpg', cv.IMREAD_GRAYSCALE)

  kernel = np.ones((3, 3), np.uint8) # kernel for erosion, dilation

  erosion = cv.erode(img, kernel, iterations=1) # iterations=1 : do erosion once (2 -> twice ...)
  dilation = cv.dilate(img, kernel, iterations=1)

  cv.imshow('original', img)
  cv.imshow('erosion', erosion)
  cv.imshow('dilation', dilation)

  cv.waitKey(0)
  cv.destroyAllWindows()

# opening, closing
# opening : erosion -> dilation
# closing : dilation -> erosion
def morphOpeningClosing():
  img1 = cv.imread('images/opening.png', cv.IMREAD_GRAYSCALE)
  img2 = cv.imread('images/closing.png', cv.IMREAD_GRAYSCALE)

  kernel = np.ones((5, 5), np.uint8)

  opening = cv.morphologyEx(img1, cv.MORPH_OPEN, kernel, iterations=2)
  closing = cv.morphologyEx(img2, cv.MORPH_CLOSE, kernel, iterations=2)

  cv.imshow('opening', opening)
  cv.imshow('closing', closing)

  cv.waitKey(0)
  cv.destroyAllWindows()


def others():
  img1 = cv.imread('images/Binary.jpg', cv.IMREAD_GRAYSCALE)
  img2 = cv.imread('images/opening.png', cv.IMREAD_GRAYSCALE)
  img3 = cv.imread('images/closing.png', cv.IMREAD_GRAYSCALE)

  img2 = cv.resize(img2, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
  img3 = cv.resize(img3, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
  cv.imshow('img2 original', img2)
  cv.imshow('img3 original', img3)

  kernel = np.ones((3, 3), np.uint8)

  grad = cv.morphologyEx(img1, cv.MORPH_GRADIENT, kernel)
  tophat = cv.morphologyEx(img2, cv.MORPH_TOPHAT, kernel)
  blackhat = cv.morphologyEx(img3, cv.MORPH_BLACKHAT, kernel)

  cv.imshow('grad', grad)
  cv.imshow('tophat', tophat)
  cv.imshow('blackhat', blackhat)

  cv.waitKey(0)
  cv.destroyAllWindows()


# (+) making kernel matrix
def makeKernel():
  M1 = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
  M2 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (9, 5))
  M3 = cv.getStructuringElement(cv.MORPH_CROSS, (5, 7))

  print(M1, '\n')
  print(M2, '\n')
  print(M3, '\n')


# morph()
# morphOpeningClosing()
# others()

makeKernel()