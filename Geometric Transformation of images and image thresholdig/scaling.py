
import cv2
import numpy as np
img = cv2.imread('dhoni.png')
res1 = cv2.resize(img, None, fx=1, fy=2, interpolation=cv2.INTER_AREA)
res2 = cv2.resize(img, None, fx=2, fy=1, interpolation=cv2.INTER_CUBIC)
res3 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
cv2.imshow('AREA', res1)
cv2.imshow('CUBIC', res2)
cv2.imshow('LINEAR', res3)
cv2.imshow('original.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
