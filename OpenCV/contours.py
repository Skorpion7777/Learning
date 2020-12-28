import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)
'''
Edges are computed as points that are extrema of the image gradient
in the direction of the gradient. 
if it helps, you can think of them as the min and max points in a 
1D function. The point is, edge pixels are a local notion:
they just point out a significant difference between neighbouring pixels.

Contours are often obtained from edges, but they are aimed at being object
contours. Thus, they need to be closed curves. 
You can think of them as boundaries (some Image Processing algorithms 
& librarires call them like that).
When they are obtained from edges, you need to connect the edges 
in order to obtain a closed contour.
'''

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

#reduction in number of contours
canny2 = cv.Canny(blur, 125, 175)
cv.imshow('Canny Blur', canny2)
contours2, hierarchies2 = cv.findContours(canny2, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#alternative: cv.CHAIN_APPROX_NONE
#contours = python list of all the coordinates of contours found in the img
#hirarchies = hirarchical representation of contours

print(f'{len(contours)} contours(s) found!')
print(f'{len(contours2)} contours(s) found!')



cv.waitKey(0)