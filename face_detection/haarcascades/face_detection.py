import cv2 as cv
import numpy as np

# Read the original image from the file 'cat.jpg'
img = cv.imread('../../Images/Group2.jpg')
cv.imshow('Person', img)

# Convert the original image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Load the Cascade Classifier
haar_cascade = cv.CascadeClassifier('haar_face.xml')
# Detect faces
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)# scaleFactor=1.1, minNeighbors=3

# Print the number of faces detected
print(f'Number of faces detected: {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
  cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

# These method is useful for simple images but if you have more complex images is not the best choice 
# These method is so sensible to images with noise

cv.waitKey(0)