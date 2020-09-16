import numpy as np
import cv2 as cv

img = cv.imread('tp.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(
    thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
img = cv.drawContours(img, contours, -1, (0, 255, 0), 3)
cv.imshow("output", img)
cv.waitKey(0)
cnt = contours[0]
x, y, w, h = cv.boundingRect(cnt)
aspect_ratio = float(w)/h
print(aspect_ratio)
area = cv.contourArea(cnt)
x, y, w, h = cv.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area
print(extent)
area = cv.contourArea(cnt)
hull = cv.convexHull(cnt)
hull_area = cv.contourArea(hull)
solidity = float(area)/hull_area
print(solidity)
area = cv.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)
print(equi_diameter)
mask = np.zeros(imgray.shape, np.uint8)
cv.drawContours(mask, [cnt], 0, 255, -1)
pixelpoints = np.transpose(np.nonzero(mask))
print(pixelpoints)
