import cv2
import numpy as np

img = cv2.imread('number.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, tresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(
    tresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0, 255,), 3)

cnt1 = contours[2]
cnt2 = contours[4]
cnt3 = contours[5]

ret0 = cv2.matchShapes(cnt1, cnt1, 1, 0.0)
ret1 = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
ret2 = cv2.matchShapes(cnt2, cnt3, 1, 0.0)
ret3 = cv2.matchShapes(cnt3, cnt1, 1, 0.0)

print('Matching cnt1 with cnt1: ', ret0)
print('Matching cnt1 with cnt2: ', ret1)
print('Matching cnt2 with cnt3: ', ret2)
print('Matching cnt3 with cnt1: ', ret3)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
