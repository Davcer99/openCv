import cv2 as cv

img = cv.imread('Images/cat.jpg')

cv.imshow('Cat', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # 150 is the threshold
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) # 150 is the threshold
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)# 255 = max value, 11 = block size, 3 = C value, You can play with these two last parameters
cv.imshow('Adaptive Thresholding', adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)# 255 = max value, 11 = block size, 3 = C value, You can play with these two last parameters
cv.imshow('Adaptive Thresholding Inverse', adaptive_thresh_inv)

cv.waitKey(0)