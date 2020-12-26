import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#Paint the image a certain colour

blank[:] = 0,255,0 #r,g,b

cv.imshow('Green', blank)

#certain portion
blank[200:300, 300:400] = 0,0,255
cv.imshow('Green', blank)

#draw a rectangle

cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=2) #fill with thickness=-1
cv.imshow('Rectangle', blank)

cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,0,0), thickness=-1)
cv.imshow('Rectangle 2', blank)

#draw a circle

cv.circle(blank, (250,250), 40, (0,0,255), thickness= 3)
cv.imshow('Circle', blank)

#draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=3)
cv.imshow('Line', blank)

#write text
cv.putText(blank, "Hello World", (225,225), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,0,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)