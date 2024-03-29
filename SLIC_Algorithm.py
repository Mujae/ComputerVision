# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:16:40 2024

@author: 51452
"""

import skimage#여긴 RGB순
import numpy as np
import cv2 as cv

img=skimage.data.coffee()
cv.imshow('Coffe image', cv.cvtColor(img,cv.COLOR_RGB2BGR))

slic1 = skimage.segmentation.slic(img, compactness=20, n_segments=600)
sp_img1 = skimage.segmentation.mark_boundaries(img, slic1)
sp_img1 = np.uint8(sp_img1*255.0)

slic2 = skimage.segmentation.slic(img,compactness=40, n_segments=600)
sg_img2=skimage.segmentation.mark_boundaries(img, slic2)
sg_img2 = np.uint8(sg_img2*255.0)

#Compact가 크면 네모 모양 잘 유지
cv.imshow('Super pixels (compact 20)', cv.cvtColor(sp_img1, cv.COLOR_RGB2BGR))
cv.imshow('Super pixels (compact 40)', cv.cvtColor(sg_img2, cv.COLOR_RGB2BGR))

cv.waitKey()
cv.destroyAllWindows()