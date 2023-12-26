import cv2 as cv

# Reading an image
""" img = cv.imread('Images/cat.jpg')
cv.imshow('Cat', img)

cv.waitKey(0)
 """

# Reading a video
capture = cv.VideoCapture('Videos/squirrel.mp4')

while True:
  isTrue, frame = capture.read()
  
  cv.imshow('Video', frame)

  if cv.waitKey(20) & 0xFF == ord('d'):
    break
capture.release()
cv.destroyAllWindows()
