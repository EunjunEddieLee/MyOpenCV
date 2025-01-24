import cv2 as cv
import numpy as np

imgfile = 'images/MET_cat_small.jpg'

# resize ----------------------

def resizing():
  img = cv.imread(imgfile)
  h, w = img.shape[:2]
  img2 = cv.resize(img, None, fx=0.5, fy=1, interpolation=cv.INTER_AREA)
  img3 = cv.resize(img, None, fx=1, fy=0.5, interpolation=cv.INTER_AREA)
  img4 = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)

  cv.imshow('original', img)
  cv.imshow('fx=0.5', img2)
  cv.imshow('fy=0.5', img3)
  cv.imshow('fx=0.5 fy=0.5', img4)

  cv.waitKey(0)
  cv.destroyAllWindows()

# shift, rotate ----------------------

def transformShiftRotate():
  img = cv.imread(imgfile)
  h, w = img.shape[:2]

  M_shift = np.float32([[1, 0, 100], [0, 1, 50]]) # matrix for transformation 'x += 100, y += 50'
  M_rotate1 = cv.getRotationMatrix2D((w/2, h/2), 45, 1) # matrix for rotation
  M_rotate2 = cv.getRotationMatrix2D((w/2, h/2), 90, 1)
  
  img2 = cv.warpAffine(img, M_shift, (w, h)) # array coordinate : (h, w) <-> graphics coordinate : (x, y) : w = x, h = y
  img3 = cv.warpAffine(img, M_rotate1, (w, h))
  img4 = cv.warpAffine(img, M_rotate2, (w, h))
  
  cv.imshow('shifted', img2)
  cv.imshow('rotated-45', img3)
  cv.imshow('rotated-90', img4)

  cv.waitKey(0)
  cv.destroyAllWindows()

# Affine/Perspective Transform ----------------

def transformAffinePerspective():
  img = cv.imread(imgfile)
  h, w = img.shape[:2]

  pts3_1 = np.float32([[50, 50], [200, 50], [20, 200]])
  pts3_2 = np.float32([[10, 100], [200, 50], [100, 250]])
  M_at = cv.getAffineTransform(pts3_1, pts3_2) # matrix that affine transform pts1 to pts2 
                                           # [50, 50] -> [10, 100], [200, 50] -> [200, 50], [20, 200] -> [100, 250]
  img5 = cv.warpAffine(img, M_at, (w, h))
  cv.imshow('affine transform', img5)

  pts4_1 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
  pts4_2 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
  M_pt = cv.getPerspectiveTransform(pts4_1, pts4_2)
  img6 = cv.warpPerspective(img, M_pt, (w, h)) # warpAffine : M = 2x3 matrix, warpPerpective : M = 3x3 matrix
  cv.imshow('perspective transform', img6)

  cv.waitKey(0)
  cv.destroyAllWindows()


resizing()
transformShiftRotate()
transformAffinePerspective()