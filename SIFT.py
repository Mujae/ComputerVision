# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:19:50 2024

@author: 51452
"""

import cv2 as cv

img=cv.imread('image/mot_color70.jpg')
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sift=cv.SIFT_create()
# sift=cv.SIFT_create(nfeatures=0, nOctaveLayers=3, contrastThreshold=0.04)
# edgeThreshold=10,sigma=1.0

kp, des=sift.detectAndCompute(gray, None)
gray=cv.drawKeypoints(gray, kp, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('sift', gray)

k=cv.waitKey()
cv.destroyAllWindows()

print(len(kp))