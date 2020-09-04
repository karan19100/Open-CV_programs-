
import cv2
import numpy as np
from matplotlib import pyplot as plt

print("the program is run and executed by karan shah 1812054-A3")
img = cv2.imread("tp2.png", 0)
ret, th1 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 55, 7)
titles = ['orginal Image', 'global thresholding',
          'Adaptive Mean thresholding', 'Adaptive Gaussian thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
