import cv2 as cv
import os
import matplotlib.pyplot as plt

def readAndWriteSinglePixel():
    imgPath = "OpenCV\\demoImage\\3.jpg"
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    

    person = imgRGB[172:210,201:266]

    dx = 266 - 201
    dy = 210 - 172

    imgRGB[120:120+dy,320:320+dx] = person

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

if __name__ == "__main__":
    readAndWriteSinglePixel()