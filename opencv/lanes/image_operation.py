# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:04:44 2019

@author: Piyush
"""
import numpy as np
import cv2

img = cv2.imread('joker.jpg', cv2.IMREAD_COLOR )

px = img[55,55]

img[55, 55 ] = [255,255,255]

print(px)

Roi = img[100:150 , 100:250]

print(Roi)

watch_face = img[37:111 , 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()