# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 23:16:27 2019

@author: Piyush
"""



import cv2
import numpy as np

img1 = cv2.imread('ml.jpg')
img2 = cv2.imread('opencv.png')

#add = img1 + img2 
#add = cv2.add(img1 , img2)

#print(cv2.add(img1,img2))

img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

dst = cv2.addWeighted(img1,0.7,img2_resized , 0.3 ,0)


cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#doing same for two diferent images 
img3 = cv2.imread('joker.png')
img4 = cv2.imread('joker2.png')

img4_resized = cv2.resize(img4, (img3.shape[1], img3.shape[0]))

weighted = cv2.addWeighted(img3 , 0.7 , img4_resized, 0.3 , 0)

cv2.imshow('dst2',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

#creating an rbg to gray  conversion and masking 

img1 = cv2.imread('ml.jpg')
img2 = cv2.imread('opencv.png')


rows , cols , channels = img2.shape
roi = img1[0:rows , 0:cols] 

img2gray = cv2.cvtColor(img2 , cv2.COLOR_BGR2GRAY)
ret , mask = cv2.threshold(img2gray, 220 , 255 , cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi , roi , mask = mask_inv)
img2_fg = cv2.bitwise_and(img2 , img2 , mask = mask)

dst2 = cv2.add(img1_bg, img2_fg )
img1[0: rows , 0:cols] = dst2

#cv2.imshow('mask', mask )
cv2.imshow('res', img1 )
cv2.imshow('mask_inv', mask_inv )
cv2.imshow('img1_bg', img1_bg )
cv2.imshow('img2_bg', img2_fg )
cv2.imshow('dst2', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
