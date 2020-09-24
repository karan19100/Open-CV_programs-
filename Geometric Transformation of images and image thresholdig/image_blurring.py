import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('tp2.png')

# three type of image blurring / image smoothing 

# 1. Averaging
blur = cv2.blur(img,(5,5))

# 2. Gaussian Filtering
#blur = cv2.GaussianBlur(img,(5,5),0)

# 3. Median Filtering
#median = cv2.medianBlur(img,5)

# 4. Bilateral Filtering
#blur = cv2.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

# for all 
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')

#only  for median
#plt.subplot(122),plt.imshow(median),plt.title('Blurred')

plt.xticks([]), plt.yticks([])
plt.show()
