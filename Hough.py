# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:12:13 2024

@author: 51452
"""

import cv2 as cv

img = cv.imread('./image/apples.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

apples = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 200, param1=150, param2=20,
                         minRAdius=50, maxRadius=120)

for i in apples[0]:
    cv.circle(img, int(i[0]), int(i[1]),int(i[2]),(255,0,0),2)
    
cv.imshow('Apple detection', img)

cv.waitKey()
cv.destroyAllWindows()