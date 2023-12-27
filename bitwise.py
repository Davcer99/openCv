import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, thickness=-1)

circle = cv.circle(blank.copy(), (200,200), 200, 255, thickness=-1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitwise AND --> returns the intersection of the two images
bitwase_and = cv.bitwise_and(rectangle, circle) 
cv.imshow('Bitwise AND', bitwase_and)

# Bitwise OR --> returns the union of the two images
bitwase_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwase_or)

# Bitwise XOR --> returns the difference of the two images
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# Bitwise NOT --> returns the inverse of the image
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)

cv.waitKey(0)