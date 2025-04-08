import cv2 as cv
import numpy as np

img = cv.imread("OpenCV//demoImage//5.jpg")

cv.imshow("Original", img)

blank = np.zeros(img.shape, dtype="uint8")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#blur
blur = cv.GaussianBlur(gray, (5, 5), 0)
cv.imshow("Blur", blur)

#canny
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# #threshold
# _, thresh = cv.threshold(canny, 150, 255, cv.THRESH_BINARY)
# cv.imshow("Threshold", thresh)

#Counture
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, 
                                        cv.CHAIN_APPROX_SIMPLE)

print("Number of contours found: ", len(contours))

cv.drawContours(blank, contours, -1, (0,0,255),1)
cv.imshow("Contours", blank)

cv.waitKey(0)

