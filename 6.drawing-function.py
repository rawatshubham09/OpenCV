import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def drawingFigure():
    imgPath = "OpenCV\\demoImage\\5.jpg"
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    
    #plt.imshow(imgRGB)
    #plt.title('Original Image')
    #plt.show()
    

    red = (0, 0, 255)
    
    # Stright Line
    cv.line(img, (124,45),(170, 45), red, 3)

    #Boundry
    r,c,d = img.shape
    offset = 20
    cv.rectangle(img, (offset,offset), (c-offset,r-offset), red, 5)

    #Circle
    cv.circle(img,(95,182),30,red,2)

    #ellipse
    cv.ellipse(img,(130,270),(20,50),130,0,360,red,2)

    #pologon
    pts = np.array([[318,155],[205,221],[168,130]])

    cv.polylines(img,[pts],True,red,2)

    #text
    cv.putText(img, "ENJOY", (250,100),cv.FONT_HERSHEY_SCRIPT_SIMPLEX,2,red,2,
               cv.LINE_AA)
    
    cv.imshow("Img",img)
    cv.waitKey(0)


if __name__ == "__main__":
    drawingFigure()