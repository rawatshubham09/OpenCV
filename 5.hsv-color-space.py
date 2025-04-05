import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def hsvColorSegmentation():
    imgPath = "OpenCV\\demoImage\\5.jpg"
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lowerBound = np.array([0,0,50])
    upperBound = np.array([250,100,100])

    mask = cv.inRange(hsv, lowerBound, upperBound)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    cv.imshow("mask",mask)
    cv.waitKey(0)

if __name__ == "__main__":
    hsvColorSegmentation()