import numpy as np
import cv2 as cv
import sys

# IMAGE
img = cv.imread("./images/MET_cat.jpg") # imread : load image file

if img is None:
  sys.exit("Could not read the images.")

cv.imshow("Display window", img) # show the image. Display window = showing window tab title

k = cv.waitKey(0) # wait for the Keyboard input

if k == ord("s"):
  cv.imwrite("METCat.png", img) # save image with the written path(+ name)

# --------------------------------

# # CAMERA ACCESS
# cap = cv.VideoCapture(0)

# if not cap.isOpened():
#   print("Cannot open camera")
#   exit()

# while True:
#   ret, frame = cap.read()
#   if not ret:
#     print("Can't receive frame (stream end?). Exiting ...")
#     break

#   gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

#   cv.imshow('frame', gray)
#   if cv.waitKey(1) == ord("q"):
#     break

# cap.release()
# cv.destroyAllWindows()

# --------------------------------

# # VIDEO
# cap = cv.VideoCapture("./videos/goat.mp4")

# while cap.isOpened():
#   ret, frame = cap.read()

#   if not ret:
#     print("Can't receive frame (stream end?). Exiting ...")
#     break
#   gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#   cv.imshow("frame", gray)
#   if cv.waitKey(1) == ord('q'):
#     break

# cap.release()
# cv.destroyAllWindows()

# --------------------------------

# # SAVE VIDEO
# cap = cv.VideoCapture(0)

# fourcc = cv.VideoWriter_fourcc(*'DIVX')
# out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# while cap.isOpened():
#   ret, frame = cap.read()
#   if not ret:
#     print("Can't receive frame (stream end?). Exiting ...")
#     break
#   frame = cv.flip(frame, 0)

#   out.write(frame)

#   cv.imshow('frame', frame)
#   if cv.waitKey(1) == ord("q"):
#     break

# cap.release()
# out.release()
# cv.destroyAllWindows()

# --------------------------------