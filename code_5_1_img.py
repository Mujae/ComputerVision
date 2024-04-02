# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:59:50 2024

@author: user
"""

import cv2 as cv
import numpy as np

img = np.zeros([10, 10], np.float32) # 기본이 np.float64 / CV_32F를 쓸 것이라 맞추어줌 
for i in range(2,7):
    img[i,3:(i+2)] = 1

print(img)
