import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass


img = cv2.imread('dhoni.png', 0)
cv2.namedWindow('Edge Image')
cv2.createTrackbar('minVal', 'Edge Image', 100, 500, nothing)
cv2.createTrackbar('maxVal', 'Edge Image', 200, 500, nothing)

while(1):
    minV = cv2.getTrackbarPos('minVal', 'Edge Image')
    maxV = cv2.getTrackbarPos('maxVal', 'Edge Image')
    edge = cv2.Canny(img, minV, maxV)
    cv2.imshow('Edge Image', edge)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
