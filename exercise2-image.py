import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def showImage():
  imgfile = 'images/MET_cat.jpg'
  img = cv.imread(imgfile, cv.IMREAD_COLOR) # COLOR(1), GRAYSCALE(0), UNCHANGED(-1)

  window_title = 'The Favorite Cat'
  cv.namedWindow(window_title, cv.WINDOW_NORMAL) # WINDOW_AUTOSIZE : fixed window size, WINDOW_NORMAL : can change size
  cv.imshow(window_title, img)

  k = cv.waitKey(0)
  
  if k == 27: # 27 : ESC key
    cv.destroyAllWindows()
  elif k == ord('c'):
    cv.imwrite('images/MET_cat_copy.jpg', img)
    cv.destroyAllWindows()  

# plot images with matplotlib
def plotImage():
  imgfile = 'images/MET_cat.jpg'
  img = cv.imread(imgfile, cv.IMREAD_COLOR) # COLOR(1), GRAYSCALE(0), UNCHANGED(-1)

  window_title = 'The Favorite Cat'

  img_gray = cv.imread(imgfile, cv.IMREAD_GRAYSCALE)

  plt.imshow(img_gray, cmap='gray', interpolation='bicubic')
  plt.xticks([])
  plt.yticks([])
  plt.title(window_title)
  plt.show()

showImage()
# plotImage()