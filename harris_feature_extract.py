# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:45:20 2024

@author: 51452
"""

import cv2 as cv
import numpy as np

img = np.zeros([10,10], np.float32)
for i in range(2,7):
    img[i,3:(i+2)]=1
    
    
print(img)


ux = np.array([-1,0,1])
uy = ux.transpose()
k = cv.getGaussianKernel(3,1)
g = np.outer(k, k.transpose())

dy = cv.filter2D(img, cv.CV_32F, uy)
dx = cv.filter2D(img, cv.CV_32F, ux)

dyy = dy*dy
dxx = dx*dx
dyx = dy*dx

gdyy = cv.filter2D(dyx, cv.CV_32F, g)
gdxx = cv.filter2D(dxx, cv.CV_32F, g)
gdyx = cv.filter2D(dyx, cv.CV_32F, g)

C = (gdyy*gdxx-gdyx*gdyx)-0.04*(gdyy+gdxx)*(gdyy+gdxx)


for j in range(1, C.shape[0]-1):
    for i in range(1, C.shape[1]-1):
        if C[j,i] >  0.1 and sum(sum(C[j,i]>C[j-1:j+2,i-1:i+2]))==8:
            img[j,i]=9
            
np.set_printoptions(precision=2)#소수점 아래 2자리까지
print(dy)
print(dx)
print(dyy)
print(dxx)
print(dyx)
print(gdyy)
print(gdxx)
print(gdyx)
print(C)
print(img)#최종 이미지

popping = np.zeros([160,160],np.uint8)
for j in range(0, 160):
    for i in range(0,160):
        popping[j,i]=np.uint8((C[j//16,i//16]+0.06)*700)
        
cv.imshow('Image Display2', popping)
cv.waitKey()
cv.destroyAllWindows()
