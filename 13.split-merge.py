import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("OpenCV//demoImage//5.jpg")
cv.imshow("Original", img)

b,g,r = cv.split(img)

blank = np.zeros(img.shape[:2], dtype="uint8")

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

#for matplotlib
rgb = cv.merge([r, g, b])
plt.imshow(rgb)
plt.title("RGB")
plt.show()


cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

cv.waitKey(0)

