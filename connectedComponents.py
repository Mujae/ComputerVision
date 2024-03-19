# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:57:38 2024

@author: 51452
"""

import cv2 as cv
import sys
import numpy as np
img = np.zeros([19,19])

img[8:16, [2,7,10,16]]=1
img[[7,16], 3:7]=1
img[16,[10,16]]=1
img[2:8, 10]=1
img[7, [11,15]]=1
img[6,12:15]=1
'''
if img is None:
    sys.exit("We find nothing.")
'''
cv.imwrite('connected.png',img)
img=cv.imread('nonnected.png')
img2=cv.resize(img, dsize=(0,0), fx=5, fy=5)
img2*=255

cv.imshow('Binary image', img2)

cv.waitKey()
cv.destroyAllWindows()
