import cv2 as cv
import numpy as np

#img = cv.imread("OpenCV//demoImage//6.jpg")
#cv.imshow("Original", img)

blank = np.zeros((400,400), dtype="uint8")

#Rectangle
rectangle = cv.rectangle(blank.copy(), (30,30),(370,370),255,2)

#circle
circle = cv.circle(blank.copy(), (200,200), 50, (255,0,0), 2)

cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)

cv.waitKey(0)