import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def readImage():
    img = cv.imread("OpenCV\\demoImage\\1.jpg",1)
    print(type(img))
    cv.imshow("img",img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    readImage()
