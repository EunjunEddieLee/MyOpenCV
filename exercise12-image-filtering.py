import cv2 as cv
import numpy as np

# averaging filter
def averaging():
  img = cv.imread('images/MET_cat_small.jpg')

  kernel = np.ones((5, 5), np.float32)/25 # kernel matrix for 5x5 averaging filter
  blur = cv.filter2D(img, -1, kernel)

  cv.imshow('original', img)
  cv.imshow('blur', blur)

  cv.waitKey(0)
  cv.destroyAllWindows()

#blurring - Averaging, Gaussian Filtering, Median Filtering, Bilateral Filtering
def onMouse(x):
  pass

def blurring():
  img = cv.imread('images/Manhattan.jpg')

  cv.namedWindow('BlurPane')
  cv.createTrackbar('BLUR_MODE', 'BlurPane', 0, 3, onMouse)
  cv.createTrackbar('BLUR', 'BlurPane', 0, 5, onMouse)

  mode = cv.getTrackbarPos('BLUR_MODE', 'BlurPane')
  val = cv.getTrackbarPos('BLUR', 'BlurPane')

  while True:
    val = val*2 + 1

    try:
      if mode == 0:
        blur = cv.blur(img, (val, val))
      elif mode == 1:
        blur = cv.GaussianBlur(img, (val, val), 0)
      elif mode == 2:
        blur = cv.medianBlur(img, val)
      elif mode == 3:
        blur = cv.bilateralFilter(img, 9, 75, 75)
      else:
        break
      cv.imshow('BlurPane', blur)
    except:
      break
    
    k = cv.waitKey(1)
    if k == 27:
      break
      
    mode = cv.getTrackbarPos('BLUR_MODE', 'BlurPane')
    val = cv.getTrackbarPos('BLUR', 'BlurPane')

  cv.destroyAllWindows()

# averaging()
blurring()