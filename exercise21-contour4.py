import cv2 as cv
import numpy as np


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

# Convexity Defects
def contour():
  hull = cv.convexHull(cnt)
  cv.drawContours(img, [hull], 0, (255, 0, 255), 1)

  hull = cv.convexHull(cnt, returnPoints=False) # only return the points that original contour and convex hull meet
  # draw convexHull
  print(hull)
  for i in range(len(hull)):
    cv.circle(img, (cnt[hull[i][0]][0][0], cnt[hull[i][0]][0][1]), 2, (255, 0, 0), -1)
  defects = cv.convexityDefects(cnt, hull)

  for i in range(defects.shape[0]):
    sp, ep, fp, dist = defects[i, 0]
    start = tuple(cnt[sp][0])
    end = tuple(cnt[ep][0])
    farthest = tuple(cnt[fp][0])

    cv.circle(img, farthest, 2, (0, 255, 0), -1)

  cv.imshow('defects', img)
  cv.waitKey(0)
  cv.destroyAllWindows()

def dist():
  outside = (50, 30)
  inside = (200, 250)

  dist1 = cv.pointPolygonTest(cnt, outside, True) # if dist < 0 --> outside point
  dist2 = cv.pointPolygonTest(cnt, inside, True)

  print('dist from Contour to (%d, %d): %.3f' %(outside[0], outside[1], dist1))
  print('dist from Contour to (%d, %d): %.3f' %(inside[0], inside[1], dist2))

  cv.circle(img, outside, 3, (0, 255, 0), -1)
  cv.circle(img, inside, 3, (255, 0, 255), -1)

  cv.imshow('distances', img)
  cv.waitKey(0)
  cv.destroyAllWindows()


# Matching Shape
# cv.matchShape(cnt1, cnt2, method, parameter)
# method : cv.CONTOURS_MATCH_I1, I2, I3
# -- usually cv.matchShape(cnt1, cnt2, 1, 0.0) --

def matching():
  imgfiles = ['images/match/original.jpg', 'images/match/diff1.jpg', 'images/match/diff2.jpg', 'images/match/diff3.jpg', 'images/match/diff4.jpg']
  wins = map(lambda x: 'img' + str(x), range(5))
  wins = list(wins)
  imgs = []
  contour_list = []

  i = 0
  for imgfile in imgfiles:
    img = cv.imread(imgfile, cv.IMREAD_GRAYSCALE)
    imgs.append(img)

    ret, thr = cv.threshold(img, 127, 255, 0)
    contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    contour_list.append(contours[0])
    i += 1

  for i in range(4):
    cv.imshow(wins[i+1], imgs[i+1])
    ret = cv.matchShapes(contour_list[0], contour_list[i+1], 1, 0.0)

    print(ret)
  
  cv.waitKey(0)
  cv.destroyAllWindows()

# contour()
dist()
# matching() # example image not ready
