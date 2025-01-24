import cv2 as cv
import numpy as np

img = cv.imread('./images/starry_night.jpg')

# # print informations
# px = img[340, 200] # color of a pixel at (340, 200)
# print('BGR(img[x, y]): ', px)

# B = img.item(340, 200, 0)
# G = img.item(340, 200, 1)
# R = img.item(340, 200, 2)
# BGR = [B, G, R]
# print('BGR(img.item(x, y, i)): ', BGR)

# print('(height, width, color channel #): ', img.shape)
# print('image size: ', img.size)
# print('data type: ', img.dtype)


# # change ROI
# cv.imshow('original', img)

# subimg = img[300:400, 350:750] # 300~400 row, 350~750 col
# cv.imshow('cutting', subimg)

# img[300:400, 0:400] = subimg

# print(img.shape)
# print(subimg.shape)

# cv.imshow('modified', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# split color channels
b, g, r = cv.split(img)
# print(img[100, 100])
# print(b[100, 100], g[100, 100], r[100, 100])

# cv.imshow('blue channel', b)
# cv.imshow('green channel', g)
# cv.imshow('red channel', r)

merged_img = cv.merge((b, g, r))
cv.imshow('merged', merged_img)

cv.waitKey(0)
cv.destroyAllWindows()