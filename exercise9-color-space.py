import cv2 as cv
import numpy as np

# BGR - Blue, Green, Red
# HSV - Hue, Saturation, Value

def hsv():
  blue = np.uint8([[[255, 0, 0]]])
  green = np.uint8([[[0, 255, 0]]])
  red = np.uint8([[[0, 0, 255]]])

  hsv_blue = cv.cvtColor(blue, cv.COLOR_BGR2HSV)
  hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
  hsv_red = cv.cvtColor(red, cv.COLOR_BGR2HSV)

  print('HSV for BLUE', hsv_blue)
  print('HSV for GREEN', hsv_green)
  print('HSV for RED', hsv_red)

# hsv()

def tracking():
  try:
    print('Turning on the webCam')
    cap = cv.VideoCapture(0)
  except:
    print('Failed turning on. Exiting ...')
    return
  
  while True:
    ret, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    min_blue = np.array([100, 50, 50])
    max_blue = np.array([140, 255, 255])
    min_green = np.array([40, 50, 50])
    max_green = np.array([80, 255, 255])
    min_red = np.array([-20, 50, 50])
    max_red = np.array([20, 255, 255])

    mask_blue = cv.inRange(hsv, min_blue, max_blue)
    mask_green = cv.inRange(hsv, min_green, max_green)
    mask_red = cv.inRange(hsv, min_red, max_red)

    mask_all = mask_blue | mask_green | mask_red

    blue_cam = cv.bitwise_and(frame, frame, mask=mask_blue)
    green_cam = cv.bitwise_and(frame, frame, mask=mask_green)
    red_cam = cv.bitwise_and(frame, frame, mask=mask_red)
    all_cam = cv.bitwise_and(frame, frame, mask=mask_all)

    cv.imshow('original', frame)
    cv.imshow('blue', blue_cam)
    cv.imshow('green', green_cam)
    cv.imshow('red', red_cam)
    cv.imshow('all', all_cam)

    k = cv.waitKey(1)
    if k == 27:
      break

  cv.destroyAllWindows()
    
tracking()