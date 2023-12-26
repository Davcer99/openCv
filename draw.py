import cv2 as cv
import numpy as np

blank = np.zeros((500, 500,3), dtype = 'uint8') # 3 = number of color channels
cv.imshow('Blank', blank)

img = cv.imread('Images/cat.jpg')
cv.imshow('Cat', img)

# 1. Paint the image a certain color
""" blank[:] = 0,255,0
cv.imshow('Green', blank) """

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness = 2)# thickness = -1 fills the rectangle
cv.imshow('Rectangle', blank)

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3)# thickness = -1 fills the circle
cv.imshow('Circle', blank)

# 4. Draw a Line
cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, "Hello World", (200, 250), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)