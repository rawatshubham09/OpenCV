import cv2 as cv

# imgPath = "OpenCV\\demoImage\\5.jpg"
# img = cv.imread(imgPath)
# cv.imshow("Image",img)

def reshape(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("OpenCV\\demoImage\\VID-20250215-WA0002.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized = reshape(frame, scale=0.5)

    cv.imshow("Video", frame_resized)
    cv.imshow("Video Original", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

