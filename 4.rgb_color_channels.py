import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def pureColor():
    zeros = np.zeros((100,100))
    ones = np.ones((100,100))
    bImg = cv.merge((zeros,zeros,255*ones))
    rImg = cv.merge((255*ones,zeros,zeros))
    gImg = cv.merge((zeros,255*ones,zeros))
    BImg = cv.merge((zeros,zeros,zeros))
    wImg = cv.merge((255*ones,255*ones,255*ones))
    greyImg = cv.merge((152*ones,zeros,152.5*ones))



    plt.figure()
    plt.subplot(231)
    plt.imshow(bImg)
    plt.title('Blue')

    plt.subplot(232)
    plt.imshow(rImg)
    plt.title('Red')

    plt.subplot(233)
    plt.imshow(gImg)
    plt.title('Green')

    plt.subplot(234)
    plt.imshow(wImg)
    plt.title('White')

    plt.subplot(235)
    plt.imshow(BImg)
    plt.title('Black')

    plt.subplot(236)
    plt.imshow(greyImg)
    plt.title('Pink')

    plt.show()

def bgrChannelGrayscale():
    imgPath = "OpenCV\\demoImage\\5.jpg"
    img = cv.imread(imgPath)
    b, g, r = cv.split(img)

    plt.figure()
    plt.subplot(131)
    plt.imshow(b, cmap='gray')
    plt.title('Blue channel')

    plt.subplot(132)
    plt.imshow(g, cmap='gray')
    plt.title('Green channel')

    plt.subplot(133)
    plt.imshow(r, cmap='gray')
    plt.title('Red channel')

    plt.show()

def bgrChannelColor():
    imgPath = "OpenCV\\demoImage\\5.jpg"
    img = cv.imread(imgPath)
    b, g, r = cv.split(img)

    zeros = np.zeros_like(b)
    bImg = cv.merge((zeros, zeros,b))
    gImg = cv.merge((zeros, g, zeros))
    rImg = cv.merge((r, zeros, zeros))

    plt.figure()
    plt.subplot(131)
    plt.imshow(bImg)
    plt.title('Blue channel')

    plt.subplot(132)
    plt.imshow(gImg)
    plt.title('Green channel')

    plt.subplot(133)
    plt.imshow(rImg)
    plt.title('Red channel')

    plt.show()



if __name__ == '__main__':
    #pureColor()
    #bgrChannelGrayscale()
    bgrChannelColor()
