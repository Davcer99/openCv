import cv2 as cv
# Rescaling video and images making them smaller
img = cv.imread('Images/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrmame(frame, scale= 0.75):
  # Images, Videos and Live Video
  width = int(frame.shape[1] * scale)# frame.shape[1] = width
  height = int(frame.shape[0] * scale)# frame.shape[0] = height

  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)


#Rescale a image
resized_image = rescaleFrmame(img)
cv. imshow('Image', resized_image)

#Change the resolution

def changeRes(width, height):
  # Only for live video
  capture.set(3, width)# 3 = width
  capture.set(4, height)# 4 = height

# Rescale a video

# Create a VideoCapture object
capture = cv.VideoCapture('Videos/squirrel.mp4')

while True:
    # Read the next frame from the video
    isTrue, frame = capture.read()

    frame_resized = rescaleFrmame(frame)
  
    # Display the frame
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    cv.imshow()

    # Break the loop if 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the VideoCapture object and close all windows
capture.release()
cv.destroyAllWindows()