import cv2 as cv
import numpy as np

# Main Properties of the Image

img = cv.imread('images/korea.jpg')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thr = cv.threshold(imgray, 180, 255, 0)
contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

maxArea = 0
maxI = 0
for i in range(len(contours)):
  tmp = contours[i]
  tmpArea = cv.contourArea(tmp)
  if tmpArea > maxArea and tmpArea < 100000:
    maxI = i
    maxArea = tmpArea

# print(maxArea)
cnt = contours[maxI]
cv.drawContours(img, [cnt], 0, (0, 0, 255), 1)

def props():
  # Aspect Ratio
  x, y, w, h = cv.boundingRect(cnt)
  aspect_ratio = float(w)/h

  # Extent
  area = cv.contourArea(cnt)
  # x, y, w, h = cv.boundingRect(cnt)
  rect_area = w*h
  extent = float(area)/rect_area

  # Solidity
  # area = cv.contourArea(cnt)
  hull = cv.convexHull(cnt)
  hull_area = cv.contourArea(hull)
  solidity = float(area)/hull_area

  # Equivalent Diameter
  # area = cv.contourArea(cnt)
  equivalent_diameter = np.sqrt(4*area/np.pi) # pi*(ED/2)^2 = area
  radius = int(equivalent_diameter/2)

  # Orientation
  ellipse = cv.fitEllipse(cnt) # ellipse = [(x, y), (MajorAxis, MinorAxis), angle]
  orientation = ellipse[2]

  # Mask & Pixel Points
  mask = np.zeros(imgray.shape, np.uint8)
  cv.drawContours(mask, [cnt], 0, 255, -1)
  pixels = cv.findNonZero(mask) # --> all position of the pixel points contained in a contour

  # Mean Color/Mean Intensity
  # mask = np.zeros(imgray.shape, np.uint8)
  mean_value = cv.mean(img, mask=mask)

  mmt = cv.moments(cnt)
  cx = int(mmt['m10']/mmt['m00'])
  cy = int(mmt['m01']/mmt['m00'])


  print('Aspect Ratio:\t%.3f' %aspect_ratio)
  print('Extent:\t%.3f' %extent)
  print('Solidity:\t%.3f' %solidity)
  print('Orientation:\t%.3f' %orientation)

  cv.circle(img, (cx, cy), 3, (0, 0, 255), -1)
  cv.circle(img, (cx, cy), radius, (0, 0, 255), 2)
  cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
  cv.ellipse(img, ellipse, (50, 50, 50), 2)

  cv.imshow('Korea Fitures', img)
  cv.waitKey(0)
  cv.destroyAllWindows()

def extremePoints():
  leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
  rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
  topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
  bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
  cv.circle(img, leftmost, 4, (0, 80, 0), -1)
  cv.circle(img, rightmost, 4, (0, 80, 0), -1)
  cv.circle(img, topmost, 4, (0, 80, 0), -1)
  cv.circle(img, bottommost, 4, (0, 80, 0), -1)

  cv.imshow('extreme points', img)
  cv.waitKey(0)
  cv.destroyAllWindows()

# props()
extremePoints()