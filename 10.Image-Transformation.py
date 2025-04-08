import cv2 as cv
import numpy as np

img = cv.imread("OpenCV//demoImage//2.jpg")

def translate(img, x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# +x --> Right
# +y --> Down

translated = translate(img, 100, 100)
cv.imshow("Translated", translated)

#Rotations
def rotate(img, angle, rotPoint=None):
    (h, w) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (w//2, h//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (w, h)

    return cv.warpAffine(img, rotMat, dimensions)

rotated_img = rotate(img, -45)
cv.imshow("Rotated", rotated_img)

#Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

#Flipping
flipped = cv.flip(img, 0) # 0 --> x-axis, 1 --> y-axis, -1 --> both
cv.imshow("Flipped", flipped)

cv.waitKey(0)