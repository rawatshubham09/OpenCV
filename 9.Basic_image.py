import cv2 as cv

img = cv.imread("OpenCV//demoImage//2.jpg")

cv.imshow("Original", img)

#Blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

#Edge Cascade
# By using Blur we can reduce noise and improve the edge detection.
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

#Dialet
dilated = cv.dilate(canny, (3, 3), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow("Eroded", eroded)

#Resizing
# we can also use cv.INTER_LINEAR for larger image but cubic give more better result
# for smaller image we can use cv.INTER_AREA
resized = cv.resize(img, (700,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)


cv.waitKey(0)
