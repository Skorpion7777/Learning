import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#for images

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img) #normal file

resized_img = rescaleFrame(img)
cv.imshow('Cat resized', resized_img)

cv.waitKey(0)

#for video

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

#capture set method
#for images, video and live video
#changeRes only works for live video - not on standalone video files!!

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

