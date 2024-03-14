# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:22:49 2024

@author: 51452
"""
import numpy as np
import cv2 as cv
import sys

cap = cv.VideoCapture('./video/jeju.mp4')

if not cap.isOpened():
    sys.exit("카메라 연결 실파이")

width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
heigh = cap.get(cv.CAP_PROP_FRAME_HEIGHT)

print('width: %d, height: %d' %(width, heigh))

frames = []

while cap.isOpened():
    ret, video = cap.read()
    
    if not ret:
        sys.exit('프레임 획득에 실패한 어쩌구')
        break
        
    cv.imshow('Vido file', video)
    key = cv.waitKey(10)
    
    if key ==ord('c'):
        frames.append(video)
    elif key==ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()

if len(frames) > 0:
    imgs = frames[0]
    for i in range(1, min(3, len(frames))):
        imgs = np.hstack((imgs, frames[i]))

    cv.imshow('collecting images', imgs)
    
    cv.waitKey()
    cv.destroyAllWindows()