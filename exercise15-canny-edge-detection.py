import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Canny Edge Detection
# 1. Noise Reduction using Gaussian Filter
# 2. Find parts that the gradient is high
# 3. remove pixels that have low gradients
# 4. Thresholding -> remove pixels that is not considered as a part of an edge

def canny():
  img = cv.imread('images/MET_cat_small.jpg', cv.IMREAD_GRAYSCALE)

  edge1 = cv.Canny(img, 50, 200) # 50, 200: min, max value for the thresholding
  edge2 = cv.Canny(img, 100, 200)
  edge3 = cv.Canny(img, 170, 200)

  cv.imshow('original', img)
  cv.imshow('Canny Edge 1', edge1)
  cv.imshow('Canny Edge 2', edge2)
  cv.imshow('Canny Edge 3', edge3)

  cv.waitKey(0)
  cv.destroyAllWindows()

canny()
