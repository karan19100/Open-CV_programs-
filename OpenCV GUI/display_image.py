
import cv2
import numpy as np

img = cv2.imread('dhoni.png', 0)
eye = img[155:170, 180:200]
img[0:15, 25:45] = eye
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('dhoni.png', img)
    cv2.destroyAllWindows()
