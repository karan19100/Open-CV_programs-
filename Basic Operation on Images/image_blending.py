import cv2
import numpy as np

img1 = cv2.imread('blen_img1.png')
img2 = cv2.imread('blen_img2.png')
dst = cv2.addWeighted(img1, 0.5, img2, 0.5, 0.0)
cv2.imshow('image',img1)
cv2.imshow('image2',img2)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()