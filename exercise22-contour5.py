import cv2 as cv
import numpy as np

# Contour Hierarchy
#
# if one contour(A) is contained inside the other contour(B), then A is child of B
# if two contours C and D are not contained in each other, than C and D are at the same level

# contours, hierarchy = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# hierarchy = [Next, Previous, First Child, Parent]
#
# Next, Previous : next/previous contour index at the same level. -1 if there is no next/previous contour
# First Child : first child contour index. -1 if there is no child contour
# Parent : parent contour index. -1 if there is no parent contour

# cv.RETR_TREE, LIST, EXTERNAL, CCOMP : how to deal with hierarchy
# 
# RETR_LIST : doesn't consider hierarchy level
# RETR_TREE : consider all relations