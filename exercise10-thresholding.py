import cv2 as cv
import numpy as np

# Global Thresholding ---------------------------------------------

# cv.threshold(img, threshold_value, value, flag)
# -->
# img : should be a grayscale image
# if the value of a pixel of the img is greater/less than threshold_value, then that pixel's value changes according to the flag
# flag : cv.THRESH_BINARY, BINARY_INV, TRUNC, TOZERO, TOZERO_INV

def globalThresholding():
  img = cv.imread('images/starry_night.jpg', cv.IMREAD_GRAYSCALE)

  ret, thr1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
  ret, thr2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
  ret, thr3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
  ret, thr4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
  ret, thr5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

  cv.imshow('original', img)
  cv.imshow('binary', thr1)
  cv.imshow('binary inv', thr2)
  cv.imshow('trunc', thr3)
  cv.imshow('tozero', thr4)
  cv.imshow('tozero inv', thr5)

  cv.waitKey(0)
  cv.destroyAllWindows()

# Adaptive Thresholding ---------------------------------------------

# cv2.adaptiveThreshold(img, value, adaptiveMethod, thresholdType, blocksize, C)
# calculate new threshold value for each small(according to the blocksize) area of the image and adapt.

# adaptiveMethod : cv.ADAPTIVE_THRESH_MEAN_C, GOUSSIAN_C
# blocksize : should be the odd #


def adaptiveThresholding():
  img = cv.imread('images/starry_night.jpg', cv.IMREAD_GRAYSCALE)

  ret, thr1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
  thr2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
  thr3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

  cv.imshow('original', img)
  cv.imshow('binary', thr1)
  cv.imshow('adaptive mean binary', thr2)
  cv.imshow('adaptive Gaussian binary', thr3)

  cv.waitKey(0)
  cv.destroyAllWindows()

# Otsu's Binarization ---------------------------------------------

import matplotlib.pyplot as plt

def otsuBi():
  img = cv.imread('images/noisy_grayscale.png', cv.IMREAD_GRAYSCALE)

  ret, thr1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
  ret, thr2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

  blur = cv.GaussianBlur(img, (5, 5), 0)
  ret, thr3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

  titles = ['original noisy', 'Histogram', 'G-Thresholding',
            'original noisy', 'Histogram', 'Otsu Thresholding',
            'Gaussian-filtered', 'Histogram', 'Otsu Thresholding']
  images = [img, 0, thr1, img, 0, thr2, blur, 0, thr3]

  for i in range(3):
    plt.subplot(3, 3, i*3+1), plt.imshow(images[i*3], 'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    
    plt.subplot(3, 3, i*3+2), plt.hist(images[i*3].ravel(), 256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, i*3+3), plt.imshow(images[i*3+2], 'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

  plt.show()

# thresholding()
# adaptiveThresholding()
otsuBi()