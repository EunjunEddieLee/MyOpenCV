import cv2 as cv
import numpy as np

img = cv.imread('images/MET_cat_small.jpg')
# img1 = np.copy(img)
# img2 = np.copy(img)
h, w = img.shape[:2]
# M_rotate1 = cv.getRotationMatrix2D((w/2, h/2), 45, 0.6) # matrix for rotation
# img = cv.warpAffine(img, M_rotate1, (w, h)) # array coordinate : (h, w) <-> graphics coordinate : (x, y) : w = x, h = y

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

# Convex Hull
def convexHull():

  check = cv.isContourConvex(cnt)

  if not check:
    hull = cv.convexHull(cnt)
    cv.drawContours(img, [hull], 0, (255, 0, 0), 2)

  cv.imshow('contour + hull', img)

  cv.waitKey(0)
  cv.destroyAllWindows()

def rect():
  x, y, w, h = cv.boundingRect(cnt)
  cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

  rect = cv.minAreaRect(cnt)
  box = cv.boxPoints(rect)
  box = np.int_(box)

  cv.drawContours(img, [box], 0, (255, 0, 0), 3)

  cv.imshow('rectangle', img)
  cv.waitKey(0)
  cv.destroyAllWindows()

def ellipse():
  rows, cols = img.shape[:2]

  (x, y), r = cv.minEnclosingCircle(cnt)
  center = (int(x), int(y))
  r = int(r)

  cv.circle(img, center, r, (255, 0, 0), 2)

  ellipse = cv.fitEllipse(cnt)
  cv.ellipse(img, ellipse, (0, 255, 0), 2)

  [vx, vy, x, y] = cv.fitLine(cnt, cv.DIST_L2, 0, 0.01, 0.01)
  l = int((-y*vx/vy) + x)
  r = int(((rows-y)*vx/vy) + x)

  cv.line(img, (l, 0), (r, rows), (255, 0, 255), 2)

  cv.imshow('fitting', img)
  cv.waitKey(0)
  cv.destroyAllWindows()

# convexHull()
# rect()
ellipse()