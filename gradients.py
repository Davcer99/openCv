import cv2 as cv
import numpy as np

# Read the original image from the file 'cat.jpg'
img = cv.imread('Images/cat.jpg')
cv.imshow('Cat', img)

# Convert the original image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)  # Sobel operator for x-direction 1 = x, 0 = y
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)  # Sobel operator for y-direction  0 = x, 1 = y
combined_sobel = cv.bitwise_or(sobelx, sobely)  # Combine Sobel x and Sobel y

# Display individual Sobel components and the combined result
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

# Canny edge detection
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)
