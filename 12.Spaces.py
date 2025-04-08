import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("OpenCV//demoImage//5.jpg")

cv.imshow("Original", img)

# blank = np.zeros(img.shape, dtype="uint8")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

#BGR to LaB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("Lab", lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()

cv.waitKey(0)