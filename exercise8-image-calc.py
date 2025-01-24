import cv2 as cv
import numpy as np

# image addition --------------------------------
def addImage(imgfile1, imgfile2):
  img1 = cv.imread(imgfile1)
  img2 = cv.imread(imgfile2)

  # cv.imshow('img1', img1)
  # cv.imshow('img2', img2)

  img1 = img1[0:600, 0:800]
  img2 = img2[0:600, 0:800]

  cv.imshow('subimg1', img1)
  cv.imshow('subimg2', img2)

  add_img1 = img1 + img2 # overflow O
  add_img2 = cv.add(img1, img2) # overflow X (fixed to 255)

  cv.imshow('img1+img2', add_img1)
  cv.imshow('cv.add(img1, img2)', add_img2)

  cv.waitKey(0)
  cv.destroyAllWindows()


# image blending (trackbar) -------------------------------------
def onMouse(x):
  pass

def imgBlending(imgfile1, imgfile2):
  img1 = cv.imread(imgfile1)
  img2 = cv.imread(imgfile2)

  # cv.imshow('img1', img1)
  # cv.imshow('img2', img2)

  img1 = img1[0:600, 0:800]
  img2 = img2[0:600, 0:800]

  cv.imshow('subimg1', img1)
  cv.imshow('subimg2', img2)

  cv.namedWindow('ImgPlane')
  cv.createTrackbar('Mixing', 'ImgPlane', 0, 100, onMouse)
  mix = cv.getTrackbarPos('Mixing', 'ImgPlane')

  while True:
    img = cv.addWeighted(img1, float(100 - mix)/100, img2, float(mix)/100, 0)
    cv.imshow('ImgPlane', img)

    k = cv.waitKey(1)
    if k == 27:
      break
    
    mix = cv.getTrackbarPos('Mixing', 'ImgPlane')

  cv.destroyAllWindows()

# image bit operation, masking ------------------------------
def bitOperation(imgfile, addimgfile, size_h, size_w, add_h, add_w):
  # size = size_h, size_w
  img = cv.imread(imgfile)
  roi = img[add_h:add_h+size_h, add_w:add_w+size_w]
  addimg = cv.imread(addimgfile)[0:size_h, 0:size_w]
  

  cv.imshow('addimg', addimg)

  addimg2gray = cv.cvtColor(addimg, cv.COLOR_BGR2GRAY)
  ret, mask = cv.threshold(addimg2gray, 100, 255, cv.THRESH_BINARY)
  mask_inv = cv.bitwise_not(mask)

  cv.imshow('mask', mask)
  cv.imshow('mask_inv', mask_inv)

  logo = cv.bitwise_and(addimg, addimg, mask=mask) # bitwise-and operation just for the area that mask isn't 0
  bg = cv.bitwise_and(roi, roi, mask=mask_inv)

  cv.imshow('logo', logo)
  cv.imshow('bg', bg)

  img[add_h:add_h+size_h, add_w:add_w+size_w] = (logo + bg)

  cv.imshow('added img', img)

  cv.waitKey(0)
  cv.destroyAllWindows()


# addImage('images/MET_cat.jpg', 'images/starry_night.jpg')
# imgBlending('images/MET_cat.jpg', 'images/starry_night.jpg')
bitOperation('images/MET_cat.jpg', 'images/starry_night.jpg', 200, 300, 100, 100)