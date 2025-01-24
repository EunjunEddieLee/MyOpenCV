import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Finding edges of the image by using gradient

# cv.Sobel(src, ddepth, dx, dy, ksize)

def grad():
  img = cv.imread('images/keyboard_edge.jpg', cv.IMREAD_GRAYSCALE)

  laplacian = cv.Laplacian(img, cv.CV_64F)
  sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3) # ddepth = CV_64F : data type of the image pixel value
  sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3) # if ddepth = CV_8U (unsigned), it can be out of working for some edge conditions (cannot detect the negative change)

  plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
  plt.title('original'), plt.xticks([]), plt.yticks([])

  plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
  plt.title('Laplacian'), plt.xticks([]), plt.yticks([]) # Sobel X + Sobel Y

  plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
  plt.title('Sobel X'), plt.xticks([]), plt.yticks([]) # vertical edges can be detected easily

  plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
  plt.title('Sobel Y'), plt.xticks([]), plt.yticks([]) # horizontal edges can be detected easily

  plt.show()
  
grad()