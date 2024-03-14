# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:54:58 2024

@author: 51452
"""

import cv2 as cv
import sys

img = cv.imread('./image/girl_laughing.jpg')

if img is None:
    sys.exit('파일 ㄴㄴ')
    
def draw(event, x, y, flags, param):
    global ix, iy
    
    if event == cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img,(ix,iy),(x,y),(0,0,255),2)
        
    cv.imshow('Drawing', img)
    
cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while(True):
    if cv.waitKey(5) == ord('q'):
        cv.destroyAllWindows()
        break