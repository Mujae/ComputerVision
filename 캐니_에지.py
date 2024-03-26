# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:45:57 2024

@author: 51452
"""

import cv2 as cv

img = cv.imread('./image/soccer.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


canny1 = cv.Canny(gray,50,10)
canny2 = cv.Canny(gray, 100,200)

cv.imshow('Original',gray)
cv.imshow('Canny1',canny1)
cv.imshow('canny2', canny2)

cv.waitKey()
cv.destroyAllWindows()

 q q q qq   qx