import cv2 as cv


def drawCircle(event, x, y, flags, param):
    img = param
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),5,(0,0,255),-1)
def doubleClickDrawing():
    imgPath = "OpenCV\\demoImage\\9.jpg"
    img = cv.imread(imgPath)

    cv.namedWindow("Drawing App")
    cv.setMouseCallback("Drawing App" ,drawCircle,img)

    while True:
        cv.imshow("Drawing App", img)
        if cv.waitKey(1) == ord('q'):
            break

class DrawingApp:
    def __init__(self,imagePath):
        self.imagePath = imagePath
        self.startX,self.startY = 0,0
        self.isDrawing = False

    def drawLine(self, event, x,y, flag, param):
        img = param
        if event == cv.EVENT_LBUTTONDOWN:
            self.isDrawing = True
            self.startX, self.startY = x,y
        elif event == cv.EVENT_MOUSEMOVE and self.isDrawing:
            cv.line(img,(self.startX,self.startY),(x,y),(255,0,255),2)
        elif event == cv.EVENT_LBUTTONUP:
            self.isDrawing = False
            cv.line(img,(self.startX,self.startY),(x,y),(255,0,255),2)
    
    def run(self):
        img = cv.imread(self.imagePath)
        cv.namedWindow("Drawing App")
        cv.setMouseCallback("Drawing App" ,self.drawLine,img)

        while True:
            cv.imshow("Drawing App", img)
            if cv.waitKey(1) == ord('q'):
                break
    
def holdAndDrawing():
    imgPath = "OpenCV\\demoImage\\9.jpg"
    app = DrawingApp(imgPath)
    app.run()

if __name__ == "__main__":
    #doubleClickDrawing()
    holdAndDrawing()