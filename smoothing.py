import cv2 as cv

img = cv.imread('Images/cat.jpg')
cv.imshow('Cat', img)

#Averaging
average = cv.blur(img, (7,7))# increasing the kernel size will blur more like (9,9)
cv.imshow('Average Blur', average)

# Gaussian
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median
median = cv.medianBlur(img, 3)# increasing the kernel size will blur more like 7
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)# 10 = diameter, 35 = sigma color, 25 = sigma space
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0) 