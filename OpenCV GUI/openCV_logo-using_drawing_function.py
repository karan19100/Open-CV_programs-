
import numpy as np
import cv2

img = np.ones((256,256,3),np.float32)
cv2.circle(img,(127,44),45,(0,0,255),-1)
cv2.circle(img,(127,44),15,(255,255,255),-1)
cv2.circle(img,(74,134),45,(0,255,0),-1)
cv2.circle(img,(74,134),15,(255,255,255),-1)
pts = np.array([[127,44],[74,134],[179,134]],np.int32)
cv2.fillPoly(img,[pts],(255,255,255))
cv2.circle(img,(179,134),45,(255,0,0),-1)
cv2.circle(img,(179,134),15,(255,255,255),-1)
pts2 = np.array([[179,134],[153,89],[205,89]])
cv2.fillPoly(img, [pts2],(255,255,255))
cv2.imshow('image',img)
cv2.imwrite('open_cv_logo.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()