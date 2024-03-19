# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:44:03 2024

@author: 51452
"""

import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

t,bin_img = cv.threshold(img[:,:,2],0,255, cv.THRESH_BINARY+cv.THRESH_OTSU)
print('오츄 알고리즘이 찾은 최적 임곗값=w', t)

cv.imshow("R channel", img[:,:,2])
cv.imshow("R channel binarization", bin_img)

cv.waitKey()
cv.destroyAllWindows()