# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.imshow('Image display', img)

cv.waitKey()
cv.destroyAllWindows()

type(img)

img.shape

print(img[0,0,0], img[0,0,1], img[0,0,2])