import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT) #increase blur with e.g. (7,7)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)
canny = cv.Canny(blur, 125, 175) #get rid of some edges by applying blur
cv.imshow('Canny Edges Blur', canny)

#dialating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

#eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#resize
resized = cv.resize(img, (500,500), interpolation= cv.INTER_AREA) #INTER_CUBIC if we scale bigger
cv.imshow('Resized', resized)

#cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)