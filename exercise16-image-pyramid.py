import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Gaussian Pyramid
# cv.pyrDown(src) : Downsampling -> make a higher level image (smaller size image)
# cv.pyrUp(src) : Upsampling -> make a lower level image

def pyramid():
  img = cv.imread('images/MET_cat_small.jpg', cv.IMREAD_GRAYSCALE)
  tmp = img.copy()

  win_titles = ['org', 'lv1', 'lv2', 'lv3']
  g_down = []
  g_down.append(tmp)

  for i in range(3):
    tmp1 = cv.pyrDown(tmp)
    g_down.append(tmp1)
    tmp = tmp1

  for i in range(4):
    cv.imshow(win_titles[i], g_down[i])

  cv.waitKey(0)
  cv.destroyAllWindows()

# Laplacian Pyramid 
# Upscale a downscaled image and subtract to the original image --> can detect edges

def laplacianPyr():
  img = cv.imread('images/MET_cat_small.jpg')
  tmp = img.copy()

  win_titles = ['org', 'lv1', 'lv2', 'lv3']
  g_down = []
  g_up = []
  img_shape = []

  g_down.append(tmp)
  img_shape.append(tmp.shape)

  for i in range(3):
    tmp1 = cv.pyrDown(tmp)
    g_down.append(tmp1)
    img_shape.append(tmp1.shape)
    tmp = tmp1

  for i in range(3):
    tmp = g_down[i+1]
    tmp1 = cv.pyrUp(tmp)
    tmp = cv.resize(tmp1, dsize=(img_shape[i][1], img_shape[i][0]), interpolation=cv.INTER_CUBIC)
    g_up.append(tmp)

  for i in range(3):
    tmp = cv.subtract(g_down[i], g_up[i])
    cv.imshow(win_titles[i], tmp)

  cv.waitKey(0)
  cv.destroyAllWindows()


# pyramid()
laplacianPyr()