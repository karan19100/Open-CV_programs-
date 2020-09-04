import cv2
import numpy as np
from matplotlib import pyplot as plt

print("the program is run and executed by karan shah 1812054-A3")
img = cv2.imread("apple.png", 0)
ret, thresh1 = cv2.threshold(img, 145, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 145, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 145, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 145, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 145, 255, cv2.THRESH_TOZERO_INV)

titles = ['orginal Image', 'binary',
          'binary_inv', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
